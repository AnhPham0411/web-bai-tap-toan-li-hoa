import json
import glob

def audit():
    errors = []
    types_found = set()
    files = glob.glob('data/*/theory/*.json') + glob.glob('data/*/theory-*.json')
    for p in files:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for lesson in data.get('lessons', []):
            for i, b in enumerate(lesson.get('blocks', [])):
                btype = b.get('type')
                types_found.add(btype)
                if btype == 'formula' and not isinstance(b.get('items'), list):
                    errors.append((p, lesson.get('id'), i, 'formula missing items list', b))
                elif btype == 'list' and not isinstance(b.get('items'), list):
                    errors.append((p, lesson.get('id'), i, 'list missing items list', b))
                elif btype == 'table' and (not isinstance(b.get('headers'), list) or not isinstance(b.get('rows'), list)):
                    errors.append((p, lesson.get('id'), i, 'table missing headers/rows', b))
                elif btype not in ['heading', 'text', 'list', 'definition', 'theorem', 'note', 'example', 'formula', 'table']:
                    errors.append((p, lesson.get('id'), i, f'unknown type: {btype}', b))
    
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print(f"Total theory files checked: {len(files)}")
    print(f"Block types found: {types_found}")
    print(f"Total schema errors found: {len(errors)}")
    for err in errors:
        print(f"[{err[0]}] lesson: {err[1]}, block #{err[2]}: {err[3]}")
        print(f"   Content keys: {list(err[4].keys())}")
        if 'title' in err[4]:
            print(f"   Title: {err[4]['title']}")

if __name__ == '__main__':
    audit()
