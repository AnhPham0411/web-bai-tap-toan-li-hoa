# Web Bài Tập Toán - Lý - Hóa 10 (GDPT 2018)

Ứng dụng web học lý thuyết và luyện bài tập cho 3 môn **Toán 10**, **Vật lí 10**, **Hóa học 10** theo chương trình GDPT 2018 (bộ sách Kết nối tri thức với cuộc sống, Học kì 1).

Repository: [https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa](https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa)

## Quy mô Dữ liệu (2.250 câu hỏi)

- **Mỗi môn 5 chương**, mỗi chương bao gồm **150 câu hỏi** (120 Trắc nghiệm + 30 Trả lời ngắn).
- **Phân bổ độ khó chuẩn:** 50% Nhận biết (`nb`), 40% Thông hiểu (`th`), 10% Vận dụng (`vd`).
- **Tổng cộng toàn hệ thống:** **2.250 câu hỏi** (1.800 câu Trắc nghiệm + 450 câu Trả lời ngắn).
- **100% câu hỏi** đều có đáp án chính xác và lời giải chi tiết (`explanation`).

| Môn học | Số chương | Trắc nghiệm | Trả lời ngắn | Tổng câu hỏi |
|---|---|---|---|---|
| **Toán 10** | 5 chương | 600 câu | 150 câu | **750 câu** |
| **Vật lí 10** | 5 chương | 600 câu | 150 câu | **750 câu** |
| **Hóa học 10** | 5 chương | 600 câu | 150 câu | **750 câu** |
| **TỔNG** | **15 chương** | **1.800 câu** | **450 câu** | **2.250 câu** |

---

## Chạy dự án cục bộ

Mở trực tiếp `index.html` qua trình duyệt sẽ bị chặn do giao diện đọc JSON bằng `fetch`. Vui lòng chạy qua web server:

```bash
# Cách 1: Chạy bằng Python (khuyên dùng)
python -m http.server 8080

# Cách 2: Chạy bằng Node.js (nếu có npx)
npx serve

# Cách 3: Nháy đúp file start.bat (trên Windows)
```
Sau đó mở trình duyệt truy cập: `http://localhost:8080`

---

## Tính năng nổi bật

- **Chuyển đổi môn học linh hoạt:** Dropdown chọn nhanh giữa Toán 10, Vật lí 10, Hóa học 10 ngay trên thanh tiêu đề.
- **Render công thức khoa học:** Tự động hiển thị công thức LaTeX, phân số, căn thức, vectơ, đơn vị đo vật lí và công thức hóa học qua engine `assets/js/math.js`.
- **Luyện tập đa dạng:** Chọn bài theo môn, theo chương, chọn độ khó, lọc câu sai, làm lại đề.
- **Lưu tiến độ tự động:** Lưu vết chế độ sáng/tối (Dark mode), môn học đang chọn, và lịch sử chấm điểm trong `localStorage`.

---

## Sinh/Cập nhật dữ liệu tự động

Để tái tạo hoặc cập nhật 2.250 câu hỏi:
```bash
python scripts/generate_all.py
```
Script sẽ tự động kiểm tra cú pháp JSON, escape ký tự LaTeX chuẩn xác và ghi vào các thư mục `data/toan10`, `data/ly10`, `data/hoa10`.

---

## Deploy Vercel

Dự án sử dụng cấu hình tĩnh với `vercel.json`. Khi push code lên nhánh `main` của kho chứa GitHub `AnhPham0411/web-bai-tap-toan-li-hoa`, Vercel sẽ tự động build & deploy lại trang web giữ nguyên domain/project hiện tại.
