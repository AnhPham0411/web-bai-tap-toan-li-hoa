import sys

with open('e:/projects/toan10/scripts/fix_hoa10_c5_p2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '"explanation":' in line:
        stripped = line.rstrip('\n\r')
        if stripped.endswith('],'):
            lines[i] = stripped[:-2] + '},\n'

with open('e:/projects/toan10/scripts/fix_hoa10_c5_p2.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
