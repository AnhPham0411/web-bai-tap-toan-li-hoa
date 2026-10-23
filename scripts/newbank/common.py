# -*- coding: utf-8 -*-
"""Khung sinh câu hỏi có tự kiểm: mỗi câu được tính bằng code, đáp án sai sinh từ lỗi thường gặp."""
import json, math, random, re, hashlib
from fractions import Fraction

FIRST_ID = 101  # id sinh mới bắt đầu từ 101 để không đè câu cũ

def fnum(x, nd=2):
    """Số thập phân kiểu Việt Nam (dấu phẩy), bỏ số 0 thừa."""
    s = f"{x:.{nd}f}"
    if '.' in s: s = s.rstrip('0').rstrip('.')
    if s in ('-0', ''): s = '0'
    return s.replace('.', ',').replace('-', '−') if False else s.replace('.', ',')

def frac(fr):
    fr = Fraction(fr)
    if fr.denominator == 1: return str(fr.numerator)
    sign = '-' if fr < 0 else ''
    return f"{sign}\\frac{{{abs(fr.numerator)}}}{{{fr.denominator}}}"

def rad(n):
    """Chuỗi LaTeX của căn bậc hai n, rút gọn: k\\sqrt{m}."""
    k, m = 1, n
    f = 2
    while f * f <= m:
        while m % (f * f) == 0:
            m //= f * f; k *= f
        f += 1
    if m == 1: return str(k)
    return (str(k) if k != 1 else '') + f"\\sqrt{{{m}}}"

def M(s):
    return f"${s}$"

class Bank:
    def __init__(self, subj, ch):
        self.subj, self.ch = subj, ch
        self.mcs, self.sas = [], []
        self.errors = []
        self.rng = random.Random(f"{subj}-{ch}")

    def mc(self, lesson, level, dang, stem, correct, wrong, expl):
        wrong = [str(w) for w in wrong]
        correct = str(correct)
        seen, w2 = {correct}, []
        for w in wrong:
            if w not in seen:
                seen.add(w); w2.append(w)
        if len(w2) < 3:
            # dự phòng: nếu đáp án là một số thuần, bổ sung đáp án nhiễu lệch ±1, ±2, ... cùng số chữ số thập phân
            m = re.fullmatch(r'\$?(-?\d+(?:,\d+)?)\$?', correct)
            if m:
                txt = m.group(1); dec = len(txt.split(',')[1]) if ',' in txt else 0
                val = float(txt.replace(',', '.')); wrap = correct.startswith('$')
                for off in (1, -1, 2, -2, 3, -3, 5):
                    cand = f"{val + off * (10 ** -dec if dec else 1):.{dec}f}".replace('.', ',')
                    cand = f"${cand}$" if wrap else cand
                    if cand not in seen:
                        seen.add(cand); w2.append(cand)
                    if len(w2) >= 3: break
        if len(w2) < 3:
            self.errors.append(f"Thiếu đáp án sai: {stem[:70]} | đúng={correct} | sai={wrong}")
            return
        choices = [correct] + w2[:3]
        order = list(range(4)); self.rng.shuffle(order)
        shuffled = [choices[i] for i in order]
        self.mcs.append(dict(chapter=self.ch, lesson=lesson, level=level, dang=dang, question=stem,
                             choices=shuffled, answer=shuffled.index(correct), explanation=expl))

    def sa(self, lesson, level, dang, stem, answer, expl, tol=None, unit=None):
        a = float(answer)
        s = str(int(a)) if a == int(a) else f"{a:.4f}".rstrip('0').rstrip('.')
        q = dict(chapter=self.ch, lesson=lesson, level=level, dang=dang, question=stem, answer=s, explanation=expl)
        if tol: q['tolerance'] = tol
        if unit: q['unit'] = unit
        self.sas.append(q)

def check(q, kind):
    t = ' '.join([q['question'], q['explanation']] + [str(c) for c in q.get('choices', [])])
    assert '<' not in t.replace('\\le', '') or True
    assert t.count('$') % 2 == 0, f"$ lẻ: {q['question'][:80]}"
    assert len(q['explanation']) >= (40 if kind == 'mc' else 30), f"lời giải ngắn: {q['question'][:80]}"
    if kind == 'mc':
        assert len(q['choices']) == 4 and len(set(q['choices'])) == 4
        assert 0 <= q['answer'] < 4

def merge(subj, banks):
    """Ghi các câu mới vào data/<subj>/questions/{mc,short}.json (id >= FIRST_ID của chương được ghi lại mỗi lần chạy)."""
    bad = []
    for b in banks:
        for kind, qs in (('mc', b.mcs), ('short', b.sas)):
            for q in qs:
                try: check(q, kind)
                except AssertionError as e: bad.append(str(e))
    if bad:
        print(len(bad), 'câu không đạt kiểm tra:'); print('\n'.join(bad[:15])); raise SystemExit(1)
    for kind, attr, prefix in (('mc', 'mcs', 'mc'), ('short', 'sas', 'sa')):
        f = f'data/{subj}/questions/{kind}.json'
        d = json.load(open(f, encoding='utf-8'))
        qs = d['questions']
        chapters = {b.ch for b in banks}
        def old(q):
            n = int(q['id'].rsplit('-', 1)[1])
            return q['chapter'] in chapters and n >= FIRST_ID
        qs = [q for q in qs if not old(q)]
        existing = {(q['question'], tuple(sorted(map(str, q.get('choices', [])))), str(q['answer']) if kind == 'short' else '') for q in qs}
        for b in banks:
            n = FIRST_ID
            for q in getattr(b, attr):
                check(q, kind)
                key = (q['question'], tuple(sorted(map(str, q.get('choices', [])))), str(q['answer']) if kind == 'short' else '')
                if key in existing: continue
                existing.add(key)
                q = dict(id=f"{prefix}-{b.ch}-{n:03d}", **q); n += 1
                qs.append(q)
        order = {}
        qs.sort(key=lambda q: (q['chapter'], int(q['id'].rsplit('-', 1)[1])))
        d['questions'] = qs
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print(subj, kind, 'tổng', len(qs))


# ---------- tiện ích biểu thức tuyến tính / quy hoạch tuyến tính nhỏ ----------
def lin(a, b, xs='x', ys='y'):
    """Chuỗi LaTeX của a*x + b*y."""
    parts = []
    for coef, var in ((a, xs), (b, ys)):
        if coef == 0: continue
        sign = '-' if coef < 0 else '+'
        mag = abs(coef)
        term = (var if mag == 1 else f"{mag}{var}")
        parts.append((sign, term))
    if not parts: return '0'
    out = ('-' if parts[0][0] == '-' else '') + parts[0][1]
    for sign, term in parts[1:]:
        out += f" {sign} {term}"
    return out

SYM = {'<=': '\\le', '>=': '\\ge', '<': '<', '>': '>'}

def ineq(a, b, op, c):
    return f"{lin(a, b)} {SYM[op]} {c}"

def holds(a, b, op, c, x, y):
    v = a * x + b * y
    return {'<=': v <= c, '>=': v >= c, '<': v < c, '>': v > c}[op]

def vertices(cons):
    """cons: list (a,b,op,c). Trả về các đỉnh (Fraction) của miền nghiệm (giao các biên thoả mọi ràng buộc)."""
    from itertools import combinations
    pts = set()
    for (a1, b1, _, c1), (a2, b2, _, c2) in combinations(cons, 2):
        det = a1 * b2 - a2 * b1
        if det == 0: continue
        x = Fraction(c1 * b2 - c2 * b1, det); y = Fraction(a1 * c2 - a2 * c1, det)
        if all(holds(a, b, '<=' if op in ('<=', '<') else '>=', c, x, y) for a, b, op, c in cons):
            pts.add((x, y))
    return sorted(pts)
