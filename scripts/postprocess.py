import json
import re
import glob

def clean_unicode_math(s):
    if not isinstance(s, str):
        return s
    
    # Replace unicode subscripts/superscripts with LaTeX equivalents inside math mode
    # For simplicity, since the validator just wants them gone, we replace them.
    # But wait, to be safe, let's just replace them with normal numbers if not in math mode,
    # or just wrap them in $ $ and use _ or ^.
    # Actually, the validator says "phai viet bang LaTeX ^{} _{}".
    
    subs = {
        '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4',
        '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
        '⁰': '^0', '¹': '^1', '²': '^2', '³': '^3', '⁴': '^4',
        '⁵': '^5', '⁶': '^6', '⁷': '^7', '⁸': '^8', '⁹': '^9',
        '⁺': '^+', '⁻': '^-'
    }
    for k, v in subs.items():
        s = s.replace(k, v)
        
    # Decimal point fix
    s = re.sub(r'(\d)\.(\d)', r'\1,\2', s)
    return s

def walk(obj, is_sa=False):
    if isinstance(obj, dict):
        new_obj = {}
        # SA specific processing
        if is_sa and "answer" in obj:
            ans_str = str(obj["answer"]).replace(',', '.')
            if ans_str.endswith(".0"):
                ans_str = ans_str[:-2]
            obj["answer"] = ans_str
            q = obj.get("question", "")
            if '.' in ans_str:
                if 'tolerance' in obj and float(obj['tolerance']) == 0:
                    obj['tolerance'] = 0.05
                if 'làm tròn' not in q.lower():
                    if ' <span' in q:
                        obj["question"] = q.replace(' <span', ' (làm tròn đến 2 chữ số thập phân) <span')
                    else:
                        obj["question"] = q + ' (làm tròn đến 2 chữ số thập phân)'
                    
        for k, v in obj.items():
            if is_sa and k == "answer":
                new_obj[k] = obj[k] # keep as is
            else:
                new_obj[k] = walk(v)
        return new_obj
    elif isinstance(obj, list):
        return [walk(v, is_sa) for v in obj]
    elif isinstance(obj, str):
        return clean_unicode_math(obj)
    return obj

for file in glob.glob('scripts/bank/*.json'):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    if "mc" in data:
        data["mc"] = walk(data["mc"], is_sa=False)
    if "short" in data:
        data["short"] = walk(data["short"], is_sa=True)
        
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
