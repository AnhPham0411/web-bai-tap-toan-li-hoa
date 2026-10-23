"""Sửa lỗi dữ liệu cũ đã dò ra: câu giữ chỗ ('biến thể', 'Ví dụ N'), tập hợp lặp phần tử, rò rỉ biến 'val', phương án trùng nhau (ký tự \\u200b)."""
import json, re, glob, sys
from collections import Counter

def load(f): return json.load(open(f, encoding='utf-8'))
def save(f, d): open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# ---- Toán 10: câu giữ chỗ / câu sai đề ----
f = 'data/toan10/questions/mc.json'; d = load(f); qs = d['questions']
DROP = {'mc-c1-018', 'mc-c1-019', 'mc-c1-020',                 # 4 bản trùng 'Ví dụ N'
        'mc-c1-033', 'mc-c1-034', 'mc-c1-035', 'mc-c1-036',    # {1,2,...,n} sai ký hiệu, trùng phương án
        'mc-c1-070', 'mc-c1-071', 'mc-c1-072',                 # 'biến thể N' (giữ lại 069)
        'mc-c1-094', 'mc-c1-095', 'mc-c1-096'}
REWORD = {'mc-c1-017': 'Chọn khẳng định đúng về điều kiện cần và đủ:',
          'mc-c1-069': 'Khẳng định nào sau đây đúng về quan hệ giữa các tập hợp số?',
          'mc-c1-093': 'Mệnh đề $P \\Rightarrow Q$ sai khi nào?'}
out = []
for q in qs:
    if q['id'] in DROP: continue
    if q['id'] in REWORD: q['question'] = REWORD[q['id']]
    if q['id'] in ('mc-c1-085', 'mc-c1-086', 'mc-c1-087', 'mc-c1-088'):
        k = {'mc-c1-085': 2, 'mc-c1-086': 3, 'mc-c1-087': 4, 'mc-c1-088': 5}[q['id']]
        q['explanation'] = f"Vì $x^2+1>0$ với mọi $x$ nên phương trình tương đương $x^2-{k*k}=0$, tức $x=\\pm{k}$. Tập nghiệm là $\\{{{k}, -{k}\\}}$."
    # tập hợp có phần tử lặp trong đề -> bỏ
    bad = False
    for m in re.findall(r'\\\{([^{}]*)\\\}', q['question']):
        items = [x.strip() for x in m.split(',') if x.strip()]
        if '...' not in m and len(items) != len(set(items)): bad = True
    if bad: continue
    out.append(q)
d['questions'] = out; save(f, d)

f = 'data/toan10/questions/short.json'; d = load(f)
for q in d['questions']:
    if q['id'] in ('sa-c1-016', 'sa-c1-017', 'sa-c1-018'):
        k = q['answer']
        q['explanation'] = f"Giao $(-\\infty; m)\\cap[{k}; +\\infty)=\\emptyset$ khi và chỉ khi $m\\le {k}$. Số nguyên $m$ lớn nhất thoả mãn là $m={k}$."
save(f, d)

# ---- Phương án trùng nhau (do ký tự ​) ở mọi môn ----
FACT = (1.5, 0.75, 3, 0.5, 2.5, 1.25, 4)
fixed = 0
for f in glob.glob('data/*/questions/mc.json'):
    d = load(f); changed = False
    for q in d['questions']:
        if not any('​' in c for c in q['choices']): continue
        ch = [c.replace('​', '') for c in q['choices']]
        correct = ch[q['answer']]
        seen = set(); new = []
        for i, c in enumerate(ch):
            if c in seen:
                m = re.search(r'-?\d+(?:,\d+)?', correct)
                repl = None
                if m:
                    base = float(m.group(0).replace(',', '.')); dec = len(m.group(0).split(',')[1]) if ',' in m.group(0) else 0
                    for fct in FACT:
                        v = base * fct
                        t = f"{v:.{dec}f}".replace('.', ',')
                        cand = correct[:m.start()] + t + correct[m.end():]
                        if cand not in ch and cand not in new and cand not in seen:
                            repl = cand; break
                if repl is None:
                    print('KHÔNG SỬA ĐƯỢC', f, q['id'], ch); continue
                c = repl
            seen.add(c); new.append(c)
        q['choices'] = new; q['answer'] = new.index(correct) if correct in new else q['answer']
        changed = True; fixed += 1
    if changed: save(f, d)
print('đã sửa phương án trùng:', fixed)
