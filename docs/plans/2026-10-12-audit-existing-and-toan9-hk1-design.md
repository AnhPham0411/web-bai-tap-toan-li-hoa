# Thiết kế: Audit Hệ thống & Xây dựng Toán 9 Học kì 1 (GDPT 2018)

**Ngày lập:** 2026-10-12  
**Tác giả:** Antigravity  
**Mục tiêu:** Rà soát và kiểm định chuyên sâu chất lượng nội dung toán học các bộ đề hiện có (Toán 10, Vật lí 10, Hóa học 10), đồng thời biên soạn lý thuyết và 750 câu hỏi chuẩn (150 câu/chương: 120 TN + 30 TLN) cho 5 chương Toán 9 Học kì 1 theo SGK Kết nối tri thức với cuộc sống (GDPT 2018).

---

## 1. Bối cảnh & Yêu cầu

1. **Yêu cầu kiểm định ("test lại"):**
   - Rà soát toàn bộ ngân hàng câu hỏi để phát hiện và xử lý triệt để các lỗi về:
     - Sai lệch đáp án trắc nghiệm hoặc đáp án không duy nhất.
     - Sai số hoặc không chuẩn trong câu hỏi trả lời ngắn (chỉ nhận số nguyên hoặc số chuẩn, không làm tròn mập mờ).
     - Lỗi cú pháp LaTeX không được engine tự chế `math.js` hỗ trợ (`\begin{cases}`, `\dots`, escape không hợp lệ).
     - Lỗi mâu thuẫn giữa câu hỏi và lời giải chi tiết.
2. **Yêu cầu mở rộng Toán 9 ("làm tiếp đề lớp 9"):**
   - Triển khai trọn vẹn Học kì 1 cho môn Toán 9 gồm 5 chương đầu:
     - Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn
     - Chương II: Phương trình và bất phương trình bậc nhất một ẩn
     - Chương III: Căn bậc hai và căn bậc ba
     - Chương IV: Hệ thức lượng trong tam giác vuông
     - Chương V: Đường tròn
   - Quy mô: Mỗi chương gồm đúng 150 câu hỏi (120 câu Trắc nghiệm + 30 câu Trả lời ngắn), tổng cộng 750 câu hỏi tự khép kín, phân loại độ khó chuẩn 50% NB / 40% TH / 10% VD, tối đa 5 biến thể/dạng bài.
   - Biên soạn 5 file lý thuyết chi tiết theo SGK GDPT 2018 Kết nối tri thức.

---

## 2. Kiến trúc & Giải pháp kỹ thuật

### 2.1. Bộ công cụ Audit Chuyên sâu (`scripts/audit_banks_deep.py`)
Kiểm tra 4 tầng tự động:
1. **Tầng cú pháp & LaTeX:** Phân tích cú pháp chuỗi của `question`, `choices`, `explanation`, phát hiện các lệnh TeX lạ hoặc lỗi định dạng.
2. **Tầng phương án trắc nghiệm:** Kiểm tra 4 phương án độc lập toán học (không trùng giá trị), chỉ số `answer` hợp lệ trong $[0, 3]$, và lời giải khớp với đáp án.
3. **Tầng trả lời ngắn:** Đảm bảo `answer` là số nguyên hoặc số thập phân chuẩn xác, không chia cho 0, không căn bậc hai của số âm.
4. **Tầng báo cáo & Sửa tự động:** Báo cáo chi tiết các câu có vấn đề và hỗ trợ vá dữ liệu trực tiếp trong `scripts/bank/`.

### 2.2. Generator Toán 9 HK1 (`scripts/gen_bank_toan9_hk1.py`)
- Xây dựng 5 module tạo ngân hàng câu hỏi cho 5 chương:
  - `toan9_c1`: 24 dạng TN (5 câu/dạng = 120 câu) + 6 dạng TLN (5 câu/dạng = 30 câu).
  - `toan9_c2`: 24 dạng TN + 6 dạng TLN.
  - `toan9_c3`: 24 dạng TN + 6 dạng TLN.
  - `toan9_c4`: 24 dạng TN + 6 dạng TLN.
  - `toan9_c5`: 24 dạng TN + 6 dạng TLN.
- Tất cả bài toán đều tự khép kín, đề bài sinh ngẫu nhiên số liệu đẹp, không câu nào trùng đề bài theo bộ lọc `norm_key` của `build_data.py`.

### 2.3. Pipeline & Cấu trúc Dữ liệu
- `scripts/bank/toan9_c1.json` .. `toan9_c5.json`: Lưu trữ ngân hàng nguồn của từng chương.
- `scripts/build_data.py`: Cập nhật cấu hình để lắp ráp `data/toan9/questions/mc.json` (600 câu) và `data/toan9/questions/short.json` (150 câu).
- `data/toan9/theory/c1.json` .. `c5.json`: 5 file lý thuyết chứa đầy đủ định nghĩa, định lí, công thức, ví dụ minh họa và chú ý.
- `data/toan9/index.json`: Mục lục 10 chương (với 5 chương HK1 có sẵn dữ liệu và 5 chương HK2 giữ khung định hướng).
- `data/manifest.json`: Chuyển `available: true` cho Toán 9.

### 2.4. Trải nghiệm người dùng (Web SPA)
- Header selector `#subject-select` tải động `toan9` với đầy đủ tính năng.
- Trang chủ hiển thị số liệu thống kê: 5 chương, 750 câu hỏi, 16 bài lý thuyết.
- Hỗ trợ đầy đủ bộ lọc học kì và luyện tập từng chương hoặc đề thi tổng hợp.

---

## 3. Tiêu chí Nghiệm thu (Success Criteria)

1. Script `audit_banks_deep.py` chạy qua tất cả ngân hàng câu hỏi hiện có và báo cáo 0 lỗi nghiêm trọng.
2. `python scripts/build_data.py --check` vượt qua 100% với 0 lỗi, 0 cảnh báo cho cả 4 môn (`toan10`, `ly10`, `hoa10`, `toan9`).
3. Ngân hàng câu hỏi Toán 9 HK1 đạt đủ 750 câu (600 TN + 150 TLN), tỷ lệ 50/40/10 chuẩn mực.
4. Toàn bộ test tự động (`pytest` và `frontend.test.mjs`) đều pass.
5. Giao diện web hiển thị chuẩn đẹp, làm bài và chấm điểm chính xác 100%.
