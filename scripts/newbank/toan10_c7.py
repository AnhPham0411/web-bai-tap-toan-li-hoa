# -*- coding: utf-8 -*-
"""Toán 10 - Chương VII: Phương pháp toạ độ trong mặt phẳng (tự kiểm bằng code)."""
import math
from fractions import Fraction
from math import gcd
from .common import Bank, M, frac, fnum, lin, rad

B19, B20, B21, B22 = 'b19', 'b20', 'b21', 'b22'

def P(x, y): return f"({x}; {y})"
def vec(n): return f"\\vec{{{n}}}"
def parallel(u, v): return u[0] * v[1] - u[1] * v[0] == 0
def norm_line(A, B, C):
    g = gcd(gcd(abs(A), abs(B)), abs(C)) or 1
    A, B, C = A // g, B // g, C // g
    if A < 0 or (A == 0 and B < 0): A, B, C = -A, -B, -C
    return A, B, C
def L(A, B, C):
    """Chuỗi LaTeX 'Ax + By + C = 0' đã chuẩn hoá."""
    A, B, C = norm_line(A, B, C)
    return f"{lin(A, B)}{'' if C == 0 else (' + ' if C > 0 else ' - ') + str(abs(C))} = 0"
def L_raw(A, B, C):
    return f"{lin(A, B)}{'' if C == 0 else (' + ' if C > 0 else ' - ') + str(abs(C))} = 0"

def build():
    b = Bank('toan10', 'c7')

    # ===== Bài 19: phương trình đường thẳng =====
    lines = [(2, -3, 1), (3, 4, -5), (1, 2, -4), (5, -1, 2), (4, 1, 0), (2, 5, -10)]
    for (A, Bc, C) in lines:
        u = (Bc, -A)
        bad = [(A, Bc), (A, -Bc), (Bc, A), (A + 1, Bc + 2), (2 * A, Bc + 1)]
        bad = [t for t in bad if not parallel(t, u) and t != (A, Bc) or t == (A, Bc)]
        bad = [t for t in bad if not parallel(t, u)]
        b.mc(B19, 'nb', 'Vectơ pháp tuyến', f"Vectơ nào sau đây là một vectơ pháp tuyến của đường thẳng $\\Delta: {L_raw(A, Bc, C)}$?", M(f"{vec('n')}={P(A, Bc)}"),
             [M(f"{vec('n')}={P(*t)}") for t in [(Bc, A), (-Bc, A + 1), (A + 1, Bc), (Bc + 2, -A)] if not parallel(t, (A, Bc))][:3],
             f"Đường thẳng $Ax+By+C=0$ có một vectơ pháp tuyến là $\\vec n=(A; B)={P(A, Bc)}$.")
        b.mc(B19, 'th', 'Vectơ chỉ phương', f"Một vectơ chỉ phương của đường thẳng $\\Delta: {L_raw(A, Bc, C)}$ là:", M(f"{vec('u')}={P(Bc, -A)}"),
             [M(f"{vec('u')}={P(*t)}") for t in [(A, Bc), (A, -Bc), (Bc, A), (A + 1, Bc + 1), (A + 2, Bc - 1)] if not parallel(t, u)][:3],
             f"Vectơ pháp tuyến là $\\vec n={P(A, Bc)}$. Vectơ chỉ phương vuông góc với $\\vec n$ nên có thể chọn $\\vec u=(B; -A)={P(Bc, -A)}$.")
    for (x0, y0, a_, b_) in ((1, 2, 1, -2), (2, -1, 3, 1), (-1, 0, 2, 5)):
        t = lambda c0, d: f"{c0}{'+' if d >= 0 else '-'}{abs(d)}t" if d not in (1, -1) else f"{c0}{'+' if d > 0 else '-'}t"
        def par(x0_, y0_, a2, b2): return f"x={x0_}{'+' if a2 >= 0 else '-'}{'' if abs(a2) == 1 else abs(a2)}t,\\ y={y0_}{'+' if b2 >= 0 else '-'}{'' if abs(b2) == 1 else abs(b2)}t"
        b.mc(B19, 'th', 'Phương trình tham số', f"Phương trình tham số của đường thẳng đi qua $A{P(x0, y0)}$ và có vectơ chỉ phương $\\vec u={P(a_, b_)}$ là:", M(par(x0, y0, a_, b_)),
             [M(par(x0, y0, b_, a_)), M(par(a_, b_, x0, y0)), M(par(x0, y0, -a_ if a_ != -a_ else a_, b_)) if False else M(par(-x0 if x0 else 1, y0, a_, b_))],
             f"Phương trình tham số có dạng $x=x_0+at,\\ y=y_0+bt$ với $(x_0;y_0)={P(x0, y0)}$ và $(a;b)={P(a_, b_)}$.")
    for (x0, y0, A, Bc) in ((1, 2, 3, 1), (2, -1, 1, 4), (0, 3, 2, -1), (-2, 1, 5, 2)):
        C = -(A * x0 + Bc * y0)
        b.mc(B19, 'th', 'Phương trình tổng quát', f"Phương trình tổng quát của đường thẳng đi qua $M{P(x0, y0)}$ và có vectơ pháp tuyến $\\vec n={P(A, Bc)}$ là:", M(L_raw(A, Bc, C)),
             [M(L_raw(A, Bc, -C)), M(L_raw(Bc, -A, C)), M(L_raw(A, Bc, C + 1))],
             f"Phương trình: ${A}(x{'-' if x0 >= 0 else '+'}{abs(x0)})+({Bc})(y{'-' if y0 >= 0 else '+'}{abs(y0)})=0$, khai triển được ${L_raw(A, Bc, C)}$.")
    for (A_, B_) in (((1, 1), (3, 5)), ((2, 0), (2, 4)), ((0, 1), (3, 4)), ((1, 2), (4, 3)), ((-1, 3), (2, -3))):
        dx, dy = B_[0] - A_[0], B_[1] - A_[1]
        Ac, Bc = dy, -dx
        C = -(Ac * A_[0] + Bc * A_[1])
        eq = norm_line(Ac, Bc, C)
        b.mc(B19, 'vd', 'Đường thẳng đi qua hai điểm', f"Phương trình đường thẳng đi qua $A{P(*A_)}$ và $B{P(*B_)}$ là:", M(L(Ac, Bc, C)),
             [M(L(-dy, Bc, C)), M(L(dx, dy, -(dx * A_[0] + dy * A_[1]))), M(L(Ac, Bc, C + 2)), M(L(Ac, Bc, C - 3)), M(L(Ac + 1, Bc, C))],
             f"$\\vec{{AB}}={P(dx, dy)}$ là vectơ chỉ phương nên vectơ pháp tuyến là $\\vec n={P(dy, -dx)}$. Đường thẳng qua $A$: ${dy}(x-({A_[0]}))+({-dx})(y-({A_[1]}))=0$, hay ${L(Ac, Bc, C)}$.")
        b.sa(B19, 'vd', 'Đường thẳng đi qua hai điểm', f"Đường thẳng đi qua $A{P(*A_)}$ và $B{P(*B_)}$ có dạng $ax+by+c=0$ với $a,b,c$ là các số nguyên nguyên tố cùng nhau và $a>0$. Tìm $a+b+c$.", sum(eq),
             f"$\\vec{{AB}}={P(dx, dy)}$ nên $\\vec n={P(dy, -dx)}$. Phương trình rút gọn: ${L(Ac, Bc, C)}$, do đó $a+b+c={eq[0]}+({eq[1]})+({eq[2]})={sum(eq)}$.")
    for (A, Bc, C) in ((2, -1, -1), (1, 1, -3), (3, 2, -7)):
        pts = [(x, y) for x in range(-2, 5) for y in range(-2, 6) if A * x + Bc * y + C == 0]
        good = pts[len(pts) // 2]
        bads = [(x, y) for x in range(-2, 5) for y in range(-2, 6) if A * x + Bc * y + C != 0 and abs(A * x + Bc * y + C) <= 2][:3]
        b.mc(B19, 'nb', 'Điểm thuộc đường thẳng', f"Điểm nào sau đây thuộc đường thẳng $\\Delta: {L_raw(A, Bc, C)}$?", M(f"M{P(*good)}"),
             [M(f"M{P(*p)}") for p in bads],
             f"Thay toạ độ vào vế trái: ${A}\\cdot{good[0]}+({Bc})\\cdot{good[1]}+({C})=0$ nên $M{P(*good)}\\in\\Delta$.")
    # ===== Bài 20: vị trí tương đối, góc, khoảng cách =====
    pairs = [((1, -2, 1), (2, -4, 5)), ((2, 1, -3), (4, 2, -6)), ((1, 1, -2), (1, -1, 0)), ((3, -1, 2), (6, -2, 7)), ((2, 3, 1), (3, -2, 5)), ((1, 2, -1), (2, 4, -2))]
    for l1, l2 in pairs:
        (A1, B1, C1), (A2, B2, C2) = l1, l2
        cross = A1 * B2 - A2 * B1
        if cross != 0: kind = "Cắt nhau"
        elif A1 * C2 - A2 * C1 == 0 and B1 * C2 - B2 * C1 == 0: kind = "Trùng nhau"
        else: kind = "Song song"
        why = {"Cắt nhau": f"$A_1B_2-A_2B_1={cross}\\ne0$ nên hai đường thẳng cắt nhau.", "Trùng nhau": "Các hệ số tương ứng tỉ lệ: $\\frac{A_1}{A_2}=\\frac{B_1}{B_2}=\\frac{C_1}{C_2}$ nên hai đường thẳng trùng nhau.", "Song song": "Có $\\frac{A_1}{A_2}=\\frac{B_1}{B_2}\\ne\\frac{C_1}{C_2}$ nên hai đường thẳng song song."}[kind]
        b.mc(B20, 'th', 'Vị trí tương đối hai đường thẳng', f"Vị trí tương đối của $\\Delta_1: {L_raw(*l1)}$ và $\\Delta_2: {L_raw(*l2)}$ là:", kind, [k for k in ("Cắt nhau", "Trùng nhau", "Song song", "Không xác định được") if k != kind][:3], why)
    for (n1, n2, ang) in (((1, 0), (1, 1), 45), ((1, 1), (1, -1), 90), ((1, 0), (0, 1), 90), ((2, 2), (1, 0), 45), ((1, 2), (2, -1), 90), ((1, 1), (2, 2), 0)):
        dot = abs(n1[0] * n2[0] + n1[1] * n2[1]); c = dot / (math.hypot(*n1) * math.hypot(*n2))
        assert abs(math.degrees(math.acos(min(1, c))) - ang) < 1e-3
        l1 = (n1[0], n1[1], -1); l2 = (n2[0], n2[1], 3)
        b.mc(B20, 'th', 'Góc giữa hai đường thẳng', f"Góc giữa hai đường thẳng $d_1: {L_raw(*l1)}$ và $d_2: {L_raw(*l2)}$ bằng:", M(f"{ang}^\\circ"),
             [M(f"{x}^\\circ") for x in (30, 45, 60, 90, 0) if x != ang][:3],
             f"Hai vectơ pháp tuyến $\\vec n_1={P(*n1)}$, $\\vec n_2={P(*n2)}$. $\\cos(d_1,d_2)=\\frac{{|\\vec n_1\\cdot\\vec n_2|}}{{|\\vec n_1||\\vec n_2|}}=\\frac{{{dot}}}{{{rad(n1[0]**2+n1[1]**2)}\\cdot{rad(n2[0]**2+n2[1]**2)}}}={fnum(c, 3)}$ nên góc bằng ${ang}^\\circ$.")
    for (A, Bc, C, x0, y0) in ((3, 4, -11, 1, 2), (3, 4, 5, 2, 1), (5, 12, -7, 1, 1), (6, 8, 0, 3, 4), (3, 4, -10, 0, 0), (5, 12, 1, 2, -1), (8, 15, -2, 1, 0)):
        num = A * x0 + Bc * y0 + C; den = math.isqrt(A * A + Bc * Bc); assert den * den == A * A + Bc * Bc
        d = Fraction(abs(num), den)
        b.mc(B20, 'th', 'Khoảng cách từ điểm đến đường thẳng', f"Khoảng cách từ điểm $M{P(x0, y0)}$ đến đường thẳng $\\Delta: {L_raw(A, Bc, C)}$ bằng:", M(frac(d) if d.denominator == 1 else frac(d)),
             [M(frac(Fraction(num, den))) if num > 0 else M(frac(d + 1)), M(frac(Fraction(abs(num), A * A + Bc * Bc))), M(frac(d + Fraction(1, 2))), M(frac(d * 2 + 1))],
             f"$d(M,\\Delta)=\\frac{{|Ax_0+By_0+C|}}{{\\sqrt{{A^2+B^2}}}}=\\frac{{|{A}\\cdot{x0}+{Bc}\\cdot{y0}+({C})|}}{{\\sqrt{{{A*A}+{Bc*Bc}}}}}=\\frac{{{abs(num)}}}{{{den}}}={frac(d)}$.")
        b.sa(B20, 'th', 'Khoảng cách từ điểm đến đường thẳng', f"Tính khoảng cách từ $M{P(x0, y0)}$ đến đường thẳng $\\Delta: {L_raw(A, Bc, C)}$ (làm tròn đến hàng phần trăm).", float(d),
             f"$d=\\frac{{|{A}\\cdot{x0}+{Bc}\\cdot{y0}+({C})|}}{{\\sqrt{{{A*A}+{Bc*Bc}}}}}=\\frac{{{abs(num)}}}{{{den}}}\\approx {fnum(float(d), 3)}$.", tol=0.01)
    for (A, Bc, C1, C2) in ((3, 4, -5, 5), (5, 12, 2, -11), (6, 8, 1, -9)):
        den = math.isqrt(A * A + Bc * Bc); d = Fraction(abs(C1 - C2), den)
        b.mc(B20, 'vd', 'Khoảng cách giữa hai đường thẳng song song', f"Khoảng cách giữa hai đường thẳng song song $d_1: {L_raw(A, Bc, C1)}$ và $d_2: {L_raw(A, Bc, C2)}$ bằng:", M(frac(d)),
             [M(frac(Fraction(abs(C1 - C2), A * A + Bc * Bc))), M(frac(d + 1)), M(frac(Fraction(abs(C1 + C2), den)) if C1 + C2 != 0 and Fraction(abs(C1 + C2), den) != d else d * 2)],
             f"Lấy một điểm của $d_1$ rồi tính khoảng cách đến $d_2$, hoặc dùng $d=\\frac{{|C_1-C_2|}}{{\\sqrt{{A^2+B^2}}}}=\\frac{{{abs(C1-C2)}}}{{{den}}}={frac(d)}$.")
    for (x0, y0, A, Bc, C) in ((1, -1, 2, -3, 1), (2, 3, 1, 4, -2), (0, 1, 3, 2, 5)):
        Cn = -(A * x0 + Bc * y0)
        b.mc(B20, 'vd', 'Đường thẳng song song', f"Đường thẳng đi qua $M{P(x0, y0)}$ và song song với $d: {L_raw(A, Bc, C)}$ có phương trình:", M(L_raw(A, Bc, Cn)),
             [M(L_raw(A, Bc, -Cn)), M(L_raw(Bc, -A, -(Bc * x0 - A * y0))), M(L_raw(A, Bc, C))],
             f"Đường thẳng song song với $d$ có dạng ${lin(A, Bc)}+C=0$. Đi qua $M{P(x0, y0)}$: ${A}\\cdot{x0}+({Bc})\\cdot{y0}+C=0\\Rightarrow C={Cn}$.")
    for (x0, y0, A, Bc, C) in ((0, 0, 2, -1, 1), (1, 2, 1, 3, -1), (3, -1, 4, 1, 2)):
        Cn = -(Bc * x0 - A * y0)
        b.mc(B20, 'vd', 'Đường thẳng vuông góc', f"Đường thẳng đi qua $M{P(x0, y0)}$ và vuông góc với $d: {L_raw(A, Bc, C)}$ có phương trình:", M(L_raw(Bc, -A, Cn)),
             [M(L_raw(A, Bc, -(A * x0 + Bc * y0))), M(L_raw(-Bc, -A, Cn)) if parallel((-Bc, -A), (Bc, -A)) is False else M(L_raw(Bc, A, Cn)), M(L_raw(Bc, -A, Cn + 1)), M(L_raw(Bc, -A, -Cn if Cn else 7))],
             f"Vectơ chỉ phương của $d$ là $\\vec u=({Bc}; {-A})$, dùng làm vectơ pháp tuyến của đường thẳng cần tìm: ${Bc}x+({-A})y+C=0$. Qua $M{P(x0, y0)}$ suy ra $C={Cn}$.")
    # ===== Bài 21: đường tròn =====
    for (a, bb, R) in ((1, 2, 3), (-2, 3, 4), (0, -1, 5), (3, 0, 2), (2, -3, 1)):
        b.mc(B21, 'nb', 'Tâm và bán kính', f"Đường tròn $(C): (x{'-' if a >= 0 else '+'}{abs(a)})^2+(y{'-' if bb >= 0 else '+'}{abs(bb)})^2={R*R}$ có tâm và bán kính là:", M(f"I{P(a, bb)},\\ R={R}"),
             [M(f"I{P(-a, -bb)},\\ R={R}"), M(f"I{P(a, bb)},\\ R={R*R}"), M(f"I{P(bb, a)},\\ R={R}"), M(f"I{P(a, bb)},\\ R={R+1}"), M(f"I{P(a + 1, bb)},\\ R={R}")],
             f"Đường tròn $(x-a)^2+(y-b)^2=R^2$ có tâm $I(a;b)={P(a, bb)}$ và bán kính $R=\\sqrt{{{R*R}}}={R}$.")
    for (a, bb, R) in ((1, 2, 2), (2, -1, 3), (-1, 3, 4), (3, 1, 5), (0, 2, 1)):
        c = a * a + bb * bb - R * R
        eq = f"x^2+y^2{'-' if a >= 0 else '+'}{2*abs(a)}x{'-' if bb >= 0 else '+'}{2*abs(bb)}y{'+' if c >= 0 else '-'}{abs(c)}=0" if a != 0 else f"x^2+y^2{'-' if bb >= 0 else '+'}{2*abs(bb)}y{'+' if c >= 0 else '-'}{abs(c)}=0"
        b.mc(B21, 'th', 'Tâm và bán kính (dạng khai triển)', f"Đường tròn $(C): {eq}$ có bán kính bằng:", M(str(R)),
             [M(str(R * R)), M(rad(a * a + bb * bb)) if a * a + bb * bb != R * R else M(str(R + 1)), M(str(R + 1)), M(str(abs(c)) if abs(c) not in (R, R * R, R + 1) else str(R + 3))],
             f"$a={a}$, $b={bb}$, $c={c}$. Bán kính $R=\\sqrt{{a^2+b^2-c}}=\\sqrt{{{a*a}+{bb*bb}-({c})}}=\\sqrt{{{R*R}}}={R}$.")
        b.sa(B21, 'th', 'Bán kính đường tròn dạng khai triển', f"Đường tròn $(C): {eq}$ có bán kính bằng bao nhiêu?", R,
             f"$R=\\sqrt{{a^2+b^2-c}}$ với $a={a}$, $b={bb}$, $c={c}$: $R=\\sqrt{{{R*R}}}={R}$.")
    for (a, bb, R) in ((0, 0, 3), (1, 2, 2), (-1, 1, 4), (2, 0, 5)):
        b.mc(B21, 'th', 'Phương trình đường tròn', f"Phương trình đường tròn tâm $I{P(a, bb)}$ và bán kính $R={R}$ là:", M(f"(x{'-' if a > 0 else '+'}{abs(a)})^2+(y{'-' if bb > 0 else '+'}{abs(bb)})^2={R*R}" if (a or bb) else f"x^2+y^2={R*R}"),
             [M(f"(x{'+' if a > 0 else '-'}{abs(a)})^2+(y{'+' if bb > 0 else '-'}{abs(bb)})^2={R*R}" if (a or bb) else f"x^2+y^2={R}"), M(f"(x{'-' if a > 0 else '+'}{abs(a)})^2+(y{'-' if bb > 0 else '+'}{abs(bb)})^2={R}" if (a or bb) else "x^2+y^2=6"), M(f"(x{'-' if bb > 0 else '+'}{abs(bb)})^2+(y{'-' if a > 0 else '+'}{abs(a)})^2={R*R}" if (a or bb) and a != bb else f"x^2+y^2={R+1}"), M(f"(x{'-' if a > 0 else '+'}{abs(a)})^2+(y{'-' if bb > 0 else '+'}{abs(bb)})^2={R*R+4}" if (a or bb) else f"x^2+y^2={R*R+4}")],
             f"Phương trình đường tròn tâm $I(a;b)$, bán kính $R$ là $(x-a)^2+(y-b)^2=R^2$ với $a={a}$, $b={bb}$, $R^2={R*R}$.")
    for (A_, B_) in (((-2, 0), (2, 0)), ((1, 1), (5, 1)), ((0, 2), (0, -4)), ((-1, 2), (3, 6))):
        I = ((A_[0] + B_[0]) // 2, (A_[1] + B_[1]) // 2)
        R2 = ((B_[0] - A_[0]) ** 2 + (B_[1] - A_[1]) ** 2) // 4
        assert ((B_[0] - A_[0]) ** 2 + (B_[1] - A_[1]) ** 2) % 4 == 0
        def circ(a, bb, r2):
            return f"(x{'-' if a > 0 else '+'}{abs(a)})^2+(y{'-' if bb > 0 else '+'}{abs(bb)})^2={r2}" if (a or bb) else f"x^2+y^2={r2}"
        b.mc(B21, 'vd', 'Đường tròn đường kính AB', f"Phương trình đường tròn đường kính $AB$ với $A{P(*A_)}$, $B{P(*B_)}$ là:", M(circ(*I, R2)),
             [M(circ(*I, 2 * R2)), M(circ(*I, R2 * 4)), M(circ(-I[0], -I[1], R2)) if I != (0, 0) else M(circ(1, 0, R2))],
             f"Tâm là trung điểm $I={P(*I)}$. Bán kính $R=\\frac{{AB}}{{2}}$, $R^2=\\frac{{AB^2}}{{4}}=\\frac{{{(B_[0]-A_[0])**2+(B_[1]-A_[1])**2}}}{{4}}={R2}$.")
    for (a, bb, R, x0, y0, pos) in ((0, 0, 5, 3, 4, 'trên'), (1, 1, 2, 1, 2, 'trong'), (0, 0, 3, 4, 0, 'ngoài'), (2, -1, 5, 5, 3, 'trên'), (0, 0, 2, 1, 1, 'trong')):
        d2 = (x0 - a) ** 2 + (y0 - bb) ** 2
        assert pos == ('trên' if d2 == R * R else ('trong' if d2 < R * R else 'ngoài'))
        b.mc(B21, 'th', 'Vị trí điểm và đường tròn', f"Cho đường tròn $(C): (x-{a})^2+(y-({bb}))^2={R*R}$ và điểm $M{P(x0, y0)}$. Điểm $M$ nằm:", f"{pos.capitalize() if False else ('Trên đường tròn' if pos == 'trên' else ('Bên trong đường tròn' if pos == 'trong' else 'Bên ngoài đường tròn'))}",
             [t for t in ('Trên đường tròn', 'Bên trong đường tròn', 'Bên ngoài đường tròn') if t != ('Trên đường tròn' if pos == 'trên' else ('Bên trong đường tròn' if pos == 'trong' else 'Bên ngoài đường tròn'))] + ['Trùng với tâm đường tròn'],
             f"$IM^2=({x0}-({a}))^2+({y0}-({bb}))^2={d2}$, còn $R^2={R*R}$. Vì $IM^2{'=' if d2 == R*R else ('<' if d2 < R*R else '>')}R^2$ nên $M$ nằm {pos} đường tròn.")
    for (a, bb, x0, y0, R2) in ((0, 0, 2, 0, 4), (0, 0, 3, 4, 25), (1, 2, 4, 2, 9), (0, 0, 0, 5, 25)):
        A_t, B_t = x0 - a, y0 - bb
        C_t = -(A_t * x0 + B_t * y0)
        b.mc(B21, 'vd', 'Tiếp tuyến của đường tròn', f"Phương trình tiếp tuyến của đường tròn $(C): (x-{a})^2+(y-{bb})^2={R2}$ tại điểm $M_0{P(x0, y0)}$ thuộc $(C)$ là:", M(L(A_t, B_t, C_t)),
             [M(L(B_t, -A_t, -(B_t * x0 - A_t * y0))), M(L(A_t, B_t, -C_t)) if C_t else M(L(A_t, B_t, 3)), M(L(A_t, B_t, C_t + 2)) ],
             f"Tiếp tuyến tại $M_0$ vuông góc với $\\vec{{IM_0}}={P(A_t, B_t)}$ nên nhận $\\vec{{IM_0}}$ làm vectơ pháp tuyến: ${A_t}(x-{x0})+{B_t}(y-{y0})=0$, hay ${L(A_t, B_t, C_t)}$.")
    for (a, bb, R, A, Bc, C) in ((0, 0, 2, 3, 4, -10), (0, 0, 2, 3, 4, 5), (0, 0, 3, 3, 4, -20), (1, 0, 2, 1, 0, -5)):
        d = Fraction(abs(A * a + Bc * bb + C), math.isqrt(A * A + Bc * Bc))
        assert math.isqrt(A * A + Bc * Bc) ** 2 == A * A + Bc * Bc
        rel = "Cắt nhau tại hai điểm" if d < R else ("Tiếp xúc nhau" if d == R else "Không có điểm chung")
        b.mc(B21, 'vd', 'Vị trí đường thẳng và đường tròn', f"Đường thẳng $\\Delta: {L_raw(A, Bc, C)}$ và đường tròn $(C): (x-{a})^2+y^2={R*R}$ có vị trí tương đối:", rel,
             [t for t in ("Cắt nhau tại hai điểm", "Tiếp xúc nhau", "Không có điểm chung") if t != rel] + ["Đường thẳng đi qua tâm"],
             f"Tâm $I{P(a, bb)}$, $R={R}$. $d(I,\\Delta)=\\frac{{|{A}\\cdot{a}+{Bc}\\cdot{bb}+({C})|}}{{\\sqrt{{{A*A}+{Bc*Bc}}}}}={frac(d)}$. So với $R={R}$: $d{'<' if d<R else ('=' if d==R else '>')}R$ nên {rel.lower()}.")
    # ===== Bài 22: conic =====
    for (a, bb, c) in ((5, 3, 4), (13, 5, 12), (10, 6, 8), (5, 4, 3), (17, 8, 15)):
        eq = f"\\frac{{x^2}}{{{a*a}}}+\\frac{{y^2}}{{{bb*bb}}}=1"
        b.mc(B22, 'th', 'Elip: tiêu cự', f"Elip $(E): {eq}$ có tiêu cự bằng:", M(str(2 * c)),
             [M(str(c)), M(str(2 * a)), M(str(2 * bb)), M(str(a + bb))],
             f"$a^2={a*a}$, $b^2={bb*bb}$, $c^2=a^2-b^2={c*c}$ nên $c={c}$. Tiêu cự $2c={2*c}$.")
        b.mc(B22, 'th', 'Elip: độ dài trục', f"Độ dài trục lớn của elip $(E): {eq}$ là:", M(str(2 * a)),
             [M(str(a)), M(str(2 * bb)), M(str(bb)), M(str(2 * c))],
             f"Với $a^2={a*a}$ ta có $a={a}$ (lớn hơn $b={bb}$). Độ dài trục lớn $2a={2*a}$.")
        b.mc(B22, 'th', 'Elip: tiêu điểm', f"Toạ độ các tiêu điểm của elip $(E): {eq}$ là:", M(f"F_1({-c}; 0),\\ F_2({c}; 0)"),
             [M(f"F_1(0; {-c}),\\ F_2(0; {c})"), M(f"F_1({-a}; 0),\\ F_2({a}; 0)"), M(f"F_1({-bb}; 0),\\ F_2({bb}; 0)")],
             f"Vì $a>b$ nên tiêu điểm nằm trên $Ox$: $c=\\sqrt{{a^2-b^2}}=\\sqrt{{{a*a}-{bb*bb}}}={c}$, $F_{{1,2}}(\\mp{c}; 0)$.")
        b.sa(B22, 'th', 'Elip: tiêu cự', f"Elip $(E): {eq}$ có tiêu cự bằng bao nhiêu?", 2 * c,
             f"$c^2=a^2-b^2={a*a}-{bb*bb}={c*c}$ nên $c={c}$ và tiêu cự $2c={2*c}$.")
    for (a, bb, c) in ((3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)):
        eq = f"\\frac{{x^2}}{{{a*a}}}-\\frac{{y^2}}{{{bb*bb}}}=1"
        b.mc(B22, 'th', 'Hypebol: tiêu cự', f"Hypebol $(H): {eq}$ có tiêu cự bằng:", M(str(2 * c)),
             [M(str(c)), M(str(2 * a)), M(str(2 * bb)), M(str(a + bb))],
             f"$a^2={a*a}$, $b^2={bb*bb}$, $c^2=a^2+b^2={c*c}$ nên $c={c}$. Tiêu cự $2c={2*c}$.")
        g = gcd(bb, a)
        b.mc(B22, 'vd', 'Hypebol: tiệm cận', f"Phương trình các đường tiệm cận của hypebol $(H): {eq}$ là:", M(f"y=\\pm{frac(Fraction(bb, a))}x"),
             [M(f"y=\\pm{frac(Fraction(a, bb))}x"), M(f"y=\\pm{bb}x"), M(f"y=\\pm{frac(Fraction(bb * bb, a * a))}x")],
             f"Hypebol $\\frac{{x^2}}{{a^2}}-\\frac{{y^2}}{{b^2}}=1$ có tiệm cận $y=\\pm\\frac{{b}}{{a}}x$ với $a={a}$, $b={bb}$, tức $y=\\pm{frac(Fraction(bb, a))}x$.")
    for p in (2, 4, 6, 8):
        fx = Fraction(p, 2)
        b.mc(B22, 'th', 'Parabol: tiêu điểm', f"Tiêu điểm của parabol $(P): y^2={2*p}x$ có toạ độ là:", M(f"F({frac(fx)}; 0)"),
             [M(f"F({p}; 0)"), M(f"F(0; {frac(fx)})"), M(f"F({frac(-fx)}; 0)")],
             f"Parabol $y^2=2px$ có $2p={2*p}$ nên $p={p}$. Tiêu điểm $F\\left(\\frac{{p}}{{2}}; 0\\right)=({frac(fx)}; 0)$.")
        b.mc(B22, 'th', 'Parabol: đường chuẩn', f"Phương trình đường chuẩn của parabol $(P): y^2={2*p}x$ là:", M(f"x={frac(-fx)}"),
             [M(f"x={frac(fx)}"), M(f"y={frac(-fx)}"), M(f"x={-p}")],
             f"Với $p={p}$, đường chuẩn là $x=-\\frac{{p}}{{2}}=-{frac(fx)}$.")
    b.mc(B22, 'nb', 'Nhận dạng conic', "Phương trình nào sau đây là phương trình chính tắc của một elip?", M('\\frac{x^2}{9}+\\frac{y^2}{4}=1'),
         [M('\\frac{x^2}{9}-\\frac{y^2}{4}=1'), M('y^2=4x'), M('x^2+y^2=9')],
         "Elip có dạng $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1$ với $a>b>0$. Phương án còn lại lần lượt là hypebol, parabol và đường tròn.")
    b.mc(B22, 'nb', 'Nhận dạng conic', "Phương trình nào sau đây là phương trình chính tắc của một hypebol?", M('\\frac{x^2}{4}-\\frac{y^2}{9}=1'),
         [M('\\frac{x^2}{4}+\\frac{y^2}{9}=1'), M('y^2=8x'), M('x^2+y^2=4')],
         "Hypebol có dạng $\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1$ (hai số hạng trái dấu).")
    return b
