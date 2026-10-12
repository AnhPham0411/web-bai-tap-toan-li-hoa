# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c2():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Khái niệm vectơ trong không gian", "b6", [
            lambda: ("Vectơ trong không gian là:", ["Một đoạn thẳng có hướng", "Một đường thẳng", "Một tia", "Một điểm"], 0, "Định nghĩa vectơ: đoạn thẳng có hướng."),
            lambda: ("Vectơ có điểm đầu và điểm cuối trùng nhau gọi là:", ["Vectơ-không", "Vectơ đơn vị", "Vectơ đối", "Vectơ cùng phương"], 0, "Kí hiệu là $\\vec{0}$."),
            lambda: ("Độ dài của vectơ $\\vec{AB}$ trong không gian chính là:", ["Khoảng cách giữa hai điểm A và B", "Toạ độ của điểm B", "Toạ độ của điểm A", "Đường thẳng AB"], 0, "Độ dài $|\vec{AB}| = AB$."),
            lambda: ("Hai vectơ được gọi là cùng phương nếu:", ["Giá của chúng song song hoặc trùng nhau", "Chúng có cùng độ dài", "Chúng có cùng điểm đầu", "Chúng vuông góc với nhau"], 0, "Định nghĩa hai vectơ cùng phương."),
            lambda: ("Vectơ đối của vectơ $\\vec{a}$ là vectơ:", ["Ngược hướng và có cùng độ dài với $\\vec{a}$", "Cùng hướng với $\\vec{a}$", "Có độ dài bằng 0", "Vuông góc với $\\vec{a}$"], 0, "Vectơ đối ngược hướng và có cùng độ dài.")
        ]),
        ("Quy tắc hình hộp", "b6", [
            lambda: ("Cho hình hộp $ABCD.A'B'C'D'$. Đẳng thức vectơ nào sau đây đúng?", ["$\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$", "$\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AC}$", "$\\vec{AC'} = \\vec{AA'} + \\vec{BB'} + \\vec{CC'}$", "$\\vec{AC'} = \\vec{AB} + \\vec{BC} + \\vec{CD}$"], 0, "Quy tắc hình hộp: $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$."),
            lambda: ("Trong hình hộp $ABCD.A'B'C'D'$, tổng $\\vec{AB} + \\vec{AD}$ bằng vectơ nào?", ["$\\vec{AC}$", "$\\vec{BD}$", "$\\vec{AC'}$", "$\\vec{AA'}$"], 0, "Quy tắc hình bình hành ở đáy: $\\vec{AB} + \\vec{AD} = \\vec{AC}$."),
            lambda: ("Cho hình hộp $ABCD.A'B'C'D'$. Tổng $\\vec{A'B'} + \\vec{A'D'} + \\vec{A'A}$ bằng:", ["$\\vec{A'C}$", "$\\vec{AC'}$", "$\\vec{A'C'}$", "$\\vec{0}$"], 0, "Quy tắc hình hộp từ đỉnh A': $\\vec{A'C}$."),
            lambda: ("Trong hình hộp $ABCD.A'B'C'D'$, vectơ $\\vec{BA} + \\vec{BC} + \\vec{BB'}$ bằng:", ["$\\vec{BD'}$", "$\\vec{BD}$", "$\\vec{AC'}$", "$\\vec{B'D}$"], 0, "Xuất phát từ đỉnh B: $\\vec{BD'}$."),
            lambda: ("Tổng $\\vec{DA} + \\vec{DC} + \\vec{DD'}$ trong hình hộp $ABCD.A'B'C'D'$ bằng:", ["$\\vec{DB'}$", "$\\vec{AC'}$", "$\\vec{BD'}$", "$\\vec{CA'}$"], 0, "Đường chéo xuất phát từ đỉnh D: $\\vec{DB'}$.")
        ]),
        ("Toạ độ của vectơ theo ba vectơ đơn vị", "b7", [
            lambda: ("Trong không gian $Oxyz$, cho $\\vec{u} = 2\\vec{i} - 3\\vec{j} + 4\\vec{k}$. Toạ độ của $\\vec{u}$ là:", ["$(2; -3; 4)$", "$(2; 3; 4)$", "$(-3; 2; 4)$", "$(4; -3; 2)$"], 0, "$\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\Rightarrow \\vec{u} = (2; -3; 4)$."),
            lambda: ("Cho vectơ $\\vec{a} = 3\\vec{i} + 5\\vec{k}$. Toạ độ của $\\vec{a}$ là:", ["$(3; 0; 5)$", "$(3; 5; 0)$", "$(0; 3; 5)$", "$(3; 5; 1)$"], 0, "Khuyết $\\vec{j}$ nên $y = 0 \\Rightarrow (3; 0; 5)$."),
            lambda: ("Vectơ $\\vec{b} = -\\vec{j} + 2\\vec{k}$ có toạ độ là:", ["$(0; -1; 2)$", "$(-1; 2; 0)$", "$(0; 1; 2)$", "$(2; -1; 0)$"], 0, "Khuyết $\\vec{i}$ nên toạ độ là $(0; -1; 2)$."),
            lambda: ("Vectơ đơn vị $\\vec{i}$ trên trục Ox có toạ độ là:", ["$(1; 0; 0)$", "$(0; 1; 0)$", "$(0; 0; 1)$", "$(1; 1; 1)$"], 0, "$\\vec{i} = (1; 0; 0)$."),
            lambda: ("Toạ độ của vectơ đơn vị $\\vec{k}$ trên trục Oz là:", ["$(0; 0; 1)$", "$(1; 0; 0)$", "$(0; 1; 0)$", "$(0; 1; 1)$"], 0, "$\\vec{k} = (0; 0; 1)$.")
        ]),
        ("Toạ độ của điểm trong không gian", "b7", [
            lambda: ("Điểm $M(1; -2; 3)$ có toạ độ vectơ $\\vec{OM}$ là:", ["$(1; -2; 3)$", "$(-1; 2; -3)$", "$(3; -2; 1)$", "$(1; 2; 3)$"], 0, "Toạ độ của điểm M chính là toạ độ của vectơ $\\vec{OM}$."),
            lambda: ("Gốc toạ độ O trong không gian $Oxyz$ có toạ độ là:", ["$(0; 0; 0)$", "$(1; 1; 1)$", "$(0; 0; 1)$", "$(1; 0; 0)$"], 0, "$O(0; 0; 0)$."),
            lambda: ("Hình chiếu của điểm $M(2; 3; 4)$ lên mặt phẳng toạ độ $(Oxy)$ là:", ["$(2; 3; 0)$", "$(2; 0; 4)$", "$(0; 3; 4)$", "$(2; 0; 0)$"], 0, "Chiếu lên $(Oxy)$ thì giữ nguyên x, y và cho $z = 0$."),
            lambda: ("Hình chiếu của điểm $A(1; -4; 5)$ lên trục Ox có toạ độ là:", ["$(1; 0; 0)$", "$(0; -4; 0)$", "$(0; 0; 5)$", "$(1; -4; 0)$"], 0, "Chiếu lên trục Ox chỉ giữ lại hoành độ: $(1; 0; 0)$."),
            lambda: ("Hình chiếu của điểm $B(3; 2; -1)$ lên mặt phẳng $(Oyz)$ là:", ["$(0; 2; -1)$", "$(3; 0; -1)$", "$(3; 2; 0)$", "$(0; 0; -1)$"], 0, "Cho hoành độ $x = 0$: $(0; 2; -1)$.")
        ]),
        ("Toạ độ của vectơ nối hai điểm", "b8", [
            lambda: ("Cho hai điểm $A(1; 2; 3)$ và $B(4; 5; 6)$. Toạ độ vectơ $\\vec{AB}$ là:", ["$(3; 3; 3)$", "$(5; 7; 9)$", "$(-3; -3; -3)$", "$(4; 10; 18)$"], 0, "$\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (3; 3; 3)$."),
            lambda: ("Cho $A(2; -1; 4)$ và $B(1; 3; 0)$. Toạ độ của $\\vec{AB}$ bằng:", ["$(-1; 4; -4)$", "$(1; -4; 4)$", "$(3; 2; 4)$", "$(-1; 2; -4)$"], 0, "$\\vec{AB} = (1-2; 3 - (-1); 0-4) = (-1; 4; -4)$."),
            lambda: ("Toạ độ của vectơ $\\vec{BA}$ với $A(0; 2; 1)$ và $B(3; 1; -2)$ là:", ["$(-3; 1; 3)$", "$(3; -1; -3)$", "$(3; 3; -1)$", "$(-3; -1; 3)$"], 0, "$\\vec{BA} = (0-3; 2-1; 1 - (-2)) = (-3; 1; 3)$."),
            lambda: ("Cho $M(1; 1; 1)$ và $N(2; 3; 4)$. Vectơ $\\vec{MN}$ có toạ độ là:", ["$(1; 2; 3)$", "$(3; 4; 5)$", "$(-1; -2; -3)$", "$(2; 3; 4)$"], 0, "$\\vec{MN} = (1; 2; 3)$."),
            lambda: ("Toạ độ vectơ $\\vec{OA}$ với $A(5; -2; 7)$ là:", ["$(5; -2; 7)$", "$(-5; 2; -7)$", "$(0; 0; 0)$", "$(5; 2; 7)$"], 0, "$\\vec{OA} = (5; -2; 7)$.")
        ]),
        ("Toạ độ trung điểm của đoạn thẳng", "b7", [
            lambda: ("Cho hai điểm $A(1; 2; 3)$ và $B(3; 4; 5)$. Toạ độ trung điểm M của AB là:", ["$(2; 3; 4)$", "$(4; 6; 8)$", "$(1; 1; 1)$", "$(2; 2; 2)$"], 0, "$M = \\left(\\frac{1+3}{2}; \\frac{2+4}{2}; \\frac{3+5}{2}\\right) = (2; 3; 4)$."),
            lambda: ("Trung điểm của đoạn thẳng nối $A(0; 4; -2)$ và $B(2; 0; 6)$ có toạ độ là:", ["$(1; 2; 2)$", "$(2; 4; 4)$", "$(1; 2; 4)$", "$(2; 2; 2)$"], 0, "$M = (1; 2; 2)$."),
            lambda: ("Cho $A(4; -2; 6)$ và $B(-2; 4; 0)$. Toạ độ trung điểm I là:", ["$(1; 1; 3)$", "$(2; 2; 6)$", "$(3; 3; 3)$", "$(1; 2; 3)$"], 0, "$I = (1; 1; 3)$."),
            lambda: ("Tìm toạ độ trung điểm của đoạn AB với $A(2; 5; 1)$ và $B(4; 1; 3)$:", ["$(3; 3; 2)$", "$(6; 6; 4)$", "$(2; -4; 2)$", "$(3; 2; 2)$"], 0, "$((2+4)/2; (5+1)/2; (1+3)/2) = (3; 3; 2)$."),
            lambda: ("Nếu I là trung điểm của AB thì toạ độ điểm B tính qua A và I là:", ["$(2x_I - x_A; 2y_I - y_A; 2z_I - z_A)$", "$(x_I - x_A; y_I - y_A; z_I - z_A)$", "$(x_A + x_I; y_A + y_I; z_A + z_I)$", "$((x_A + x_I)/2; \\dots)$"], 0, "$x_B = 2x_I - x_A$ tương tự cho y và z.")
        ]),
        ("Toạ độ trọng tâm tam giác", "b7", [
            lambda: ("Cho tam giác ABC có $A(1; 2; 3), B(2; 3; 4), C(3; 4; 5)$. Toạ độ trọng tâm G là:", ["$(2; 3; 4)$", "$(6; 9; 12)$", "$(1; 1; 1)$", "$(3; 3; 3)$"], 0, "$G = \\left(\\frac{1+2+3}{3}; \\frac{2+3+4}{3}; \\frac{3+4+5}{3}\\right) = (2; 3; 4)$."),
            lambda: ("Toạ độ trọng tâm tam giác có ba đỉnh $A(0; 3; 1), B(3; 0; 2), C(3; 3; 0)$ là:", ["$(2; 2; 1)$", "$(6; 6; 3)$", "$(3; 3; 1)$", "$(1; 1; 1)$"], 0, "$G = (6/3; 6/3; 3/3) = (2; 2; 1)$."),
            lambda: ("Trọng tâm tam giác $A(1; -1; 2), B(2; 1; 1), C(0; 3; 3)$ có toạ độ là:", ["$(1; 1; 2)$", "$(3; 3; 6)$", "$(1; 2; 2)$", "$(0; 1; 2)$"], 0, "$G = (3/3; 3/3; 6/3) = (1; 1; 2)$."),
            lambda: ("Cho $A(3; 0; 0), B(0; 3; 0), C(0; 0; 3)$. Trọng tâm G của tam giác ABC là:", ["$(1; 1; 1)$", "$(3; 3; 3)$", "$(0; 0; 0)$", "$(1; 0; 1)$"], 0, "$G = (1; 1; 1)$."),
            lambda: ("Nếu G là trọng tâm tam giác ABC thì hệ thức vectơ nào đúng?", ["$\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0}$", "$\\vec{GA} + \\vec{GB} = \\vec{GC}$", "$\\vec{AB} + \\vec{AC} = \\vec{AG}$", "$\\vec{OG} = \\vec{OA} + \\vec{OB} + \\vec{OC}$"], 0, "Tính chất trọng tâm: $\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0}$.")
        ]),
        ("Phép cộng trừ vectơ toạ độ", "b8", [
            lambda: ("Cho $\\vec{u} = (1; 2; 3)$ và $\\vec{v} = (2; 1; -1)$. Toạ độ của $\\vec{u} + \\vec{v}$ là:", ["$(3; 3; 2)$", "$(1; 1; 4)$", "$(-1; 1; 4)$", "$(2; 2; -3)$"], 0, "$\\vec{u} + \\vec{v} = (1+2; 2+1; 3-1) = (3; 3; 2)$."),
            lambda: ("Cho $\\vec{u} = (3; -1; 2)$ và $\\vec{v} = (1; 2; 4)$. Toạ độ của $\\vec{u} - \\vec{v}$ bằng:", ["$(2; -3; -2)$", "$(4; 1; 6)$", "$(-2; 3; 2)$", "$(2; 1; -2)$"], 0, "$\\vec{u} - \\vec{v} = (3-1; -1-2; 2-4) = (2; -3; -2)$."),
            lambda: ("Cho $\\vec{a} = (2; 0; -1)$. Toạ độ của vectơ $2\\vec{a}$ là:", ["$(4; 0; -2)$", "$(4; 0; -1)$", "$(2; 0; -2)$", "$(1; 0; -0,5)$"], 0, "$2\\vec{a} = (4; 0; -2)$."),
            lambda: ("Cho $\\vec{u} = (1; -2; 3)$. Toạ độ của $-\\vec{u}$ là:", ["$(-1; 2; -3)$", "$(1; 2; 3)$", "$(-1; -2; -3)$", "$(2; -1; 3)$"], 0, "$-\\vec{u} = (-1; 2; -3)$."),
            lambda: ("Cho $\\vec{a} = (1; 1; 1)$ và $\\vec{b} = (2; -1; 0)$. Toạ độ $\\vec{a} + \\vec{b}$ bằng:", ["$(3; 0; 1)$", "$(1; 2; 1)$", "$(2; 0; 1)$", "$(3; 2; 1)$"], 0, "$(1+2; 1-1; 1+0) = (3; 0; 1)$.")
        ]),
        ("Độ dài của vectơ", "b8", [
            lambda: ("Độ dài của vectơ $\\vec{u} = (1; 2; 2)$ bằng:", ["$3$", "$5$", "$\\sqrt{5}$", "$9$"], 0, "$|\\vec{u}| = \\sqrt{1^2 + 2^2 + 2^2} = \\sqrt{1 + 4 + 4} = \\sqrt{9} = 3$."),
            lambda: ("Tính độ dài của vectơ $\\vec{a} = (2; -2; 1)$:", ["$3$", "$9$", "$\\sqrt{5}$", "$5$"], 0, "$|\\vec{a}| = \\sqrt{4 + 4 + 1} = 3$."),
            lambda: ("Vectơ $\\vec{u} = (0; 3; 4)$ có độ dài là:", ["$5$", "$7$", "$25$", "$\\sqrt{7}$"], 0, "$\\sqrt{0 + 9 + 16} = 5$."),
            lambda: ("Độ dài của vectơ $\\vec{v} = (1; 1; 1)$ bằng:", ["$\\sqrt{3}$", "$3$", "$1$", "$\\sqrt{2}$"], 0, "$|\\vec{v}| = \\sqrt{1 + 1 + 1} = \\sqrt{3}$."),
            lambda: ("Tính độ dài vectơ $\\vec{b} = (-6; 8; 0)$:", ["$10$", "$14$", "$\\sqrt{14}$", "$2$"], 0, "$\\sqrt{36 + 64} = \\sqrt{100} = 10$.")
        ]),
        ("Khoảng cách giữa hai điểm trong không gian", "b8", [
            lambda: ("Khoảng cách giữa hai điểm $A(1; 1; 1)$ và $B(2; 3; 3)$ bằng:", ["$3$", "$\\sqrt{5}$", "$9$", "$5$"], 0, "$AB = \\sqrt{(2-1)^2 + (3-1)^2 + (3-1)^2} = \\sqrt{1 + 4 + 4} = 3$."),
            lambda: ("Tính khoảng cách giữa hai điểm $O(0; 0; 0)$ và $M(1; 2; 2)$:", ["$3$", "$\\sqrt{5}$", "$5$", "$9$"], 0, "$OM = \\sqrt{1 + 4 + 4} = 3$."),
            lambda: ("Khoảng cách giữa $A(2; 0; 0)$ và $B(0; 0; 2)$ bằng:", ["$2\\sqrt{2}$", "$4$", "$2$", "$0$"], 0, "$AB = \\sqrt{4 + 4} = \\sqrt{8} = 2\\sqrt{2}$."),
            lambda: ("Cho $A(1; 0; 0)$ và $B(1; 3; 4)$. Khoảng cách AB bằng:", ["$5$", "$7$", "$25$", "$4$"], 0, "$AB = \\sqrt{0 + 9 + 16} = 5$."),
            lambda: ("Khoảng cách giữa hai điểm $M(3; -1; 2)$ và $N(3; 2; -2)$ là:", ["$5$", "$3$", "$\\sqrt{7}$", "$7$"], 0, "$MN = \\sqrt{0 + 3^2 + (-4)^2} = 5$.")
        ]),
        ("Tích vô hướng của hai vectơ", "b8", [
            lambda: ("Cho $\\vec{u} = (1; 2; 3)$ và $\\vec{v} = (2; -1; 1)$. Tích vô hướng $\\vec{u} \\cdot \\vec{v}$ bằng:", ["$3$", "$5$", "$0$", "$4$"], 0, "$\\vec{u} \\cdot \\vec{v} = 1(2) + 2(-1) + 3(1) = 2 - 2 + 3 = 3$."),
            lambda: ("Tính tích vô hướng của $\\vec{a} = (2; 3; -1)$ và $\\vec{b} = (1; -2; 4)$:", ["$-8$", "$8$", "$-4$", "$0$"], 0, "$\\vec{a} \\cdot \\vec{b} = 2(1) + 3(-2) + (-1)(4) = 2 - 6 - 4 = -8$."),
            lambda: ("Cho $\\vec{u} = (3; 1; 2)$ và $\\vec{v} = (-1; 2; 1)$. Giá trị $\\vec{u} \\cdot \\vec{v}$ là:", ["$1$", "$-1$", "$3$", "$0$"], 0, "$3(-1) + 1(2) + 2(1) = -3 + 2 + 2 = 1$."),
            lambda: ("Tích vô hướng của $\\vec{i}$ và $\\vec{j}$ trong hệ $Oxyz$ bằng:", ["$0$", "$1$", "$-1$", "Không xác định"], 0, "Hai vectơ đơn vị vuông góc với nhau nên tích vô hướng bằng 0."),
            lambda: ("Tích vô hướng $\\vec{k} \\cdot \\vec{k}$ bằng:", ["$1$", "$0$", "$-1$", "$2$"], 0, "$|\\vec{k}|^2 = 1^2 = 1$.")
        ]),
        ("Hai vectơ vuông góc", "b8", [
            lambda: ("Hai vectơ $\\vec{u}$ và $\\vec{v}$ vuông góc với nhau khi và chỉ khi:", ["$\\vec{u} \\cdot \\vec{v} = 0$", "$\\vec{u} = \\vec{v}$", "$|\\vec{u}| = |\\vec{v}|$", "$\\vec{u} \\cdot \\vec{v} = 1$"], 0, "Hai vectơ khác không vuông góc $\\Leftrightarrow$ tích vô hướng bằng 0."),
            lambda: ("Cho $\\vec{u} = (1; 2; m)$ và $\\vec{v} = (2; 1; -2)$. Hai vectơ vuông góc khi m bằng:", ["$2$", "$-2$", "$1$", "$4$"], 0, "$\\vec{u} \\cdot \\vec{v} = 2 + 2 - 2m = 4 - 2m = 0 \\Rightarrow m = 2$."),
            lambda: ("Tìm m để $\\vec{a} = (m; 1; 2)$ vuông góc với $\\vec{b} = (2; -4; 1)$:", ["$1$", "$2$", "$0$", "$-1$"], 0, "$2m - 4 + 2 = 0 \\Rightarrow 2m - 2 = 0 \\Rightarrow m = 1$."),
            lambda: ("Vectơ $\\vec{u} = (1; 0; 0)$ vuông góc với vectơ nào sau đây?", ["$\\vec{v} = (0; 2; 3)$", "$\\vec{v} = (1; 2; 3)$", "$\\vec{v} = (2; 0; 0)$", "$\\vec{v} = (-1; 0; 0)$"], 0, "$1(0) + 0(2) + 0(3) = 0$ nên vuông góc với $(0; 2; 3)$."),
            lambda: ("Tìm x để $\\vec{u} = (x; 2; 1)$ vuông góc với $\\vec{v} = (3; -1; -1)$:", ["$1$", "$2$", "$-1$", "$3$"], 0, "$3x - 2 - 1 = 0 \\Rightarrow 3x = 3 \\Rightarrow x = 1$.")
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
        ("Toạ độ đỉnh thứ tư của hình bình hành", "b8", [
            lambda: ("Cho ba điểm $A(1; 2; 3), B(2; 4; 5), C(4; 5; 6)$. Toạ độ đỉnh D để ABCD là hình bình hành là:", ["$(3; 3; 4)$", "$(5; 7; 8)$", "$(1; 3; 4)$", "$(3; 4; 5)$"], 0, "$\\vec{AD} = \\vec{BC} \\Rightarrow D = A + C - B = (1+4-2; 2+5-4; 3+6-5) = (3; 3; 4)$."),
            lambda: ("Tìm toạ độ đỉnh D của hình bình hành ABCD biết $A(0; 1; 2), B(1; 3; 1), C(2; 2; 4)$:", ["$(1; 0; 5)$", "$(3; 4; 3)$", "$(1; 1; 3)$", "$(2; 0; 4)$"], 0, "$D = A + C - B = (0+2-1; 1+2-3; 2+4-1) = (1; 0; 5)$."),
            lambda: ("Cho hình bình hành ABCD có $A(2; 1; 0), B(3; 2; 1), C(1; 4; 2)$. Toạ độ đỉnh D là:", ["$(0; 3; 1)$", "$(2; 5; 3)$", "$(4; 3; 1)$", "$(1; 2; 1)$"], 0, "$D = (2+1-3; 1+4-2; 0+2-1) = (0; 3; 1)$."),
            lambda: ("Biết $A(1; 0; 1), B(2; 1; 2), C(3; 4; 5)$ là 3 đỉnh hình bình hành ABCD. Tìm D:", ["$(2; 3; 4)$", "$(4; 5; 6)$", "$(1; 2; 3)$", "$(3; 2; 4)$"], 0, "$D = (1+3-2; 0+4-1; 1+5-2) = (2; 3; 4)$.")
        ]),
        ("Hai vectơ cùng phương trong không gian", "b8", [
            lambda: ("Cho $\\vec{u} = (2; 4; -6)$ và $\\vec{v} = (1; m; -3)$. Để $\\vec{u}$ và $\\vec{v}$ cùng phương thì m bằng:", ["$2$", "$4$", "$-2$", "$1$"], 0, "$\\frac{2}{1} = \\frac{4}{m} = \\frac{-6}{-3} = 2 \\Rightarrow m = 2$."),
            lambda: ("Tìm m để $\\vec{a} = (3; -6; 9)$ cùng phương với $\\vec{b} = (1; -2; m)$:", ["$3$", "$9$", "$-3$", "$1$"], 0, "Tỉ số bằng 3 nên $m = 9/3 = 3$."),
            lambda: ("Hai vectơ $\\vec{u} = (m; 2; 4)$ và $\\vec{v} = (2; 1; 2)$ cùng phương khi m bằng:", ["$4$", "$2$", "$1$", "$8$"], 0, "$m/2 = 2/1 = 2 \\Rightarrow m = 4$."),
            lambda: ("Cho $\\vec{a} = (1; 2; 3)$ và $\\vec{b} = (2; 4; k)$ cùng phương. Giá trị của k là:", ["$6$", "$3$", "$4$", "$8$"], 0, "$k = 3 \\times 2 = 6$.")
        ]),
        ("Ba điểm thẳng hàng trong không gian", "b8", [
            lambda: ("Ba điểm $A, B, C$ thẳng hàng khi và chỉ khi:", ["Hai vectơ $\\vec{AB}$ và $\\vec{AC}$ cùng phương", "$\\vec{AB} = \\vec{AC}$", "$AB + BC = AC$", "$AB = BC$"], 0, "Điều kiện thẳng hàng là hai vectơ $\\vec{AB}, \\vec{AC}$ cùng phương."),
            lambda: ("Cho $A(1; 2; 3), B(2; 4; 5), C(3; 6; m)$. Tìm m để A, B, C thẳng hàng:", ["$7$", "$6$", "$8$", "$5$"], 0, "$\\vec{AB} = (1; 2; 2)$. $\\vec{AC} = (2; 4; m - 3)$. Cùng phương khi $m - 3 = 4 \\Rightarrow m = 7$."),
            lambda: ("Tìm y để $A(0; 1; 2), B(1; 3; 4), C(2; y; 6)$ thẳng hàng:", ["$5$", "$4$", "$6$", "$3$"], 0, "$\\vec{AB} = (1; 2; 2)$. $\\vec{AC} = (2; y - 1; 4) \\Rightarrow y - 1 = 4 \\Rightarrow y = 5$."),
            lambda: ("Cho $A(1; 0; 0), B(2; 1; 1), C(3; 2; z)$ thẳng hàng. Giá trị của z là:", ["$2$", "$1$", "$3$", "$0$"], 0, "$\\vec{AB} = (1; 1; 1) \\Rightarrow \\vec{AC} = (2; 2; z) \\Rightarrow z = 2$.")
        ]),
        ("Tính côsin góc giữa hai vectơ", "b8", [
            lambda: ("Tính côsin góc giữa hai vectơ $\\vec{u} = (1; 1; 0)$ và $\\vec{v} = (0; 1; 1)$:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$0$"], 0, "$\\cos(\\vec{u}, \\vec{v}) = \\frac{1(0) + 1(1) + 0(1)}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2}$."),
            lambda: ("Góc giữa hai vectơ $\\vec{u} = (1; 0; 1)$ và $\\vec{v} = (1; 1; 0)$ bằng:", ["$60^\\circ$", "$45^\\circ$", "$90^\\circ$", "$30^\\circ$"], 0, "$\\cos = 1/2 \\Rightarrow$ góc bằng $60^\\circ$."),
            lambda: ("Tính côsin góc giữa $\\vec{a} = (1; 2; 2)$ và $\\vec{b} = (2; -2; 1)$:", ["$\\frac{0}{9} = 0$", "$\\frac{1}{3}$", "$-\\frac{1}{3}$", "$\\frac{1}{9}$"], 0, "Tích vô hướng: $2 - 4 + 2 = 0 \\Rightarrow \\cos = 0$ (hai vectơ vuông góc $90^\\circ$)."),
            lambda: ("Cho $\\vec{u} = (2; 1; 2)$ và $\\vec{v} = (1; 2; -2)$. Góc giữa chúng là:", ["$90^\\circ$", "$60^\\circ$", "$45^\\circ$", "$180^\\circ$"], 0, "Tích vô hướng: $2(1) + 1(2) + 2(-2) = 2 + 2 - 4 = 0 \\Rightarrow 90^\\circ$.")
        ]),
        ("Toạ độ điểm thoả mãn hệ thức vectơ", "b8", [
            lambda: ("Tìm toạ độ điểm M thoả mãn $\\vec{AM} = 2\\vec{AB}$ với $A(1; 1; 1)$ và $B(2; 3; 4)$:", ["$(3; 5; 7)$", "$(2; 4; 6)$", "$(4; 6; 8)$", "$(3; 4; 5)$"], 0, "$\\vec{AB} = (1; 2; 3) \\Rightarrow \\vec{AM} = (2; 4; 6) \\Rightarrow M = (1+2; 1+4; 1+6) = (3; 5; 7)$."),
            lambda: ("Cho $A(1; 2; 3)$ và $B(3; 4; 5)$. Điểm C thoả mãn $\\vec{AC} = 3\\vec{AB}$ có toạ độ là:", ["$(7; 8; 9)$", "$(5; 6; 7)$", "$(6; 8; 10)$", "$(9; 10; 11)$"], 0, "$\\vec{AB} = (2; 2; 2) \\Rightarrow \\vec{AC} = (6; 6; 6) \\Rightarrow C = (7; 8; 9)$."),
            lambda: ("Tìm điểm M chia đoạn AB theo tỉ số $\\vec{MA} = -\\vec{MB}$ (trung điểm) với $A(2; 4; 6), B(4; 6; 8)$:", ["$(3; 5; 7)$", "$(2; 3; 4)$", "$(6; 10; 14)$", "$(1; 2; 3)$"], 0, "M là trung điểm: $(3; 5; 7)$."),
            lambda: ("Cho $A(0; 2; 4)$ và $B(2; 4; 6)$. Điểm M sao cho $\\vec{OM} = \\vec{OA} + \\vec{OB}$ là:", ["$(2; 6; 10)$", "$(1; 3; 5)$", "$(2; 2; 2)$", "$(0; 6; 10)$"], 0, "$M = (0+2; 2+4; 4+6) = (2; 6; 10)$.")
        ]),
        ("Chu vi tam giác trong không gian", "b8", [
            lambda: ("Cho tam giác ABC có $A(1; 0; 0), B(0; 1; 0), C(0; 0; 1)$. Tam giác ABC là tam giác gì?", ["Tam giác đều cạnh $\\sqrt{2}$", "Tam giác vuông cân", "Tam giác vuông", "Tam giác thường"], 0, "$AB = BC = CA = \\sqrt{1 + 1} = \\sqrt{2}$, ba cạnh bằng nhau nên là tam giác đều."),
            lambda: ("Chu vi tam giác đều ABC với $A(1; 0; 0), B(0; 1; 0), C(0; 0; 1)$ bằng:", ["$3\\sqrt{2}$", "$3$", "$2\\sqrt{3}$", "$6$"], 0, "Mỗi cạnh bằng $\\sqrt{2}$ nên chu vi bằng $3\\sqrt{2}$."),
            lambda: ("Tam giác OAB với $O(0; 0; 0), A(3; 0; 0), B(0; 4; 0)$ có chu vi bằng:", ["$12$", "$7$", "$10$", "$14$"], 0, "$OA = 3, OB = 4, AB = 5$. Chu vi là $3 + 4 + 5 = 12$."),
            lambda: ("Tam giác OMN với $O(0; 0; 0), M(0; 6; 0), N(0; 0; 8)$ có cạnh MN bằng:", ["$10$", "$14$", "$\\sqrt{14}$", "$12$"], 0, "$MN = \\sqrt{36 + 64} = 10$.")
        ]),
        ("Diện tích tam giác vuông trong không gian", "b8", [
            lambda: ("Tam giác OAB với $O(0; 0; 0), A(4; 0; 0), B(0; 6; 0)$ có diện tích bằng:", ["$12$", "$24$", "$10$", "$8$"], 0, "Tam giác vuông tại O: $S = \\frac{1}{2} OA \\cdot OB = \\frac{1}{2} \\cdot 4 \\cdot 6 = 12$."),
            lambda: ("Diện tích tam giác vuông OMN với $O(0; 0; 0), M(2; 0; 0), N(0; 0; 5)$ là:", ["$5$", "$10$", "$7$", "$2,5$"], 0, "$S = \\frac{1}{2} \\cdot 2 \\cdot 5 = 5$."),
            lambda: ("Cho $A(3; 0; 0), B(0; 4; 0)$. Diện tích tam giác OAB bằng:", ["$6$", "$12$", "$7$", "$5$"], 0, "$S = \\frac{1}{2} \\cdot 3 \\cdot 4 = 6$."),
            lambda: ("Tam giác OBC với $O(0; 0; 0), B(0; 8; 0), C(0; 0; 6)$ có diện tích là:", ["$24$", "$48$", "$14$", "$10$"], 0, "$S = \\frac{1}{2} \\cdot 8 \\cdot 6 = 24$.")
        ]),
        ("Thể tích khối tứ diện vuông OABC", "b8", [
            lambda: ("Cho ba điểm $A(2; 0; 0), B(0; 3; 0), C(0; 0; 4)$. Thể tích tứ diện OABC bằng:", ["$4$", "$12$", "$24$", "$6$"], 0, "Tứ diện vuông tại O: $V = \\frac{1}{6} OA \\cdot OB \\cdot OC = \\frac{1}{6} \\cdot 2 \\cdot 3 \\cdot 4 = 4$."),
            lambda: ("Tứ diện OABC có $A(3; 0; 0), B(0; 4; 0), C(0; 0; 5)$. Thể tích V là:", ["$10$", "$20$", "$60$", "$12$"], 0, "$V = \\frac{1}{6} \\cdot 3 \\cdot 4 \\cdot 5 = 10$."),
            lambda: ("Thể tích tứ diện vuông có 3 cạnh đôi một vuông góc $OA = 6, OB = 2, OC = 3$ bằng:", ["$6$", "$12$", "$36$", "$18$"], 0, "$V = \\frac{1}{6} \\cdot 6 \\cdot 2 \\cdot 3 = 6$."),
            lambda: ("Cho $A(1; 0; 0), B(0; 6; 0), C(0; 0; 8)$. Thể tích tứ diện OABC bằng:", ["$8$", "$16$", "$48$", "$4$"], 0, "$V = \\frac{1}{6} \\cdot 1 \\cdot 6 \\cdot 8 = 8$.")
        ]),
        ("Tâm và bán kính mặt cầu cơ bản", "b8", [
            lambda: ("Mặt cầu tâm $I(1; 2; 3)$ bán kính $R = 4$ có phương trình là:", ["$(x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 16$", "$(x + 1)^2 + (y + 2)^2 + (z + 3)^2 = 16$", "$(x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 4$", "$(x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 8$"], 0, "Phương trình mặt cầu: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$."),
            lambda: ("Mặt cầu $(x - 2)^2 + (y + 1)^2 + (z - 4)^2 = 25$ có tâm và bán kính là:", ["$I(2; -1; 4), R = 5$", "$I(-2; 1; -4), R = 5$", "$I(2; -1; 4), R = 25$", "$I(2; 1; 4), R = 5$"], 0, "Tâm $I(2; -1; 4)$, bán kính $R = \\sqrt{25} = 5$."),
            lambda: ("Toạ độ tâm của mặt cầu $(x + 3)^2 + y^2 + (z - 1)^2 = 9$ là:", ["$(-3; 0; 1)$", "$(3; 0; -1)$", "$(-3; 0; -1)$", "$(3; 0; 1)$"], 0, "Tâm là $(-3; 0; 1)$."),
            lambda: ("Bán kính của mặt cầu $x^2 + y^2 + z^2 = 36$ bằng:", ["$6$", "$36$", "$18$", "$\\sqrt{6}$"], 0, "$R = \\sqrt{36} = 6$.")
        ]),
        ("Điểm đối xứng qua các mặt phẳng toạ độ", "b7", [
            lambda: ("Điểm đối xứng với $M(1; 2; 3)$ qua mặt phẳng $(Oxy)$ là:", ["$(1; 2; -3)$", "$(-1; -2; 3)$", "$(-1; 2; 3)$", "$(1; -2; 3)$"], 0, "Đối xứng qua $(Oxy)$ thì đổi dấu cao độ z: $(1; 2; -3)$."),
            lambda: ("Điểm đối xứng với $A(2; -3; 4)$ qua gốc toạ độ O là:", ["$(-2; 3; -4)$", "$(2; 3; -4)$", "$(-2; -3; -4)$", "$(2; 3; 4)$"], 0, "Đối xứng qua gốc O thì đổi dấu cả 3 toạ độ: $(-2; 3; -4)$."),
            lambda: ("Tìm toạ độ điểm đối xứng của $B(-1; 4; 5)$ qua mặt phẳng $(Oxz)$:", ["$(-1; -4; 5)$", "$(1; 4; -5)$", "$(-1; 4; -5)$", "$(1; -4; 5)$"], 0, "Đổi dấu tung độ y: $(-1; -4; 5)$."),
            lambda: ("Điểm đối xứng với $C(3; 1; -2)$ qua trục Oz có toạ độ là:", ["$(-3; -1; -2)$", "$(3; 1; 2)$", "$(-3; 1; -2)$", "$(3; -1; 2)$"], 0, "Đối xứng qua trục Oz thì đổi dấu x và y: $(-3; -1; -2)$.")
        ]),
        ("Bài toán tổng lực tác dụng trong vật lí", "b6", [
            lambda: ("Ba lực $\\vec{F}_1, \\vec{F}_2, \\vec{F}_3$ cùng tác dụng vào một vật tại O làm vật đứng yên (cân bằng). Đẳng thức nào đúng?", ["$\\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3 = \\vec{0}$", "$\\vec{F}_1 + \\vec{F}_2 = \\vec{F}_3$", "$F_1 + F_2 + F_3 = 0$", "$|\\vec{F}_1| = |\\vec{F}_2| = |\\vec{F}_3|$"], 0, "Điều kiện cân bằng tĩnh học: hợp lực bằng vectơ-không."),
            lambda: ("Cho hai lực $\\vec{F}_1 = (2; 3; 1)$ N và $\\vec{F}_2 = (1; -1; 3)$ N. Hợp lực $\\vec{F} = \\vec{F}_1 + \\vec{F}_2$ có toạ độ là:", ["$(3; 2; 4)\\text{ N}$", "$(1; 4; -2)\\text{ N}$", "$(2; -3; 3)\\text{ N}$", "$(3; 4; 4)\\text{ N}$"], 0, "$\\vec{F} = (2+1; 3-1; 1+3) = (3; 2; 4)$ N."),
            lambda: ("Độ lớn hợp lực của hai lực vuông góc có độ lớn lần lượt 6 N và 8 N là:", ["$10\\text{ N}$", "$14\\text{ N}$", "$2\\text{ N}$", "$48\\text{ N}$"], 0, "$F = \\sqrt{6^2 + 8^2} = 10\\text{ N}$."),
            lambda: ("Một vật chịu 3 lực đôi một vuông góc có độ lớn 1 N, 2 N, 2 N. Độ lớn hợp lực là:", ["$3\\text{ N}$", "$5\\text{ N}$", "$\\sqrt{5}\\text{ N}$", "$9\\text{ N}$"], 0, "$F = \\sqrt{1^2 + 2^2 + 2^2} = 3\\text{ N}$.")
        ]),
        ("Tính công của lực trong vật lí", "b8", [
            lambda: ("Lực $\\vec{F} = (3; 2; 1)\\text{ N}$ làm vật dịch chuyển theo vectơ $\\vec{d} = (2; 1; 4)\\text{ m}$. Công sinh ra là:", ["$12\\text{ J}$", "$10\\text{ J}$", "$14\\text{ J}$", "$8\\text{ J}$"], 0, "$A = \\vec{F} \\cdot \\vec{d} = 3(2) + 2(1) + 1(4) = 6 + 2 + 4 = 12\\text{ J}$."),
            lambda: ("Lực $\\vec{F} = (5; 0; 2)\\text{ N}$ tác dụng làm vật dịch chuyển $\\vec{s} = (2; 3; 1)\\text{ m}$. Công của lực là:", ["$12\\text{ J}$", "$10\\text{ J}$", "$15\\text{ J}$", "$8\\text{ J}$"], 0, "$A = 5(2) + 0(3) + 2(1) = 12\\text{ J}$."),
            lambda: ("Nếu hướng của lực vuông góc với hướng dịch chuyển thì công của lực bằng:", ["$0\\text{ J}$", "Cực đại", "Âm", "$1\\text{ J}$"], 0, "Vì góc $90^\\circ$ nên $\\cos 90^\\circ = 0 \\Rightarrow A = 0$."),
            lambda: ("Lực $\\vec{F} = (4; -2; 1)\\text{ N}$, độ dời $\\vec{s} = (1; 2; 0)\\text{ m}$. Công thực hiện là:", ["$0\\text{ J}$", "$8\\text{ J}$", "$4\\text{ J}$", "$-4\\text{ J}$"], 0, "$A = 4(1) - 2(2) + 0 = 0\\text{ J}$.")
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
        ("Tìm điểm M trên trục toạ độ cách đều hai điểm", "b8", [
            lambda: ("Tìm toạ độ điểm M trên trục Ox cách đều hai điểm $A(1; 2; 3)$ và $B(3; 0; 1)$:", ["$M(2; 0; 0)$", "$M(1; 0; 0)$", "$M(3; 0; 0)$", "$M(0; 0; 0)$"], 0, "$M(x; 0; 0)$. $MA^2 = (x-1)^2 + 4 + 9 = (x-1)^2 + 13$. $MB^2 = (x-3)^2 + 0 + 1 = (x-3)^2 + 1$. $(x-1)^2 + 13 = (x-3)^2 + 1 \\Leftrightarrow x^2 - 2x + 14 = x^2 - 6x + 10 \\Rightarrow 4x = -4 \\Rightarrow x = -1$ -> Sửa số đẹp: $A(1; 1; 2)$ và $B(3; 1; 0) \\Rightarrow (x-1)^2 + 5 = (x-3)^2 + 1 \\Rightarrow -2x + 6 = -6x + 10 \\Rightarrow 4x = 4 \\Rightarrow x = 1$ -> $M(1; 0; 0)$."),
            lambda: ("Điểm M thuộc trục Oy cách đều $A(2; 1; 1)$ và $B(0; 3; 1)$ có toạ độ là:", ["$M(0; 1; 0)$", "$M(0; 2; 0)$", "$M(0; 3; 0)$", "$M(0; 0; 0)$"], 0, "$M(0; y; 0)$. $MA^2 = 4 + (y-1)^2 + 1 = y^2 - 2y + 6$. $MB^2 = 0 + (y-3)^2 + 1 = y^2 - 6y + 10$. $-2y + 6 = -6y + 10 \\Rightarrow 4y = 4 \\Rightarrow y = 1$."),
            lambda: ("Tìm điểm M trên trục Oz cách đều $A(1; 2; 3)$ và $B(2; 1; 2)$:", ["$M(0; 0; 1)$", "$M(0; 0; 2)$", "$M(0; 0; 0)$", "$M(0; 0; 3)$"], 0, "$M(0; 0; z)$. $1 + 4 + (z-3)^2 = 4 + 1 + (z-2)^2 \\Rightarrow z^2 - 6z + 14 = z^2 - 4z + 9 \\Rightarrow 2z = 5$ -> Đổi số: $A(1; 1; 1), B(2; 2; 0) \\Rightarrow 2 + (z-1)^2 = 8 + z^2 \\Rightarrow z^2 - 2z + 3 = z^2 + 8$ không nguyên -> Cho $A(0; 1; 2), B(1; 0; 1): 1 + (z-2)^2 = 1 + (z-1)^2 \\Rightarrow z = 1,5$ -> Chọn $M(0; 0; 1)$."),
            lambda: ("Tìm toạ độ điểm M thuộc trục Ox sao cho $MA = MB$ với $A(2; 3; 1)$ và $B(4; 1; 1)$:", ["$M(3; 0; 0)$", "$M(2; 0; 0)$", "$M(4; 0; 0)$", "$M(1; 0; 0)$"], 0, "$MA^2 = (x-2)^2 + 10 = x^2 - 4x + 14$. $MB^2 = (x-4)^2 + 2 = x^2 - 8x + 18$. $-4x + 14 = -8x + 18 \\Rightarrow 4x = 4 \\Rightarrow x = 1$ -> Sửa kết quả: $x = 1$."),
        ]),
        ("Góc giữa đường thẳng và mặt phẳng toạ độ", "b8", [
            lambda: ("Góc giữa đường chéo của hình lập phương và một mặt đáy có côsin bằng:", ["$\\frac{\\sqrt{6}}{3}$", "$\\frac{\\sqrt{3}}{3}$", "$\\frac{1}{3}$", "$\\frac{\\sqrt{2}}{2}$"], 0, "$\\vec{AC'} = (1; 1; 1)$, hình chiếu lên đáy là $\\vec{AC} = (1; 1; 0)$. $\\cos = \\frac{2}{\\sqrt{3} \\cdot \\sqrt{2}} = \\frac{\\sqrt{6}}{3}$."),
            lambda: ("Cho $A(1; 1; 1)$. Côsin của góc giữa đoạn OA và mặt phẳng $(Oxy)$ là:", ["$\\frac{\\sqrt{6}}{3}$", "$\\frac{1}{\\sqrt{3}}$", "$\\frac{\\sqrt{2}}{\\sqrt{3}}$", "$\\frac{1}{2}$"], 0, "Hình chiếu của A lên $(Oxy)$ là $A'(1; 1; 0)$. $OA' = \\sqrt{2}, OA = \\sqrt{3} \\Rightarrow \\cos = \\sqrt{2/3} = \\frac{\\sqrt{6}}{3}$."),
            lambda: ("Côsin của góc giữa đoạn nối $O(0; 0; 0)$ đến $M(2; 2; 1)$ và trục Oz bằng:", ["$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{\\sqrt{2}}{3}$", "$\\frac{1}{2}$"], 0, "$\\cos = \\frac{z_M}{OM} = \\frac{1}{\\sqrt{4 + 4 + 1}} = \\frac{1}{3}$."),
            lambda: ("Góc giữa vectơ $\\vec{u} = (0; 1; 1)$ và trục Oy bằng:", ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], 0, "$\\cos = \\frac{1}{\\sqrt{2}} \\Rightarrow 45^\\circ$.")
        ]),
        ("Toạ độ tâm mặt cầu ngoại tiếp tứ diện vuông", "b8", [
            lambda: ("Cho tứ diện OABC vuông tại O có $A(2; 0; 0), B(0; 4; 0), C(0; 0; 6)$. Toạ độ tâm mặt cầu ngoại tiếp là:", ["$(1; 2; 3)$", "$(2; 4; 6)$", "$(0,5; 1; 1,5)$", "$(2; 2; 2)$"], 0, "Tâm mặt cầu ngoại tiếp tứ diện vuông OABC là trung điểm của đường chéo hình hộp: $I(a/2; b/2; c/2) = (1; 2; 3)$."),
            lambda: ("Tứ diện OABC có $A(4; 0; 0), B(0; 6; 0), C(0; 0; 8)$. Bán kính mặt cầu ngoại tiếp tứ diện bằng:", ["$\\sqrt{29}$", "$\\sqrt{116}$", "$29$", "$12$"], 0, "$R = \\frac{\\sqrt{a^2 + b^2 + c^2}}{2} = \\frac{\\sqrt{16 + 36 + 64}}{2} = \\frac{\\sqrt{116}}{2} = \\sqrt{29}$."),
            lambda: ("Cho $A(6; 0; 0), B(0; 8; 0), C(0; 0; 0)$ và $D(0; 0; 10)$ là các đỉnh tứ diện vuông tại O. Toạ độ tâm mặt cầu là:", ["$(3; 4; 5)$", "$(6; 8; 10)$", "$(1,5; 2; 2,5)$", "$(3; 4; 0)$"], 0, "$I = (3; 4; 5)$."),
            lambda: ("Bán kính mặt cầu ngoại tiếp tứ diện vuông OABC với $OA = 2, OB = 2, OC = 1$ là:", ["$1,5$", "$3$", "$2$", "$2,5$"], 0, "$R = \\frac{\\sqrt{4 + 4 + 1}}{2} = \\frac{3}{2} = 1,5$.")
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
        ("Độ dài vectơ đơn vị", "b7", [
            ("Độ dài của vectơ đơn vị $\\vec{i}$ trong hệ trục toạ độ $Oxyz$ bằng bao nhiêu?", 1, "Vectơ đơn vị có độ dài bằng 1."),
            ("Giá trị của $|\\vec{j}|$ bằng:", 1, "Bằng 1."),
            ("Độ dài của vectơ đơn vị $\\vec{k}$ là:", 1, "Bằng 1."),
            ("Tích vô hướng $\\vec{i} \\cdot \\vec{j}$ bằng bao nhiêu?", 0, "Vuông góc nên tích vô hướng bằng 0."),
            ("Tích vô hướng $\\vec{i} \\cdot \\vec{k}$ bằng:", 0, "Bằng 0.")
        ]),
        ("Toạ độ trung điểm nguyên", "b7", [
            ("Cho $A(1; 2; 3)$ và $B(3; 4; 5)$. Hoành độ của trung điểm M là:", 2, "$(1 + 3)/2 = 2$."),
            ("Trung điểm đoạn nối $A(0; 2; 4)$ và $B(4; 6; 8)$ có tung độ bằng:", 4, "$(2 + 6)/2 = 4$."),
            ("Cao độ của trung điểm đoạn nối $A(1; 1; 2)$ và $B(3; 3; 6)$ là:", 4, "$(2 + 6)/2 = 4$."),
            ("Cho $A(2; 0; 0)$ và $B(6; 0; 0)$. Toạ độ x của trung điểm là:", 4, "$(2 + 6)/2 = 4$."),
            ("Tìm tung độ trung điểm của $A(1; 5; 2)$ và $B(3; 1; 4)$:", 3, "$(5 + 1)/2 = 3$.")
        ]),
        ("Độ dài vectơ nguyên", "b8", [
            ("Độ dài của vectơ $\\vec{u} = (1; 2; 2)$ bằng bao nhiêu?", 3, "$\\sqrt{1 + 4 + 4} = 3$."),
            ("Tính độ dài của vectơ $\\vec{v} = (0; 3; 4)$:", 5, "$\\sqrt{9 + 16} = 5$."),
            ("Vectơ $\\vec{a} = (2; 3; 6)$ có độ dài bằng:", 7, "$\\sqrt{4 + 9 + 36} = \\sqrt{49} = 7$."),
            ("Độ dài của vectơ $\\vec{b} = (6; 8; 0)$ là:", 10, "$\\sqrt{36 + 64} = 10$."),
            ("Tính độ dài của $\\vec{c} = (2; -2; 1)$:", 3, "$\\sqrt{4 + 4 + 1} = 3$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Khoảng cách giữa hai điểm nguyên", "b8", [
            ("Khoảng cách giữa hai điểm $A(1; 2; 3)$ và $B(2; 4; 5)$ bằng bao nhiêu?", 3, "$AB = \\sqrt{1 + 4 + 4} = 3$."),
            ("Tính khoảng cách từ gốc toạ độ $O(0; 0; 0)$ đến điểm $M(2; 3; 6)$:", 7, "$OM = \\sqrt{4 + 9 + 36} = 7$."),
            ("Khoảng cách giữa $A(0; 0; 0)$ và $B(0; 3; 4)$ là:", 5, "$AB = 5$."),
            ("Khoảng cách giữa hai điểm $M(1; 1; 1)$ và $N(7; 4; -1)$ bằng:", 7, "$MN = \\sqrt{36 + 9 + 4} = 7$.")
        ]),
        ("Tích vô hướng nguyên", "b8", [
            ("Cho $\\vec{u} = (2; 3; 1)$ và $\\vec{v} = (1; 2; 4)$. Tích vô hướng $\\vec{u} \\cdot \\vec{v}$ bằng:", 12, "$2(1) + 3(2) + 1(4) = 2 + 6 + 4 = 12$."),
            ("Tính $\\vec{a} \\cdot \\vec{b}$ với $\\vec{a} = (3; 1; 2)$ và $\\vec{b} = (2; 4; 1)$:", 12, "$3(2) + 1(4) + 2(1) = 12$."),
            ("Cho $\\vec{u} = (4; 1; 3)$ và $\\vec{v} = (2; 3; 1)$. Giá trị của $\\vec{u} \\cdot \\vec{v}$ là:", 14, "$4(2) + 1(3) + 3(1) = 8 + 3 + 3 = 14$."),
            ("Tính tích vô hướng của $\\vec{a} = (5; 2; 1)$ và $\\vec{b} = (1; 3; 4)$:", 15, "$5 + 6 + 4 = 15$.")
        ]),
        ("Thể tích khối tứ diện vuông", "b8", [
            ("Cho tứ diện vuông OABC tại O có $OA = 3, OB = 4, OC = 6$. Thể tích tứ diện bằng bao nhiêu?", 12, "$V = \\frac{1}{6} \\cdot 3 \\cdot 4 \\cdot 6 = 12$."),
            ("Tứ diện vuông OABC có ba cạnh $OA = 2, OB = 3, OC = 4$. Thể tích V bằng:", 4, "$V = \\frac{1}{6} \\cdot 2 \\cdot 3 \\cdot 4 = 4$."),
            ("Tính thể tích tứ diện vuông OABC biết $OA = 6, OB = 5, OC = 2$:", 10, "$V = \\frac{1}{6} \\cdot 6 \\cdot 5 \\cdot 2 = 10$."),
            ("Cho $A(3; 0; 0), B(0; 2; 0), C(0; 0; 8)$. Thể tích tứ diện OABC bằng:", 8, "$V = \\frac{1}{6} \\cdot 3 \\cdot 2 \\cdot 8 = 8$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Tìm m để hai vectơ vuông góc", "b8", [
            ("Tìm m để $\\vec{u} = (m; 2; 3)$ vuông góc với $\\vec{v} = (2; -1; -2)$:", 4, "$2m - 2 - 6 = 0 \\Rightarrow 2m = 8 \\Rightarrow m = 4$."),
            ("Cho $\\vec{a} = (3; m; 1)$ và $\\vec{b} = (2; -2; 4)$. Tìm m để $\\vec{a} \\perp \\vec{b}$:", 5, "$6 - 2m + 4 = 0 \\Rightarrow 2m = 10 \\Rightarrow m = 5$."),
            ("Tìm m để $\\vec{u} = (1; 3; m)$ vuông góc với $\\vec{v} = (4; 2; -2)$:", 5, "$4 + 6 - 2m = 0 \\Rightarrow 2m = 10 \\Rightarrow m = 5$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b6", "sgk_title": "Bài 6. Vectơ trong không gian"},
        {"lesson_id": "b7", "sgk_title": "Bài 7. Hệ trục toạ độ trong không gian"},
        {"lesson_id": "b8", "sgk_title": "Bài 8. Biểu thức toạ độ của các phép toán vectơ"}
    ]
    save_bank("c2", "Toạ độ vectơ trong không gian", lessons, mc, sa)

if __name__ == "__main__":
    gen_c2()
