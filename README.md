# Toán 10 — Lý thuyết & bài tập

Web học Toán 10 theo chương trình GDPT 2018 (bộ Kết nối tri thức với cuộc sống), phần **học kì 1**.
Toàn bộ nội dung nằm trong các file JSON ở thư mục `data/`, giao diện đọc trực tiếp từ đó.

Không dùng framework, không cần cài đặt, không phụ thuộc mạng (công thức toán được render bằng
một bộ render nhỏ tự viết trong `assets/js/math.js`).

## Chạy

Trang dùng `fetch` để đọc JSON nên **phải chạy qua web server**; mở trực tiếp bằng `file://`
sẽ bị trình duyệt chặn.

Cách nhanh nhất — nháy đúp `start.bat`. Hoặc chạy tay:

```bash
python -m http.server 8080      # rồi mở http://localhost:8080
npx serve                       # nếu dùng Node.js
```

Trong VS Code: cài extension **Live Server**, bấm chuột phải `index.html` → *Open with Live Server*.

## Nội dung hiện có

| Chương | Tên | Bài lý thuyết | Trắc nghiệm | Trả lời ngắn |
|---|---|---|---|---|
| I | Mệnh đề và tập hợp | 2 | 15 | 13 |
| II | Bất phương trình và hệ bất phương trình bậc nhất hai ẩn | 2 | 11 | 10 |
| III | Hệ thức lượng trong tam giác | 2 | 15 | 15 |
| IV | Vectơ | 5 | 22 | 16 |
| V | Các số đặc trưng của mẫu số liệu không ghép nhóm | 3 | 15 | 15 |
| | **Tổng** | **14** | **78** | **69** |

Mỗi câu hỏi đều có lời giải và được gắn nhãn mức độ: nhận biết / thông hiểu / vận dụng.

## Chức năng

- **Lý thuyết** — đọc theo từng bài, có mục lục bên trái, chuyển bài trước/sau, ghi nhớ bài đang đọc.
- **Luyện tập** — chọn dạng bài, chọn nhiều chương, chọn mức độ, số câu, trộn thứ tự.
  - *Xem đáp án ngay*: chấm và hiện lời giải sau mỗi câu.
  - *Làm hết rồi chấm*: chỉ chấm khi nộp bài.
- **Chấm điểm** — trắc nghiệm so đáp án; trả lời ngắn nhận cả `7,5` và `7.5`, cả dấu trừ `−` và `-`,
  cả dạng phân số `15/2`, và có sai số cho phép với các đáp số làm tròn.
- **Kết quả** — điểm theo thang 10, lọc riêng câu sai để xem lại kèm lời giải.
- Chế độ sáng/tối, lưu lịch sử làm bài trong `localStorage`.

## Cấu trúc

```
index.html
start.bat                       mở server + trình duyệt (Windows)
assets/
  css/style.css
  js/
    app.js                      router theo hash, khởi tạo
    data.js                     đọc & cache JSON
    math.js                     render công thức toán
    grade.js                    chấm bài, chuẩn hoá đáp số
    store.js                    localStorage
    views/{home,theory,practice}.js
data/
  manifest.json                 danh sách lớp/học kì
  toan10/
    index.json                  chương, bài, các bộ câu hỏi
    theory/c1.json … c5.json    lý thuyết từng chương
    questions/mc.json           trắc nghiệm
    questions/short.json        trả lời ngắn
```

## Viết công thức toán trong JSON

Dùng một tập con của LaTeX, phần còn lại viết ký tự Unicode trực tiếp:

| Viết | Kết quả |
|---|---|
| `\frac{a}{b}` | phân số |
| `\sqrt{2}` | căn bậc hai |
| `\vec{AB}` | vectơ (mũi tên trên đầu) |
| `\overline{x}` | gạch ngang trên đầu |
| `x^{2}` hoặc `x^2` | số mũ |
| `a_{1}` hoặc `a_1` | chỉ số dưới |
| `\le \ge \ne \pm \cdot \in \cup \cap \Rightarrow` | ≤ ≥ ≠ ± · ∈ ∪ ∩ ⇒ |

Các ký hiệu như `≤ ∈ ∪ ∩ ∅ ∀ ∃ ⇔ ° √ α β ℝ ℚ ℤ ℕ` gõ thẳng cũng được.
Trong JSON nhớ escape dấu gạch chéo: `"\\frac{1}{2}"`.

## Thêm câu hỏi

Thêm phần tử vào mảng `questions` của `data/toan10/questions/mc.json` hoặc `short.json`.

Trắc nghiệm — `answer` là **chỉ số** của phương án đúng (0 = A, 1 = B, 2 = C, 3 = D):

```json
{
  "id": "mc-c1-16",
  "chapter": "c1",
  "lesson": "b2",
  "level": "th",
  "question": "Cho A = {1; 2; 3}. Số tập con của A là:",
  "choices": ["6", "8", "9", "3"],
  "answer": 1,
  "explanation": "Tập có n phần tử thì có 2^{n} tập con."
}
```

Trả lời ngắn — `answer` là một số, viết dấu chấm thập phân:

```json
{
  "id": "sa-c1-14",
  "chapter": "c1",
  "level": "vd",
  "question": "Tính tổng các phần tử của A = {x ∈ ℕ | x là ước của 12}.",
  "answer": "28",
  "explanation": "Các ước là 1; 2; 3; 4; 6; 12."
}
```

Trường tuỳ chọn: `tolerance` (sai số cho phép, dùng cho đáp số làm tròn như `2.83`),
`accept` (mảng đáp án khác cũng được tính đúng), `unit` (đơn vị hiển thị cạnh ô nhập).

## Thêm bài lý thuyết

Khai báo bài trong `data/toan10/index.json` (mảng `lessons` của chương), rồi thêm bài
tương ứng vào `data/toan10/theory/c<N>.json`. Mỗi bài là một mảng `blocks`; các loại block:

| `type` | Trường | Dùng cho |
|---|---|---|
| `heading` | `text` | tiêu đề mục |
| `text` | `content` | đoạn văn (dòng trống = đoạn mới) |
| `list` | `title?`, `items[]` | gạch đầu dòng |
| `definition` | `title?`, `content` | định nghĩa |
| `theorem` | `title?`, `content` | định lí, tính chất |
| `example` | `question`, `solution` | ví dụ có lời giải |
| `note` | `content` | chú ý, lưu ý |
| `formula` | `items[{label?, math}]` | bảng công thức |
| `table` | `title?`, `headers[]`, `rows[][]` | bảng |

## Thêm lớp hoặc học kì khác

1. Trong `data/manifest.json`, đổi `available` của mục tương ứng thành `true`
   (hoặc thêm mục mới), đặt `path` là tên thư mục dữ liệu.
2. Tạo thư mục `data/<path>/` với `index.json`, `theory/` và `questions/` theo đúng
   cấu trúc như `toan10`.

Không cần sửa code — ứng dụng lấy môn `available` đầu tiên trong manifest làm môn hiện hành.

## Có thể mở rộng thêm

Kiến trúc đã sẵn cho các dạng bài khác: thêm một mục vào `questionSets` của `index.json`
với `type` mới, rồi bổ sung nhánh render/chấm tương ứng trong `views/practice.js` và `grade.js`
(hai dạng hiện có là `multiple-choice` và `short-answer`).
