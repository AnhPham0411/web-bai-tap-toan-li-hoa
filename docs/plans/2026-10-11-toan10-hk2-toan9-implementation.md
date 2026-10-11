# Kế hoạch Triển khai: Mở rộng Toán 10 Kì 2 và Nền móng Toán 9

> **For Antigravity:** REQUIRED SUB-SKILL: Load executing-plans to implement this plan task-by-task.

**Goal:** Xây dựng và tích hợp hoàn chỉnh 600 câu hỏi (120 TN + 30 TLN/chương) kèm lý thuyết cho 4 chương Toán 10 Kì 2 (SGK Kết nối tri thức), nâng cấp hệ thống web với bộ lọc học kì, và thiết lập cấu trúc nền tảng cho môn Toán 9.

**Architecture:** Sử dụng pipeline `scripts/bank/` -> `scripts/build_data.py` -> `data/` với bộ kiểm định chất lượng nghiêm ngặt (tỉ lệ độ khó 50/40/10, <= 5 biến thể/dạng, LaTeX chuẩn). Nâng cấp giao diện Web SPA để tải danh sách môn động và cho phép lọc bài học theo Học kì 1 / Học kì 2 / Cả năm mà không gây ảnh hưởng đến dữ liệu cũ.

**Tech Stack:** Python 3 (cho script kiểm định & assemble ngân hàng câu hỏi), Vanilla HTML5/CSS3/JavaScript ES Modules (cho web SPA).

---

### Task 1: Nâng cấp `scripts/build_data.py` hỗ trợ linh hoạt số chương theo từng môn

**Files:**
- Modify: `scripts/build_data.py:25-35`

**Step 1: Cập nhật cấu hình môn học và chương**
Thay đổi cấu hình `CHAPTERS` cố định toàn cục thành cấu hình linh hoạt theo từng môn học trong `scripts/build_data.py`:
- `toan10`: `["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"]`
- `ly10`: `["c1", "c2", "c3", "c4", "c5"]`
- `hoa10`: `["c1", "c2", "c3", "c4", "c5"]`
- Hỗ trợ cờ bỏ qua chương chưa tạo file bank khi đang ở chế độ dev/check.

**Step 2: Chạy kiểm tra đảm bảo tương thích ngược**
Run: `python scripts/build_data.py --check`  
Expected: KIEM DINH toan10, ly10, hoa10: OK - chi kiem dinh, khong ghi file.

**Step 3: Commit**
```bash
git add scripts/build_data.py
git commit -m "refactor(build_data): support dynamic chapter lists per subject"
```

---

### Task 2: Cập nhật `data/manifest.json` và cấu trúc `data/toan10/index.json`

**Files:**
- Modify: `data/manifest.json`
- Modify: `data/toan10/index.json`

**Step 1: Cập nhật `data/toan10/index.json`**
- Thêm thuộc tính `"term": 1` cho các chương c1 đến c5.
- Khai báo thêm 4 chương mới cho Học kì 2 (`"term": 2`):
  - `c6`: "Hàm số, đồ thị và ứng dụng" (Bài 15, 16, 17, 18), `theory`: "theory/c6.json"
  - `c7`: "Phương pháp toạ độ trong mặt phẳng" (Bài 19, 20, 21, 22), `theory`: "theory/c7.json"
  - `c8`: "Đại số tổ hợp" (Bài 23, 24, 25), `theory`: "theory/c8.json"
  - `c9`: "Tính xác suất theo định nghĩa cổ điển" (Bài 26, 27), `theory`: "theory/c9.json"

**Step 2: Cập nhật `data/manifest.json`**
- Đổi tiêu đề Toán 10 thành cả năm, cập nhật `terms: ["Học kì 1", "Học kì 2"]`.
- Khai báo môn `toan9` (Toán 9 GDPT 2018).

**Step 3: Commit**
```bash
git add data/manifest.json data/toan10/index.json
git commit -m "feat(data): declare chapters 6-9 in toan10 and add toan9 to manifest"
```

---

### Task 3: Biên soạn nội dung lý thuyết cho 4 chương Toán 10 Kì 2

**Files:**
- Create: `data/toan10/theory/c6.json`
- Create: `data/toan10/theory/c7.json`
- Create: `data/toan10/theory/c8.json`
- Create: `data/toan10/theory/c9.json`

**Step 1: Biên soạn `data/toan10/theory/c6.json`**
Tóm tắt lý thuyết trọng tâm 4 bài: Hàm số, Hàm số bậc hai, Dấu tam thức bậc hai, Phương trình quy về bậc hai (công thức, điều kiện, dạng đồ thị parabol).

**Step 2: Biên soạn `data/toan10/theory/c7.json`**
Tóm tắt lý thuyết trọng tâm 4 bài: Phương trình đường thẳng, Vị trí tương đối & góc & khoảng cách, Phương trình đường tròn, Ba đường conic (elip, hypebol, parabol).

**Step 3: Biên soạn `data/toan10/theory/c8.json`**
Tóm tắt lý thuyết trọng tâm 3 bài: Quy tắc cộng & quy tắc nhân, Hoán vị - Chỉnh hợp - Tổ hợp, Nhị thức Newton bậc 4 và 5.

**Step 4: Biên soạn `data/toan10/theory/c9.json`**
Tóm tắt lý thuyết trọng tâm 2 bài: Biến cố & định nghĩa cổ điển của xác suất, Thực hành tính xác suất (dùng sơ đồ hình cây và đại số tổ hợp).

**Step 5: Commit**
```bash
git add data/toan10/theory/c6.json data/toan10/theory/c7.json data/toan10/theory/c8.json data/toan10/theory/c9.json
git commit -m "feat(toan10): add theory for chapters 6, 7, 8, 9"
```

---

### Task 4: Xây dựng Ngân hàng câu hỏi Chương VI: Hàm số, đồ thị và ứng dụng (`toan10_c6.json`)

**Files:**
- Create: `scripts/bank/toan10_c6.json`

**Step 1: Biên soạn 150 câu hỏi chuẩn GDPT 2018**
- 120 câu Trắc nghiệm: 60 Nhận biết, 48 Thông hiểu, 12 Vận dụng.
- 30 câu Trả lời ngắn: 15 Nhận biết, 12 Thông hiểu, 3 Vận dụng.
- Bao phủ đầy đủ 4 bài: TXĐ hàm số, đồng biến/nghịch biến, đỉnh và trục đối xứng parabol, dấu tam thức, bất phương trình bậc hai, phương trình chứa căn $\sqrt{f(x)}=\sqrt{g(x)}$ và $\sqrt{f(x)}=g(x)$.
- Tối đa 5 biến thể/dạng bài, số liệu độc lập, lời giải chi tiết.

**Step 2: Kiểm định chất lượng**
Run: `python scripts/build_data.py --check`  
Expected: Chương 6 toan10 đạt chuẩn và không có lỗi LaTeX / phân bổ độ khó.

**Step 3: Commit**
```bash
git add scripts/bank/toan10_c6.json
git commit -m "feat(toan10): add question bank for chapter 6"
```

---

### Task 5: Xây dựng Ngân hàng câu hỏi Chương VII: Phương pháp toạ độ trong mặt phẳng (`toan10_c7.json`)

**Files:**
- Create: `scripts/bank/toan10_c7.json`

**Step 1: Biên soạn 150 câu hỏi chuẩn GDPT 2018**
- 120 câu Trắc nghiệm: 60 Nhận biết, 48 Thông hiểu, 12 Vận dụng.
- 30 câu Trả lời ngắn: 15 Nhận biết, 12 Thông hiểu, 3 Vận dụng.
- Bao phủ đầy đủ 4 bài: VTCP, VTPT, phương trình tham số & tổng quát đường thẳng; góc giữa hai đường thẳng; khoảng cách từ điểm đến đường thẳng; phương trình đường tròn, tiếp tuyến đường tròn; phương trình chính tắc của elip, hypebol, parabol.

**Step 2: Kiểm định chất lượng**
Run: `python scripts/build_data.py --check`  
Expected: Chương 7 toan10 đạt chuẩn và không có lỗi.

**Step 3: Commit**
```bash
git add scripts/bank/toan10_c7.json
git commit -m "feat(toan10): add question bank for chapter 7"
```

---

### Task 6: Xây dựng Ngân hàng câu hỏi Chương VIII: Đại số tổ hợp (`toan10_c8.json`)

**Files:**
- Create: `scripts/bank/toan10_c8.json`

**Step 1: Biên soạn 150 câu hỏi chuẩn GDPT 2018**
- 120 câu Trắc nghiệm: 60 Nhận biết, 48 Thông hiểu, 12 Vận dụng.
- 30 câu Trả lời ngắn: 15 Nhận biết, 12 Thông hiểu, 3 Vận dụng.
- Bao phủ đầy đủ 3 bài: Quy tắc cộng, quy tắc nhân, sơ đồ cây; hoán vị $P_n$, chỉnh hợp $A_n^k$, tổ hợp $C_n^k$; khai triển nhị thức Newton $(a+b)^4, (a+b)^5$ và hệ số số hạng.

**Step 2: Kiểm định chất lượng**
Run: `python scripts/build_data.py --check`  
Expected: Chương 8 toan10 đạt chuẩn và không có lỗi.

**Step 3: Commit**
```bash
git add scripts/bank/toan10_c8.json
git commit -m "feat(toan10): add question bank for chapter 8"
```

---

### Task 7: Xây dựng Ngân hàng câu hỏi Chương IX: Tính xác suất theo định nghĩa cổ điển (`toan10_c9.json`)

**Files:**
- Create: `scripts/bank/toan10_c9.json`

**Step 1: Biên soạn 150 câu hỏi chuẩn GDPT 2018**
- 120 câu Trắc nghiệm: 60 Nhận biết, 48 Thông hiểu, 12 Vận dụng.
- 30 câu Trả lời ngắn: 15 Nhận biết, 12 Thông hiểu, 3 Vận dụng.
- Bao phủ đầy đủ 2 bài: Không gian mẫu, biến cố, biến cố đối; tính xác suất cổ điển $P(A) = \frac{n(A)}{n(\Omega)}$ kết hợp kỹ thuật đếm tổ hợp và xác suất hình học/sơ đồ.

**Step 2: Kiểm định chất lượng**
Run: `python scripts/build_data.py --check`  
Expected: Chương 9 toan10 đạt chuẩn và không có lỗi.

**Step 3: Commit**
```bash
git add scripts/bank/toan10_c9.json
git commit -m "feat(toan10): add question bank for chapter 9"
```

---

### Task 8: Lắp ráp toàn bộ dữ liệu Toán 10 và Kiểm định tổng thể

**Files:**
- Modify: `data/toan10/questions/mc.json`
- Modify: `data/toan10/questions/short.json`

**Step 1: Chạy build dữ liệu chính thức**
Run: `python scripts/build_data.py`  
Expected:
- Ghi thành công `data/toan10/questions/mc.json` (1.080 câu hỏi trắc nghiệm).
- Ghi thành công `data/toan10/questions/short.json` (270 câu hỏi trả lời ngắn).
- Tất cả 3 môn `toan10`, `ly10`, `hoa10` đều hợp lệ 100%.

**Step 2: Chạy kiểm định độc lập**
Run: `python scripts/build_data.py --check`  
Expected: Exit code 0, không có bất kỳ cảnh báo nào.

**Step 3: Commit**
```bash
git add data/toan10/questions/mc.json data/toan10/questions/short.json
git commit -m "feat(toan10): assemble full 1350 questions for grade 10 math"
```

---

### Task 9: Nâng cấp Giao diện Web (Bộ lọc Học kì & Chọn môn động)

**Files:**
- Modify: `assets/js/app.js`
- Modify: `assets/js/views/home.js`
- Modify: `assets/js/views/practice.js`
- Modify: `assets/css/style.css`

**Step 1: Nạp danh sách môn học tự động từ `manifest.json`**
Đảm bảo dropdown `#subject-select` được render động theo danh mục môn có trong manifest thay vì chỉ có 3 môn cố định trong HTML.

**Step 2: Bổ sung bộ lọc học kì trên UI**
Thêm tab chuyển đổi: `[ Tất cả ]`, `[ Học kì 1 ]`, `[ Học kì 2 ]` tại Trang chủ và trang Luyện tập. Khi bấm chọn học kì, danh sách chương hiển thị tương ứng (`c1..c5` cho HK1, `c6..c9` cho HK2).

**Step 3: Kiểm thử giao diện web**
Kiểm tra router, hiển thị lý thuyết, luyện tập trắc nghiệm và trả lời ngắn cho các chương mới.

**Step 4: Commit**
```bash
git add assets/js/ assets/css/
git commit -m "feat(ui): add semester filter and dynamic subject selector"
```

---

### Task 10: Khởi tạo Khung dữ liệu cho môn Toán 9 (GDPT 2018)

**Files:**
- Create: `data/toan9/index.json`
- Create: `data/toan9/theory/.gitkeep`

**Step 1: Xây dựng cấu trúc mục lục chuẩn 10 chương cho Toán 9 KNTT**
- Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn
- Chương II: Phương trình và bất phương trình bậc nhất một ẩn
- Chương III: Căn bậc hai và căn bậc ba
- Chương IV: Hệ thức lượng trong tam giác vuông
- Chương V: Đường tròn
- Chương VI: Hàm số $y = ax^2$ ($a \neq 0$). Phương trình bậc hai một ẩn
- Chương VII: Tần số và tần số tương đối
- Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản
- Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp
- Chương X: Một số hình khối trong thực tiễn

**Step 2: Đăng ký sẵn sàng trong hệ thống**
Đảm bảo khi chọn "Toán 9" trên web, khung mục lục và lý thuyết hiển thị chuẩn xác, sẵn sàng cho việc nạp ngân hàng câu hỏi.

**Step 3: Commit**
```bash
git add data/toan9/
git commit -m "feat(toan9): scaffold structure for Grade 9 Math (GDPT 2018)"
```
