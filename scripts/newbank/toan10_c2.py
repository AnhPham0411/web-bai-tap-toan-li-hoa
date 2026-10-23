# -*- coding: utf-8 -*-
"""Toán 10 - Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn."""
import math
from fractions import Fraction
from itertools import product
from .common import Bank, M, frac, fnum, lin, ineq, holds, vertices

B3, B4 = 'b3', 'b4'

def pt(x, y): return f"({x}; {y})"

def build():
    b = Bank('toan10', 'c2')
    rng = b.rng

    # ===== Bài 3: bất phương trình bậc nhất hai ẩn =====
    # (1) cặp số nào là nghiệm
    cases = [(2, -3, '<=', 6), (1, 2, '>', 4), (3, 1, '>=', 5), (-1, 2, '<', 3), (2, 1, '<=', 4), (1, -1, '>', 2), (4, 3, '<', 12), (-2, 3, '>=', -6)]
    grid = [(x, y) for x in range(-3, 6) for y in range(-3, 6)]
    for (a, bb, op, c) in cases:
        ok = [p for p in grid if holds(a, bb, op, c, *p)]
        bad = [p for p in grid if not holds(a, bb, op, c, *p)]
        r = random_r = (a * 7 + bb * 3 + c) % len(ok)
        good = ok[r]
        wrongs = [bad[(r * 5 + k * 11) % len(bad)] for k in range(3)]
        # chọn điểm sai gần đường biên để có tính "bẫy"
        bad_sorted = sorted(bad, key=lambda p: abs(a * p[0] + bb * p[1] - c))
        wrongs = bad_sorted[:3]
        b.mc(B3, 'nb', 'Kiểm tra nghiệm của bất phương trình', f"Cặp số nào sau đây là một nghiệm của bất phương trình ${ineq(a, bb, op, c)}$?",
             M(pt(*good)), [M(pt(*w)) for w in wrongs],
             f"Thay lần lượt toạ độ vào vế trái: với ${pt(*good)}$ ta có ${a}\\cdot({good[0]})+({bb})\\cdot({good[1]})={a*good[0]+bb*good[1]}$, thoả ${SYMTXT(op)}{c}$. "
             f"Các cặp còn lại không thoả bất phương trình.")
    # (2) nhận dạng BPT bậc nhất hai ẩn
    b.mc(B3, 'nb', 'Nhận dạng bất phương trình bậc nhất hai ẩn', "Bất phương trình nào sau đây là bất phương trình bậc nhất hai ẩn?",
         M('2x-3y\\le 5'), [M('x^2+y>1'), M('xy\\ge 2'), M('\\sqrt{x}+y<3')],
         "Bất phương trình bậc nhất hai ẩn có dạng $ax+by\\le c$ (hoặc $<,\\ge,>$) với $a,b$ không đồng thời bằng $0$. Các biểu thức còn lại chứa $x^2$, $xy$, $\\sqrt{x}$ nên không phải bậc nhất.")
    b.mc(B3, 'nb', 'Nhận dạng bất phương trình bậc nhất hai ẩn', "Bất phương trình nào sau đây KHÔNG phải là bất phương trình bậc nhất hai ẩn?",
         M('x^2+y^2\\le 4'), [M('3x+y>0'), M('x-4y\\ge 1'), M('2y<5')],
         "Dạng $ax+by\\le c$ yêu cầu các ẩn có bậc $1$. Biểu thức $x^2+y^2\\le 4$ có bậc hai nên không phải bậc nhất hai ẩn.")
    # (3) miền nghiệm chứa gốc O hay không
    for (a, bb, op, c) in ((2, 1, '<=', 4), (1, -2, '>', 3), (3, 2, '>=', -1), (1, 1, '<', -2), (2, -1, '>=', 1), (4, 1, '<=', 8)):
        o = holds(a, bb, op, c, 0, 0)
        stmt = "chứa" if o else "không chứa"
        wrong_stmt = "không chứa" if o else "chứa"
        b.mc(B3, 'th', 'Miền nghiệm và gốc toạ độ', f"Miền nghiệm của bất phương trình ${ineq(a, bb, op, c)}$ (kể cả bờ nếu có dấu bằng) có chứa gốc toạ độ $O(0;0)$ không?",
             f"Có" if o else "Không", ["Không" if o else "Có", "Chỉ chứa khi $x>0$", "Chỉ chứa khi $y>0$"],
             f"Thay $x=0,y=0$ vào: vế trái bằng $0$. Ta so sánh $0 {SYMTXT(op)} {c}$: {'đúng' if o else 'sai'}. Vậy miền nghiệm {stmt} gốc $O$.")
    # (4) đường thẳng biên
    for (a, bb, op, c) in ((3, -2, '>=', 6), (1, 4, '<', 8), (-2, 5, '<=', 10)):
        b.mc(B3, 'nb', 'Đường thẳng biên', f"Miền nghiệm của bất phương trình ${ineq(a, bb, op, c)}$ là một nửa mặt phẳng có bờ là đường thẳng nào?",
             M(f"{lin(a, bb)} = {c}"), [M(f"{lin(a, bb)} = {-c}"), M(f"{lin(bb, a)} = {c}"), M(f"{lin(a, -bb)} = {c}")],
             f"Bờ của nửa mặt phẳng nghiệm là đường thẳng thu được khi thay dấu bất đẳng thức bằng dấu bằng: ${lin(a, bb)} = {c}$.")
    # ===== Bài 4: hệ bất phương trình =====
    systems = [
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 1, '<=', 4)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (2, 1, '<=', 6)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 2, '<=', 8)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 1, '<=', 5), (1, 0, '<=', 3)],
        [(1, 0, '>=', 1), (0, 1, '>=', 0), (1, 1, '<=', 5)],
        [(1, 0, '>=', 0), (0, 1, '>=', 1), (2, 1, '<=', 7)],
    ]
    grid2 = [(x, y) for x in range(-2, 8) for y in range(-2, 8)]
    for sys_ in systems:
        inside = [p for p in grid2 if all(holds(a, bb, op, c, *p) for a, bb, op, c in sys_)]
        outside = [p for p in grid2 if not all(holds(a, bb, op, c, *p) for a, bb, op, c in sys_)]
        def margin(p): return min(abs(a * p[0] + bb * p[1] - c) for a, bb, op, c in sys_)
        outside_sorted = sorted(outside, key=lambda p: (margin(p), p))
        good = inside[len(inside) // 2]
        stem_sys = "\\begin{cases}" if False else ""
        sys_txt = ",\\ ".join(ineq(*t) for t in sys_)
        b.mc(B4, 'th', 'Nghiệm của hệ bất phương trình', f"Cặp số nào sau đây là nghiệm của hệ bất phương trình: ${sys_txt}$ ?",
             M(pt(*good)), [M(pt(*w)) for w in outside_sorted[:3]],
             f"Cặp ${pt(*good)}$ thoả đồng thời tất cả các bất phương trình của hệ (thay trực tiếp để kiểm tra). Mỗi cặp còn lại vi phạm ít nhất một bất phương trình nên không là nghiệm của hệ.")
    # miền nghiệm là đa giác: số đỉnh
    for sys_ in systems[:4]:
        vs = vertices(sys_)
        sys_txt = ",\\ ".join(ineq(*t) for t in sys_)
        b.mc(B4, 'th', 'Miền nghiệm của hệ: số đỉnh', f"Miền nghiệm của hệ bất phương trình ${sys_txt}$ là một đa giác lồi có bao nhiêu đỉnh?",
             str(len(vs)), [str(len(vs) + 1), str(len(vs) - 1), str(len(vs) + 2)],
             "Các đỉnh là giao điểm của các đường biên thoả mọi bất phương trình của hệ: " + ", ".join(f"$({frac(x)}; {frac(y)})$" for x, y in vs) + f". Vậy có {len(vs)} đỉnh.")
    # ===== Tối ưu F = px + qy =====
    objs = [(3, 2), (2, 3), (1, 1), (4, 1), (5, 2), (2, 5)]
    lps = [
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 1, '<=', 6), (2, 1, '<=', 8)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 2, '<=', 8), (3, 1, '<=', 9)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 1, '<=', 10), (1, 0, '<=', 6), (0, 1, '<=', 7)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (2, 1, '<=', 10), (1, 1, '<=', 7)],
        [(1, 0, '>=', 0), (0, 1, '>=', 0), (1, 1, '<=', 8), (1, 3, '<=', 18)],
    ]
    count = 0
    for k, sys_ in enumerate(lps):
        vs = vertices(sys_)
        assert all(x.denominator == 1 and y.denominator == 1 for x, y in vs), (sys_, vs)
        for (p, q) in (objs[k % 6], objs[(k + 3) % 6]):
            vals = {(x, y): p * x + q * y for x, y in vs}
            mx = max(vals.values()); mn = min(vals.values())
            sys_txt = ",\\ ".join(ineq(*t) for t in sys_)
            vtxt = ", ".join(f"$({int(x)};{int(y)})$" for x, y in vs)
            others = sorted({int(v) for v in vals.values() if v != mx}, reverse=True) + [int(mx) + 2, int(mx) - 1, int(mx) + 5]
            ex = f"Miền nghiệm là đa giác lồi với các đỉnh {vtxt}. Giá trị $F={lin(p, q, 'x', 'y')}$ tại các đỉnh lần lượt là " + ", ".join(str(int(v)) for v in vals.values()) + "."
            b.mc(B4, 'vd', 'Giá trị lớn nhất của biểu thức F', f"Cho $x,y$ thoả mãn hệ ${sys_txt}$. Giá trị lớn nhất của $F={lin(p, q)}$ bằng:",
                 str(int(mx)), [str(v) for v in others], ex + f" Giá trị lớn nhất là {int(mx)}.")
            b.sa(B4, 'vd', 'Giá trị lớn nhất của biểu thức F', f"Cho $x,y$ thoả mãn hệ ${sys_txt}$. Tìm giá trị lớn nhất của $F={lin(p, q)}$.", int(mx), ex + f" Giá trị lớn nhất là {int(mx)}.")
            mns = sorted({int(v) for v in vals.values() if v != mn}) + [int(mn) - 1, int(mn) + 7, int(mx) + 6]
            b.mc(B4, 'vd', 'Giá trị nhỏ nhất của biểu thức F', f"Cho $x,y$ thoả mãn hệ ${sys_txt}$. Giá trị nhỏ nhất của $F={lin(p, q)}$ bằng:",
                 str(int(mn)), [str(v) for v in mns], ex + f" Giá trị nhỏ nhất là {int(mn)}.")
            count += 1
    # ===== bài toán thực tế =====
    probs = [
        ("Một xưởng sản xuất hai loại sản phẩm $A$ và $B$. Mỗi sản phẩm $A$ cần 2 giờ gia công và 1 giờ lắp ráp; mỗi sản phẩm $B$ cần 1 giờ gia công và 1 giờ lắp ráp. Mỗi ngày xưởng có tối đa 8 giờ gia công và 6 giờ lắp ráp. Lãi mỗi sản phẩm $A$ là 3 triệu đồng, mỗi sản phẩm $B$ là 2 triệu đồng. Hỏi lãi lớn nhất mỗi ngày là bao nhiêu triệu đồng?",
         [(2, 1, '<=', 8), (1, 1, '<=', 6)], (3, 2)),
        ("Một nhà máy sản xuất hai loại bánh $A$ và $B$. Một mẻ bánh $A$ dùng 1 kg bột và 2 kg đường; một mẻ bánh $B$ dùng 3 kg bột và 1 kg đường. Nhà máy có tối đa 9 kg bột và 8 kg đường. Mỗi mẻ $A$ lãi 40 nghìn đồng, mỗi mẻ $B$ lãi 30 nghìn đồng. Lãi lớn nhất là bao nhiêu nghìn đồng?",
         [(1, 3, '<=', 9), (2, 1, '<=', 8)], (40, 30)),
        ("Một cửa hàng bán hai loại nước ép $A$ và $B$. Mỗi ly $A$ cần 2 quả cam và 1 quả táo, mỗi ly $B$ cần 1 quả cam và 2 quả táo. Cửa hàng có tối đa 10 quả cam và 8 quả táo. Mỗi ly $A$ lãi 4 nghìn đồng, mỗi ly $B$ lãi 5 nghìn đồng. Hỏi lãi lớn nhất là bao nhiêu nghìn đồng?",
         [(2, 1, '<=', 10), (1, 2, '<=', 8)], (4, 5)),
    ]
    for (txt, cons, (p, q)) in probs:
        cons2 = [(1, 0, '>=', 0), (0, 1, '>=', 0)] + cons
        vs = vertices(cons2)
        assert all(x.denominator == 1 and y.denominator == 1 for x, y in vs)
        vals = {(int(x), int(y)): p * int(x) + q * int(y) for x, y in vs}
        best = max(vals, key=vals.get); mx = vals[best]
        other = sorted({v for v in vals.values() if v != mx}, reverse=True)
        ex = (f"Gọi $x,y$ là số sản phẩm $A$, $B$ ($x,y\\ge0$). Các ràng buộc cho hệ ${', '.join(ineq(*t) for t in cons2)}$ và mục tiêu $F={lin(p, q)}$. "
              f"Các đỉnh của miền nghiệm: " + ", ".join(f"$({a};{c})$" for a, c in vals) + f". Giá trị $F$ tại các đỉnh: " + ", ".join(str(v) for v in vals.values()) + f". Lớn nhất là {mx} tại $({best[0]};{best[1]})$.")
        b.mc(B4, 'vd', 'Bài toán thực tế: quy hoạch tuyến tính', txt, str(mx), [str(v) for v in other[:3]] + [str(mx + 6)], ex)
        b.sa(B4, 'vd', 'Bài toán thực tế: quy hoạch tuyến tính', txt, mx, ex)
    # đếm nghiệm nguyên
    for (n,) in ((3,), (4,), (5,)):
        cnt = sum(1 for x in range(0, n + 1) for y in range(0, n + 1) if x + y <= n)
        b.sa(B4, 'th', 'Đếm nghiệm nguyên không âm', f"Có bao nhiêu cặp số nguyên $(x;y)$ thoả mãn $x\\ge0,\\ y\\ge0,\\ x+y\\le {n}$?", cnt,
             f"Với mỗi $x=0,1,\\dots,{n}$ thì $y$ nhận các giá trị $0,1,\\dots,{n}-x$, tức có ${n}-x+1$ giá trị. Tổng cộng: " + "+".join(str(n - x + 1) for x in range(n + 1)) + f"={cnt}.")
    for (a, bb, op, c) in ((2, 1, '<=', 4), (1, 3, '<=', 6)):
        cnt = sum(1 for x in range(0, 10) for y in range(0, 10) if holds(a, bb, op, c, x, y))
        b.sa(B4, 'th', 'Đếm nghiệm nguyên không âm', f"Có bao nhiêu cặp số nguyên $(x;y)$ với $x\\ge0,\\ y\\ge0$ thoả mãn ${ineq(a, bb, op, c)}$?", cnt,
             "Liệt kê theo từng giá trị của $x$ và đếm các giá trị nguyên $y\\ge0$ thoả bất phương trình: " + ", ".join(f"$x={x}$: {sum(1 for y in range(0, 10) if holds(a, bb, op, c, x, y))} giá trị" for x in range(0, 8) if any(holds(a, bb, op, c, x, y) for y in range(0, 10))) + f". Tổng: {cnt}.")
    return b

def SYMTXT(op):
    return {'<=': '\\le ', '>=': '\\ge ', '<': '<', '>': '>'}[op]
