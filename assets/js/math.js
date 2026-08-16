/**
 * Bộ render công thức toán tối giản (một tập con của LaTeX).
 * Không phụ thuộc thư viện ngoài nên chạy được cả khi không có mạng.
 *
 * Hỗ trợ:
 *   \frac{a}{b}      phân số
 *   \sqrt{a}         căn bậc hai
 *   \vec{AB}         vectơ (mũi tên phía trên)
 *   \overline{x}     gạch ngang phía trên
 *   ^{...} hoặc ^2   số mũ
 *   _{...} hoặc _1   chỉ số dưới
 *   \le \ge \ne ...  các ký hiệu thông dụng
 * Ký hiệu đặc biệt: \{, \}, \%, \_, \$, \&, \\
 */

const SYMBOLS = {
  le: '≤', ge: '≥', ne: '≠', pm: '±', mp: '∓',
  times: '×', div: '÷', cdot: '·', deg: '°', circ: '°',
  sin: 'sin', cos: 'cos', tan: 'tan', cot: 'cot', log: 'log',
  infty: '∞', in: '∈', notin: '∉', subset: '⊂', supset: '⊃',
  cup: '∪', cap: '∩', emptyset: '∅', setminus: '∖',
  forall: '∀', exists: '∃', neg: '¬',
  Rightarrow: '⇒', Leftrightarrow: '⇔', rightarrow: '→', to: '→', mapsto: '↦',
  perp: '⊥', parallel: '∥', angle: '∠', triangle: '△',
  alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', Delta: 'Δ',
  theta: 'θ', lambda: 'λ', mu: 'μ', pi: 'π', rho: 'ρ',
  sigma: 'σ', Sigma: 'Σ', tau: 'τ', phi: 'φ', omega: 'ω', Omega: 'Ω',
  approx: '≈', equiv: '≡', propto: '∝', sum: 'Σ', prod: '∏',
  R: 'ℝ', Q: 'ℚ', Z: 'ℤ', N: 'ℕ'
};

const ONE_ARG = {
  sqrt: (inner) => `<span class="m-sqrt"><span class="m-rad">√</span><span class="m-radicand">${inner}</span></span>`,
  vec: (inner) => `<span class="m-vec">${inner}</span>`,
  bar: (inner) => `<span class="m-obar">${inner}</span>`,
  overline: (inner) => `<span class="m-obar">${inner}</span>`,
  hat: (inner) => `<span class="m-obar">${inner}</span>`,
  mathbb: (inner) => inner,
  mathrm: (inner) => inner,
  mathbf: (inner) => inner,
  mathit: (inner) => inner,
  text: (inner) => inner
};

export function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/** Đọc một nhóm {...} bắt đầu tại vị trí i (str[i] phải là '{'). */
function readGroup(str, i) {
  if (str[i] !== '{') return null;
  let depth = 0;
  for (let j = i; j < str.length; j++) {
    if (str[j] === '{') depth++;
    else if (str[j] === '}') {
      depth--;
      if (depth === 0) return { body: str.slice(i + 1, j), next: j + 1 };
    }
  }
  return null;
}

/** Chuyển chuỗi đã escape HTML thành HTML có công thức. */
function transform(src) {
  let out = '';
  let i = 0;

  while (i < src.length) {
    const ch = src[i];

    if (ch === '\\') {
      const nextChar = src[i + 1];
      if (nextChar === '{') { out += '{'; i += 2; continue; }
      if (nextChar === '}') { out += '}'; i += 2; continue; }
      if (nextChar === '%') { out += '%'; i += 2; continue; }
      if (nextChar === '_') { out += '_'; i += 2; continue; }
      if (nextChar === '$') { out += '$'; i += 2; continue; }
      if (nextChar === '&') { out += '&amp;'; i += 2; continue; }
      if (nextChar === '\\') { out += '<br>'; i += 2; continue; }

      const m = /^\\([A-Za-z]+)/.exec(src.slice(i));
      if (m) {
        const name = m[1];
        const afterName = i + m[0].length;

        if (name === 'frac') {
          const g1 = readGroup(src, afterName);
          const g2 = g1 && readGroup(src, g1.next);
          if (g1 && g2) {
            out += `<span class="m-frac"><span class="m-num">${transform(g1.body)}</span>`
                 + `<span class="m-den">${transform(g2.body)}</span></span>`;
            i = g2.next;
            continue;
          }
        } else if (ONE_ARG[name]) {
          const g = readGroup(src, afterName);
          if (g) {
            out += ONE_ARG[name](transform(g.body));
            i = g.next;
            continue;
          }
        } else if (SYMBOLS[name]) {
          out += SYMBOLS[name];
          i = afterName;
          continue;
        }
      }
      out += '\\';
      i++;
      continue;
    }

    if (ch === '^' || ch === '_') {
      const tag = ch === '^' ? 'sup' : 'sub';
      const g = readGroup(src, i + 1);
      if (g) {
        out += `<${tag}>${transform(g.body)}</${tag}>`;
        i = g.next;
        continue;
      }
      const mSub = /^([0-9]+|[A-Za-z])/.exec(src.slice(i + 1));
      if (mSub) {
        out += `<${tag}>${mSub[1]}</${tag}>`;
        i += 1 + mSub[1].length;
        continue;
      }
    }

    out += ch;
    i++;
  }

  return out;
}

/** Render nội dung có công thức thành HTML an toàn (một dòng). */
export function mathHtml(text) {
  if (text === null || text === undefined) return '';
  return transform(escapeHtml(text));
}

/** Như mathHtml nhưng chuyển ký tự xuống dòng thành <br>. */
export function mathBlock(text) {
  return mathHtml(text).replace(/\n/g, '<br>');
}

/** Render thành các đoạn <p> riêng theo dòng trống hoặc mỗi dòng. */
export function mathParagraphs(text) {
  return String(text ?? '')
    .split(/\n{2,}/)
    .filter((p) => p.trim() !== '')
    .map((p) => `<p>${mathHtml(p).replace(/\n/g, '<br>')}</p>`)
    .join('');
}
