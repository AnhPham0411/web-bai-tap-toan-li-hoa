# -*- coding: utf-8 -*-
"""Toán 10 - Chương IV: Vectơ."""
import math
from fractions import Fraction
from .common import Bank, M, frac, rad, fnum

B7, B8, B9, B10, B11 = 'b7', 'b8', 'b9', 'b10', 'b11'

def V(x, y): return f"({x}; {y})"
def vec(n): return f"\\vec{{{n}}}"

def build():
    b = Bank('toan10', 'c4')

    # ===== Bài 7: khái niệm mở đầu (lý thuyết) =====
    b.mc(B7, 'nb', 'Khái niệm vectơ', "Vectơ là một đoạn thẳng:", "Có hướng (đã chỉ rõ điểm đầu và điểm cuối)",
         ["Không phân biệt điểm đầu và điểm cuối", "Có độ dài bằng $1$", "Luôn nằm trên trục hoành"],
         "Theo định nghĩa, vectơ là đoạn thẳng có hướng: trong hai đầu mút, một điểm được chỉ rõ là điểm đầu, điểm kia là điểm cuối.")
    b.mc(B7, 'nb', 'Độ dài vectơ', f"Cho hình vuông $ABCD$ cạnh $a$. Độ dài vectơ ${vec('AC')}$ bằng:", M('a\\sqrt{2}'), [M('a'), M('2a'), M('\\frac{a\\sqrt{2}}{2}')],
         "Độ dài vectơ $\\vec{AC}$ là độ dài đoạn $AC$, chính là đường chéo hình vuông cạnh $a$ nên $AC=a\\sqrt{2}$.")
    b.mc(B7, 'nb', 'Vectơ-không', "Khẳng định nào sau đây về vectơ-không là đúng?", "Vectơ-không có độ dài bằng $0$ và cùng phương với mọi vectơ",
         ["Vectơ-không có độ dài bằng $1$", "Vectơ-không không cùng phương với vectơ nào", "Vectơ-không có hướng từ trái sang phải"],
         "Vectơ-không có điểm đầu trùng điểm cuối, độ dài bằng $0$, và quy ước là cùng phương, cùng hướng với mọi vectơ.")
    b.mc(B7, 'th', 'Hai vectơ bằng nhau', f"Cho hình bình hành $ABCD$. Vectơ nào sau đây bằng ${vec('AB')}$?", M(vec('DC')), [M(vec('CD')), M(vec('BA')), M(vec('AD'))],
         "Trong hình bình hành $ABCD$, $AB$ và $DC$ song song, bằng nhau và cùng hướng nên $\\vec{AB}=\\vec{DC}$. Còn $\\vec{CD}$ ngược hướng với $\\vec{AB}$.")
    b.mc(B7, 'th', 'Hai vectơ đối nhau', f"Khẳng định nào sau đây đúng với mọi điểm $A$, $B$?", M(f"{vec('AB')} \\text{{ và }} {vec('BA')} \\text{{ là hai vectơ đối nhau}}"),
         [M(f"{vec('AB')}={vec('BA')}"), M(f"|{vec('AB')}|\\ne|{vec('BA')}|"), M(f"{vec('AB')} \\text{{ và }} {vec('BA')} \\text{{ cùng hướng}}")],
         "Hai vectơ $\\vec{AB}$ và $\\vec{BA}$ có cùng độ dài và ngược hướng nên là hai vectơ đối nhau, tức $\\vec{BA}=-\\vec{AB}$.")

    # ===== Bài 8: tổng và hiệu =====
    b.mc(B8, 'nb', 'Quy tắc ba điểm', "Với ba điểm $A$, $B$, $C$ bất kì, đẳng thức nào sau đây đúng?", M(f"{vec('AB')}+{vec('BC')}={vec('AC')}"),
         [M(f"{vec('AB')}+{vec('BC')}={vec('CA')}"), M(f"{vec('AB')}+{vec('AC')}={vec('BC')}"), M(f"{vec('AB')}-{vec('BC')}={vec('AC')}")],
         "Quy tắc ba điểm: điểm cuối của vectơ thứ nhất trùng điểm đầu của vectơ thứ hai thì $\\vec{AB}+\\vec{BC}=\\vec{AC}$.")
    b.mc(B8, 'nb', 'Quy tắc hiệu', "Với ba điểm $A$, $B$, $C$ bất kì, đẳng thức nào sau đây đúng?", M(f"{vec('AB')}-{vec('AC')}={vec('CB')}"),
         [M(f"{vec('AB')}-{vec('AC')}={vec('BC')}"), M(f"{vec('AB')}-{vec('AC')}={vec('BA')}"), M(f"{vec('AB')}-{vec('AC')}={vec('AC')}")],
         "Ta có $\\vec{AB}-\\vec{AC}=\\vec{AB}+\\vec{CA}=\\vec{CA}+\\vec{AB}=\\vec{CB}$ (quy tắc ba điểm).")
    b.mc(B8, 'nb', 'Quy tắc hình bình hành', "Cho hình bình hành $ABCD$. Đẳng thức nào sau đây đúng?", M(f"{vec('AB')}+{vec('AD')}={vec('AC')}"),
         [M(f"{vec('AB')}+{vec('AD')}={vec('BD')}"), M(f"{vec('AB')}+{vec('AD')}={vec('DB')}"), M(f"{vec('AB')}+{vec('AD')}={vec('CA')}")],
         "Quy tắc hình bình hành: nếu $ABCD$ là hình bình hành thì $\\vec{AB}+\\vec{AD}=\\vec{AC}$ ($AC$ là đường chéo xuất phát từ $A$).")
    b.mc(B8, 'th', 'Trung điểm', "Điểm $I$ là trung điểm của đoạn $AB$ khi và chỉ khi:", M(f"{vec('IA')}+{vec('IB')}={vec('0')}"),
         [M(f"{vec('IA')}={vec('IB')}"), M(f"{vec('AI')}+{vec('IB')}={vec('0')}"), M(f"{vec('IA')}-{vec('IB')}={vec('0')}")],
         "$I$ là trung điểm $AB$ khi $\\vec{IA}$ và $\\vec{IB}$ là hai vectơ đối nhau, tức $\\vec{IA}+\\vec{IB}=\\vec{0}$.")
    b.mc(B8, 'th', 'Trọng tâm', "Điểm $G$ là trọng tâm tam giác $ABC$ khi và chỉ khi:", M(f"{vec('GA')}+{vec('GB')}+{vec('GC')}={vec('0')}"),
         [M(f"{vec('GA')}={vec('GB')}+{vec('GC')}"), M(f"{vec('AG')}+{vec('BG')}+{vec('CG')}=3{vec('0')}\\text{{ và }}G\\notin(ABC)"), M(f"{vec('GA')}+{vec('GB')}=3{vec('GC')}")],
         "Với trọng tâm $G$ của tam giác $ABC$ ta có hệ thức quen thuộc $\\vec{GA}+\\vec{GB}+\\vec{GC}=\\vec{0}$ và ngược lại.")
    b.mc(B8, 'th', 'Độ dài tổng hai vectơ', "Cho tam giác $ABC$ đều cạnh $a$. Độ dài vectơ $\\vec{AB}+\\vec{AC}$ bằng:", M('a\\sqrt{3}'), [M('2a'), M('a'), M('\\frac{a\\sqrt{3}}{2}')],
         "Gọi $M$ là trung điểm $BC$ thì $\\vec{AB}+\\vec{AC}=2\\vec{AM}$. Đường trung tuyến $AM=\\frac{a\\sqrt{3}}{2}$ nên độ dài là $2\\cdot\\frac{a\\sqrt{3}}{2}=a\\sqrt{3}$.")
    b.mc(B8, 'th', 'Độ dài hiệu hai vectơ', "Cho hình vuông $ABCD$ cạnh $a$. Độ dài vectơ $\\vec{AB}-\\vec{AD}$ bằng:", M('a\\sqrt{2}'), [M('a'), M('2a'), M('0')],
         "Ta có $\\vec{AB}-\\vec{AD}=\\vec{DB}$ nên độ dài là $DB=a\\sqrt{2}$ (đường chéo hình vuông).")

    # ===== Bài 9: tích với một số =====
    for k in (2, 3, -2, -3):
        a_ = (3, -4)
        r = (k * a_[0], k * a_[1])
        b.mc(B9, 'nb', 'Tích vectơ với một số (toạ độ)', f"Cho $\\vec{{a}}={V(*a_)}$. Toạ độ của vectơ ${k}\\vec{{a}}$ là:", M(V(*r)),
             [M(V(a_[0] + k, a_[1] + k)), M(V(k * a_[1], k * a_[0])), M(V(r[0], -r[1]))],
             f"Nhân từng toạ độ với ${k}$: ${k}\\vec{{a}}=({k}\\cdot{a_[0]};\\ {k}\\cdot({a_[1]}))={V(*r)}$.")
    b.mc(B9, 'th', 'Trung điểm và tích với số', "Cho $I$ là trung điểm đoạn $AB$. Với mọi điểm $M$, đẳng thức nào sau đây đúng?", M(f"{vec('MA')}+{vec('MB')}=2{vec('MI')}"),
         [M(f"{vec('MA')}+{vec('MB')}={vec('MI')}"), M(f"{vec('MA')}-{vec('MB')}=2{vec('MI')}"), M(f"{vec('MA')}+{vec('MB')}=\\frac{{1}}{{2}}{vec('MI')}")],
         "Vì $\\vec{IA}+\\vec{IB}=\\vec{0}$ nên $\\vec{MA}+\\vec{MB}=(\\vec{MI}+\\vec{IA})+(\\vec{MI}+\\vec{IB})=2\\vec{MI}$.")
    b.mc(B9, 'th', 'Hai vectơ cùng phương', "Hai vectơ $\\vec{a}$ và $\\vec{b}\\ (\\vec{b}\\ne\\vec{0})$ cùng phương khi và chỉ khi:", M('\\text{có số } k \\text{ để } \\vec{a}=k\\vec{b}'),
         [M("\\vec{a}\\cdot\\vec{b}=0"), M("|\\vec{a}|=|\\vec{b}|"), M("\\vec{a}+\\vec{b}=\\vec{0}")],
         "Điều kiện cần và đủ để $\\vec{a}$ cùng phương với $\\vec{b}\\ne\\vec{0}$ là tồn tại số $k$ sao cho $\\vec{a}=k\\vec{b}$.")
    for (m_, n_, tgt) in ((3, 2, 6), (4, 5, 20)):
        pass

    # ===== Bài 10: toạ độ =====
    # toạ độ vectơ AB
    for (A, B_) in (((1, 2), (4, 6)), ((-2, 3), (1, -1)), ((0, 5), (-3, 2)), ((2, -1), (-4, -4)), ((3, 3), (7, 0))):
        r = (B_[0] - A[0], B_[1] - A[1])
        b.mc(B10, 'nb', 'Toạ độ vectơ AB', f"Cho $A{V(*A)}$ và $B{V(*B_)}$. Toạ độ vectơ ${vec('AB')}$ là:", M(V(*r)),
             [M(V(-r[0], -r[1])), M(V(A[0] + B_[0], A[1] + B_[1])), M(V(r[1], r[0])), M(V(r[0], r[1] + 1)), M(V(r[0] - 1, r[1] + 2))],
             f"$\\vec{{AB}}=(x_B-x_A;\\ y_B-y_A)=({B_[0]}-({A[0]});\\ {B_[1]}-({A[1]}))={V(*r)}$.")
        b.sa(B10, 'nb', 'Toạ độ vectơ AB', f"Cho $A{V(*A)}$ và $B{V(*B_)}$. Tính hoành độ của vectơ ${vec('AB')}$.", r[0],
             f"Hoành độ của $\\vec{{AB}}$ là $x_B-x_A={B_[0]}-({A[0]})={r[0]}$.")
    # trung điểm
    for (A, B_) in (((2, 4), (6, 8)), ((-1, 3), (5, -1)), ((0, 0), (4, -6)), ((3, -2), (-5, 4))):
        mid = (Fraction(A[0] + B_[0], 2), Fraction(A[1] + B_[1], 2))
        b.mc(B10, 'nb', 'Toạ độ trung điểm', f"Cho $A{V(*A)}$, $B{V(*B_)}$. Toạ độ trung điểm $I$ của $AB$ là:", M(V(frac(mid[0]), frac(mid[1]))),
             [M(V(frac(Fraction(A[0] - B_[0], 2)), frac(Fraction(A[1] - B_[1], 2)))), M(V(A[0] + B_[0], A[1] + B_[1])), M(V(frac(Fraction(B_[0] - A[0], 2)), frac(Fraction(B_[1] - A[1], 2)))), M(V(frac(mid[0] + 1), frac(mid[1]))), M(V(frac(mid[0]), frac(mid[1] - 1)))],
             f"$I\\left(\\frac{{x_A+x_B}}{{2}};\\ \\frac{{y_A+y_B}}{{2}}\\right)=\\left(\\frac{{{A[0]}+({B_[0]})}}{{2}};\\ \\frac{{{A[1]}+({B_[1]})}}{{2}}\\right)={V(frac(mid[0]), frac(mid[1]))}$.")
    # trọng tâm
    for (A, B_, C) in (((1, 2), (4, 5), (7, 2)), ((0, 0), (6, 3), (3, 9)), ((-3, 1), (0, 4), (6, -2))):
        g = (Fraction(A[0] + B_[0] + C[0], 3), Fraction(A[1] + B_[1] + C[1], 3))
        b.mc(B10, 'th', 'Toạ độ trọng tâm', f"Cho tam giác $ABC$ với $A{V(*A)}$, $B{V(*B_)}$, $C{V(*C)}$. Toạ độ trọng tâm $G$ là:", M(V(frac(g[0]), frac(g[1]))),
             [M(V(frac(Fraction(A[0] + B_[0] + C[0], 2)), frac(Fraction(A[1] + B_[1] + C[1], 2)))), M(V(A[0] + B_[0] + C[0], A[1] + B_[1] + C[1])), M(V(frac(Fraction(A[0] + B_[0] + C[0], 3) + 1), frac(g[1])))],
             f"$G\\left(\\frac{{x_A+x_B+x_C}}{{3}};\\ \\frac{{y_A+y_B+y_C}}{{3}}\\right)=\\left(\\frac{{{A[0]+B_[0]+C[0]}}}{{3}};\\ \\frac{{{A[1]+B_[1]+C[1]}}}{{3}}\\right)={V(frac(g[0]), frac(g[1]))}$.")
        b.sa(B10, 'th', 'Toạ độ trọng tâm', f"Tam giác $ABC$ có $A{V(*A)}$, $B{V(*B_)}$, $C{V(*C)}$. Tổng hoành độ và tung độ của trọng tâm $G$ bằng bao nhiêu (làm tròn đến hàng phần trăm)?", float(g[0] + g[1]),
             f"$G=\\left(\\frac{{{A[0]+B_[0]+C[0]}}}{{3}};\\ \\frac{{{A[1]+B_[1]+C[1]}}}{{3}}\\right)$, tổng hai toạ độ là ${fnum(float(g[0]+g[1]))}$.", tol=0.01)
    # hình bình hành: tìm D
    for (A, B_, C) in (((1, 2), (3, 1), (5, 4)), ((0, 0), (4, 1), (6, 5)), ((-1, 3), (2, 0), (5, 2))):
        D = (A[0] + C[0] - B_[0], A[1] + C[1] - B_[1])
        b.mc(B10, 'th', 'Hình bình hành: tìm đỉnh còn lại', f"Cho ba điểm $A{V(*A)}$, $B{V(*B_)}$, $C{V(*C)}$. Tìm toạ độ điểm $D$ để $ABCD$ là hình bình hành.", M(V(*D)),
             [M(V(B_[0] + C[0] - A[0], B_[1] + C[1] - A[1])), M(V(A[0] + B_[0] - C[0], A[1] + B_[1] - C[1])), M(V(A[0] + B_[0] + C[0], A[1] + B_[1] + C[1])), M(V(D[0] + 1, D[1])), M(V(D[0], D[1] - 1))],
             f"$ABCD$ là hình bình hành nên $\\vec{{AB}}=\\vec{{DC}}$, suy ra $D=A+C-B=({A[0]}+{C[0]}-({B_[0]});\\ {A[1]}+{C[1]}-({B_[1]}))={V(*D)}$.")
        b.sa(B10, 'th', 'Hình bình hành: tìm đỉnh còn lại', f"Cho $A{V(*A)}$, $B{V(*B_)}$, $C{V(*C)}$ và $ABCD$ là hình bình hành. Tính hoành độ của điểm $D$.", D[0],
             f"Từ $\\vec{{AB}}=\\vec{{DC}}$ ta có $x_D=x_A+x_C-x_B={A[0]}+{C[0]}-({B_[0]})={D[0]}$.")
    # độ dài vectơ
    for (x, y, L, expr) in ((3, 4, 5, '5'), (5, 12, 13, '13'), (1, 1, math.sqrt(2), '\\sqrt{2}'), (2, -2, 2 * math.sqrt(2), '2\\sqrt{2}'), (6, 8, 10, '10'), (-1, 2, math.sqrt(5), '\\sqrt{5}')):
        b.mc(B10, 'nb', 'Độ dài vectơ', f"Cho $\\vec{{a}}={V(x, y)}$. Độ dài $|\\vec{{a}}|$ bằng:", M(expr),
             [M(str(abs(x) + abs(y))), M(rad(abs(x) ** 2 - y * y if abs(x) != abs(y) else 7)) if abs(x) != abs(y) and x * x - y * y > 0 else M('\\sqrt{7}'), M(str(x * x + y * y)), M('1')] ,
             f"$|\\vec{{a}}|=\\sqrt{{x^2+y^2}}=\\sqrt{{{x*x}+{y*y}}}=\\sqrt{{{x*x+y*y}}}={expr}$.")
        b.sa(B10, 'nb', 'Độ dài vectơ', f"Cho $\\vec{{a}}={V(x, y)}$. Tính $|\\vec{{a}}|$ (làm tròn đến hàng phần trăm).", L,
             f"$|\\vec{{a}}|=\\sqrt{{{x*x}+{y*y}}}=\\sqrt{{{x*x+y*y}}}\\approx {fnum(L)}$.", tol=0.01)
    # cộng, trừ vectơ theo toạ độ
    for (a_, b_) in (((1, 2), (3, -1)), ((2, 0), (-1, 4)), ((-3, 5), (2, 2))):
        s = (a_[0] + b_[0], a_[1] + b_[1]); d = (a_[0] - b_[0], a_[1] - b_[1])
        b.mc(B10, 'nb', 'Tổng hai vectơ (toạ độ)', f"Cho $\\vec{{a}}={V(*a_)}$, $\\vec{{b}}={V(*b_)}$. Toạ độ của $\\vec{{a}}+\\vec{{b}}$ là:", M(V(*s)),
             [M(V(*d)), M(V(a_[0] * b_[0], a_[1] * b_[1])), M(V(s[1], s[0]))],
             f"Cộng các toạ độ tương ứng: $({a_[0]}+({b_[0]});\\ {a_[1]}+({b_[1]}))={V(*s)}$.")
        c2 = (2 * a_[0] - b_[0], 2 * a_[1] - b_[1])
        b.mc(B10, 'th', 'Biểu thức vectơ theo toạ độ', f"Cho $\\vec{{a}}={V(*a_)}$, $\\vec{{b}}={V(*b_)}$. Toạ độ của $2\\vec{{a}}-\\vec{{b}}$ là:", M(V(*c2)),
             [M(V(2 * a_[0] + b_[0], 2 * a_[1] + b_[1])), M(V(a_[0] - 2 * b_[0], a_[1] - 2 * b_[1])), M(V(2 * (a_[0] - b_[0]), a_[1] - b_[1]))],
             f"$2\\vec{{a}}={V(2*a_[0], 2*a_[1])}$ nên $2\\vec{{a}}-\\vec{{b}}=({2*a_[0]}-({b_[0]});\\ {2*a_[1]}-({b_[1]}))={V(*c2)}$.")
    # cùng phương: tìm m
    for (a_, y_, bx) in (((1, 2), 6, None), ((2, 3), 9, None), ((3, -1), 4, None)):
        # b = (m, y_), cùng phương a: m*a_[1] = a_[0]*y_  -> m = a_[0]*y_/a_[1]
        m = Fraction(a_[0] * y_, a_[1])
        b.mc(B9, 'th', 'Điều kiện cùng phương', f"Cho $\\vec{{a}}={V(*a_)}$ và $\\vec{{b}}=(m;\\ {y_})$. Giá trị của $m$ để hai vectơ cùng phương là:", M(frac(m)),
             [M(frac(-m)), M(frac(Fraction(y_ * a_[1], a_[0]) if a_[0] else 1)), M(frac(m + 1))],
             f"Hai vectơ cùng phương khi $\\frac{{m}}{{{a_[0]}}}=\\frac{{{y_}}}{{{a_[1]}}}$, tức $m\\cdot{a_[1]}={a_[0]}\\cdot{y_}$ nên $m={frac(m)}$.")
        b.sa(B9, 'th', 'Điều kiện cùng phương', f"Cho $\\vec{{a}}={V(*a_)}$ và $\\vec{{b}}=(m;\\ {y_})$. Tìm $m$ để hai vectơ cùng phương (làm tròn đến hàng phần trăm).", float(m),
             f"Cùng phương khi $m\\cdot{a_[1]}={a_[0]}\\cdot{y_}$, suy ra $m={fnum(float(m))}$.", tol=0.01)

    # ===== Bài 11: tích vô hướng =====
    for (u, v, ang, val) in ((3, 4, 60, 6), (3, 4, 120, -6), (2, 5, 90, 0), (4, 6, 60, 12), (5, 2, 180, -10), (6, 3, 0, 18)):
        c = {60: 0.5, 120: -0.5, 90: 0, 180: -1, 0: 1}[ang]
        assert abs(u * v * c - val) < 1e-9
        b.mc(B11, 'th', 'Tích vô hướng theo định nghĩa', f"Cho hai vectơ $\\vec{{a}}$, $\\vec{{b}}$ có $|\\vec{{a}}|={u}$, $|\\vec{{b}}|={v}$ và góc giữa chúng bằng ${ang}^\\circ$. Tích vô hướng $\\vec{{a}}\\cdot\\vec{{b}}$ bằng:", M(str(val)),
             [M(str(u * v)), M(str(-val if val else u + v)), M(str(val + u)), M(str(val + 3)), M(str(val - 4)), M(str(val * 2 + 1))],
             f"$\\vec{{a}}\\cdot\\vec{{b}}=|\\vec{{a}}||\\vec{{b}}|\\cos(\\vec{{a}},\\vec{{b}})={u}\\cdot{v}\\cdot\\cos {ang}^\\circ={val}$.")
        b.sa(B11, 'th', 'Tích vô hướng theo định nghĩa', f"Cho $|\\vec{{a}}|={u}$, $|\\vec{{b}}|={v}$ và góc giữa hai vectơ là ${ang}^\\circ$. Tính $\\vec{{a}}\\cdot\\vec{{b}}$.", val,
             f"$\\vec{{a}}\\cdot\\vec{{b}}=|\\vec{{a}}||\\vec{{b}}|\\cos {ang}^\\circ={u}\\cdot{v}\\cdot{fnum(c)}={val}$.")
    for (a_, b_) in (((1, 2), (3, -1)), ((2, 3), (4, -2)), ((-1, 4), (5, 2)), ((3, 0), (0, 7))):
        dot = a_[0] * b_[0] + a_[1] * b_[1]
        b.mc(B11, 'nb', 'Tích vô hướng theo toạ độ', f"Cho $\\vec{{a}}={V(*a_)}$, $\\vec{{b}}={V(*b_)}$. Tích vô hướng $\\vec{{a}}\\cdot\\vec{{b}}$ bằng:", M(str(dot)),
             [M(str(a_[0] * b_[1] + a_[1] * b_[0])), M(str(a_[0] * b_[0] - a_[1] * b_[1])), M(str(dot + 2)), M(str(dot + 1)), M(str(dot - 3)), M(str(dot * 2 + 5))],
             f"$\\vec{{a}}\\cdot\\vec{{b}}=x_1x_2+y_1y_2={a_[0]}\\cdot({b_[0]})+({a_[1]})\\cdot({b_[1]})={dot}$.")
        b.sa(B11, 'nb', 'Tích vô hướng theo toạ độ', f"Cho $\\vec{{a}}={V(*a_)}$, $\\vec{{b}}={V(*b_)}$. Tính $\\vec{{a}}\\cdot\\vec{{b}}$.", dot,
             f"$\\vec{{a}}\\cdot\\vec{{b}}=({a_[0]})({b_[0]})+({a_[1]})({b_[1]})={dot}$.")
    # vuông góc: tìm m
    for (k_, p_, q_) in ((3, 2, -4), (6, 3, -2), (4, 2, -1), (2, 5, -10)):
        # a=(m,k_), b=(p_,q_): m*p_ + k_*q_ = 0 -> m = -k_*q_/p_
        m = Fraction(-k_ * q_, p_)
        b.mc(B11, 'vd', 'Hai vectơ vuông góc', f"Cho $\\vec{{a}}=(m;\\ {k_})$ và $\\vec{{b}}={V(p_, q_)}$. Giá trị của $m$ để $\\vec{{a}}\\perp\\vec{{b}}$ là:", M(frac(m)),
             [M(frac(-m)), M(frac(Fraction(k_ * p_, -q_) if q_ else 1) if False else frac(Fraction(p_, k_))), M(frac(m + 2))],
             f"$\\vec{{a}}\\perp\\vec{{b}}\\iff\\vec{{a}}\\cdot\\vec{{b}}=0\\iff {p_}m+{k_}\\cdot({q_})=0\\iff m={frac(m)}$.")
        b.sa(B11, 'vd', 'Hai vectơ vuông góc', f"Cho $\\vec{{a}}=(m;\\ {k_})$ và $\\vec{{b}}={V(p_, q_)}$. Tìm $m$ để $\\vec{{a}}\\perp\\vec{{b}}$ (làm tròn đến hàng phần trăm).", float(m),
             f"$\\vec{{a}}\\cdot\\vec{{b}}=0\\iff {p_}m+{k_}\\cdot({q_})=0$, suy ra $m={fnum(float(m))}$.", tol=0.01)
    # góc giữa hai vectơ
    for (a_, b_, ang) in (((1, 0), (1, 1), 45), ((1, 1), (-1, 1), 90), ((1, 2), (2, 4), 0), ((1, 2), (-2, -4), 180)):
        dot = a_[0] * b_[0] + a_[1] * b_[1]
        na = math.hypot(*a_); nb_ = math.hypot(*b_)
        assert abs(math.degrees(math.acos(max(-1, min(1, dot / (na * nb_))))) - ang) < 1e-3
        b.mc(B11, 'vd', 'Góc giữa hai vectơ', f"Cho $\\vec{{a}}={V(*a_)}$, $\\vec{{b}}={V(*b_)}$. Góc giữa hai vectơ bằng:", M(f"{ang}^\\circ"),
             [M(f"{x}^\\circ") for x in (30, 60, 135, 90, 45, 0, 180) if x != ang][:3],
             f"$\\cos(\\vec a,\\vec b)=\\frac{{\\vec a\\cdot\\vec b}}{{|\\vec a||\\vec b|}}=\\frac{{{dot}}}{{{rad(a_[0]**2+a_[1]**2)}\\cdot{rad(b_[0]**2+b_[1]**2)}}}={fnum(math.cos(math.radians(ang)))}$, suy ra góc bằng ${ang}^\\circ$ (góc nhận giá trị trong $[0^\\circ;180^\\circ]$).")
    return b
