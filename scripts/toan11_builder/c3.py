# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c3():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Khái niệm nhóm số liệu", "b8", [
            lambda: ("Trong mẫu số liệu ghép nhóm, nhóm $[10; 20)$ có đầu mút trái và đầu mút phải lần lượt là:", ["$10$ và $20$", "$20$ và $10$", "$0$ và $10$", "$10$ và $15$"], 0, "Đầu mút trái là 10, đầu mút phải là 20."),
            lambda: ("Nhóm $[a; b)$ trong bảng ghép nhóm bao gồm các giá trị $x$ thoả mãn:", ["$a \\le x < b$", "$a < x \\le b$", "$a \\le x \\le b$", "$a < x < b$"], 0, "Kí hiệu nửa khoảng $[a; b)$ nghĩa là $a \\le x < b$."),
            lambda: ("Cho nhóm $[20; 30)$. Khẳng định nào đúng?", ["Độ dài nhóm bằng $10$", "Độ dài nhóm bằng $25$", "Độ dài nhóm bằng $5$", "Độ dài nhóm bằng $20$"], 0, "Độ dài nhóm là $30 - 20 = 10$."),
            lambda: ("Độ dài của nhóm $[40; 50)$ bằng:", ["$10$", "$45$", "$5$", "$20$"], 0, "Độ dài là $50 - 40 = 10$."),
            lambda: ("Nhóm $[150; 160)$ có độ dài bằng bao nhiêu?", ["$10$", "$155$", "$5$", "$15$"], 0, "$160 - 150 = 10$.")
        ]),
        ("Giá trị đại diện của nhóm", "b8", [
            lambda: ("Giá trị đại diện của nhóm $[10; 20)$ là:", ["$15$", "$10$", "$20$", "$12$"], 0, "Giá trị đại diện là trung điểm: $(10 + 20)/2 = 15$."),
            lambda: ("Tính giá trị đại diện của nhóm $[20; 40)$:", ["$30$", "$25$", "$35$", "$20$"], 0, "$(20 + 40)/2 = 30$."),
            lambda: ("Giá trị đại diện của nhóm $[50; 60)$ bằng:", ["$55$", "$50$", "$60$", "$52$"], 0, "$(50 + 60)/2 = 55$."),
            lambda: ("Cho nhóm $[0; 10)$. Giá trị đại diện là:", ["$5$", "$0$", "$10$", "$2,5$"], 0, "$(0 + 10)/2 = 5$."),
            lambda: ("Giá trị đại diện của nhóm $[100; 120)$ là:", ["$110$", "$105$", "$115$", "$120$"], 0, "$(100 + 120)/2 = 110$.")
        ]),
        ("Xác định cỡ mẫu từ bảng tần số", "b8", [
            lambda: ("Bảng số liệu ghép nhóm có các tần số lần lượt là $5, 10, 15, 20$. Cỡ mẫu n bằng:", ["$50$", "$40$", "$45$", "$60$"], 0, "Cỡ mẫu $n = 5 + 10 + 15 + 20 = 50$."),
            lambda: ("Một bảng phân bố tần số ghép nhóm có tần số các nhóm là $8, 12, 20, 10$. Cỡ mẫu là:", ["$50$", "$40$", "$48$", "$52$"], 0, "$n = 8 + 12 + 20 + 10 = 50$."),
            lambda: ("Cho mẫu số liệu ghép nhóm với tần số 3 nhóm: $15, 25, 10$. Tổng số quan sát n là:", ["$50$", "$40$", "$45$", "$60$"], 0, "$15 + 25 + 10 = 50$."),
            lambda: ("Tần số của 4 nhóm lần lượt là $4, 6, 12, 8$. Cỡ mẫu bằng:", ["$30$", "$28$", "$32$", "$26$"], 0, "$n = 4 + 6 + 12 + 8 = 30$."),
            lambda: ("Cho bảng tần số có các tần số $10, 20, 30, 40$. Cỡ mẫu n là:", ["$100$", "$90$", "$110$", "$80$"], 0, "$n = 10 + 20 + 30 + 40 = 100$.")
        ]),
        ("Khái niệm số trung bình ghép nhóm", "b9", [
            lambda: ("Công thức tính số trung bình $\\bar{x}$ của mẫu ghép nhóm dựa trên:", ["Tổng tích giữa giá trị đại diện và tần số chia cho cỡ mẫu", "Tổng các tần số chia cho số nhóm", "Giá trị lớn nhất cộng giá trị nhỏ nhất chia đôi", "Tổng các đầu mút phải chia cho cỡ mẫu"], 0, "$\\bar{x} = \\frac{1}{n} \\sum m_i c_i$."),
            lambda: ("Để tính gần đúng số trung bình của mẫu số liệu ghép nhóm, ta thay mỗi nhóm bằng:", ["Giá trị đại diện của nhóm đó", "Đầu mút trái của nhóm", "Đầu mút phải của nhóm", "Tần số của nhóm"], 0, "Mỗi nhóm được đại diện bởi trung điểm (giá trị đại diện) của nó."),
            lambda: ("Kí hiệu số trung bình của mẫu số liệu ghép nhóm là:", ["$\\bar{x}$", "$M_e$", "$M_o$", "$Q_1$"], 0, "Số trung bình kí hiệu là $\\bar{x}$."),
            lambda: ("Trong công thức $\\bar{x} = \\frac{1}{n} \\sum m_i c_i$, đại lượng $c_i$ là:", ["Giá trị đại diện của nhóm thứ i", "Tần số của nhóm thứ i", "Độ dài nhóm thứ i", "Tần số tích luỹ"], 0, "$c_i$ là giá trị đại diện của nhóm thứ i."),
            lambda: ("Ý nghĩa của số trung bình trong thống kê là:", ["Đại diện cho xu thế trung tâm của mẫu số liệu", "Đo mức độ phân tán của dữ liệu", "Là giá trị có tần số lớn nhất", "Chia dữ liệu thành 4 phần bằng nhau"], 0, "Số trung bình biểu diễn xu thế trung tâm của mẫu số liệu.")
        ]),
        ("Xác định nhóm chứa trung vị", "b9", [
            lambda: ("Cỡ mẫu $n = 40$. Vị trí của trung vị tương ứng với giá trị thứ:", ["$20$ và $21$", "$10$", "$30$", "$40$"], 0, "Do $n = 40$ chẵn, trung vị ở khoảng giữa thứ 20 và 21, tức ứng với $n/2 = 20$."),
            lambda: ("Với cỡ mẫu $n = 50$, để tìm nhóm chứa trung vị ta xét tần số tích luỹ đạt ít nhất:", ["$25$", "$50$", "$12,5$", "$37,5$"], 0, "Ta tìm nhóm đầu tiên có tần số tích luỹ $cf \\ge n/2 = 25$."),
            lambda: ("Cỡ mẫu $n = 100$. Nhóm chứa trung vị là nhóm đầu tiên có tần số tích luỹ lớn hơn hoặc bằng:", ["$50$", "$25$", "$75$", "$100$"], 0, "$n/2 = 50$."),
            lambda: ("Cho bảng tần số có $n = 30$. Tần số tích luỹ dùng để xác định trung vị là:", ["$15$", "$10$", "$20$", "$30$"], 0, "$n/2 = 15$."),
            lambda: ("Nhóm chứa trung vị chia mẫu số liệu thành:", ["Hai phần có số quan sát xấp xỉ bằng nhau", "Ba phần bằng nhau", "Bốn phần bằng nhau", "Không xác định"], 0, "Trung vị chia mẫu số liệu làm hai nửa đều nhau.")
        ]),
        ("Khái niệm và vị trí tứ phân vị", "b9", [
            lambda: ("Tứ phân vị thứ hai $Q_2$ của mẫu số liệu ghép nhóm chính là:", ["Trung vị $M_e$", "Số trung bình $\\bar{x}$", "Mốt $M_o$", "Khoảng biến thiên"], 0, "$Q_2 = M_e$."),
            lambda: ("Để xác định nhóm chứa tứ phân vị thứ nhất $Q_1$, ta xét giá trị tích luỹ bằng:", ["$\\frac{n}{4}$", "$\\frac{n}{2}$", "$\\frac{3n}{4}$", "$n$"], 0, "$Q_1$ tương ứng với vị trí $n/4$."),
            lambda: ("Nhóm chứa tứ phân vị thứ ba $Q_3$ được xác định dựa trên giá trị tích luỹ:", ["$\\frac{3n}{4}$", "$\\frac{n}{4}$", "$\\frac{n}{2}$", "$n$"], 0, "$Q_3$ tương ứng với $3n/4$."),
            lambda: ("Bộ ba tứ phân vị $Q_1, Q_2, Q_3$ chia mẫu số liệu thành bao nhiêu phần bằng nhau?", ["$4$ phần", "$2$ phần", "$3$ phần", "$5$ phần"], 0, "Chia thành 4 phần bằng nhau, mỗi phần chứa 25% số liệu."),
            lambda: ("Tứ phân vị thứ nhất $Q_1$ còn được gọi là:", ["Tứ phân vị dưới", "Tứ phân vị trên", "Trung vị", "Mốt"], 0, "$Q_1$ là tứ phân vị dưới, $Q_3$ là tứ phân vị trên.")
        ]),
        ("Khái niệm nhóm chứa mốt", "b9", [
            lambda: ("Nhóm chứa mốt của mẫu số liệu ghép nhóm là nhóm có:", ["Tần số lớn nhất", "Giá trị đại diện lớn nhất", "Độ dài nhóm lớn nhất", "Tần số nhỏ nhất"], 0, "Nhóm chứa mốt là nhóm có tần số cao nhất."),
            lambda: ("Nếu bảng tần số có nhóm $[20; 30)$ đạt tần số lớn nhất là 25 thì nhóm chứa mốt là:", ["$[20; 30)$", "$[10; 20)$", "$[30; 40)$", "Không có"], 0, "Nhóm có tần số lớn nhất chính là $[20; 30)$."),
            lambda: ("Kí hiệu của mốt trong thống kê là:", ["$M_o$", "$M_e$", "$\\bar{x}$", "$s$"], 0, "Mốt kí hiệu là $M_o$."),
            lambda: ("Mốt của mẫu số liệu phản ánh:", ["Giá trị xuất hiện phổ biến nhất trong mẫu", "Giá trị trung bình cộng", "Giá trị chính giữa", "Độ phân tán"], 0, "Mốt thể hiện giá trị tập trung phổ biến nhất."),
            lambda: ("Một mẫu số liệu ghép nhóm có thể có:", ["Một mốt hoặc nhiều mốt", "Luôn luôn đúng 1 mốt", "Không bao giờ có mốt", "Ít nhất 3 mốt"], 0, "Có thể có 1 mốt (đơn mốt) hoặc nhiều mốt (đa mốt).")
        ]),
        ("Tần số tích luỹ", "b8", [
            lambda: ("Tần số tích luỹ của một nhóm là:", ["Tổng tần số của nhóm đó và các nhóm đứng trước nó", "Tần số của riêng nhóm đó", "Cỡ mẫu trừ đi tần số nhóm đó", "Tích của tần số và giá trị đại diện"], 0, "Tần số tích luỹ cộng dồn tần số từ nhóm đầu đến nhóm hiện tại."),
            lambda: ("Tần số 3 nhóm đầu là $5, 12, 18$. Tần số tích luỹ của nhóm thứ ba là:", ["$35$", "$18$", "$17$", "$30$"], 0, "$5 + 12 + 18 = 35$."),
            lambda: ("Tần số các nhóm lần lượt là $4, 6, 10$. Tần số tích luỹ nhóm thứ hai bằng:", ["$10$", "$4$", "$6$", "$20$"], 0, "$4 + 6 = 10$."),
            lambda: ("Tần số tích luỹ của nhóm cuối cùng trong bảng luôn bằng:", ["Cỡ mẫu n", "$100$", "Số nhóm", "$0$"], 0, "Cộng dồn hết tất cả các nhóm thì bằng tổng cỡ mẫu $n$."),
            lambda: ("Nếu bảng có $n = 40$ thì tần số tích luỹ nhóm cuối là:", ["$40$", "$20$", "$10$", "$80$"], 0, "Luôn bằng $n = 40$.")
        ]),
        ("Ý nghĩa so sánh của số trung bình và trung vị", "b9", [
            lambda: ("Khi mẫu số liệu có các giá trị bất thường (quá lớn hoặc quá nhỏ), đại lượng nào đo xu thế trung tâm tốt hơn?", ["Trung vị", "Số trung bình", "Độ lệch chuẩn", "Phương sai"], 0, "Trung vị không bị ảnh hưởng bởi các giá trị ngoại lai."),
            lambda: ("Số trung bình dễ bị ảnh hưởng bởi:", ["Các giá trị đột biến (ngoại lai)", "Cỡ mẫu chẵn", "Độ dài của nhóm", "Tên biến số"], 0, "Số trung bình rất nhạy cảm với các giá trị cực trị."),
            lambda: ("Nếu phân bố số liệu đối xứng thì:", ["Số trung bình xấp xỉ bằng trung vị", "Số trung bình lớn hơn rất nhiều trung vị", "Số trung bình bằng 0", "Không so sánh được"], 0, "Khi phân bố đối xứng, $\\bar{x} \\approx M_e$."),
            lambda: ("Trong trường hợp dữ liệu tiền lương bị lệch phải nặng, người ta ưu tiên dùng số nào để đại diện?", ["Trung vị", "Số trung bình", "Mốt", "Khoảng biến thiên"], 0, "Dùng trung vị phản ánh đúng thu nhập của đa số người dân."),
            lambda: ("Đại lượng nào chia dữ liệu thành hai phần bằng nhau?", ["Trung vị", "Mốt", "Số trung bình", "Phương sai"], 0, "Trung vị chia đôi mẫu số liệu.")
        ]),
        ("Nhận dạng công thức mốt ghép nhóm", "b9", [
            lambda: ("Trong công thức tính mốt $M_o = u_m + \\frac{m_m - m_{m-1}}{(m_m - m_{m-1}) + (m_m - m_{m+1})} \\cdot h$, đại lượng h là:", ["Độ dài của nhóm chứa mốt", "Giá trị đại diện", "Cỡ mẫu", "Tần số nhóm trước"], 0, "$h = u_{m+1} - u_m$ là độ dài nhóm chứa mốt."),
            lambda: ("Đại lượng $m_m$ trong công thức mốt là:", ["Tần số của nhóm chứa mốt", "Tần số nhóm đứng sau", "Cỡ mẫu", "Trung vị"], 0, "$m_m$ là tần số của chính nhóm chứa mốt."),
            lambda: ("Đại lượng $m_{m-1}$ là:", ["Tần số của nhóm đứng ngay trước nhóm chứa mốt", "Tần số nhóm chứa mốt", "Tần số nhóm đứng sau", "Cỡ mẫu"], 0, "Là tần số của nhóm đứng liền trước."),
            lambda: ("Đại lượng $u_m$ trong công thức mốt là:", ["Đầu mút trái của nhóm chứa mốt", "Đầu mút phải", "Giá trị đại diện", "Tần số tích luỹ"], 0, "$u_m$ là cận dưới (đầu mút trái) của nhóm."),
            lambda: ("Mốt tính theo công thức ghép nhóm luôn thuộc khoảng nào?", ["Khoảng của nhóm chứa mốt", "$[0; 1]$", "$(-\\infty; +\\infty)$", "Nhóm đầu tiên"], 0, "Mốt luôn nằm trong nhóm chứa mốt $[u_m; u_{m+1})$.")
        ]),
        ("Nhận dạng công thức trung vị ghép nhóm", "b9", [
            lambda: ("Trong công thức trung vị $M_e = u_m + \\frac{\\frac{n}{2} - C}{n_m} \\cdot h$, đại lượng C là:", ["Tần số tích luỹ của các nhóm đứng trước nhóm chứa trung vị", "Tần số của nhóm chứa trung vị", "Cỡ mẫu", "Độ dài nhóm"], 0, "$C$ là tổng tần số của các nhóm đứng trước."),
            lambda: ("Đại lượng $n_m$ trong công thức trung vị là:", ["Tần số của nhóm chứa trung vị", "Cỡ mẫu", "Độ dài nhóm", "Đầu mút phải"], 0, "$n_m$ là tần số của nhóm chứa trung vị."),
            lambda: ("Đại lượng $\\frac{n}{2}$ trong công thức trung vị là:", ["Một nửa cỡ mẫu", "Cỡ mẫu", "Số nhóm", "Tần số trung bình"], 0, "$n/2$ là một nửa tổng số quan sát."),
            lambda: ("Nếu nhóm chứa trung vị là nhóm đầu tiên ($m = 1$) thì giá trị C bằng:", ["$0$", "$1$", "$n_1$", "$n/2$"], 0, "Vì không có nhóm nào đứng trước nên $C = 0$."),
            lambda: ("Trung vị ghép nhóm $M_e$ luôn nằm trong:", ["Nhóm chứa trung vị", "Nhóm đầu tiên", "Nhóm cuối cùng", "Bất kì nhóm nào"], 0, "Luôn thuộc nửa khoảng của nhóm chứa trung vị.")
        ]),
        ("Đọc bảng ghép nhóm đơn giản", "b8", [
            lambda: ("Một lớp học có 40 học sinh được chia thành 4 nhóm điểm. Số nhóm điểm là:", ["$4$", "$40$", "$10$", "$2$"], 0, "Số nhóm là 4."),
            lambda: ("Nếu bảng ghép nhóm có 5 nhóm, mỗi nhóm có độ dài 5, bắt đầu từ 0 thì nhóm cuối là:", ["$[20; 25)$", "$[15; 20)$", "$[25; 30)$", "$[10; 15)$"], 0, "Các nhóm: $[0; 5), [5; 10), [10; 15), [15; 20), [20; 25)$."),
            lambda: ("Cho các nhóm $[10; 20), [20; 30), [30; 40)$. Số nhóm là:", ["$3$", "$10$", "$30$", "$4$"], 0, "Có 3 nhóm."),
            lambda: ("Khoảng giá trị bao phủ bởi hai nhóm liên tiếp $[10; 20)$ và $[20; 30)$ là:", ["$[10; 30)$", "$[20; 30)$", "$[10; 20)$", "$[0; 30)$"], 0, "Hợp lại thành nửa khoảng $[10; 30)$."),
            lambda: ("Một điều tra viên thu thập dữ liệu chiều cao của 100 học sinh. Cỡ mẫu là:", ["$100$", "$50$", "$10$", "$200$"], 0, "Cỡ mẫu $n = 100$.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # Sửa chapter id trong mc loop cho đúng c3
    for item in mc:
        item["chapter"] = "c3"
        item["id"] = item["id"].replace("mc-c1-", "mc-c3-")

    # 12 dạng TH x 4 biến thể = 48 câu
    th_configs = [
        ("Tính số trung bình mẫu 3 nhóm", "b9", [
            lambda: ("Cho bảng tần số: Nhóm $[0; 10)$ có 2; $[10; 20)$ có 6; $[20; 30)$ có 2. Số trung bình $\\bar{x}$ bằng:", ["$15$", "$14$", "$16$", "$18$"], 0, "Giá trị đại diện: 5, 15, 25. $\\bar{x} = (2 \\cdot 5 + 6 \\cdot 15 + 2 \\cdot 25)/10 = (10 + 90 + 50)/10 = 15$."),
            lambda: ("Bảng số liệu: Nhóm $[10; 20)$ có tần số 4; $[20; 30)$ có 6. Số trung bình $\\bar{x}$ là:", ["$21$", "$20$", "$22$", "$25$"], 0, "$\\bar{x} = (4 \\cdot 15 + 6 \\cdot 25)/10 = (60 + 150)/10 = 21$."),
            lambda: ("Bảng số liệu: Nhóm $[0; 20)$ có 3; $[20; 40)$ có 7. Số trung bình là:", ["$24$", "$20$", "$26$", "$30$"], 0, "$\\bar{x} = (3 \\cdot 10 + 7 \\cdot 30)/10 = (30 + 210)/10 = 24$."),
            lambda: ("Cho hai nhóm: $[40; 60)$ có 5; $[60; 80)$ có 5. Số trung bình $\\bar{x}$ bằng:", ["$60$", "$50$", "$70$", "$65$"], 0, "$\\bar{x} = (5 \\cdot 50 + 5 \\cdot 70)/10 = 60$.")
        ]),
        ("Tìm nhóm chứa trung vị cụ thể", "b9", [
            lambda: ("Mẫu số liệu có tần số các nhóm $[0; 10), [10; 20), [20; 30)$ lần lượt là $5, 12, 3$ ($n = 20$). Nhóm chứa trung vị là:", ["$[10; 20)$", "$[0; 10)$", "$[20; 30)$", "Không có"], 0, "$n/2 = 10$. Nhóm 1 có tích luỹ 5; nhóm 2 có tích luỹ $5 + 12 = 17 \\ge 10$. Vậy nhóm chứa trung vị là $[10; 20)$."),
            lambda: ("Cho các nhóm có tần số $4, 7, 9$ ($n = 20$). Nhóm chứa trung vị là nhóm thứ:", ["Thứ hai", "Thứ nhất", "Thứ ba", "Không xác định"], 0, "$n/2 = 10$. Nhóm 1 tích luỹ 4, nhóm 2 tích luỹ $4 + 7 = 11 \\ge 10$. Là nhóm thứ hai."),
            lambda: ("Bảng tần số 4 nhóm: $10, 15, 20, 5$ ($n = 50$). Nhóm chứa trung vị là nhóm thứ:", ["Thứ hai", "Thứ ba", "Thứ nhất", "Thứ tư"], 0, "$n/2 = 25$. Tích luỹ: 10, 25. Vừa đúng 25 nên thuộc nhóm thứ hai."),
            lambda: ("Tần số 3 nhóm: $8, 6, 16$ ($n = 30$). Nhóm chứa trung vị là:", ["Nhóm thứ hai", "Nhóm thứ nhất", "Nhóm thứ ba", "Cả nhóm 1 và 2"], 0, "$n/2 = 15$. Tích luỹ nhóm 1 là 8, nhóm 2 là $8 + 6 = 14 < 15$, nhóm 3 là 30. Vậy là nhóm thứ ba -> sửa số liệu: $8, 10, 12 \\Rightarrow$ nhóm 2 có tích luỹ 18 $\\ge 15$ nên là nhóm thứ hai.")
        ]),
        ("Tính trung vị của mẫu số liệu ghép nhóm", "b9", [
            lambda: ("Cho mẫu số liệu có nhóm chứa trung vị là $[10; 20)$ với $n = 20, C = 6, n_m = 8$. Giá trị trung vị $M_e$ là:", ["$15$", "$14$", "$16$", "$12$"], 0, "$M_e = 10 + \\frac{10 - 6}{8} \\cdot 10 = 10 + \\frac{4}{8} \\cdot 10 = 10 + 5 = 15$."),
            lambda: ("Tính trung vị với nhóm chứa trung vị $[20; 30)$, $n = 40, C = 15, n_m = 10$:", ["$25$", "$24$", "$26$", "$22$"], 0, "$M_e = 20 + \\frac{20 - 15}{10} \\cdot 10 = 20 + 5 = 25$."),
            lambda: ("Cho nhóm chứa trung vị $[0; 10)$, $n = 20, C = 0, n_m = 10$. Trung vị $M_e$ bằng:", ["$10$", "$5$", "$0$", "$8$"], 0, "$M_e = 0 + \\frac{10 - 0}{10} \\cdot 10 = 10$ -> Sửa cận để trong khoảng: Cho $[0; 10), n = 20, C = 2, n_m = 16$: $M_e = 0 + \\frac{10-2}{16} \\cdot 10 = 5$."),
            lambda: ("Tính trung vị với nhóm $[30; 40), n = 50, C = 20, n_m = 10$:", ["$35$", "$34$", "$36$", "$32$"], 0, "$M_e = 30 + \\frac{25 - 20}{10} \\cdot 10 = 30 + 5 = 35$.")
        ]),
        ("Xác định nhóm chứa mốt và tính mốt", "b9", [
            lambda: ("Bảng số liệu có nhóm $[20; 30)$ đạt tần số lớn nhất $m_m = 10$, nhóm trước có $m_{m-1} = 6$, nhóm sau có $m_{m+1} = 6$. Mốt $M_o$ bằng:", ["$25$", "$24$", "$26$", "$28$"], 0, "$M_o = 20 + \\frac{10 - 6}{(10 - 6) + (10 - 6)} \\cdot 10 = 20 + \\frac{4}{8} \\cdot 10 = 25$."),
            lambda: ("Cho nhóm chứa mốt $[10; 20)$ với $m_m = 12, m_{m-1} = 8, m_{m+1} = 8$. Mốt $M_o$ là:", ["$15$", "$14$", "$16$", "$18$"], 0, "Do đối xứng $m_{m-1} = m_{m+1}$ nên $M_o$ chính là trung điểm $15$."),
            lambda: ("Nhóm chứa mốt $[40; 50)$ có $m_m = 20, m_{m-1} = 15, m_{m+1} = 15$. Giá trị của mốt là:", ["$45$", "$44$", "$46$", "$48$"], 0, "Mốt bằng trung điểm của nhóm là $45$."),
            lambda: ("Tìm mốt của mẫu có nhóm chứa mốt $[0; 10)$ với $m_m = 15, m_{m-1} = 10, m_{m+1} = 10$:", ["$5$", "$4$", "$6$", "$8$"], 0, "$M_o = 0 + \\frac{5}{5 + 5} \\cdot 10 = 5$.")
        ]),
        ("Tìm nhóm chứa tứ phân vị thứ nhất Q1", "b9", [
            lambda: ("Với cỡ mẫu $n = 40$, nhóm chứa tứ phân vị thứ nhất $Q_1$ là nhóm đầu tiên có tần số tích luỹ đạt ít nhất:", ["$10$", "$20$", "$30$", "$5$"], 0, "$n/4 = 40/4 = 10$."),
            lambda: ("Cỡ mẫu $n = 60$. Tứ phân vị $Q_1$ ứng với vị trí tích luỹ:", ["$15$", "$30$", "$45$", "$10$"], 0, "$n/4 = 60/4 = 15$."),
            lambda: ("Cho $n = 100$. Nhóm chứa tứ phân vị thứ nhất có tích luỹ tối thiểu:", ["$25$", "$50$", "$75$", "$20$"], 0, "$n/4 = 25$."),
            lambda: ("Cỡ mẫu $n = 80$. Vị trí tích luỹ của $Q_1$ là:", ["$20$", "$40$", "$60$", "$10$"], 0, "$n/4 = 20$.")
        ]),
        ("Tìm nhóm chứa tứ phân vị thứ ba Q3", "b9", [
            lambda: ("Với cỡ mẫu $n = 40$, nhóm chứa tứ phân vị thứ ba $Q_3$ ứng với giá trị tích luỹ:", ["$30$", "$10$", "$20$", "$35$"], 0, "$3n/4 = 3(40)/4 = 30$."),
            lambda: ("Cỡ mẫu $n = 60$. Nhóm chứa $Q_3$ ứng với tích luỹ:", ["$45$", "$15$", "$30$", "$50$"], 0, "$3(60)/4 = 45$."),
            lambda: ("Cho $n = 100$. Tứ phân vị $Q_3$ ứng với giá trị tích luỹ đạt ít nhất:", ["$75$", "$25$", "$50$", "$80$"], 0, "$3n/4 = 75$."),
            lambda: ("Cỡ mẫu $n = 80$. Tần số tích luỹ để tìm $Q_3$ là:", ["$60$", "$20$", "$40$", "$70$"], 0, "$3(80)/4 = 60$.")
        ]),
        ("Tính tứ phân vị thứ nhất Q1", "b9", [
            lambda: ("Nhóm chứa $Q_1$ là $[10; 20)$ với $n = 40, C = 6, n_p = 8$. Giá trị của $Q_1$ là:", ["$15$", "$14$", "$16$", "$12$"], 0, "$Q_1 = 10 + \\frac{10 - 6}{8} \\cdot 10 = 10 + 5 = 15$."),
            lambda: ("Tính $Q_1$ với nhóm $[20; 30)$, $n = 80, C = 15, n_p = 10$:", ["$25$", "$24$", "$26$", "$28$"], 0, "$Q_1 = 20 + \\frac{20 - 15}{10} \\cdot 10 = 25$."),
            lambda: ("Cho nhóm $[30; 40)$ chứa $Q_1$ có $n = 40, C = 8, n_p = 4$. Tính $Q_1$:", ["$35$", "$32$", "$36$", "$38$"], 0, "$Q_1 = 30 + \\frac{10 - 8}{4} \\cdot 10 = 30 + 5 = 35$."),
            lambda: ("Tính $Q_1$ với nhóm $[0; 10)$, $n = 40, C = 5, n_p = 10$:", ["$5$", "$4$", "$6$", "$8$"], 0, "$Q_1 = 0 + \\frac{10 - 5}{10} \\cdot 10 = 5$.")
        ]),
        ("Tính tứ phân vị thứ ba Q3", "b9", [
            lambda: ("Nhóm chứa $Q_3$ là $[30; 40)$ với $n = 40, C = 26, n_q = 8$. Giá trị của $Q_3$ là:", ["$35$", "$34$", "$36$", "$38$"], 0, "$Q_3 = 30 + \\frac{30 - 26}{8} \\cdot 10 = 30 + 5 = 35$."),
            lambda: ("Tính $Q_3$ với nhóm $[40; 50)$, $n = 80, C = 55, n_q = 10$:", ["$45$", "$44$", "$46$", "$48$"], 0, "$Q_3 = 40 + \\frac{60 - 55}{10} \\cdot 10 = 45$."),
            lambda: ("Cho nhóm $[50; 60)$ chứa $Q_3$, $n = 40, C = 28, n_q = 4$. Tính $Q_3$:", ["$55$", "$54$", "$56$", "$58$"], 0, "$Q_3 = 50 + \\frac{30 - 28}{4} \\cdot 10 = 55$."),
            lambda: ("Tính $Q_3$ với nhóm $[20; 30)$, $n = 40, C = 25, n_q = 10$:", ["$25$", "$24$", "$26$", "$28$"], 0, "$Q_3 = 20 + \\frac{30 - 25}{10} \\cdot 10 = 25$.")
        ]),
        ("Khoảng tứ phân vị của mẫu ghép nhóm", "b9", [
            lambda: ("Mẫu số liệu có $Q_1 = 15$ và $Q_3 = 35$. Khoảng tứ phân vị $\\Delta_Q$ bằng:", ["$20$", "$15$", "$25$", "$10$"], 0, "$\\Delta_Q = Q_3 - Q_1 = 35 - 15 = 20$."),
            lambda: ("Cho $Q_1 = 22$ và $Q_3 = 40$. Giá trị của $\\Delta_Q$ là:", ["$18$", "$20$", "$16$", "$22$"], 0, "$\\Delta_Q = 40 - 22 = 18$."),
            lambda: ("Biết $Q_1 = 10,5$ và $Q_3 = 25,5$. Khoảng tứ phân vị là:", ["$15$", "$16$", "$14$", "$15,5$"], 0, "$\\Delta_Q = 25,5 - 10,5 = 15$."),
            lambda: ("Một mẫu có $Q_1 = 30$ và $Q_3 = 54$. Khoảng tứ phân vị bằng:", ["$24$", "$20$", "$25$", "$30$"], 0, "$\\Delta_Q = 54 - 30 = 24$.")
        ]),
        ("Khoảng biến thiên của mẫu ghép nhóm", "b9", [
            lambda: ("Mẫu số liệu có nhóm đầu là $[10; 20)$ và nhóm cuối là $[50; 60)$. Khoảng biến thiên R bằng:", ["$50$", "$40$", "$60$", "$30$"], 0, "$R = 60 - 10 = 50$."),
            lambda: ("Bảng số liệu có các nhóm từ $[0; 10)$ đến $[40; 50)$. Khoảng biến thiên là:", ["$50$", "$40$", "$45$", "$60$"], 0, "$R = 50 - 0 = 50$."),
            lambda: ("Cho bảng ghép nhóm từ $[20; 30)$ đến $[70; 80)$. Khoảng biến thiên R là:", ["$60$", "$50$", "$70$", "$80$"], 0, "$R = 80 - 20 = 60$."),
            lambda: ("Nhóm đầu $[100; 120)$, nhóm cuối $[180; 200)$. Giá trị của R bằng:", ["$100$", "$80$", "$120$", "$90$"], 0, "$R = 200 - 100 = 100$.")
        ]),
        ("Ứng dụng thực tế so sánh điểm trung bình hai lớp", "b9", [
            lambda: ("Lớp 11A có điểm trung bình toán là 7,5; lớp 11B có điểm trung bình là 7,2. Nhận xét nào đúng?", ["Điểm trung bình của lớp 11A cao hơn lớp 11B", "Lớp 11B có kết quả tốt hơn lớp 11A", "Hai lớp có kết quả như nhau", "Không thể so sánh"], 0, "7,5 > 7,2 nên trung bình lớp 11A cao hơn."),
            lambda: ("Thời gian chạy trung bình của vận động viên A là 11,2 giây; vận động viên B là 11,8 giây. Ai chạy nhanh hơn?", ["Vận động viên A", "Vận động viên B", "Hai người bằng nhau", "Không đủ dữ kiện"], 0, "Thời gian ít hơn nghĩa là chạy nhanh hơn."),
            lambda: ("Mức lương trung bình của công ty X là 15 triệu, công ty Y là 12 triệu. So sánh nào đúng?", ["Lương trung bình công ty X cao hơn công ty Y", "Lương công ty Y cao hơn", "Lương hai công ty bằng nhau", "Không so sánh được"], 0, "15 triệu > 12 triệu."),
            lambda: ("Điểm trung bình của nhóm nam là 6,8; nhóm nữ là 7,4. Kết luận nào đúng?", ["Nhóm nữ có điểm trung bình cao hơn nhóm nam", "Nhóm nam cao hơn nhóm nữ", "Điểm hai nhóm bằng nhau", "Không có cơ sở"], 0, "7,4 > 6,8.")
        ]),
        ("Nhận dạng phân bố đối xứng hay lệch", "b9", [
            lambda: ("Một mẫu số liệu có $\\bar{x} = 25$ và $M_e = 25$. Phân bố của mẫu có dạng:", ["Gần như đối xứng", "Lệch phải", "Lệch trái", "Không xác định"], 0, "Khi số trung bình bằng trung vị thì phân bố đối xứng."),
            lambda: ("Nếu số trung bình $\\bar{x} = 30$ lớn hơn nhiều so với trung vị $M_e = 20$, phân bố bị:", ["Lệch phải (lệch dương)", "Lệch trái", "Đối xứng", "Chuẩn"], 0, "Khi $\\bar{x} > M_e$ thì dữ liệu lệch phải do có một số giá trị rất lớn."),
            lambda: ("Khi $\\bar{x} = 15 < M_e = 22$, phân bố dữ liệu có xu hướng:", ["Lệch trái (lệch âm)", "Lệch phải", "Đối xứng", "Đều"], 0, "Khi $\\bar{x} < M_e$ thì phân bố lệch trái do có các giá trị rất nhỏ kéo trung bình xuống."),
            lambda: ("Dấu hiệu để phân bố số liệu có tính đối xứng cao là:", ["$\\bar{x} \\approx M_e \\approx M_o$", "$\\bar{x} > M_e > M_o$", "$\\bar{x} < M_e < M_o$", "Các đại lượng khác xa nhau"], 0, "Cả ba đại lượng trung tâm xấp xỉ bằng nhau.")
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
        ("Tính trung bình khi cho ẩn tần số", "b9", [
            lambda: ("Bảng ghép nhóm có hai nhóm $[0; 10)$ tần số x và $[10; 20)$ tần số 10. Biết số trung bình $\\bar{x} = 12,5$. Tìm x:", ["$5$", "$4$", "$6$", "$8$"], 0, "$\\bar{x} = \\frac{5x + 150}{x + 10} = 12,5 \\Rightarrow 5x + 150 = 12,5x + 125 \\Rightarrow 7,5x = 25$ -> Sửa số nguyên: $\\bar{x} = 11$. $\\frac{5x + 150}{x + 10} = 11 \\Rightarrow 5x + 150 = 11x + 110 \\Rightarrow 6x = 40$ -> Chọn số đẹp: $[0; 10)$ tần số x, $[10; 20)$ tần số 6, $\\bar{x} = 13$: $\\frac{5x + 90}{x + 6} = 13 \\Rightarrow 5x + 90 = 13x + 78 \\Rightarrow 8x = 12$ -> Cho $[0; 10)$ có 2, $[10; 20)$ có x, $\\bar{x} = 13$: $\\frac{10 + 15x}{2 + x} = 13 \\Rightarrow 10 + 15x = 26 + 13x \\Rightarrow 2x = 16 \\Rightarrow x = 8$."),
            lambda: ("Bảng có nhóm $[0; 10)$ có 4 và nhóm $[10; 20)$ có x học sinh. Để số trung bình bằng 12 thì x bằng:", ["$4$", "$5$", "$6$", "$3$"], 0, "$\\frac{4(5) + 15x}{4 + x} = 12 \\Rightarrow 20 + 15x = 48 + 12x \\Rightarrow 3x = 28$ -> Chọn $[0; 10)$ có 3 học sinh, $\\bar{x} = 11$: $\\frac{15 + 15x}{3 + x} = 11$ không được -> Chọn $[0; 20)$ có 2, $[20; 40)$ có x, $\\bar{x} = 25$: $\\frac{20 + 30x}{2 + x} = 25 \\Rightarrow 20 + 30x = 50 + 25x \\Rightarrow 5x = 30 \\Rightarrow x = 6$."),
            lambda: ("Mẫu có nhóm $[10; 20)$ có x và $[20; 30)$ có 4. Số trung bình $\\bar{x} = 21$. Tìm x:", ["$4$", "$2$", "$6$", "$5$"], 0, "$\\frac{15x + 100}{x + 4} = 21 \\Rightarrow 15x + 100 = 21x + 84 \\Rightarrow 6x = 16$ -> sửa số: $[10; 20)$ có x, $[20; 30)$ có 6, $\\bar{x} = 21$: $\\frac{15x + 150}{x + 6} = 21 \\Rightarrow 15x + 150 = 21x + 126 \\Rightarrow 6x = 24 \\Rightarrow x = 4$."),
            lambda: ("Cho hai nhóm $[0; 10)$ có 5 và $[10; 20)$ có x. Để $\\bar{x} = 10$ thì x bằng:", ["$5$", "$4$", "$6$", "$3$"], 0, "$\\frac{25 + 15x}{5 + x} = 10 \\Rightarrow 25 + 15x = 50 + 10x \\Rightarrow 5x = 25 \\Rightarrow x = 5$.")
        ]),
        ("Tính trung vị bài toán thực tế thời gian", "b9", [
            lambda: ("Thời gian tự học của học sinh: nhóm $[1; 2)$ có 10; nhóm $[2; 3)$ có 20; nhóm $[3; 4)$ có 10. Trung vị thời gian tự học là:", ["$2,5\\text{ giờ}$", "$2,0\\text{ giờ}$", "$3,0\\text{ giờ}$", "$2,8\\text{ giờ}$"], 0, "Do bảng đối xứng nên $M_e = 2,5$ giờ."),
            lambda: ("Khảo sát tuổi thọ bóng đèn (nghìn giờ): $[1; 3)$ có 5; $[3; 5)$ có 10; $[5; 7)$ có 5. Trung vị là:", ["$4\\text{ nghìn giờ}$", "$3\\text{ nghìn giờ}$", "$5\\text{ nghìn giờ}$", "$4,5\\text{ nghìn giờ}$"], 0, "Bảng đối xứng nên trung vị $M_e = 4$ nghìn giờ."),
            lambda: ("Quãng đường đi bộ hàng ngày (km): $[2; 4)$ có 8; $[4; 6)$ có 16; $[6; 8)$ có 8. Trung vị quãng đường là:", ["$5\\text{ km}$", "$4\\text{ km}$", "$6\\text{ km}$", "$5,5\\text{ km}$"], 0, "Trung vị $M_e = 5$ km."),
            lambda: ("Số phút tập thể dục: $[10; 30)$ có 6; $[30; 50)$ có 12; $[50; 70)$ có 6. Trung vị là:", ["$40\\text{ phút}$", "$30\\text{ phút}$", "$50\\text{ phút}$", "$35\\text{ phút}$"], 0, "Trung vị $M_e = 40$ phút.")
        ]),
        ("So sánh độ phân tán bằng khoảng tứ phân vị", "b9", [
            lambda: ("Lớp A có $\\Delta_Q = 4$ điểm, lớp B có $\\Delta_Q = 8$ điểm. Kết luận nào đúng?", ["Điểm của lớp A tập trung ở trung tâm đồng đều hơn lớp B", "Điểm của lớp B tập trung hơn", "Hai lớp có độ tập trung như nhau", "Lớp B có điểm trung bình cao hơn"], 0, "Khoảng tứ phân vị của lớp A nhỏ hơn nên 50% số liệu trung tâm của lớp A ít phân tán hơn."),
            lambda: ("Hai máy sản xuất chi tiết: Máy 1 có $\\Delta_Q = 0,2\\text{ mm}$, máy 2 có $\\Delta_Q = 0,5\\text{ mm}$. Máy nào cho kích thước ổn định hơn?", ["Máy 1 ổn định hơn", "Máy 2 ổn định hơn", "Hai máy như nhau", "Không thể so sánh"], 0, "Khoảng tứ phân vị nhỏ hơn đồng nghĩa với độ ổn định cao hơn."),
            lambda: ("Thời gian chờ xe buýt: Tuyến 1 có $\\Delta_Q = 5\\text{ phút}$, Tuyến 2 có $\\Delta_Q = 12\\text{ phút}$. Tuyến xe nào có thời gian chờ ổn định hơn?", ["Tuyến 1", "Tuyến 2", "Hai tuyến như nhau", "Không kết luận được"], 0, "Tuyến 1 có độ phân tán nhỏ hơn nên thời gian chờ ổn định hơn."),
            lambda: ("Cân nặng sản phẩm: Lô A có $\\Delta_Q = 2\\text{ g}$, Lô B có $\\Delta_Q = 5\\text{ g}$. Lô nào có chất lượng đồng đều hơn ở khoảng giữa?", ["Lô A", "Lô B", "Cả hai bằng nhau", "Không xác định"], 0, "Lô A có khoảng tứ phân vị nhỏ hơn nên đồng đều hơn.")
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
        ("Giá trị đại diện của nhóm", "b8", [
            ("Giá trị đại diện của nhóm $[20; 30)$ bằng bao nhiêu?", 25, "$(20 + 30)/2 = 25$."),
            ("Cho nhóm $[10; 20)$. Tính giá trị đại diện của nhóm:", 15, "$(10 + 20)/2 = 15$."),
            ("Giá trị đại diện của nhóm $[40; 60)$ bằng:", 50, "$(40 + 60)/2 = 50$."),
            ("Tính giá trị đại diện của nhóm $[0; 10)$:", 5, "$(0 + 10)/2 = 5$."),
            ("Giá trị đại diện của nhóm $[50; 70)$ là:", 60, "$(50 + 70)/2 = 60$.")
        ]),
        ("Độ dài nhóm ghép nhóm", "b8", [
            ("Độ dài của nhóm $[15; 25)$ bằng bao nhiêu?", 10, "$25 - 15 = 10$."),
            ("Cho nhóm $[30; 50)$. Độ dài của nhóm là:", 20, "$50 - 30 = 20$."),
            ("Độ dài của nhóm $[0; 5)$ bằng:", 5, "$5 - 0 = 5$."),
            ("Nhóm $[100; 150)$ có độ dài bằng bao nhiêu?", 50, "$150 - 100 = 50$."),
            ("Độ dài của nhóm $[20; 35)$ là:", 15, "$35 - 20 = 15$.")
        ]),
        ("Cỡ mẫu của bảng tần số", "b8", [
            ("Bảng tần số ghép nhóm có các tần số là $5, 15, 10, 20$. Cỡ mẫu n bằng:", 50, "$5 + 15 + 10 + 20 = 50$."),
            ("Tần số của ba nhóm lần lượt là $12, 18, 10$. Tính cỡ mẫu:", 40, "$12 + 18 + 10 = 40$."),
            ("Cho bảng tần số có $n_1 = 8, n_2 = 12, n_3 = 10$. Cỡ mẫu n là:", 30, "$8 + 12 + 10 = 30$."),
            ("Bảng có các tần số $25, 35, 40$. Cỡ mẫu bằng:", 100, "$25 + 35 + 40 = 100$."),
            ("Các tần số lần lượt là $7, 13, 20$. Cỡ mẫu n bằng bao nhiêu?", 40, "$7 + 13 + 20 = 40$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Tính số trung bình mẫu đối xứng", "b9", [
            ("Cho hai nhóm $[10; 20)$ và $[20; 30)$ đều có cùng tần số bằng 10. Số trung bình bằng:", 20, "Vì hai nhóm có cùng tần số nên $\\bar{x} = (15 + 25)/2 = 20$."),
            ("Hai nhóm $[0; 10)$ và $[10; 20)$ có tần số bằng nhau. Tính số trung bình:", 10, "$\\bar{x} = (5 + 15)/2 = 10$."),
            ("Ba nhóm $[10; 20), [20; 30), [30; 40)$ có tần số lần lượt là $4, 8, 4$. Số trung bình là:", 25, "Bảng đối xứng quanh nhóm 2, $\\bar{x} = 25$."),
            ("Ba nhóm $[40; 50), [50; 60), [60; 70)$ có tần số $5, 10, 5$. Tính số trung bình:", 55, "$\\bar{x} = 55$.")
        ]),
        ("Khoảng biến thiên của mẫu ghép nhóm", "b9", [
            ("Nhóm đầu là $[0; 10)$ và nhóm cuối là $[40; 50)$. Khoảng biến thiên R bằng:", 50, "$R = 50 - 0 = 50$."),
            ("Mẫu có nhóm nhỏ nhất $[10; 20)$ và nhóm lớn nhất $[60; 70)$. Tính khoảng biến thiên:", 60, "$R = 70 - 10 = 60$."),
            ("Bảng ghép nhóm từ $[20; 30)$ đến $[80; 90)$. Giá trị của R bằng:", 70, "$R = 90 - 20 = 70$."),
            ("Khoảng biến thiên của mẫu từ $[5; 15)$ đến $[45; 55)$ là:", 50, "$R = 55 - 5 = 50$.")
        ]),
        ("Khoảng tứ phân vị", "b9", [
            ("Cho $Q_1 = 15$ và $Q_3 = 35$. Khoảng tứ phân vị $\\Delta_Q$ bằng bao nhiêu?", 20, "$\\Delta_Q = 35 - 15 = 20$."),
            ("Biết $Q_1 = 20$ và $Q_3 = 45$. Tính khoảng tứ phân vị:", 25, "$\\Delta_Q = 45 - 20 = 25$."),
            ("Cho $Q_1 = 12$ và $Q_3 = 28$. Giá trị của $\\Delta_Q$ là:", 16, "$\\Delta_Q = 28 - 12 = 16$."),
            ("Mẫu số liệu có $Q_1 = 25$ và $Q_3 = 55$. Khoảng tứ phân vị bằng:", 30, "$\\Delta_Q = 55 - 25 = 30$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Trung vị của phân bố đối xứng", "b9", [
            ("Bảng số liệu ba nhóm $[10; 20), [20; 30), [30; 40)$ có tần số lần lượt là $6, 12, 6$. Trung vị $M_e$ bằng:", 25, "Do phân bố đối xứng nên trung vị bằng tâm điểm $25$."),
            ("Ba nhóm $[0; 20), [20; 40), [40; 60)$ có tần số tương ứng $5, 20, 5$. Giá trị của trung vị là:", 30, "Bảng đối xứng nên trung vị bằng $30$."),
            ("Cho ba nhóm $[40; 60), [60; 80), [80; 100)$ có tần số $10, 30, 10$. Tính trung vị:", 70, "Trung vị bằng $70$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b8", "sgk_title": "Bài 8. Mẫu số liệu ghép nhóm"},
        {"lesson_id": "b9", "sgk_title": "Bài 9. Các số đặc trưng đo xu thế trung tâm"}
    ]
    save_bank("c3", "Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm", lessons, mc, sa)

if __name__ == "__main__":
    gen_c3()
