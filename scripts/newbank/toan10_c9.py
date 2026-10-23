# -*- coding: utf-8 -*-
"""Toán 10 - Chương IX: Tính xác suất theo định nghĩa cổ điển (đáp án kiểm bằng liệt kê)."""
import math
from itertools import product, combinations
from fractions import Fraction
from .common import Bank, M, frac

B26, B27 = 'b26', 'b27'

def pf(p): return M(frac(p))
def dist(p):
    """Các đáp án nhiễu hợp lý cho một xác suất p."""
    p = Fraction(p)
    out = []
    for q in (1 - p, p / 2, Fraction(p.numerator + 1, p.denominator), Fraction(p.numerator, p.denominator + 1), Fraction(p.numerator, max(p.denominator - 1, 1)), Fraction(1, p.denominator), min(p * 2, Fraction(9, 10))):
        if q != p and q not in out and 0 < q < 1: out.append(q)
    return [pf(q) for q in out]

def build():
    b = Bank('toan10', 'c9')
    # ===== Bài 26: biến cố và định nghĩa cổ điển =====
    for k in (2, 3, 4):
        b.mc(B26, 'nb', 'Không gian mẫu (đồng xu)', f"Gieo {k} đồng xu cân đối, đồng chất. Số phần tử của không gian mẫu là:", str(2 ** k),
             [str(2 * k), str(k * k), str(2 ** k + 2)], f"Mỗi đồng xu có $2$ kết quả (sấp, ngửa) nên có ${2**k}$ kết quả: $2^{k}={2**k}$.")
    for k in (1, 2, 3):
        b.mc(B26, 'nb', 'Không gian mẫu (xúc xắc)', f"Gieo {'một' if k == 1 else k} con xúc xắc cân đối, đồng chất{' một lần' if k == 1 else ''}. Số phần tử của không gian mẫu là:", str(6 ** k),
             [str(6 * k), str(6 ** k + 6), str(k ** 6 if k != 1 else 5)], f"Mỗi con xúc xắc có $6$ mặt nên $n(\\Omega)=6^{k}={6**k}$.")
    for (n, k) in ((5, 2), (6, 3), (7, 2), (8, 3)):
        b.mc(B26, 'nb', 'Không gian mẫu (chọn ngẫu nhiên)', f"Chọn ngẫu nhiên {k} học sinh từ một tổ có {n} học sinh. Số phần tử của không gian mẫu là:", str(math.comb(n, k)),
             [str(math.perm(n, k)), str(n * k), str(math.comb(n, k) + n)], f"Số cách chọn {k} bạn từ {n} bạn là $C_{{{n}}}^{{{k}}}={math.comb(n, k)}$, nên $n(\\Omega)={math.comb(n, k)}$.")
    b.mc(B26, 'nb', 'Xác suất biến cố chắc chắn', "Xác suất của biến cố chắc chắn $\\Omega$ bằng:", "$1$", ["$0$", "$\\frac{1}{2}$", "Không xác định"], "Biến cố chắc chắn luôn xảy ra, nên $P(\\Omega)=\\frac{n(\\Omega)}{n(\\Omega)}=1$.")
    b.mc(B26, 'nb', 'Xác suất biến cố không thể', "Xác suất của biến cố không thể $\\emptyset$ bằng:", "$0$", ["$1$", "$\\frac{1}{2}$", "Không xác định"], "Biến cố không thể không bao giờ xảy ra: $P(\\emptyset)=\\frac{0}{n(\\Omega)}=0$.")
    b.mc(B26, 'nb', 'Tính chất xác suất', "Với mọi biến cố $A$, khẳng định nào sau đây luôn đúng?", M('0\\le P(A)\\le1'), [M('P(A)>1'), M('P(A)<0'), M('0<P(A)<1')], "Xác suất của một biến cố luôn nằm trong đoạn $[0;1]$ (có thể bằng $0$ hoặc $1$).")
    b.mc(B26, 'nb', 'Định nghĩa cổ điển', "Phép thử có không gian mẫu $\\Omega$ gồm hữu hạn kết quả đồng khả năng. Xác suất của biến cố $A$ là:", M('P(A)=\\frac{n(A)}{n(\\Omega)}'), [M('P(A)=\\frac{n(\\Omega)}{n(A)}'), M('P(A)=n(A)\\cdot n(\\Omega)'), M('P(A)=n(A)-n(\\Omega)')], "Theo định nghĩa cổ điển, $P(A)$ bằng tỉ số giữa số kết quả thuận lợi cho $A$ và số phần tử của không gian mẫu.")
    for pA in (Fraction(1, 5), Fraction(3, 10), Fraction(2, 5), Fraction(3, 4)):
        q = 1 - pA
        b.mc(B26, 'nb', 'Xác suất biến cố đối', f"Biến cố $A$ có xác suất $P(A)={frac(pA)}$. Xác suất của biến cố đối $\\overline{{A}}$ là:", pf(q),
             [pf(pA), pf(Fraction(1, 2)) if Fraction(1, 2) != q else pf(Fraction(1, 3)), pf(q / 2), M('1')],
             f"$P(\\overline{{A}})=1-P(A)=1-{frac(pA)}={frac(q)}$.")
    one_die = [("xuất hiện mặt có số chấm là số chẵn", lambda x: x % 2 == 0), ("xuất hiện mặt có số chấm lớn hơn 4", lambda x: x > 4), ("số chấm xuất hiện chia hết cho 3", lambda x: x % 3 == 0),
               ("xuất hiện mặt có số chấm là số nguyên tố", lambda x: x in (2, 3, 5)), ("xuất hiện mặt có số chấm không lớn hơn 2", lambda x: x <= 2), ("xuất hiện mặt có số chấm là số lẻ", lambda x: x % 2 == 1)]
    for (txt, f) in one_die:
        fav = [x for x in range(1, 7) if f(x)]
        p = Fraction(len(fav), 6)
        b.mc(B26, 'th', 'Xác suất (một xúc xắc)', f"Gieo một con xúc xắc cân đối, đồng chất. Xác suất để {txt} là:", pf(p), dist(p),
             f"$n(\\Omega)=6$. Các kết quả thuận lợi: {', '.join(map(str, fav))}, nên $n(A)={len(fav)}$ và $P(A)=\\frac{{{len(fav)}}}{{6}}={frac(p)}$.")
    for (r, g) in ((1, 2), (2, 3), (3, 4), (4, 1), (5, 3)):
        p = Fraction(g, r + g)
        b.mc(B26, 'th', 'Xác suất lấy một viên bi', f"Một hộp có {r} viên bi đỏ và {g} viên bi xanh có cùng kích thước. Lấy ngẫu nhiên một viên. Xác suất lấy được viên bi xanh là:", pf(p), dist(p),
             f"Tổng số bi là ${r+g}$, số bi xanh là ${g}$ nên $P=\\frac{{{g}}}{{{r+g}}}={frac(p)}$.")
    for (lo, hi, k, label) in ((1, 20, 2, 'chẵn'), (10, 99, 5, 'chia hết cho 5'), (1, 30, 3, 'chia hết cho 3'), (1, 10, None, 'nguyên tố')):
        nums = list(range(lo, hi + 1))
        if k: fav = [x for x in nums if x % k == 0]
        else: fav = [x for x in nums if x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))]
        p = Fraction(len(fav), len(nums))
        b.mc(B26, 'th', 'Xác suất chọn số', f"Chọn ngẫu nhiên một số nguyên từ {lo} đến {hi}. Xác suất để số được chọn là số {label} là:", pf(p), dist(p),
             f"Có ${len(nums)}$ số từ {lo} đến {hi}, trong đó có ${len(fav)}$ số {label}. Vậy $P=\\frac{{{len(fav)}}}{{{len(nums)}}}={frac(p)}$.")
    # ===== Bài 27: thực hành =====
    two = list(product(range(1, 7), repeat=2))
    for (txt, f) in (("tổng số chấm bằng 7", lambda t: t[0] + t[1] == 7), ("hai mặt có số chấm bằng nhau", lambda t: t[0] == t[1]), ("tổng số chấm bằng 8", lambda t: t[0] + t[1] == 8),
                     ("tổng số chấm nhỏ hơn 5", lambda t: t[0] + t[1] < 5), ("có ít nhất một con xuất hiện mặt 6", lambda t: 6 in t), ("tích số chấm là số lẻ", lambda t: (t[0] * t[1]) % 2 == 1),
                     ("tổng số chấm là số chẵn", lambda t: (t[0] + t[1]) % 2 == 0), ("hiệu hai số chấm bằng 1", lambda t: abs(t[0] - t[1]) == 1)):
        fav = [t for t in two if f(t)]
        p = Fraction(len(fav), 36)
        b.mc(B27, 'th', 'Xác suất (hai xúc xắc)', f"Gieo đồng thời hai con xúc xắc cân đối, đồng chất. Xác suất để {txt} là:", pf(p), dist(p),
             f"$n(\\Omega)=6\\times6=36$. Số kết quả thuận lợi (đếm trực tiếp) là ${len(fav)}$, nên $P=\\frac{{{len(fav)}}}{{36}}={frac(p)}$.")
        if len(fav) in (6, 4, 10, 5):
            b.sa(B27, 'th', 'Xác suất (hai xúc xắc)', f"Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để {txt} (làm tròn đến hàng phần trăm).", float(p),
                 f"$n(\\Omega)=36$, số kết quả thuận lợi là ${len(fav)}$ nên $P=\\frac{{{len(fav)}}}{{36}}\\approx{float(p):.2f}$.".replace('.', ','), tol=0.01)
    for (txt, f) in (("xuất hiện ít nhất một mặt sấp", lambda t: 'S' in t), ("xuất hiện đúng hai mặt sấp", lambda t: t.count('S') == 2), ("cả ba đồng xu đều ngửa", lambda t: t.count('N') == 3), ("xuất hiện đúng một mặt ngửa", lambda t: t.count('N') == 1)):
        outs = list(product('SN', repeat=3)); fav = [t for t in outs if f(t)]; p = Fraction(len(fav), 8)
        b.mc(B27, 'th', 'Xác suất (ba đồng xu)', f"Gieo ba đồng xu cân đối, đồng chất. Xác suất để {txt} là:", pf(p), dist(p),
             f"$n(\\Omega)=2^3=8$. Số kết quả thuận lợi (liệt kê) là ${len(fav)}$, nên $P=\\frac{{{len(fav)}}}{{8}}={frac(p)}$.")
        b.sa(B27, 'th', 'Xác suất (ba đồng xu)', f"Gieo ba đồng xu cân đối. Tính xác suất để {txt} (làm tròn đến hàng phần trăm).", float(p),
             f"$n(\\Omega)=8$, số kết quả thuận lợi là ${len(fav)}$, nên $P=\\frac{{{len(fav)}}}{{8}}={float(p):.3f}$.".replace('.', ','), tol=0.01)
    for (r, g, k, txt, f) in ((3, 2, 2, "cả hai viên đều đỏ", lambda c: all(x == 'r' for x in c)), (3, 2, 2, "hai viên khác màu", lambda c: len(set(c)) == 2), (3, 2, 2, "có ít nhất một viên đỏ", lambda c: 'r' in c),
                              (4, 3, 2, "hai viên cùng màu", lambda c: len(set(c)) == 1), (4, 3, 3, "ba viên đều đỏ", lambda c: all(x == 'r' for x in c)), (5, 3, 2, "hai viên khác màu", lambda c: len(set(c)) == 2)):
        balls = ['r'] * r + ['g'] * g
        outs = list(combinations(range(len(balls)), k)); fav = [c for c in outs if f([balls[i] for i in c])]
        p = Fraction(len(fav), len(outs))
        b.mc(B27, 'vd', 'Xác suất lấy bi', f"Một hộp có {r} viên bi đỏ và {g} viên bi xanh có cùng kích thước. Lấy ngẫu nhiên đồng thời {k} viên bi. Xác suất để {txt} là:", pf(p), dist(p),
             f"$n(\\Omega)=C_{{{r+g}}}^{{{k}}}={len(outs)}$. Số kết quả thuận lợi (đếm theo cách chọn) là ${len(fav)}$, nên $P=\\frac{{{len(fav)}}}{{{len(outs)}}}={frac(p)}$.")
        b.sa(B27, 'vd', 'Xác suất lấy bi', f"Hộp có {r} bi đỏ và {g} bi xanh. Lấy ngẫu nhiên đồng thời {k} viên. Tính xác suất để {txt} (làm tròn đến hàng phần trăm).", float(p),
             f"$n(\\Omega)=C_{{{r+g}}}^{{{k}}}={len(outs)}$; số kết quả thuận lợi là ${len(fav)}$, nên $P=\\frac{{{len(fav)}}}{{{len(outs)}}}\\approx{float(p):.3f}$.".replace('.', ','), tol=0.01)
    for (nam, nu, txt, f) in ((3, 2, "có ít nhất một bạn nữ", lambda c: 'n' in c), (4, 3, "cả hai bạn đều là nam", lambda c: all(x == 'm' for x in c)), (5, 4, "có đúng một bạn nữ", lambda c: c.count('n') == 1), (3, 3, "hai bạn cùng giới", lambda c: len(set(c)) == 1)):
        pp = ['m'] * nam + ['n'] * nu
        outs = list(combinations(range(len(pp)), 2)); fav = [c for c in outs if f([pp[i] for i in c])]
        p = Fraction(len(fav), len(outs))
        b.mc(B27, 'vd', 'Xác suất chọn học sinh', f"Một tổ có {nam} bạn nam và {nu} bạn nữ. Chọn ngẫu nhiên 2 bạn. Xác suất để {txt} là:", pf(p), dist(p),
             f"$n(\\Omega)=C_{{{nam+nu}}}^2={len(outs)}$. Số cách chọn thuận lợi là ${len(fav)}$ nên $P=\\frac{{{len(fav)}}}{{{len(outs)}}}={frac(p)}$.")
    for (n, txt, f) in ((3, "ba chữ số đôi một khác nhau lập từ {1,2,3,4,5}", None),):
        pass
    for N in (50, 100):
        fav = [x for x in range(1, N + 1) if x % 3 == 0 or x % 5 == 0]
        p = Fraction(len(fav), N)
        b.mc(B27, 'vd', 'Xác suất chọn số (hợp hai điều kiện)', f"Chọn ngẫu nhiên một số nguyên từ 1 đến {N}. Xác suất để số được chọn chia hết cho $3$ hoặc chia hết cho $5$ là:", pf(p), dist(p),
             f"Có ${N//3}$ số chia hết cho 3, ${N//5}$ số chia hết cho 5 và ${N//15}$ số chia hết cho 15. Số thuận lợi: ${N//3}+{N//5}-{N//15}={len(fav)}$. Vậy $P=\\frac{{{len(fav)}}}{{{N}}}={frac(p)}$.")
    return b
