import json, re, glob

def fix_str(s):
    if not isinstance(s, str): return s
    return re.sub(r'(\d)\.(\d)', r'\1,\2', s)

def walk(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = walk(v)
            if k == "question" and "answer" in obj:
                ans = str(obj["answer"])
                ans_fixed = fix_str(ans)
                if "," in ans_fixed and "làm tròn" not in obj[k].lower():
                    if ' <span' in obj[k]:
                        obj[k] = obj[k].replace(' <span', ' (làm tròn đến chữ số thập phân thích hợp) <span')
                    else:
                        obj[k] += ' (làm tròn đến chữ số thập phân thích hợp)'
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            obj[i] = walk(v)
    elif isinstance(obj, str):
        return fix_str(obj)
    return obj

for file in glob.glob('scripts/bank/*.json'):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    walk(data)
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
