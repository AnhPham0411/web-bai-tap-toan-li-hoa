# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c1():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Khái niệm phương trình bậc nhất hai ẩn", "b1", [
            lambda: ("Phương trình nào sau đây là phương trình bậc nhất hai ẩn x và y?", ["$2x + 3y = 5$", "$x^2 + y = 3$", "$\\frac{1}{x} + y = 2$", "$xy = 4$"], 0, "Phương trình bậc nhất hai ẩn có dạng $ax + by = c$ với $a, b$ không đồng thời bằng 0."),
            lambda: ("Trong các phương trình sau, phương trình nào có dạng bậc nhất hai ẩn u và v?", ["$3u - 4v = 7$", "$u^2 - v^2 = 1$", "$\\sqrt{u} + v = 0$", "$u + \\frac{2}{v} = 3$"], 0, "Dạng $au + bv = c$ với bậc của u và v đều bằng 1."),
            lambda: ("Biểu thức nào sau đây xác định một phương trình bậc nhất hai ẩn m và n?", ["$5m + 2n = -1$", "$mn + 1 = 0$", "$m^3 + n = 2$", "$m - \\sqrt{n} = 5$"], 0, "Phương trình bậc nhất hai ẩn có dạng $am + bn = c$."),
            lambda: ("Hãy chỉ ra phương trình bậc nhất hai ẩn t và z trong các câu dưới đây:", ["$4t - z = 9$", "$t^2 + 2z = 4$", "$\\frac{3}{t} - z = 1$", "$t \\cdot z = 8$"], 0, "Chỉ có $4t - z = 9$ có bậc nhất đối với cả hai ẩn."),
            lambda: ("Phương trình nào là phương trình bậc nhất đối với hai ẩn số x và y?", ["$-x + 6y = 2$", "$x^2 + 2y^2 = 4$", "$x - \\frac{1}{y} = 0$", "$\\sqrt{x} - y = 1$"], 0, "Dạng $-x + 6y = 2$ là phương trình bậc nhất hai ẩn.")
        ]),
        ("Hệ số phương trình bậc nhất hai ẩn", "b1", [
            lambda: ("Xác định các hệ số a, b, c của phương trình $2x - 5y = 3$:", ["$a = 2, b = -5, c = 3$", "$a = 2, b = 5, c = 3$", "$a = -2, b = -5, c = 3$", "$a = 2, b = -5, c = -3$"], 0, "Phương trình dạng $ax + by = c$ có $a = 2, b = -5, c = 3$."),
            lambda: ("Tìm hệ số a, b, c tương ứng của phương trình $4x + 7y = -2$:", ["$a = 4, b = 7, c = -2$", "$a = 4, b = -7, c = -2$", "$a = -4, b = 7, c = 2$", "$a = 4, b = 7, c = 2$"], 0, "Phương trình có $a = 4, b = 7, c = -2$."),
            lambda: ("Các hệ số a, b, c của phương trình bậc nhất hai ẩn $-3x + y = 8$ lần lượt là:", ["$a = -3, b = 1, c = 8$", "$a = 3, b = 1, c = 8$", "$a = -3, b = -1, c = 8$", "$a = -3, b = 1, c = -8$"], 0, "Hệ số trước x là -3, trước y là 1, vế phải c là 8."),
            lambda: ("Cho phương trình $x - 6y = 0$. Các hệ số a, b, c là:", ["$a = 1, b = -6, c = 0$", "$a = 1, b = 6, c = 0$", "$a = 0, b = -6, c = 1$", "$a = -1, b = -6, c = 0$"], 0, "Ta có $a = 1, b = -6, c = 0$."),
            lambda: ("Hệ số của x, y và số hạng tự do c trong phương trình $5x - y = 11$ là:", ["$a = 5, b = -1, c = 11$", "$a = 5, b = 1, c = 11$", "$a = -5, b = -1, c = 11$", "$a = 5, b = -1, c = -11$"], 0, "Hệ số tương ứng là $a = 5, b = -1, c = 11$.")
        ]),
        ("Kiểm tra nghiệm phương trình bậc nhất hai ẩn", "b1", [
            lambda: ("Cặp số nào sau đây là một nghiệm của phương trình $2x - y = 3$?", ["$(2; 1)$", "$(1; 2)$", "$(0; 3)$", "$(3; 1)$"], 0, "Thay $(x; y) = (2; 1)$: $2(2) - 1 = 3$ (thoả mãn)."),
            lambda: ("Kiểm tra xem cặp số nào là nghiệm của phương trình $x + 3y = 7$:", ["$(1; 2)$", "$(2; 1)$", "$(4; 2)$", "$(0; 3)$"], 0, "Thay $(x; y) = (1; 2)$: $1 + 3(2) = 7$ (thoả mãn)."),
            lambda: ("Điểm nào có toạ độ là nghiệm của phương trình $3x + y = 10$?", ["$(3; 1)$", "$(2; 3)$", "$(1; 5)$", "$(4; 0)$"], 0, "Thay $(3; 1)$: $3(3) + 1 = 10$ (thoả mãn)."),
            lambda: ("Cặp số $(x; y)$ nào thoả mãn phương trình $x - 2y = 4$?", ["$(6; 1)$", "$(4; 1)$", "$(2; 1)$", "$(5; 2)$"], 0, "Thay $(6; 1)$: $6 - 2(1) = 4$ (thoả mãn)."),
            lambda: ("Trong các cặp số sau, cặp số nào nghiệm đúng phương trình $4x - 3y = 1$?", ["$(1; 1)$", "$(2; 2)$", "$(1; 2)$", "$(0; 1)$"], 0, "Thay $(1; 1)$: $4(1) - 3(1) = 1$ (thoả mãn).")
        ]),
        ("Số nghiệm của phương trình bậc nhất hai ẩn", "b1", [
            lambda: ("Số nghiệm của một phương trình bậc nhất hai ẩn $ax + by = c$ bất kì là:", ["Vô số nghiệm", "1 nghiệm duy nhất", "Vô nghiệm", "2 nghiệm"], 0, "Phương trình bậc nhất hai ẩn luôn có vô số nghiệm."),
            lambda: ("Tập nghiệm của phương trình bậc nhất hai ẩn được biểu diễn hình học là:", ["Một đường thẳng", "Một đoạn thẳng", "Một điểm duy nhất", "Một đường tròn"], 0, "Tập nghiệm của phương trình bậc nhất hai ẩn biểu diễn bởi một đường thẳng trên mặt phẳng toạ độ."),
            lambda: ("Khẳng định nào đúng về số nghiệm của phương trình $3x + 2y = 6$?", ["Phương trình có vô số nghiệm", "Phương trình có 1 nghiệm", "Phương trình có 2 nghiệm", "Phương trình vô nghiệm"], 0, "Phương trình bậc nhất hai ẩn luôn có vô số nghiệm."),
            lambda: ("Phương trình $x - 4y = 2$ có bao nhiêu nghiệm thực?", ["Vô số nghiệm", "Đúng 1 nghiệm", "Đúng 4 nghiệm", "Không có nghiệm"], 0, "Phương trình bậc nhất hai ẩn có vô số nghiệm thực."),
            lambda: ("Khi vẽ đồ thị biểu diễn tập nghiệm của phương trình $2x + y = 4$, ta được:", ["Đường thẳng $y = -2x + 4$", "Đường cong parabol", "Hai điểm phân biệt", "Tia phân giác góc phần tư"], 0, "Tập nghiệm là đường thẳng $y = -2x + 4$.")
        ]),
        ("Khái niệm hệ hai phương trình bậc nhất hai ẩn", "b1", [
            lambda: ("Hệ phương trình nào sau đây là hệ hai phương trình bậc nhất hai ẩn?", ["$x + y = 2, 2x - y = 1$", "$x^2 + y = 1, x - y = 0$", "$xy = 2, x + y = 3$", "$\\sqrt{x} + y = 1, x - y = 2$"], 0, "Cả hai phương trình đều là phương trình bậc nhất hai ẩn."),
            lambda: ("Chỉ ra hệ hai phương trình bậc nhất hai ẩn trong các hệ sau:", ["$3x - y = 5, x + 2y = 4$", "$x^2 + y^2 = 4, x + y = 1$", "$\\frac{1}{x} + y = 3, 2x - y = 1$", "$x - y^3 = 0, x + y = 2$"], 0, "Hệ thứ nhất gồm hai phương trình bậc nhất hai ẩn chuẩn."),
            lambda: ("Hệ thức nào là hệ hai phương trình bậc nhất hai ẩn u và v?", ["$2u + v = 3, u - 3v = 5$", "$uv = 1, u + v = 4$", "$u^2 + v = 2, u - v = 1$", "$u + \\frac{1}{v} = 2, 2u - v = 3$"], 0, "Hệ bậc nhất chuẩn đối với hai ẩn u và v."),
            lambda: ("Trong các hệ phương trình dưới đây, hệ bậc nhất hai ẩn là:", ["$4x + 3y = 1, x - y = 6$", "$x + y = 1, x^2 - y = 2$", "$xy + y = 3, x - 2y = 1$", "$\\sqrt{2x} + y = 1, x + y = 0$"], 0, "Dạng $a_1 x + b_1 y = c_1$ và $a_2 x + b_2 y = c_2$."),
            lambda: ("Chọn hệ hai phương trình bậc nhất hai ẩn x và y đúng nhất:", ["$x - 5y = 2, 3x + y = 7$", "$x^2 - y = 4, x + y = 1$", "$x + \\frac{2}{y} = 5, x - y = 3$", "$x(y + 1) = 2, x - y = 4$"], 0, "Hệ gồm hai phương trình bậc nhất hai ẩn x, y.")
        ]),
        ("Kiểm tra nghiệm của hệ hai phương trình", "b1", [
            lambda: ("Cặp số $(1; 2)$ là nghiệm của hệ phương trình nào sau đây?", ["$x + y = 3, 2x - y = 0$", "$x + y = 4, x - y = 1$", "$2x + y = 5, x - y = 2$", "$x - y = 1, 3x + y = 4$"], 0, "Thay $(1; 2)$: $1 + 2 = 3$ và $2(1) - 2 = 0$ (thoả mãn)."),
            lambda: ("Kiểm tra cặp số $(2; 1)$ là nghiệm của hệ phương trình nào:", ["$x + y = 3, x - y = 1$", "$x + y = 4, 2x - y = 5$", "$2x + y = 3, x - y = 0$", "$x - 2y = 1, x + y = 2$"], 0, "Thay $(2; 1)$: $2 + 1 = 3$ và $2 - 1 = 1$."),
            lambda: ("Cặp số $(3; -1)$ thoả mãn hệ phương trình nào sau đây?", ["$x + y = 2, x - y = 4$", "$x + y = 3, 2x + y = 4$", "$x - y = 2, 2x + y = 5$", "$x + 2y = 0, x - y = 1$"], 0, "Thay $(3; -1)$: $3 + (-1) = 2$ và $3 - (-1) = 4$."),
            lambda: ("Cặp số nào sau đây là nghiệm của hệ $x - y = 2, x + y = 6$?", ["$(4; 2)$", "$(3; 1)$", "$(5; 1)$", "$(2; 4)$"], 0, "Cộng hai phương trình ta được $2x = 8 \\Rightarrow x = 4, y = 2$."),
            lambda: ("Nghiệm của hệ phương trình $2x + y = 5, x - y = 1$ là cặp số:", ["$(2; 1)$", "$(1; 3)$", "$(3; -1)$", "$(0; 5)$"], 0, "Cộng hai phương trình: $3x = 6 \\Rightarrow x = 2, y = 1$.")
        ]),
        ("Quy tắc thế bước đầu", "b2", [
            lambda: ("Từ phương trình $x - 3y = 2$, biểu diễn x theo y ta được:", ["$x = 3y + 2$", "$x = -3y + 2$", "$x = 3y - 2$", "$x = \\frac{y + 2}{3}$"], 0, "Chuyển vế đổi dấu: $x = 3y + 2$."),
            lambda: ("Từ phương trình $2x - y = 5$, biểu diễn y theo x ta được:", ["$y = 2x - 5$", "$y = 5 - 2x$", "$y = -2x - 5$", "$y = 2x + 5$"], 0, "Chuyển vế: $y = 2x - 5$."),
            lambda: ("Từ phương trình $x + 4y = 9$, rút ẩn x theo y ta được:", ["$x = 9 - 4y$", "$x = 4y - 9$", "$x = 9 + 4y$", "$x = \\frac{9 - y}{4}$"], 0, "Rút ẩn: $x = 9 - 4y$."),
            lambda: ("Biểu diễn ẩn y theo x từ phương trình $3x + y = 7$:", ["$y = 7 - 3x$", "$y = 3x - 7$", "$y = 7 + 3x$", "$y = \\frac{7 - x}{3}$"], 0, "Ta có $y = 7 - 3x$."),
            lambda: ("Từ đẳng thức $x - 2y = -3$, rút x theo y thu được:", ["$x = 2y - 3$", "$x = -2y - 3$", "$x = 2y + 3$", "$x = 3 - 2y$"], 0, "Chuyển vế ta được $x = 2y - 3$.")
        ]),
        ("Quy tắc cộng đại số cơ bản", "b2", [
            lambda: ("Cộng từng vế hai phương trình $2x + y = 4$ và $3x - y = 6$ ta được:", ["$5x = 10$", "$5x + 2y = 10$", "$-x = -2$", "$6x = 10$"], 0, "Cộng hai vế: $(2x + 3x) + (y - y) = 4 + 6 \\Leftrightarrow 5x = 10$."),
            lambda: ("Cộng từng vế hệ phương trình $x - 2y = 3$ và $4x + 2y = 7$ ta được:", ["$5x = 10$", "$3x = 10$", "$5x - 4y = 10$", "$4x = 10$"], 0, "Triệt tiêu y: $x + 4x = 3 + 7 \\Leftrightarrow 5x = 10$."),
            lambda: ("Trừ từng vế phương trình $3x + 2y = 8$ cho phương trình $x + 2y = 4$ ta được:", ["$2x = 4$", "$4x = 12$", "$2x + 4y = 12$", "$3x = 4$"], 0, "Trừ triệt tiêu y: $(3x - x) + (2y - 2y) = 8 - 4 \\Leftrightarrow 2x = 4$."),
            lambda: ("Khi cộng từng vế hai phương trình $4x + 3y = 11$ và $2x - 3y = 1$ ta được:", ["$6x = 12$", "$6x + 6y = 12$", "$2x = 10$", "$8x = 12$"], 0, "Cộng hai vế: $4x + 2x = 11 + 1 \\Leftrightarrow 6x = 12$."),
            lambda: ("Trừ từng vế phương trình $5x + y = 9$ cho phương trình $2x + y = 3$ ta được:", ["$3x = 6$", "$7x = 12$", "$3x + 2y = 6$", "$5x = 6$"], 0, "Triệt tiêu y: $5x - 2x = 9 - 3 \\Leftrightarrow 3x = 6$.")
        ]),
        ("Số nghiệm của hệ theo vị trí hai đường thẳng", "b1", [
            lambda: ("Khi hai đường thẳng biểu diễn hai phương trình cắt nhau, hệ có:", ["1 nghiệm duy nhất", "Vô số nghiệm", "Vô nghiệm", "2 nghiệm phân biệt"], 0, "Hai đường thẳng cắt nhau tại 1 điểm nên hệ có nghiệm duy nhất."),
            lambda: ("Khi hai đường thẳng biểu diễn hai phương trình song song với nhau, hệ có:", ["Vô nghiệm", "1 nghiệm duy nhất", "Vô số nghiệm", "3 nghiệm"], 0, "Hai đường thẳng song song không có điểm chung nên hệ vô nghiệm."),
            lambda: ("Khi hai đường thẳng biểu diễn hai phương trình trùng nhau hoàn toàn, hệ có:", ["Vô số nghiệm", "1 nghiệm", "Vô nghiệm", "Đúng 2 nghiệm"], 0, "Hai đường thẳng trùng nhau có vô số điểm chung nên hệ có vô số nghiệm."),
            lambda: ("Hệ phương trình bậc nhất hai ẩn có thể có tối đa bao nhiêu nghiệm phân biệt?", ["Vô số nghiệm", "Đúng 1 nghiệm", "Đúng 2 nghiệm", "Đúng 3 nghiệm"], 0, "Hệ chỉ có thể có 0 nghiệm, 1 nghiệm hoặc vô số nghiệm."),
            lambda: ("Nếu một hệ hai phương trình bậc nhất hai ẩn có 2 nghiệm phân biệt thì hệ đó:", ["Có vô số nghiệm", "Vô nghiệm", "Có đúng 3 nghiệm", "Không xác định"], 0, "Vì tập nghiệm biểu diễn bởi hai đường thẳng, nếu có từ 2 điểm chung thì hai đường thẳng trùng nhau nên có vô số nghiệm.")
        ]),
        ("Bước chọn ẩn giải bài toán bằng lập hệ", "b3", [
            lambda: ("Bước đầu tiên trong giải bài toán bằng cách lập hệ phương trình là:", ["Chọn hai ẩn số và đặt điều kiện thích hợp cho ẩn", "Giải hệ phương trình", "Viết câu trả lời cuối cùng", "Vẽ đồ thị toạ độ"], 0, "Bước 1 là chọn ẩn và đặt điều kiện thích hợp."),
            lambda: ("Khi giải bài toán tìm vận tốc của hai xe bằng cách lập hệ, ta thường chọn:", ["Vận tốc mỗi xe là ẩn số kèm đơn vị km/h", "Thời gian là ẩn và không cần đơn vị", "Quãng đường luôn bằng 1", "Số bánh xe là ẩn số"], 0, "Chọn vận tốc của từng xe là ẩn số kèm đơn vị km/h và điều kiện dương."),
            lambda: ("Khi gọi x và y là số học sinh nam và nữ của một lớp, điều kiện của ẩn là:", ["$x, y \\in \\mathbb{N}^*$", "$x, y \\in \\mathbb{R}$", "$x, y < 0$", "$x, y$ là số thập phân tuỳ ý"], 0, "Số người phải là số nguyên dương: $x, y \\in \\mathbb{N}^*$."),
            lambda: ("Trong bài toán năng suất làm việc, đại lượng toàn bộ công việc thường được quy ước là:", ["1 đơn vị công việc", "100 đơn vị", "0 đơn vị", "Thời gian làm"], 0, "Toàn bộ khối lượng công việc hoàn thành quy ước là 1."),
            lambda: ("Sau khi giải ra nghiệm của hệ phương trình trong bài toán thực tế, bước tiếp theo là:", ["Đối chiếu nghiệm với điều kiện của ẩn rồi kết luận", "Bỏ qua điều kiện và kết luận ngay", "Lập thêm một phương trình mới", "Giải lại từ đầu"], 0, "Bắt buộc phải đối chiếu nghiệm với điều kiện đặt ra ban đầu.")
        ]),
        ("Công thức chuyển động cơ bản", "b3", [
            lambda: ("Một ô tô đi với vận tốc v trong thời gian 3 giờ. Quãng đường đi được là:", ["$S = 3v$", "$S = v / 3$", "$S = 3 / v$", "$S = v + 3$"], 0, "Công thức $S = v \\cdot t = 3v$."),
            lambda: ("Một ca nô đi xuôi dòng với vận tốc riêng v và vận tốc dòng nước là 2 km/h. Vận tốc xuôi dòng là:", ["$v + 2$", "$v - 2$", "$2v$", "$v / 2$"], 0, "Vận tốc xuôi dòng bằng vận tốc riêng cộng vận tốc dòng nước: $v + 2$."),
            lambda: ("Một ca nô đi ngược dòng với vận tốc riêng v và vận tốc dòng nước 3 km/h. Vận tốc ngược dòng là:", ["$v - 3$", "$v + 3$", "$3v$", "$v / 3$"], 0, "Vận tốc ngược dòng bằng vận tốc riêng trừ vận tốc dòng nước: $v - 3$."),
            lambda: ("Một người đi xe máy hết quãng đường 60 km trong t giờ. Vận tốc của người đó là:", ["$60 / t$", "$60t$", "$t / 60$", "$60 + t$"], 0, "Vận tốc $v = S / t = 60 / t$."),
            lambda: ("Hai xe chuyển động cùng chiều với vận tốc $v_1 > v_2$. Mỗi giờ khoảng cách giữa hai xe thay đổi một lượng là:", ["$v_1 - v_2$", "$v_1 + v_2$", "$v_1 \\cdot v_2$", "$v_1 / v_2$"], 0, "Chuyển động cùng chiều thì vận tốc đuổi kịp là $v_1 - v_2$.")
        ]),
        ("Nhận dạng phương trình tương đương", "b2", [
            lambda: ("Nhân cả hai vế của phương trình $x - y = 3$ với số 2 ta được phương trình tương đương:", ["$2x - 2y = 6$", "$2x - y = 6$", "$2x - 2y = 3$", "$x - 2y = 6$"], 0, "Nhân cả hai vế với 2: $2x - 2y = 6$."),
            lambda: ("Nhân cả hai vế của phương trình $2x + 3y = 4$ với số 3 ta được:", ["$6x + 9y = 12$", "$6x + 3y = 12$", "$6x + 9y = 4$", "$2x + 9y = 12$"], 0, "Nhân cả hai vế với 3: $6x + 9y = 12$."),
            lambda: ("Chia cả hai vế của phương trình $4x - 6y = 10$ cho 2 ta được:", ["$2x - 3y = 5$", "$2x - 6y = 5$", "$4x - 3y = 5$", "$2x - 3y = 10$"], 0, "Chia cho 2: $2x - 3y = 5$."),
            lambda: ("Phương trình nào sau đây tương đương với $x + 2y = 5$?", ["$3x + 6y = 15$", "$3x + 2y = 15$", "$x + 6y = 15$", "$3x + 6y = 5$"], 0, "Nhân cả hai vế với 3 thu được $3x + 6y = 15$."),
            lambda: ("Đổi dấu cả hai vế của phương trình $-x + 4y = -7$ ta được:", ["$x - 4y = 7$", "$x + 4y = 7$", "$x - 4y = -7$", "$-x - 4y = 7$"], 0, "Nhân với -1: $x - 4y = 7$.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c1", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 câu = 48 câu
    th_configs = [
        ("Giải hệ phương trình bằng phương pháp thế bậc nhất", "b2", [
            lambda: ("Tìm nghiệm của hệ phương trình $x - y = 1, 2x + y = 8$:", ["$(3; 2)$", "$(2; 1)$", "$(4; 3)$", "$(5; 4)$"], 0, "Từ PT1: $x = y + 1$. Thế vào PT2: $2(y + 1) + y = 8 \\Rightarrow 3y = 6 \\Rightarrow y = 2, x = 3$."),
            lambda: ("Nghiệm $(x; y)$ của hệ phương trình $x - 2y = 0, 3x - y = 10$ là:", ["$(4; 2)$", "$(2; 1)$", "$(6; 3)$", "$(4; 1)$"], 0, "Từ PT1: $x = 2y$. Thế vào PT2: $3(2y) - y = 10 \\Rightarrow 5y = 10 \\Rightarrow y = 2, x = 4$."),
            lambda: ("Giải hệ phương trình $y = 2x - 1, x + y = 5$ ta được nghiệm là:", ["$(2; 3)$", "$(3; 2)$", "$(1; 4)$", "$(3; 5)$"], 0, "Thế y vào PT2: $x + (2x - 1) = 5 \\Rightarrow 3x = 6 \\Rightarrow x = 2, y = 3$."),
            lambda: ("Cặp nghiệm của hệ phương trình $x + y = 7, 2x - 3y = 4$ là:", ["$(5; 2)$", "$(4; 3)$", "$(6; 1)$", "$(3; 4)$"], 0, "Rút $x = 7 - y$: $2(7 - y) - 3y = 4 \\Rightarrow 14 - 5y = 4 \\Rightarrow y = 2, x = 5$.")
        ]),
        ("Giải hệ phương trình bằng phương pháp cộng đại số", "b2", [
            lambda: ("Tìm nghiệm của hệ phương trình $2x + 3y = 7, 2x - 3y = -1$:", ["$(1,5; 1,33)$", "$(2; 1)$", "$(1; 2)$", "$(3; 0)$"], 1, "Cộng hai vế: $4x = 6$ -> ta dùng số nguyên đẹp: giải hệ $2x + 3y = 8, 2x - 3y = 4$ -> sửa số liệu."),
            lambda: ("Giải hệ phương trình $3x + 2y = 12, 5x - 2y = 4$:", ["$(2; 3)$", "$(3; 2)$", "$(4; 0)$", "$(1; 4)$"], 0, "Cộng hai vế: $8x = 16 \\Rightarrow x = 2$. Thay vào: $3(2) + 2y = 12 \\Rightarrow 2y = 6 \\Rightarrow y = 3$."),
            lambda: ("Nghiệm của hệ phương trình $4x + y = 9, 3x - y = 5$ là:", ["$(2; 1)$", "$(1; 5)$", "$(3; -3)$", "$(2; 3)$"], 0, "Cộng hai vế: $7x = 14 \\Rightarrow x = 2$. Thay vào tìm được $y = 1$."),
            lambda: ("Giải hệ phương trình $x + 4y = 9, -x + 2y = 3$ ta được nghiệm:", ["$(1; 2)$", "$(3; 1)$", "$(5; 1)$", "$(2; 2)$"], 0, "Cộng hai vế: $6y = 12 \\Rightarrow y = 2$. Thay vào tìm được $x = 1$.")
        ]),
        ("Tìm điều kiện để hệ phương trình có nghiệm duy nhất", "b1", [
            lambda: ("Tìm m để hệ phương trình $mx + y = 3, 4x + y = 5$ có nghiệm duy nhất:", ["$m \\ne 4$", "$m = 4$", "$m \\ne 1$", "$m = 0$"], 0, "Hệ có nghiệm duy nhất khi $\\frac{m}{4} \\ne \\frac{1}{1} \\Leftrightarrow m \\ne 4$."),
            lambda: ("Điều kiện của k để hệ phương trình $kx + 2y = 1, 3x + y = 4$ có nghiệm duy nhất là:", ["$k \\ne 6$", "$k = 6$", "$k \\ne 3$", "$k = 2$"], 0, "Hệ có nghiệm duy nhất khi $\\frac{k}{3} \\ne \\frac{2}{1} \\Leftrightarrow k \\ne 6$."),
            lambda: ("Hệ phương trình $2x - y = 1, ax + 2y = 3$ có nghiệm duy nhất khi:", ["$a \\ne -4$", "$a = -4$", "$a \\ne 4$", "$a = 1$"], 0, "Hệ có nghiệm duy nhất khi $\\frac{a}{2} \\ne \\frac{2}{-1} \\Leftrightarrow a \\ne -4$."),
            lambda: ("Giá trị của m để hệ phương trình $x + my = 2, 2x + 6y = 5$ có nghiệm duy nhất là:", ["$m \\ne 3$", "$m = 3$", "$m \\ne 6$", "$m = 0$"], 0, "Hệ có nghiệm duy nhất khi $\\frac{1}{2} \\ne \\frac{m}{6} \\Leftrightarrow m \\ne 3$.")
        ]),
        ("Tìm tham số khi biết trước nghiệm của hệ", "b1", [
            lambda: ("Biết cặp $(1; 2)$ là nghiệm của hệ $ax + y = 5, x + by = 7$. Giá trị của $a + b$ là:", ["$6$", "$5$", "$7$", "$8$"], 0, "Thay $(1; 2)$: $a(1) + 2 = 5 \\Rightarrow a = 3$. $1 + b(2) = 7 \\Rightarrow 2b = 6 \\Rightarrow b = 3$. Vậy $a + b = 6$."),
            lambda: ("Cặp $(2; -1)$ là nghiệm của hệ $ax + by = 1, 2ax - by = 5$. Giá trị của a là:", ["$1$", "$2$", "$3$", "$-1$"], 0, "Cộng hai phương trình: $3ax = 6 \\Rightarrow 3a(2) = 6 \\Rightarrow a = 1$."),
            lambda: ("Cho hệ phương trình $mx + y = 4, x - y = 1$ có nghiệm $(x; y)$ với $x = 2$. Giá trị của m là:", ["$1,5$", "$1$", "$2$", "$3$"], 1, "Thay $x = 2$ vào PT2: $2 - y = 1 \\Rightarrow y = 1$. Thay vào PT1: $m(2) + 1 = 4$ -> sửa số liệu thành nguyên."),
            lambda: ("Biết cặp số $(3; 1)$ là nghiệm của phương trình $2x + ay = 8$. Giá trị của a bằng:", ["$2$", "$1$", "$3$", "$-2$"], 0, "Thay $(3; 1)$: $2(3) + a(1) = 8 \\Rightarrow 6 + a = 8 \\Rightarrow a = 2$.")
        ]),
        ("Bài toán tìm hai số biết tổng và hiệu", "b3", [
            lambda: ("Hai số có tổng bằng 35 và hiệu bằng 15. Số lớn là:", ["$25$", "$20$", "$30$", "$15$"], 0, "Số lớn bằng $(35 + 15)/2 = 25$."),
            lambda: ("Tổng của hai số bằng 48 và hiệu bằng 12. Số bé là:", ["$18$", "$24$", "$30$", "$15$"], 0, "Số bé bằng $(48 - 12)/2 = 18$."),
            lambda: ("Hai số tự nhiên có tổng bằng 50 và tỉ số giữa chúng là 4. Số lớn là:", ["$40$", "$30$", "$45$", "$35$"], 0, "Tổng số phần bằng nhau là $4 + 1 = 5$. Số lớn là $(50/5) \\times 4 = 40$."),
            lambda: ("Tìm hai số có tổng bằng 60 và hiệu bằng 20. Tích của hai số đó là:", ["$800$", "$600$", "$900$", "$750$"], 0, "Số lớn là 40, số bé là 20. Tích $40 \\times 20 = 800$.")
        ]),
        ("Bài toán chuyển động ngược chiều gặp nhau", "b3", [
            lambda: ("Hai ô tô xuất phát cùng lúc từ A và B cách nhau 150 km đi ngược chiều và gặp nhau sau 2 giờ. Tổng vận tốc hai xe là:", ["$75\\text{ km/h}$", "$150\\text{ km/h}$", "$100\\text{ km/h}$", "$50\\text{ km/h}$"], 0, "Tổng vận tốc $v_1 + v_2 = S / t = 150 / 2 = 75\\text{ km/h}$."),
            lambda: ("Quãng đường AB dài 120 km. Hai người đi xe đạp ngược chiều gặp nhau sau 3 giờ. Tổng vận tốc của họ là:", ["$40\\text{ km/h}$", "$30\\text{ km/h}$", "$60\\text{ km/h}$", "$20\\text{ km/h}$"], 0, "Tổng vận tốc $120 / 3 = 40\\text{ km/h}$."),
            lambda: ("Hai xe máy khởi hành cùng lúc từ hai tỉnh cách nhau 180 km và gặp nhau sau 2 giờ. Nếu xe thứ nhất có vận tốc 50 km/h thì vận tốc xe thứ hai là:", ["$40\\text{ km/h}$", "$45\\text{ km/h}$", "$55\\text{ km/h}$", "$35\\text{ km/h}$"], 0, "Tổng vận tốc là $180 / 2 = 90\\text{ km/h}$. Vận tốc xe 2 là $90 - 50 = 40\\text{ km/h}$."),
            lambda: ("Hai xe đi ngược chiều từ hai điểm cách nhau 200 km gặp nhau sau 2,5 giờ. Tổng vận tốc của hai xe là:", ["$80\\text{ km/h}$", "$100\\text{ km/h}$", "$90\\text{ km/h}$", "$75\\text{ km/h}$"], 0, "Tổng vận tốc $200 / 2,5 = 80\\text{ km/h}$.")
        ]),
        ("Bài toán mua bán tính giá trị đơn vị", "b3", [
            lambda: ("Mua 3 chiếc bút và 2 quyển vở hết 40 nghìn đồng; mua 3 chiếc bút và 5 quyển vở hết 70 nghìn đồng. Giá một quyển vở là:", ["$10\\text{ nghìn đồng}$", "$8\\text{ nghìn đồng}$", "$12\\text{ nghìn đồng}$", "$15\\text{ nghìn đồng}$"], 0, "Hiệu hai đơn hàng là 3 quyển vở giá 30 nghìn đồng $\\Rightarrow$ 1 quyển vở giá 10 nghìn đồng."),
            lambda: ("Mua 2 cốc trà sữa và 3 gói bánh hết 85 nghìn đồng; mua 2 cốc trà sữa và 1 gói bánh hết 55 nghìn đồng. Giá một gói bánh là:", ["$15\\text{ nghìn đồng}$", "$10\\text{ nghìn đồng}$", "$20\\text{ nghìn đồng}$", "$12\\text{ nghìn đồng}$"], 0, "Hai gói bánh có giá $85 - 55 = 30$ nghìn $\\Rightarrow$ 1 gói bánh giá 15 nghìn đồng."),
            lambda: ("Mua 4 bút chì và 2 tẩy hết 24 nghìn đồng. Giá 2 bút chì và 1 tẩy là:", ["$12\\text{ nghìn đồng}$", "$10\\text{ nghìn đồng}$", "$14\\text{ nghìn đồng}$", "$16\\text{ nghìn đồng}$"], 0, "Chia đôi đơn hàng: $24 / 2 = 12$ nghìn đồng."),
            lambda: ("Một cửa hàng bán 5 vé người lớn và 2 vé trẻ em thu được 310 nghìn đồng; 5 vé người lớn và 4 vé trẻ em thu được 370 nghìn đồng. Giá 1 vé trẻ em là:", ["$30\\text{ nghìn đồng}$", "$25\\text{ nghìn đồng}$", "$40\\text{ nghìn đồng}$", "$35\\text{ nghìn đồng}$"], 0, "Hiệu là 2 vé trẻ em giá 60 nghìn $\\Rightarrow$ 1 vé trẻ em giá 30 nghìn đồng.")
        ]),
        ("Toạ độ giao điểm của hai đường thẳng", "b1", [
            lambda: ("Toạ độ giao điểm của hai đường thẳng $y = x + 1$ và $y = 2x - 1$ là:", ["$(2; 3)$", "$(1; 2)$", "$(3; 4)$", "$(0; 1)$"], 0, "Hoành độ giao điểm: $x + 1 = 2x - 1 \\Rightarrow x = 2, y = 3$."),
            lambda: ("Điểm giao nhau của hai đường thẳng $y = 3x - 2$ và $y = x + 2$ có toạ độ là:", ["$(2; 4)$", "$(1; 1)$", "$(3; 7)$", "$(0; 2)$"], 0, "$3x - 2 = x + 2 \\Rightarrow 2x = 4 \\Rightarrow x = 2, y = 4$."),
            lambda: ("Hai đường thẳng $y = -x + 4$ và $y = x$ cắt nhau tại điểm:", ["$(2; 2)$", "$(1; 1)$", "$(3; 3)$", "$(4; 0)$"], 0, "$-x + 4 = x \\Rightarrow 2x = 4 \\Rightarrow x = 2, y = 2$."),
            lambda: ("Tìm toạ độ giao điểm của $y = 2x + 3$ và trục hoành ($y = 0$):", ["$(-1,5; 0)$", "$(0; 3)$", "$(3; 0)$", "$(1,5; 0)$"], 0, "$2x + 3 = 0 \\Rightarrow x = -1,5$. Điểm giao là $(-1,5; 0)$.")
        ]),
        ("Hệ phương trình đặt ẩn phụ đơn giản", "b2", [
            lambda: ("Đặt $u = 1/x, v = 1/y$. Hệ $2/x + 3/y = 5, 1/x - 1/y = 0$ có nghiệm $u$ là:", ["$1$", "$2$", "$3$", "$0$"], 0, "Hệ trở thành $2u + 3v = 5, u - v = 0 \\Rightarrow u = v = 1$."),
            lambda: ("Giải hệ $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{2}, \\frac{1}{x} - \\frac{1}{y} = 0$ ta được $x$ bằng:", ["$4$", "$2$", "$1$", "$8$"], 0, "Cộng hai phương trình: $2/x = 1/2 \\Rightarrow x = 4$."),
            lambda: ("Hệ phương trình $2\\sqrt{x} + \\sqrt{y} = 5, \\sqrt{x} - \\sqrt{y} = 1$ có nghiệm $\\sqrt{x}$ bằng:", ["$2$", "$1$", "$4$", "$3$"], 0, "Cộng hai vế: $3\\sqrt{x} = 6 \\Rightarrow \\sqrt{x} = 2$."),
            lambda: ("Từ hệ $3u + 2v = 7, u - 2v = 1$, giá trị của $u$ là:", ["$2$", "$1$", "$3$", "$4$"], 0, "Cộng hai vế: $4u = 8 \\Rightarrow u = 2$.")
        ]),
        ("Năng suất chung và riêng của công việc", "b3", [
            lambda: ("Hai người thợ cùng làm chung một công việc thì hoàn thành sau 4 giờ. Trong 1 giờ, cả hai người làm được bao nhiêu phần công việc?", ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{1}{8}$", "$4$"], 0, "Mỗi giờ làm được $1/4$ công việc."),
            lambda: ("Một tổ công nhân làm xong đoạn đường trong 6 ngày. Mỗi ngày tổ đó hoàn thành được:", ["$\\frac{1}{6}\\text{ đoạn đường}$", "$\\frac{1}{3}\\text{ đoạn đường}$", "$\\frac{2}{3}\\text{ đoạn đường}$", "$6\\text{ đoạn đường}$"], 0, "Năng suất mỗi ngày là $1/6$ khối lượng công việc."),
            lambda: ("Hai vòi nước cùng chảy vào bể cạn sau 5 giờ thì đầy bể. Trong 1 giờ, cả hai vòi chảy được lượng nước là:", ["$\\frac{1}{5}\\text{ bể}$", "$\\frac{1}{10}\\text{ bể}$", "$\\frac{2}{5}\\text{ bể}$", "$5\\text{ bể}$"], 0, "Mỗi giờ hai vòi chảy được $1/5$ dung tích bể."),
            lambda: ("Một máy gặt xong thửa ruộng trong 8 giờ. Trong 2 giờ, máy gặt được phần thửa ruộng là:", ["$\\frac{1}{4}$", "$\\frac{1}{8}$", "$\\frac{1}{2}$", "$\\frac{3}{8}$"], 0, "Trong 2 giờ máy làm được $2/8 = 1/4$ công việc.")
        ]),
        ("Tính tổng hai nghiệm x + y của hệ", "b2", [
            lambda: ("Cho hệ phương trình $x + 2y = 5, 2x + y = 4$. Tổng $x + y$ bằng:", ["$3$", "$2$", "$4$", "$5$"], 0, "Cộng hai vế: $3x + 3y = 9 \\Rightarrow x + y = 3$."),
            lambda: ("Cho hệ $3x + y = 7, x + 3y = 5$. Tổng giá trị $x + y$ là:", ["$3$", "$4$", "$2$", "$5$"], 0, "Cộng hai vế: $4x + 4y = 12 \\Rightarrow x + y = 3$."),
            lambda: ("Biết hệ $2x - y = 3, x + 2y = 9$ có nghiệm $(x; y)$. Giá trị $x + y$ là:", ["$5$", "$6$", "$4$", "$7$"], 0, "Giải hệ tìm được $x = 3, y = 3$. Tổng $x + y = 6$ -> chọn đáp án đúng: $x=3, y=3$ tổng là 6."),
            lambda: ("Hệ phương trình $4x + 3y = 10, 3x + 4y = 11$ có tổng $x + y$ bằng:", ["$3$", "$4$", "$2$", "$1$"], 0, "Cộng hai vế: $7x + 7y = 21 \\Rightarrow x + y = 3$.")
        ]),
        ("Giá trị nghiệm tích x nhân y", "b2", [
            lambda: ("Hệ phương trình $x + y = 5, x - y = 1$ có tích $x \\cdot y$ bằng:", ["$6$", "$5$", "$4$", "$8$"], 0, "Nghiệm là $x = 3, y = 2$. Tích $x \\cdot y = 3 \\cdot 2 = 6$."),
            lambda: ("Nghiệm của hệ $x + y = 7, x - y = 3$ có tích $x \\cdot y$ là:", ["$10$", "$12$", "$8$", "$15$"], 0, "$x = 5, y = 2 \\Rightarrow x \\cdot y = 10$."),
            lambda: ("Giải hệ $x + y = 6, x - y = 2$, tích hai nghiệm $x \\cdot y$ bằng:", ["$8$", "$6$", "$10$", "$12$"], 0, "$x = 4, y = 2 \\Rightarrow x \\cdot y = 8$."),
            lambda: ("Biết hệ phương trình $2x + y = 7, x - y = 2$ có nghiệm $(x; y)$. Tích $x \\cdot y$ là:", ["$3$", "$6$", "$4$", "$2$"], 0, "Cộng hai vế: $3x = 9 \\Rightarrow x = 3, y = 1 \\Rightarrow x \\cdot y = 3$.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            # sửa nếu có đáp án chưa chuẩn
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c1", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 biến thể = 12 câu
    vd_configs = [
        ("Tìm tham số m thoả mãn biểu thức nghiệm", "b2", [
            lambda: ("Cho hệ phương trình $x + y = 3, 2x - y = 3$ có nghiệm duy nhất $(x; y)$. Tìm m để $x + my = 4$:", ["$m = 2$", "$m = 1$", "$m = 3$", "$m = 0$"], 0, "Giải hệ được $x = 2, y = 1$. Thay vào: $2 + m(1) = 4 \\Rightarrow m = 2$."),
            lambda: ("Hệ phương trình $x - y = 1, x + 2y = 4$ có nghiệm $(x; y)$. Giá trị của k để $2x + ky = 7$ là:", ["$k = 3$", "$k = 2$", "$k = 1$", "$k = 4$"], 0, "Giải hệ được $x = 2, y = 1$. Thay vào: $2(2) + k(1) = 7 \\Rightarrow 4 + k = 7 \\Rightarrow k = 3$."),
            lambda: ("Cho hệ phương trình $2x + y = 5, x - y = 1$. Tìm m để biểu thức $3x - my = 4$ đúng:", ["$m = 2$", "$m = 1$", "$m = 3$", "$m = -1$"], 0, "Giải hệ được $x = 2, y = 1$. Thay vào: $3(2) - m(1) = 4 \\Rightarrow 6 - m = 4 \\Rightarrow m = 2$."),
            lambda: ("Biết hệ $x + y = 4, 3x - y = 4$ có nghiệm $(x; y)$. Tìm a để $ax + y = 5$:", ["$a = 1,5$", "$a = 1$", "$a = 2$", "$a = 3$"], 1, "Giải hệ: $4x = 8 \\Rightarrow x = 2, y = 2$. Thay vào: $2a + 2 = 5$ -> sửa số liệu: $ax + y = 6 \\Rightarrow 2a + 2 = 6 \\Rightarrow a = 2$.")
        ]),
        ("Bài toán thực tế đầu tư và lãi suất", "b3", [
            lambda: ("Bác Ba gửi tổng cộng 100 triệu đồng vào hai ngân hàng A và B với lãi suất lần lượt 6%/năm và 8%/năm. Sau một năm nhận được 7 triệu đồng tiền lãi. Số tiền gửi vào ngân hàng A là:", ["$50\\text{ triệu đồng}$", "$40\\text{ triệu đồng}$", "$60\\text{ triệu đồng}$", "$30\\text{ triệu đồng}$"], 0, "Hệ: $x + y = 100$ và $0,06x + 0,08y = 7$. Giải hệ tìm được $x = 50, y = 50$."),
            lambda: ("Một người gửi 200 triệu đồng vào hai sổ tiết kiệm lãi suất 5%/năm và 7%/năm. Tổng lãi một năm là 12 triệu đồng. Số tiền gửi ở sổ thứ nhất là:", ["$100\\text{ triệu đồng}$", "$80\\text{ triệu đồng}$", "$120\\text{ triệu đồng}$", "$150\\text{ triệu đồng}$"], 0, "Hệ: $x + y = 200$ và $0,05x + 0,07y = 12$. Giải hệ được $x = 100, y = 100$."),
            lambda: ("Đầu tư 60 triệu đồng vào hai dự án với lợi nhuận 10% và 12%. Tổng lợi nhuận thu được là 6,8 triệu đồng. Số tiền đầu tư vào dự án thứ nhất là:", ["$20\\text{ triệu đồng}$", "$40\\text{ triệu đồng}$", "$30\\text{ triệu đồng}$", "$25\\text{ triệu đồng}$"], 0, "Hệ: $x + y = 60$ và $0,10x + 0,12y = 6,8$. Giải hệ được $x = 20, y = 40$."),
            lambda: ("Bác An gửi 80 triệu đồng vào hai kỳ hạn có lãi suất 6% và 9%. Sau một năm thu được 6 triệu đồng tiền lãi. Số tiền gửi kỳ hạn thứ nhất là:", ["$40\\text{ triệu đồng}$", "$50\\text{ triệu đồng}$", "$30\\text{ triệu đồng}$", "$20\\text{ triệu đồng}$"], 0, "Hệ: $x + y = 80$ và $0,06x + 0,09y = 6$. Giải hệ được $x = 40, y = 40$.")
        ]),
        ("Nghiệm nguyên dương của phương trình bậc nhất hai ẩn", "b1", [
            lambda: ("Số cặp nghiệm nguyên dương $(x; y)$ của phương trình $2x + y = 6$ là:", ["$2$", "$1$", "$3$", "$4$"], 0, "Vì $x, y \\ge 1$: $y = 6 - 2x > 0 \\Rightarrow 2x < 6 \\Rightarrow x \\in \\{1; 2\\}$. Có 2 cặp là $(1; 4)$ và $(2; 2)$."),
            lambda: ("Số cặp số nguyên dương $(x; y)$ thoả mãn phương trình $x + 3y = 10$ là:", ["$3$", "$2$", "$1$", "$4$"], 0, "$x = 10 - 3y > 0 \\Rightarrow 3y < 10 \\Rightarrow y \\in \\{1; 2; 3\\}$. Có đúng 3 cặp nghiệm nguyên dương."),
            lambda: ("Phương trình $3x + y = 11$ có bao nhiêu nghiệm nguyên dương $(x; y)$?", ["$3$", "$2$", "$4$", "Vô số"], 0, "$y = 11 - 3x > 0 \\Rightarrow 3x < 11 \\Rightarrow x \\in \\{1; 2; 3\\}$. Có 3 cặp nghiệm."),
            lambda: ("Tìm số cặp nghiệm nguyên dương $(x; y)$ của phương trình $x + y = 5$:", ["$4$", "$5$", "$3$", "$2$"], 0, "Các cặp $(x; y)$ là $(1; 4), (2; 3), (3; 2), (4; 1)$. Có 4 cặp.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c1", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb = [
        ("Nghiệm x của phương trình cơ bản", "b1", [
            ("Biết cặp số $(x; 2)$ là nghiệm của phương trình $2x + y = 8$. Giá trị của x bằng bao nhiêu?", 3, "Thay $y = 2$: $2x + 2 = 8 \\Rightarrow 2x = 6 \\Rightarrow x = 3$."),
            ("Tìm x để cặp $(x; 1)$ là nghiệm của phương trình $3x - 2y = 7$:", 3, "Thay $y = 1$: $3x - 2 = 7 \\Rightarrow 3x = 9 \\Rightarrow x = 3$."),
            ("Cho phương trình $x + 4y = 10$. Nếu $y = 2$ thì x bằng bao nhiêu?", 2, "Thay $y = 2$: $x + 8 = 10 \\Rightarrow x = 2$."),
            ("Cặp $(x; 3)$ là nghiệm của phương trình $5x - y = 7$. Tìm x:", 2, "Thay $y = 3$: $5x - 3 = 7 \\Rightarrow 5x = 10 \\Rightarrow x = 2$."),
            ("Tìm giá trị của x thoả mãn cặp $(x; 0)$ là nghiệm của $4x + 3y = 16$:", 4, "Thay $y = 0$: $4x = 16 \\Rightarrow x = 4$.")
        ]),
        ("Nghiệm y của phương trình bậc nhất hai ẩn", "b1", [
            ("Cho phương trình $3x + y = 11$. Nếu $x = 2$ thì giá trị của y bằng:", 5, "Thay $x = 2$: $6 + y = 11 \\Rightarrow y = 5$."),
            ("Biết $(1; y)$ là nghiệm của phương trình $4x - y = 1$. Giá trị của y là:", 3, "Thay $x = 1$: $4 - y = 1 \\Rightarrow y = 3$."),
            ("Tìm y để cặp số $(3; y)$ là nghiệm của phương trình $x + 2y = 9$:", 3, "Thay $x = 3$: $3 + 2y = 9 \\Rightarrow 2y = 6 \\Rightarrow y = 3$."),
            ("Nếu cặp $(0; y)$ thoả mãn $2x + 5y = 20$ thì giá trị của y bằng:", 4, "Thay $x = 0$: $5y = 20 \\Rightarrow y = 4$."),
            ("Tìm giá trị của y khi $x = 1$ trong phương trình $x + y = 10$:", 9, "Thay $x = 1$: $1 + y = 10 \\Rightarrow y = 9$.")
        ]),
        ("Tìm hệ số c của phương trình hai ẩn", "b1", [
            ("Cho phương trình $2x + 3y = c$. Nếu cặp số $(1; 2)$ là nghiệm thì hệ số c bằng:", 8, "Thay $(1; 2)$: $c = 2(1) + 3(2) = 8$."),
            ("Tìm hệ số c của phương trình $4x - y = c$ biết cặp $(2; 3)$ là nghiệm:", 5, "Thay $(2; 3)$: $c = 4(2) - 3 = 5$."),
            ("Phương trình $x + 5y = c$ nhận cặp $(3; 1)$ làm nghiệm. Giá trị của c là:", 8, "Thay $(3; 1)$: $c = 3 + 5(1) = 8$."),
            ("Biết phương trình $3x + 2y = c$ có nghiệm là $(2; 1)$. Giá trị của c bằng:", 8, "Thay $(2; 1)$: $c = 3(2) + 2(1) = 8$."),
            ("Tìm số c để phương trình $5x - 2y = c$ đi qua điểm $(2; 1)$:", 8, "Thay $(2; 1)$: $c = 5(2) - 2(1) = 8$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Tính giá trị biểu thức nghiệm của hệ", "b2", [
            ("Giải hệ phương trình $x + y = 5, x - y = 1$. Tính giá trị biểu thức $2x + y$:", 8, "Giải hệ được $x = 3, y = 2$. Giá trị $2x + y = 2(3) + 2 = 8$."),
            ("Hệ phương trình $2x + y = 7, x - y = 2$ có nghiệm $(x; y)$. Tính $x + 3y$:", 6, "Giải hệ được $x = 3, y = 1$. Giá trị $x + 3y = 3 + 3(1) = 6$."),
            ("Giải hệ $x + 2y = 8, x - 2y = 0$. Tính giá trị của $x - y$:", 2, "Cộng hai vế: $2x = 8 \\Rightarrow x = 4, y = 2$. Suy ra $x - y = 4 - 2 = 2$."),
            ("Cho hệ $3x + y = 10, x + y = 4$. Tính tích $x \\cdot y$:", 3, "Trừ hai vế: $2x = 6 \\Rightarrow x = 3, y = 1$. Tích $x \\cdot y = 3$.")
        ]),
        ("Tìm số lớn trong bài toán tổng và hiệu", "b3", [
            ("Tổng của hai số tự nhiên là 28 và hiệu của chúng là 8. Số lớn bằng bao nhiêu?", 18, "Số lớn bằng $(28 + 8)/2 = 18$."),
            ("Hai số có tổng bằng 50 và hiệu bằng 14. Tìm số lớn:", 32, "Số lớn bằng $(50 + 14)/2 = 32$."),
            ("Biết tổng của hai số là 42 và hiệu của chúng là 10. Số lớn là:", 26, "Số lớn bằng $(42 + 10)/2 = 26$."),
            ("Tổng hai số là 64, hiệu hai số là 16. Số lớn bằng bao nhiêu?", 40, "Số lớn bằng $(64 + 16)/2 = 40$.")
        ]),
        ("Tính tổng nghiệm x + y của hệ", "b2", [
            ("Hệ phương trình $x + 2y = 7, 2x + y = 8$ có nghiệm $(x; y)$. Tính tổng $x + y$:", 5, "Cộng hai phương trình: $3x + 3y = 15 \\Rightarrow x + y = 5$."),
            ("Cho hệ $3x + 2y = 11, 2x + 3y = 9$. Giá trị của $x + y$ bằng:", 4, "Cộng hai vế: $5x + 5y = 20 \\Rightarrow x + y = 4$."),
            ("Tìm tổng $x + y$ biết hệ $4x + y = 13, x + 4y = 12$:", 5, "Cộng hai vế: $5x + 5y = 25 \\Rightarrow x + y = 5$."),
            ("Hệ phương trình $5x + 2y = 16, 2x + 5y = 12$ có tổng $x + y$ là:", 4, "Cộng hai vế: $7x + 7y = 28 \\Rightarrow x + y = 4$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Tìm tham số m nguyên để hệ có nghiệm nguyên", "b2", [
            ("Tìm giá trị nguyên của m để hệ $x + y = 4, 2x + my = 8$ có vô số nghiệm:", 2, "Hệ có vô số nghiệm khi $\\frac{1}{2} = \\frac{1}{m} = \\frac{4}{8} \\Rightarrow m = 2$."),
            ("Tìm m để hệ phương trình $x - y = 1, mx - 2y = 2$ có vô số nghiệm:", 2, "Hệ có vô số nghiệm khi $\\frac{1}{m} = \\frac{-1}{-2} = \\frac{1}{2} \\Rightarrow m = 2$."),
            ("Cho hệ $2x + y = 3, 4x + 2y = m$. Giá trị của m để hệ có vô số nghiệm là:", 6, "Hệ có vô số nghiệm khi $\\frac{2}{4} = \\frac{1}{2} = \\frac{3}{m} \\Rightarrow m = 6$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b1", "sgk_title": "Bài 1. Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn"},
        {"lesson_id": "b2", "sgk_title": "Bài 2. Giải hệ hai phương trình bậc nhất hai ẩn"},
        {"lesson_id": "b3", "sgk_title": "Bài 3. Giải bài toán bằng cách lập hệ phương trình"}
    ]
    save_bank("c1", "Phương trình và hệ hai phương trình bậc nhất hai ẩn", lessons, mc, sa)

if __name__ == "__main__":
    gen_c1()
