# Kế hoạch triển khai: Hoàn thiện Học kì 2 môn Toán 11 và Toán 12 (GDPT 2018)

> **For Antigravity:** REQUIRED SUB-SKILL: Load executing-plans to implement this plan task-by-task.

**Goal:** Xây dựng trọn vẹn Học kì 2 cho môn Toán 11 (4 chương c6-c9, 15 bài học, 600 câu hỏi) và môn Toán 12 (3 chương c4-c6, 9 bài học, 450 câu hỏi) bám sát SGK Kết nối tri thức với cuộc sống (GDPT 2018), nâng quy mô hệ thống lên 5.850 câu hỏi.

**Architecture:** Sử dụng cấu trúc builder module `scripts/toan11_builder/` và `scripts/toan12_builder/` để sinh ngân hàng chuẩn vào `scripts/bank/`, đồng bộ hóa lý thuyết vào `data/*/theory/`, dùng pipeline `build_data.py` để kiểm định chất lượng và đóng gói dữ liệu câu hỏi.

**Tech Stack:** Python 3 (data generator, validation), Node.js (frontend testing), Vanilla JS (ES Modules) & CSS.

---

### Task 1: Biên soạn Dữ liệu Lý thuyết HK2 cho Toán 11
**Files:**
- Create: `data/toan11/theory/c6.json` (Hàm số mũ và hàm số lôgarit - 4 bài)
- Create: `data/toan11/theory/c7.json` (Quan hệ vuông góc trong không gian - 6 bài)
- Create: `data/toan11/theory/c8.json` (Các quy tắc tính đạo hàm - 3 bài)
- Create: `data/toan11/theory/c9.json` (Các quy tắc tính xác suất - 2 bài)

**Step 1:** Viết 4 file lý thuyết chuẩn GDPT 2018 cho Toán 11 HK2 với đầy đủ blocks (heading, definition, theorem, example, formula).
**Step 2:** Kiểm tra tính hợp lệ bằng `python scripts/audit_theory.py`.
**Step 3:** Commit: `git commit -m "feat(toan11): add term 2 theory data files c6-c9"`.

---

### Task 2: Biên soạn Dữ liệu Lý thuyết HK2 cho Toán 12
**Files:**
- Create: `data/toan12/theory/c4.json` (Nguyên hàm và tích phân - 3 bài)
- Create: `data/toan12/theory/c5.json` (Phương pháp toạ độ trong không gian - 4 bài)
- Create: `data/toan12/theory/c6.json` (Xác suất có điều kiện - 2 bài)

**Step 1:** Viết 3 file lý thuyết chuẩn GDPT 2018 cho Toán 12 HK2.
**Step 2:** Kiểm tra tính hợp lệ bằng `python scripts/audit_theory.py`.
**Step 3:** Commit: `git commit -m "feat(toan12): add term 2 theory data files c4-c6"`.

---

### Task 3: Xây dựng Module sinh ngân hàng câu hỏi Toán 11 HK2 (600 câu)
**Files:**
- Create: `scripts/toan11_builder/c6.py` (120 TN + 30 TLN)
- Create: `scripts/toan11_builder/c7.py` (120 TN + 30 TLN)
- Create: `scripts/toan11_builder/c8.py` (120 TN + 30 TLN)
- Create: `scripts/toan11_builder/c9.py` (120 TN + 30 TLN)
- Create: `scripts/gen_bank_toan11_hk2.py` (runner sinh ra `scripts/bank/toan11_c6..c9.json`)

**Step 1:** Lập trình các module sinh đề với thuật toán sinh biến thể toán học chuẩn xác, phân bổ 50% NB / 40% TH / 10% VD.
**Step 2:** Chạy `python scripts/gen_bank_toan11_hk2.py` và kiểm tra 4 file ngân hàng được tạo thành công trong `scripts/bank/`.
**Step 3:** Commit: `git commit -m "feat(toan11): create question bank builders for chapters c6-c9"`.

---

### Task 4: Xây dựng Module sinh ngân hàng câu hỏi Toán 12 HK2 (450 câu)
**Files:**
- Create: `scripts/toan12_builder/c4.py` (120 TN + 30 TLN)
- Create: `scripts/toan12_builder/c5.py` (120 TN + 30 TLN)
- Create: `scripts/toan12_builder/c6.py` (120 TN + 30 TLN)
- Create: `scripts/gen_bank_toan12_hk2.py` (runner sinh ra `scripts/bank/toan12_c4..c6.json`)

**Step 1:** Lập trình các module sinh đề cho Chương IV, V, VI của Toán 12.
**Step 2:** Chạy `python scripts/gen_bank_toan12_hk2.py` và kiểm tra 3 file ngân hàng được tạo thành công trong `scripts/bank/`.
**Step 3:** Commit: `git commit -m "feat(toan12): create question bank builders for chapters c4-c6"`.

---

### Task 5: Cập nhật Pipeline `build_data.py` và Biên dịch Dữ liệu
**Files:**
- Modify: `scripts/build_data.py` (Cập nhật `SUBJECT_CHAPTERS` mở rộng toan11 lên c1-c9, toan12 lên c1-c6)
- Modify: `data/toan11/index.json` (Khai báo đủ 9 chương, gán `term: 2` cho c6-c9)
- Modify: `data/toan12/index.json` (Khai báo đủ 6 chương, gán `term: 2` cho c4-c6)
- Output: `data/toan11/questions/mc.json`, `data/toan11/questions/short.json` (1.350 câu)
- Output: `data/toan12/questions/mc.json`, `data/toan12/questions/short.json` (900 câu)

**Step 1:** Chạy `python scripts/postprocess.py` để chuẩn hóa unicode và format đáp số.
**Step 2:** Chạy `python scripts/build_data.py` để kiểm định chất lượng toán học và ghi dữ liệu ra thư mục `data/`.
**Step 3:** Commit: `git commit -m "feat(data): compile term 2 data for toan11 and toan12 via build_data pipeline"`.

---

### Task 6: Đồng bộ Manifest, Branding và Tài liệu thống kê
**Files:**
- Modify: `data/manifest.json` (Cập nhật toan11 và toan12 thành Cả năm, gỡ bỏ toan11_hk2 và toan12_hk2 khỏi danh sách mở rộng)
- Modify: `index.html` (Cập nhật meta & footer thống kê 5.850 câu hỏi)
- Modify: `README.md` (Thống kê đầy đủ toàn bộ 39 chương / 115 bài học / 5.850 câu hỏi)

**Step 1:** Chỉnh sửa các file trên theo đúng số liệu 5.850 câu hỏi.
**Step 2:** Commit: `git commit -m "docs: update manifest, index.html, and README for 5850 questions"`.

---

### Task 7: Kiểm thử Toàn diện Hệ thống
**Files:**
- Run: `python scripts/super_deep_audit.py`
- Run: `node scripts/verify_all_theory_renders.mjs`
- Run: `node scripts/verify_all_questions_grading.mjs`
- Run: `pytest -v`
- Run: `node tests/frontend.test.mjs`

**Step 1:** Chạy tất cả các bộ kiểm thử tự động, xác nhận 100% PASS và 0 lỗi.
**Step 2:** Commit nếu có điều chỉnh kiểm thử.

---

### Task 8: Triển khai Vercel Production và Kiểm tra Live
**Step 1:** Push nhánh `main` lên GitHub `origin/main`.
**Step 2:** Chạy `vercel --prod --yes` deploy lên Vercel.
**Step 3:** Kiểm tra trực tiếp trên link live `https://toan10-rouge.vercel.app`.
