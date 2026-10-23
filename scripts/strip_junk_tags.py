"""Xoá thẻ rác (<span style="display:none">vN</span>, <!-- vN -->) khỏi data câu hỏi/lý thuyết."""
import json, re, glob, sys

JUNK = re.compile(r'\s*(?:<span style="display:none">[^<]*</span>|<!--\s*v\d+\s*-->)')

def clean(o):
    if isinstance(o, str):
        return JUNK.sub('', o).rstrip()
    if isinstance(o, list):
        return [clean(x) for x in o]
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    return o

changed = 0
for f in sorted(glob.glob('data/**/*.json', recursive=True)):
    raw = open(f, encoding='utf-8').read()
    data = json.loads(raw)
    new = clean(data)
    if new != data:
        indent = 2 if raw.startswith('{\n  ') or raw.startswith('[\n  ') else None
        open(f, 'w', encoding='utf-8').write(json.dumps(new, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else ''))
        changed += 1
        print('cleaned', f)
print('files changed:', changed)
