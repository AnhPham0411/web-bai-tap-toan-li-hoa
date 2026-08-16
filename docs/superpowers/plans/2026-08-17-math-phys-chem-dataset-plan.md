# Multi-Subject Exercise Web App & 2,250 Questions Dataset Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and generate 2,250 high-quality exercises (750 each for Grade 10 Math, Physics, and Chemistry), update the web app UI for multi-subject switching, initialize Git linked to GitHub `https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa`, push code, and verify Vercel deployment.

**Architecture:** A Python generation pipeline in `scripts/generate_all.py` creates robust JSON datasets for Math (`data/toan10`), Physics (`data/ly10`), and Chemistry (`data/hoa10`). The web app frontend (`assets/js/`) dynamically reads the selected subject from `data/manifest.json`.

**Tech Stack:** JavaScript (ES6), HTML5, Vanilla CSS, Python 3, Git, Vercel.

---

### Task 1: Create Dataset Generation Engine for Toán 10 (750 questions)

**Files:**
- Create: `scripts/generators/toan10_gen.py`
- Modify: `scripts/generate_all.py`

- [ ] **Step 1: Write `toan10_gen.py` module**

Write Python functions to generate 120 MC and 30 Short questions per chapter for all 5 chapters of Grade 10 Math (750 questions total), respecting the 50% `nb`, 40% `th`, 10% `vd` difficulty distribution.

- [ ] **Step 2: Verify `toan10` generator execution**

Run: `python -c "import sys; sys.path.append('scripts'); from generators.toan10_gen import generate_toan10; data = generate_toan10(); print({c: (len(d['mc']), len(d['short'])) for c, d in data.items()})"`
Expected output: `{ 'c1': (120, 30), 'c2': (120, 30), 'c3': (120, 30), 'c4': (120, 30), 'c5': (120, 30) }`

- [ ] **Step 3: Commit Task 1**

```bash
git add scripts/generators/toan10_gen.py
git commit -m "feat: add grade 10 math 750 questions generator engine"
```

---

### Task 2: Create Dataset Generators for Vật lí 10 & Hóa học 10 (1,500 questions)

**Files:**
- Create: `scripts/generators/ly10_gen.py`
- Create: `scripts/generators/hoa10_gen.py`
- Create: `scripts/generate_all.py`

- [ ] **Step 1: Write `ly10_gen.py` and `hoa10_gen.py` modules**

Implement generators for:
- Vật lí 10 (Chapters c1 to c5: 120 MC + 30 Short per chapter = 750 questions)
- Hóa học 10 (Chapters c1 to c5: 120 MC + 30 Short per chapter = 750 questions)

- [ ] **Step 2: Create master script `scripts/generate_all.py`**

Script imports all generators, validates total count (2,250 items), validates JSON syntax, escapes LaTeX properly, writes `index.json`, `mc.json`, `short.json` into `data/toan10/`, `data/ly10/`, `data/hoa10/`, and theory json files.

- [ ] **Step 3: Execute `generate_all.py` to produce full dataset**

Run: `python scripts/generate_all.py`
Expected: Output files created in `data/toan10/questions/`, `data/ly10/questions/`, `data/hoa10/questions/`, theory files created. Total questions = 2,250.

- [ ] **Step 4: Commit Task 2**

```bash
git add scripts/ data/
git commit -m "feat: generate 2250 questions across Math, Physics, and Chemistry Grade 10"
```

---

### Task 3: Update Manifest, Web Frontend & Subject Navigation UI

**Files:**
- Modify: `data/manifest.json`
- Modify: `index.html`
- Modify: `assets/js/app.js`
- Modify: `assets/js/data.js`
- Modify: `assets/css/style.css`

- [ ] **Step 1: Update `data/manifest.json`**

Enable `toan10`, `ly10`, and `hoa10` as available subjects with full metadata.

- [ ] **Step 2: Update `index.html` and header subject picker**

Add subject selector control in header to switch dynamically between Toán 10, Vật lí 10, and Hóa học 10. Update page titles and brand tags.

- [ ] **Step 3: Update `assets/js/data.js` and `app.js`**

Ensure `loadSubject(subjectId)` correctly reloads index, theories, and questions when subject changes.

- [ ] **Step 4: Verify local web app loading**

Test loading subject data using node server or local verification.

- [ ] **Step 5: Commit Task 3**

```bash
git add data/manifest.json index.html assets/
git commit -m "feat: add multi-subject UI support for Math, Physics, Chemistry"
```

---

### Task 4: Git Remote Setup & Push to GitHub Repository

**Files:**
- Repository: `https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa.git`

- [ ] **Step 1: Initialize Git repo (if needed) & set remote**

Run:
```bash
git init
git remote add origin https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa.git
```

- [ ] **Step 2: Push changes to GitHub main branch**

Run:
```bash
git branch -M main
git push -u origin main --force
```

- [ ] **Step 3: Verify GitHub push status**

Confirm repository updated with all source code, datasets, and Vercel configuration.

---

### Task 5: Vercel Configuration Verification & Documentation Update

**Files:**
- Modify: `README.md`
- Modify: `vercel.json`

- [ ] **Step 1: Update `README.md`**

Update README with full documentation of dataset structure, 2,250 questions count, subjects, Vercel deployment link, and running instructions.

- [ ] **Step 2: Commit & final push**

```bash
git add README.md vercel.json
git commit -m "docs: update README with 2250 questions multi-subject specification"
git push origin main
```
