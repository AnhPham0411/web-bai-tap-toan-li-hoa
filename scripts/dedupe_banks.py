"""Bỏ nhãn rác '(BT N)'/'(Nhóm N)' và loại câu trùng (cùng đề + cùng tập lựa chọn / cùng đáp án) cho Toán/Lý/Hóa 10."""
import json, re, sys, collections

MARK = re.compile(r'\s*\((?:BT|Nhóm)\s*\d+\)', re.I)

def load(f):
    d = json.load(open(f, encoding='utf-8'))
    return d, (d['questions'] if isinstance(d, dict) else d)

def dump(f, d, qs):
    if isinstance(d, dict): d['questions'] = qs
    else: d = qs
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def run(subj):
    for kind in ('mc', 'short'):
        f = f'data/{subj}/questions/{kind}.json'
        d, qs = load(f)
        seen, out = set(), []
        for q in qs:
            for k in ('question', 'dang'):
                if k in q: q[k] = MARK.sub('', q[k]).strip()
            key = (q['question'], tuple(sorted(map(str, q.get('choices', [])))), str(q['answer']) if kind == 'short' else '')
            if key in seen: continue
            seen.add(key); out.append(q)
        dump(f, d, out)
        c = collections.Counter(q['chapter'] for q in out)
        print(subj, kind, len(qs), '->', len(out), dict(sorted(c.items())))

for s in sys.argv[1:]: run(s)
