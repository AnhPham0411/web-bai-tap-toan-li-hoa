# Web Bài Tập Toán - Lý - Hóa 10 (GDPT 2018)

Ứng dụng web học lý thuyết và luyện bài tập cho 3 môn **Toán 10**, **Vật lí 10**, **Hóa học 10** theo chương trình GDPT 2018 (bộ sách Kết nối tri thức với cuộc sống, Học kì 1).

Repository: [https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa](https://github.com/AnhPham0411/web-bai-tap-toan-li-hoa)

## Quy mô Dữ liệu (2.250 câu hỏi)

- **Mỗi môn 5 chương**, mỗi chương **150 câu hỏi** (120 Trắc nghiệm + 30 Trả lời ngắn).
- **Phân bổ độ khó:** 50% Nhận biết (`nb`), 40% Thông hiểu (`th`), 10% Vận dụng (`vd`).
- **Tổng cộng:** **2.250 câu hỏi** (1.800 Trắc nghiệm + 450 Trả lời ngắn).
- **Mỗi dạng bài tối đa 5 biến thể**, và các biến thể bắt buộc khác nhau về số liệu lẫn đáp số — không có chuyện một câu bị nhân bản hàng chục lần chỉ để đảo thứ tự A/B/C/D.
- **100% câu hỏi** có đáp án đúng và lời giải chi tiết (`explanation`).

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
- **Chấm câu trả lời ngắn có sai số cho phép:** Câu nào đáp số phải làm tròn thì đề nói rõ, và bộ chấm chấp nhận cả đáp số chưa làm tròn qua trường `tolerance`.
- **Lưu tiến độ tự động, tách riêng theo môn:** Chế độ sáng/tối, môn đang chọn, vị trí đọc lý thuyết và lịch sử chấm điểm lưu trong `localStorage`; dữ liệu của Toán, Lý, Hóa **không lẫn vào nhau**.

---

## Cấu trúc dữ liệu

```
data/
  manifest.json              # danh sách môn học
  <mon>/
    index.json               # chương, bài, bộ câu hỏi, mức độ
    theory/c1..c5.json       # lý thuyết theo bài
    questions/mc.json        # 600 câu trắc nghiệm
    questions/short.json     # 150 câu trả lời ngắn
scripts/
  bank/<mon>_<chuong>.json   # NGÂN HÀNG NGUỒN — nơi biên soạn câu hỏi
  build_data.py              # lắp ráp + kiểm định + ghi ra data/
```

### Trường của một câu hỏi

| Trường | Trắc nghiệm | Trả lời ngắn | Ý nghĩa |
|---|:-:|:-:|---|
| `id` | ✓ | ✓ | `mc-c1-001` / `sa-c1-001` |
| `chapter`, `lesson` | ✓ | ✓ | Chương và bài trong SGK (`lesson` phải thuộc đúng `chapter`) |
| `level` | ✓ | ✓ | `nb` / `th` / `vd` |
| `dang` | ✓ | ✓ | Tên dạng bài — dùng để chặn quá 5 biến thể |
| `question`, `explanation` | ✓ | ✓ | Đề và lời giải |
| `choices`, `answer` | ✓ | | 4 phương án và **chỉ số** 0–3 của phương án đúng |
| `answer` | | ✓ | Đáp số dạng chuỗi, dấu chấm thập phân (`"0.67"`) |
| `tolerance` | | tuỳ | Sai số chấp nhận; bắt buộc > 0 nếu đáp số đã làm tròn |
| `unit` | | tuỳ | Đơn vị hiển thị cạnh ô nhập |

---

## Sinh/Cập nhật dữ liệu

Câu hỏi được biên soạn trong `scripts/bank/`, sau đó lắp ráp bằng:

```bash
python scripts/build_data.py --check   # chỉ kiểm định, không ghi
python scripts/build_data.py           # kiểm định rồi ghi vào data/
```

Script **không tự sinh câu hỏi**. Nó gán `id`, trộn thứ tự phương án bằng seed cố định (`SEED`, build lại cho kết quả giống hệt), đồng bộ tiêu đề bài theo SGK, và **từ chối ghi dữ liệu nếu còn lỗi**. Bộ kiểm định bắt:

- số câu và phân bổ độ khó sai so với chuẩn 60/48/12 và 15/12/3;
- một dạng bài vượt quá 5 biến thể, hoặc hai câu trùng đề (kể cả khác chương);
- `lesson` không thuộc `chapter` đang khai báo;
- phương án trùng giá trị nhau, hoặc chỉ số `answer` nằm ngoài 0–3;
- lệnh LaTeX nằm ngoài tập mà `assets/js/math.js` render được;
- dấu chấm thập phân kiểu Anh (`3.15`) trong đề/phương án/lời giải — chuẩn SGK Việt Nam dùng dấu phẩy;
- ký tự Unicode mũ/chỉ số (`H₂SO₄`) thay vì LaTeX (`H_2SO_4`);
- dấu vết sinh tự động còn sót như `(Câu 12)`;
- đáp số trả lời ngắn không đọc được thành số, hoặc là số thập phân mà `tolerance = 0` (học sinh nộp đáp số chưa làm tròn sẽ bị chấm sai).

---

## Deploy Vercel

Dự án dùng cấu hình tĩnh với `vercel.json`. Khi push lên nhánh `main` của kho `AnhPham0411/web-bai-tap-toan-li-hoa`, Vercel tự động build & deploy lại, giữ nguyên domain/project hiện tại.
