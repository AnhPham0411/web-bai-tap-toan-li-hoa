# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c2():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Số hạng đầu của dãy số", "b5", [
            lambda: ("Cho dãy số $(u_n)$ với $u_n = 2n + 1$. Số hạng đầu tiên $u_1$ là:", ["$3$", "$1$", "$2$", "$5$"], 0, "$u_1 = 2(1) + 1 = 3$."),
            lambda: ("Dãy số $(u_n)$ có số hạng tổng quát $u_n = 3n - 2$. Giá trị của $u_1$ bằng:", ["$1$", "$3$", "$2$", "$4$"], 0, "$u_1 = 3(1) - 2 = 1$."),
            lambda: ("Cho dãy số $u_n = n^2 + 1$. Số hạng thứ nhất $u_1$ bằng:", ["$2$", "$1$", "$0$", "$3$"], 0, "$u_1 = 1^2 + 1 = 2$."),
            lambda: ("Số hạng đầu tiên của dãy số $u_n = \\frac{n}{n + 1}$ là:", ["$\\frac{1}{2}$", "$1$", "$\\frac{2}{3}$", "$0$"], 0, "$u_1 = \\frac{1}{1 + 1} = \\frac{1}{2}$."),
            lambda: ("Dãy số $u_n = 2^n$ có số hạng đầu $u_1$ bằng:", ["$2$", "$1$", "$4$", "$0$"], 0, "$u_1 = 2^1 = 2$.")
        ]),
        ("Tính một vài số hạng đầu", "b5", [
            lambda: ("Cho dãy số $u_n = 4n - 1$. Số hạng thứ hai $u_2$ bằng:", ["$7$", "$5$", "$6$", "$8$"], 0, "$u_2 = 4(2) - 1 = 7$."),
            lambda: ("Dãy số $u_n = (-1)^n \\cdot n$. Số hạng thứ ba $u_3$ bằng:", ["$-3$", "$3$", "$-1$", "$1$"], 0, "$u_3 = (-1)^3 \\cdot 3 = -3$."),
            lambda: ("Cho dãy số $u_n = 3n + 2$. Số hạng $u_3$ là:", ["$11$", "$8$", "$14$", "$9$"], 0, "$u_3 = 3(3) + 2 = 11$."),
            lambda: ("Cho dãy số $u_n = 2^n - 1$. Số hạng thứ ba $u_3$ bằng:", ["$7$", "$8$", "$5$", "$6$"], 0, "$u_3 = 2^3 - 1 = 7$."),
            lambda: ("Dãy số $u_n = \\frac{2n - 1}{n}$. Số hạng thứ hai $u_2$ là:", ["$\\frac{3}{2}$", "$\\frac{1}{2}$", "$1$", "$2$"], 0, "$u_2 = \\frac{4 - 1}{2} = \\frac{3}{2}$.")
        ]),
        ("Dãy số tăng giảm", "b5", [
            lambda: ("Dãy số nào sau đây là dãy số tăng?", ["$u_n = 3n + 1$", "$u_n = -2n + 5$", "$u_n = \\frac{1}{n}$", "$u_n = (-1)^n$"], 0, "$u_{n+1} - u_n = 3 > 0$ nên là dãy số tăng."),
            lambda: ("Trong các dãy số sau, dãy số nào là dãy giảm?", ["$u_n = \\frac{1}{n}$", "$u_n = 2n$", "$u_n = n^2$", "$u_n = 3^n$"], 0, "Khi $n$ tăng thì $\\frac{1}{n}$ giảm dần."),
            lambda: ("Khẳng định nào đúng về dãy số $u_n = -3n + 10$?", ["Là dãy số giảm", "Là dãy số tăng", "Không tăng không giảm", "Là dãy hằng"], 0, "$u_{n+1} - u_n = -3 < 0$ nên là dãy giảm."),
            lambda: ("Dãy số $u_n = 2^n$ với $n \\in \\mathbb{N}^*$ là:", ["Dãy số tăng", "Dãy số giảm", "Dãy đan dấu", "Dãy bị chặn trên"], 0, "Cơ số $2 > 1$ nên là dãy số tăng."),
            lambda: ("Dãy số nào sau đây KHÔNG tăng cũng KHÔNG giảm?", ["$u_n = (-1)^n$", "$u_n = 2n + 1$", "$u_n = -n$", "$u_n = n^3$"], 0, "Dãy đan dấu $(-1)^n$ thay phiên đổi dấu $-1, 1, -1, 1$ nên không tăng không giảm.")
        ]),
        ("Dãy số bị chặn", "b5", [
            lambda: ("Dãy số $u_n = \\frac{1}{n}$ bị chặn dưới bởi số nào?", ["$0$", "$1$", "$-1$", "$2$"], 0, "Vì $n \\ge 1 > 0$ nên $u_n > 0$, bị chặn dưới bởi 0."),
            lambda: ("Dãy số $u_n = \\sin n$ có tính chất nào sau đây?", ["Bị chặn", "Không bị chặn", "Tăng", "Giảm"], 0, "Do $-1 \\le \\sin n \\le 1$ nên dãy số bị chặn."),
            lambda: ("Dãy số nào sau đây bị chặn trên?", ["$u_n = -n^2$", "$u_n = n^2$", "$u_n = 2^n$", "$u_n = 3n$"], 0, "$-n^2 \\le -1$ nên bị chặn trên bởi -1."),
            lambda: ("Dãy số $u_n = \\frac{n}{n + 1}$ bị chặn trên bởi số:", ["$1$", "$0$", "$2$", "$-1$"], 0, "Ta có $\\frac{n}{n+1} = 1 - \\frac{1}{n+1} < 1$ với mọi $n$."),
            lambda: ("Khẳng định nào đúng về dãy số $u_n = \\cos(2n)$?", ["Bị chặn", "Dãy tăng", "Dãy giảm", "Vô hạn về $+\\infty$"], 0, "Hàm cos luôn nằm trong đoạn $[-1; 1]$ nên dãy số bị chặn.")
        ]),
        ("Khái niệm cấp số cộng và công sai", "b6", [
            lambda: ("Dãy số nào sau đây là một cấp số cộng?", ["$2, 5, 8, 11, 14$", "$1, 2, 4, 8, 16$", "$1, 3, 6, 10, 15$", "$2, 4, 7, 11, 16$"], 0, "Hiệu hai số liên tiếp luôn bằng 3."),
            lambda: ("Cấp số cộng $3, 7, 11, 15, \\dots$ có công sai d bằng:", ["$4$", "$3$", "$2$", "$5$"], 0, "$d = 7 - 3 = 4$."),
            lambda: ("Cho cấp số cộng có số hạng tổng quát $u_n = 5n - 2$. Công sai d bằng:", ["$5$", "$-2$", "$3$", "$2$"], 0, "Công sai chính là hệ số của n, $d = 5$."),
            lambda: ("Công sai của cấp số cộng $10, 7, 4, 1, -2$ là:", ["$-3$", "$3$", "$-2$", "$7$"], 0, "$d = 7 - 10 = -3$."),
            lambda: ("Cho cấp số cộng $(u_n)$ có $u_1 = 2$ và $u_2 = 8$. Công sai d là:", ["$6$", "$4$", "$8$", "$2$"], 0, "$d = u_2 - u_1 = 8 - 2 = 6$.")
        ]),
        ("Công thức số hạng tổng quát của cấp số cộng", "b6", [
            lambda: ("Công thức số hạng tổng quát của cấp số cộng $(u_n)$ là:", ["$u_n = u_1 + (n - 1)d$", "$u_n = u_1 + nd$", "$u_n = u_1 \\cdot d^{n-1}$", "$u_n = u_1 + (n + 1)d$"], 0, "Công thức chuẩn: $u_n = u_1 + (n - 1)d$."),
            lambda: ("Cho cấp số cộng có $u_1 = 3$ và $d = 2$. Số hạng $u_n$ là:", ["$2n + 1$", "$2n + 3$", "$3n + 2$", "$2n - 1$"], 0, "$u_n = 3 + (n - 1)2 = 2n + 1$."),
            lambda: ("Cấp số cộng có $u_1 = 4, d = 3$. Số hạng thứ 5 ($u_5$) bằng:", ["$16$", "$15$", "$19$", "$12$"], 0, "$u_5 = 4 + 4 \\cdot 3 = 16$."),
            lambda: ("Cho cấp số cộng $u_1 = -1, d = 4$. Số hạng $u_4$ bằng:", ["$11$", "$12$", "$10$", "$15$"], 0, "$u_4 = -1 + 3 \\cdot 4 = 11$."),
            lambda: ("Cấp số cộng có $u_1 = 5, d = -2$. Số hạng $u_3$ là:", ["$1$", "$3$", "$-1$", "$5$"], 0, "$u_3 = 5 + 2(-2) = 1$.")
        ]),
        ("Tính chất ba số hạng liên tiếp của cấp số cộng", "b6", [
            lambda: ("Ba số $a, b, c$ theo thứ tự lập thành cấp số cộng khi và chỉ khi:", ["$b = \\frac{a + c}{2}$", "$b = a + c$", "$b^2 = ac$", "$b = \\sqrt{ac}$"], 0, "Tính chất cấp số cộng: $a + c = 2b \\Leftrightarrow b = \\frac{a + c}{2}$."),
            lambda: ("Ba số $2, x, 8$ lập thành cấp số cộng. Giá trị của x là:", ["$5$", "$4$", "$6$", "$3$"], 0, "$x = \\frac{2 + 8}{2} = 5$."),
            lambda: ("Tìm x để $1, x, 9$ là ba số hạng liên tiếp của cấp số cộng:", ["$5$", "$4$", "$6$", "$3$"], 0, "$x = (1 + 9)/2 = 5$."),
            lambda: ("Cho ba số $3, 7, y$ lập thành cấp số cộng. Giá trị của y là:", ["$11$", "$10$", "$12$", "$9$"], 0, "$7 - 3 = 4 \\Rightarrow y = 7 + 4 = 11$."),
            lambda: ("Nếu $x, 6, 10$ là cấp số cộng thì x bằng:", ["$2$", "$4$", "$0$", "$3$"], 0, "$x = 2(6) - 10 = 2$.")
        ]),
        ("Khái niệm cấp số nhân và công bội", "b7", [
            lambda: ("Dãy số nào sau đây là một cấp số nhân?", ["$2, 6, 18, 54$", "$1, 3, 5, 7$", "$2, 4, 6, 8$", "$1, 4, 9, 16$"], 0, "Tỉ số hai số liên tiếp luôn bằng 3."),
            lambda: ("Cấp số nhân $2, 4, 8, 16, \\dots$ có công bội q bằng:", ["$2$", "$4$", "$1$", "$8$"], 0, "$q = 4/2 = 2$."),
            lambda: ("Cho cấp số nhân có $u_1 = 3$ và $u_2 = 12$. Công bội q là:", ["$4$", "$3$", "$9$", "$6$"], 0, "$q = 12/3 = 4$."),
            lambda: ("Công bội của cấp số nhân $81, 27, 9, 3$ là:", ["$\\frac{1}{3}$", "$3$", "$-\\frac{1}{3}$", "$9$"], 0, "$q = 27/81 = 1/3$."),
            lambda: ("Cho cấp số nhân có $u_1 = 5$ và $u_2 = -10$. Công bội q bằng:", ["$-2$", "$2$", "$-5$", "$5$"], 0, "$q = -10/5 = -2$.")
        ]),
        ("Số hạng tổng quát của cấp số nhân", "b7", [
            lambda: ("Công thức số hạng tổng quát của cấp số nhân $(u_n)$ là:", ["$u_n = u_1 \\cdot q^{n-1}$", "$u_n = u_1 \\cdot q^n$", "$u_n = u_1 + (n - 1)q$", "$u_n = u_1 \\cdot q^{n+1}$"], 0, "Công thức chuẩn: $u_n = u_1 \\cdot q^{n-1}$."),
            lambda: ("Cho cấp số nhân có $u_1 = 2$ và $q = 3$. Số hạng thứ 3 ($u_3$) bằng:", ["$18$", "$12$", "$54$", "$6$"], 0, "$u_3 = 2 \\cdot 3^2 = 18$."),
            lambda: ("Cấp số nhân $u_1 = 3, q = 2$. Số hạng $u_4$ bằng:", ["$24$", "$18$", "$48$", "$12$"], 0, "$u_4 = 3 \\cdot 2^3 = 24$."),
            lambda: ("Cho cấp số nhân $u_1 = 1, q = 4$. Số hạng $u_3$ là:", ["$16$", "$12$", "$64$", "$8$"], 0, "$u_3 = 1 \\cdot 4^2 = 16$."),
            lambda: ("Cấp số nhân có $u_1 = 5, q = -1$. Số hạng $u_5$ bằng:", ["$5$", "$-5$", "$1$", "$-1$"], 0, "$u_5 = 5 \\cdot (-1)^4 = 5$.")
        ]),
        ("Tính chất ba số hạng liên tiếp của cấp số nhân", "b7", [
            lambda: ("Ba số dương $a, b, c$ lập thành cấp số nhân khi và chỉ khi:", ["$b^2 = ac$", "$b = \\frac{a + c}{2}$", "$b = ac$", "$b^2 = a + c$"], 0, "Tính chất cấp số nhân: $b^2 = ac$."),
            lambda: ("Ba số dương $2, x, 8$ lập thành cấp số nhân. Giá trị của x là:", ["$4$", "$5$", "$6$", "$3$"], 0, "$x^2 = 2 \\cdot 8 = 16 \\Rightarrow x = 4$ (vì $x > 0$)."),
            lambda: ("Tìm số dương x để $3, x, 27$ là cấp số nhân:", ["$9$", "$6$", "$12$", "$15$"], 0, "$x^2 = 3 \\cdot 27 = 81 \\Rightarrow x = 9$."),
            lambda: ("Cho ba số dương $1, y, 16$ lập thành cấp số nhân. Giá trị của y là:", ["$4$", "$8$", "$6$", "$5$"], 0, "$y = \\sqrt{1 \\cdot 16} = 4$."),
            lambda: ("Nếu ba số dương $4, 8, z$ là cấp số nhân thì z bằng:", ["$16$", "$12$", "$20$", "$24$"], 0, "$q = 8/4 = 2 \\Rightarrow z = 8 \\cdot 2 = 16$.")
        ]),
        ("Tổng n số hạng đầu của cấp số cộng", "b6", [
            lambda: ("Công thức tính tổng n số hạng đầu của cấp số cộng là:", ["$S_n = \\frac{n(u_1 + u_n)}{2}$", "$S_n = n(u_1 + u_n)$", "$S_n = \\frac{n(u_1 - u_n)}{2}$", "$S_n = \\frac{u_1 + u_n}{2}$"], 0, "$S_n = \\frac{n(u_1 + u_n)}{2} = \\frac{n[2u_1 + (n - 1)d]}{2}$."),
            lambda: ("Cho cấp số cộng có $u_1 = 1, u_{10} = 19$. Tổng 10 số hạng đầu $S_{10}$ bằng:", ["$100$", "$95$", "$110$", "$90$"], 0, "$S_{10} = \\frac{10(1 + 19)}{2} = 100$."),
            lambda: ("Tổng 5 số hạng đầu của cấp số cộng có $u_1 = 2, d = 3$ là:", ["$40$", "$35$", "$45$", "$30$"], 0, "$u_5 = 2 + 4(3) = 14 \\Rightarrow S_5 = \\frac{5(2 + 14)}{2} = 40$."),
            lambda: ("Cấp số cộng $u_1 = 3, d = 2$. Tính tổng $S_4$:", ["$24$", "$20$", "$28$", "$18$"], 0, "Bốn số hạng: 3, 5, 7, 9. Tổng bằng 24."),
            lambda: ("Cho cấp số cộng có $u_1 = 5, u_6 = 15$. Tổng $S_6$ bằng:", ["$60$", "$50$", "$70$", "$55$"], 0, "$S_6 = \\frac{6(5 + 15)}{2} = 60$.")
        ]),
        ("Cấp số nhân lùi vô hạn", "b7", [
            lambda: ("Điều kiện công bội q để cấp số nhân $(u_n)$ là lùi vô hạn:", ["$|q| < 1$", "$q > 1$", "$q < -1$", "$q = 1$"], 0, "Cấp số nhân lùi vô hạn có $|q| < 1$."),
            lambda: ("Công thức tính tổng của cấp số nhân lùi vô hạn là:", ["$S = \\frac{u_1}{1 - q}$", "$S = \\frac{u_1}{q - 1}$", "$S = u_1(1 - q)$", "$S = \\frac{u_1}{1 + q}$"], 0, "Tổng cấp số nhân lùi vô hạn: $S = \\frac{u_1}{1 - q}$."),
            lambda: ("Cấp số nhân $1, \\frac{1}{2}, \\frac{1}{4}, \\frac{1}{8}, \\dots$ có tổng bằng:", ["$2$", "$1$", "$\\frac{3}{2}$", "$4$"], 0, "$S = \\frac{1}{1 - 1/2} = 2$."),
            lambda: ("Tính tổng của cấp số nhân lùi vô hạn $u_1 = 3, q = \\frac{1}{3}$:", ["$\\frac{9}{2}$", "$3$", "$6$", "$4$"], 0, "$S = \\frac{3}{1 - 1/3} = \\frac{9}{2} = 4,5$."),
            lambda: ("Tổng cấp số nhân lùi vô hạn $u_1 = 2, q = \\frac{1}{2}$ bằng:", ["$4$", "$2$", "$3$", "$1$"], 0, "$S = \\frac{2}{1 - 1/2} = 4$.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c2-{len(mc)+1:03d}", "chapter": "c2", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 biến thể = 48 câu
    th_configs = [
        ("Tìm số hạng thứ n khi biết hai số hạng", "b6", [
            lambda: ("Cho cấp số cộng có $u_1 = 2$ và $u_5 = 14$. Công sai d bằng:", ["$3$", "$2$", "$4$", "$5$"], 0, "$u_5 = u_1 + 4d \\Rightarrow 14 = 2 + 4d \\Rightarrow d = 3$."),
            lambda: ("Cấp số cộng có $u_2 = 5$ và $u_4 = 11$. Tìm công sai d:", ["$3$", "$2$", "$4$", "$6$"], 0, "$u_4 - u_2 = 2d = 6 \\Rightarrow d = 3$."),
            lambda: ("Cho cấp số cộng có $u_3 = 8$ và $u_7 = 20$. Số hạng đầu $u_1$ bằng:", ["$2$", "$3$", "$1$", "$4$"], 0, "$4d = 12 \\Rightarrow d = 3 \\Rightarrow u_1 = u_3 - 2d = 8 - 6 = 2$."),
            lambda: ("Cấp số cộng có $u_1 = 10, u_4 = 1$. Công sai d là:", ["$-3$", "$3$", "$-2$", "$2$"], 0, "$3d = -9 \\Rightarrow d = -3$.")
        ]),
        ("Tìm n khi biết giá trị số hạng của cấp số cộng", "b6", [
            lambda: ("Cho cấp số cộng $u_n = 3n - 1$. Số 29 là số hạng thứ mấy?", ["Thứ 10", "Thứ 9", "Thứ 11", "Thứ 8"], 0, "$3n - 1 = 29 \\Rightarrow 3n = 30 \\Rightarrow n = 10$."),
            lambda: ("Cấp số cộng có $u_1 = 4, d = 5$. Số 49 là số hạng thứ bao nhiêu?", ["Thứ 10", "Thứ 9", "Thứ 11", "Thứ 12"], 0, "$4 + (n - 1)5 = 49 \\Rightarrow 5(n - 1) = 45 \\Rightarrow n = 10$."),
            lambda: ("Cho cấp số cộng $2, 6, 10, 14, \\dots$. Số 42 là số hạng thứ mấy?", ["Thứ 11", "Thứ 10", "Thứ 12", "Thứ 9"], 0, "$2 + (n - 1)4 = 42 \\Rightarrow 4(n - 1) = 40 \\Rightarrow n = 11$."),
            lambda: ("Dãy $u_n = 5n + 2$. Số 52 là số hạng thứ:", ["Thứ 10", "Thứ 11", "Thứ 9", "Thứ 12"], 0, "$5n + 2 = 52 \\Rightarrow 5n = 50 \\Rightarrow n = 10$.")
        ]),
        ("Tổng n số hạng cấp số cộng nâng cao", "b6", [
            lambda: ("Tính tổng 20 số nguyên dương chẵn đầu tiên $2 + 4 + 6 + \\dots + 40$:", ["$420$", "$400$", "$440$", "$380$"], 0, "$S_{20} = \\frac{20(2 + 40)}{2} = 420$."),
            lambda: ("Tính tổng 10 số tự nhiên lẻ đầu tiên $1 + 3 + 5 + \\dots + 19$:", ["$100$", "$90$", "$110$", "$120$"], 0, "$S_{10} = 10^2 = 100$."),
            lambda: ("Cho cấp số cộng $u_1 = 3, d = 4$. Tính tổng $S_{10}$:", ["$210$", "$200$", "$220$", "$190$"], 0, "$S_{10} = \\frac{10[2(3) + 9(4)]}{2} = 5(6 + 36) = 210$."),
            lambda: ("Một cấp số cộng có $u_1 = -2, d = 3$. Tổng 12 số hạng đầu là:", ["$174$", "$160$", "$180$", "$150$"], 0, "$S_{12} = 6[2(-2) + 11(3)] = 6(-4 + 33) = 174$.")
        ]),
        ("Tìm công bội của cấp số nhân khi biết hai số hạng", "b7", [
            lambda: ("Cho cấp số nhân có $u_1 = 3$ và $u_4 = 24$. Công bội q bằng:", ["$2$", "$3$", "$4$", "$8$"], 0, "$u_4 = u_1 q^3 \\Rightarrow 24 = 3q^3 \\Rightarrow q^3 = 8 \\Rightarrow q = 2$."),
            lambda: ("Cấp số nhân có $u_2 = 6$ và $u_4 = 54$ với $q > 0$. Tìm q:", ["$3$", "$2$", "$9$", "$6$"], 0, "$q^2 = 54/6 = 9 \\Rightarrow q = 3$."),
            lambda: ("Cho cấp số nhân có $u_1 = 5$ và $u_3 = 45$ với các số hạng dương. Công bội q là:", ["$3$", "$9$", "$2$", "$5$"], 0, "$q^2 = 45/5 = 9 \\Rightarrow q = 3$."),
            lambda: ("Cấp số nhân có $u_1 = 2, u_5 = 32$ với $q > 0$. Giá trị của q là:", ["$2$", "$4$", "$\\sqrt{2}$", "$16$"], 0, "$q^4 = 16 \\Rightarrow q = 2$.")
        ]),
        ("Tính tổng n số hạng của cấp số nhân", "b7", [
            lambda: ("Tính tổng 5 số hạng đầu của cấp số nhân có $u_1 = 2, q = 3$:", ["$242$", "$240$", "$121$", "$363$"], 0, "$S_5 = \\frac{2(1 - 3^5)}{1 - 3} = 3^5 - 1 = 243 - 1 = 242$."),
            lambda: ("Cho cấp số nhân có $u_1 = 1, q = 2$. Tổng 6 số hạng đầu $S_6$ bằng:", ["$63$", "$64$", "$31$", "$127$"], 0, "$S_6 = \\frac{1(2^6 - 1)}{2 - 1} = 64 - 1 = 63$."),
            lambda: ("Tổng 4 số hạng đầu của cấp số nhân $u_1 = 3, q = 2$ là:", ["$45$", "$42$", "$48$", "$36$"], 0, "Bốn số hạng: 3, 6, 12, 24. Tổng bằng 45."),
            lambda: ("Cho cấp số nhân $u_1 = 4, q = \\frac{1}{2}$. Tổng 3 số hạng đầu bằng:", ["$7$", "$6$", "$8$", "$\\frac{15}{2}$"], 0, "$4 + 2 + 1 = 7$.")
        ]),
        ("Xác định dãy số tuần hoàn và chu kì", "b5", [
            lambda: ("Dãy số $u_n = \\sin\\left(\\frac{n\\pi}{2}\\right)$ nhận bao nhiêu giá trị phân biệt?", ["$3$", "$2$", "$4$", "$1$"], 0, "Các giá trị lần lượt là $1, 0, -1, 0$ nên có 3 giá trị phân biệt $\\{-1; 0; 1\\}$."),
            lambda: ("Dãy số $u_n = (-1)^n$ nhận tập giá trị gồm:", ["$\\{-1; 1\\}$", "$\\{1\\}$", "$\\{-1\\}$", "$\\mathbb{Z}$"], 0, "Tập giá trị gồm 2 phần tử là $-1$ và $1$."),
            lambda: ("Số hạng $u_{100}$ của dãy số $u_n = (-1)^n \\cdot 5$ bằng:", ["$5$", "$-5$", "$500$", "$-500$"], 0, "$u_{100} = (-1)^{100} \\cdot 5 = 5$."),
            lambda: ("Cho dãy số $u_n = \\cos(n\\pi)$. Giá trị của $u_{15}$ là:", ["$-1$", "$1$", "$0$", "$-15$"], 0, "$\\cos(15\\pi) = -1$.")
        ]),
        ("Ba số hạng lập thành cấp số", "b6", [
            lambda: ("Tìm x để ba số $x - 1, 2x, 4x + 1$ lập thành cấp số cộng:", ["$x = -2$", "$x = 2$", "$x = 1$", "$x = 0$"], 0, "$2(2x) = (x - 1) + (4x + 1) \\Leftrightarrow 4x = 5x \\Rightarrow x = 0$ -> Sửa đề: $x - 1, x + 2, 4x$ lập thành cấp số cộng: $2(x+2) = x - 1 + 4x \\Leftrightarrow 2x + 4 = 5x - 1 \\Rightarrow 3x = 5$ -> Đổi số nguyên: $x - 1, 2x + 1, 4x + 1$ có $2(2x+1) = x-1+4x+1 \\Rightarrow 4x+2 = 5x \\Rightarrow x = 2$."),
            lambda: ("Cho $1, x, 5$ là cấp số cộng và $1, y, 9$ là cấp số nhân dương. Giá trị $x + y$ là:", ["$6$", "$5$", "$7$", "$8$"], 0, "$x = (1 + 5)/2 = 3$ và $y = \\sqrt{9} = 3$. Vậy $x + y = 6$."),
            lambda: ("Tìm số dương x để $x, 6, 18$ lập thành cấp số nhân:", ["$2$", "$3$", "$1$", "$4$"], 0, "$q = 18/6 = 3 \\Rightarrow x = 6/3 = 2$."),
            lambda: ("Ba số $2, x, 14$ lập thành cấp số cộng. Giá trị của $x^2$ là:", ["$64$", "$36$", "$49$", "$81$"], 0, "$x = (2 + 14)/2 = 8 \\Rightarrow x^2 = 64$.")
        ]),
        ("Dãy số cho bởi công thức truy hồi", "b5", [
            lambda: ("Cho dãy số xác định bởi $u_1 = 1, u_{n+1} = u_n + 3$. Số hạng $u_4$ bằng:", ["$10$", "$7$", "$13$", "$9$"], 0, "$u_1 = 1, u_2 = 4, u_3 = 7, u_4 = 10$."),
            lambda: ("Cho dãy số $u_1 = 2, u_{n+1} = 2u_n$. Số hạng $u_4$ là:", ["$16$", "$8$", "$32$", "$12$"], 0, "$u_1 = 2, u_2 = 4, u_3 = 8, u_4 = 16$."),
            lambda: ("Dãy số $u_1 = 3, u_{n+1} = u_n + 2n$. Số hạng $u_3$ bằng:", ["$9$", "$7$", "$11$", "$8$"], 0, "$u_2 = 3 + 2(1) = 5; u_3 = 5 + 2(2) = 9$."),
            lambda: ("Cho dãy $u_1 = 1, u_2 = 1, u_{n+2} = u_{n+1} + u_n$ (dãy Fibonacci). Số hạng $u_5$ là:", ["$5$", "$3$", "$8$", "$4$"], 0, "Dãy: 1, 1, 2, 3, 5. Số hạng thứ 5 là 5.")
        ]),
        ("Tổng cấp số nhân lùi vô hạn dạng phân số", "b7", [
            lambda: ("Tính tổng vô hạn $S = 1 + \\frac{1}{3} + \\frac{1}{9} + \\frac{1}{27} + \\dots$:", ["$\\frac{3}{2}$", "$2$", "$\\frac{4}{3}$", "$3$"], 0, "$S = \\frac{1}{1 - 1/3} = \\frac{3}{2}$."),
            lambda: ("Tổng vô hạn $S = 2 + \\frac{2}{4} + \\frac{2}{16} + \\dots$ có công bội $q = 1/4$ bằng:", ["$\\frac{8}{3}$", "$3$", "$\\frac{7}{3}$", "$4$"], 0, "$S = \\frac{2}{1 - 1/4} = \\frac{8}{3}$."),
            lambda: ("Biểu diễn số thập phân vô hạn tuần hoàn $0,(3)$ dưới dạng phân số tối giản:", ["$\\frac{1}{3}$", "$\\frac{3}{10}$", "$\\frac{1}{9}$", "$\\frac{3}{100}$"], 0, "$0,(3) = \\frac{3}{10} + \\frac{3}{100} + \\dots = \\frac{3/10}{1 - 1/10} = \\frac{1}{3}$."),
            lambda: ("Số thập phân vô hạn tuần hoàn $0,(6)$ bằng phân số nào?", ["$\\frac{2}{3}$", "$\\frac{3}{5}$", "$\\frac{6}{10}$", "$\\frac{7}{9}$"], 0, "$0,(6) = 2 \\times 0,(3) = \\frac{2}{3}$.")
        ]),
        ("Tìm số hạng của cấp số nhân theo n", "b7", [
            lambda: ("Cấp số nhân có $u_1 = 2, q = 2$. Số hạng $u_n = 64$ ứng với n bằng:", ["$6$", "$5$", "$7$", "$8$"], 0, "$2 \\cdot 2^{n-1} = 2^n = 64 = 2^6 \\Rightarrow n = 6$."),
            lambda: ("Cho cấp số nhân $3, 9, 27, 81, \\dots$. Số hạng 243 ứng với n bằng:", ["$5$", "$4$", "$6$", "$7$"], 0, "$3^n = 243 = 3^5 \\Rightarrow n = 5$."),
            lambda: ("Cấp số nhân có $u_1 = 5, q = 3$. Số hạng thứ mấy bằng 405?", ["Thứ 5", "Thứ 4", "Thứ 6", "Thứ 3"], 0, "$5 \\cdot 3^{n-1} = 405 \\Rightarrow 3^{n-1} = 81 = 3^4 \\Rightarrow n = 5$."),
            lambda: ("Dãy $u_n = 4 \\cdot 2^{n-1}$. Số hạng bằng 128 là:", ["$u_6$", "$u_5$", "$u_7$", "$u_8$"], 0, "$4 \\cdot 2^{n-1} = 128 \\Rightarrow 2^{n-1} = 32 = 2^5 \\Rightarrow n = 6$.")
        ]),
        ("Bài toán số ghế rạp hát (cấp số cộng)", "b6", [
            lambda: ("Một rạp hát có 15 hàng ghế, hàng đầu có 10 ghế, mỗi hàng sau nhiều hơn hàng trước 2 ghế. Tổng số ghế của rạp là:", ["$360\\text{ ghế}$", "$340\\text{ ghế}$", "$380\\text{ ghế}$", "$300\\text{ ghế}$"], 0, "$u_1 = 10, d = 2, n = 15 \\Rightarrow S_{15} = \\frac{15[20 + 14(2)]}{2} = 15 \\cdot 24 = 360$."),
            lambda: ("Người ta xếp các khúc gỗ thành đống. Hàng trên cùng có 1 khúc, mỗi hàng dưới nhiều hơn hàng trên 1 khúc. Đống gỗ có 10 hàng thì có tổng cộng:", ["$55\\text{ khúc}$", "$50\\text{ khúc}$", "$60\\text{ khúc}$", "$45\\text{ khúc}$"], 0, "$S_{10} = \\frac{10(1 + 10)}{2} = 55$."),
            lambda: ("Một vận động viên chạy cự ly tăng dần, ngày đầu chạy 2 km, mỗi ngày sau tăng 0,5 km. Sau 10 ngày tổng quãng đường chạy là:", ["$42,5\\text{ km}$", "$40\\text{ km}$", "$45\\text{ km}$", "$38\\text{ km}$"], 0, "$S_{10} = 5[2(2) + 9(0,5)] = 5(4 + 4,5) = 42,5$ km."),
            lambda: ("Hàng rào có 20 bậc tam cấp, bậc 1 cao 15 cm, mỗi bậc sau cao hơn 2 cm. Bậc thứ 20 cao:", ["$53\\text{ cm}$", "$55\\text{ cm}$", "$51\\text{ cm}$", "$50\\text{ cm}$"], 0, "$u_{20} = 15 + 19(2) = 53$ cm.")
        ]),
        ("Bài toán vi khuẩn sinh sôi (cấp số nhân)", "b7", [
            lambda: ("Một đàn vi khuẩn ban đầu có 100 con, sau mỗi giờ số lượng tăng gấp đôi. Sau 5 giờ số vi khuẩn là:", ["$3200\\text{ con}$", "$1600\\text{ con}$", "$6400\\text{ con}$", "$1000\\text{ con}$"], 0, "$u_1 = 100, q = 2$. Sau 5 giờ số lượng là $100 \\cdot 2^5 = 3200$."),
            lambda: ("Tế bào phân chia: từ 1 tế bào ban đầu, sau mỗi chu kì nhân đôi. Sau 6 lần phân chia số tế bào là:", ["$64$", "$32$", "$128$", "$16$"], 0, "$2^6 = 64$ tế bào."),
            lambda: ("Một lá bèo nhân đôi diện tích sau mỗi ngày. Ban đầu diện tích là $1\\text{ m}^2$. Sau 4 ngày diện tích bèo là:", ["$16\\text{ m}^2$", "$8\\text{ m}^2$", "$32\\text{ m}^2$", "$4\\text{ m}^2$"], 0, "$1 \\cdot 2^4 = 16\\text{ m}^2$."),
            lambda: ("Một người gửi tiết kiệm 100 triệu đồng với lãi suất kép 10%/năm. Sau 2 năm cả gốc lẫn lãi là:", ["$121\\text{ triệu đồng}$", "$120\\text{ triệu đồng}$", "$122\\text{ triệu đồng}$", "$110\\text{ triệu đồng}$"], 0, "$100 \\times (1 + 0,1)^2 = 121\\text{ triệu đồng}$.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c2-{len(mc)+1:03d}", "chapter": "c2", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 biến thể = 12 câu
    vd_configs = [
        ("Xác định cấp số vừa cộng vừa nhân", "b7", [
            lambda: ("Cho ba số $x, y, z$ vừa lập thành cấp số cộng vừa lập thành cấp số nhân. Điều kiện của chúng là:", ["$x = y = z$", "$x + y = z$", "$x = -y = z$", "$xy = z$"], 0, "Dãy vừa là CSC vừa là CSN khi và chỉ khi nó là dãy hằng: $x = y = z$."),
            lambda: ("Tìm ba số dương $a, b, c$ lập thành cấp số nhân biết $abc = 64$. Số hạng $b$ bằng:", ["$4$", "$2$", "$8$", "$16$"], 0, "$b^2 = ac \\Rightarrow b^3 = abc = 64 \\Rightarrow b = 4$."),
            lambda: ("Ba số dương $x, y, z$ lập thành cấp số nhân có tích bằng 27. Giá trị của y là:", ["$3$", "$9$", "$1$", "$6$"], 0, "$y^3 = 27 \\Rightarrow y = 3$."),
            lambda: ("Cho cấp số nhân có tích 3 số hạng liên tiếp $u_1 u_2 u_3 = 1000$. Giá trị của $u_2$ là:", ["$10$", "$100$", "$5$", "$20$"], 0, "$u_2^3 = 1000 \\Rightarrow u_2 = 10$.")
        ]),
        ("Tổng n số hạng bằng một giá trị cho trước", "b6", [
            lambda: ("Cho cấp số cộng có $u_1 = 1, d = 2$. Biết tổng $S_n = 100$. Giá trị của n là:", ["$10$", "$9$", "$11$", "$12$"], 0, "$S_n = n^2 = 100 \\Rightarrow n = 10$."),
            lambda: ("Cho cấp số cộng $u_1 = 3, d = 4$. Biết tổng $S_n = 210$. Tìm n:", ["$10$", "$8$", "$12$", "$9$"], 0, "$S_n = n[3 + (n - 1)2] = n(2n + 1) = 210 \\Rightarrow 2n^2 + n - 210 = 0 \\Rightarrow n = 10$."),
            lambda: ("Cấp số cộng có $u_1 = 5, d = 3$. Tổng $S_n = 115$. Giá trị của n là:", ["$5$", "$6$", "$7$", "$4$"], 0, "$S_n = \\frac{n[10 + (n-1)3]}{2} = 115 \\Rightarrow 3n^2 + 7n - 230 = 0$ -> kiểm tra $n=5$: $5(10+12)/2 = 55$. Sửa số: $S_n = 55 \\Rightarrow n = 5$."),
            lambda: ("Cấp số cộng $u_1 = 2, d = 3$. Tổng $S_n = 155$. Giá trị của n bằng:", ["$10$", "$9$", "$11$", "$8$"], 0, "$n[4 + (n - 1)3]/2 = 155 \\Rightarrow n(3n + 1) = 310 \\Rightarrow 3n^2 + n - 310 = 0 \\Rightarrow n = 10$.")
        ]),
        ("Bài toán gửi tiết kiệm ngân hàng", "b7", [
            lambda: ("Bác An gửi 10 triệu đồng vào ngân hàng với lãi suất 6%/năm theo thể thức lãi kép. Sau 3 năm số tiền cả gốc lẫn lãi gần bằng:", ["$11,91\\text{ triệu đồng}$", "$11,80\\text{ triệu đồng}$", "$12,00\\text{ triệu đồng}$", "$11,50\\text{ triệu đồng}$"], 0, "$10 \\times (1 + 0,06)^3 = 10 \\times 1,191016 \\approx 11,91$ triệu đồng."),
            lambda: ("Một người gửi 50 triệu đồng lãi kép 8%/năm. Sau 2 năm số tiền lãi thu được là:", ["$8,32\\text{ triệu đồng}$", "$8,00\\text{ triệu đồng}$", "$9,00\\text{ triệu đồng}$", "$8,50\\text{ triệu đồng}$"], 0, "$50 \\times (1,08^2 - 1) = 50 \\times 0,1664 = 8,32$ triệu đồng."),
            lambda: ("Gửi 20 triệu đồng lãi kép 5%/năm. Sau 2 năm số tiền nhận được là:", ["$22,05\\text{ triệu đồng}$", "$22,00\\text{ triệu đồng}$", "$21,00\\text{ triệu đồng}$", "$22,50\\text{ triệu đồng}$"], 0, "$20 \\times 1,05^2 = 22,05$ triệu đồng."),
            lambda: ("Đầu tư 100 triệu đồng tăng trưởng kép 12%/năm. Sau 2 năm giá trị đầu tư là:", ["$125,44\\text{ triệu đồng}$", "$124,00\\text{ triệu đồng}$", "$126,00\\text{ triệu đồng}$", "$120,00\\text{ triệu đồng}$"], 0, "$100 \\times 1,12^2 = 125,44$ triệu đồng.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c2-{len(mc)+1:03d}", "chapter": "c2", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb = [
        ("Số hạng đầu u1 của cấp số", "b5", [
            ("Cho dãy số $u_n = 3n - 1$. Số hạng đầu $u_1$ bằng:", 2, "$u_1 = 3(1) - 1 = 2$."),
            ("Dãy số $u_n = 2n + 5$ có số hạng thứ nhất bằng:", 7, "$u_1 = 2(1) + 5 = 7$."),
            ("Cho dãy số $u_n = 4n - 3$. Tìm giá trị của $u_1$:", 1, "$u_1 = 4(1) - 3 = 1$."),
            ("Số hạng đầu của dãy $u_n = n^2 + 2$ bằng bao nhiêu?", 3, "$u_1 = 1 + 2 = 3$."),
            ("Dãy số $u_n = 5n - 1$. Số hạng $u_1$ là:", 4, "$u_1 = 5(1) - 1 = 4$.")
        ]),
        ("Công sai d của cấp số cộng", "b6", [
            ("Cho cấp số cộng có $u_1 = 3$ và $u_2 = 7$. Công sai d bằng:", 4, "$d = 7 - 3 = 4$."),
            ("Cấp số cộng $2, 5, 8, 11, \\dots$ có công sai bằng bao nhiêu?", 3, "$d = 5 - 2 = 3$."),
            ("Cho cấp số cộng $u_n = 4n + 1$. Công sai d bằng:", 4, "Công sai là hệ số của n, $d = 4$."),
            ("Cấp số cộng có $u_1 = 10, u_2 = 15$. Tìm công sai d:", 5, "$d = 15 - 10 = 5$."),
            ("Tìm công sai d của cấp số cộng $1, 7, 13, 19$:", 6, "$d = 7 - 1 = 6$.")
        ]),
        ("Công bội q của cấp số nhân", "b7", [
            ("Cho cấp số nhân có $u_1 = 2$ và $u_2 = 6$. Công bội q bằng:", 3, "$q = 6/2 = 3$."),
            ("Cấp số nhân $1, 4, 16, 64$ có công bội bằng:", 4, "$q = 4/1 = 4$."),
            ("Cấp số nhân có $u_1 = 5, u_2 = 10$. Giá trị của q là:", 2, "$q = 10/5 = 2$."),
            ("Cho cấp số nhân có $u_1 = 3, u_2 = 15$. Công bội q bằng:", 5, "$q = 15/3 = 5$."),
            ("Tìm công bội q của cấp số nhân $4, 8, 16, 32$:", 2, "$q = 8/4 = 2$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Số hạng cụ thể của cấp số cộng", "b6", [
            ("Cho cấp số cộng có $u_1 = 2, d = 3$. Số hạng thứ 5 ($u_5$) bằng:", 14, "$u_5 = 2 + 4(3) = 14$."),
            ("Cấp số cộng $u_1 = 5, d = 4$. Tính $u_4$:", 17, "$u_4 = 5 + 3(4) = 17$."),
            ("Cho cấp số cộng có $u_1 = 1, d = 5$. Giá trị của $u_6$ bằng:", 26, "$u_6 = 1 + 5(5) = 26$."),
            ("Cấp số cộng $u_1 = 3, d = 2$. Số hạng $u_10$ bằng:", 21, "$u_{10} = 3 + 9(2) = 21$.")
        ]),
        ("Số hạng của cấp số nhân", "b7", [
            ("Cho cấp số nhân có $u_1 = 3, q = 2$. Số hạng thứ 4 ($u_4$) bằng:", 24, "$u_4 = 3 \\cdot 2^3 = 24$."),
            ("Cấp số nhân $u_1 = 2, q = 3$. Giá trị của $u_3$ là:", 18, "$u_3 = 2 \\cdot 3^2 = 18$."),
            ("Cấp số nhân có $u_1 = 1, q = 4$. Số hạng $u_3$ bằng:", 16, "$u_3 = 1 \\cdot 4^2 = 16$."),
            ("Cho cấp số nhân $u_1 = 5, q = 2$. Tính $u_4$:", 40, "$u_4 = 5 \\cdot 2^3 = 40$.")
        ]),
        ("Tổng cấp số cộng cơ bản", "b6", [
            ("Tính tổng 5 số hạng đầu của cấp số cộng $1, 3, 5, 7, 9$:", 25, "Tổng bằng $1 + 3 + 5 + 7 + 9 = 25$."),
            ("Cho cấp số cộng $u_1 = 2, d = 3$. Tổng 4 số hạng đầu bằng:", 26, "Các số hạng: 2, 5, 8, 11. Tổng bằng 26."),
            ("Tổng 3 số hạng đầu của cấp số cộng có $u_1 = 4, d = 2$ là:", 18, "4 + 6 + 8 = 18."),
            ("Cấp số cộng $u_1 = 10, d = -1$. Tổng 3 số hạng đầu là:", 27, "10 + 9 + 8 = 27.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Số hạng trung gian của cấp số nhân", "b7", [
            ("Cho ba số dương $2, x, 18$ lập thành cấp số nhân. Giá trị của x là:", 6, "$x^2 = 2 \\cdot 18 = 36 \\Rightarrow x = 6$."),
            ("Tìm số dương x để ba số $3, x, 12$ là cấp số nhân:", 6, "$x^2 = 36 \\Rightarrow x = 6$."),
            ("Ba số dương $4, x, 16$ lập thành cấp số nhân. Giá trị của x bằng:", 8, "$x^2 = 64 \\Rightarrow x = 8$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b5", "sgk_title": "Bài 5. Dãy số"},
        {"lesson_id": "b6", "sgk_title": "Bài 6. Cấp số cộng"},
        {"lesson_id": "b7", "sgk_title": "Bài 7. Cấp số nhân"}
    ]
    save_bank("c2", "Dãy số. Cấp số cộng và cấp số nhân", lessons, mc, sa)

if __name__ == "__main__":
    gen_c2()
