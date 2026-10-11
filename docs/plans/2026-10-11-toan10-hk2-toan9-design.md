# Thiết kế Hệ thống: Mở rộng Toán 10 Kì 2 và Toán 9 (GDPT 2018)

**Ngày lập:** 2026-10-11  
**Tác giả:** Antigravity AI Assistant & AnhPham0411  
**Trạng thái:** Đã phê duyệt (Approved)

---

## 1. Bối cảnh & Mục tiêu

Dự án hiện đã hoàn thiện trọn vẹn Học kì 1 cho 3 môn **Toán 10**, **Vật lí 10**, **Hóa học 10** theo chương trình GDPT 2018 (bộ sách Kết nối tri thức với cuộc sống), bao gồm 2.250 câu hỏi trắc nghiệm và trả lời ngắn được kiểm định tự động bằng `scripts/build_data.py`.

Mục tiêu giai đoạn mới:
1. Mở rộng môn **Toán 10** sang trọn vẹn cả năm bằng cách bổ sung **Học kì 2** (Chương VI đến IX, thêm 600 câu hỏi: 480 trắc nghiệm + 120 trả lời ngắn).
2. Nâng cấp cấu trúc dữ liệu (`manifest.json`, `index.json`) và giao diện Web SPA để hỗ trợ phân cấp môn học theo học kì và khối lớp.
3. Chuẩn bị kiến trúc và lộ trình cho môn **Toán 9** theo chương trình GDPT 2018 mới.

---

## 2. Phạm vi Dữ liệu Toán 10 Kì 2 (600 câu hỏi)

Bám sát bộ sách **Kết nối tri thức với cuộc sống — Toán 10 (Tập 2)**, bao gồm 4 chương:

| Mã | Tên chương | Các bài học | Số câu hỏi |
|---|---|---|---|
| `c6` | **Chương VI: Hàm số, đồ thị và ứng dụng** | Bài 15 (Hàm số), Bài 16 (Hàm số bậc hai), Bài 17 (Dấu tam thức bậc hai), Bài 18 (Phương trình quy về bậc hai) | 120 TN + 30 TLN = 150 câu |
| `c7` | **Chương VII: Phương pháp toạ độ trong mặt phẳng** | Bài 19 (Phương trình đường thẳng), Bài 20 (Vị trí tương đối, góc, khoảng cách), Bài 21 (Đường tròn trong Oxy), Bài 22 (Ba đường conic) | 120 TN + 30 TLN = 150 câu |
| `c8` | **Chương VIII: Đại số tổ hợp** | Bài 23 (Quy tắc đếm), Bài 24 (Hoán vị, chỉnh hợp, tổ hợp), Bài 25 (Nhị thức Newton) | 120 TN + 30 TLN = 150 câu |
| `c9` | **Chương IX: Tính xác suất theo định nghĩa cổ điển** | Bài 26 (Biến cố và định nghĩa cổ điển), Bài 27 (Thực hành tính xác suất) | 120 TN + 30 TLN = 150 câu |

### Quy chuẩn Chất lượng:
- **Tỉ lệ phân bổ độ khó**: 
  - Trắc nghiệm (120 câu/chương): 60 Nhận biết (`nb`), 48 Thông hiểu (`th`), 12 Vận dụng (`vd`).
  - Trả lời ngắn (30 câu/chương): 15 Nhận biết (`nb`), 12 Thông hiểu (`th`), 3 Vận dụng (`vd`).
- **Giới hạn biến thể**: Mỗi dạng bài (`dang`) tối đa 5 biến thể, các biến thể độc lập số liệu và đáp số.
- **Tính tự khép kín**: 100% câu hỏi có lời giải chi tiết (`explanation`), không tham chiếu hình ảnh ngoài.
- **Chuẩn hóa SGK**: Biểu thức toán học dùng cú pháp LaTeX được `assets/js/math.js` hỗ trợ; dấu số thập phân dùng dấu phẩy kiểu Việt Nam; câu trả lời ngắn có trường `tolerance` cho số làm tròn.

---

## 3. Kiến trúc Dữ liệu & UI

### 3.1. Dữ liệu
- Môn `toan10` sẽ tích hợp liền mạch toàn bộ 9 chương (c1 đến c9).
- `data/toan10/index.json`: Bổ sung thuộc tính `"term": 1` cho chương 1–5 và `"term": 2` cho chương 6–9.
- Thư mục ngân hàng nguồn: `scripts/bank/toan10_c6.json` đến `toan10_c9.json`.
- Thư mục lý thuyết: `data/toan10/theory/c6.json` đến `c9.json`.
- Đăng ký môn `toan9` trong `data/manifest.json`.

### 3.2. Giao diện Web
- Cập nhật `#subject-select` trên thanh Header để tự động sinh từ `manifest.json`.
- Trang chủ và màn hình Luyện tập bổ sung bộ lọc học kì: `[ Tất cả chương ]`, `[ Học kì 1 ]`, `[ Học kì 2 ]`.

---

## 4. Công cụ Xây dựng & Kiểm định

Cập nhật `scripts/build_data.py`:
- Cấu hình danh sách chương linh hoạt: `toan10` hỗ trợ `c1`..`c9`.
- Tự động kiểm định và lắp ráp dữ liệu ra `data/toan10/questions/mc.json` (1.080 câu) và `short.json` (270 câu).
- Đảm bảo lệnh `python scripts/build_data.py --check` đạt chuẩn 100% không có lỗi.

---

## 5. Lộ trình Toán 9

Sau khi hoàn thành và xác minh toàn bộ Toán 10 Kì 2:
- Khởi tạo thư mục `data/toan9/` và các file ngân hàng `scripts/bank/toan9_*.json`.
- Thiết kế 10 chương bám sát SGK Toán 9 (Kết nối tri thức): Phương trình, Hệ phương trình, Bất đẳng thức, Căn thức, Hệ thức lượng, Đường tròn, Hàm số bậc hai, Thống kê, Xác suất, Hình không gian.
