import { mathHtml, mathBlock } from '../math.js';
import { isCorrect, formatAnswer, shuffle } from '../grade.js';
import { saveResult, saveLastSetup, getLastSetup } from '../store.js';

const LEVEL_LABEL = { nb: 'Nhận biết', th: 'Thông hiểu', vd: 'Vận dụng' };
const KEYS = ['A', 'B', 'C', 'D'];

/** Phiên làm bài hiện tại (giữ trong bộ nhớ, không lưu localStorage). */
let session = null;

export function hasSession() {
  return session !== null;
}

export function clearSession() {
  session = null;
}

/* ==========================================================================
   1. Trang thiết lập
   ========================================================================== */

export function renderSetup(ctx, query) {
  const { index, sets } = ctx;
  const saved = getLastSetup() || {};
  const preChapter = query.get('chuong');

  const activeSetId = saved.setId && sets[saved.setId] ? saved.setId : index.questionSets[0].id;

  const setCards = index.questionSets.map((s) => `
    <label class="opt-card${s.id === activeSetId ? ' selected' : ''}" data-set-card="${s.id}">
      <input type="radio" name="setId" value="${s.id}" ${s.id === activeSetId ? 'checked' : ''}>
      <span>
        <strong>${s.title}</strong>
        <small>${s.description} — ${sets[s.id].questions.length} câu.</small>
      </span>
    </label>`).join('');

  const chapterRows = index.chapters.map((ch) => {
    const checked = preChapter ? ch.id === preChapter : (saved.chapterIds ? saved.chapterIds.includes(ch.id) : true);
    return `
      <label class="check-row">
        <input type="checkbox" name="chapter" value="${ch.id}" ${checked ? 'checked' : ''}>
        <span>Chương ${ch.roman}. ${mathHtml(ch.title)}</span>
        <span class="count" data-chapter-count="${ch.id}"></span>
      </label>`;
  }).join('');

  const levelRows = index.levels.map((lv) => {
    const checked = saved.levels ? saved.levels.includes(lv.id) : true;
    return `
      <label class="check-row">
        <input type="checkbox" name="level" value="${lv.id}" ${checked ? 'checked' : ''}>
        <span>${lv.label}</span>
        <span class="count" data-level-count="${lv.id}"></span>
      </label>`;
  }).join('');

  const mode = saved.mode || 'instant';

  return `
    <div class="page-head">
      <h1>Luyện tập</h1>
      <p class="sub">Chọn dạng bài, phạm vi kiến thức và số câu, sau đó bắt đầu làm bài.</p>
    </div>

    <form class="setup-grid" id="setup-form">
      <div>
        <div class="field">
          <span class="field-label">Dạng bài tập</span>
          <div class="opt-cards">${setCards}</div>
        </div>

        <div class="field">
          <span class="field-label">Phạm vi kiến thức</span>
          <p class="hint">Có thể chọn nhiều chương để làm đề tổng hợp.</p>
          <div class="check-list">
            ${chapterRows}
          </div>
          <div class="btn-row" style="margin-top:10px">
            <button type="button" class="btn btn-sm" data-select="all">Chọn tất cả</button>
            <button type="button" class="btn btn-sm" data-select="none">Bỏ chọn tất cả</button>
          </div>
        </div>

        <div class="field">
          <span class="field-label">Mức độ</span>
          <div class="check-list">${levelRows}</div>
        </div>

        <div class="field">
          <span class="field-label">Cách làm bài</span>
          <div class="opt-cards">
            <label class="opt-card${mode === 'instant' ? ' selected' : ''}" data-mode-card="instant">
              <input type="radio" name="mode" value="instant" ${mode === 'instant' ? 'checked' : ''}>
              <span>
                <strong>Xem đáp án ngay</strong>
                <small>Chấm và hiện lời giải sau mỗi câu. Phù hợp khi đang học.</small>
              </span>
            </label>
            <label class="opt-card${mode === 'exam' ? ' selected' : ''}" data-mode-card="exam">
              <input type="radio" name="mode" value="exam" ${mode === 'exam' ? 'checked' : ''}>
              <span>
                <strong>Làm hết rồi chấm</strong>
                <small>Chỉ chấm khi nộp bài. Phù hợp khi tự kiểm tra.</small>
              </span>
            </label>
          </div>
        </div>
      </div>

      <aside class="summary-panel">
        <h3>Đề của bạn</h3>
        <dl>
          <dt>Số câu khả dụng</dt><dd data-available>0</dd>
        </dl>
        <div class="field" style="margin-bottom:16px">
          <label class="field-label" for="count-input">Số câu muốn làm</label>
          <input type="number" id="count-input" name="count" min="1" step="1" value="${saved.count || 15}">
        </div>
        <label class="check-row" style="margin-bottom:16px">
          <input type="checkbox" name="shuffle" ${saved.shuffle === false ? '' : 'checked'}>
          <span>Trộn thứ tự câu hỏi</span>
        </label>
        <button class="btn btn-primary" type="submit" data-start>Bắt đầu làm bài</button>
        <p class="hint" style="margin:10px 0 0" data-setup-error></p>
      </aside>
    </form>`;
}

export function bindSetup(ctx, root) {
  const { index, sets } = ctx;
  const form = root.querySelector('#setup-form');
  if (!form) return;

  const availableEl = form.querySelector('[data-available]');
  const countInput = form.querySelector('#count-input');
  const errorEl = form.querySelector('[data-setup-error]');
  const startBtn = form.querySelector('[data-start]');

  const readSelection = () => ({
    setId: form.querySelector('input[name="setId"]:checked')?.value || index.questionSets[0].id,
    chapterIds: [...form.querySelectorAll('input[name="chapter"]:checked')].map((i) => i.value),
    levels: [...form.querySelectorAll('input[name="level"]:checked')].map((i) => i.value),
    mode: form.querySelector('input[name="mode"]:checked')?.value || 'instant',
    shuffle: form.querySelector('input[name="shuffle"]').checked,
    count: Number(countInput.value) || 1
  });

  const pool = (sel) => sets[sel.setId].questions
    .filter((q) => sel.chapterIds.includes(q.chapter))
    .filter((q) => sel.levels.includes(q.level));

  const refresh = () => {
    const sel = readSelection();
    const questions = sets[sel.setId].questions;

    index.chapters.forEach((ch) => {
      const el = form.querySelector(`[data-chapter-count="${ch.id}"]`);
      if (el) el.textContent = `${questions.filter((q) => q.chapter === ch.id).length} câu`;
    });
    index.levels.forEach((lv) => {
      const el = form.querySelector(`[data-level-count="${lv.id}"]`);
      const n = questions.filter((q) => q.level === lv.id && sel.chapterIds.includes(q.chapter)).length;
      if (el) el.textContent = `${n} câu`;
    });

    const total = pool(sel).length;
    availableEl.textContent = `${total} câu`;
    countInput.max = Math.max(total, 1);
    if (Number(countInput.value) > total) countInput.value = total || 1;

    startBtn.disabled = total === 0;
    errorEl.textContent = total === 0 ? 'Không có câu hỏi nào khớp với lựa chọn hiện tại.' : '';

    form.querySelectorAll('[data-set-card]').forEach((card) => {
      card.classList.toggle('selected', card.dataset.setCard === sel.setId);
    });
    form.querySelectorAll('[data-mode-card]').forEach((card) => {
      card.classList.toggle('selected', card.dataset.modeCard === sel.mode);
    });
  };

  form.addEventListener('change', refresh);
  form.addEventListener('input', refresh);

  form.querySelectorAll('[data-select]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const check = btn.dataset.select === 'all';
      form.querySelectorAll('input[name="chapter"]').forEach((i) => { i.checked = check; });
      refresh();
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const sel = readSelection();
    let questions = pool(sel);
    if (!questions.length) return;

    if (sel.shuffle) questions = shuffle(questions);
    questions = questions.slice(0, Math.min(sel.count, questions.length));

    const setMeta = index.questionSets.find((s) => s.id === sel.setId);
    const chapterLabel = sel.chapterIds.length === index.chapters.length
      ? 'Tất cả các chương'
      : sel.chapterIds
        .map((id) => `Chương ${index.chapters.find((c) => c.id === id).roman}`)
        .join(', ');

    saveLastSetup(sel);

    session = {
      setId: sel.setId,
      setTitle: setMeta.title,
      type: setMeta.type,
      chapterLabel,
      mode: sel.mode,
      questions,
      responses: questions.map(() => null),
      checked: questions.map(() => false),
      current: 0,
      finished: false
    };

    location.hash = '#/luyen-tap/lam-bai';
  });

  refresh();
}

/* ==========================================================================
   2. Trang làm bài
   ========================================================================== */

export function renderQuiz() {
  return `
    <div class="quiz-layout">
      <div>
        <div class="quiz-bar">
          <span class="q-pos" data-pos></span>
          <span class="badge" data-set-badge></span>
          <span class="badge" data-scope-badge></span>
          <span class="spacer"></span>
          <button class="btn btn-sm btn-ghost" data-quit type="button">Thoát</button>
        </div>
        <div class="progress"><span data-progress></span></div>
        <div id="q-area"></div>
      </div>
      <aside class="q-nav">
        <h3>Danh sách câu</h3>
        <div class="q-grid" id="q-grid"></div>
        <div class="q-legend">
          <div>Ô tô đậm: đã trả lời</div>
          <div>Viền nổi: câu đang làm</div>
        </div>
        <button class="btn btn-primary btn-sm" style="width:100%;margin-top:14px" data-submit type="button">Nộp bài</button>
      </aside>
    </div>`;
}

function renderChoices(q, response, revealed) {
  return `<div class="choices">
    ${q.choices.map((choice, i) => {
      const classes = ['choice'];
      if (revealed) {
        classes.push('locked');
        if (i === q.answer) classes.push('correct');
        else if (i === response) classes.push('wrong');
      } else if (i === response) {
        classes.push('selected');
      }
      return `<button type="button" class="${classes.join(' ')}" data-choice="${i}" ${revealed ? 'disabled' : ''}>
        <span class="key">${KEYS[i]}</span>
        <span>${mathBlock(choice)}</span>
      </button>`;
    }).join('')}
  </div>`;
}

function renderShortInput(q, response, revealed) {
  return `<div class="answer-input">
    <input type="text" data-answer inputmode="decimal" autocomplete="off"
           placeholder="Nhập đáp số…" value="${response ?? ''}" ${revealed ? 'disabled' : ''}>
    ${q.unit ? `<span class="unit">${mathHtml(q.unit)}</span>` : ''}
    ${revealed ? '' : '<button type="button" class="btn" data-check>Kiểm tra</button>'}
  </div>
  <p class="hint" style="margin:10px 0 0;color:var(--text-muted);font-size:13.5px">
    Đáp án là một số. Có thể nhập 7,5 hoặc 7.5 — cả hai đều được chấp nhận.
  </p>`;
}

function renderFeedback(q, ok) {
  return `<div class="feedback ${ok ? 'ok' : 'bad'}">
    <div class="fb-head">${ok ? 'Chính xác.' : 'Chưa đúng.'} Đáp án: ${mathBlock(formatAnswer(q, session.type))}</div>
    ${q.explanation ? `<div class="fb-body">${mathBlock(q.explanation)}</div>` : ''}
  </div>`;
}

function paintQuiz(root) {
  const s = session;
  const q = s.questions[s.current];
  const response = s.responses[s.current];
  const revealed = s.mode === 'instant' && s.checked[s.current];
  const answeredCount = s.responses.filter((r) => r !== null && r !== '').length;

  root.querySelector('[data-pos]').textContent = `Câu ${s.current + 1} / ${s.questions.length}`;
  root.querySelector('[data-set-badge]').textContent = s.setTitle;
  root.querySelector('[data-scope-badge]').textContent = s.chapterLabel;
  root.querySelector('[data-progress]').style.width = `${(answeredCount / s.questions.length) * 100}%`;

  root.querySelector('#q-area').innerHTML = `
    <div class="q-card">
      <div class="q-meta">
        <span class="badge badge-accent">Câu ${s.current + 1}</span>
        ${q.level ? `<span class="badge">${LEVEL_LABEL[q.level] || q.level}</span>` : ''}
        <span class="badge">${q.id}</span>
      </div>
      <div class="q-text">${mathBlock(q.question)}</div>
      ${s.type === 'multiple-choice'
        ? renderChoices(q, response, revealed)
        : renderShortInput(q, response, revealed)}
      ${revealed ? renderFeedback(q, isCorrect(q, s.type, response)) : ''}
      <div class="quiz-actions">
        <button class="btn" data-prev type="button" ${s.current === 0 ? 'disabled' : ''}>← Câu trước</button>
        <button class="btn" data-next type="button" ${s.current === s.questions.length - 1 ? 'disabled' : ''}>Câu sau →</button>
        <span class="spacer"></span>
        <span style="color:var(--text-muted);font-size:14px">Đã trả lời ${answeredCount}/${s.questions.length}</span>
      </div>
    </div>`;

  root.querySelector('#q-grid').innerHTML = s.questions.map((_, i) => {
    const classes = ['q-dot'];
    const r = s.responses[i];
    if (r !== null && r !== '') classes.push('answered');
    if (s.mode === 'instant' && s.checked[i]) {
      classes.push(isCorrect(s.questions[i], s.type, r) ? 'correct' : 'wrong');
    }
    if (i === s.current) classes.push('current');
    return `<button type="button" class="${classes.join(' ')}" data-goto="${i}">${i + 1}</button>`;
  }).join('');

  bindQuizArea(root);
}

function goTo(root, i) {
  session.current = Math.max(0, Math.min(i, session.questions.length - 1));
  paintQuiz(root);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function bindQuizArea(root) {
  const s = session;

  root.querySelectorAll('[data-choice]').forEach((btn) => {
    btn.addEventListener('click', () => {
      s.responses[s.current] = Number(btn.dataset.choice);
      if (s.mode === 'instant') s.checked[s.current] = true;
      paintQuiz(root);
    });
  });

  const input = root.querySelector('[data-answer]');
  if (input) {
    input.addEventListener('input', () => { s.responses[s.current] = input.value; });
    input.addEventListener('keydown', (e) => {
      if (e.key !== 'Enter') return;
      e.preventDefault();
      if (s.mode === 'instant') {
        if (input.value.trim() !== '') {
          s.responses[s.current] = input.value;
          s.checked[s.current] = true;
          paintQuiz(root);
        }
      } else if (s.current < s.questions.length - 1) {
        goTo(root, s.current + 1);
      }
    });
    if (!s.checked[s.current]) input.focus();
  }

  const checkBtn = root.querySelector('[data-check]');
  if (checkBtn) {
    checkBtn.addEventListener('click', () => {
      if (!input || input.value.trim() === '') return;
      s.responses[s.current] = input.value;
      s.checked[s.current] = true;
      paintQuiz(root);
    });
  }

  root.querySelector('[data-prev]')?.addEventListener('click', () => goTo(root, s.current - 1));
  root.querySelector('[data-next]')?.addEventListener('click', () => goTo(root, s.current + 1));
  root.querySelectorAll('[data-goto]').forEach((btn) => {
    btn.addEventListener('click', () => goTo(root, Number(btn.dataset.goto)));
  });
}

export function bindQuiz(ctx, root) {
  paintQuiz(root);

  root.querySelector('[data-quit]').addEventListener('click', () => {
    if (confirm('Thoát và bỏ bài làm hiện tại?')) {
      clearSession();
      location.hash = '#/luyen-tap';
    }
  });

  root.querySelector('[data-submit]').addEventListener('click', () => {
    const s = session;
    const unanswered = s.responses.filter((r) => r === null || r === '').length;
    if (unanswered > 0 && !confirm(`Còn ${unanswered} câu chưa trả lời. Nộp bài luôn?`)) return;

    s.finished = true;
    s.checked = s.checked.map(() => true);

    const correct = s.questions.filter((q, i) => isCorrect(q, s.type, s.responses[i])).length;
    saveResult({
      setId: s.setId,
      setTitle: s.setTitle,
      chapters: s.chapterLabel,
      total: s.questions.length,
      correct,
      ratio: correct / s.questions.length,
      at: Date.now()
    });

    location.hash = '#/luyen-tap/ket-qua';
  });
}

/* ==========================================================================
   3. Trang kết quả
   ========================================================================== */

export function renderResult() {
  const s = session;
  const results = s.questions.map((q, i) => ({
    q,
    i,
    response: s.responses[i],
    ok: isCorrect(q, s.type, s.responses[i])
  }));
  const correct = results.filter((r) => r.ok).length;
  const pct = Math.round((correct / results.length) * 100);
  const score10 = (correct / results.length * 10).toFixed(2).replace('.', ',');

  return `
    <div class="score-card">
      <div class="eyebrow">${s.setTitle} · ${s.chapterLabel}</div>
      <div class="big">${correct}/${results.length}</div>
      <p class="pct">Đúng ${pct}% — quy về thang điểm 10 là ${score10}</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn-primary" href="#/luyen-tap">Làm đề khác</a>
        <a class="btn" href="#/ly-thuyet">Xem lại lý thuyết</a>
      </div>
    </div>

    <h2>Xem lại từng câu</h2>
    <div class="filter-tabs" data-filters>
      <button class="active" data-filter="all">Tất cả (${results.length})</button>
      <button data-filter="wrong">Câu sai (${results.length - correct})</button>
      <button data-filter="right">Câu đúng (${correct})</button>
    </div>
    <div id="review-list">
      ${results.map((r) => reviewItem(r, s.type)).join('')}
    </div>`;
}

function reviewItem({ q, i, response, ok }, type) {
  const given = type === 'multiple-choice'
    ? (Number.isInteger(response) ? `${KEYS[response]}. ${mathBlock(q.choices[response])}` : '<em>chưa trả lời</em>')
    : (response ? mathBlock(String(response)) : '<em>chưa trả lời</em>');

  return `
    <article class="review-item ${ok ? 'is-right' : 'is-wrong'}" data-state="${ok ? 'right' : 'wrong'}">
      <div class="r-head">
        <span class="num">Câu ${i + 1}</span>
        <span class="badge ${ok ? 'badge-ok' : 'badge-bad'}">${ok ? 'Đúng' : 'Sai'}</span>
        ${q.level ? `<span class="badge">${LEVEL_LABEL[q.level] || q.level}</span>` : ''}
      </div>
      <div class="r-q">${mathBlock(q.question)}</div>
      ${type === 'multiple-choice' ? renderChoices(q, response, true) : ''}
      <p class="r-line"><span class="lbl">Bạn trả lời:</span> ${given}</p>
      <p class="r-line"><span class="lbl">Đáp án:</span> <strong>${mathBlock(formatAnswer(q, type))}</strong></p>
      ${q.explanation ? `<div class="r-exp"><strong>Lời giải.</strong> ${mathBlock(q.explanation)}</div>` : ''}
    </article>`;
}

export function bindResult(ctx, root) {
  const tabs = root.querySelector('[data-filters]');
  if (!tabs) return;

  tabs.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-filter]');
    if (!btn) return;
    tabs.querySelectorAll('button').forEach((b) => b.classList.toggle('active', b === btn));
    const filter = btn.dataset.filter;
    root.querySelectorAll('.review-item').forEach((item) => {
      item.style.display = (filter === 'all' || item.dataset.state === filter) ? '' : 'none';
    });
  });
}
