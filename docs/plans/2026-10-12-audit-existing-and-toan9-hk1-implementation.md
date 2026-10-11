# Kế hoạch Triển khai: Audit Hệ thống & Xây dựng Toán 9 Học kì 1

> **For Antigravity:** REQUIRED SUB-SKILL: Load executing-plans to implement this plan task-by-task.

**Goal:** Kiểm định & sửa lỗi toán học chuyên sâu cho các ngân hàng câu hỏi hiện tại, đồng thời xây dựng hoàn chỉnh lý thuyết và 750 câu hỏi tự khép kín cho 5 chương Toán 9 Học kì 1 (SGK Kết nối tri thức GDPT 2018), tích hợp kích hoạt trên Web SPA.

**Architecture:** Sử dụng script audit 4 tầng để làm sạch ngân hàng dữ liệu hiện có; sử dụng generator `scripts/gen_bank_toan9_hk1.py` để sinh chuẩn 750 câu hỏi đạt chuẩn tỉ lệ độ khó 50/40/10; cập nhật `build_data.py` để assemble và kiểm định 0 lỗi.

**Tech Stack:** Python 3 (Audit & Bank Generator, Build Data pipeline), JavaScript ES Modules / CSS3 (Web SPA).

---

### Task 1: Xây dựng script kiểm tra toán học và cú pháp chuyên sâu `scripts/audit_banks_deep.py`

**Files:**
- Create: `scripts/audit_banks_deep.py`

**Step 1: Viết script audit chuyên sâu 4 tầng**
- Quét toàn bộ file trong `scripts/bank/` và `data/*/questions/`.
- Kiểm tra các lỗi:
  - LaTeX không tương thích engine `math.js` (`\begin{cases}`, `\dots`, escape sai).
  - Trùng lặp phương án trong câu trắc nghiệm.
  - Đáp án đúng `answer` không hợp lệ hoặc không có trong phương án.
  - Câu hỏi trả lời ngắn có đáp án không phải số nguyên/thập phân chuẩn.
  - Mâu thuẫn giữa đề bài, đáp án và lời giải.

**Step 2: Chạy script audit trên các bộ đề hiện tại**
Run: `python scripts/audit_banks_deep.py`  
Expected: Danh sách các vấn đề được phát hiện hoặc báo cáo 0 lỗi.

**Step 3: Commit**
```bash
git add scripts/audit_banks_deep.py
git commit -m "feat(audit): add deep math and latex auditor for question banks"
```

---

### Task 2: Khắc phục các lỗi phát hiện được từ bước Audit (nếu có)

**Files:**
- Modify: Các file ngân hàng tương ứng trong `scripts/bank/` hoặc `data/*/questions/`

**Step 1: Vá lỗi số liệu, LaTeX hoặc đáp án**
Sửa chính xác các câu hỏi có vấn đề để đảm bảo tính chặt chẽ về toán học và hiển thị.

**Step 2: Chạy lại audit và kiểm định dữ liệu**
Run: `python scripts/audit_banks_deep.py && python scripts/build_data.py --check`  
Expected: Tất cả vượt qua 100% không còn lỗi.

**Step 3: Commit**
```bash
git add scripts/bank/ data/
git commit -m "fix(banks): resolve issues identified by deep audit"
```

---

### Task 3: Cập nhật `scripts/build_data.py` hỗ trợ môn `toan9`

**Files:**
- Modify: `scripts/build_data.py`

**Step 1: Cấu hình danh sách chương cho `toan9`**
Thêm `toan9` vào `CHAPTERS`: `["c1", "c2", "c3", "c4", "c5"]`.

**Step 2: Kiểm tra tương thích ngược**
Run: `python scripts/build_data.py --check`  
Expected: KIEM DINH toan10, ly10, hoa10: OK.

**Step 3: Commit**
```bash
git add scripts/build_data.py
git commit -m "refactor(build_data): configure chapter list for toan9"
```

---

### Task 4: Biên soạn lý thuyết cho 5 chương Toán 9 HK1

**Files:**
- Create: `data/toan9/theory/c1.json`
- Create: `data/toan9/theory/c2.json`
- Create: `data/toan9/theory/c3.json`
- Create: `data/toan9/theory/c4.json`
- Create: `data/toan9/theory/c5.json`

**Step 1: Biên soạn `c1.json` (Hệ phương trình bậc nhất hai ẩn)**  
Khái niệm, phương pháp thế, phương pháp cộng đại số, giải bài toán bằng cách lập hệ phương trình.

**Step 2: Biên soạn `c2.json` (Phương trình và bất phương trình bậc nhất một ẩn)**  
Phương trình tích, phương trình chứa ẩn ở mẫu, bất đẳng thức, bất phương trình bậc nhất một ẩn.

**Step 3: Biên soạn `c3.json` (Căn bậc hai và căn bậc ba)**  
Căn bậc hai số học, khai phương tích và thương, biến đổi biểu thức chứa căn, căn bậc ba.

**Step 4: Biên soạn `c4.json` (Hệ thức lượng trong tam giác vuông)**  
Tỉ số lượng giác góc nhọn, hệ thức cạnh và góc, ứng dụng thực tế.

**Step 5: Biên soạn `c5.json` (Đường tròn)**  
Cung và dây, góc ở tâm, độ dài cung và diện tích quạt tròn, vị trí tương đối của đường thẳng và đường tròn, tiếp tuyến.

**Step 6: Commit**
```bash
git add data/toan9/theory/
git commit -m "feat(toan9): add comprehensive theory for chapters 1-5"
```

---

### Task 5: Xây dựng Generator sinh câu hỏi Toán 9 HK1 (`scripts/gen_bank_toan9_hk1.py`)

**Files:**
- Create: `scripts/gen_bank_toan9_hk1.py`

**Step 1: Cấu trúc hóa các dạng bài cho 5 chương**
- Mỗi chương: 24 dạng TN $\times$ 5 biến thể = 120 câu TN (60 NB, 48 TH, 12 VD).
- Mỗi chương: 6 dạng TLN $\times$ 5 biến thể = 30 câu TLN (15 NB, 12 TH, 3 VD).
- Đảm bảo độc lập số liệu, không trùng `norm_key`, đáp số nguyên chuẩn xác.

**Step 2: Chạy thử nghiệm sinh dữ liệu cho 5 chương**
Run: `python scripts/gen_bank_toan9_hk1.py`  
Expected: Tạo thành công `scripts/bank/toan9_c1.json` đến `toan9_c5.json`.

**Step 3: Commit**
```bash
git add scripts/gen_bank_toan9_hk1.py scripts/bank/toan9_c*.json
git commit -m "feat(toan9): create question banks for chapters 1-5 (750 questions)"
```

---

### Task 6: Lắp ráp dữ liệu và Kiểm định toàn diện Toán 9

**Files:**
- Modify: `data/toan9/questions/mc.json`
- Modify: `data/toan9/questions/short.json`
- Modify: `data/manifest.json`

**Step 1: Chạy build dữ liệu chính thức**
Run: `python scripts/build_data.py`  
Expected: Ghi 600 câu TN vào `data/toan9/questions/mc.json` và 150 câu TLN vào `data/toan9/questions/short.json`.

**Step 2: Cập nhật `data/manifest.json`**
Đặt `toan9.available = true`, ghi chú rõ 750 câu hỏi HK1.

**Step 3: Chạy kiểm định toàn diện 4 môn**
Run: `python scripts/build_data.py --check`  
Expected: OK 100% cả 4 môn `toan10`, `ly10`, `hoa10`, `toan9`.

**Step 4: Commit**
```bash
git add data/toan9/questions/ data/manifest.json
git commit -m "feat(toan9): assemble 750 questions and activate subject in manifest"
```

---

### Task 7: Chạy kiểm thử tự động toàn diện

**Files:**
- Test: `tests/test_audit_static.py`
- Test: `tests/frontend.test.mjs`

**Step 1: Chạy pytest**
Run: `python -m pytest tests/`  
Expected: 7 passed.

**Step 2: Chạy frontend test**
Run: `node tests/frontend.test.mjs`  
Expected: 57 passed (TẤT CẢ ĐỀU PASS).

**Step 3: Chạy lại deep audit**
Run: `python scripts/audit_banks_deep.py`  
Expected: 0 lỗi trên toàn bộ hệ thống.
