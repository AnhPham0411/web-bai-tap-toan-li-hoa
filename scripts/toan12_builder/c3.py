# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c3():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Khái niệm khoảng biến thiên", "b9", [
            lambda: ("Khoảng biến thiên R của mẫu số liệu ghép nhóm là:", ["Hiệu giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên", "Hiệu giữa hai tứ phân vị $Q_3 - Q_1$", "Giá trị lớn nhất trừ giá trị nhỏ nhất của tần số", "Tổng các độ dài nhóm"], 0, "$R = a_{k+1} - a_1$."),
            lambda: ("Mẫu số liệu ghép nhóm từ $[10; 20)$ đến $[50; 60)$. Khoảng biến thiên R bằng:", ["$50$", "$40$", "$60$", "$10$"], 0, "$R = 60 - 10 = 50$."),
            lambda: ("Ý nghĩa của khoảng biến thiên R trong thống kê là:", ["Đo độ biến thiên giữa giá trị lớn nhất và nhỏ nhất của mẫu", "Đo độ phân tán của 50% số liệu trung tâm", "Đại diện cho xu thế trung tâm", "Xác định mốt của mẫu"], 0, "Khoảng biến thiên phản ánh độ dàn trải toàn bộ của dữ liệu."),
            lambda: ("Khoảng biến thiên của mẫu số liệu có các nhóm $[0; 5), [5; 10), [10; 15)$ là:", ["$15$", "$5$", "$10$", "$20$"], 0, "$R = 15 - 0 = 15$."),
            lambda: ("Cho các nhóm $[20; 30), [30; 40), [40; 50), [50; 60)$. Giá trị của R là:", ["$40$", "$30$", "$50$", "$60$"], 0, "$R = 60 - 20 = 40$.")
        ]),
        ("Khái niệm khoảng tứ phân vị", "b9", [
            lambda: ("Khoảng tứ phân vị $\\Delta_Q$ của mẫu số liệu ghép nhóm được tính bởi:", ["$\\Delta_Q = Q_3 - Q_1$", "$\\Delta_Q = Q_3 - Q_2$", "$\\Delta_Q = Q_2 - Q_1$", "$\\Delta_Q = \\frac{Q_3 - Q_1}{2}$"], 0, "Định nghĩa khoảng tứ phân vị: $\\Delta_Q = Q_3 - Q_1$."),
            lambda: ("Khoảng tứ phân vị phản ánh mức độ phân tán của bao nhiêu phần trăm dữ liệu ở trung tâm?", ["$50\\%$", "$25\\%$", "$75\\%$", "$100\\%$"], 0, "Nằm giữa $Q_1$ và $Q_3$ chứa 50% số liệu trung tâm."),
            lambda: ("Ưu điểm chính của khoảng tứ phân vị so với khoảng biến thiên là:", ["Không bị ảnh hưởng bởi các giá trị bất thường (ngoại lai)", "Dễ tính hơn", "Luôn là số nguyên", "Bằng phương sai"], 0, "Khoảng tứ phân vị loại trừ 25% đầu và 25% cuối nên không bị méo bởi ngoại lai."),
            lambda: ("Nếu $Q_1 = 12$ và $Q_3 = 28$ thì khoảng tứ phân vị $\\Delta_Q$ bằng:", ["$16$", "$20$", "$14$", "$40$"], 0, "$\\Delta_Q = 28 - 12 = 16$."),
            lambda: ("Một mẫu có $Q_1 = 40$ và $Q_3 = 65$. Giá trị của $\\Delta_Q$ là:", ["$25$", "$30$", "$20$", "$15$"], 0, "$\\Delta_Q = 65 - 40 = 25$.")
        ]),
        ("Giá trị ngoại lai trong mẫu ghép nhóm", "b9", [
            lambda: ("Giá trị x trong mẫu được coi là giá trị ngoại lai (bất thường) nếu:", ["$x < Q_1 - 1,5\\Delta_Q$ hoặc $x > Q_3 + 1,5\\Delta_Q$", "$x < Q_1$ hoặc $x > Q_3$", "$x = \\bar{x}$", "$x < 0$"], 0, "Tiêu chuẩn xác định giá trị ngoại lai bằng tứ phân vị."),
            lambda: ("Khoảng xác định các giá trị không phải là ngoại lai là:", ["$[Q_1 - 1,5\\Delta_Q; Q_3 + 1,5\\Delta_Q]$", "$[Q_1; Q_3]$", "$[0; +\\infty)$", "$[\\bar{x} - s; \\bar{x} + s]$"], 0, "Bao gồm đoạn từ $Q_1 - 1,5\\Delta_Q$ đến $Q_3 + 1,5\\Delta_Q$."),
            lambda: ("Nếu $Q_1 = 10, Q_3 = 20 \\Rightarrow \\Delta_Q = 10$. Ranh giới trên của giá trị ngoại lai là:", ["$35$", "$30$", "$25$", "$40$"], 0, "$Q_3 + 1,5\\Delta_Q = 20 + 15 = 35$."),
            lambda: ("Ranh giới dưới để xác định ngoại lai với $Q_1 = 10, \\Delta_Q = 10$ là:", ["$-5$", "$0$", "$5$", "$-10$"], 0, "$Q_1 - 1,5\\Delta_Q = 10 - 15 = -5$."),
            lambda: ("Giá trị ngoại lai phản ánh:", ["Các giá trị quá lớn hoặc quá nhỏ bất thường", "Giá trị trung bình", "Trung vị", "Tần số lớn nhất"], 0, "Là những quan sát dị thường lệch xa khỏi quần thể dữ liệu.")
        ]),
        ("Khái niệm phương sai", "b10", [
            lambda: ("Phương sai của mẫu số liệu ghép nhóm là đại lượng dùng để đo:", ["Mức độ phân tán của các số liệu xung quanh số trung bình", "Xu thế trung tâm", "Giá trị lớn nhất của mẫu", "Độ dài của nhóm"], 0, "Phương sai đo độ phân tán bình phương xung quanh $\\bar{x}$."),
            lambda: ("Kí hiệu của phương sai mẫu số liệu ghép nhóm là:", ["$s^2$", "$s$", "$\\bar{x}$", "$R$"], 0, "Phương sai kí hiệu là $s^2$."),
            lambda: ("Phương sai $s^2$ có giá trị luôn:", ["Không âm ($s^2 \\ge 0$)", "Dương ($s^2 > 0$)", "Có thể âm", "Bằng 0 với mọi mẫu"], 0, "Là trung bình của các bình phương nên $s^2 \\ge 0$."),
            lambda: ("Khi tất cả các số liệu trong mẫu đều bằng nhau thì phương sai bằng:", ["$0$", "$1$", "$+\\infty$", "Không xác định"], 0, "Không có sự phân tán nên $s^2 = 0$."),
            lambda: ("Công thức tính phương sai $s^2$ theo giá trị đại diện $c_i$ là:", ["$s^2 = \\frac{1}{n} \\sum m_i c_i^2 - (\\bar{x})^2$", "$s^2 = \\frac{1}{n} \\sum m_i c_i - \\bar{x}$", "$s^2 = \\sqrt{\\frac{1}{n} \\sum m_i c_i^2}$", "$s^2 = (\\bar{x})^2$"], 0, "$s^2 = \\frac{1}{n} \\sum m_i c_i^2 - (\\bar{x})^2$.")
        ]),
        ("Khái niệm độ lệch chuẩn", "b10", [
            lambda: ("Độ lệch chuẩn s của mẫu số liệu ghép nhóm là:", ["Căn bậc hai số học của phương sai: $s = \\sqrt{s^2}$", "Bình phương của phương sai: $s = (s^2)^2$", "Nghịch đảo của phương sai", "Khoảng biến thiên chia đôi"], 0, "$s = \\sqrt{s^2}$."),
            lambda: ("Ưu điểm lớn nhất của độ lệch chuẩn so với phương sai là:", ["Có cùng đơn vị đo với dấu hiệu đang nghiên cứu", "Luôn là số nguyên", "Dễ tính nhẩm hơn", "Không phụ thuộc vào cỡ mẫu"], 0, "Độ lệch chuẩn có cùng đơn vị với biến số (mét, kg, điểm...) giúp dễ giải thích thực tế."),
            lambda: ("Kí hiệu của độ lệch chuẩn mẫu là:", ["$s$", "$s^2$", "$\\sigma^2$", "$\\Delta_Q$"], 0, "Kí hiệu là s."),
            lambda: ("Nếu phương sai $s^2 = 16$ thì độ lệch chuẩn s bằng:", ["$4$", "$8$", "$256$", "$2$"], 0, "$s = \\sqrt{16} = 4$."),
            lambda: ("Cho độ lệch chuẩn $s = 5$. Phương sai $s^2$ bằng:", ["$25$", "$10$", "$\\sqrt{5}$", "$50$"], 0, "$s^2 = 5^2 = 25$.")
        ]),
        ("Ý nghĩa so sánh của độ lệch chuẩn", "b10", [
            lambda: ("Hai lớp có cùng điểm trung bình môn Toán. Lớp nào có độ lệch chuẩn nhỏ hơn thì:", ["Điểm số của học sinh đồng đều hơn", "Điểm số phân tán nhiều hơn", "Có nhiều học sinh giỏi hơn", "Có điểm trung bình cao hơn"], 0, "Độ lệch chuẩn nhỏ hơn thể hiện dữ liệu tập trung hơn, đồng đều hơn."),
            lambda: ("Trong đầu tư tài chính, cổ phiếu có độ lệch chuẩn của tỉ suất sinh lời lớn hơn thể hiện:", ["Mức độ rủi ro cao hơn (biến động lớn hơn)", "Độ an toàn cao hơn", "Lợi nhuận chắc chắn cao hơn", "Không có rủi ro"], 0, "Độ lệch chuẩn đo lường mức độ biến động (rủi ro)."),
            lambda: ("Hai máy tiện chi tiết: Máy A có $s = 0,1\\text{ mm}$, máy B có $s = 0,3\\text{ mm}$. Máy nào hoạt động ổn định hơn?", ["Máy A ổn định hơn", "Máy B ổn định hơn", "Hai máy như nhau", "Không so sánh được"], 0, "Máy A có sai số nhỏ hơn nên chất lượng đồng đều, ổn định hơn."),
            lambda: ("Một xạ thủ có độ lệch chuẩn điểm bắn qua các lần bắn nhỏ thì:", ["Bắn ổn định, phong độ vững vàng", "Bắn kém chính xác", "Điểm trung bình thấp", "Dễ bắn trúng hồng tâm hơn người khác"], 0, "Độ lệch chuẩn nhỏ chứng tỏ phong độ ổn định."),
            lambda: ("Khi hai mẫu số liệu có số trung bình xấp xỉ nhau, để so sánh độ đồng đều ta dùng:", ["Độ lệch chuẩn hoặc phương sai", "Trung vị", "Mốt", "Cỡ mẫu"], 0, "Dùng độ lệch chuẩn s để so sánh mức độ phân tán.")
        ]),
        ("Đơn vị đo của các số đặc trưng", "b10", [
            lambda: ("Nếu mẫu số liệu khảo sát về chiều cao tính bằng centimét (cm) thì đơn vị của phương sai là:", ["$\\text{cm}^2$", "$\\text{cm}$", "Không có đơn vị", "$\\text{cm}^3$"], 0, "Phương sai tính bằng bình phương của đơn vị gốc: $\\text{cm}^2$."),
            lambda: ("Nếu đơn vị của dữ liệu là kilôgam (kg) thì đơn vị của độ lệch chuẩn là:", ["$\\text{kg}$", "$\\text{kg}^2$", "$\\text{g}$", "Phần trăm"], 0, "Độ lệch chuẩn có cùng đơn vị với dữ liệu gốc: kg."),
            lambda: ("Đơn vị của khoảng tứ phân vị và khoảng biến thiên là:", ["Cùng đơn vị với dữ liệu gốc", "Bình phương đơn vị gốc", "Không có đơn vị", "Phần trăm"], 0, "Cả hai đều có cùng đơn vị với dữ liệu khảo sát."),
            lambda: ("Đại lượng nào sau đây KHÔNG có cùng đơn vị với dữ liệu gốc?", ["Phương sai $s^2$", "Độ lệch chuẩn s", "Khoảng biến thiên R", "Khoảng tứ phân vị $\\Delta_Q$"], 0, "Phương sai có đơn vị bình phương."),
            lambda: ("Nếu đơn vị là 'triệu đồng', đơn vị của phương sai là:", ["$(\\text{triệu đồng})^2$", "triệu đồng", "nghìn đồng", "tỉ đồng"], 0, "Đơn vị là $(\\text{triệu đồng})^2$.")
        ]),
        ("Nhận dạng công thức phương sai", "b10", [
            lambda: ("Trong công thức $s^2 = \\frac{1}{n} \\sum m_i (c_i - \\bar{x})^2$, biểu thức $(c_i - \\bar{x})$ gọi là:", ["Độ lệch của giá trị đại diện nhóm so với số trung bình", "Khoảng cách nhóm", "Tần số", "Độ lệch chuẩn"], 0, "Là khoảng cách (độ lệch) từ tâm nhóm đến trung bình."),
            lambda: ("Đại lượng $m_i$ trong công thức phương sai đóng vai trò là:", ["Trọng số (tần số của nhóm)", "Cỡ mẫu", "Giá trị đại diện", "Số nhóm"], 0, "$m_i$ là tần số của nhóm tương ứng."),
            lambda: ("Nếu cộng thêm một hằng số c vào tất cả các giá trị của mẫu thì phương sai của mẫu mới:", ["Không thay đổi", "Tăng thêm c", "Tăng thêm $c^2$", "Gấp c lần"], 0, "Tịnh tiến dữ liệu không làm thay đổi độ phân tán."),
            lambda: ("Nếu nhân tất cả các giá trị của mẫu với số thực $k > 0$ thì phương sai mới gấp phương sai cũ:", ["$k^2$ lần", "k lần", "$\\sqrt{k}$ lần", "Không đổi"], 0, "Phương sai gấp $k^2$ lần, độ lệch chuẩn gấp k lần."),
            lambda: ("Nếu nhân tất cả các giá trị với 3 thì độ lệch chuẩn mới gấp độ lệch chuẩn cũ:", ["$3$ lần", "$9$ lần", "$\\sqrt{3}$ lần", "Không đổi"], 0, "Độ lệch chuẩn tỉ lệ bậc nhất nên gấp 3 lần.")
        ]),
        ("Đọc bảng số liệu tính tổng bình phương", "b10", [
            lambda: ("Để tính phương sai nhanh, người ta lập thêm cột trong bảng phân bố là:", ["$m_i c_i^2$ (tần số nhân bình phương giá trị đại diện)", "$c_i^3$", "$m_i / c_i$", "$c_i - m_i$"], 0, "Cột $m_i c_i^2$ giúp tính nhanh tổng $\\sum m_i c_i^2$."),
            lambda: ("Cho $c_1 = 5, m_1 = 4$. Giá trị tích $m_1 c_1^2$ bằng:", ["$100$", "$20$", "$50$", "$200$"], 0, "$4 \\times 5^2 = 4 \\times 25 = 100$."),
            lambda: ("Cho $c_2 = 10, m_2 = 3$. Giá trị của $m_2 c_2^2$ là:", ["$300$", "$30$", "$100$", "$900$"], 0, "$3 \\times 100 = 300$."),
            lambda: ("Giá trị của $c_3 = 2, m_3 = 5$. Tích $m_3 c_3^2$ bằng:", ["$20$", "$10$", "$50$", "$40$"], 0, "$5 \\times 4 = 20$."),
            lambda: ("Cho $c = 4, m = 2$. Tính $m c^2$:", ["$32$", "$16$", "$64$", "$8$"], 0, "$2 \\times 16 = 32$.")
        ]),
        ("Ý nghĩa thực tế của khoảng biến thiên", "b9", [
            lambda: ("Nhiệt độ trong ngày có nhiệt độ thấp nhất là $20^\\circ\\text{C}$ và cao nhất là $32^\\circ\\text{C}$. Biên độ nhiệt trong ngày (khoảng biến thiên) là:", ["$12^\\circ\\text{C}$", "$26^\\circ\\text{C}$", "$10^\\circ\\text{C}$", "$15^\\circ\\text{C}$"], 0, "$R = 32 - 20 = 12^\\circ\\text{C}$."),
            lambda: ("Giá cổ phiếu trong phiên dao động từ 45 nghìn đồng đến 52 nghìn đồng. Khoảng biến thiên là:", ["$7\\text{ nghìn đồng}$", "$6\\text{ nghìn đồng}$", "$8\\text{ nghìn đồng}$", "$5\\text{ nghìn đồng}$"], 0, "$52 - 45 = 7$ nghìn đồng."),
            lambda: ("Thời gian giao hàng từ 2 ngày đến 8 ngày. Khoảng biến thiên bằng:", ["$6\\text{ ngày}$", "$5\\text{ ngày}$", "$8\\text{ ngày}$", "$4\\text{ ngày}$"], 0, "$8 - 2 = 6$ ngày."),
            lambda: ("Mức lương thấp nhất là 8 triệu, cao nhất là 30 triệu. Khoảng biến thiên mức lương là:", ["$22\\text{ triệu đồng}$", "$20\\text{ triệu đồng}$", "$15\\text{ triệu đồng}$", "$38\\text{ triệu đồng}$"], 0, "$30 - 8 = 22$ triệu đồng."),
            lambda: ("Tuổi của các thành viên trong câu lạc bộ từ 15 đến 25 tuổi. Khoảng biến thiên độ tuổi là:", ["$10\\text{ tuổi}$", "$20\\text{ tuổi}$", "$5\\text{ tuổi}$", "$15\\text{ tuổi}$"], 0, "$25 - 15 = 10$ tuổi.")
        ]),
        ("Tứ phân vị trong mẫu ghép nhóm", "b9", [
            lambda: ("Tứ phân vị thứ nhất $Q_1$ của mẫu ghép nhóm luôn thoả mãn:", ["$Q_1 \\le M_e$", "$Q_1 > M_e$", "$Q_1 = Q_3$", "$Q_1 \\ge Q_3$"], 0, "$Q_1 \\le Q_2 = M_e \\le Q_3$."),
            lambda: ("Tứ phân vị thứ ba $Q_3$ luôn thoả mãn:", ["$Q_3 \\ge M_e$", "$Q_3 < M_e$", "$Q_3 \\le Q_1$", "$Q_3 = 0$"], 0, "$Q_3$ luôn lớn hơn hoặc bằng trung vị."),
            lambda: ("Khoảng tứ phân vị $\\Delta_Q$ luôn là một số:", ["Không âm ($\\Delta_Q \\ge 0$)", "Âm", "Bằng 0", "Tuỳ ý"], 0, "Do $Q_3 \\ge Q_1$ nên $\\Delta_Q \\ge 0$."),
            lambda: ("Nếu $Q_1 = M_e = Q_3$ thì khoảng tứ phân vị bằng:", ["$0$", "$1$", "Không xác định", "$10$"], 0, "$\\Delta_Q = Q_3 - Q_1 = 0$."),
            lambda: ("Trong hộp biểu đồ đoạn thẳng (Boxplot), độ dài của 'hộp' chính là:", ["Khoảng tứ phân vị $\\Delta_Q$", "Khoảng biến thiên R", "Độ lệch chuẩn", "Phương sai"], 0, "Chiều dài hộp trong boxplot bằng $Q_3 - Q_1 = \\Delta_Q$.")
        ]),
        ("So sánh hai phân bố qua độ phân tán", "b10", [
            lambda: ("Nếu hai lớp có cùng điểm trung bình nhưng lớp 1 có $s_1 = 1,2$ và lớp 2 có $s_2 = 2,0$ thì:", ["Lớp 1 học đều hơn lớp 2", "Lớp 2 học đều hơn lớp 1", "Hai lớp đều như nhau", "Lớp 2 có nhiều bạn điểm cao hơn"], 0, "Độ lệch chuẩn của lớp 1 nhỏ hơn nên phân bố điểm đều hơn."),
            lambda: ("Hai quy trình sản xuất có độ lệch chuẩn khối lượng $s_A = 0,5\\text{ g}$ và $s_B = 1,2\\text{ g}$. Quy trình nào có chất lượng đồng đều hơn?", ["Quy trình A", "Quy trình B", "Cả hai bằng nhau", "Không xác định"], 0, "Quy trình A có độ lệch chuẩn nhỏ hơn nên đồng đều hơn."),
            lambda: ("Khi đánh giá độ ổn định của máy móc, chỉ số càng nhỏ càng tốt là:", ["Độ lệch chuẩn", "Số trung bình", "Số nhóm", "Cỡ mẫu"], 0, "Độ lệch chuẩn càng nhỏ máy hoạt động càng ổn định."),
            lambda: ("Phương sai $s^2 = 0$ khi và chỉ khi:", ["Tất cả các giá trị quan sát đều bằng nhau", "Cỡ mẫu bằng 0", "Số trung bình bằng 0", "Mốt bằng 0"], 0, "Tất cả các số liệu đều trùng nhau."),
            lambda: ("Nếu hai nhóm khách hàng có cùng mức chi tiêu trung bình nhưng nhóm 1 có phương sai nhỏ hơn nhóm 2 thì:", ["Mức chi tiêu của nhóm 1 đồng đều hơn", "Mức chi tiêu của nhóm 2 đồng đều hơn", "Hai nhóm đồng đều như nhau", "Nhóm 2 chi tiêu nhiều hơn"], 0, "Phương sai nhỏ hơn nghĩa là các số liệu ít phân tán hơn, đồng đều hơn.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c3-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 biến thể = 48 câu
    th_configs = [
        ("Khoảng biến thiên của bảng phân bố", "b9", [
            lambda: ("Bảng số liệu có các nhóm $[0; 10), [10; 20), [20; 30), [30; 40)$. Khoảng biến thiên là:", ["$40$", "$30$", "$50$", "$20$"], 0, "$R = 40 - 0 = 40$."),
            lambda: ("Mẫu số liệu từ $[20; 30)$ đến $[60; 70)$ có khoảng biến thiên R bằng:", ["$50$", "$40$", "$60$", "$70$"], 0, "$R = 70 - 20 = 50$."),
            lambda: ("Cho bảng phân bố từ $[15; 25)$ đến $[55; 65)$. Khoảng biến thiên là:", ["$50$", "$40$", "$45$", "$60$"], 0, "$R = 65 - 15 = 50$."),
            lambda: ("Các nhóm từ $[50; 60)$ đến $[90; 100)$ có R bằng:", ["$50$", "$40$", "$60$", "$45$"], 0, "$R = 100 - 50 = 50$.")
        ]),
        ("Khoảng tứ phân vị từ Q1 và Q3", "b9", [
            lambda: ("Cho $Q_1 = 15$ và $Q_3 = 35$. Khoảng tứ phân vị $\\Delta_Q$ bằng:", ["$20$", "$15$", "$25$", "$10$"], 0, "$\\Delta_Q = 35 - 15 = 20$."),
            lambda: ("Mẫu số liệu có $Q_1 = 25$ và $Q_3 = 52$. Giá trị $\\Delta_Q$ là:", ["$27$", "$25$", "$30$", "$22$"], 0, "$\\Delta_Q = 52 - 25 = 27$."),
            lambda: ("Cho $Q_1 = 40$ và $Q_3 = 70$. Tính khoảng tứ phân vị:", ["$30$", "$40$", "$20$", "$35$"], 0, "$\\Delta_Q = 70 - 40 = 30$."),
            lambda: ("Nếu $Q_1 = 10,5$ và $Q_3 = 30,5$ thì $\\Delta_Q$ bằng:", ["$20$", "$10$", "$15$", "$25$"], 0, "$\\Delta_Q = 30,5 - 10,5 = 20$.")
        ]),
        ("Xác định nhóm chứa Q1", "b9", [
            lambda: ("Bảng số liệu có $n = 40$. Nhóm chứa tứ phân vị thứ nhất $Q_1$ tương ứng vị trí tích luỹ:", ["$10$", "$20$", "$30$", "$5$"], 0, "$n/4 = 40/4 = 10$."),
            lambda: ("Cỡ mẫu $n = 60$. Nhóm chứa $Q_1$ ứng với tần số tích luỹ ít nhất:", ["$15$", "$30$", "$45$", "$20$"], 0, "$n/4 = 15$."),
            lambda: ("Cho $n = 100$. Tứ phân vị $Q_1$ rơi vào nhóm có tích luỹ ít nhất:", ["$25$", "$50$", "$75$", "$20$"], 0, "$n/4 = 25$."),
            lambda: ("Cỡ mẫu $n = 80$. Tần số tích luỹ để xác định $Q_1$ là:", ["$20$", "$40$", "$60$", "$10$"], 0, "$n/4 = 20$.")
        ]),
        ("Xác định nhóm chứa Q3", "b9", [
            lambda: ("Bảng số liệu có $n = 40$. Nhóm chứa tứ phân vị thứ ba $Q_3$ ứng với tích luỹ:", ["$30$", "$10$", "$20$", "$35$"], 0, "$3n/4 = 3(40)/4 = 30$."),
            lambda: ("Cỡ mẫu $n = 60$. Nhóm chứa $Q_3$ có tần số tích luỹ tối thiểu:", ["$45$", "$15$", "$30$", "$50$"], 0, "$3(60)/4 = 45$."),
            lambda: ("Cho $n = 100$. Nhóm chứa $Q_3$ ứng với tích luỹ ít nhất:", ["$75$", "$25$", "$50$", "$80$"], 0, "$3n/4 = 75$."),
            lambda: ("Cỡ mẫu $n = 80$. Giá trị tích luỹ để tìm $Q_3$ là:", ["$60$", "$20$", "$40$", "$70$"], 0, "$3(80)/4 = 60$.")
        ]),
        ("Tính Q1 ghép nhóm cụ thể", "b9", [
            lambda: ("Nhóm chứa $Q_1$ là $[10; 20)$ với $n = 40, C = 6, n_p = 8$. Giá trị $Q_1$ là:", ["$15$", "$14$", "$16$", "$12$"], 0, "$Q_1 = 10 + \\frac{10-6}{8} \\cdot 10 = 15$."),
            lambda: ("Tính $Q_1$ với nhóm $[20; 30)$, $n = 80, C = 15, n_p = 10$:", ["$25$", "$24$", "$26$", "$28$"], 0, "$Q_1 = 20 + \\frac{20-15}{10} \\cdot 10 = 25$."),
            lambda: ("Nhóm chứa $Q_1$ là $[0; 10)$ với $n = 40, C = 5, n_p = 10$. Tính $Q_1$:", ["$5$", "$4$", "$6$", "$8$"], 0, "$Q_1 = 0 + \\frac{10-5}{10} \\cdot 10 = 5$."),
            lambda: ("Cho nhóm $[30; 40)$ chứa $Q_1$, $n = 40, C = 8, n_p = 4$. Giá trị $Q_1$ bằng:", ["$35$", "$32$", "$36$", "$38$"], 0, "$Q_1 = 30 + \\frac{10-8}{4} \\cdot 10 = 35$.")
        ]),
        ("Tính Q3 ghép nhóm cụ thể", "b9", [
            lambda: ("Nhóm chứa $Q_3$ là $[30; 40)$ với $n = 40, C = 26, n_q = 8$. Giá trị $Q_3$ là:", ["$35$", "$34$", "$36$", "$38$"], 0, "$Q_3 = 30 + \\frac{30-26}{8} \\cdot 10 = 35$."),
            lambda: ("Tính $Q_3$ với nhóm $[40; 50)$, $n = 80, C = 55, n_q = 10$:", ["$45$", "$44$", "$46$", "$48$"], 0, "$Q_3 = 40 + \\frac{60-55}{10} \\cdot 10 = 45$."),
            lambda: ("Cho nhóm $[50; 60)$ chứa $Q_3$, $n = 40, C = 28, n_q = 4$. Tính $Q_3$:", ["$55$", "$54$", "$56$", "$58$"], 0, "$Q_3 = 50 + \\frac{30-28}{4} \\cdot 10 = 55$."),
            lambda: ("Tính $Q_3$ với nhóm $[20; 30)$, $n = 40, C = 25, n_q = 10$:", ["$25$", "$24$", "$26$", "$28$"], 0, "$Q_3 = 20 + \\frac{30-25}{10} \\cdot 10 = 25$.")
        ]),
        ("Ranh giới giá trị ngoại lai", "b9", [
            lambda: ("Cho $Q_1 = 20$ và $Q_3 = 40$. Ranh giới trên của giá trị ngoại lai là:", ["$70$", "$60$", "$80$", "$65$"], 0, "$\\Delta_Q = 20 \\Rightarrow Q_3 + 1,5(20) = 40 + 30 = 70$."),
            lambda: ("Biết $Q_1 = 15, Q_3 = 25$. Ranh giới trên để xác định ngoại lai là:", ["$40$", "$35$", "$45$", "$50$"], 0, "$\\Delta_Q = 10 \\Rightarrow 25 + 15 = 40$."),
            lambda: ("Cho $Q_1 = 30, Q_3 = 50$. Ranh giới dưới ngoại lai bằng:", ["$0$", "$10$", "$-10$", "$5$"], 0, "$\\Delta_Q = 20 \\Rightarrow 30 - 1,5(20) = 0$."),
            lambda: ("Nếu $Q_1 = 10, Q_3 = 20$. Ranh giới dưới ngoại lai là:", ["$-5$", "$0$", "$5$", "$-10$"], 0, "$10 - 1,5(10) = -5$.")
        ]),
        ("Tính phương sai mẫu hai nhóm đối xứng", "b10", [
            lambda: ("Hai nhóm $[0; 10)$ và $[10; 20)$ có cùng tần số. Phương sai $s^2$ bằng:", ["$25$", "$50$", "$10$", "$100$"], 0, "Đại diện 5 và 15, $\\bar{x} = 10 \\Rightarrow s^2 = 25$."),
            lambda: ("Mẫu có hai nhóm $[10; 30)$ và $[30; 50)$ có tần số bằng nhau. Phương sai $s^2$ là:", ["$100$", "$50$", "$200$", "$25$"], 0, "Đại diện 20 và 40, $\\bar{x} = 30 \\Rightarrow s^2 = 100$."),
            lambda: ("Hai nhóm $[20; 40)$ và $[40; 60)$ có cùng tần số. Phương sai bằng:", ["$100$", "$50$", "$200$", "$40$"], 0, "Đại diện 30 và 50, $\\bar{x} = 40 \\Rightarrow s^2 = 100$."),
            lambda: ("Cho hai nhóm $[0; 20)$ và $[20; 40)$ có cùng tần số. Phương sai $s^2$ là:", ["$100$", "$50$", "$200$", "$20$"], 0, "$s^2 = 100$.")
        ]),
        ("Tính độ lệch chuẩn mẫu hai nhóm", "b10", [
            lambda: ("Hai nhóm $[0; 10)$ và $[10; 20)$ có cùng tần số. Độ lệch chuẩn s bằng:", ["$5$", "$25$", "$10$", "$2,5$"], 0, "$s = \\sqrt{25} = 5$."),
            lambda: ("Mẫu có hai nhóm $[10; 30)$ và $[30; 50)$ có cùng tần số. Độ lệch chuẩn s là:", ["$10$", "$100$", "$5$", "$20$"], 0, "$s = \\sqrt{100} = 10$."),
            lambda: ("Cho phương sai $s^2 = 144$. Độ lệch chuẩn của mẫu bằng:", ["$12$", "$14$", "$\\sqrt{12}$", "$144$"], 0, "$s = \\sqrt{144} = 12$."),
            lambda: ("Phương sai của mẫu bằng 81. Độ lệch chuẩn s bằng:", ["$9$", "$81$", "$18$", "$\\sqrt{9}$"], 0, "$s = \\sqrt{81} = 9$.")
        ]),
        ("So sánh độ phân tán hai lớp học", "b10", [
            lambda: ("Lớp A có $s = 1,2$ điểm, lớp B có $s = 1,8$ điểm. Kết luận nào đúng?", ["Lớp A có điểm số đồng đều hơn lớp B", "Lớp B có điểm số đồng đều hơn lớp A", "Hai lớp đều như nhau", "Lớp B có nhiều bạn giỏi hơn"], 0, "Độ lệch chuẩn nhỏ hơn nghĩa là độ phân tán nhỏ hơn, điểm đều hơn."),
            lambda: ("Tổ 1 có $s = 0,8$ kg, tổ 2 có $s = 1,5$ kg. Cân nặng của tổ nào đồng đều hơn?", ["Tổ 1 đồng đều hơn", "Tổ 2 đồng đều hơn", "Hai tổ như nhau", "Không xác định"], 0, "Tổ 1 có độ lệch chuẩn nhỏ hơn nên đồng đều hơn."),
            lambda: ("Hai vận động viên có cùng điểm bắn trung bình, $s_1 = 0,5$ và $s_2 = 1,0$. Vận động viên nào ổn định hơn?", ["Vận động viên 1", "Vận động viên 2", "Hai người như nhau", "Không so sánh được"], 0, "VĐV 1 có độ lệch chuẩn nhỏ hơn nên bắn ổn định hơn."),
            lambda: ("Quy trình A có $s = 0,2$ mm, quy trình B có $s = 0,6$ mm. Quy trình nào chính xác hơn?", ["Quy trình A", "Quy trình B", "Cả hai bằng nhau", "Không có cơ sở"], 0, "Quy trình A có sai số chuẩn nhỏ hơn.")
        ]),
        ("Ứng dụng tài chính mức độ rủi ro", "b10", [
            lambda: ("Cổ phiếu X có độ lệch chuẩn lợi nhuận $s = 5\\%$, cổ phiếu Y có $s = 12\\%$. Cổ phiếu nào an toàn hơn (ít rủi ro hơn)?", ["Cổ phiếu X", "Cổ phiếu Y", "Hai cổ phiếu rủi ro như nhau", "Không so sánh được"], 0, "Độ lệch chuẩn nhỏ hơn đồng nghĩa với biến động giá thấp hơn, ít rủi ro hơn."),
            lambda: ("Quỹ đầu tư A có $s = 8\\%$, quỹ B có $s = 15\\%$. Quỹ nào biến động mạnh hơn?", ["Quỹ B", "Quỹ A", "Hai quỹ biến động như nhau", "Không xác định"], 0, "Quỹ B có độ lệch chuẩn lớn hơn nên biến động mạnh hơn."),
            lambda: ("Để đầu tư an toàn, nhà đầu tư nên chọn danh mục có độ lệch chuẩn:", ["Nhỏ", "Lớn", "Bằng 0", "Vô hạn"], 0, "Độ lệch chuẩn nhỏ đại diện cho mức độ biến động thấp."),
            lambda: ("Tỉ suất sinh lời của hai dự án như nhau. Dự án 1 có $s = 3\\%$, dự án 2 có $s = 7\\%$. Dự án nào rủi ro cao hơn?", ["Dự án 2", "Dự án 1", "Hai dự án rủi ro ngang nhau", "Không có rủi ro"], 0, "Dự án 2 có độ lệch chuẩn lớn hơn nên rủi ro cao hơn.")
        ]),
        ("Ý nghĩa độ lệch chuẩn trong kiểm soát chất lượng", "b10", [
            lambda: ("Trong dây chuyền sản xuất bulông, độ lệch chuẩn kích thước đường kính càng nhỏ thì:", ["Tỉ lệ phế phẩm càng thấp, chất lượng càng cao", "Tỉ lệ phế phẩm càng cao", "Tốc độ sản xuất càng chậm", "Không ảnh hưởng"], 0, "Sai số càng nhỏ thì sản phẩm càng chuẩn xác, ít phế phẩm."),
            lambda: ("Máy đóng gói sữa có dung tích trung bình 180 ml, độ lệch chuẩn $s = 1\\text{ ml}$. Khẳng định nào đúng?", ["Dung tích các hộp sữa rất đồng đều quanh mức 180 ml", "Các hộp sữa lệch nhau rất nhiều", "Có nhiều hộp bị rỗng", "Máy bị lỗi nặng"], 0, "Sai lệch chỉ 1 ml trên 180 ml là rất nhỏ, chất lượng đồng đều."),
            lambda: ("Để đạt chuẩn ISO trong sản xuất, độ lệch chuẩn của các thông số kỹ thuật phải:", ["Nằm trong giới hạn kiểm soát cho phép (càng nhỏ càng tốt)", "Càng lớn càng tốt", "Bằng trung bình", "Không cần đo"], 0, "Cần kiểm soát độ lệch chuẩn ở mức tối thiểu cho phép."),
            lambda: ("Hai lô hàng nước ngọt: Lô 1 có $s = 2\\text{ ml}$, Lô 2 có $s = 5\\text{ ml}$. Lô hàng nào đạt chuẩn chất lượng đồng đều hơn?", ["Lô 1", "Lô 2", "Cả hai như nhau", "Không đánh giá được"], 0, "Lô 1 có độ phân tán nhỏ hơn.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c3-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 biến thể = 12 câu
    vd_configs = [
        ("Tính phương sai mẫu ghép nhóm số nguyên", "b10", [
            lambda: ("Cho mẫu số liệu ghép nhóm gồm hai nhóm $[0; 10)$ có tần số 5 và $[10; 20)$ có tần số 5. Phương sai $s^2$ bằng:", ["$25$", "$50$", "$10$", "$100$"], 0, "Giá trị đại diện: $c_1 = 5, c_2 = 15$. Số trung bình $\\bar{x} = 10$. $s^2 = \\frac{5(5-10)^2 + 5(15-10)^2}{10} = \\frac{5(25) + 5(25)}{10} = 25$."),
            lambda: ("Mẫu có hai nhóm $[10; 20)$ có 4 và $[20; 30)$ có 4. Phương sai $s^2$ là:", ["$25$", "$15$", "$20$", "$50$"], 0, "Trung bình bằng 20. $s^2 = \\frac{4(15-20)^2 + 4(25-20)^2}{8} = 25$."),
            lambda: ("Cho hai nhóm $[0; 20)$ và $[20; 40)$ có tần số bằng nhau. Phương sai của mẫu bằng:", ["$100$", "$50$", "$200$", "$20$"], 0, "Giá trị đại diện: 10 và 30, trung bình bằng 20. $s^2 = \\frac{(10-20)^2 + (30-20)^2}{2} = 100$."),
            lambda: ("Mẫu có ba nhóm $[0; 10), [10; 20), [20; 30)$ có tần số tương ứng $2, 6, 2$. Phương sai của mẫu là:", ["$40$", "$50$", "$25$", "$30$"], 0, "Đại diện: 5, 15, 25. $\\bar{x} = 15$. $s^2 = \\frac{2(5-15)^2 + 6(15-15)^2 + 2(25-15)^2}{10} = \\frac{200 + 0 + 200}{10} = 40$.")
        ]),
        ("Tính độ lệch chuẩn của mẫu ghép nhóm", "b10", [
            lambda: ("Cho mẫu số liệu có hai nhóm $[0; 10)$ và $[10; 20)$ cùng tần số. Độ lệch chuẩn s bằng:", ["$5$", "$25$", "$10$", "$2,5$"], 0, "$s^2 = 25 \\Rightarrow s = \\sqrt{25} = 5$."),
            lambda: ("Mẫu có hai nhóm $[20; 40)$ và $[40; 60)$ có tần số bằng nhau. Độ lệch chuẩn s là:", ["$10$", "$100$", "$5$", "$20$"], 0, "Đại diện 30 và 50, trung bình 40. $s^2 = 100 \\Rightarrow s = 10$."),
            lambda: ("Mẫu có phương sai $s^2 = 49$. Độ lệch chuẩn của mẫu bằng:", ["$7$", "$14$", "$\\sqrt{7}$", "$49$"], 0, "$s = \\sqrt{49} = 7$."),
            lambda: ("Hai nhóm $[10; 30)$ và $[30; 50)$ có cùng tần số. Độ lệch chuẩn s bằng:", ["$10$", "$20$", "$100$", "$5$"], 0, "Đại diện 20 và 40, $s = \\sqrt{100} = 10$.")
        ]),
        ("Xác định giá trị ngoại lai cụ thể", "b9", [
            lambda: ("Một mẫu có $Q_1 = 20, Q_3 = 40$. Giá trị nào sau đây là giá trị ngoại lai?", ["$75$", "$25$", "$35$", "$65$"], 0, "$\\Delta_Q = 20$. Giới hạn trên là $Q_3 + 1,5\\Delta_Q = 40 + 30 = 70$. Giá trị 75 > 70 nên là giá trị ngoại lai."),
            lambda: ("Cho $Q_1 = 30, Q_3 = 50$. Giá trị nào dưới đây là ngoại lai phía dưới?", ["$-5$", "$10$", "$5$", "$15$"], 0, "$\\Delta_Q = 20$. Giới hạn dưới: $Q_1 - 1,5\\Delta_Q = 30 - 30 = 0$. Giá trị $-5 < 0$ là ngoại lai."),
            lambda: ("Cho $Q_1 = 15, Q_3 = 25$. Giá trị nào sau đây là giá trị ngoại lai?", ["$45$", "$20$", "$30$", "$35$"], 0, "$\\Delta_Q = 10$. Ranh giới trên là $25 + 15 = 40$. Giá trị 45 > 40 là ngoại lai."),
            lambda: ("Mẫu số liệu có $Q_1 = 50, Q_3 = 80$. Điểm ngoại lai là:", ["$130$", "$70$", "$90$", "$120$"], 0, "$\\Delta_Q = 30$. Ranh giới trên: $80 + 1,5(30) = 125$. Giá trị 130 > 125 là ngoại lai.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c3-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb = [
        ("Khoảng biến thiên cơ bản", "b9", [
            ("Mẫu số liệu ghép nhóm từ $[10; 20)$ đến $[40; 50)$. Khoảng biến thiên R bằng bao nhiêu?", 40, "$R = 50 - 10 = 40$."),
            ("Cho các nhóm từ $[0; 10)$ đến $[50; 60)$. Giá trị của R là:", 60, "$R = 60 - 0 = 60$."),
            ("Khoảng biến thiên của mẫu từ $[20; 30)$ đến $[70; 80)$ bằng:", 60, "$R = 80 - 20 = 60$."),
            ("Nhóm đầu là $[5; 15)$ và nhóm cuối là $[35; 45)$. Khoảng biến thiên R bằng:", 40, "$R = 45 - 5 = 40$."),
            ("Mẫu từ $[100; 120)$ đến $[180; 200)$ có R bằng:", 100, "$R = 200 - 100 = 100$.")
        ]),
        ("Khoảng tứ phân vị cơ bản", "b9", [
            ("Cho $Q_1 = 20$ và $Q_3 = 45$. Khoảng tứ phân vị $\\Delta_Q$ bằng bao nhiêu?", 25, "$\\Delta_Q = 45 - 20 = 25$."),
            ("Biết $Q_1 = 15$ và $Q_3 = 35$. Giá trị của $\\Delta_Q$ là:", 20, "$\\Delta_Q = 35 - 15 = 20$."),
            ("Cho $Q_1 = 30$ và $Q_3 = 60$. Khoảng tứ phân vị bằng:", 30, "$\\Delta_Q = 60 - 30 = 30$."),
            ("Tìm $\\Delta_Q$ biết $Q_1 = 18$ và $Q_3 = 34$:", 16, "$\\Delta_Q = 34 - 18 = 16$."),
            ("Cho $Q_1 = 22$ và $Q_3 = 50$. Tính $\\Delta_Q$:", 28, "$\\Delta_Q = 50 - 22 = 28$.")
        ]),
        ("Độ lệch chuẩn từ phương sai", "b10", [
            ("Cho phương sai $s^2 = 25$. Độ lệch chuẩn s bằng bao nhiêu?", 5, "$s = \\sqrt{25} = 5$."),
            ("Nếu $s^2 = 36$ thì độ lệch chuẩn s bằng:", 6, "$s = \\sqrt{36} = 6$."),
            ("Phương sai của mẫu bằng 64. Độ lệch chuẩn s là:", 8, "$s = \\sqrt{64} = 8$."),
            ("Biết $s^2 = 81$. Giá trị của độ lệch chuẩn là:", 9, "$s = \\sqrt{81} = 9$."),
            ("Cho $s^2 = 100$. Tính độ lệch chuẩn s:", 10, "$s = \\sqrt{100} = 10$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Tính phương sai mẫu đối xứng", "b10", [
            ("Cho hai nhóm $[0; 10)$ và $[10; 20)$ cùng tần số bằng nhau. Phương sai $s^2$ bằng bao nhiêu?", 25, "$s^2 = 25$."),
            ("Hai nhóm $[10; 30)$ và $[30; 50)$ có tần số bằng nhau. Phương sai $s^2$ bằng:", 100, "$s^2 = 100$."),
            ("Hai nhóm $[20; 40)$ và $[40; 60)$ có tần số bằng nhau. Giá trị của $s^2$ là:", 100, "$s^2 = 100$."),
            ("Hai nhóm $[0; 20)$ và $[20; 40)$ có cùng tần số. Tính $s^2$:", 100, "$s^2 = 100$.")
        ]),
        ("Tính độ lệch chuẩn của hai nhóm", "b10", [
            ("Hai nhóm $[0; 10)$ và $[10; 20)$ có tần số bằng nhau. Độ lệch chuẩn s bằng:", 5, "$s = \\sqrt{25} = 5$."),
            ("Hai nhóm $[0; 20)$ và $[20; 40)$ có cùng tần số. Độ lệch chuẩn s là:", 10, "$s = \\sqrt{100} = 10$."),
            ("Hai nhóm $[20; 40)$ và $[40; 60)$ có cùng tần số. Tính s:", 10, "$s = 10$."),
            ("Cho mẫu có phương sai $s^2 = 144$. Độ lệch chuẩn bằng:", 12, "$s = \\sqrt{144} = 12$.")
        ]),
        ("Ranh giới trên của giá trị ngoại lai", "b9", [
            ("Cho $Q_1 = 10, Q_3 = 20$. Ranh giới trên $Q_3 + 1,5\\Delta_Q$ bằng bao nhiêu?", 35, "$20 + 1,5(10) = 35$."),
            ("Cho $Q_1 = 20, Q_3 = 40$. Giá trị $Q_3 + 1,5\\Delta_Q$ bằng:", 70, "$40 + 1,5(20) = 70$."),
            ("Biết $Q_1 = 30, Q_3 = 50$. Tính ranh giới trên:", 80, "$50 + 1,5(20) = 80$."),
            ("Cho $Q_1 = 15, Q_3 = 25$. Ranh giới trên ngoại lai là:", 40, "$25 + 1,5(10) = 40$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Phương sai mẫu 3 nhóm đối xứng", "b10", [
            ("Mẫu có ba nhóm $[0; 10), [10; 20), [20; 30)$ có tần số $2, 6, 2$. Phương sai $s^2$ bằng bao nhiêu?", 40, "$s^2 = 40$."),
            ("Ba nhóm $[10; 20), [20; 30), [30; 40)$ có tần số $1, 8, 1$. Phương sai $s^2$ là:", 20, "$\\bar{x} = 25$. $s^2 = \\frac{1(15-25)^2 + 1(35-25)^2}{10} = 200/10 = 20$."),
            ("Cho ba nhóm $[0; 20), [20; 40), [40; 60)$ có tần số $1, 8, 1$. Tính phương sai $s^2$:", 80, "$s^2 = \\frac{1(10-30)^2 + 1(50-30)^2}{10} = 800/10 = 80$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b9", "sgk_title": "Bài 9. Khoảng biến thiên và khoảng tứ phân vị"},
        {"lesson_id": "b10", "sgk_title": "Bài 10. Phương sai và độ lệch chuẩn"}
    ]
    save_bank("c3", "Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm", lessons, mc, sa)

if __name__ == "__main__":
    gen_c3()
