# -*- coding: utf-8 -*-
"""Toán 10 - Chương III: Hệ thức lượng trong tam giác (bổ sung câu hỏi mới, tự kiểm bằng code)."""
import math
from fractions import Fraction
from .common import Bank, M, frac, rad, fnum

B5, B6 = 'b5', 'b6'

# ---- giá trị lượng giác đặc biệt (chuỗi LaTeX) ----
SIN = {30: '\\frac{1}{2}', 45: '\\frac{\\sqrt{2}}{2}', 60: '\\frac{\\sqrt{3}}{2}', 120: '\\frac{\\sqrt{3}}{2}', 135: '\\frac{\\sqrt{2}}{2}', 150: '\\frac{1}{2}'}
COS = {30: '\\frac{\\sqrt{3}}{2}', 45: '\\frac{\\sqrt{2}}{2}', 60: '\\frac{1}{2}', 120: '-\\frac{1}{2}', 135: '-\\frac{\\sqrt{2}}{2}', 150: '-\\frac{\\sqrt{3}}{2}'}
TAN = {30: '\\frac{\\sqrt{3}}{3}', 45: '1', 60: '\\sqrt{3}', 120: '-\\sqrt{3}', 135: '-1', 150: '-\\frac{\\sqrt{3}}{3}'}
POOL = ['\\frac{1}{2}', '-\\frac{1}{2}', '\\frac{\\sqrt{2}}{2}', '-\\frac{\\sqrt{2}}{2}', '\\frac{\\sqrt{3}}{2}', '-\\frac{\\sqrt{3}}{2}',
        '\\frac{\\sqrt{3}}{3}', '-\\frac{\\sqrt{3}}{3}', '1', '-1', '\\sqrt{3}', '-\\sqrt{3}']
def neg(s): return s[1:] if s.startswith('-') else '-' + s

def pick_wrong(correct, extra, k=3):
    out = []
    for w in extra + POOL:
        if w != correct and w not in out: out.append(w)
        if len(out) == k: break
    return [M(w) for w in out]

def build():
    b = Bank('toan10', 'c3')

    # ===== Bài 5: giá trị lượng giác =====
    for fn, table, angles in (('sin', SIN, (120, 135, 150)), ('cos', COS, (30, 120, 135, 150)), ('tan', TAN, (60, 120, 135, 150))):
        for a in angles:
            c = table[a]
            sup = 180 - a
            if a > 90:
                rel = {'sin': f'\\sin {a}^\\circ = \\sin {sup}^\\circ', 'cos': f'\\cos {a}^\\circ = -\\cos {sup}^\\circ', 'tan': f'\\tan {a}^\\circ = -\\tan {sup}^\\circ'}[fn]
                expl = f"Hai góc {a}° và {sup}° bù nhau nên ${rel}$. Tra bảng giá trị đặc biệt ta được $\\{fn} {a}^\\circ = {c}$."
            else:
                expl = f"Tra bảng giá trị lượng giác của các góc đặc biệt: $\\{fn} {a}^\\circ = {c}$."
            other = {'sin': COS, 'cos': SIN, 'tan': SIN}[fn][a]
            b.mc(B5, 'nb' if a <= 60 or fn == 'sin' else 'th', 'Giá trị lượng giác góc đặc biệt',
                 f"Giá trị của $\\{fn} {a}^\\circ$ bằng:", M(c), pick_wrong(c, [neg(c), other, neg(other)]), expl)

    # sin = p/q (góc tù) -> cos, tan
    for p, q, r in ((3, 5, 4), (5, 13, 12), (8, 17, 15), (7, 25, 24), (20, 29, 21)):
        cos = Fraction(-r, q); tan = Fraction(-p, r)
        expl = (f"Vì $0^\\circ<\\alpha<180^\\circ$ nên $\\sin\\alpha>0$; $\\alpha$ tù nên $\\cos\\alpha<0$. "
                f"Từ $\\sin^2\\alpha+\\cos^2\\alpha=1$: $\\cos^2\\alpha = 1-\\frac{{{p*p}}}{{{q*q}}}=\\frac{{{r*r}}}{{{q*q}}}$, suy ra $\\cos\\alpha=-\\frac{{{r}}}{{{q}}}$.")
        b.mc(B5, 'th', 'Tính cos khi biết sin (góc tù)',
             f"Cho $\\alpha$ là góc tù và $\\sin\\alpha=\\frac{{{p}}}{{{q}}}$. Giá trị của $\\cos\\alpha$ bằng:",
             M(frac(cos)), [M(frac(-cos)), M(frac(Fraction(q - p, q))), M(frac(Fraction(p, r)))], expl)
        expl2 = (f"Có $\\cos\\alpha=-\\frac{{{r}}}{{{q}}}$ (góc tù). Do đó $\\tan\\alpha=\\frac{{\\sin\\alpha}}{{\\cos\\alpha}}=\\frac{{{p}}}{{{q}}}:\\left(-\\frac{{{r}}}{{{q}}}\\right)=-\\frac{{{p}}}{{{r}}}$.")
        b.mc(B5, 'th', 'Tính tan khi biết sin (góc tù)',
             f"Cho $\\alpha$ là góc tù và $\\sin\\alpha=\\frac{{{p}}}{{{q}}}$. Giá trị của $\\tan\\alpha$ bằng:",
             M(frac(tan)), [M(frac(-tan)), M(frac(Fraction(r, p))), M(frac(Fraction(-r, p)))], expl2)

    # tan = p/r (góc nhọn) -> cos
    for p, r, q in ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)):
        expl = (f"Với góc nhọn: $1+\\tan^2\\alpha=\\frac{{1}}{{\\cos^2\\alpha}}$, tức $\\frac{{1}}{{\\cos^2\\alpha}}=1+\\frac{{{p*p}}}{{{r*r}}}=\\frac{{{q*q}}}{{{r*r}}}$. "
                f"Vì $\\cos\\alpha>0$ nên $\\cos\\alpha=\\frac{{{r}}}{{{q}}}$.")
        b.mc(B5, 'th', 'Tính cos khi biết tan (góc nhọn)',
             f"Cho góc nhọn $\\alpha$ có $\\tan\\alpha=\\frac{{{p}}}{{{r}}}$. Giá trị của $\\cos\\alpha$ bằng:",
             M(frac(Fraction(r, q))), [M(frac(Fraction(p, q))), M(frac(Fraction(q, r))), M(frac(Fraction(-r, q)))], expl)

    # liên hệ trong tam giác ABC
    b.mc(B5, 'nb', 'Quan hệ góc trong tam giác', "Cho tam giác $ABC$. Khẳng định nào sau đây đúng?",
         M('\\sin(A+B)=\\sin C'), [M('\\sin(A+B)=-\\sin C'), M('\\cos(A+B)=\\cos C'), M('\\sin(A+B)=\\cos C')],
         "Trong tam giác $A+B+C=180^\\circ$ nên $A+B=180^\\circ-C$, hai góc bù nhau. Vì $\\sin(180^\\circ-\\alpha)=\\sin\\alpha$ nên $\\sin(A+B)=\\sin C$.")
    b.mc(B5, 'th', 'Quan hệ góc trong tam giác', "Cho tam giác $ABC$. Biểu thức $\\cos(A+B)+\\cos C$ bằng:",
         M('0'), [M('1'), M('2\\cos C'), M('-1')],
         "Vì $A+B=180^\\circ-C$ nên $\\cos(A+B)=\\cos(180^\\circ-C)=-\\cos C$. Do đó $\\cos(A+B)+\\cos C=0$.")
    b.mc(B5, 'nb', 'Giá trị không xác định', "Giá trị lượng giác nào sau đây KHÔNG xác định?",
         M('\\tan 90^\\circ'), [M('\\cot 90^\\circ'), M('\\tan 45^\\circ'), M('\\sin 90^\\circ')],
         "$\\tan\\alpha=\\frac{\\sin\\alpha}{\\cos\\alpha}$ chỉ xác định khi $\\cos\\alpha\\ne 0$. Vì $\\cos 90^\\circ=0$ nên $\\tan 90^\\circ$ không xác định (còn $\\cot 90^\\circ=0$).")
    b.mc(B5, 'nb', 'Dấu của giá trị lượng giác', "Với $90^\\circ<\\alpha<180^\\circ$, khẳng định nào sau đây đúng?",
         M('\\sin\\alpha>0,\\ \\cos\\alpha<0'), [M('\\sin\\alpha<0,\\ \\cos\\alpha>0'), M('\\sin\\alpha>0,\\ \\cos\\alpha>0'), M('\\sin\\alpha<0,\\ \\cos\\alpha<0')],
         "Với góc tù, điểm trên nửa đường tròn đơn vị nằm bên trái trục tung nên hoành độ $\\cos\\alpha<0$, còn tung độ $\\sin\\alpha>0$.")
    for x in (20, 35, 50):
        b.mc(B5, 'th', 'Rút gọn biểu thức lượng giác', f"Giá trị của biểu thức $A=\\sin {x}^\\circ+\\sin {180-x}^\\circ-2\\sin {x}^\\circ+\\cos^2 {x}^\\circ+\\sin^2 {x}^\\circ$ bằng:",
             M('1'), [M('0'), M('2'), M(f'2\\sin {x}^\\circ')],
             f"Do $\\sin {180-x}^\\circ=\\sin {x}^\\circ$ nên $\\sin {x}^\\circ+\\sin {180-x}^\\circ-2\\sin {x}^\\circ=0$. Còn $\\cos^2 {x}^\\circ+\\sin^2 {x}^\\circ=1$. Vậy $A=1$.")
    for (fa, fb, a1, a2, res, text) in (
        ('\\sin^2 30^\\circ', '\\cos^2 60^\\circ', 30, 60, Fraction(1, 2), 'S=\\sin^2 30^\\circ+\\cos^2 60^\\circ'),
        ('\\sin^2 45^\\circ', '\\cos^2 45^\\circ', 45, 45, Fraction(1), 'S=\\sin^2 45^\\circ+\\cos^2 45^\\circ'),
        ('\\sin^2 60^\\circ', '\\cos^2 30^\\circ', 60, 30, Fraction(3, 2), 'S=\\sin^2 60^\\circ+\\cos^2 30^\\circ')):
        b.mc(B5, 'th', 'Tính giá trị biểu thức', f"Giá trị của ${text}$ bằng:", M(frac(res)),
             [M(frac(res + Fraction(1, 2))), M(frac(res - Fraction(1, 4))), M(frac(res * 2 + 1))],
             f"Ta có ${fa}$ và ${fb}$ lấy từ bảng giá trị đặc biệt (bình phương các giá trị tương ứng). Cộng lại được $S={frac(res)}$.")

    # ===== Bài 6: hệ thức lượng =====
    # định lí côsin: tính cạnh
    cos_cases = [(3, 8, 60, 49), (5, 8, 60, 49), (8, 15, 60, 169), (7, 15, 60, 169), (3, 5, 120, 49), (6, 10, 120, 196), (9, 15, 120, 441), (4, 5, 60, 21), (2, 3, 120, 19)]
    for bb, cc, A, a2 in cos_cases:
        cosA = Fraction(1, 2) if A == 60 else Fraction(-1, 2)
        a2c = bb * bb + cc * cc - 2 * bb * cc * cosA
        assert a2c == a2
        wrong_plus = bb * bb + cc * cc + 2 * bb * cc * cosA
        b.mc(B6, 'th', 'Định lí côsin: tính cạnh', f"Tam giác $ABC$ có $b={bb}$, $c={cc}$, $A={A}^\\circ$. Độ dài cạnh $a$ bằng:",
             M(rad(a2)), [M(rad(int(wrong_plus))), M(str(a2)), M(rad(bb * bb + cc * cc))],
             f"Định lí côsin: $a^2=b^2+c^2-2bc\\cos A={bb*bb}+{cc*cc}-2\\cdot{bb}\\cdot{cc}\\cdot\\cos {A}^\\circ={a2}$. Vậy $a={rad(a2)}$.")
    # cos góc khi biết 3 cạnh
    for (a, bb, cc) in ((4, 5, 6), (5, 6, 7), (6, 7, 8), (5, 7, 8), (7, 9, 10)):
        cosA = Fraction(bb * bb + cc * cc - a * a, 2 * bb * cc)
        wrong = Fraction(a * a + bb * bb - cc * cc, 2 * a * bb)
        b.mc(B6, 'th', 'Định lí côsin: tính cos góc', f"Tam giác $ABC$ có $a={a}$, $b={bb}$, $c={cc}$. Giá trị $\\cos A$ bằng:",
             M(frac(cosA)), [M(frac(wrong)), M(frac(-cosA)), M(frac(Fraction(bb * bb + cc * cc - a * a, bb * cc)))],
             f"$\\cos A=\\frac{{b^2+c^2-a^2}}{{2bc}}=\\frac{{{bb*bb}+{cc*cc}-{a*a}}}{{2\\cdot{bb}\\cdot{cc}}}={frac(cosA)}$.")
    # tìm góc
    for (a, bb, cc, ang) in ((7, 5, 8, 60), (7, 3, 5, 120), (13, 8, 15, 60), (14, 6, 10, 120), (5, 3, 4, 90)):
        cosA = Fraction(bb * bb + cc * cc - a * a, 2 * bb * cc)
        assert {60: Fraction(1, 2), 120: Fraction(-1, 2), 90: Fraction(0)}[ang] == cosA
        others = [x for x in (30, 60, 90, 120, 150) if x != ang]
        pick = [60 if ang != 60 else 120, 30 if ang not in (30,) else 45, 150 if ang != 150 else 135]
        b.mc(B6, 'th', 'Định lí côsin: tính góc', f"Tam giác $ABC$ có $a={a}$, $b={bb}$, $c={cc}$. Số đo góc $A$ bằng:",
             M(f'{ang}^\\circ'), [M(f'{x}^\\circ') for x in pick],
             f"$\\cos A=\\frac{{b^2+c^2-a^2}}{{2bc}}=\\frac{{{bb*bb+cc*cc-a*a}}}{{{2*bb*cc}}}={frac(cosA)}$, suy ra $A={ang}^\\circ$.")
    # định lí sin: bán kính
    for (a, A, R) in ((6, 30, '6'), (10, 30, '10'), (8, 45, '4\\sqrt{2}'), (9, 90, '4,5'), (12, 150, '12'), (6, 60, '2\\sqrt{3}')):
        sA = {30: 0.5, 45: math.sqrt(2) / 2, 60: math.sqrt(3) / 2, 90: 1, 150: 0.5}[A]
        val = a / (2 * sA)
        sym = {'6': 6, '10': 10, '4\\sqrt{2}': 4 * math.sqrt(2), '4,5': 4.5, '12': 12, '2\\sqrt{3}': 2 * math.sqrt(3)}[R]
        assert abs(val - sym) < 1e-9
        b.mc(B6, 'th', 'Định lí sin: bán kính đường tròn ngoại tiếp', f"Tam giác $ABC$ có $a={a}$ và $A={A}^\\circ$. Bán kính $R$ của đường tròn ngoại tiếp bằng:",
             M(R), [M(str(a * 2)), M(str(a)), M(str(a * 3)), M('3'), M('5,5'), M('7')],
             f"Định lí sin: $\\frac{{a}}{{\\sin A}}=2R$ nên $R=\\frac{{a}}{{2\\sin A}}=\\frac{{{a}}}{{2\\sin {A}^\\circ}}={R}$.")
    # diện tích 1/2 bc sinA
    for (bb, cc, A, S) in ((6, 8, 30, 12), (10, 12, 150, 30), (8, 9, 30, 18), (5, 8, 30, 10), (6, 10, 90, 30), (4, 6, 30, 6)):
        sA = {30: 0.5, 90: 1, 150: 0.5}[A]
        assert abs(0.5 * bb * cc * sA - S) < 1e-9
        b.mc(B6, 'th', 'Diện tích tam giác', f"Tam giác $ABC$ có $b={bb}$, $c={cc}$, $A={A}^\\circ$. Diện tích $S$ bằng:",
             M(str(S)), [M(str(S * 2)), M(str(bb * cc)), M(fnum(S / 2)), M(str(S + bb)), M(str(S + cc + 1))],
             f"$S=\\frac{{1}}{{2}}bc\\sin A=\\frac{{1}}{{2}}\\cdot{bb}\\cdot{cc}\\cdot\\sin {A}^\\circ={S}$.")
    # Heron
    for (x, y, z, S) in ((13, 14, 15, 84), (5, 12, 13, 30), (9, 10, 17, 36), (10, 17, 21, 84), (4, 13, 15, 24)):
        p = (x + y + z) // 2
        assert (x + y + z) % 2 == 0 and abs(math.sqrt(p * (p - x) * (p - y) * (p - z)) - S) < 1e-9
        b.mc(B6, 'th', 'Công thức Heron', f"Tam giác có ba cạnh {x}, {y}, {z}. Diện tích tam giác bằng:",
             M(str(S)), [M(str(S + 6)), M(str(S * 2)), M(str(p * (p - x))), M(str(S - 12)), M(str(x * y // 2))],
             f"Nửa chu vi $p=\\frac{{{x}+{y}+{z}}}{{2}}={p}$. Heron: $S=\\sqrt{{p(p-a)(p-b)(p-c)}}=\\sqrt{{{p}\\cdot{p-x}\\cdot{p-y}\\cdot{p-z}}}={S}$.")
    # r = S/p
    for (x, y, z, S, r) in ((13, 14, 15, 84, '4'), (5, 12, 13, 30, '2'), (9, 10, 17, 36, '2'), (10, 17, 21, 84, '3,5')):
        p = (x + y + z) // 2
        assert abs(S / p - float(r.replace(',', '.'))) < 1e-9
        b.mc(B6, 'th', 'Bán kính đường tròn nội tiếp', f"Tam giác có ba cạnh {x}, {y}, {z}. Bán kính đường tròn nội tiếp $r$ bằng:",
             M(r), [M(str(S)), M(fnum(S / (2 * p))), M(fnum(S / (p - 1)))],
             f"Có $p={p}$ và $S={S}$ (công thức Heron). Do $S=pr$ nên $r=\\frac{{S}}{{p}}=\\frac{{{S}}}{{{p}}}={r}$.")
    # R = abc/4S
    for (x, y, z, S, R) in ((3, 4, 5, 6, '2,5'), (5, 12, 13, 30, '6,5'), (13, 14, 15, 84, '8,125')):
        assert abs(x * y * z / (4 * S) - float(R.replace(',', '.'))) < 1e-9
        b.mc(B6, 'vd', 'Bán kính đường tròn ngoại tiếp', f"Tam giác có ba cạnh {x}, {y}, {z}. Bán kính đường tròn ngoại tiếp $R$ bằng:",
             M(R), [M(fnum(x * y * z / (2 * S))), M(fnum(S / ((x + y + z) / 2))), M(fnum(x * y * z / S))],
             f"Diện tích tam giác là $S={S}$. Từ $S=\\frac{{abc}}{{4R}}$ suy ra $R=\\frac{{abc}}{{4S}}=\\frac{{{x*y*z}}}{{{4*S}}}={R}$.")
    # trung tuyến
    med = []
    for a in range(2, 20):
        for bb in range(2, 20):
            for cc in range(bb, 20):
                if abs(a - bb) < cc < a + bb:
                    m2 = Fraction(2 * bb * bb + 2 * cc * cc - a * a, 4)
                    if m2.denominator == 1 and int(math.isqrt(int(m2))) ** 2 == int(m2) and bb != cc and len(med) < 60:
                        med.append((a, bb, cc, math.isqrt(int(m2))))
    for (a, bb, cc, m) in med[2:60:13][:4]:
        b.mc(B6, 'vd', 'Độ dài đường trung tuyến', f"Tam giác $ABC$ có $a={a}$, $b={bb}$, $c={cc}$. Độ dài trung tuyến $m_a$ bằng:",
             M(str(m)), [M(str(m + 1)), M(rad(2 * bb * bb + 2 * cc * cc - a * a)), M(rad(bb * bb + cc * cc - a * a))],
             f"$m_a^2=\\frac{{2(b^2+c^2)-a^2}}{{4}}=\\frac{{2({bb*bb}+{cc*cc})-{a*a}}}{{4}}={m*m}$ nên $m_a={m}$.")
    # giải tam giác: góc C
    for (A, Bg) in ((50, 60), (45, 75), (35, 95)):
        b.mc(B6, 'nb', 'Giải tam giác: tìm góc', f"Tam giác $ABC$ có $A={A}^\\circ$, $B={Bg}^\\circ$. Số đo góc $C$ bằng:",
             M(f'{180-A-Bg}^\\circ'), [M(f'{A+Bg}^\\circ'), M(f'{360-A-Bg}^\\circ'), M(f'{90-A}^\\circ')],
             f"Tổng ba góc của tam giác bằng $180^\\circ$ nên $C=180^\\circ-{A}^\\circ-{Bg}^\\circ={180-A-Bg}^\\circ$.")
    # sin law: tính cạnh
    for (a, A, Bg, res, sym) in ((10, 30, 90, 20, '20'), (10, 30, 60, 10 * math.sqrt(3), '10\\sqrt{3}'), (6, 30, 45, 6 * math.sqrt(2), '6\\sqrt{2}'), (8, 45, 90, 8 * math.sqrt(2), '8\\sqrt{2}')):
        sA = {30: 0.5, 45: math.sqrt(2) / 2}[A]; sB = {90: 1, 60: math.sqrt(3) / 2, 45: math.sqrt(2) / 2}[Bg]
        assert abs(a * sB / sA - res) < 1e-9
        b.mc(B6, 'th', 'Định lí sin: tính cạnh', f"Tam giác $ABC$ có $a={a}$, $A={A}^\\circ$, $B={Bg}^\\circ$. Độ dài cạnh $b$ bằng:",
             M(sym), [M(str(a)), M(rad(a * 3)), M(str(a * 3)), M(str(a * 2)), M('7')],
             f"Định lí sin: $\\frac{{a}}{{\\sin A}}=\\frac{{b}}{{\\sin B}}$ nên $b=\\frac{{a\\sin B}}{{\\sin A}}=\\frac{{{a}\\sin {Bg}^\\circ}}{{\\sin {A}^\\circ}}={sym}$.")
    # nhọn / tù / vuông
    for (x, y, z, kind) in ((5, 6, 7, 'nhọn'), (4, 5, 7, 'tù'), (3, 4, 5, 'vuông'), (6, 8, 10, 'vuông'), (7, 8, 9, 'nhọn'), (2, 3, 4, 'tù')):
        big = max(x, y, z); rest = [t for t in (x, y, z) if t != big or True]
        s2 = sorted((x, y, z)); lhs, rhs = s2[2] ** 2, s2[0] ** 2 + s2[1] ** 2
        assert kind == ('vuông' if lhs == rhs else ('tù' if lhs > rhs else 'nhọn'))
        b.mc(B6, 'th', 'Nhận dạng tam giác theo cạnh', f"Tam giác có ba cạnh {x}, {y}, {z} là tam giác:",
             f"Tam giác {kind}", [f"Tam giác {k}" for k in ('nhọn', 'tù', 'vuông') if k != kind] + ['Tam giác đều'],
             f"Cạnh lớn nhất là {s2[2]} có ${s2[2]}^2={lhs}$, còn ${s2[0]}^2+{s2[1]}^2={rhs}$. Vì ${lhs}{'=' if lhs==rhs else ('>' if lhs>rhs else '<')}{rhs}$ nên tam giác {kind} (theo định lí côsin cho góc đối diện cạnh lớn nhất).")
    # ứng dụng: hai tàu
    for (k, d1, d2, dist) in ((3, 15, 24, 21), (4, 20, 32, 28), (2, 10, 16, 14)):
        b.mc(B6, 'vd', 'Ứng dụng định lí côsin', f"Hai tàu cùng rời cảng, đi theo hai hướng tạo với nhau góc $60^\\circ$. Sau một giờ, tàu thứ nhất cách cảng {d1} km, tàu thứ hai cách cảng {d2} km. Khoảng cách giữa hai tàu lúc đó là:",
             f"{dist} km", [f"{dist+4} km", f"{d1+d2} km", f"{d2-d1} km"],
             f"Gọi $O$ là cảng. Theo định lí côsin: $d^2={d1}^2+{d2}^2-2\\cdot{d1}\\cdot{d2}\\cos 60^\\circ={dist*dist}$ nên $d={dist}$ km.")
    # ứng dụng: chiều cao tháp
    for (d, sym) in ((20, '10\\sqrt{3}'), (30, '15\\sqrt{3}')):
        h = d * math.sqrt(3) / 2
        assert abs(h - (10 * math.sqrt(3) if d == 20 else 15 * math.sqrt(3))) < 1e-9
        b.mc(B6, 'vd', 'Ứng dụng: chiều cao', f"Từ hai điểm $A$, $B$ thẳng hàng với chân tháp, cách nhau {d} m, người ta nhìn đỉnh tháp với góc nâng lần lượt là $30^\\circ$ (tại $A$) và $60^\\circ$ (tại $B$, $B$ gần tháp hơn). Chiều cao tháp bằng:",
             f"${sym}$ m", [f"${d}$ m", f"${d+10}$ m", f"${d//2}$ m"],
             f"Góc $\\angle ADB=60^\\circ-30^\\circ=30^\\circ=\\angle DAB$ nên tam giác $ABD$ cân tại $B$, suy ra $BD=AB={d}$ m. Chiều cao tháp $h=BD\\sin 60^\\circ={d}\\cdot\\frac{{\\sqrt{{3}}}}{{2}}={sym}$ m.")

    # ===== Câu trả lời ngắn =====
    for bb, cc, A, a2 in cos_cases[:6]:
        b.sa(B6, 'th', 'Định lí côsin: tính cạnh', f"Tam giác $ABC$ có $b={bb}$, $c={cc}$, $A={A}^\\circ$. Tính độ dài cạnh $a$ (làm tròn đến hàng phần trăm nếu cần).",
             math.sqrt(a2), f"$a^2=b^2+c^2-2bc\\cos A={a2}$ nên $a=\\sqrt{{{a2}}}={fnum(math.sqrt(a2))}$.", tol=0.01)
    for (a, bb, cc) in ((4, 5, 6), (5, 6, 7), (6, 7, 8), (7, 9, 10)):
        cosA = Fraction(bb * bb + cc * cc - a * a, 2 * bb * cc)
        b.sa(B6, 'th', 'Định lí côsin: tính cos góc', f"Tam giác $ABC$ có $a={a}$, $b={bb}$, $c={cc}$. Tính $\\cos A$ (làm tròn đến hàng phần trăm).",
             float(cosA), f"$\\cos A=\\frac{{b^2+c^2-a^2}}{{2bc}}=\\frac{{{bb*bb+cc*cc-a*a}}}{{{2*bb*cc}}}\\approx {fnum(float(cosA))}$.", tol=0.01)
    for (bb, cc, A, S) in ((6, 8, 30, 12), (10, 12, 150, 30), (8, 9, 30, 18), (5, 8, 30, 10)):
        b.sa(B6, 'th', 'Diện tích tam giác', f"Tam giác $ABC$ có $b={bb}$, $c={cc}$, $A={A}^\\circ$. Tính diện tích tam giác.",
             S, f"$S=\\frac{{1}}{{2}}bc\\sin A=\\frac{{1}}{{2}}\\cdot{bb}\\cdot{cc}\\cdot\\frac{{1}}{{2}}={S}$.")
    for (x, y, z, S) in ((13, 14, 15, 84), (9, 10, 17, 36), (10, 17, 21, 84)):
        p = (x + y + z) // 2
        b.sa(B6, 'th', 'Công thức Heron', f"Tam giác có ba cạnh {x}, {y}, {z}. Tính diện tích tam giác.",
             S, f"$p={p}$, $S=\\sqrt{{{p}\\cdot{p-x}\\cdot{p-y}\\cdot{p-z}}}={S}$.")
    for (x, y, z, S, r) in ((13, 14, 15, 84, 4), (9, 10, 17, 36, 2), (10, 17, 21, 84, 3.5)):
        p = (x + y + z) // 2
        b.sa(B6, 'th', 'Bán kính đường tròn nội tiếp', f"Tam giác có ba cạnh {x}, {y}, {z}. Tính bán kính đường tròn nội tiếp $r$.",
             r, f"$S={S}$, $p={p}$, nên $r=\\frac{{S}}{{p}}={fnum(r)}$.")
    for (x, y, z, S, R) in ((3, 4, 5, 6, 2.5), (5, 12, 13, 30, 6.5), (13, 14, 15, 84, 8.125)):
        b.sa(B6, 'vd', 'Bán kính đường tròn ngoại tiếp', f"Tam giác có ba cạnh {x}, {y}, {z}. Tính bán kính đường tròn ngoại tiếp $R$ (làm tròn đến hàng phần trăm).",
             R, f"$S={S}$, $R=\\frac{{abc}}{{4S}}=\\frac{{{x*y*z}}}{{{4*S}}}={fnum(R, 3)}$.", tol=0.01)
    for (a, bb, cc, ang) in ((7, 5, 8, 60), (7, 3, 5, 120), (13, 8, 15, 60)):
        b.sa(B6, 'th', 'Định lí côsin: tính góc', f"Tam giác $ABC$ có $a={a}$, $b={bb}$, $c={cc}$. Tính số đo góc $A$ (đơn vị: độ).",
             ang, f"$\\cos A=\\frac{{{bb*bb}+{cc*cc}-{a*a}}}{{2\\cdot{bb}\\cdot{cc}}}={frac(Fraction(bb*bb+cc*cc-a*a, 2*bb*cc))}$ nên $A={ang}^\\circ$.", unit='độ')
    for (d, h) in ((20, 10 * math.sqrt(3)), (30, 15 * math.sqrt(3))):
        b.sa(B6, 'vd', 'Ứng dụng: chiều cao', f"Từ hai điểm $A$, $B$ thẳng hàng với chân tháp, cách nhau {d} m, nhìn đỉnh tháp với góc nâng $30^\\circ$ tại $A$ và $60^\\circ$ tại $B$ ($B$ gần tháp hơn). Tính chiều cao tháp (m, làm tròn đến hàng phần trăm).",
             h, f"Tam giác $ABD$ cân tại $B$ nên $BD=AB={d}$; $h=BD\\sin 60^\\circ={d}\\cdot\\frac{{\\sqrt{{3}}}}{{2}}\\approx {fnum(h)}$.", tol=0.01, unit='m')
    # ----- trả lời ngắn Bài 5 -----
    for (p_, q_, r_) in ((3, 5, 4), (5, 13, 12), (8, 17, 15)):
        v = -r_ / q_
        b.sa(B5, 'th', 'Tính cos khi biết sin (góc tù)', f"Cho góc tù $\\alpha$ có $\\sin\\alpha=\\frac{{{p_}}}{{{q_}}}$. Tính $\\cos\\alpha$ (làm tròn đến hàng phần trăm).",
             v, f"$\\cos^2\\alpha=1-\\frac{{{p_*p_}}}{{{q_*q_}}}=\\frac{{{r_*r_}}}{{{q_*q_}}}$; góc tù nên $\\cos\\alpha=-\\frac{{{r_}}}{{{q_}}}\\approx {fnum(v)}$.", tol=0.01)
    for (p_, r_, q_) in ((3, 4, 5), (5, 12, 13)):
        v = r_ / q_
        b.sa(B5, 'th', 'Tính cos khi biết tan (góc nhọn)', f"Cho góc nhọn $\\alpha$ có $\\tan\\alpha=\\frac{{{p_}}}{{{r_}}}$. Tính $\\cos\\alpha$ (làm tròn đến hàng phần trăm).",
             v, f"$\\frac{{1}}{{\\cos^2\\alpha}}=1+\\tan^2\\alpha=\\frac{{{q_*q_}}}{{{r_*r_}}}$ nên $\\cos\\alpha=\\frac{{{r_}}}{{{q_}}}\\approx {fnum(v)}$ (góc nhọn).", tol=0.01)
    for (cv, txt, ang) in (('-\\frac{1}{2}', '-\\frac{1}{2}', 120), ('-\\frac{\\sqrt{3}}{2}', '-\\frac{\\sqrt{3}}{2}', 150), ('-\\frac{\\sqrt{2}}{2}', '-\\frac{\\sqrt{2}}{2}', 135), ('\\frac{\\sqrt{2}}{2}', '\\frac{\\sqrt{2}}{2}', 45)):
        b.sa(B5, 'nb', 'Tìm góc khi biết cos', f"Cho $0^\\circ\\le\\alpha\\le180^\\circ$ và $\\cos\\alpha={cv}$. Tìm số đo $\\alpha$ (đơn vị: độ).",
             ang, f"Trên khoảng $[0^\\circ;180^\\circ]$, $\\cos$ nhận mỗi giá trị đúng một lần. Tra bảng giá trị đặc biệt: $\\cos {ang}^\\circ={cv}$ nên $\\alpha={ang}^\\circ$.", unit='độ')
    return b
