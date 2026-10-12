import json
import os

with open('data/manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

for subj in manifest['subjects']:
    if not subj.get('available'):
        continue
    sid = subj['id']
    spath = subj['path']
    ipath = f'data/{spath}/index.json'
    print(f'=== Auditing subject {sid} ({spath}) ===')
    if not os.path.exists(ipath):
        print(f'ERROR: {ipath} does not exist!')
        continue
    with open(ipath, 'r', encoding='utf-8') as f:
        idx = json.load(f)
    for ch in idx['chapters']:
        cid = ch['id']
        tpath = f'data/{spath}/{ch["theory"]}'
        if not os.path.exists(tpath):
            print(f'  MISSING THEORY: chapter {cid} -> {tpath}')
        else:
            with open(tpath, 'r', encoding='utf-8') as f:
                tdata = json.load(f)
            t_lessons = {l['id'] for l in tdata.get('lessons', [])}
            idx_lessons = {l['id'] for l in ch.get('lessons', [])}
            if not idx_lessons.issubset(t_lessons):
                print(f'  LESSON MISMATCH in {cid}: index has {idx_lessons - t_lessons} not in theory')
    for qset in idx.get('questionSets', []):
        qpath = f'data/{spath}/{qset["file"]}'
        if not os.path.exists(qpath):
            print(f'  MISSING QUESTION FILE: {qpath}')
