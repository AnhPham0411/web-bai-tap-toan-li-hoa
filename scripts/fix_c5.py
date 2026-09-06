import json

with open('data/toan10/questions/mc.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_qs = [
    {
        "id": "mc-c5-089",
        "chapter": "c5", "lesson": "b13", "level": "nb",
        "dang": "Khoảng biến thiên",
        "question": "Khoảng biến thiên (range) của một mẫu số liệu cho ta biết điều gì?",
        "choices": [
            "Khoảng cách giữa giá trị lớn nhất và giá trị nhỏ nhất của mẫu",
            "Khoảng cách giữa hai tứ phân vị $Q_3$ và $Q_1$",
            "Độ lệch trung bình của các số liệu so với số trung bình",
            "Mật độ tập trung của các giá trị ở chính giữa mẫu"
        ],
        "answer": 0,
        "explanation": "Định nghĩa cơ bản: Khoảng biến thiên $R = x_{\\max} - x_{\\min}$ phản ánh khoảng cách giữa giá trị lớn nhất và nhỏ nhất."
    },
    {
        "id": "mc-c5-090",
        "chapter": "c5", "lesson": "b13", "level": "th",
        "dang": "Khoảng biến thiên",
        "question": "Cho mẫu số liệu về thời gian (phút) hoàn thành bài thi của 6 học sinh: 45, 50, 42, 60, 48, 55. Khoảng biến thiên của mẫu là:",
        "choices": [
            "18", "15", "60", "42"
        ],
        "answer": 0,
        "explanation": "Giá trị lớn nhất $x_{\\max} = 60$, nhỏ nhất $x_{\\min} = 42$. Khoảng biến thiên $R = 60 - 42 = 18$."
    },
    {
        "id": "mc-c5-091",
        "chapter": "c5", "lesson": "b13", "level": "th",
        "dang": "Khoảng biến thiên",
        "question": "Nhược điểm lớn nhất của việc dùng khoảng biến thiên để đo mức độ phân tán của số liệu là gì?",
        "choices": [
            "Rất dễ bị ảnh hưởng bởi các giá trị ngoại lệ (outliers)",
            "Không thể tính được nếu số lượng dữ liệu là số lẻ",
            "Luôn cho ra một số âm nếu dữ liệu có giá trị âm",
            "Tính toán quá phức tạp với mẫu số liệu lớn"
        ],
        "answer": 0,
        "explanation": "Khoảng biến thiên chỉ dựa vào 2 giá trị cực trị, nên nếu có một giá trị quá lớn hoặc quá nhỏ (ngoại lệ), khoảng biến thiên sẽ thay đổi đột ngột và không phản ánh đúng sự phân tán của đa số dữ liệu."
    },
    {
        "id": "mc-c5-092",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Khoảng biến thiên",
        "question": "Trong đợt kiểm tra, điểm của 5 học sinh là 6, 7, 8, 9 và $x$. Biết khoảng biến thiên của mẫu số liệu này là 5. Tìm các giá trị có thể của $x$.",
        "choices": [
            "$x = 4$ hoặc $x = 11$",
            "$x = 3$ hoặc $x = 10$",
            "$x = 1$ hoặc $x = 14$",
            "$x = 5$ hoặc $x = 10$"
        ],
        "answer": 0,
        "explanation": "Min hiện tại 6, Max 9 (Khoảng = 3). Để khoảng = 5, $x$ tạo ra biên mới. TH1: $x$ là max $\\Rightarrow x - 6 = 5 \\Rightarrow x = 11$. TH2: $x$ là min $\\Rightarrow 9 - x = 5 \\Rightarrow x = 4$."
    },
    {
        "id": "mc-c5-093",
        "chapter": "c5", "lesson": "b13", "level": "nb",
        "dang": "Khoảng tứ phân vị",
        "question": "Khoảng tứ phân vị, kí hiệu là $\\Delta_Q$, được tính bằng công thức nào sau đây?",
        "choices": [
            "$\\Delta_Q = Q_3 - Q_1$",
            "$\\Delta_Q = Q_2 - Q_1$",
            "$\\Delta_Q = Q_3 - Q_2$",
            "$\\Delta_Q = (Q_1 + Q_3)/2$"
        ],
        "answer": 0,
        "explanation": "Khoảng tứ phân vị là hiệu số giữa tứ phân vị thứ ba ($Q_3$) và tứ phân vị thứ nhất ($Q_1$)."
    },
    {
        "id": "mc-c5-094",
        "chapter": "c5", "lesson": "b13", "level": "th",
        "dang": "Khoảng tứ phân vị",
        "question": "So với khoảng biến thiên, ưu điểm của khoảng tứ phân vị trong việc đo độ phân tán là gì?",
        "choices": [
            "Ít bị ảnh hưởng bởi các giá trị bất thường (ngoại lệ)",
            "Đo lường sự phân tán của toàn bộ 100% dữ liệu",
            "Dễ tính toán hơn vì không cần sắp xếp số liệu",
            "Luôn luôn bằng một nửa của khoảng biến thiên"
        ],
        "answer": 0,
        "explanation": "$\\Delta_Q = Q_3 - Q_1$ tập trung vào 50% số liệu ở giữa, loại bỏ ảnh hưởng của 25% số liệu thấp nhất và 25% số liệu cao nhất, không bị nhiễu bởi ngoại lệ."
    },
    {
        "id": "mc-c5-095",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Khoảng tứ phân vị",
        "question": "Cho mẫu số liệu: 2, 4, 6, 7, 8, 9, 12, 15. Khoảng tứ phân vị $\\Delta_Q$ của mẫu là:",
        "choices": [
            "5.5", "6.5", "13", "8"
        ],
        "answer": 0,
        "explanation": "Mẫu có 8 giá trị (đã sắp xếp). Tứ phân vị $Q_2 = 7.5$. $Q_1$ là trung vị của {2, 4, 6, 7} $\\Rightarrow Q_1 = 5$. $Q_3$ là trung vị của {8, 9, 12, 15} $\\Rightarrow Q_3 = 10.5$. Khoảng tứ phân vị $\\Delta_Q = 10.5 - 5 = 5.5$."
    },
    {
        "id": "mc-c5-096",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Khoảng tứ phân vị",
        "question": "Một mẫu số liệu có $Q_1 = 15, Q_3 = 27$. Một giá trị $x$ được gọi là giá trị ngoại lệ nếu nó thoả mãn điều kiện nào?",
        "choices": [
            "$x < -3$ hoặc $x > 45$",
            "$x < 12$ hoặc $x > 30$",
            "$x < 0$ hoặc $x > 42$",
            "$x < 15$ hoặc $x > 27$"
        ],
        "answer": 0,
        "explanation": "$\\Delta_Q = 27 - 15 = 12$. Ngưỡng dưới: $Q_1 - 1.5\\Delta_Q = 15 - 1.5 \\times 12 = -3$. Ngưỡng trên: $Q_3 + 1.5\\Delta_Q = 27 + 1.5 \\times 12 = 45$. Ngoại lệ khi $x < -3$ hoặc $x > 45$."
    },
    {
        "id": "mc-c5-097",
        "chapter": "c5", "lesson": "b13", "level": "nb",
        "dang": "Phương sai và độ lệch chuẩn",
        "question": "Phương sai của một mẫu số liệu bằng 16. Độ lệch chuẩn của mẫu số liệu đó là:",
        "choices": [
            "4", "-4", "256", "8"
        ],
        "answer": 0,
        "explanation": "Độ lệch chuẩn $s$ là căn bậc hai số học của phương sai $s^2$. Vậy $s = \\sqrt{16} = 4$."
    },
    {
        "id": "mc-c5-098",
        "chapter": "c5", "lesson": "b13", "level": "th",
        "dang": "Phương sai và độ lệch chuẩn",
        "question": "Khẳng định nào sau đây về phương sai ($s^2$) là ĐÚNG?",
        "choices": [
            "Phương sai luôn lớn hơn hoặc bằng 0",
            "Phương sai có cùng đơn vị với dữ liệu gốc",
            "Nếu tất cả các giá trị trong mẫu đều dương thì phương sai lớn hơn 0",
            "Phương sai là hiệu của trung bình và trung vị"
        ],
        "answer": 0,
        "explanation": "Phương sai là trung bình của bình phương các độ lệch, nên luôn $\\ge 0$. Bằng 0 chỉ khi mọi giá trị bằng nhau. Đơn vị là bình phương đơn vị gốc."
    },
    {
        "id": "mc-c5-099",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Phương sai và độ lệch chuẩn",
        "question": "Cho mẫu số liệu gồm n=4 phần tử: 2, 4, 4, 6. Phương sai $s^2$ của mẫu này là (tính theo công thức mẫu không chuẩn hóa $1/n$):",
        "choices": [
            "2", "4", "$\\sqrt{2}$", "8"
        ],
        "answer": 0,
        "explanation": "Số trung bình $\\bar{x} = 4$. Tổng bình phương độ lệch là $(2-4)^2 + (4-4)^2 + (4-4)^2 + (6-4)^2 = 4 + 0 + 0 + 4 = 8$. Phương sai $s^2 = 8 / 4 = 2$."
    },
    {
        "id": "mc-c5-100",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Phương sai và độ lệch chuẩn",
        "question": "Nếu cộng thêm 5 vào mỗi số liệu của một mẫu thì độ lệch chuẩn của mẫu sẽ thay đổi như thế nào?",
        "choices": [
            "Không thay đổi",
            "Tăng thêm 5",
            "Tăng thêm $\\sqrt{5}$",
            "Nhân lên 5 lần"
        ],
        "answer": 0,
        "explanation": "Khi cộng thêm hằng số, số trung bình cũng tăng. Độ lệch của mỗi số so với trung bình $(x_i + c) - (\\bar{x} + c) = x_i - \\bar{x}$ không đổi $\\Rightarrow$ phương sai và độ lệch chuẩn không thay đổi."
    },
    {
        "id": "mc-c5-101",
        "chapter": "c5", "lesson": "b13", "level": "th",
        "dang": "Tổng hợp đặc trưng phân tán",
        "question": "Kết quả đo chiều cao của nhóm nam có $s_1 = 4.2$ cm, nhóm nữ có $s_2 = 2.8$ cm. Kết luận nào hợp lý nhất?",
        "choices": [
            "Chiều cao nhóm nam phân tán nhiều hơn nhóm nữ",
            "Nhóm nam cao hơn nhóm nữ",
            "Nhóm nam đông người hơn nhóm nữ",
            "Có sai số khi đo nhóm nam nhiều hơn nhóm nữ"
        ],
        "answer": 0,
        "explanation": "Độ lệch chuẩn $s$ càng lớn thì mức độ phân tán quanh trung bình càng cao."
    },
    {
        "id": "mc-c5-102",
        "chapter": "c5", "lesson": "b13", "level": "th",
        "dang": "Giá trị ngoại lệ",
        "question": "Khi có nhiều giá trị ngoại lệ bất thường, số đặc trưng nào đo mức độ phân tán TỐT NHẤT?",
        "choices": [
            "Khoảng tứ phân vị",
            "Khoảng biến thiên",
            "Phương sai",
            "Độ lệch chuẩn"
        ],
        "answer": 0,
        "explanation": "Phương sai, độ lệch chuẩn và khoảng biến thiên nhạy cảm với ngoại lệ. Khoảng tứ phân vị chỉ phụ thuộc $Q_1, Q_3$ nên bền vững hơn."
    },
    {
        "id": "mc-c5-103",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Tổng hợp đặc trưng phân tán",
        "question": "Nếu nhân mỗi số liệu của mẫu với hằng số $k > 0$, thì phương sai của mẫu bị ảnh hưởng thế nào?",
        "choices": [
            "Nhân với $k^2$",
            "Nhân với $k$",
            "Không thay đổi",
            "Cộng thêm $k^2$"
        ],
        "answer": 0,
        "explanation": "Độ lệch $x_i - \\bar{x}$ nhân lên $k$. Bình phương độ lệch nhân lên $k^2$. Do đó phương sai tăng gấp $k^2$ lần."
    },
    {
        "id": "mc-c5-104",
        "chapter": "c5", "lesson": "b13", "level": "vd",
        "dang": "Tổng hợp đặc trưng phân tán",
        "question": "Cho một mẫu có phương sai $s^2 = 10$ và trung bình $\\bar{x} = 5$. Nếu thêm vào mẫu một giá trị đúng bằng 5, phương sai mới sẽ:",
        "choices": [
            "Giảm xuống",
            "Không thay đổi",
            "Tăng lên",
            "Không đủ dữ kiện tính"
        ],
        "answer": 0,
        "explanation": "Giá trị 5 bằng trung bình nên độ lệch bằng 0. Tổng bình phương độ lệch không đổi, nhưng số lượng phần tử $n$ tăng lên nên phương sai giảm."
    },
    {
        "id": "mc-c5-105",
        "chapter": "c5", "lesson": "b11", "level": "nb",
        "dang": "Số gần đúng",
        "question": "Số $\\pi \\approx 3.14159265...$ được làm tròn tới hàng phần trăm là:",
        "choices": [
            "3.14", "3.15", "3.1", "3.141"
        ],
        "answer": 0,
        "explanation": "Chữ số hàng phần trăm là 4. Kế bên là 1 < 5 nên giữ nguyên 4 $\\Rightarrow 3.14$."
    },
    {
        "id": "mc-c5-106",
        "chapter": "c5", "lesson": "b11", "level": "th",
        "dang": "Số gần đúng",
        "question": "Một tấm gỗ đo được chiều dài $a = 125 \\pm 0.5$ (cm). Sai số tuyệt đối của phép đo này không vượt quá:",
        "choices": [
            "0.5 cm", "125 cm", "125.5 cm", "0.25 cm"
        ],
        "answer": 0,
        "explanation": "Kí hiệu $a = \\bar{a} \\pm d$ chỉ ra sai số tuyệt đối $\\Delta_a \\le d = 0.5$ cm."
    },
    {
        "id": "mc-c5-107",
        "chapter": "c5", "lesson": "b11", "level": "th",
        "dang": "Số gần đúng",
        "question": "Sai số tương đối $\\delta_a$ trong phép đo $a = 125 \\pm 0.5$ (cm) xấp xỉ bằng:",
        "choices": [
            "0.4%", "0.5%", "2.5%", "4%"
        ],
        "answer": 0,
        "explanation": "$\\delta_a \\le \\frac{d}{|a|} = \\frac{0.5}{125} = 0.004 = 0.4\\%$."
    },
    {
        "id": "mc-c5-108",
        "chapter": "c5", "lesson": "b11", "level": "vd",
        "dang": "Số gần đúng",
        "question": "Đo bán kính $R = 10 \\pm 0.1$ m. Sai số tương đối của phép đo DIỆN TÍCH xấp xỉ là:",
        "choices": [
            "2%", "1%", "0.1%", "0.01%"
        ],
        "answer": 0,
        "explanation": "Diện tích tỉ lệ thuận với $R^2$. Sai số tương đối của $R$ là $1\\%$. Sai số tương đối của $R^2$ xấp xỉ gấp đôi $\\Rightarrow 2\\%$."
    },
    {
        "id": "mc-c5-109",
        "chapter": "c5", "lesson": "b11", "level": "nb",
        "dang": "Số quy tròn",
        "question": "Quy tròn số $a = 1234.567$ đến hàng phần mười được:",
        "choices": [
            "1234.6", "1234.5", "1230", "1234.57"
        ],
        "answer": 0,
        "explanation": "Chữ số hàng phần mười là 5, sau nó là 6 $\\ge 5$ $\\Rightarrow$ cộng 1 thành $1234.6$."
    },
    {
        "id": "mc-c5-110",
        "chapter": "c5", "lesson": "b11", "level": "th",
        "dang": "Số quy tròn",
        "question": "Số quy tròn của số gần đúng $174567 \\pm 200$ là:",
        "choices": [
            "175000", "174600", "174000", "174500"
        ],
        "answer": 0,
        "explanation": "Độ chính xác ở hàng trăm ($d=200$), cần làm tròn đến hàng nghìn. Chữ số hàng nghìn là 4, sau nó là 5 $\\Rightarrow 175000$."
    },
    {
        "id": "mc-c5-111",
        "chapter": "c5", "lesson": "b11", "level": "vd",
        "dang": "Số quy tròn",
        "question": "Biết $\\sqrt{2} \\approx 1.4142135$. Số gần đúng của $\\sqrt{2}$ với độ chính xác $d = 0.005$ là:",
        "choices": [
            "1.41", "1.4", "1.414", "1.42"
        ],
        "answer": 0,
        "explanation": "Độ chính xác $0.005$ ở hàng phần nghìn, ta quy tròn đến hàng phần trăm $\\Rightarrow 1.41$."
    },
    {
        "id": "mc-c5-112",
        "chapter": "c5", "lesson": "b11", "level": "vd",
        "dang": "Số quy tròn",
        "question": "Chiều dài $l = 1500 \\pm 2$ m. Số chữ số chắc (đáng tin) của 1500 là:",
        "choices": [
            "3", "4", "2", "0"
        ],
        "answer": 0,
        "explanation": "Chữ số chắc ở hàng $k$ nếu $d \\le 0.5 \\times 10^k$. Ở đây $2 \\le 5 = 0.5 \\times 10^1$ (hàng chục). Vậy hàng nghìn, trăm, chục (1, 5, 0) là 3 chữ số chắc."
    },
    {
        "id": "mc-c5-113",
        "chapter": "c5", "lesson": "b12", "level": "nb",
        "dang": "Tổng hợp xu thế",
        "question": "Số đặc trưng nào KHÔNG bị ảnh hưởng bởi giá trị ngoại lệ?",
        "choices": [
            "Trung vị", "Số trung bình", "Phương sai", "Khoảng biến thiên"
        ],
        "answer": 0,
        "explanation": "Trung vị dựa trên vị trí đứng giữa, không phụ thuộc giá trị của số liệu lớn nhất hay nhỏ nhất."
    },
    {
        "id": "mc-c5-114",
        "chapter": "c5", "lesson": "b12", "level": "th",
        "dang": "Tổng hợp xu thế",
        "question": "Khi thống kê size giày bán chạy để nhập hàng, ta nên dùng:",
        "choices": [
            "Mốt (Mode)",
            "Số trung bình",
            "Trung vị",
            "Độ lệch chuẩn"
        ],
        "answer": 0,
        "explanation": "Mốt là giá trị xuất hiện nhiều nhất, rất quan trọng cho quyết định nhập hàng hóa."
    },
    {
        "id": "mc-c5-115",
        "chapter": "c5", "lesson": "b12", "level": "vd",
        "dang": "Tổng hợp xu thế",
        "question": "Mẫu lương: 5, 6, 7, 7, 8, 50 (triệu đồng). Phát biểu nào đúng?",
        "choices": [
            "Trung vị phản ánh mặt bằng lương tốt hơn trung bình",
            "Trung vị bằng 50, phản ánh sai lệch",
            "Trung bình và trung vị bằng nhau",
            "Trung bình nhỏ hơn trung vị"
        ],
        "answer": 0,
        "explanation": "Ngoại lệ 50 kéo trung bình lên quá cao. Trung vị $M_e = 7$ phản ánh sát thực tế lương số đông."
    },
    {
        "id": "mc-c5-116",
        "chapter": "c5", "lesson": "b12", "level": "vd",
        "dang": "Tổng hợp xu thế",
        "question": "Trong một phân bố đối xứng hoàn hảo hình chuông, mối quan hệ giữa Trung bình, Trung vị và Mốt là:",
        "choices": [
            "Bằng nhau",
            "Trung bình lớn nhất",
            "Mốt nhỏ nhất",
            "Không cố định"
        ],
        "answer": 0,
        "explanation": "Phân bố chuẩn/đối xứng có cả 3 chỉ số này trùng nhau tại trung tâm."
    },
    {
        "id": "mc-c5-117",
        "chapter": "c5", "lesson": "b14", "level": "nb",
        "dang": "Biểu đồ hộp",
        "question": "Đường gạch ngang chia đôi \"hộp\" (box) trong biểu đồ hộp thể hiện:",
        "choices": [
            "Trung vị",
            "Số trung bình",
            "Tứ phân vị 1",
            "Mốt"
        ],
        "answer": 0,
        "explanation": "Hộp được giới hạn bởi $Q_1, Q_3$ và chia bởi $Q_2$ (Trung vị)."
    },
    {
        "id": "mc-c5-118",
        "chapter": "c5", "lesson": "b14", "level": "th",
        "dang": "Biểu đồ hộp",
        "question": "Nếu không có ngoại lệ, râu của biểu đồ hộp kéo dài tới đâu?",
        "choices": [
            "Giá trị min và max",
            "Trung bình cộng",
            "Tới $Q_1 - 1.5\\Delta_Q$",
            "Vô cực"
        ],
        "answer": 0,
        "explanation": "Râu kết nối từ $Q_1, Q_3$ tới các giá trị nhỏ nhất, lớn nhất (nằm trong giới hạn không ngoại lệ)."
    },
    {
        "id": "mc-c5-119",
        "chapter": "c5", "lesson": "b14", "level": "vd",
        "dang": "Biểu đồ hộp",
        "question": "Độ dài của hình hộp chữ nhật trong biểu đồ hộp là:",
        "choices": [
            "Khoảng tứ phân vị $\\Delta_Q$",
            "Tổng hai râu",
            "Khoảng biến thiên",
            "Độ lệch chuẩn"
        ],
        "answer": 0,
        "explanation": "Hộp đi từ $Q_1$ tới $Q_3$, nên chiều dài chính là $Q_3 - Q_1 = \\Delta_Q$."
    },
    {
        "id": "mc-c5-120",
        "chapter": "c5", "lesson": "b14", "level": "vd",
        "dang": "Biểu đồ hộp",
        "question": "Lớp 10A và 10B có cùng trung bình 7.0. Lớp 10A có \"hộp\" trên biểu đồ dài hơn 10B. Điều này ám chỉ:",
        "choices": [
            "Điểm lớp 10A phân tán rộng hơn ở nửa giữa",
            "Lớp 10A học đều hơn",
            "Lớp 10A có nhiều điểm 10 hơn",
            "Mốt điểm 10A lớn hơn"
        ],
        "answer": 0,
        "explanation": "Hộp dài hơn tức là Khoảng tứ phân vị lớn hơn, biểu thị mức độ phân tán của 50% số liệu giữa cao hơn, không đồng đều bằng."
    }
]

for i in range(len(data['questions'])):
    qid = data['questions'][i]['id']
    match = next((q for q in new_qs if q['id'] == qid), None)
    if match:
        data['questions'][i] = match

with open('e:/projects/toan10/data/toan10/questions/mc.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully replaced.")
