import re

with open('e:/projects/toan10/scripts/fix_hoa10_c5_p1.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace duplicated answer keys where the first one ends with `],` instead of `},`
pattern = re.compile(r'\"answer\": 0, \"explanation\": \".*?\"],\n\s*\"answer\": 0, \"explanation\": (\".*?\"})')

new_content = pattern.sub(r'"answer": 0, "explanation": \1', content)

with open('e:/projects/toan10/scripts/fix_hoa10_c5_p1.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
