# -*- coding: utf-8 -*-
"""Toán 10 - Chương VI: Hàm số, đồ thị và ứng dụng (tự kiểm bằng code)."""
import math
from fractions import Fraction
from .common import Bank, M, frac, fnum

B15, B16, B17, B18 = 'b15', 'b16', 'b17', 'b18'

def sgn(n): return '+' if n >= 0 else '-'
def quad(a, b, c, v='x'):
    out = ''
    for coef, p in ((a, f'{v}^2'), (b, v), (c, '')):
        if coef == 0: continue
        mag = abs(coef)
        t = (p if (mag == 1 and p) else f'{mag}{p}')
        out += (('-' if coef < 0 else '') + t) if not out else f" {sgn(coef)} {t}"
    return out or '0'
def vtx(h, k): return f"I({frac(h)}; {frac(k)})"
def R_minus(*pts):
    return "\\mathbb{R}\\setminus\\{" + ", ".join(str(p) for p in pts) + "\\}"
def interval(l, r, lc='(', rc=')'):
    ls = '-\\infty' if l is None else str(l); rs = '+\\infty' if r is None else str(r)
    return f"{lc if l is not None else '('}{ls}; {rs}{rc if r is not None else ')'}"

def build():
    b = Bank('toan10', 'c6')

    # ===== Bài 15: hàm số =====
    for a in (2, 3, 4, 5):
        b.mc(B15, 'nb', 'Tập xác định (mẫu số)', f"Tập xác định của hàm số $y=\\frac{{1}}{{x-{a}}}$ là:", M(R_minus(a)),
             [M(R_minus(-a)), M(interval(a, None)), M('\\mathbb{R}')],
             f"Hàm số xác định khi mẫu số khác $0$: $x-{a}\\ne0\\iff x\\ne{a}$. Vậy $D={R_minus(a)}$.")
        b.mc(B15, 'nb', 'Tập xác định (căn bậc hai)', f"Tập xác định của hàm số $y=\\sqrt{{{a}-x}}$ là:", M(interval(None, a, '(', ']')),
             [M(interval(None, a)), M(interval(a, None, '[', ')')), M(interval(a, None))],
             f"Điều kiện: ${a}-x\\ge0\\iff x\\le{a}$. Vậy $D=(-\\infty; {a}]$.")
        b.mc(B15, 'nb', 'Tập xác định (căn bậc hai)', f"Tập xác định của hàm số $y=\\sqrt{{x-{a}}}$ là:", M(interval(a, None, '[', ')')),
             [M(interval(a, None)), M(interval(None, a, '(', ']')), M(interval(-a, None, '[', ')'))],
             f"Điều kiện: $x-{a}\\ge0\\iff x\\ge{a}$. Vậy $D=[{a}; +\\infty)$.")
    for a in (1, 2, 3):
        b.mc(B15, 'th', 'Tập xác định (căn ở mẫu)', f"Tập xác định của hàm số $y=\\frac{{1}}{{\\sqrt{{x-{a}}}}}$ là:", M(interval(a, None)),
             [M(interval(a, None, '[', ')')), M(interval(None, a)), M(R_minus(a))],
             f"Cần $x-{a}>0$ (căn ở mẫu nên không được bằng $0$). Vậy $D=({a}; +\\infty)$.")
    for a, c in ((1, 4), (2, 5), (3, 6)):
        b.mc(B15, 'th', 'Tập xác định (kết hợp)', f"Tập xác định của hàm số $y=\\sqrt{{x-{a}}}+\\frac{{1}}{{x-{c}}}$ là:", M(f"{interval(a, None, '[', ')')}\\setminus\\{{{c}\\}}"),
             [M(interval(a, None, '[', ')')), M(R_minus(c)), M(f"{interval(a, None)}\\setminus\\{{{c}\\}}")],
             f"Cần đồng thời $x-{a}\\ge0$ và $x-{c}\\ne0$, tức $x\\ge{a}$ và $x\\ne{c}$. Vì ${c}>{a}$ nên $D=[{a}; +\\infty)\\setminus\\{{{c}\\}}$.")
    for (a, bb) in ((2, -1), (3, 2), (-1, 4), (1, -3)):
        pts = [(x, a * x + bb) for x in (-1, 0, 1, 2, 3)]
        good = pts[2]
        bad = [(good[0], good[1] + 1), (good[0] + 1, good[1]), (good[1], good[0]), (good[0] + 2, good[1] - 1), (good[0] - 1, good[1] + 3)]
        b.mc(B15, 'nb', 'Điểm thuộc đồ thị', f"Điểm nào sau đây thuộc đồ thị hàm số $y={quad(0, a, bb)}$?", M(f"({good[0]}; {good[1]})"),
             [M(f"({x}; {y})") for x, y in bad],
             f"Thay $x={good[0]}$ vào hàm số: $y={a}\\cdot{good[0]}{sgn(bb)}{abs(bb)}={good[1]}$. Vậy điểm $({good[0]}; {good[1]})$ thuộc đồ thị.")
    for (a, bb, c, x0) in ((1, -2, 3, 2), (2, 1, -1, 3), (-1, 3, 2, -2), (3, 0, -4, 1)):
        v = a * x0 * x0 + bb * x0 + c
        b.sa(B15, 'nb', 'Tính giá trị hàm số', f"Cho hàm số $f(x)={quad(a, bb, c)}$. Tính $f({x0})$.", v,
             f"$f({x0})={a}\\cdot({x0})^2{sgn(bb)}{abs(bb)}\\cdot({x0}){sgn(c)}{abs(c)}={v}$.")
    b.mc(B15, 'nb', 'Tính đơn điệu hàm bậc nhất', "Hàm số $y=3x-5$ đồng biến trên khoảng nào?", M(interval(None, None)),
         [M(interval(None, 0)), M(interval(0, None)), M(interval(None, 5))],
         "Hàm số bậc nhất $y=ax+b$ có $a=3>0$ nên đồng biến trên toàn bộ $\\mathbb{R}$, tức trên $(-\\infty; +\\infty)$.")
    b.mc(B15, 'nb', 'Tính đơn điệu hàm bậc nhất', "Hàm số $y=-2x+7$ nghịch biến trên khoảng nào?", M(interval(None, None)),
         [M(interval(None, 0)), M(interval(0, None)), M(interval(-2, None))],
         "Hàm số bậc nhất $y=ax+b$ có $a=-2<0$ nên nghịch biến trên toàn bộ $\\mathbb{R}$.")
    for (a, bb, x0, y0, m) in ((1, 0, 2, 5, 3), (2, 1, 1, 0, -3), (1, 1, -1, 4, 5)):
        # y = x^2 + b x + m qua (x0,y0): m = y0 - x0^2 - b x0
        mm = y0 - x0 * x0 - bb * x0
        b.mc(B15, 'th', 'Tìm tham số để đồ thị đi qua điểm', f"Đồ thị hàm số $y=x^2{sgn(bb)}{abs(bb) if bb else ''}{'x' if bb else ''}+m$ đi qua điểm $M({x0}; {y0})$ khi $m$ bằng:", M(str(mm)),
             [M(str(-mm)), M(str(mm + 1)), M(str(y0))],
             f"Thay $x={x0},\\ y={y0}$: ${y0}={x0*x0}{sgn(bb*x0)}{abs(bb*x0)}+m$, suy ra $m={mm}$.".replace('+0+', '+'))
    # ===== Bài 16: hàm số bậc hai =====
    combos = [(1, 1, 0), (1, 2, -1), (2, 1, 3), (-1, 2, 5), (-2, 1, 1), (1, 3, -4), (2, 2, 0), (-1, 3, 2), (3, 1, -2), (1, -1, 4)]
    for (a, h, k) in combos:
        bb, c = -2 * a * h, a * h * h + k
        f = quad(a, bb, c)
        shape = "lên trên" if a > 0 else "xuống dưới"
        b.mc(B16, 'th', 'Toạ độ đỉnh parabol', f"Toạ độ đỉnh của parabol $y={f}$ là:", M(f"I({h}; {k})"),
             [M(f"I({-h}; {k})"), M(f"I({h}; {-k})"), M(f"I({k}; {h})"), M(f"I({h + 1}; {k + 2})"), M(f"I({h - 2}; {k + 1})")],
             f"Hoành độ đỉnh $x_I=-\\frac{{b}}{{2a}}=-\\frac{{{bb}}}{{{2*a}}}={h}$. Tung độ đỉnh $y_I={a}\\cdot{h*h}{sgn(bb*h)}{abs(bb*h)}{sgn(c)}{abs(c)}={k}$.".replace('0=', '0='))
        b.mc(B16, 'th', 'Trục đối xứng parabol', f"Trục đối xứng của parabol $y={f}$ là đường thẳng:", M(f"x={h}"),
             [M(f"x={-h}"), M(f"y={h}"), M(f"x={k}"), M(f"x={h + 1}"), M(f"x={h + 3}")],
             f"Trục đối xứng là $x=-\\frac{{b}}{{2a}}=-\\frac{{{bb}}}{{{2*a}}}={h}$.")
        if a > 0:
            b.mc(B16, 'th', 'Giá trị nhỏ nhất của hàm bậc hai', f"Giá trị nhỏ nhất của hàm số $y={f}$ trên $\\mathbb{{R}}$ là:", M(str(k)),
                 [M(str(h)), M(str(-k)), M(str(c))],
                 f"Vì $a={a}>0$ nên hàm số đạt giá trị nhỏ nhất tại đỉnh: $y_{{min}}=y_I={k}$.")
            b.sa(B16, 'th', 'Giá trị nhỏ nhất của hàm bậc hai', f"Tìm giá trị nhỏ nhất của hàm số $y={f}$.", k,
                 f"Đỉnh parabol $I({h}; {k})$ và $a={a}>0$ nên giá trị nhỏ nhất bằng ${k}$.")
        else:
            b.mc(B16, 'th', 'Giá trị lớn nhất của hàm bậc hai', f"Giá trị lớn nhất của hàm số $y={f}$ trên $\\mathbb{{R}}$ là:", M(str(k)),
                 [M(str(h)), M(str(-k)), M(str(c))],
                 f"Vì $a={a}<0$ nên hàm số đạt giá trị lớn nhất tại đỉnh: $y_{{max}}=y_I={k}$.")
            b.sa(B16, 'th', 'Giá trị lớn nhất của hàm bậc hai', f"Tìm giá trị lớn nhất của hàm số $y={f}$.", k,
                 f"Đỉnh parabol $I({h}; {k})$ và $a={a}<0$ nên giá trị lớn nhất bằng ${k}$.")
        inc = interval(h, None) if a > 0 else interval(None, h)
        dec = interval(None, h) if a > 0 else interval(h, None)
        b.mc(B16, 'th', 'Khoảng đồng biến của hàm bậc hai', f"Hàm số $y={f}$ đồng biến trên khoảng nào?", M(inc),
             [M(dec), M(interval(None, None)), M(interval(k, None)), M(interval(h + 2, None)), M(interval(None, h - 1))],
             f"Đỉnh có hoành độ $x_I={h}$ và $a={a}{'>' if a>0 else '<'}0$, nên hàm số đồng biến trên ${inc}$ và nghịch biến trên ${dec}$.")
    for a in (2, -3, 1):
        b.mc(B16, 'nb', 'Bề lõm của parabol', f"Đồ thị hàm số $y={quad(a, 4, -1)}$ có bề lõm:", "Quay lên trên" if a > 0 else "Quay xuống dưới",
             ["Quay xuống dưới" if a > 0 else "Quay lên trên", "Quay sang trái", "Quay sang phải"],
             f"Bề lõm phụ thuộc dấu của hệ số $a={a}$: $a{'>' if a>0 else '<'}0$ nên parabol quay {'lên trên' if a>0 else 'xuống dưới'}.")
    for (a, bb, c) in ((1, 5, -3), (2, -1, 4), (-1, 3, 7)):
        b.mc(B16, 'nb', 'Giao điểm với trục tung', f"Giao điểm của parabol $y={quad(a, bb, c)}$ với trục tung là:", M(f"(0; {c})"),
             [M(f"({c}; 0)"), M(f"(0; {bb})"), M(f"(0; {-c})")],
             f"Giao với trục tung ứng với $x=0$, khi đó $y={c}$. Vậy giao điểm là $(0; {c})$.")
    for (p, q) in ((1, 3), (2, 5), (-1, 4)):
        bb, c = -(p + q), p * q
        b.mc(B16, 'th', 'Giao điểm với trục hoành', f"Hoành độ giao điểm của parabol $y={quad(1, bb, c)}$ với trục hoành là:", M(f"x={p}\\text{{ và }}x={q}"),
             [M(f"x={-p}\\text{{ và }}x={-q}"), M(f"x={p}\\text{{ và }}x={-q}"), M(f"x={p+q}")],
             f"Giải $x^2{sgn(bb)}{abs(bb)}x{sgn(c)}{abs(c)}=0$ ta được $(x-{p})(x-{q})=0$ nên $x={p}$ hoặc $x={q}$.".replace('-(-1)', '+1'))
    for (h, k, x1, y1) in ((1, 1, 2, 2), (2, -1, 3, 1), (1, 3, 3, 11)):
        a = Fraction(y1 - k, (x1 - h) ** 2)
        assert a.denominator == 1
        a = int(a)
        b.mc(B16, 'vd', 'Xác định parabol', f"Parabol $y=ax^2+bx+c$ có đỉnh $I({h}; {k})$ và đi qua điểm $A({x1}; {y1})$. Hệ số $a$ bằng:", M(str(a)),
             [M(str(a + 1)), M(str(-a)), M(str(a * 2))],
             f"Dạng đỉnh: $y=a(x-{h})^2+({k})$. Thay $A({x1}; {y1})$: ${y1}=a\\cdot{(x1-h)**2}+({k})$, suy ra $a={a}$.")
        b.sa(B16, 'vd', 'Xác định parabol', f"Parabol $y=ax^2+bx+c$ có đỉnh $I({h}; {k})$ và đi qua $A({x1}; {y1})$. Tìm $a$.", a,
             f"Viết $y=a(x-{h})^2+({k})$ rồi thay $A$: ${y1}=a\\cdot{(x1-h)**2}+({k})$, vậy $a={a}$.")
    # ===== Bài 17: dấu tam thức =====
    for (a, bb, c) in ((1, -4, 3), (2, 1, -3), (1, 2, 5), (-1, 4, -4), (3, -6, 3), (1, -5, 4)):
        D = bb * bb - 4 * a * c
        b.mc(B17, 'nb', 'Biệt thức Δ', f"Biệt thức $\\Delta$ của tam thức $f(x)={quad(a, bb, c)}$ bằng:", M(str(D)),
             [M(str(bb * bb + 4 * a * c)), M(str(bb * bb - 2 * a * c)), M(str(-D if D else 4))],
             f"$\\Delta=b^2-4ac=({bb})^2-4\\cdot({a})\\cdot({c})={bb*bb}-({4*a*c})={D}$.")
        b.sa(B17, 'nb', 'Biệt thức Δ', f"Tính biệt thức $\\Delta$ của $f(x)={quad(a, bb, c)}$.", D,
             f"$\\Delta=b^2-4ac=({bb})^2-4({a})({c})={D}$.")
    pq = [(1, 3), (2, 5), (-1, 2), (-3, 1), (0, 4), (1, 6)]
    for (p, q) in pq:
        for a in (1, -1):
            bb, c = -a * (p + q), a * p * q
            f = quad(a, bb, c)
            out_ = f"{interval(None, p)}\\cup{interval(q, None)}"
            in_ = interval(p, q)
            sol_pos = in_ if a < 0 else out_          # f > 0
            sol_neg = out_ if a < 0 else in_          # f < 0
            if a == 1 and (p, q) in ((1, 3), (2, 5), (-3, 1)):
                b.mc(B17, 'th', 'Giải bất phương trình bậc hai', f"Tập nghiệm của bất phương trình ${f}<0$ là:", M(sol_neg),
                     [M(sol_pos), M(interval(p, q, '[', ']')), M(f"{interval(None, p, '(', ']')}\\cup{interval(q, None, '[', ')')}")],
                     f"Tam thức có hai nghiệm $x={p}$, $x={q}$ và $a=1>0$. Theo quy tắc 'trong trái, ngoài cùng', $f(x)<0$ trong khoảng giữa hai nghiệm: ${sol_neg}$.")
                b.mc(B17, 'th', 'Giải bất phương trình bậc hai', f"Tập nghiệm của bất phương trình ${f}\\ge0$ là:", M(f"{interval(None, p, '(', ']')}\\cup{interval(q, None, '[', ')')}"),
                     [M(out_), M(interval(p, q, '[', ']')), M(in_)],
                     f"Hai nghiệm $x={p}$, $x={q}$ và $a=1>0$ nên $f(x)\\ge0$ ngoài khoảng hai nghiệm (kể cả nghiệm): $(-\\infty; {p}]\\cup[{q}; +\\infty)$.")
            if a == -1 and (p, q) in ((1, 3), (-1, 2), (0, 4)):
                b.mc(B17, 'th', 'Giải bất phương trình bậc hai', f"Tập nghiệm của bất phương trình ${f}>0$ là:", M(sol_pos),
                     [M(sol_neg), M(interval(p, q, '[', ']')), M(f"{interval(None, p, '(', ']')}\\cup{interval(q, None, '[', ')')}")],
                     f"Tam thức có nghiệm $x={p}$, $x={q}$ và $a=-1<0$, nên $f(x)>0$ trong khoảng giữa hai nghiệm: ${sol_pos}$.")
    for (p, q) in ((1, 5), (-2, 3), (0, 6), (2, 7)):
        cnt = q - p - 1
        bb, c = -(p + q), p * q
        f = quad(1, bb, c)
        b.mc(B17, 'vd', 'Số nghiệm nguyên của bất phương trình', f"Số nghiệm nguyên của bất phương trình ${f}<0$ là:", str(cnt),
             [str(cnt + 1), str(cnt + 2), str(cnt - 1) if cnt > 1 else '0'],
             f"Nghiệm của bất phương trình là $({p}; {q})$. Các số nguyên trong khoảng này là " + ", ".join(str(x) for x in range(p + 1, q)) + f" nên có {cnt} số.")
        b.sa(B17, 'vd', 'Số nghiệm nguyên của bất phương trình', f"Có bao nhiêu số nguyên $x$ thoả mãn ${f}<0$?", cnt,
             f"Nghiệm là $({p}; {q})$. Các số nguyên: " + ", ".join(str(x) for x in range(p + 1, q)) + f" — tổng {cnt} số.")
    for (bb, c, case) in ((2, 3, 'pos'), (-2, 5, 'pos'), (1, 1, 'neg')):
        f = quad(1, bb, c) if case == 'pos' else quad(-1, bb, -c)
        if case == 'pos':
            b.mc(B17, 'th', 'Tam thức có Δ<0', f"Tập nghiệm của bất phương trình ${f}>0$ là:", M('\\mathbb{R}'), [M('\\emptyset'), M(interval(0, None)), M(interval(None, 0))],
                 f"$\\Delta={bb*bb-4*c}<0$ và $a=1>0$ nên $f(x)>0$ với mọi $x$. Tập nghiệm là $\\mathbb{{R}}$.")
        else:
            b.mc(B17, 'th', 'Tam thức có Δ<0', f"Tập nghiệm của bất phương trình ${f}\\ge0$ là:", M('\\emptyset'), [M('\\mathbb{R}'), M(interval(0, None)), M(interval(None, 0))],
                 f"$\\Delta={bb*bb-4*c}<0$ và $a=-1<0$ nên $f(x)<0$ với mọi $x$. Do đó $f(x)\\ge0$ vô nghiệm, tập nghiệm là $\\emptyset$.")
    for k in (1, 2, 3):
        b.mc(B17, 'vd', 'Tìm tham số để bất phương trình nghiệm đúng', f"Tìm $m$ để $x^2-{2*k}x+m>0$ đúng với mọi $x\\in\\mathbb{{R}}$.", M(f"m>{k*k}"),
             [M(f"m>{k}"), M(f"m<{k*k}"), M(f"m\\ge{k*k}"), M(f"m>{k*k + 1}"), M(f"m>{k + 2}")],
             f"Do $a=1>0$ nên cần $\\Delta'<0$: $\\Delta'=(-{k})^2-m={k*k}-m<0\\iff m>{k*k}$.")
        b.sa(B17, 'vd', 'Tìm tham số để bất phương trình nghiệm đúng', f"Tìm số nguyên $m$ nhỏ nhất để $x^2-{2*k}x+m>0$ đúng với mọi $x\\in\\mathbb{{R}}$.", k * k + 1,
             f"Cần $\\Delta'={k*k}-m<0\\iff m>{k*k}$. Số nguyên nhỏ nhất thoả mãn là $m={k*k+1}$.")
    for k in (1, 2):
        b.mc(B17, 'vd', 'Điều kiện phương trình vô nghiệm', f"Phương trình $x^2-{2*k}x+m=0$ vô nghiệm khi và chỉ khi:", M(f"m>{k*k}"),
             [M(f"m<{k*k}"), M(f"m={k*k}"), M(f"m\\le{k*k}")],
             f"Phương trình vô nghiệm khi $\\Delta'=({k})^2-m<0$, tức $m>{k*k}$.")
    # ===== Bài 18: phương trình chứa căn =====
    def solve_sqrt(a, bb, c, d):
        """Giải sqrt(a x + b) = c x + d: trả về (danh sách nghiệm của pt sau bình phương, nghiệm thoả điều kiện)."""
        A, Bq, C = c * c, 2 * c * d - a, d * d - bb
        if A == 0:
            cand = [Fraction(d * d - bb, a)]
        else:
            D = Bq * Bq - 4 * A * C
            if D < 0: return [], []
            r = math.isqrt(D)
            if r * r != D: return None
            cand = sorted({Fraction(-Bq + r, 2 * A), Fraction(-Bq - r, 2 * A)})
        return cand, [x for x in cand if c * x + d >= 0 and a * x + bb >= 0]
    cases = [(1, 3, 1, 1), (2, 1, 1, -1), (1, 2, 1, 0), (3, 1, 1, 1), (2, 4, 0, 2), (1, 7, 1, 1), (4, 1, 2, -1), (1, 1, -1, 3), (2, 8, 1, 2), (1, -1, 1, -3)]
    OR = "\\text{ và }"
    for (a, bb, c, d) in cases:
        res = solve_sqrt(a, bb, c, d)
        if res is None: continue
        cand, s_ = res
        lhs = f"\\sqrt{{{quad(0, a, bb)}}}"; rhs = quad(0, c, d)
        ans = "Vô nghiệm" if not s_ else OR.join([]) .join([]) or (f"x={frac(s_[0])}" if len(s_) == 1 else f"x={frac(s_[0])}{OR}x={frac(s_[1])}")
        base = s_[0] if s_ else Fraction(0)
        pool = [f"x={frac(base + 1)}", "Vô nghiệm" if s_ else "x=0", f"x={frac(base - 1)}", f"x=0{OR}x=1", f"x={frac(base * 2 + 3)}", f"x={frac(base + 4)}"]
        correct = ans if ans == "Vô nghiệm" else M(ans)
        wrong = [w if w == "Vô nghiệm" else M(w) for w in pool]
        cond = f"Điều kiện ${rhs}\\ge0$." if c != 0 else f"Vế phải là hằng số ${d}\\ge0$ nên chỉ cần bình phương hai vế."
        if c != 0:
            eq = f"${quad(0, a, bb)}=({rhs})^2\\iff {quad(c * c, 2 * c * d - a, d * d - bb)}=0$"
        else:
            eq = f"${quad(0, a, bb)}={d * d}$"
        roots_txt = ", ".join(f"$x={frac(x)}$" for x in cand) if cand else "không có nghiệm thực"
        check_txt = ""
        if cand:
            check_txt = " Kiểm tra: " + "; ".join(f"$x={frac(x)}$: vế phải $={frac(c*x+d)}$ ({'nhận' if (c*x+d>=0 and a*x+bb>=0) else 'loại'})" for x in cand) + "."
        expl = f"{cond} Bình phương hai vế: {eq}, nghiệm: {roots_txt}.{check_txt}"
        b.mc(B18, 'vd', 'Phương trình chứa căn', f"Nghiệm của phương trình ${lhs}={rhs}$ là:", correct, wrong, expl)
        b.sa(B18, 'vd', 'Phương trình chứa căn', f"Phương trình ${lhs}={rhs}$ có bao nhiêu nghiệm thực?", len(s_), expl + f" Vậy có {len(s_)} nghiệm.")
    for (a, bb, c, d, x0) in ((2, 3, 1, 5, 2), (3, 1, 2, 4, 3), (1, 5, 2, 3, 4)):
        # sqrt(a x + b) = sqrt(c x + d): nghiệm x0 = (d-b)/(a-c)
        x = Fraction(d - bb, a - c)
        ok = a * x + bb >= 0
        ans = f"x={frac(x)}" if ok else "Vô nghiệm"
        b.mc(B18, 'th', 'Phương trình căn bằng căn', f"Nghiệm của phương trình $\\sqrt{{{quad(0, a, bb)}}}=\\sqrt{{{quad(0, c, d)}}}$ là:", M(ans) if ok else ans,
             [M(f"x={frac(-x)}"), M(f"x={frac(x + 1)}"), "Vô nghiệm" if ok else M("x=1")],
             f"Bình phương hai vế: ${quad(0, a, bb)}={quad(0, c, d)}$, suy ra $x={frac(x)}$. Thử lại: ${quad(0, a, bb)}$ tại $x={frac(x)}$ bằng ${frac(a*x+bb)}\\ge0$ nên thoả mãn.")
    for k in (1, 2, 3):
        b.mc(B18, 'th', 'Điều kiện xác định', f"Điều kiện xác định của phương trình $\\sqrt{{x-{k}}}=x-{k+1}$ là:", M(f"x\\ge{k}"),
             [M(f"x>{k}"), M(f"x\\ge{k+1}"), M(f"x\\le{k}")],
             f"Biểu thức dưới căn phải không âm: $x-{k}\\ge0\\iff x\\ge{k}$.")
    # phương trình căn bậc hai của bình phương
    b.mc(B18, 'th', 'Căn của bình phương', "Số nghiệm của phương trình $\\sqrt{x^2-4x+4}=x-2$ là:", "Vô số nghiệm", ["Một nghiệm", "Hai nghiệm", "Vô nghiệm"],
         "Ta có $\\sqrt{x^2-4x+4}=|x-2|$. Phương trình trở thành $|x-2|=x-2$, đúng khi và chỉ khi $x\\ge2$. Vậy có vô số nghiệm (mọi $x\\ge2$).")
    b.mc(B18, 'th', 'Căn của bình phương', "Tập nghiệm của phương trình $\\sqrt{x^2+2x+1}=x+1$ là:", M('[-1; +\\infty)'), [M('\\{-1\\}'), M('\\{0\\}'), M('\\emptyset')],
         "Ta có $\\sqrt{x^2+2x+1}=|x+1|$. Phương trình trở thành $|x+1|=x+1$, đúng khi và chỉ khi $x+1\\ge0\\iff x\\ge-1$. Tập nghiệm là $[-1; +\\infty)$.")
    return b
