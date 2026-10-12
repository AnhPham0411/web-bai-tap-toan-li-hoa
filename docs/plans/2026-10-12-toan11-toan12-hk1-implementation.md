# Kế hoạch Triển khai: Mở rộng Toán 11 và Toán 12 (Học kì 1)

> **For Antigravity:** REQUIRED SUB-SKILL: Load executing-plans to implement this plan task-by-task.

**Goal:** Xây dựng hoàn chỉnh khung mục lục cả năm, nội dung lý thuyết và ngân hàng 1.200 câu hỏi (960 TN + 240 TLN, tỉ lệ 50/40/10) cho Học kì 1 của Toán 11 (5 chương, 750 câu) và Toán 12 (3 chương, 450 câu) theo SGK Kết nối tri thức GDPT 2018, tích hợp vào pipeline kiểm định và Web SPA.

**Architecture:** Sử dụng kiến trúc mô-đun hoá builder (`scripts/toan11_builder/`, `scripts/toan12_builder/`) với bộ sinh ngân hàng độc lập; tích hợp vào pipeline kiểm định `scripts/build_data.py` và bộ audit chuyên sâu `scripts/audit_banks_deep.py` đảm bảo không có bất kì lỗi toán học, LaTeX hay trùng lặp nào.

**Tech Stack:** Python 3 (Generator & Audit pipeline), JavaScript ES Modules / CSS3 (Web SPA), Node.js (Frontend test runner), Pytest.

---

### Task 1: Thiết lập cấu trúc khung mục lục và đăng ký môn trong manifest

**Files:**
- Create: `data/toan11/index.json`
- Create: `data/toan12/index.json`
- Modify: `data/manifest.json`

**Step 1: Tạo `data/toan11/index.json`**
Khai báo đầy đủ 9 chương cả năm theo SGK Kết nối tri thức Toán 11, gắn `term: 1` cho c1..c5 và `term: 2` cho c6..c9:
- `c1`: "Hàm số lượng giác và phương trình lượng giác" (Bài 1 -> Bài 5)
- `c2`: "Dãy số. Cấp số cộng và cấp số nhân" (Bài 6 -> Bài 8)
- `c3`: "Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm" (Bài 9, 10)
- `c4`: "Quan hệ song song trong không gian" (Bài 11 -> Bài 15)
- `c5`: "Giới hạn. Hàm số liên tục" (Bài 16, 17)
- `c6`: "Hàm số mũ và hàm số lôgarit" (Bài 18 -> Bài 21)
- `c7`: "Đạo hàm" (Bài 22 -> Bài 24)
- `c8`: "Quan hệ vuông góc trong không gian" (Bài 25 -> Bài 27)
- `c9`: "Các quy tắc tính xác suất" (Bài 28 -> Bài 30)

**Step 2: Tạo `data/toan12/index.json`**
Khai báo đầy đủ 6 chương cả năm theo SGK Kết nối tri thức Toán 12, gắn `term: 1` cho c1..c3 và `term: 2` cho c4..c6:
- `c1`: "Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số" (Bài 1 -> Bài 5)
- `c2`: "Toạ độ vectơ trong không gian" (Bài 6, 7)
- `c3`: "Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm" (Bài 8, 9)
- `c4`: "Nguyên hàm và tích phân" (Bài 10 -> Bài 12)
- `c5`: "Phương pháp toạ độ trong không gian" (Bài 13 -> Bài 15)
- `c6`: "Xác suất có điều kiện" (Bài 16 -> Bài 18)

**Step 3: Cập nhật `data/manifest.json`**
Thêm 2 đối tượng `toan11` và `toan12` vào `subjects`:
```json
"toan11": {
  "name": "Toán 11",
  "grade": 11,
  "icon": "📐",
  "terms": ["Học kì 1", "Học kì 2"],
  "available": true,
  "note": "Chương trình GDPT 2018 (SGK Kết nối tri thức) - Đã hoàn thiện HK1 (750 câu)"
},
"toan12": {
  "name": "Toán 12",
  "grade": 12,
  "icon": "🎓",
  "terms": ["Học kì 1", "Học kì 2"],
  "available": true,
  "note": "Chương trình GDPT 2018 (SGK Kết nối tri thức) - Đã hoàn thiện HK1 (450 câu)"
}
```

**Step 4: Commit**
```bash
git add data/toan11/index.json data/toan12/index.json data/manifest.json
git commit -m "feat(data): scaffold syllabus structure for Toan 11 and Toan 12"
```

---

### Task 2: Soạn lý thuyết 5 chương Toán 11 Học kì 1

**Files:**
- Create: `data/toan11/theory/c1.json`
- Create: `data/toan11/theory/c2.json`
- Create: `data/toan11/theory/c3.json`
- Create: `data/toan11/theory/c4.json`
- Create: `data/toan11/theory/c5.json`

**Step 1: Biên soạn lý thuyết `c1.json` (Hàm số lượng giác và PT lượng giác)**
Góc lượng giác, giá trị lượng giác, công thức lượng giác, hàm số lượng giác, phương trình lượng giác cơ bản ($\sin x = m, \cos x = m, \tan x = m, \cot x = m$).

**Step 2: Biên soạn lý thuyết `c2.json` (Dãy số, Cấp số cộng, Cấp số nhân)**
Khái niệm dãy số, cấp số cộng (công sai, số hạng tổng quát, tổng $n$ số hạng đầu), cấp số nhân (công bội, số hạng tổng quát, tổng $n$ số hạng đầu).

**Step 3: Biên soạn lý thuyết `c3.json` (Số đặc trưng đo xu thế trung tâm mẫu số liệu ghép nhóm)**
Mẫu số liệu ghép nhóm, số trung bình, trung vị, tứ phân vị ($Q_1, Q_2, Q_3$), mốt của mẫu số liệu ghép nhóm.

**Step 4: Biên soạn lý thuyết `c4.json` (Quan hệ song song trong không gian)**
Đường thẳng và mặt phẳng, hai đường thẳng song song, đường thẳng song song với mặt phẳng, hai mặt phẳng song song, phép chiếu song song.

**Step 5: Biên soạn lý thuyết `c5.json` (Giới hạn và Hàm số liên tục)**
Giới hạn của dãy số, giới hạn của hàm số (tại một điểm, tại vô cực, một phía), hàm số liên tục (tại một điểm, trên một khoảng, định lí giá trị trung gian).

**Step 6: Commit**
```bash
git add data/toan11/theory/
git commit -m "feat(toan11): add theory for chapters 1 to 5"
```

---

### Task 3: Soạn lý thuyết 3 chương Toán 12 Học kì 1

**Files:**
- Create: `data/toan12/theory/c1.json`
- Create: `data/toan12/theory/c2.json`
- Create: `data/toan12/theory/c3.json`

**Step 1: Biên soạn lý thuyết `c1.json` (Ứng dụng đạo hàm khảo sát hàm số)**
Tính đơn điệu, cực trị, giá trị lớn nhất và nhỏ nhất, đường tiệm cận (đứng, ngang, xiên), khảo sát và vẽ đồ thị hàm đa thức bậc 3, hàm phân thức bậc nhất/bậc nhất, hàm phân thức bậc hai/bậc nhất.

**Step 2: Biên soạn lý thuyết `c2.json` (Toạ độ vectơ trong không gian)**
Vectơ trong không gian, hệ toạ độ $Oxyz$, toạ độ điểm và vectơ, các phép toán vectơ, tích vô hướng và ứng dụng (khoảng cách, góc).

**Step 3: Biên soạn lý thuyết `c3.json` (Số đặc trưng đo mức độ phân tán mẫu ghép nhóm)**
Khoảng biến thiên, khoảng tứ phân vị, phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm, ý nghĩa thực tiễn.

**Step 4: Commit**
```bash
git add data/toan12/theory/
git commit -m "feat(toan12): add theory for chapters 1 to 3"
```

---

### Task 4: Xây dựng Builder và Sinh ngân hàng câu hỏi Toán 11 HK1 (750 câu)

**Files:**
- Create: `scripts/toan11_builder/__init__.py`
- Create: `scripts/toan11_builder/common.py`
- Create: `scripts/toan11_builder/c1.py`
- Create: `scripts/toan11_builder/c2.py`
- Create: `scripts/toan11_builder/c3.py`
- Create: `scripts/toan11_builder/c4.py`
- Create: `scripts/toan11_builder/c5.py`
- Create: `scripts/gen_bank_toan11_hk1.py`

**Step 1: Viết module builder cho từng chương (c1..c5)**
- Mỗi chương: 24 dạng TN $\times$ 5 biến thể = 120 câu TN (60 NB, 48 TH, 12 VD).
- Mỗi chương: 6 dạng TLN $\times$ 5 biến thể = 30 câu TLN (15 NB, 12 TH, 3 VD).
- Độc lập số liệu, không trùng lặp, lời giải rõ ràng, định dạng chuẩn.

**Step 2: Chạy script sinh ngân hàng câu hỏi**
Run: `python scripts/gen_bank_toan11_hk1.py`  
Expected: Tạo thành công 5 file `scripts/bank/toan11_c1.json` đến `toan11_c5.json` (mỗi file đúng 120 TN và 30 TLN).

**Step 3: Commit**
```bash
git add scripts/toan11_builder/ scripts/gen_bank_toan11_hk1.py scripts/bank/toan11_c*.json
git commit -m "feat(toan11): create question banks for chapters 1-5 (750 questions)"
```

---

### Task 5: Xây dựng Builder và Sinh ngân hàng câu hỏi Toán 12 HK1 (450 câu)

**Files:**
- Create: `scripts/toan12_builder/__init__.py`
- Create: `scripts/toan12_builder/common.py`
- Create: `scripts/toan12_builder/c1.py`
- Create: `scripts/toan12_builder/c2.py`
- Create: `scripts/toan12_builder/c3.py`
- Create: `scripts/gen_bank_toan12_hk1.py`

**Step 1: Viết module builder cho từng chương (c1..c3)**
- Mỗi chương: 24 dạng TN $\times$ 5 biến thể = 120 câu TN (60 NB, 48 TH, 12 VD).
- Mỗi chương: 6 dạng TLN $\times$ 5 biến thể = 30 câu TLN (15 NB, 12 TH, 3 VD).
- Độc lập số liệu, không trùng lặp, lời giải rõ ràng.

**Step 2: Chạy script sinh ngân hàng câu hỏi**
Run: `python scripts/gen_bank_toan12_hk1.py`  
Expected: Tạo thành công 3 file `scripts/bank/toan12_c1.json` đến `toan12_c3.json` (mỗi file đúng 120 TN và 30 TLN).

**Step 3: Commit**
```bash
git add scripts/toan12_builder/ scripts/gen_bank_toan12_hk1.py scripts/bank/toan12_c*.json
git commit -m "feat(toan12): create question banks for chapters 1-3 (450 questions)"
```

---

### Task 6: Cập nhật pipeline `build_data.py` và Lắp ráp toàn bộ dữ liệu

**Files:**
- Modify: `scripts/build_data.py`
- Create/Assemble: `data/toan11/questions/mc.json`
- Create/Assemble: `data/toan11/questions/short.json`
- Create/Assemble: `data/toan12/questions/mc.json`
- Create/Assemble: `data/toan12/questions/short.json`

**Step 1: Cấu hình `CHAPTERS` cho `toan11` và `toan12` trong `build_data.py`**
- `toan11`: `["c1", "c2", "c3", "c4", "c5"]`
- `toan12`: `["c1", "c2", "c3"]`

**Step 2: Chạy lắp ráp dữ liệu chính thức**
Run: `python scripts/build_data.py`  
Expected:
- Ghi thành công 600 TN + 150 TLN cho `toan11`.
- Ghi thành công 360 TN + 90 TLN cho `toan12`.
- Kiểm định schema và tỉ lệ độ khó 50/40/10 thành công 100%.

**Step 3: Commit**
```bash
git add scripts/build_data.py data/toan11/questions/ data/toan12/questions/
git commit -m "feat(data): assemble question banks for Toan 11 and Toan 12"
```

---

### Task 7: Cập nhật Audit chuyên sâu và Kiểm tra 0 lỗi toán học

**Files:**
- Modify: `scripts/audit_banks_deep.py`

**Step 1: Bổ sung `toan11` và `toan12` vào danh sách audit của `scripts/audit_banks_deep.py`**

**Step 2: Chạy kiểm định toàn diện**
Run: `python scripts/audit_banks_deep.py`  
Expected: Tất cả các môn (`toan9`, `toan10`, `toan11`, `toan12`, `ly10`, `hoa10`) đều đạt 0 lỗi toán học, 0 lỗi LaTeX, 0 lỗi trùng lặp phương án.

**Step 3: Commit**
```bash
git add scripts/audit_banks_deep.py
git commit -m "feat(audit): include toan11 and toan12 in deep math auditor"
```

---

### Task 8: Chạy kiểm thử tự động toàn diện (Backend + Frontend)

**Files:**
- Test: `tests/test_audit_static.py`
- Test: `tests/frontend.test.mjs`

**Step 1: Chạy pytest**
Run: `pytest`  
Expected: 7 passed.

**Step 2: Chạy frontend test**
Run: `node tests/frontend.test.mjs`  
Expected: 57 passed.

**Step 3: Chạy build_data kiểm định độc lập**
Run: `python scripts/build_data.py --check`  
Expected: 100% OK cho cả 6 môn trong hệ thống.
