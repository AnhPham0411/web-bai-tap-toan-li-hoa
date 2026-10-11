# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

# ==============================================================================
# CHƯƠNG 3: CĂN BẬC HAI VÀ CĂN BẬC BA
# ==============================================================================
def gen_c3():
    mc, sa = [], []

    nb_configs = [
        ("Khái niệm căn bậc hai số học", "b7", [
            lambda: ("Căn bậc hai số học của số 9 là:", ["$3$", "$-3$", "$\\pm 3$", "$81$"], 0, "Căn bậc hai số học của 9 là $\\sqrt{9} = 3$."),
            lambda: ("Căn bậc hai số học của 16 bằng:", ["$4$", "$-4$", "$\\pm 4$", "$256$"], 0, "$\\sqrt{16} = 4$."),
            lambda: ("Tìm căn bậc hai số học của số 25:", ["$5$", "$-5$", "$\\pm 5$", "$625$"], 0, "$\\sqrt{25} = 5$."),
            lambda: ("Số nào sau đây là căn bậc hai số học của 36?", ["$6$", "$-6$", "$\\pm 6$", "$18$"], 0, "$\\sqrt{36} = 6$."),
            lambda: ("Căn bậc hai số học của số 49 là:", ["$7$", "$-7$", "$\\pm 7$", "$14$"], 0, "$\\sqrt{49} = 7$.")
        ]),
        ("Điều kiện xác định căn thức bậc hai", "b7", [
            lambda: ("Căn thức $\\sqrt{x - 3}$ xác định khi và chỉ khi:", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x \\ne 3$"], 0, "Biểu thức dưới dấu căn không âm: $x - 3 \\ge 0 \\Leftrightarrow x \\ge 3$."),
            lambda: ("Tìm điều kiện để $\\sqrt{x - 5}$ có nghĩa:", ["$x \\ge 5$", "$x > 5$", "$x \\le 5$", "$x \\ne 5$"], 0, "$x - 5 \\ge 0 \\Leftrightarrow x \\ge 5$."),
            lambda: ("Biểu thức $\\sqrt{2x - 4}$ xác định với các giá trị x thoả mãn:", ["$x \\ge 2$", "$x > 2$", "$x \\le 2$", "$x \\ge 4$"], 0, "$2x - 4 \\ge 0 \\Leftrightarrow 2x \\ge 4 \\Leftrightarrow x \\ge 2$."),
            lambda: ("Căn thức $\\sqrt{x + 2}$ có nghĩa khi:", ["$x \\ge -2$", "$x > -2$", "$x \\le -2$", "$x \\ne -2$"], 0, "$x + 2 \\ge 0 \\Leftrightarrow x \\ge -2$."),
            lambda: ("Điều kiện xác định của biểu thức $\\sqrt{3 - x}$ là:", ["$x \\le 3$", "$x < 3$", "$x \\ge 3$", "$x \\ne 3$"], 0, "$3 - x \\ge 0 \\Leftrightarrow x \\le 3$.")
        ]),
        ("Hằng đẳng thức căn bậc hai cơ bản", "b7", [
            lambda: ("Giá trị của biểu thức $\\sqrt{(-4)^2}$ bằng:", ["$4$", "$-4$", "$\\pm 4$", "$16$"], 0, "$\\sqrt{(-4)^2} = |-4| = 4$."),
            lambda: ("Tính giá trị của $\\sqrt{(-7)^2}$:", ["$7$", "$-7$", "$\\pm 7$", "$49$"], 0, "$\\sqrt{(-7)^2} = |-7| = 7$."),
            lambda: ("Kết quả của phép tính $\\sqrt{(-9)^2}$ là:", ["$9$", "$-9$", "$\\pm 9$", "$81$"], 0, "$\\sqrt{(-9)^2} = |-9| = 9$."),
            lambda: ("Tính $\\sqrt{(-5)^2}$ ta được:", ["$5$", "$-5$", "$\\pm 5$", "$25$"], 0, "$\\sqrt{(-5)^2} = |-5| = 5$."),
            lambda: ("Biểu thức $\\sqrt{(-10)^2}$ có giá trị bằng:", ["$10$", "$-10$", "$\\pm 10$", "$100$"], 0, "$\\sqrt{(-10)^2} = |-10| = 10$.")
        ]),
        ("Khai phương một tích", "b8", [
            lambda: ("Tính giá trị của biểu thức $\\sqrt{4 \\cdot 9}$:", ["$6$", "$36$", "$12$", "$5$"], 0, "$\\sqrt{4 \\cdot 9} = \\sqrt{4} \\cdot \\sqrt{9} = 2 \\cdot 3 = 6$."),
            lambda: ("Kết quả của phép tính $\\sqrt{9 \\cdot 16}$ là:", ["$12$", "$144$", "$7$", "$24$"], 0, "$\\sqrt{9} \\cdot \\sqrt{16} = 3 \\cdot 4 = 12$."),
            lambda: ("Tính $\\sqrt{25 \\cdot 4}$ thu được:", ["$10$", "$100$", "$20$", "$50$"], 0, "$\\sqrt{25} \\cdot \\sqrt{4} = 5 \\cdot 2 = 10$."),
            lambda: ("Giá trị của $\\sqrt{16 \\cdot 25}$ bằng:", ["$20$", "$400$", "$9$", "$40$"], 0, "$\\sqrt{16} \\cdot \\sqrt{25} = 4 \\cdot 5 = 20$."),
            lambda: ("Tính kết quả của $\\sqrt{4 \\cdot 36}$:", ["$12$", "$144$", "$8$", "$24$"], 0, "$\\sqrt{4} \\cdot \\sqrt{36} = 2 \\cdot 6 = 12$.")
        ]),
        ("Khai phương một thương", "b8", [
            lambda: ("Tính giá trị của $\\sqrt{\\frac{9}{16}}$:", ["$\\frac{3}{4}$", "$\\frac{9}{4}$", "$\\frac{3}{16}$", "$\\frac{4}{3}$"], 0, "$\\frac{\\sqrt{9}}{\\sqrt{16}} = \\frac{3}{4}$."),
            lambda: ("Kết quả của phép tính $\\sqrt{\\frac{25}{36}}$ là:", ["$\\frac{5}{6}$", "$\\frac{25}{6}$", "$\\frac{5}{36}$", "$\\frac{6}{5}$"], 0, "$\\frac{\\sqrt{25}}{\\sqrt{36}} = \\frac{5}{6}$."),
            lambda: ("Tính $\\sqrt{\\frac{4}{49}}$ thu được:", ["$\\frac{2}{7}$", "$\\frac{4}{7}$", "$\\frac{2}{49}$", "$\\frac{7}{2}$"], 0, "$\\frac{\\sqrt{4}}{\\sqrt{49}} = \\frac{2}{7}$."),
            lambda: ("Giá trị của $\\sqrt{\\frac{1}{64}}$ bằng:", ["$\\frac{1}{8}$", "$\\frac{1}{64}$", "$\\frac{1}{16}$", "$8$"], 0, "$\\frac{\\sqrt{1}}{\\sqrt{64}} = \\frac{1}{8}$."),
            lambda: ("Tính kết quả $\\sqrt{\\frac{16}{81}}$:", ["$\\frac{4}{9}$", "$\\frac{16}{9}$", "$\\frac{4}{81}$", "$\\frac{9}{4}$"], 0, "$\\frac{\\sqrt{16}}{\\sqrt{81}} = \\frac{4}{9}$.")
        ]),
        ("Đưa thừa số ra ngoài dấu căn", "b9", [
            lambda: ("Đưa thừa số ra ngoài dấu căn của biểu thức $\\sqrt{12}$:", ["$2\\sqrt{3}$", "$3\\sqrt{2}$", "$4\\sqrt{3}$", "$6$"], 0, "$\\sqrt{12} = \\sqrt{4 \\cdot 3} = 2\\sqrt{3}$."),
            lambda: ("Biểu diễn $\\sqrt{18}$ dưới dạng đưa thừa số ra ngoài căn:", ["$3\\sqrt{2}$", "$2\\sqrt{3}$", "$9\\sqrt{2}$", "$6$"], 0, "$\\sqrt{18} = \\sqrt{9 \\cdot 2} = 3\\sqrt{2}$."),
            lambda: ("Đưa thừa số ra ngoài dấu căn của $\\sqrt{20}$ ta được:", ["$2\\sqrt{5}$", "$5\\sqrt{2}$", "$4\\sqrt{5}$", "$10$"], 0, "$\\sqrt{20} = \\sqrt{4 \\cdot 5} = 2\\sqrt{5}$."),
            lambda: ("Rút gọn $\\sqrt{27}$ bằng cách đưa thừa số ra ngoài căn:", ["$3\\sqrt{3}$", "$9\\sqrt{3}$", "$3\\sqrt{9}$", "$6\\sqrt{3}$"], 0, "$\\sqrt{27} = \\sqrt{9 \\cdot 3} = 3\\sqrt{3}$."),
            lambda: ("Tính $\\sqrt{32}$ theo dạng đưa thừa số ra ngoài căn:", ["$4\\sqrt{2}$", "$2\\sqrt{8}$", "$16\\sqrt{2}$", "$8\\sqrt{2}$"], 0, "$\\sqrt{32} = \\sqrt{16 \\cdot 2} = 4\\sqrt{2}$.")
        ]),
        ("Đưa thừa số vào trong dấu căn", "b9", [
            lambda: ("Đưa thừa số vào trong dấu căn của $2\\sqrt{3}$ ta được:", ["$\\sqrt{12}$", "$\\sqrt{6}$", "$\\sqrt{18}$", "$\\sqrt{24}$"], 0, "$2\\sqrt{3} = \\sqrt{2^2 \\cdot 3} = \\sqrt{12}$."),
            lambda: ("Đưa số 3 vào trong dấu căn của $3\\sqrt{2}$:", ["$\\sqrt{18}$", "$\\sqrt{6}$", "$\\sqrt{12}$", "$\\sqrt{36}$"], 0, "$3\\sqrt{2} = \\sqrt{3^2 \\cdot 2} = \\sqrt{18}$."),
            lambda: ("Biểu diễn $4\\sqrt{2}$ dưới dạng căn bậc hai đơn:", ["$\\sqrt{32}$", "$\\sqrt{8}$", "$\\sqrt{16}$", "$\\sqrt{64}$"], 0, "$4\\sqrt{2} = \\sqrt{16 \\cdot 2} = \\sqrt{32}$."),
            lambda: ("Đưa thừa số vào trong căn của $2\\sqrt{5}$:", ["$\\sqrt{20}$", "$\\sqrt{10}$", "$\\sqrt{40}$", "$\\sqrt{50}$"], 0, "$2\\sqrt{5} = \\sqrt{4 \\cdot 5} = \\sqrt{20}$."),
            lambda: ("Đưa số 5 vào trong dấu căn của $5\\sqrt{3}$ ta được:", ["$\\sqrt{75}$", "$\\sqrt{15}$", "$\\sqrt{45}$", "$\\sqrt{30}$"], 0, "$5\\sqrt{3} = \\sqrt{25 \\cdot 3} = \\sqrt{75}$.")
        ]),
        ("Khái niệm căn bậc ba", "b10", [
            lambda: ("Căn bậc ba của -8 là:", ["$-2$", "$2$", "$\\pm 2$", "Không tồn tại"], 0, "Vì $(-2)^3 = -8$ nên $\\sqrt[3]{-8} = -2$."),
            lambda: ("Tính căn bậc ba của 27:", ["$3$", "$-3$", "$\\pm 3$", "$9$"], 0, "Vì $3^3 = 27$ nên $\\sqrt[3]{27} = 3$."),
            lambda: ("Giá trị của $\\sqrt[3]{-64}$ bằng:", ["$-4$", "$4$", "$\\pm 4$", "$-8$"], 0, "$(-4)^3 = -64 \\Rightarrow \\sqrt[3]{-64} = -4$."),
            lambda: ("Căn bậc ba của số 125 là:", ["$5$", "$-5$", "$\\pm 5$", "$25$"], 0, "$5^3 = 125 \\Rightarrow \\sqrt[3]{125} = 5$."),
            lambda: ("Tính căn bậc ba của -1:", ["$-1$", "$1$", "$\\pm 1$", "Không xác định"], 0, "$(-1)^3 = -1 \\Rightarrow \\sqrt[3]{-1} = -1$.")
        ]),
        ("Hằng đẳng thức căn bậc ba", "b10", [
            lambda: ("Giá trị của $(\\sqrt[3]{5})^3$ bằng:", ["$5$", "$25$", "$\\sqrt{5}$", "$125$"], 0, "Theo định nghĩa, $(\\sqrt[3]{a})^3 = a$ nên bằng 5."),
            lambda: ("Tính giá trị của $(\\sqrt[3]{-7})^3$:", ["$-7$", "$7$", "$-343$", "$49$"], 0, "$(\\sqrt[3]{-7})^3 = -7$."),
            lambda: ("Biểu thức $(\\sqrt[3]{11})^3$ có kết quả là:", ["$11$", "$121$", "$\\sqrt{11}$", "$1$"], 0, "Bằng 11."),
            lambda: ("Giá trị của $(\\sqrt[3]{-2})^3$ là:", ["$-2$", "$2$", "$-8$", "$4$"], 0, "Bằng -2."),
            lambda: ("Kết quả của $(\\sqrt[3]{3})^3$ bằng:", ["$3$", "$9$", "$27$", "$\\sqrt{3}$"], 0, "Bằng 3.")
        ]),
        ("Trục căn thức ở mẫu đơn giản", "b9", [
            lambda: ("Trục căn thức ở mẫu của $\\frac{1}{\\sqrt{2}}$ ta được:", ["$\\frac{\\sqrt{2}}{2}$", "$\\sqrt{2}$", "$\\frac{1}{2}$", "$2\\sqrt{2}$"], 0, "Nhân cả tử và mẫu với $\\sqrt{2}$: $\\frac{\\sqrt{2}}{2}$."),
            lambda: ("Khử căn thức ở mẫu của $\\frac{3}{\\sqrt{3}}$ thu được:", ["$\\sqrt{3}$", "$3\\sqrt{3}$", "$\\frac{\\sqrt{3}}{3}$", "$3$"], 0, "$\\frac{3}{\\sqrt{3}} = \\frac{3\\sqrt{3}}{3} = \\sqrt{3}$."),
            lambda: ("Trục căn thức ở mẫu của biểu thức $\\frac{2}{\\sqrt{5}}$:", ["$\\frac{2\\sqrt{5}}{5}$", "$\\frac{\\sqrt{5}}{5}$", "$2\\sqrt{5}$", "$\\frac{5\\sqrt{2}}{2}$"], 0, "Nhân tử và mẫu với $\\sqrt{5}$: $\\frac{2\\sqrt{5}}{5}$."),
            lambda: ("Kết quả trục căn thức ở mẫu của $\\frac{6}{\\sqrt{3}}$ là:", ["$2\\sqrt{3}$", "$3\\sqrt{3}$", "$\\frac{2\\sqrt{3}}{3}$", "$6\\sqrt{3}$"], 0, "$\\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}$."),
            lambda: ("Trục căn thức ở mẫu của phân số $\\frac{5}{\\sqrt{5}}$ ta được:", ["$\\sqrt{5}$", "$5\\sqrt{5}$", "$\\frac{\\sqrt{5}}{5}$", "$1$"], 0, "$\\frac{5\\sqrt{5}}{5} = \\sqrt{5}$.")
        ]),
        ("So sánh hai căn bậc hai", "b7", [
            lambda: ("So sánh $\\sqrt{7}$ và $\\sqrt{5}$:", ["$\\sqrt{7} > \\sqrt{5}$", "$\\sqrt{7} < \\sqrt{5}$", "$\\sqrt{7} = \\sqrt{5}$", "Không so sánh được"], 0, "Vì 7 > 5 nên $\\sqrt{7} > \\sqrt{5}$."),
            lambda: ("So sánh số 3 và $\\sqrt{8}$:", ["$3 > \\sqrt{8}$", "$3 < \\sqrt{8}$", "$3 = \\sqrt{8}$", "$3 \\le \\sqrt{8}$"], 0, "Vì $3 = \\sqrt{9}$ và 9 > 8 nên $3 > \\sqrt{8}$."),
            lambda: ("So sánh số 4 và $\\sqrt{17}$:", ["$4 < \\sqrt{17}$", "$4 > \\sqrt{17}$", "$4 = \\sqrt{17}$", "$4 \\ge \\sqrt{17}$"], 0, "Vì $4 = \\sqrt{16}$ và 16 < 17 nên $4 < \\sqrt{17}$."),
            lambda: ("Khẳng định nào đúng khi so sánh $\\sqrt{10}$ và 3?", ["$\\sqrt{10} > 3$", "$\\sqrt{10} < 3$", "$\\sqrt{10} = 3$", "$\\sqrt{10} \\le 3$"], 0, "Vì $\\sqrt{10} > \\sqrt{9} = 3$."),
            lambda: ("So sánh $\\sqrt{2}$ và 1,5:", ["$\\sqrt{2} < 1,5$", "$\\sqrt{2} > 1,5$", "$\\sqrt{2} = 1,5$", "Không kết luận được"], 0, "$(\\sqrt{2})^2 = 2 < 1,5^2 = 2,25 \\Rightarrow \\sqrt{2} < 1,5$.")
        ]),
        ("Rút gọn biểu thức căn đồng dạng", "b9", [
            lambda: ("Rút gọn biểu thức $2\\sqrt{3} + 5\\sqrt{3}$ ta được:", ["$7\\sqrt{3}$", "$10\\sqrt{3}$", "$7\\sqrt{6}$", "$10$"], 0, "Cộng căn thức đồng dạng: $(2 + 5)\\sqrt{3} = 7\\sqrt{3}$."),
            lambda: ("Tính giá trị của $4\\sqrt{2} - \\sqrt{2}$:", ["$3\\sqrt{2}$", "$4$", "$3$", "$5\\sqrt{2}$"], 0, "$(4 - 1)\\sqrt{2} = 3\\sqrt{2}$."),
            lambda: ("Kết quả của $3\\sqrt{5} + 2\\sqrt{5} - \\sqrt{5}$ là:", ["$4\\sqrt{5}$", "$5\\sqrt{5}$", "$4\\sqrt{15}$", "$6\\sqrt{5}$"], 0, "$(3 + 2 - 1)\\sqrt{5} = 4\\sqrt{5}$."),
            lambda: ("Rút gọn $6\\sqrt{7} - 4\\sqrt{7}$ thu được:", ["$2\\sqrt{7}$", "$10\\sqrt{7}$", "$2$", "$24\\sqrt{7}$"], 0, "$(6 - 4)\\sqrt{7} = 2\\sqrt{7}$."),
            lambda: ("Tính $5\\sqrt{2} + 3\\sqrt{2} - 6\\sqrt{2}$:", ["$2\\sqrt{2}$", "$8\\sqrt{2}$", "$14\\sqrt{2}$", "$2$"], 0, "$(5 + 3 - 6)\\sqrt{2} = 2\\sqrt{2}$.")
        ])
    ]
    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c3-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    th_configs = [
        ("Rút gọn căn thức có biến", "b7", [
            lambda: ("Rút gọn $\\sqrt{(x - 3)^2}$ với $x < 3$ ta được:", ["$3 - x$", "$x - 3$", "$\\pm (x - 3)$", "$9 - x^2$"], 0, "Vì $x < 3 \\Rightarrow x - 3 < 0$, do đó $|x - 3| = 3 - x$."),
            lambda: ("Rút gọn biểu thức $\\sqrt{(x - 5)^2}$ với $x \\ge 5$:", ["$x - 5$", "$5 - x$", "$x + 5$", "$25 - x^2$"], 0, "Vì $x \\ge 5 \\Rightarrow x - 5 \\ge 0$, do đó $|x - 5| = x - 5$."),
            lambda: ("Với $a < 0$, rút gọn biểu thức $\\sqrt{4a^2}$ ta được:", ["$-2a$", "$2a$", "$\\pm 2a$", "$4a$"], 0, "$\\sqrt{4a^2} = 2|a| = -2a$ vì $a < 0$."),
            lambda: ("Rút gọn $\\sqrt{(2 - x)^2}$ khi $x > 2$:", ["$x - 2$", "$2 - x$", "$\\pm (2 - x)$", "$4 - x^2$"], 0, "Vì $x > 2 \\Rightarrow 2 - x < 0 \\Rightarrow |2 - x| = x - 2$.")
        ]),
        ("Tính giá trị biểu thức chứa căn tích và thương", "b8", [
            lambda: ("Tính giá trị của biểu thức $P = \\sqrt{2} \\cdot \\sqrt{18}$:", ["$6$", "$36$", "$12$", "$9$"], 0, "$P = \\sqrt{2 \\cdot 18} = \\sqrt{36} = 6$."),
            lambda: ("Tính $Q = \\sqrt{3} \\cdot \\sqrt{12}$ thu được:", ["$6$", "$36$", "$3$", "$12$"], 0, "$Q = \\sqrt{3 \\cdot 12} = \\sqrt{36} = 6$."),
            lambda: ("Giá trị của phép tính $\\sqrt{5} \\cdot \\sqrt{20}$ bằng:", ["$10$", "$100$", "$25$", "$5$"], 0, "$\\sqrt{5 \\cdot 20} = \\sqrt{100} = 10$."),
            lambda: ("Tính kết quả của $\\sqrt{8} \\cdot \\sqrt{2}$:", ["$4$", "$16$", "$2$", "$8$"], 0, "$\\sqrt{8 \\cdot 2} = \\sqrt{16} = 4$.")
        ]),
        ("Trục căn thức ở mẫu dạng liên hợp", "b9", [
            lambda: ("Trục căn thức ở mẫu của $\\frac{1}{\\sqrt{3} - 1}$:", ["$\\frac{\\sqrt{3} + 1}{2}$", "$\\sqrt{3} + 1$", "$\\frac{\\sqrt{3} - 1}{2}$", "$\\sqrt{3} - 1$"], 0, "Nhân liên hợp $\\sqrt{3} + 1$: mẫu là $(\\sqrt{3})^2 - 1^2 = 2$."),
            lambda: ("Khử mẫu của $\\frac{2}{\\sqrt{5} - \\sqrt{3}}$ ta được:", ["$\\sqrt{5} + \\sqrt{3}$", "$\\frac{\\sqrt{5} + \\sqrt{3}}{2}$", "$2(\\sqrt{5} + \\sqrt{3})$", "$\\sqrt{5} - \\sqrt{3}$"], 0, "Mẫu là $5 - 3 = 2$, triệt tiêu với tử còn $\\sqrt{5} + \\sqrt{3}$."),
            lambda: ("Trục căn thức ở mẫu của biểu thức $\\frac{1}{\\sqrt{2} + 1}$:", ["$\\sqrt{2} - 1$", "$\\sqrt{2} + 1$", "$\\frac{\\sqrt{2} - 1}{2}$", "$2(\\sqrt{2} - 1)$"], 0, "Mẫu là $(\\sqrt{2})^2 - 1^2 = 1 \\Rightarrow \\sqrt{2} - 1$."),
            lambda: ("Kết quả trục căn thức ở mẫu của $\\frac{4}{\\sqrt{7} - \\sqrt{3}}$ là:", ["$\\sqrt{7} + \\sqrt{3}$", "$2(\\sqrt{7} + \\sqrt{3})$", "$\\frac{\\sqrt{7} + \\sqrt{3}}{4}$", "$4(\\sqrt{7} + \\sqrt{3})$"], 0, "Mẫu là $7 - 3 = 4$, triệt tiêu tử số 4 còn $\\sqrt{7} + \\sqrt{3}$.")
        ]),
        ("Giải phương trình căn thức đơn giản", "b7", [
            lambda: ("Nghiệm của phương trình $\\sqrt{x - 1} = 3$ là:", ["$x = 10$", "$x = 9$", "$x = 8$", "$x = 4$"], 0, "Bình phương hai vế: $x - 1 = 9 \\Leftrightarrow x = 10$."),
            lambda: ("Giải phương trình $\\sqrt{x + 2} = 4$ ta được nghiệm:", ["$x = 14$", "$x = 16$", "$x = 18$", "$x = 6$"], 0, "$x + 2 = 16 \\Leftrightarrow x = 14$."),
            lambda: ("Tìm nghiệm của phương trình $\\sqrt{2x} = 6$:", ["$x = 18$", "$x = 36$", "$x = 12$", "$x = 9$"], 0, "$2x = 36 \\Leftrightarrow x = 18$."),
            lambda: ("Phương trình $\\sqrt{3x - 2} = 5$ có nghiệm là:", ["$x = 9$", "$x = 25$", "$x = 27$", "$x = 8$"], 0, "$3x - 2 = 25 \\Leftrightarrow 3x = 27 \\Leftrightarrow x = 9$.")
        ]),
        ("Rút gọn tổng các căn thức bậc hai", "b9", [
            lambda: ("Rút gọn biểu thức $A = \\sqrt{12} + \\sqrt{27}$:", ["$5\\sqrt{3}$", "$6\\sqrt{3}$", "$3\\sqrt{3}$", "$9\\sqrt{3}$"], 0, "$\\sqrt{12} = 2\\sqrt{3}, \\sqrt{27} = 3\\sqrt{3} \\Rightarrow A = 5\\sqrt{3}$."),
            lambda: ("Tính giá trị của $B = \\sqrt{20} + \\sqrt{45}$:", ["$5\\sqrt{5}$", "$6\\sqrt{5}$", "$4\\sqrt{5}$", "$7\\sqrt{5}$"], 0, "$2\\sqrt{5} + 3\\sqrt{5} = 5\\sqrt{5}$."),
            lambda: ("Kết quả thu gọn của $C = \\sqrt{18} + \\sqrt{50}$ là:", ["$8\\sqrt{2}$", "$7\\sqrt{2}$", "$6\\sqrt{2}$", "$9\\sqrt{2}$"], 0, "$3\\sqrt{2} + 5\\sqrt{2} = 8\\sqrt{2}$."),
            lambda: ("Rút gọn biểu thức $D = \\sqrt{48} - \\sqrt{12}$:", ["$2\\sqrt{3}$", "$4\\sqrt{3}$", "$3\\sqrt{3}$", "$\\sqrt{3}$"], 0, "$4\\sqrt{3} - 2\\sqrt{3} = 2\\sqrt{3}$.")
        ]),
        ("Tính giá trị biểu thức căn bậc ba", "b10", [
            lambda: ("Tính giá trị của $M = \\sqrt[3]{8} + \\sqrt[3]{27}$:", ["$5$", "$6$", "$35$", "$9$"], 0, "$\\sqrt[3]{8} = 2, \\sqrt[3]{27} = 3 \\Rightarrow M = 2 + 3 = 5$."),
            lambda: ("Kết quả của phép tính $\\sqrt[3]{64} - \\sqrt[3]{-8}$ là:", ["$6$", "$2$", "$4$", "$-2$"], 0, "$4 - (-2) = 6$."),
            lambda: ("Tính $N = \\sqrt[3]{125} + \\sqrt[3]{-27}$:", ["$2$", "$8$", "$-2$", "$5$"], 0, "$5 + (-3) = 2$."),
            lambda: ("Giá trị của $\\sqrt[3]{1000} - \\sqrt[3]{216}$ bằng:", ["$4$", "$16$", "$6$", "$10$"], 0, "$10 - 6 = 4$.")
        ]),
        ("So sánh số vô tỉ và số hữu tỉ", "b7", [
            lambda: ("So sánh $2\\sqrt{3}$ và $\\sqrt{13}$:", ["$2\\sqrt{3} < \\sqrt{13}$", "$2\\sqrt{3} > \\sqrt{13}$", "$2\\sqrt{3} = \\sqrt{13}$", "Không so sánh được"], 0, "$2\\sqrt{3} = \\sqrt{12} < \\sqrt{13}$."),
            lambda: ("So sánh $3\\sqrt{2}$ và $\\sqrt{17}$:", ["$3\\sqrt{2} > \\sqrt{17}$", "$3\\sqrt{2} < \\sqrt{17}$", "$3\\sqrt{2} = \\sqrt{17}$", "Không xác định"], 0, "$3\\sqrt{2} = \\sqrt{18} > \\sqrt{17}$."),
            lambda: ("Khẳng định nào đúng khi so sánh số 5 và $2\\sqrt{6}$?", ["$5 > 2\\sqrt{6}$", "$5 < 2\\sqrt{6}$", "$5 = 2\\sqrt{6}$", "$5 \\le 2\\sqrt{6}$"], 0, "$5 = \\sqrt{25} > 2\\sqrt{6} = \\sqrt{24}$."),
            lambda: ("So sánh $4\\sqrt{2}$ và 6:", ["$4\\sqrt{2} < 6$", "$4\\sqrt{2} > 6$", "$4\\sqrt{2} = 6$", "$4\\sqrt{2} \\ge 6$"], 0, "$4\\sqrt{2} = \\sqrt{32} < 6 = \\sqrt{36}$.")
        ]),
        ("Tìm x để phân thức chứa căn ở mẫu xác định", "b7", [
            lambda: ("Biểu thức $\\frac{1}{\\sqrt{x - 2}}$ xác định khi và chỉ khi:", ["$x > 2$", "$x \\ge 2$", "$x < 2$", "$x \\ne 2$"], 0, "Mẫu số nằm trong căn và dưới mẫu nên phải dương nghiêm ngặt: $x > 2$."),
            lambda: ("Tìm điều kiện để $\\frac{3}{\\sqrt{x - 4}}$ có nghĩa:", ["$x > 4$", "$x \\ge 4$", "$x < 4$", "$x \\ne 4$"], 0, "$x - 4 > 0 \\Leftrightarrow x > 4$."),
            lambda: ("Biểu thức $\\frac{x}{\\sqrt{5 - x}}$ có nghĩa khi:", ["$x < 5$", "$x \\le 5$", "$x > 5$", "$x \\ne 5$"], 0, "$5 - x > 0 \\Leftrightarrow x < 5$."),
            lambda: ("Điều kiện xác định của $\\frac{2}{\\sqrt{2x - 6}}$ là:", ["$x > 3$", "$x \\ge 3$", "$x < 3$", "$x > 6$"], 0, "$2x - 6 > 0 \\Leftrightarrow x > 3$.")
        ]),
        ("Khai phương biểu thức dạng bình phương hoàn chỉnh", "b7", [
            lambda: ("Rút gọn biểu thức $\\sqrt{4 - 2\\sqrt{3}}$:", ["$\\sqrt{3} - 1$", "$1 - \\sqrt{3}$", "$\\sqrt{3} + 1$", "$2 - \\sqrt{3}$"], 0, "$4 - 2\\sqrt{3} = (\\sqrt{3} - 1)^2 \\Rightarrow \\sqrt{(\\sqrt{3}-1)^2} = \\sqrt{3} - 1$."),
            lambda: ("Tính giá trị của $\\sqrt{3 - 2\\sqrt{2}}$:", ["$\\sqrt{2} - 1$", "$1 - \\sqrt{2}$", "$\\sqrt{2} + 1$", "$2 - \\sqrt{2}$"], 0, "$3 - 2\\sqrt{2} = (\\sqrt{2} - 1)^2 \\Rightarrow \\sqrt{2} - 1$."),
            lambda: ("Rút gọn biểu thức $\\sqrt{6 - 2\\sqrt{5}}$ thu được:", ["$\\sqrt{5} - 1$", "$1 - \\sqrt{5}$", "$\\sqrt{5} + 1$", "$5 - \\sqrt{5}$"], 0, "$6 - 2\\sqrt{5} = (\\sqrt{5} - 1)^2 \\Rightarrow \\sqrt{5} - 1$."),
            lambda: ("Tính kết quả của $\\sqrt{7 + 2\\sqrt{10}}$:", ["$\\sqrt{5} + \\sqrt{2}$", "$\\sqrt{5} - \\sqrt{2}$", "$\\sqrt{7} + \\sqrt{10}$", "$5 + \\sqrt{2}$"], 0, "$7 + 2\\sqrt{10} = (\\sqrt{5} + \\sqrt{2})^2 \\Rightarrow \\sqrt{5} + \\sqrt{2}$.")
        ]),
        ("Tính giá trị biểu thức liên hợp đối xứng", "b9", [
            lambda: ("Giá trị của biểu thức $C = \\frac{1}{\\sqrt{2} - 1} + \\frac{1}{\\sqrt{2} + 1}$ là:", ["$2\\sqrt{2}$", "$2$", "$\\sqrt{2}$", "$4$"], 0, "Quy đồng: $\\frac{(\\sqrt{2}+1)+(\\sqrt{2}-1)}{2 - 1} = 2\\sqrt{2}$."),
            lambda: ("Tính $D = \\frac{1}{\\sqrt{3} - 1} - \\frac{1}{\\sqrt{3} + 1}$:", ["$1$", "$\\sqrt{3}$", "$2$", "$\\frac{\\sqrt{3}}{2}$"], 0, "$\\frac{(\\sqrt{3}+1)-(\\sqrt{3}-1)}{3 - 1} = \\frac{2}{2} = 1$."),
            lambda: ("Rút gọn biểu thức $E = \\frac{1}{\\sqrt{5} - 2} + \\frac{1}{\\sqrt{5} + 2}$:", ["$2\\sqrt{5}$", "$4$", "$\\sqrt{5}$", "$2$"], 0, "Mẫu là $5 - 4 = 1$. Tử là $(\\sqrt{5}+2)+(\\sqrt{5}-2) = 2\\sqrt{5}$."),
            lambda: ("Giá trị của $\\frac{1}{2 - \\sqrt{3}} - \\frac{1}{2 + \\sqrt{3}}$ bằng:", ["$2\\sqrt{3}$", "$4$", "$2$", "$\\sqrt{3}$"], 0, "Mẫu là $4 - 3 = 1$. Tử là $(2+\\sqrt{3})-(2-\\sqrt{3}) = 2\\sqrt{3}$.")
        ]),
        ("Căn bậc ba của biểu thức tích", "b10", [
            lambda: ("Tính giá trị của $\\sqrt[3]{8 \\cdot 64}$:", ["$8$", "$16$", "$4$", "$32$"], 0, "$\\sqrt[3]{8} \\cdot \\sqrt[3]{64} = 2 \\cdot 4 = 8$."),
            lambda: ("Kết quả của phép tính $\\sqrt[3]{27 \\cdot 8}$ là:", ["$6$", "$18$", "$9$", "$12$"], 0, "$3 \\cdot 2 = 6$."),
            lambda: ("Tính $\\sqrt[3]{125 \\cdot 8}$ thu được:", ["$10$", "$20$", "$50$", "$15$"], 0, "$5 \\cdot 2 = 10$."),
            lambda: ("Giá trị của $\\sqrt[3]{-27 \\cdot 64}$ bằng:", ["$-12$", "$12$", "$-36$", "$36$"], 0, "$-3 \\cdot 4 = -12$.")
        ]),
        ("Tìm x biết căn thức bằng một số", "b7", [
            lambda: ("Tìm x biết $\\sqrt{x} = 5$:", ["$x = 25$", "$x = 10$", "$x = 5$", "$x = \\pm 25$"], 0, "$x = 5^2 = 25$."),
            lambda: ("Nghiệm của phương trình $\\sqrt{x} = 7$ là:", ["$x = 49$", "$x = 14$", "$x = 7$", "$x = 49$ hoặc $x = -49$"], 0, "$x = 7^2 = 49$."),
            lambda: ("Tìm số thực x thoả mãn $\\sqrt{x} = 8$:", ["$x = 64$", "$x = 16$", "$x = 8$", "$x = 32$"], 0, "$x = 8^2 = 64$."),
            lambda: ("Giá trị của x để $\\sqrt{x} = 9$ là:", ["$x = 81$", "$x = 18$", "$x = 9$", "$x = 3$"], 0, "$x = 9^2 = 81$.")
        ])
    ]
    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c3-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    vd_configs = [
        ("Rút gọn biểu thức chứa căn thức nâng cao", "b9", [
            lambda: ("Tính giá trị của biểu thức $P = (\\sqrt{3} + 1)^2 - 2\\sqrt{3}$:", ["$4$", "$3$", "$5$", "$6$"], 0, "Khai triển: $3 + 2\\sqrt{3} + 1 - 2\\sqrt{3} = 4$."),
            lambda: ("Rút gọn biểu thức $Q = (\\sqrt{5} - 1)^2 + 2\\sqrt{5}$ ta được:", ["$6$", "$5$", "$4$", "$7$"], 0, "Khai triển: $5 - 2\\sqrt{5} + 1 + 2\\sqrt{5} = 6$."),
            lambda: ("Giá trị của $(\\sqrt{2} + 3)^2 - 6\\sqrt{2}$ bằng:", ["$11$", "$10$", "$9$", "$12$"], 0, "Khai triển: $2 + 6\\sqrt{2} + 9 - 6\\sqrt{2} = 11$."),
            lambda: ("Tính $R = (\\sqrt{7} - 2)^2 + 4\\sqrt{7}$:", ["$11$", "$9$", "$13$", "$7$"], 0, "Khai triển: $7 - 4\\sqrt{7} + 4 + 4\\sqrt{7} = 11$.")
        ]),
        ("Giải phương trình vô tỉ đưa về bình phương", "b7", [
            lambda: ("Nghiệm của phương trình $\\sqrt{x^2 - 2x + 1} = 3$ là:", ["$x = 4$ hoặc $x = -2$", "$x = 4$", "$x = -2$", "$x = 3$"], 0, "$|x - 1| = 3 \\Rightarrow x - 1 = 3 \\Rightarrow x = 4$ hoặc $x - 1 = -3 \\Rightarrow x = -2$."),
            lambda: ("Giải phương trình $\\sqrt{x^2 - 4x + 4} = 5$ ta được:", ["$x = 7$ hoặc $x = -3$", "$x = 7$", "$x = -3$", "$x = 5$"], 0, "$|x - 2| = 5 \\Rightarrow x = 7$ hoặc $x = -3$."),
            lambda: ("Nghiệm của phương trình $\\sqrt{x^2 + 6x + 9} = 2$ là:", ["$x = -1$ hoặc $x = -5$", "$x = -1$", "$x = -5$", "$x = 2$"], 0, "$|x + 3| = 2 \\Rightarrow x = -1$ hoặc $x = -5$."),
            lambda: ("Phương trình $\\sqrt{x^2 - 8x + 16} = 1$ có nghiệm là:", ["$x = 5$ hoặc $x = 3$", "$x = 5$", "$x = 3$", "$x = 4$"], 0, "$|x - 4| = 1 \\Rightarrow x = 5$ hoặc $x = 3$.")
        ]),
        ("Tính giá trị biểu thức đối xứng căn bậc ba", "b10", [
            lambda: ("Tính giá trị của biểu thức $M = \\sqrt[3]{5\\sqrt{2} + 7} - \\sqrt[3]{5\\sqrt{2} - 7}$:", ["$2$", "$\\sqrt{2}$", "$1$", "$0$"], 0, "$(\\sqrt{2}+1)^3 = 5\\sqrt{2}+7$ và $(\\sqrt{2}-1)^3 = 5\\sqrt{2}-7$. Do đó $M = (\\sqrt{2}+1) - (\\sqrt{2}-1) = 2$."),
            lambda: ("Giá trị của $\\sqrt[3]{20 + 14\\sqrt{2}} + \\sqrt[3]{20 - 14\\sqrt{2}}$ bằng:", ["$4$", "$2$", "$2\\sqrt{2}$", "$8$"], 0, "Bằng $(2 + \\sqrt{2}) + (2 - \\sqrt{2}) = 4$."),
            lambda: ("Tính $K = \\sqrt[3]{2 + \\sqrt{5}} + \\sqrt[3]{2 - \\sqrt{5}}$ có giá trị bằng:", ["$1$", "$2$", "$\\sqrt{5}$", "$0$"], 0, "Lập phương hai vế chứng minh được $K = 1$."),
            lambda: ("Rút gọn biểu thức $\\sqrt[3]{9 + 4\\sqrt{5}} + \\sqrt[3]{9 - 4\\sqrt{5}}$ thu được:", ["$3$", "$1$", "$2$", "$\\sqrt{5}$"], 0, "Giá trị đúng bằng 3.")
        ])
    ]
    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c3-{len(mc)+1:03d}", "chapter": "c3", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    sa_nb = [
        ("Tính căn bậc hai số học", "b7", [
            ("Tính căn bậc hai số học của số 16:", 4, "$\\sqrt{16} = 4$."),
            ("Căn bậc hai số học của 25 bằng bao nhiêu?", 5, "$\\sqrt{25} = 5$."),
            ("Giá trị căn bậc hai số học của số 36 là:", 6, "$\\sqrt{36} = 6$."),
            ("Tính căn bậc hai số học của số 49:", 7, "$\\sqrt{49} = 7$."),
            ("Căn bậc hai số học của 64 bằng:", 8, "$\\sqrt{64} = 8$.")
        ]),
        ("Tính giá trị căn thức bình phương", "b7", [
            ("Tính giá trị của $\\sqrt{7^2}$:", 7, "$\\sqrt{7^2} = 7$."),
            ("Giá trị của $\\sqrt{8^2}$ bằng bao nhiêu?", 8, "$\\sqrt{8^2} = 8$."),
            ("Tính giá trị của biểu thức $\\sqrt{9^2}$:", 9, "$\\sqrt{9^2} = 9$."),
            ("Biểu thức $\\sqrt{10^2}$ có giá trị bằng:", 10, "$\\sqrt{10^2} = 10$."),
            ("Tính kết quả của $\\sqrt{12^2}$:", 12, "$\\sqrt{12^2} = 12$.")
        ]),
        ("Tính căn bậc ba cơ bản", "b10", [
            ("Tính giá trị của $\\sqrt[3]{8}$:", 2, "$\\sqrt[3]{8} = 2$."),
            ("Căn bậc ba của 27 bằng bao nhiêu?", 3, "$\\sqrt[3]{27} = 3$."),
            ("Tính căn bậc ba của số 64:", 4, "$\\sqrt[3]{64} = 4$."),
            ("Giá trị của $\\sqrt[3]{125}$ là:", 5, "$\\sqrt[3]{125} = 5$."),
            ("Căn bậc ba của số 216 bằng:", 6, "$\\sqrt[3]{216} = 6$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Nghiệm x của phương trình căn", "b7", [
            ("Tìm nghiệm x của phương trình $\\sqrt{x} = 4$:", 16, "$x = 4^2 = 16$."),
            ("Phương trình $\\sqrt{x} = 5$ có nghiệm x bằng:", 25, "$x = 5^2 = 25$."),
            ("Giải phương trình $\\sqrt{x} = 6$. Giá trị của x là:", 36, "$x = 6^2 = 36$."),
            ("Tìm x thoả mãn $\\sqrt{x} = 7$:", 49, "$x = 7^2 = 49$.")
        ]),
        ("Tính tích hai căn bậc hai", "b8", [
            ("Tính giá trị của tích $\\sqrt{2} \\cdot \\sqrt{8}$:", 4, "$\\sqrt{16} = 4$."),
            ("Giá trị của $\\sqrt{3} \\cdot \\sqrt{12}$ bằng:", 6, "$\\sqrt{36} = 6$."),
            ("Tính kết quả của $\\sqrt{5} \\cdot \\sqrt{20}$:", 10, "$\\sqrt{100} = 10$."),
            ("Tích $\\sqrt{2} \\cdot \\sqrt{18}$ có giá trị bằng:", 6, "$\\sqrt{36} = 6$.")
        ]),
        ("Giá trị của biểu thức hiệu hai căn", "b9", [
            ("Tính giá trị của $(\\sqrt{5} + 2)(\\sqrt{5} - 2)$:", 1, "$(\\sqrt{5})^2 - 2^2 = 5 - 4 = 1$."),
            ("Kết quả của $(\\sqrt{10} + 3)(\\sqrt{10} - 3)$ bằng:", 1, "$10 - 9 = 1$."),
            ("Tính $(\\sqrt{2} + 1)(\\sqrt{2} - 1)$:", 1, "$2 - 1 = 1$."),
            ("Giá trị của $(\\sqrt{17} + 4)(\\sqrt{17} - 4)$ là:", 1, "$17 - 16 = 1$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Giá trị rút gọn biểu thức lồng nhau", "b7", [
            ("Tính giá trị của biểu thức $\\sqrt{(3 - \\sqrt{2})^2} + \\sqrt{2}$:", 3, "$|3 - \\sqrt{2}| + \\sqrt{2} = 3 - \\sqrt{2} + \\sqrt{2} = 3$."),
            ("Tính $\\sqrt{(4 - \\sqrt{3})^2} + \\sqrt{3}$:", 4, "$4 - \\sqrt{3} + \\sqrt{3} = 4$."),
            ("Giá trị của $\\sqrt{(5 - \\sqrt{7})^2} + \\sqrt{7}$ bằng:", 5, "$5 - \\sqrt{7} + \\sqrt{7} = 5$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c3-{len(sa)+1:03d}", "chapter": "c3", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b7", "sgk_title": "Bài 7. Căn bậc hai và căn thức bậc hai"},
        {"lesson_id": "b8", "sgk_title": "Bài 8. Khai căn bậc hai với phép nhân và phép chia"},
        {"lesson_id": "b9", "sgk_title": "Bài 9. Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai"},
        {"lesson_id": "b10", "sgk_title": "Bài 10. Căn bậc ba và căn thức bậc ba"}
    ]
    save_bank("c3", "Căn bậc hai và căn bậc ba", lessons, mc, sa)
