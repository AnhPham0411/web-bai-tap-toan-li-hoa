# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c5():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Giới hạn cơ bản của dãy số", "b15", [
            lambda: ("Giới hạn $\\lim \\frac{1}{n}$ khi $n \\to +\\infty$ bằng:", ["$0$", "$1$", "$+\\infty$", "Không tồn tại"], 0, "$\\lim \\frac{1}{n} = 0$."),
            lambda: ("Giá trị của $\\lim \\frac{1}{n^2}$ bằng:", ["$0$", "$1$", "$\\frac{1}{2}$", "$+\\infty$"], 0, "$\\lim \\frac{1}{n^2} = 0$."),
            lambda: ("Với $k \\in \\mathbb{N}^*$, giới hạn $\\lim \\frac{1}{n^k}$ bằng:", ["$0$", "$1$", "$k$", "$+\\infty$"], 0, "$\\lim \\frac{1}{n^k} = 0$."),
            lambda: ("Giới hạn của dãy hằng $u_n = 5$ là:", ["$5$", "$0$", "$1$", "$+\\infty$"], 0, "Giới hạn của hằng số c là c: $\\lim 5 = 5$."),
            lambda: ("Giới hạn $\\lim \\left(-\\frac{3}{n}\\right)$ bằng:", ["$0$", "$-3$", "$3$", "$-\\infty$"], 0, "$\\lim \\left(-\\frac{3}{n}\\right) = 0$.")
        ]),
        ("Giới hạn q mũ n với trị tuyệt đối nhỏ hơn 1", "b15", [
            lambda: ("Cho số thực q thoả mãn $|q| < 1$. Giới hạn $\\lim q^n$ bằng:", ["$0$", "$1$", "$q$", "$+\\infty$"], 0, "Nếu $|q| < 1$ thì $\\lim q^n = 0$."),
            lambda: ("Tính $\\lim \\left(\\frac{1}{2}\\right)^n$:", ["$0$", "$1$", "$\\frac{1}{2}$", "$+\\infty$"], 0, "Do $|1/2| < 1$ nên giới hạn bằng 0."),
            lambda: ("Giới hạn $\\lim \\left(-\\frac{1}{3}\\right)^n$ bằng:", ["$0$", "$-\\frac{1}{3}$", "$1$", "Không tồn tại"], 0, "Vì $|-1/3| < 1$ nên giới hạn bằng 0."),
            lambda: ("Giá trị của $\\lim \\left(\\frac{2}{3}\\right)^n$ là:", ["$0$", "$\\frac{2}{3}$", "$1$", "$+\\infty$"], 0, "Do $|2/3| < 1$ nên bằng 0."),
            lambda: ("Giới hạn nào sau đây bằng 0?", ["$\\lim \\left(\\frac{3}{4}\\right)^n$", "$\\lim \\left(\\frac{4}{3}\\right)^n$", "$\\lim 2^n$", "$\\lim (-2)^n$"], 0, "Chỉ có $3/4 < 1$ nên có giới hạn bằng 0.")
        ]),
        ("Giới hạn vô cực của dãy số", "b15", [
            lambda: ("Giới hạn $\\lim n$ khi $n \\to +\\infty$ bằng:", ["$+\\infty$", "$0$", "$1$", "$-\\infty$"], 0, "Dãy số tăng vô hạn, $\\lim n = +\\infty$."),
            lambda: ("Giá trị của $\\lim n^2$ là:", ["$+\\infty$", "$0$", "$1$", "$-\\infty$"], 0, "$\\lim n^2 = +\\infty$."),
            lambda: ("Giới hạn $\\lim (-n)$ bằng:", ["$-\\infty$", "$+\\infty$", "$0$", "$-1$"], 0, "$\\lim (-n) = -\\infty$."),
            lambda: ("Cho $q > 1$. Giới hạn $\\lim q^n$ bằng:", ["$+\\infty$", "$0$", "$1$", "$q$"], 0, "Khi $q > 1$, $q^n$ tiến đến $+\\infty$."),
            lambda: ("Giới hạn $\\lim 2^n$ bằng:", ["$+\\infty$", "$0$", "$2$", "$-\\infty$"], 0, "Do cơ số $2 > 1$ nên $\\lim 2^n = +\\infty$.")
        ]),
        ("Giới hạn hàm số tại một điểm đơn giản", "b16", [
            lambda: ("Giới hạn $\\lim_{x \\to 2} (x + 3)$ bằng:", ["$5$", "$2$", "$3$", "$6$"], 0, "Thay $x = 2$: $2 + 3 = 5$."),
            lambda: ("Tính $\\lim_{x \\to 1} (2x^2 - 1)$:", ["$1$", "$2$", "$0$", "$3$"], 0, "Thay $x = 1$: $2(1) - 1 = 1$."),
            lambda: ("Giá trị của $\\lim_{x \\to 3} (4x - 5)$ là:", ["$7$", "$12$", "$9$", "$8$"], 0, "Thay $x = 3$: $4(3) - 5 = 7$."),
            lambda: ("Giới hạn $\\lim_{x \\to -1} (x^3 + 2)$ bằng:", ["$1$", "$-1$", "$3$", "$0$"], 0, "Thay $x = -1$: $(-1)^3 + 2 = 1$."),
            lambda: ("Tính $\\lim_{x \\to 0} (5x + 4)$:", ["$4$", "$5$", "$0$", "$9$"], 0, "Thay $x = 0$: $5(0) + 4 = 4$.")
        ]),
        ("Giới hạn hàm phân thức tại một điểm xác định", "b16", [
            lambda: ("Tính giới hạn hàm phân thức $\\lim_{x \\to 2} \\frac{x + 1}{x + 2}$:", ["$\\frac{3}{4}$", "$1$", "$\\frac{1}{2}$", "$\\frac{3}{2}$"], 0, "Mẫu số khác 0, thay trực tiếp: $(2 + 1)/(2 + 2) = 3/4$."),
            lambda: ("Giá trị của $\\lim_{x \\to 1} \\frac{2x + 3}{x + 1}$ là:", ["$\\frac{5}{2}$", "$3$", "$2$", "$5$"], 0, "Thay $x = 1$: $(2 + 3)/(1 + 1) = 5/2$."),
            lambda: ("Giới hạn $\\lim_{x \\to 0} \\frac{3x + 6}{x + 2}$ bằng:", ["$3$", "$6$", "$2$", "$0$"], 0, "Thay $x = 0$: $6/2 = 3$."),
            lambda: ("Tính $\\lim_{x \\to 3} \\frac{x - 1}{x + 1}$:", ["$\\frac{1}{2}$", "$1$", "$\\frac{2}{3}$", "$\\frac{3}{4}$"], 0, "Thay $x = 3$: $2/4 = 1/2$."),
            lambda: ("Giá trị của $\\lim_{x \\to -2} \\frac{x^2}{x + 4}$ bằng:", ["$2$", "$-2$", "$4$", "$1$"], 0, "Thay $x = -2$: $4/2 = 2$.")
        ]),
        ("Khái niệm giới hạn một phía", "b16", [
            lambda: ("Kí hiệu giới hạn của hàm số $f(x)$ khi $x$ dần tới $x_0$ về phía bên phải là:", ["$\\lim_{x \\to x_0^+} f(x)$", "$\\lim_{x \\to x_0^-} f(x)$", "$\\lim_{x \\to x_0} f(x)$", "$\\lim_{x \\to +\\infty} f(x)$"], 0, "Bên phải kí hiệu là $x \\to x_0^+$."),
            lambda: ("Kí hiệu $x \\to x_0^-$ có nghĩa là:", ["x tiến tới $x_0$ và $x < x_0$", "x tiến tới $x_0$ và $x > x_0$", "x tiến tới $-x_0$", "x tiến tới $-\\infty$"], 0, "Tiến tới $x_0$ về bên trái ($x < x_0$)."),
            lambda: ("Điều kiện để tồn tại giới hạn $\\lim_{x \\to x_0} f(x) = L$ là:", ["$\\lim_{x \\to x_0^+} f(x) = \\lim_{x \\to x_0^-} f(x) = L$", "Chỉ cần tồn tại giới hạn bên phải", "Chỉ cần tồn tại giới hạn bên trái", "$f(x_0) = L$"], 0, "Giới hạn hai phía phải cùng tồn tại và bằng nhau."),
            lambda: ("Nếu $\\lim_{x \\to 1^+} f(x) = 2$ và $\\lim_{x \\to 1^-} f(x) = 3$ thì $\\lim_{x \\to 1} f(x)$:", ["Không tồn tại", "Bằng 2", "Bằng 3", "Bằng 2,5"], 0, "Do hai giới hạn một phía khác nhau nên không tồn tại giới hạn tại điểm đó."),
            lambda: ("Nếu $\\lim_{x \\to 2^+} f(x) = 4$ và $\\lim_{x \\to 2^-} f(x) = 4$ thì $\\lim_{x \\to 2} f(x)$ bằng:", ["$4$", "$8$", "$0$", "Không tồn tại"], 0, "Hai giới hạn một phía bằng nhau và bằng 4.")
        ]),
        ("Giới hạn hàm số tại vô cực cơ bản", "b16", [
            lambda: ("Giới hạn $\\lim_{x \\to +\\infty} \\frac{1}{x}$ bằng:", ["$0$", "$1$", "$+\\infty$", "$-\\infty$"], 0, "Khi $x \\to +\\infty$ thì $1/x \\to 0$."),
            lambda: ("Tính $\\lim_{x \\to -\\infty} \\frac{1}{x^2}$:", ["$0$", "$1$", "$-\\infty$", "$+\\infty$"], 0, "$\\lim_{x \\to -\\infty} 1/x^2 = 0$."),
            lambda: ("Giá trị của $\\lim_{x \\to +\\infty} \\frac{2}{x}$ là:", ["$0$", "$2$", "$+\\infty$", "$1$"], 0, "Hằng số chia cho vô cực bằng 0."),
            lambda: ("Tính giới hạn dần tới dương vô cực $\\lim_{x \\to +\\infty} x^3$:", ["$+\\infty$", "$0$", "$1$", "$-\\infty$"], 0, "Tiến đến $+\\infty$."),
            lambda: ("Tính giới hạn dần tới âm vô cực $\\lim_{x \\to -\\infty} x^3$:", ["$-\\infty$", "$+\\infty$", "$0$", "$-1$"], 0, "$(-\\infty)^3 = -\\infty$.")
        ]),
        ("Khái niệm hàm số liên tục tại một điểm", "b17", [
            lambda: ("Hàm số $y = f(x)$ liên tục tại điểm $x_0$ khi và chỉ khi:", ["$\\lim_{x \\to x_0} f(x) = f(x_0)$", "Chỉ cần $f(x_0)$ xác định", "Chỉ cần tồn tại $\\lim_{x \\to x_0} f(x)$", "$f(x_0) = 0$"], 0, "Định nghĩa hàm số liên tục tại một điểm: $\\lim_{x \\to x_0} f(x) = f(x_0)$."),
            lambda: ("Nếu $\\lim_{x \\to x_0} f(x) \\neq f(x_0)$ thì hàm số $f(x)$:", ["Gián đoạn tại $x_0$", "Liên tục tại $x_0$", "Không xác định tại $x_0$", "Đồng biến tại $x_0$"], 0, "Hàm số không liên tục thì gọi là gián đoạn tại $x_0$."),
            lambda: ("Hàm số đa thức $P(x)$ liên tục trên tập hợp nào?", ["Toàn bộ tập số thực $\\mathbb{R}$", "$[0; +\\infty)$", "$\\mathbb{R} \\setminus \\{0\\}$", "$(-1; 1)$"], 0, "Hàm đa thức liên tục trên toàn bộ $\\mathbb{R}$."),
            lambda: ("Hàm phân thức $y = \\frac{1}{x - 2}$ gián đoạn tại điểm nào?", ["$x = 2$", "$x = 0$", "$x = -2$", "$x = 1$"], 0, "Tại $x = 2$ hàm số không xác định nên gián đoạn tại $x = 2$."),
            lambda: ("Hàm số $y = \\sin x$ liên tục trên:", ["$\\mathbb{R}$", "$[-1; 1]$", "$(0; \\pi)$", "$[0; 2\\pi]$"], 0, "Hàm số lượng giác $\\sin x$ liên tục trên toàn bộ $\\mathbb{R}$.")
        ]),
        ("Tính liên tục trên một khoảng", "b17", [
            lambda: ("Hàm số $y = f(x)$ liên tục trên khoảng $(a; b)$ nếu nó:", ["Liên tục tại mọi điểm thuộc khoảng $(a; b)$", "Liên tục tại ít nhất 1 điểm", "Chỉ cần liên tục tại trung điểm", "Xác định tại a và b"], 0, "Định nghĩa liên tục trên khoảng."),
            lambda: ("Hàm số $y = \\sqrt{x}$ liên tục trên khoảng nào?", ["$(0; +\\infty)$", "$(-\\infty; 0)$", "$\\mathbb{R}$", "$(-1; 1)$"], 0, "Hàm căn bậc hai liên tục trên tập xác định của nó $[0; +\\infty)$."),
            lambda: ("Hàm số $y = \\frac{1}{x}$ liên tục trên các khoảng:", ["$(-\\infty; 0)$ và $(0; +\\infty)$", "$\\mathbb{R}$", "$[-1; 1]$", "$[0; +\\infty)$"], 0, "Liên tục trên từng khoảng xác định của nó."),
            lambda: ("Tổng, hiệu, tích của hai hàm số liên tục tại $x_0$ là hàm số:", ["Liên tục tại $x_0$", "Gián đoạn tại $x_0$", "Không xác định", "Chẵn lẻ"], 0, "Các phép toán đại số bảo toàn tính liên tục."),
            lambda: ("Thương $\\frac{f(x)}{g(x)}$ của hai hàm số liên tục tại $x_0$ sẽ liên tục tại $x_0$ nếu:", ["$g(x_0) \\neq 0$", "$g(x_0) = 0$", "$f(x_0) = 0$", "$f(x_0) \\neq 0$"], 0, "Cần điều kiện mẫu số tại điểm đó khác 0.")
        ]),
        ("Định lí giá trị trung gian", "b17", [
            lambda: ("Cho hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$. Nếu $f(a) \\cdot f(b) < 0$ thì phương trình $f(x) = 0$:", ["Có ít nhất một nghiệm trong khoảng $(a; b)$", "Vô nghiệm trên $[a; b]$", "Có đúng 2 nghiệm", "Có vô số nghiệm"], 0, "Định lí giá trị trung gian (Bolzano): luôn tồn tại ít nhất 1 nghiệm."),
            lambda: ("Điều kiện để phương trình $f(x) = 0$ có ít nhất 1 nghiệm trên $(a; b)$ theo định lí Bolzano là:", ["f liên tục trên $[a; b]$ và $f(a) \\cdot f(b) < 0$", "f đồng biến trên $[a; b]$", "$f(a) + f(b) = 0$", "$f(a) = f(b)$"], 0, "Cần liên tục trên đoạn và trái dấu ở hai đầu mút."),
            lambda: ("Nếu $f(1) = -2$ và $f(2) = 3$ với $f(x)$ liên tục trên $[1; 2]$ thì:", ["Phương trình $f(x) = 0$ có ít nhất 1 nghiệm trong $(1; 2)$", "$f(x) = 0$ vô nghiệm", "f có nghiệm $x = 1,5$", "Không kết luận được"], 0, "Do $f(1) \\cdot f(2) = -6 < 0$ nên có ít nhất 1 nghiệm trong khoảng $(1; 2)$."),
            lambda: ("Để chứng minh phương trình $x^3 - 3x + 1 = 0$ có nghiệm trong $(0; 1)$, ta xét giá trị tại 0 và 1:", ["$f(0) = 1 > 0$ và $f(1) = -1 < 0$", "$f(0) = 0$ và $f(1) = 1$", "$f(0) = 1$ và $f(1) = 2$", "Cả hai đều âm"], 0, "$f(0) = 1$ và $f(1) = 1 - 3 + 1 = -1$, trái dấu nhau."),
            lambda: ("Định lí giá trị trung gian áp dụng cho hàm số:", ["Liên tục trên một đoạn", "Gián đoạn", "Bất kì", "Hàm bậc hai"], 0, "Bắt buộc hàm số phải liên tục trên đoạn $[a; b]$.")
        ]),
        ("Quy tắc tính giới hạn của tổng hiệu tích thương", "b15", [
            lambda: ("Nếu $\\lim u_n = a$ và $\\lim v_n = b$ thì $\\lim (u_n + v_n)$ bằng:", ["$a + b$", "$a - b$", "$ab$", "$a/b$"], 0, "Giới hạn của tổng bằng tổng các giới hạn."),
            lambda: ("Nếu $\\lim u_n = a$ và $\\lim v_n = b$ thì $\\lim (u_n \\cdot v_n)$ bằng:", ["$a \\cdot b$", "$a + b$", "$a/b$", "$a^b$"], 0, "Giới hạn của tích bằng tích các giới hạn."),
            lambda: ("Nếu $\\lim u_n = a$ và $\\lim v_n = b \\neq 0$ thì $\\lim \\frac{u_n}{v_n}$ bằng:", ["$\\frac{a}{b}$", "$ab$", "$a - b$", "$b/a$"], 0, "Giới hạn của thương bằng thương hai giới hạn khi mẫu khác 0."),
            lambda: ("Cho $\\lim u_n = 3$. Giá trị của $\\lim (2u_n + 1)$ là:", ["$7$", "$6$", "$5$", "$8$"], 0, "$2(3) + 1 = 7$."),
            lambda: ("Cho $\\lim u_n = 4$. Tính $\\lim \\sqrt{u_n}$:", ["$2$", "$4$", "$16$", "Không tồn tại"], 0, "$\\sqrt{4} = 2$.")
        ]),
        ("Dạng vô định không trên không", "b16", [
            lambda: ("Khi tính $\\lim_{x \\to x_0} \\frac{f(x)}{g(x)}$ mà $f(x_0) = 0$ và $g(x_0) = 0$, ta gặp dạng vô định:", ["$\\frac{0}{0}$", "$\\frac{\\infty}{\\infty}$", "$\\infty - \\infty$", "$0 \\cdot \\infty$"], 0, "Dạng $0/0$ là dạng vô định cơ bản."),
            lambda: ("Phương pháp thường dùng để khử dạng vô định $\\frac{0}{0}$ đối với hàm đa thức là:", ["Phân tích tử và mẫu thành nhân tử chứa $(x - x_0)$ rồi rút gọn", "Quy đồng mẫu số", "Chia cho x", "Thay trực tiếp"], 0, "Triệt tiêu nhân tử chung $(x - x_0)$."),
            lambda: ("Khi gặp dạng $\\frac{0}{0}$ có chứa căn thức, ta thường dùng phương pháp:", ["Nhân lượng liên hợp", "Bình phương hai vế", "Chia cho $x^2$", "Đặt ẩn phụ lượng giác"], 0, "Nhân liên hợp để trục căn thức làm xuất hiện nhân tử triệt tiêu."),
            lambda: ("Biểu thức liên hợp của $\\sqrt{x} - 2$ là:", ["$\\sqrt{x} + 2$", "$\\sqrt{x} - 2$", "$x - 4$", "$x + 4$"], 0, "Liên hợp của $a - b$ là $a + b$."),
            lambda: ("Tích $(\\sqrt{x} - 1)(\\sqrt{x} + 1)$ bằng:", ["$x - 1$", "$x + 1$", "$x^2 - 1$", "$\\sqrt{x} - 1$"], 0, "$(\\sqrt{x})^2 - 1^2 = x - 1$.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c5-{len(mc)+1:03d}", "chapter": "c5", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 biến thể = 48 câu
    th_configs = [
        ("Giới hạn dãy phân thức cùng bậc", "b15", [
            lambda: ("Tính giới hạn $\\lim \\frac{2n + 1}{n + 3}$:", ["$2$", "$1$", "$\\frac{1}{3}$", "$0$"], 0, "Cùng bậc 1, tỉ số hệ số cao nhất là $2/1 = 2$."),
            lambda: ("Giới hạn $\\lim \\frac{4n^2 - 1}{2n^2 + 3n}$ bằng:", ["$2$", "$4$", "$\\frac{1}{2}$", "$0$"], 0, "Bậc tử bằng bậc mẫu, tỉ số hệ số là $4/2 = 2$."),
            lambda: ("Giá trị của $\\lim \\frac{3n + 5}{6n - 2}$ là:", ["$\\frac{1}{2}$", "$3$", "$2$", "$0$"], 0, "Tỉ số hệ số $3/6 = 1/2$."),
            lambda: ("Tính $\\lim \\frac{5n^3 + 2}{n^3 + n}$:", ["$5$", "$1$", "$0$", "$+\\infty$"], 0, "Tỉ số hệ số cao nhất là $5/1 = 5$.")
        ]),
        ("Giới hạn dãy bậc tử nhỏ hơn bậc mẫu", "b15", [
            lambda: ("Tính $\\lim \\frac{2n + 1}{n^2 + 1}$:", ["$0$", "$2$", "$1$", "$+\\infty$"], 0, "Bậc tử nhỏ hơn bậc mẫu nên giới hạn bằng 0."),
            lambda: ("Giới hạn $\\lim \\frac{3n^2 - 1}{n^3 + 4}$ bằng:", ["$0$", "$3$", "$1$", "$+\\infty$"], 0, "Bậc tử là 2, mẫu là 3 nên giới hạn bằng 0."),
            lambda: ("Giá trị của $\\lim \\frac{n + 10}{2n^2 + 5}$ là:", ["$0$", "$\\frac{1}{2}$", "$2$", "$5$"], 0, "Giới hạn bằng 0."),
            lambda: ("Tính $\\lim \\frac{5}{n^2 + 3}$:", ["$0$", "$5$", "$\\frac{5}{3}$", "$1$"], 0, "Giới hạn bằng 0.")
        ]),
        ("Giới hạn dạng 0/0 phân tích nhân tử", "b16", [
            lambda: ("Tính giới hạn $\\lim_{x \\to 1} \\frac{x^2 - 1}{x - 1}$:", ["$2$", "$1$", "$0$", "Không tồn tại"], 0, "$\\frac{x^2 - 1}{x - 1} = x + 1$. Khi $x \\to 1$, giới hạn bằng $1 + 1 = 2$."),
            lambda: ("Giá trị của $\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2}$ là:", ["$4$", "$2$", "$0$", "$1$"], 0, "$\\lim_{x \\to 2} (x + 2) = 4$."),
            lambda: ("Tính $\\lim_{x \\to 3} \\frac{x^2 - 9}{x - 3}$:", ["$6$", "$3$", "$9$", "$0$"], 0, "$\\lim_{x \\to 3} (x + 3) = 6$."),
            lambda: ("Giới hạn $\\lim_{x \\to -1} \\frac{x^2 - 1}{x + 1}$ bằng:", ["$-2$", "$2$", "$0$", "$-1$"], 0, "$\\lim_{x \\to -1} (x - 1) = -1 - 1 = -2$.")
        ]),
        ("Giới hạn dạng 0/0 nhân lượng liên hợp", "b16", [
            lambda: ("Tính giới hạn $\\lim_{x \\to 4} \\frac{\\sqrt{x} - 2}{x - 4}$:", ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$2$", "$0$"], 0, "$\\frac{\\sqrt{x}-2}{x-4} = \\frac{1}{\\sqrt{x}+2}$. Khi $x \\to 4$ bằng $1/(2+2) = 1/4$."),
            lambda: ("Giá trị của $\\lim_{x \\to 1} \\frac{\\sqrt{x} - 1}{x - 1}$ bằng:", ["$\\frac{1}{2}$", "$1$", "$2$", "$0$"], 0, "$\\frac{1}{\\sqrt{x}+1} = 1/(1+1) = 1/2$."),
            lambda: ("Tính $\\lim_{x \\to 9} \\frac{\\sqrt{x} - 3}{x - 9}$:", ["$\\frac{1}{6}$", "$\\frac{1}{3}$", "$3$", "$0$"], 0, "$1/(\\sqrt{9}+3) = 1/6$."),
            lambda: ("Giới hạn $\\lim_{x \\to 0} \\frac{\\sqrt{x + 1} - 1}{x}$ bằng:", ["$\\frac{1}{2}$", "$1$", "$0$", "$2$"], 0, "Nhân liên hợp: $\\frac{x}{x(\\sqrt{x+1}+1)} = \\frac{1}{\\sqrt{x+1}+1} \\to 1/2$.")
        ]),
        ("Giới hạn hàm số tại vô cực cùng bậc", "b16", [
            lambda: ("Tính $\\lim_{x \\to +\\infty} \\frac{3x + 1}{x - 2}$:", ["$3$", "$1$", "$-3$", "$0$"], 0, "Chia cả tử và mẫu cho x ta được 3."),
            lambda: ("Giá trị của $\\lim_{x \\to +\\infty} \\frac{4x^2 - 1}{2x^2 + 5}$ bằng:", ["$2$", "$4$", "$\\frac{1}{2}$", "$0$"], 0, "Hệ số bậc cao nhất là $4/2 = 2$."),
            lambda: ("Tính $\\lim_{x \\to -\\infty} \\frac{6x - 2}{2x + 1}$:", ["$3$", "$-3$", "$6$", "$0$"], 0, "Tỉ số hệ số cao nhất là $6/2 = 3$."),
            lambda: ("Giới hạn $\\lim_{x \\to +\\infty} \\frac{2x^2 + 3}{x^2 + 1}$ bằng:", ["$2$", "$1$", "$3$", "$0$"], 0, "Bằng 2.")
        ]),
        ("Tính liên tục tại điểm chứa tham số m", "b17", [
            lambda: ("Cho hàm số $f(x) = \\frac{x^2 - 1}{x - 1}$ khi $x \\neq 1$ và $f(1) = m$. Để hàm số liên tục tại $x = 1$ thì m bằng:", ["$2$", "$1$", "$0$", "$-1$"], 0, "$\\lim_{x \\to 1} f(x) = 2$. Để liên tục cần $f(1) = m = 2$."),
            lambda: ("Cho hàm số $f(x) = 2x + m$ khi $x \\ge 1$ và $f(x) = 5$ khi $x < 1$. Để hàm số liên tục tại $x = 1$ thì:", ["$m = 3$", "$m = 2$", "$m = 5$", "$m = 1$"], 0, "$\\lim_{x \\to 1^+} f(x) = 2 + m$. Cần $2 + m = 5 \\Rightarrow m = 3$."),
            lambda: ("Hàm số $f(x) = 3x - 1$ với $x \\le 2$ và $f(x) = ax + 1$ với $x > 2$. Để liên tục tại $x = 2$ thì a bằng:", ["$2$", "$3$", "$1$", "$4$"], 0, "$f(2) = 5$. Giới hạn phải là $2a + 1 = 5 \\Rightarrow a = 2$."),
            lambda: ("Tìm m để hàm số $f(x) = x + m$ liên tục tại $x = 3$ biết $f(3) = 7$:", ["$m = 4$", "$m = 3$", "$m = 7$", "$m = 10$"], 0, "$3 + m = 7 \\Rightarrow m = 4$.")
        ]),
        ("Giới hạn một phía dẫn đến vô cực", "b16", [
            lambda: ("Tính giới hạn $\\lim_{x \\to 1^+} \\frac{1}{x - 1}$:", ["$+\\infty$", "$-\\infty$", "$0$", "$1$"], 0, "Khi $x \\to 1^+$, mẫu số dương và tiến về 0, nên giới hạn bằng $+\\infty$."),
            lambda: ("Giới hạn $\\lim_{x \\to 1^-} \\frac{1}{x - 1}$ bằng:", ["$-\\infty$", "$+\\infty$", "$0$", "$-1$"], 0, "Khi $x \\to 1^-$, mẫu số âm và tiến về 0 nên bằng $-\\infty$."),
            lambda: ("Tính giới hạn một phía bên phải $\\lim_{x \\to 2^+} \\frac{x + 1}{x - 2}$:", ["$+\\infty$", "$-\\infty$", "$3$", "$0$"], 0, "Tử số tiến về 3 > 0, mẫu số tiến về $0^+$ nên bằng $+\\infty$."),
            lambda: ("Tính giới hạn một phía bên trái $\\lim_{x \\to 2^-} \\frac{x + 1}{x - 2}$:", ["$-\\infty$", "$+\\infty$", "$-3$", "$0$"], 0, "Tử số là 3 > 0, mẫu là $0^-$ nên bằng $-\\infty$.")
        ]),
        ("Tổng cấp số nhân lùi vô hạn", "b15", [
            lambda: ("Tổng của cấp số nhân lùi vô hạn $u_1 = 1, q = \\frac{1}{2}$ bằng:", ["$2$", "$1$", "$\\frac{3}{2}$", "$4$"], 0, "$S = \\frac{1}{1 - 1/2} = 2$."),
            lambda: ("Tính tổng $S = 2 + 1 + \\frac{1}{2} + \\frac{1}{4} + \\dots$:", ["$4$", "$2$", "$3$", "$\\frac{7}{2}$"], 0, "$u_1 = 2, q = 1/2 \\Rightarrow S = \\frac{2}{1 - 1/2} = 4$."),
            lambda: ("Cho cấp số nhân lùi vô hạn $u_1 = 6, q = \\frac{1}{3}$. Tổng S là:", ["$9$", "$6$", "$18$", "$12$"], 0, "$S = \\frac{6}{1 - 1/3} = 9$."),
            lambda: ("Tổng $S = 3 + 1 + \\frac{1}{3} + \\dots$ bằng:", ["$\\frac{9}{2}$", "$4$", "$3$", "$5$"], 0, "$S = \\frac{3}{1 - 1/3} = 4,5 = \\frac{9}{2}$.")
        ]),
        ("Chứng minh phương trình có nghiệm trên khoảng", "b17", [
            lambda: ("Phương trình $x^3 + 2x - 1 = 0$ có ít nhất một nghiệm trong khoảng nào sau đây?", ["$(0; 1)$", "$(1; 2)$", "$(-2; -1)$", "$(2; 3)$"], 0, "Đặt $f(x) = x^3 + 2x - 1$. Ta có $f(0) = -1 < 0$ và $f(1) = 2 > 0$ nên có nghiệm trong $(0; 1)$."),
            lambda: ("Phương trình $x^3 - 3x + 1 = 0$ có nghiệm trong khoảng:", ["$(1; 2)$", "$(2; 3)$", "$(3; 4)$", "$(-3; -2)$"], 0, "$f(1) = -1 < 0$ và $f(2) = 3 > 0$ nên có nghiệm trong $(1; 2)$."),
            lambda: ("Xét $f(x) = x^4 - 2x - 2 = 0$. Phương trình có nghiệm trong khoảng:", ["$(1; 2)$", "$(0; 1)$", "$(-1; 0)$", "$(2; 3)$"], 0, "$f(1) = -3 < 0, f(2) = 16 - 4 - 2 = 10 > 0$ nên có nghiệm trong $(1; 2)$."),
            lambda: ("Phương trình $2x^3 - 5x + 1 = 0$ có nghiệm trong khoảng:", ["$(0; 1)$", "$(2; 3)$", "$(3; 4)$", "$(-3; -2)$"], 0, "$f(0) = 1 > 0$ và $f(1) = -2 < 0$, tích âm nên có nghiệm trong $(0; 1)$.")
        ]),
        ("Giới hạn chứa căn thức tại vô cực", "b16", [
            lambda: ("Tính giới hạn $\\lim_{x \\to +\\infty} \\frac{\\sqrt{x^2 + 1}}{x}$:", ["$1$", "$-1$", "$0$", "$+\\infty$"], 0, "Rút x ra ngoài: $\\frac{x\\sqrt{1 + 1/x^2}}{x} = 1$."),
            lambda: ("Giá trị của $\\lim_{x \\to -\\infty} \\frac{\\sqrt{x^2 + 1}}{x}$ là:", ["$-1$", "$1$", "$0$", "$-\\infty$"], 0, "Khi $x < 0$ thì $\\sqrt{x^2} = -x$, do đó giới hạn bằng $-1$."),
            lambda: ("Tính $\\lim_{x \\to +\\infty} \\frac{\\sqrt{4x^2 + 3}}{x + 1}$:", ["$2$", "$4$", "$1$", "$0$"], 0, "$\\sqrt{4} = 2$, hệ số bằng 2."),
            lambda: ("Giới hạn $\\lim_{x \\to +\\infty} \\frac{\\sqrt{9x^2 + 2}}{2x - 1}$ bằng:", ["$\\frac{3}{2}$", "$3$", "$9$", "$\\frac{9}{2}$"], 0, "$\\frac{3}{2}$.")
        ]),
        ("Giới hạn dạng vô định vô cùng trừ vô cùng", "b15", [
            lambda: ("Tính giới hạn $\\lim (\\sqrt{n + 1} - \\sqrt{n})$:", ["$0$", "$1$", "$+\\infty$", "$\\frac{1}{2}$"], 0, "Nhân liên hợp: $\\frac{1}{\\sqrt{n+1} + \\sqrt{n}} \\to 0$."),
            lambda: ("Giá trị của $\\lim (\\sqrt{n^2 + 2n} - n)$ là:", ["$1$", "$2$", "$0$", "$\\frac{1}{2}$"], 0, "Nhân liên hợp: $\\frac{2n}{\\sqrt{n^2+2n} + n} = \\frac{2}{1 + 1} = 1$."),
            lambda: ("Tính $\\lim (\\sqrt{n^2 + 4n} - n)$:", ["$2$", "$4$", "$1$", "$0$"], 0, "$\\frac{4n}{2n} = 2$."),
            lambda: ("Giới hạn $\\lim (\\sqrt{n^2 + 6n} - n)$ bằng:", ["$3$", "$6$", "$2$", "$1$"], 0, "$\\frac{6}{2} = 3$.")
        ]),
        ("Ý nghĩa vận tốc tức thời và giới hạn", "b16", [
            lambda: ("Vận tốc tức thời của vật chuyển động theo quy luật $s(t) = t^2$ tại thời điểm $t = 2$ là:", ["$4\\text{ m/s}$", "$2\\text{ m/s}$", "$8\\text{ m/s}$", "$1\\text{ m/s}$"], 0, "$v(2) = \\lim_{\\Delta t \\to 0} \\frac{(2 + \\Delta t)^2 - 4}{\\Delta t} = 4\\text{ m/s}$."),
            lambda: ("Một vật rơi tự do theo công thức $s(t) = 5t^2$ (m). Vận tốc tức thời tại $t = 3\\text{ s}$ là:", ["$30\\text{ m/s}$", "$15\\text{ m/s}$", "$45\\text{ m/s}$", "$10\\text{ m/s}$"], 0, "$v(t) = 10t \\Rightarrow v(3) = 30\\text{ m/s}$."),
            lambda: ("Quy luật chuyển động $s(t) = 3t^2 + 2t$. Vận tốc tức thời tại $t = 1$ là:", ["$8\\text{ m/s}$", "$5\\text{ m/s}$", "$6\\text{ m/s}$", "$7\\text{ m/s}$"], 0, "$v(t) = 6t + 2 \\Rightarrow v(1) = 8\\text{ m/s}$."),
            lambda: ("Vật chuyển động $s(t) = 4t^2$. Tại thời điểm nào thì vận tốc tức thời bằng 16 m/s?", ["$t = 2\\text{ s}$", "$t = 4\\text{ s}$", "$t = 1\\text{ s}$", "$t = 3\\text{ s}$"], 0, "$v(t) = 8t = 16 \\Rightarrow t = 2\\text{ s}$.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c5-{len(mc)+1:03d}", "chapter": "c5", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 biến thể = 12 câu
    vd_configs = [
        ("Giới hạn dạng 0/0 chứa hai căn thức", "b16", [
            lambda: ("Tính giới hạn $\\lim_{x \\to 0} \\frac{\\sqrt{1 + x} - \\sqrt{1 - x}}{x}$:", ["$1$", "$2$", "$0$", "$\\frac{1}{2}$"], 0, "Nhân liên hợp: $\\frac{2x}{x(\\sqrt{1+x} + \\sqrt{1-x})} = \\frac{2}{2} = 1$."),
            lambda: ("Giá trị của $\\lim_{x \\to 0} \\frac{\\sqrt{1 + 2x} - 1}{x}$ là:", ["$1$", "$2$", "$\\frac{1}{2}$", "$0$"], 0, "$\\frac{2x}{x(\\sqrt{1+2x}+1)} = \\frac{2}{2} = 1$."),
            lambda: ("Tính $\\lim_{x \\to 0} \\frac{\\sqrt{1 + 4x} - 1}{x}$:", ["$2$", "$4$", "$1$", "$\\frac{1}{2}$"], 0, "$\\frac{4x}{x(\\sqrt{1+4x}+1)} = \\frac{4}{2} = 2$."),
            lambda: ("Giới hạn $\\lim_{x \\to 0} \\frac{\\sqrt{1 + 6x} - 1}{x}$ bằng:", ["$3$", "$6$", "$2$", "$1$"], 0, "$\\frac{6}{2} = 3$.")
        ]),
        ("Xác định tham số a để hàm liên tục tại điểm", "b17", [
            lambda: ("Cho hàm số $f(x) = \\frac{x^2 - 4}{x - 2}$ khi $x \\neq 2$ và $f(2) = 2a + 2$. Tìm a để hàm số liên tục tại $x = 2$:", ["$a = 1$", "$a = 2$", "$a = 0$", "$a = 3$"], 0, "$\\lim_{x \\to 2} f(x) = 4$. Cần $2a + 2 = 4 \\Rightarrow 2a = 2 \\Rightarrow a = 1$."),
            lambda: ("Tìm m để hàm số $f(x) = \\frac{x^2 - 9}{x - 3}$ ($x \\neq 3$) và $f(3) = 3m$ liên tục tại $x = 3$:", ["$m = 2$", "$m = 3$", "$m = 1$", "$m = 6$"], 0, "Giới hạn bằng 6. Cần $3m = 6 \\Rightarrow m = 2$."),
            lambda: ("Cho $f(x) = \\frac{x^2 - 16}{x - 4}$ ($x \\neq 4$) và $f(4) = 4m$. Để liên tục tại $x = 4$ thì m là:", ["$m = 2$", "$m = 4$", "$m = 1$", "$m = 8$"], 0, "Giới hạn bằng 8. Cần $4m = 8 \\Rightarrow m = 2$."),
            lambda: ("Hàm số $f(x) = \\frac{x^2 - 25}{x - 5}$ ($x \\neq 5$) và $f(5) = 2m$. Tìm m để hàm liên tục tại $x = 5$:", ["$m = 5$", "$m = 10$", "$m = 2$", "$m = 4$"], 0, "Giới hạn bằng 10. $2m = 10 \\Rightarrow m = 5$.")
        ]),
        ("Giới hạn vô cực trừ vô cực tại vô cực", "b16", [
            lambda: ("Tính giới hạn $\\lim_{x \\to +\\infty} (\\sqrt{x^2 + 2x} - x)$:", ["$1$", "$2$", "$0$", "$\\frac{1}{2}$"], 0, "Nhân liên hợp: $\\frac{2x}{\\sqrt{x^2+2x} + x} = \\frac{2}{2} = 1$."),
            lambda: ("Giá trị của $\\lim_{x \\to +\\infty} (\\sqrt{x^2 + 4x} - x)$ là:", ["$2$", "$4$", "$1$", "$0$"], 0, "$\\frac{4x}{2x} = 2$."),
            lambda: ("Tính $\\lim_{x \\to +\\infty} (\\sqrt{x^2 + 6x} - x)$:", ["$3$", "$6$", "$2$", "$1$"], 0, "$\\frac{6x}{2x} = 3$."),
            lambda: ("Giới hạn $\\lim_{x \\to +\\infty} (\\sqrt{x^2 + 8x} - x)$ bằng:", ["$4$", "$8$", "$2$", "$1$"], 0, "$\\frac{8x}{2x} = 4$.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c5-{len(mc)+1:03d}", "chapter": "c5", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb = [
        ("Giới hạn cơ bản tại một điểm", "b16", [
            ("Tính giới hạn $\\lim_{x \\to 2} (3x + 4)$:", 10, "Thay $x = 2$: $3(2) + 4 = 10$."),
            ("Giá trị của $\\lim_{x \\to 1} (5x - 2)$ bằng:", 3, "$5(1) - 2 = 3$."),
            ("Tính $\\lim_{x \\to 3} (2x^2 + 1)$:", 19, "$2(9) + 1 = 19$."),
            ("Giới hạn $\\lim_{x \\to 0} (4x + 7)$ bằng:", 7, "$4(0) + 7 = 7$."),
            ("Tính giá trị của $\\lim_{x \\to 4} (2x - 3)$:", 5, "$2(4) - 3 = 5$.")
        ]),
        ("Giới hạn dãy số bằng 0", "b15", [
            ("Giá trị của $\\lim \\frac{5}{n}$ bằng bao nhiêu?", 0, "Hằng số chia cho vô cực bằng 0."),
            ("Tính giới hạn $\\lim \\frac{1}{n^3}$:", 0, "Bằng 0."),
            ("Giới hạn $\\lim \\left(\\frac{1}{4}\\right)^n$ bằng:", 0, "Do $|1/4| < 1$ nên giới hạn bằng 0."),
            ("Tính $\\lim \\frac{-8}{n^2}$:", 0, "Bằng 0."),
            ("Giá trị của $\\lim \\left(-\\frac{1}{2}\\right)^n$ là:", 0, "Bằng 0.")
        ]),
        ("Tính liên tục của đa thức tại một điểm", "b17", [
            ("Cho hàm số $f(x) = x^2 + 3$. Giá trị của $f(2)$ bằng bao nhiêu?", 7, "$2^2 + 3 = 7$."),
            ("Hàm số $f(x) = 2x + 5$ có giá trị tại $x = 3$ bằng:", 11, "$2(3) + 5 = 11$."),
            ("Giá trị của $f(1)$ với $f(x) = 4x^3 - 1$ là:", 3, "$4(1) - 1 = 3$."),
            ("Tính $f(0)$ biết $f(x) = 3x^2 + 8$:", 8, "$f(0) = 8$."),
            ("Cho $f(x) = 5 - 2x$. Tính $f(1)$:", 3, "$5 - 2(1) = 3$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c5-{len(sa)+1:03d}", "chapter": "c5", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Giới hạn phân thức cùng bậc", "b15", [
            ("Tính giới hạn $\\lim \\frac{6n + 1}{2n + 3}$:", 3, "$6/2 = 3$."),
            ("Giá trị của $\\lim \\frac{8n^2 + 5}{2n^2 + 1}$ bằng:", 4, "$8/2 = 4$."),
            ("Tính $\\lim \\frac{10n - 3}{5n + 2}$:", 2, "$10/5 = 2$."),
            ("Giới hạn $\\lim \\frac{12n^3 + 1}{3n^3 + 4}$ bằng:", 4, "$12/3 = 4$.")
        ]),
        ("Khử dạng vô định 0/0", "b16", [
            ("Tính giới hạn $\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2}$:", 4, "$\\lim_{x \\to 2} (x + 2) = 4$."),
            ("Giá trị của $\\lim_{x \\to 3} \\frac{x^2 - 9}{x - 3}$ là:", 6, "$\\lim_{x \\to 3} (x + 3) = 6$."),
            ("Tính $\\lim_{x \\to 4} \\frac{x^2 - 16}{x - 4}$:", 8, "$\\lim_{x \\to 4} (x + 4) = 8$."),
            ("Giới hạn $\\lim_{x \\to 5} \\frac{x^2 - 25}{x - 5}$ bằng:", 10, "$\\lim_{x \\to 5} (x + 5) = 10$.")
        ]),
        ("Tổng cấp số nhân lùi vô hạn nguyên", "b15", [
            ("Tính tổng cấp số nhân lùi vô hạn có $u_1 = 3, q = \\frac{1}{2}$:", 6, "$S = 3 / (1 - 1/2) = 6$."),
            ("Cấp số nhân lùi vô hạn $u_1 = 4, q = \\frac{1}{2}$ có tổng bằng:", 8, "$S = 4 / (1/2) = 8$."),
            ("Tính tổng $S = 5 + \\frac{5}{2} + \\frac{5}{4} + \\dots$:", 10, "$S = 5 / (1/2) = 10$."),
            ("Cho $u_1 = 2, q = \\frac{2}{3}$. Tổng của cấp số nhân lùi vô hạn bằng:", 6, "$S = 2 / (1 - 2/3) = 6$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c5-{len(sa)+1:03d}", "chapter": "c5", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Tìm m để hàm liên tục tại điểm", "b17", [
            ("Cho hàm số $f(x) = \\frac{x^2 - 1}{x - 1}$ khi $x \\neq 1$ và $f(1) = m$. Tìm m để hàm liên tục tại $x = 1$:", 2, "Giới hạn bằng 2, vậy $m = 2$."),
            ("Tìm m để hàm số $f(x) = \\frac{x^2 - 4}{x - 2}$ khi $x \\neq 2$ và $f(2) = m$ liên tục tại $x = 2$:", 4, "Giới hạn bằng 4, vậy $m = 4$."),
            ("Cho $f(x) = \\frac{x^2 - 9}{x - 3}$ ($x \\neq 3$) và $f(3) = 2m$. Tìm m để hàm liên tục tại $x = 3$:", 3, "$2m = 6 \\Rightarrow m = 3$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c5-{len(sa)+1:03d}", "chapter": "c5", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b15", "sgk_title": "Bài 15. Giới hạn của dãy số"},
        {"lesson_id": "b16", "sgk_title": "Bài 16. Giới hạn của hàm số"},
        {"lesson_id": "b17", "sgk_title": "Bài 17. Hàm số liên tục"}
    ]
    save_bank("c5", "Giới hạn. Hàm số liên tục", lessons, mc, sa)

if __name__ == "__main__":
    gen_c5()
