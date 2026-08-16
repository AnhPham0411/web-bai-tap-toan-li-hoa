# Design Document: Web Bài Tập Toán - Lý - Hóa 10 & Generator Dataset

## 1. Overview
Expanding the existing Grade 10 web learning application (`toan10`) into a comprehensive multi-subject exercise web application supporting **Toán 10 (Math)**, **Vật lí 10 (Physics)**, and **Hóa học 10 (Chemistry)** based on the GDPT 2018 curriculum (Kết nối tri thức với cuộc sống, Semester 1).

The project will generate and host **2,250 high-quality exercises** (750 questions per subject across 5 chapters each), connect to GitHub repository `https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa`, and deploy to Vercel.

---

## 2. Core Requirements & Dataset Specifications

### 2.1 Multi-Subject Architecture
- **Subjects Included:**
  1. `toan10`: Toán 10 — Học kì 1 (5 Chapters)
  2. `ly10`: Vật lí 10 — Học kì 1 (5 Chapters)
  3. `hoa10`: Hóa học 10 — Học kì 1 (5 Chapters)
- **Data Manifest (`data/manifest.json`):** Updated to enable all three subjects with seamless switching in the web UI.

### 2.2 Question Volume & Distribution
- **Per Chapter Breakdown (5 chapters per subject):**
  - Total per chapter: **150 questions**
  - Multiple Choice (`mc.json`): **120 questions**
  - Short Answer (`short.json`): **30 questions**
- **Difficulty Breakdown per Chapter:**
  - Nhận biết (`nb`): 50% (60 MC + 15 Short = 75 items)
  - Thông hiểu (`th`): 40% (48 MC + 12 Short = 60 items)
  - Vận dụng (`vd`): 10% (12 MC + 3 Short = 15 items)
- **Total Dataset Volume across 3 subjects:**
  - 3 subjects × 5 chapters × 150 questions = **2,250 questions** (1,800 MC + 450 Short).

---

## 3. Curriculum Coverage

### 3.1 Toán 10 (Math 10)
- **Chapter 1 (c1):** Mệnh đề và tập hợp (Lessons: b1, b2)
- **Chapter 2 (c2):** Bất phương trình và hệ bất phương trình bậc nhất hai ẩn (Lessons: b3, b4)
- **Chapter 3 (c3):** Hệ thức lượng trong tam giác (Lessons: b5, b6)
- **Chapter 4 (c4):** Vectơ (Lessons: b7, b8, b9, b10, b11)
- **Chapter 5 (c5):** Các số đặc trưng của mẫu số liệu không ghép nhóm (Lessons: b12, b13, b14)

### 3.2 Vật lí 10 (Physics 10)
- **Chapter 1 (c1):** Mở đầu & Sai số trong đo lường vật lí
- **Chapter 2 (c2):** Mô tả chuyển động (Vận tốc, độ dịch chuyển, đồ thị)
- **Chapter 3 (c3):** Chuyển động biến đổi (Gia tốc, chuyển động biến đổi đều, rơi tự do)
- **Chapter 4 (c4):** Động lực học (Các định luật Newton, các lực cơ học)
- **Chapter 5 (c5):** Năng lượng, Công và Công suất

### 3.3 Hóa học 10 (Chemistry 10)
- **Chapter 1 (c1):** Cấu tạo nguyên tử (Hạt nhân, vỏ nguyên tử, orbital, cấu hình electron)
- **Chapter 2 (c2):** Bảng tuần hoàn các nguyên tố hóa học & Định luật tuần hoàn
- **Chapter 3 (c3):** Liên kết hóa học (Liên kết ion, liên kết cộng hóa trị, liên kết hydrogen)
- **Chapter 4 (c4):** Phản ứng oxi hóa - khử & Số oxi hóa
- **Chapter 5 (c5):** Năng lượng hóa học (Biến thiên enthalpy phản ứng)

---

## 4. Python Generator Architecture (`scripts/generate_all.py`)

A modular Python generation engine will produce all 2,250 questions cleanly formatted into JSON.

### 4.1 Schema Verification
Each question item complies strictly with the schema:
```json
{
  "id": "mc-c1-001",
  "chapter": "c1",
  "lesson": "b1",
  "level": "nb",
  "question": "Formatted LaTeX question text",
  "choices": ["Choice A", "Choice B", "Choice C", "Choice D"],
  "answer": 0,
  "explanation": "Step-by-step detailed solution text"
}
```
Short answer format:
```json
{
  "id": "sa-c1-001",
  "chapter": "c1",
  "lesson": "b1",
  "level": "nb",
  "question": "Formatted LaTeX question text requiring numerical answer",
  "answer": "12.5",
  "tolerance": 0.05,
  "unit": "m/s",
  "explanation": "Step-by-step solution"
}
```

### 4.2 Formatting & LaTeX Escaping
- Escapes LaTeX backslashes for valid JSON strings (`"\\frac{a}{b}"`, `"\\vec{v}"`, `"\\degree"`).
- Chemistry formulas support chemical symbols (`H_2SO_4`, `Fe^{3+}`).

---

## 5. UI Updates & Multi-Subject Switching

- **Web Title & Brand:** Update header to "Luyện Bài Tập Toán - Lý - Hóa 10".
- **Subject Selector:** Modern dropdown / pill selector in navbar allowing users to pick subject (`Toán 10`, `Vật lí 10`, `Hóa học 10`).
- **Data Engine:** Dynamic path fetching based on active subject (`data/toan10`, `data/ly10`, `data/hoa10`).

---

## 6. Git Repository & Deployment Plan

1. **Git Initialization & Remote Setup:**
   - Initialize git repo in workspace.
   - Remote URL: `https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa.git`
2. **Push to Remote:**
   - Commit all code, generator scripts, theories, index.json, questions, and UI changes.
   - Push to `main` branch.
3. **Vercel Deployment:**
   - Maintain Vercel configuration (`vercel.json`).
   - Trigger deployment update via Git / Vercel integration.
