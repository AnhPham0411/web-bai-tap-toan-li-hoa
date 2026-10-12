# Bản thiết kế chi tiết: Mở rộng Học kì 2 cho Toán 11 và Toán 12 (GDPT 2018)

- **Ngày lập**: 12/10/2026
- **Tác giả**: Antigravity Pair Programmer
- **Mục tiêu**: Xây dựng trọn vẹn Học kì 2 cho hai môn Toán 11 và Toán 12 theo chương trình SGK Kết nối tri thức với cuộc sống (GDPT 2018), đưa Toán 11 và Toán 12 thành các môn học trọn gói cả năm (tương tự như mô hình Toán 10).

---

## 1. Mục tiêu & Phạm vi phát triển

### 1.1. Toán 11 - Học kì 2 (4 chương, 15 bài học, 600 câu hỏi)
- **Chương VI. Hàm số mũ và hàm số lôgarit** (150 câu: 120 TN + 30 TLN)
  - Bài 18: Lũy thừa với số mũ thực
  - Bài 19: Lôgarit
  - Bài 20: Hàm số mũ và hàm số lôgarit
  - Bài 21: Phương trình, bất phương trình mũ và lôgarit
- **Chương VII. Quan hệ vuông góc trong không gian** (150 câu: 120 TN + 30 TLN)
  - Bài 22: Hai đường thẳng vuông góc
  - Bài 23: Đường thẳng vuông góc với mặt phẳng
  - Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng
  - Bài 25: Hai mặt phẳng vuông góc
  - Bài 26: Khoảng cách
  - Bài 27: Thể tích
- **Chương VIII. Các quy tắc tính đạo hàm** (150 câu: 120 TN + 30 TLN)
  - Bài 28: Định nghĩa và ý nghĩa của đạo hàm
  - Bài 29: Các quy tắc tính đạo hàm
  - Bài 30: Đạo hàm cấp hai
- **Chương IX. Các quy tắc tính xác suất** (150 câu: 120 TN + 30 TLN)
  - Bài 31: Biến cố giao và quy tắc nhân xác suất
  - Bài 32: Biến cố hợp và quy tắc cộng xác suất

*Sau khi bổ sung*: Toán 11 trọn vẹn cả năm có **9 chương**, **32 bài lý thuyết**, **1.350 câu hỏi** (1.080 TN + 270 TLN).

---

### 1.2. Toán 12 - Học kì 2 (3 chương, 9 bài học, 450 câu hỏi)
- **Chương IV. Nguyên hàm và tích phân** (150 câu: 120 TN + 30 TLN)
  - Bài 11: Nguyên hàm
  - Bài 12: Tích phân
  - Bài 13: Ứng dụng hình học của tích phân (Diện tích hình phẳng, thể tích khối tròn xoay)
- **Chương V. Phương pháp toạ độ trong không gian** (150 câu: 120 TN + 30 TLN)
  - Bài 14: Phương trình mặt phẳng
  - Bài 15: Phương trình đường thẳng trong không gian
  - Bài 16: Công thức tính góc và khoảng cách trong không gian
  - Bài 17: Phương trình mặt cầu
- **Chương VI. Xác suất có điều kiện** (150 câu: 120 TN + 30 TLN)
  - Bài 18: Xác suất có điều kiện
  - Bài 19: Công thức xác suất toàn phần và công thức Bayes

*Sau khi bổ sung*: Toán 12 trọn vẹn cả năm có **6 chương**, **19 bài lý thuyết**, **900 câu hỏi** (720 TN + 180 TLN).

---

### 1.3. Thống kê toàn hệ thống sau khi hoàn thành
- Tổng số môn: 6 môn học (Toán 9, Toán 10, Toán 11, Toán 12, Vật lí 10, Hóa học 10).
- Tổng số bài lý thuyết: 91 + 24 = **115 bài học**.
- Tổng ngân hàng câu hỏi: 4.800 + 1.050 = **5.850 câu hỏi**.

---

## 2. Kiến trúc & Tích hợp giao diện

1. **Cấu trúc môn học trọn gói (Full-year Bundle)**:
   - Các chương HK2 được gán `"term": 2` trong `index.json`.
   - Giao diện `assets/js/views/home.js` và `practice.js` tự động nhận diện `hasTerms = true` và kích hoạt thanh lọc:
     `[Tất cả các chương | Học kì 1 | Học kì 2]`.
2. **Cập nhật Manifest (`data/manifest.json`)**:
   - Chuyển `toan11` và `toan12` thành `"term": "Cả năm (Học kì 1 & 2)"`.
   - Gỡ bỏ mục dự kiến `toan11_hk2` và `toan12_hk2` khỏi danh sách sắp có (chỉ còn giữ lại `ly11` và `hoa11`).
3. **Quy chuẩn chất lượng sư phạm**:
   - Mỗi chương có đúng 120 câu Trắc nghiệm (4 phương án, 1 đáp án đúng duy nhất, có giải thích).
   - Mỗi chương có đúng 30 câu Trả lời ngắn (điền đáp số nguyên, phân số hoặc số thập phân).
   - Phân bổ đều theo 3 mức độ nhận thức: Nhận biết (40%), Thông hiểu (40%), Vận dụng (20%).
   - Kiểm định tự động: 0 lỗi LaTeX, 0 trùng lặp ID, 100% câu hỏi có lời giải.

---

## 3. Kế hoạch triển khai (Implementation Stages)

- **Giai đoạn 1**: Sinh dữ liệu Lý thuyết chuẩn GDPT 2018 cho 4 chương Toán 11 HK2 (`c6.json` đến `c9.json`) và 3 chương Toán 12 HK2 (`c4.json` đến `c6.json`).
- **Giai đoạn 2**: Sinh ngân hàng 600 bài tập cho Toán 11 HK2 và 450 bài tập cho Toán 12 HK2 (kèm kiểm định toán học tự động).
- **Giai đoạn 3**: Hợp nhất vào `data/toan11/index.json`, `data/toan12/index.json` và bộ câu hỏi `mc.json`, `short.json`.
- **Giai đoạn 4**: Kiểm thử toàn diện (`super_deep_audit`, `frontend.test.mjs`, `verify_all_theory_renders`, `verify_all_questions_grading`).
- **Giai đoạn 5**: Triển khai lên Vercel Production và kiểm tra live.
