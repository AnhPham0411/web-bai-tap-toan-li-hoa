# Thiết kế Kiến trúc: Mở rộng Toán 11 và Toán 12 (Học kì 1)

> **Ngày lập:** 2026-10-12  
> **Trạng thái:** Đã phê duyệt (Approved)  
> **Mục tiêu:** Xây dựng cấu trúc danh mục cả năm, nội dung lý thuyết trọng tâm và ngân hàng 1.200 câu hỏi (960 TN + 240 TLN) cho Học kì 1 của hai khối lớp Toán 11 và Toán 12 theo chương trình GDPT 2018 (SGK Kết nối tri thức).

---

## 1. Bối cảnh & Mục tiêu

Hệ thống hiện tại đã hỗ trợ hoàn chỉnh:
- **Toán 10**: Cả năm (9 chương, 1.350 câu hỏi).
- **Vật lí 10**: HK1 (5 chương, 750 câu hỏi).
- **Hoá học 10**: HK1 (5 chương, 750 câu hỏi).
- **Toán 9**: HK1 (5 chương, 750 câu hỏi).

Yêu cầu tiếp theo là mở rộng hệ sinh thái sang hai khối lớp cấp THPT còn lại: **Toán 11** và **Toán 12**.

### Phạm vi giai đoạn này
1. **Khung mục lục cả năm**:
   - `toan11`: 9 chương (Chương 1-5 thuộc HK1, Chương 6-9 thuộc HK2).
   - `toan12`: 6 chương (Chương 1-3 thuộc HK1, Chương 4-6 thuộc HK2).
2. **Lý thuyết trọng tâm Học kì 1**:
   - Toán 11: 5 file lý thuyết `c1.json` đến `c5.json`.
   - Toán 12: 3 file lý thuyết `c1.json` đến `c3.json`.
3. **Ngân hàng câu hỏi Học kì 1 (150 câu/chương)**:
   - **Toán 11 HK1 (5 chương)**: 750 câu (600 TN + 150 TLN).
     - Chương I: Hàm số lượng giác và phương trình lượng giác.
     - Chương II: Dãy số. Cấp số cộng và cấp số nhân.
     - Chương III: Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm.
     - Chương IV: Quan hệ song song trong không gian.
     - Chương V: Giới hạn. Hàm số liên tục.
   - **Toán 12 HK1 (3 chương)**: 450 câu (360 TN + 90 TLN).
     - Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số.
     - Chương II: Toạ độ vectơ trong không gian.
     - Chương III: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm.
4. **Tổng khối lượng câu hỏi mới**: **1.200 câu hỏi** (960 TN + 240 TLN).

---

## 2. Tiêu chuẩn Kỹ thuật & Chất lượng Câu hỏi

Tất cả câu hỏi tuân thủ nghiêm ngặt chuẩn kiến thức GDPT 2018:
1. **Phân bổ độ khó chuẩn 50 / 40 / 10**:
   - Mỗi chương 120 câu Trắc nghiệm: 60 Nhận biết (50%), 48 Thông hiểu (40%), 12 Vận dụng (10%). Gồm 24 dạng bài $\times$ 5 biến thể.
   - Mỗi chương 30 câu Trả lời ngắn: 15 Nhận biết (50%), 12 Thông hiểu (40%), 3 Vận dụng (10%). Gồm 6 dạng bài $\times$ 5 biến thể.
2. **Độc lập số liệu**: Mỗi biến thể có tham số và câu hỏi độc lập, không trùng lặp đề bài (`norm_key`).
3. **Độ tương thích LaTeX**:
   - Biểu thức bọc trong `$...$` hoặc `$$...$$`.
   - Sử dụng cú pháp tương thích với renderer `math.js` trên Web (tránh `\begin{cases}`, `\dots`, escape sai).
   - Dấu phẩy thập phân kiểu Việt `,` (ví dụ `0,5`).
4. **Đáp số câu hỏi trả lời ngắn**:
   - Bắt buộc là số nguyên hoặc số thập phân chuẩn. Không dùng phân số hay căn thức trong trường `answer` của câu hỏi trả lời ngắn.

---

## 3. Kiến trúc Mô-đun & Luồng dữ liệu

Áp dụng mô hình **Builder theo từng chương** đã thành công tại Toán 9:

```
scripts/
├── toan11_builder/
│   ├── __init__.py
│   ├── common.py             # Helper sinh lựa chọn nhiễu, chuẩn hóa
│   ├── c1.py -> c5.py        # Logic 24 dạng TN + 6 dạng TLN cho từng chương
├── toan12_builder/
│   ├── __init__.py
│   ├── common.py
│   ├── c1.py -> c3.py        # Logic 24 dạng TN + 6 dạng TLN cho từng chương
├── gen_bank_toan11_hk1.py    # Điều phối sinh scripts/bank/toan11_c*.json
├── gen_bank_toan12_hk1.py    # Điều phối sinh scripts/bank/toan12_c*.json
├── build_data.py             # Cấu hình CHAPTERS cho toan11 và toan12
└── audit_banks_deep.py       # Cấu hình danh sách môn audit thêm toan11, toan12
```

Luồng tổng hợp dữ liệu:
```
toan11_builder/ + toan12_builder/
       ↓
scripts/bank/toan11_c*.json & toan12_c*.json
       ↓ (python scripts/build_data.py)
data/toan11/questions/ (mc.json, short.json)
data/toan12/questions/ (mc.json, short.json)
       ↓
Kiểm định: build_data.py --check & audit_banks_deep.py
```

---

## 4. Kế hoạch Kiểm thử & Nghiệm thu (Verification)

1. **Pipeline build**: `python scripts/build_data.py --check`
   - Kiểm tra định dạng schema, tỉ lệ độ khó 50/40/10, số lượng câu hỏi, số dạng bài.
2. **Audit chuyên sâu**: `python scripts/audit_banks_deep.py`
   - 0 cảnh báo LaTeX không tương thích.
   - 0 câu hỏi có các lựa chọn bị trùng nhau.
   - Đáp án đúng nằm trong các lựa chọn.
   - Đáp số trả lời ngắn có định dạng số hợp lệ.
3. **Unit Tests Backend**: `pytest` vượt qua 7/7 tests hiện có.
4. **Frontend Tests**: `node tests/frontend.test.mjs` vượt qua toàn bộ 57 tests.
5. **UI Web Verification**: Web SPA tự động hiển thị Toán 11 và Toán 12 trong danh sách môn, bộ lọc học kì hoạt động chuẩn xác, hiển thị lý thuyết và làm bài mượt mà.
