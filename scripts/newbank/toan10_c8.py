# -*- coding: utf-8 -*-
"""Toán 10 - Chương VIII: Đại số tổ hợp (đáp án kiểm bằng đếm trực tiếp)."""
import math
from itertools import permutations, combinations, product
from fractions import Fraction
from .common import Bank, M

B23, B24, B25 = 'b23', 'b24', 'b25'

def build():
    b = Bank('toan10', 'c8')
    # ===== Bài 23: quy tắc đếm =====
    for (m_, v_) in ((3, 4), (5, 6), (7, 2), (8, 5)):
        b.mc(B23, 'nb', 'Quy tắc cộng', f"Một học sinh có {m_} quyển sách Toán và {v_} quyển sách Văn (các quyển đều khác nhau). Có bao nhiêu cách chọn một quyển sách để đọc?", str(m_ + v_),
             [str(m_ * v_), str(abs(m_ - v_)), str(m_ + v_ + 1)],
             f"Chọn một quyển hoặc là sách Toán ({m_} cách) hoặc là sách Văn ({v_} cách), hai trường hợp không trùng nhau. Theo quy tắc cộng: ${m_}+{v_}={m_+v_}$ cách.")
        b.sa(B23, 'nb', 'Quy tắc cộng', f"Có {m_} bông hồng và {v_} bông cúc (đôi một khác nhau). Có bao nhiêu cách chọn một bông hoa?", m_ + v_,
             f"Hai nhóm hoa không trùng nhau nên dùng quy tắc cộng: ${m_}+{v_}={m_+v_}$ cách chọn.")
    for (a, c) in ((2, 3), (4, 5), (3, 6), (5, 2)):
        b.mc(B23, 'nb', 'Quy tắc nhân', f"Một bạn có {a} chiếc áo sơ mi và {c} chiếc quần khác nhau. Có bao nhiêu cách chọn một bộ gồm một áo và một quần?", str(a * c),
             [str(a + c), str(a * c + a), str(a * c - 1)],
             f"Chọn áo có {a} cách, với mỗi cách chọn áo có {c} cách chọn quần. Theo quy tắc nhân: ${a}\\times{c}={a*c}$ cách.")
        b.sa(B23, 'nb', 'Quy tắc nhân', f"Có {a} chiếc áo và {c} chiếc quần khác nhau. Có bao nhiêu cách chọn một bộ áo - quần?", a * c, f"Chọn áo rồi chọn quần nên dùng quy tắc nhân: ${a}\\times{c}={a*c}$ cách chọn.")
    for (a, c, d) in ((2, 3, 2), (3, 2, 4), (4, 3, 2)):
        b.mc(B23, 'th', 'Quy tắc nhân (nhiều bước)', f"Một thực đơn có {a} món khai vị, {c} món chính và {d} món tráng miệng. Có bao nhiêu cách chọn một suất ăn gồm đủ ba loại món?", str(a * c * d),
             [str(a + c + d), str(a * c + d), str(a * c * d + a)],
             f"Chọn lần lượt ba món, theo quy tắc nhân: ${a}\\times{c}\\times{d}={a*c*d}$ cách.")
    for (a, c, d, e) in ((2, 3, 1, 4), (3, 2, 2, 2), (4, 1, 3, 3)):
        total = a * c + d * e
        b.mc(B23, 'th', 'Kết hợp quy tắc cộng và nhân', f"Từ $A$ đến $B$ có hai nhóm đường đi. Nhóm thứ nhất đi qua $C$: từ $A$ đến $C$ có {a} đường, từ $C$ đến $B$ có {c} đường. Nhóm thứ hai đi qua $D$: từ $A$ đến $D$ có {d} đường, từ $D$ đến $B$ có {e} đường. Có bao nhiêu cách đi từ $A$ đến $B$?", str(total),
             [str(a * c * d * e), str(a + c + d + e), str(total + 2)],
             f"Qua $C$: ${a}\\times{c}={a*c}$ cách. Qua $D$: ${d}\\times{e}={d*e}$ cách. Hai nhóm không trùng nhau nên cộng: ${a*c}+{d*e}={total}$ cách.")
    for (digits, k) in (((1, 2, 3, 4, 5), 3), ((1, 2, 3, 4, 5, 6), 3), ((0, 1, 2, 3, 4), 3)):
        # số tự nhiên có k chữ số khác nhau lập từ digits
        cnt = sum(1 for t in permutations(digits, k) if t[0] != 0)
        ev = sum(1 for t in permutations(digits, k) if t[0] != 0 and t[-1] % 2 == 0)
        ds = ", ".join(map(str, digits))
        b.mc(B23, 'vd', 'Lập số tự nhiên', f"Từ các chữ số {ds} lập được bao nhiêu số tự nhiên có {k} chữ số đôi một khác nhau?", str(cnt),
             [str(len(digits) ** k), str(math.comb(len(digits), k)), str(cnt + len(digits))],
             f"Đếm trực tiếp (kiểm tra bằng liệt kê): có ${cnt}$ số. Với {ds}" + (" (chữ số đầu khác $0$)" if 0 in digits else "") + ", số cách chọn lần lượt các chữ số theo quy tắc nhân cho kết quả " + str(cnt) + ".")
        b.sa(B23, 'vd', 'Lập số tự nhiên chẵn', f"Từ các chữ số {ds} lập được bao nhiêu số tự nhiên chẵn có {k} chữ số đôi một khác nhau?", ev,
             f"Chọn chữ số hàng đơn vị là chữ số chẵn rồi chọn các chữ số còn lại (chữ số đầu khác $0$). Đếm trực tiếp được ${ev}$ số.")
    for (n, k) in ((4, 3), (5, 2), (3, 4)):
        b.mc(B23, 'th', 'Số cách điền khi cho phép lặp', f"Có bao nhiêu số tự nhiên có {k} chữ số mà mỗi chữ số thuộc tập $\\{{1, 2, \\dots, {n}\\}}$ (các chữ số có thể lặp lại)?", str(n ** k),
             [str(math.perm(n, k)) if k <= n else str(n * k), str(n * k), str(math.comb(n, k)) if k <= n else str(n + k), str(n ** k + n)],
             f"Mỗi chữ số có {n} cách chọn và độc lập với nhau nên theo quy tắc nhân có ${n}^{k}={n**k}$ số.")
    # ===== Bài 24: hoán vị, chỉnh hợp, tổ hợp =====
    for n in (4, 5, 6, 7):
        v = math.factorial(n)
        b.mc(B24, 'nb', 'Hoán vị', f"Có bao nhiêu cách xếp {n} bạn học sinh thành một hàng dọc?", str(v),
             [str(n * n), str(v // n), str(v * n), str(v + n)],
             f"Mỗi cách xếp là một hoán vị của {n} phần tử nên có $P_{{{n}}}={n}!={v}$ cách.")
        b.sa(B24, 'nb', 'Hoán vị', f"Có bao nhiêu cách xếp {n} bạn học sinh thành một hàng dọc?", v, f"Mỗi cách xếp là một hoán vị của {n} phần tử, nên có $P_{{{n}}}={n}!={v}$ cách xếp.")
    for (n, k) in ((5, 2), (6, 3), (7, 2), (8, 3)):
        v = math.perm(n, k)
        b.mc(B24, 'th', 'Chỉnh hợp', f"Một tổ có {n} học sinh. Có bao nhiêu cách chọn {k} bạn giữ các chức vụ khác nhau (mỗi bạn một chức vụ) từ tổ đó?", str(v),
             [str(math.comb(n, k)), str(n ** k), str(v + n), str(v * 2)],
             f"Chọn có phân biệt thứ tự (chức vụ khác nhau) là chỉnh hợp: $A_{{{n}}}^{{{k}}}=\\frac{{{n}!}}{{({n}-{k})!}}={v}$.")
        c = math.comb(n, k)
        b.mc(B24, 'th', 'Tổ hợp', f"Một tổ có {n} học sinh. Có bao nhiêu cách chọn {k} bạn đi lao động (không phân biệt công việc)?", str(c),
             [str(v), str(n * k), str(c + n), str(c * 2)],
             f"Chọn không phân biệt thứ tự là tổ hợp: $C_{{{n}}}^{{{k}}}=\\frac{{{n}!}}{{{k}!({n}-{k})!}}={c}$.")
        b.sa(B24, 'th', 'Tổ hợp', f"Có bao nhiêu cách chọn {k} học sinh từ {n} học sinh?", c, f"Chọn không phân biệt thứ tự nên là tổ hợp: $C_{{{n}}}^{{{k}}}={c}$ cách.")
    for (n, k) in ((8, 3), (10, 2), (9, 4), (6, 2)):
        b.mc(B24, 'nb', 'Giá trị tổ hợp', f"Giá trị của $C_{{{n}}}^{{{k}}}$ bằng:", str(math.comb(n, k)),
             [str(math.perm(n, k)), str(math.comb(n, k) + n), str(math.comb(n, k) - 2), str(n * k)],
             f"Áp dụng công thức: $C_{{{n}}}^{{{k}}}=\\frac{{{n}!}}{{{k}!\\cdot{n-k}!}}={math.comb(n, k)}$.")
    for (n, k) in ((6, 2), (7, 3), (9, 2)):
        b.mc(B24, 'nb', 'Giá trị chỉnh hợp', f"Giá trị của $A_{{{n}}}^{{{k}}}$ bằng:", str(math.perm(n, k)),
             [str(math.comb(n, k)), str(math.perm(n, k) + n), str(n ** k), str(n * k)],
             f"Áp dụng công thức: $A_{{{n}}}^{{{k}}}=\\frac{{{n}!}}{{({n}-{k})!}}={math.perm(n, k)}$.")
    for (nam, nu, kn, kc) in ((4, 3, 1, 1), (5, 3, 2, 1), (4, 4, 2, 2), (6, 4, 3, 2)):
        v = math.comb(nam, kn) * math.comb(nu, kc)
        b.mc(B24, 'vd', 'Chọn nhóm theo giới tính', f"Một nhóm có {nam} nam và {nu} nữ. Có bao nhiêu cách chọn một nhóm gồm {kn} nam và {kc} nữ?", str(v),
             [str(math.comb(nam + nu, kn + kc)), str(math.comb(nam, kn) + math.comb(nu, kc)), str(math.perm(nam, kn) * math.perm(nu, kc)), str(v + nam)],
             f"Chọn {kn} nam: $C_{{{nam}}}^{{{kn}}}={math.comb(nam, kn)}$ cách; chọn {kc} nữ: $C_{{{nu}}}^{{{kc}}}={math.comb(nu, kc)}$ cách. Theo quy tắc nhân: ${math.comb(nam, kn)}\\times{math.comb(nu, kc)}={v}$ cách.")
        b.sa(B24, 'vd', 'Chọn nhóm theo giới tính', f"Một nhóm có {nam} nam và {nu} nữ. Có bao nhiêu cách chọn {kn} nam và {kc} nữ?", v,
             f"$C_{{{nam}}}^{{{kn}}}\\cdot C_{{{nu}}}^{{{kc}}}={math.comb(nam, kn)}\\cdot{math.comb(nu, kc)}={v}$.")
    for n in (4, 5, 6):
        cnt = sum(1 for p in permutations(range(n)) if abs(p.index(0) - p.index(1)) == 1)
        assert cnt == 2 * math.factorial(n - 1)
        b.mc(B24, 'vd', 'Hoán vị có hai bạn đứng cạnh nhau', f"Có bao nhiêu cách xếp {n} bạn thành một hàng dọc sao cho hai bạn $A$ và $B$ luôn đứng cạnh nhau?", str(cnt),
             [str(math.factorial(n)), str(math.factorial(n - 1)), str(cnt + n), str(cnt // 2 + 1)],
             f"Coi $A$, $B$ là một khối: xếp khối cùng {n-2} bạn còn lại có $({n-1})!={math.factorial(n-1)}$ cách; hoán đổi $A$, $B$ trong khối có $2$ cách. Tổng: $2\\cdot{math.factorial(n-1)}={cnt}$.")
    for n in (5, 6, 8, 10):
        diag = n * (n - 3) // 2
        assert diag == math.comb(n, 2) - n
        b.mc(B24, 'vd', 'Số đường chéo đa giác', f"Số đường chéo của một đa giác lồi có {n} đỉnh là:", str(diag),
             [str(math.comb(n, 2)), str(math.comb(n, 3)), str(diag + n), str(n * (n - 1))],
             f"Số đoạn thẳng nối hai đỉnh bất kì là $C_{{{n}}}^2={math.comb(n, 2)}$, trừ đi {n} cạnh ta được ${math.comb(n, 2)}-{n}={diag}$ đường chéo.")
        b.sa(B24, 'vd', 'Số đường chéo đa giác', f"Một đa giác lồi có {n} đỉnh. Tính số đường chéo của đa giác.", diag, f"Số đường chéo bằng số đoạn nối hai đỉnh trừ số cạnh: $C_{{{n}}}^2-{n}={math.comb(n, 2)}-{n}={diag}$.")
    for n in (5, 7, 8):
        b.mc(B24, 'th', 'Số tam giác từ các đỉnh đa giác', f"Cho đa giác lồi có {n} đỉnh. Có bao nhiêu tam giác có ba đỉnh là đỉnh của đa giác?", str(math.comb(n, 3)),
             [str(math.perm(n, 3)), str(math.comb(n, 2)), str(math.comb(n, 3) + n)],
             f"Mỗi tam giác ứng với một cách chọn $3$ đỉnh: $C_{{{n}}}^3={math.comb(n, 3)}$.")
    for (n, k, kind) in ((None, 10, 'C2'), (None, 20, 'A2'), (None, 15, 'C2')):
        pass
    for target in (10, 15, 21):
        n = next(n for n in range(2, 30) if math.comb(n, 2) == target)
        b.mc(B24, 'vd', 'Tìm n từ đẳng thức tổ hợp', f"Tìm số nguyên dương $n$ thoả mãn $C_n^2={target}$.", f"$n={n}$",
             [f"$n={n+1}$", f"$n={n-1}$", f"$n={target}$"],
             f"$C_n^2=\\frac{{n(n-1)}}{{2}}={target}\\iff n^2-n-{2*target}=0$, nhận nghiệm dương $n={n}$.")
        b.sa(B24, 'vd', 'Tìm n từ đẳng thức tổ hợp', f"Tìm số nguyên dương $n$ thoả mãn $C_n^2={target}$.", n,
             f"$\\frac{{n(n-1)}}{{2}}={target}\\iff n^2-n-{2*target}=0$, suy ra $n={n}$ (loại nghiệm âm).")
    for target in (20, 30, 42):
        n = next(n for n in range(2, 30) if n * (n - 1) == target)
        b.mc(B24, 'vd', 'Tìm n từ đẳng thức chỉnh hợp', f"Tìm số nguyên dương $n$ thoả mãn $A_n^2={target}$.", f"$n={n}$",
             [f"$n={n+1}$", f"$n={n-1}$", f"$n={target//2}$"],
             f"$A_n^2=n(n-1)={target}\\iff n^2-n-{target}=0$, nhận nghiệm dương $n={n}$.")
    b.mc(B24, 'nb', 'Tính chất tổ hợp', "Với $0\\le k\\le n$, đẳng thức nào sau đây đúng?", M('C_n^k=C_n^{n-k}'),
         [M('C_n^k=C_n^{k+1}'), M('C_n^k=A_n^k'), M('C_n^k=k!\\cdot A_n^k')],
         "Chọn $k$ phần tử từ $n$ phần tử cũng tương đương với việc chọn $n-k$ phần tử còn lại, nên $C_n^k=C_n^{n-k}$.")
    b.mc(B24, 'nb', 'Quan hệ chỉnh hợp - tổ hợp', "Với $0\\le k\\le n$, đẳng thức nào sau đây đúng?", M('A_n^k=k!\\cdot C_n^k'),
         [M('A_n^k=\\frac{C_n^k}{k!}'), M('A_n^k=C_n^k'), M('A_n^k=n!\\cdot C_n^k')],
         "Từ công thức $C_n^k=\\frac{n!}{k!(n-k)!}$ và $A_n^k=\\frac{n!}{(n-k)!}$ suy ra $A_n^k=k!\\cdot C_n^k$.")
    b.mc(B24, 'nb', 'Công thức Pascal', "Với $1\\le k\\le n$, đẳng thức nào sau đây đúng?", M('C_{n}^{k-1}+C_n^k=C_{n+1}^k'),
         [M('C_{n}^{k-1}+C_n^k=C_{n+1}^{k-1}'), M('C_{n}^{k-1}+C_n^k=C_n^{k+1}'), M('C_{n}^{k-1}+C_n^k=2C_n^k')],
         "Đây là công thức Pascal: $C_n^{k-1}+C_n^k=C_{n+1}^k$.")
    # ===== Bài 25: nhị thức Newton =====
    def expand(a, bcoef, n):
        """Hệ số của (a x + b)^n theo luỹ thừa x^k, k=0..n."""
        return [math.comb(n, k) * (a ** k) * (bcoef ** (n - k)) for k in range(n + 1)]
    for n in (3, 4, 5, 6):
        b.mc(B25, 'nb', 'Số số hạng khai triển', f"Khai triển nhị thức $(a+b)^{n}$ có bao nhiêu số hạng?", str(n + 1),
             [str(n), str(n + 2), str(2 * n)],
             f"Khai triển $(a+b)^n$ có $n+1$ số hạng. Với $n={n}$ có ${n+1}$ số hạng.")
    for (a, c, n, k) in ((1, 1, 4, 2), (2, 1, 5, 2), (1, 2, 5, 3), (3, 1, 4, 3), (2, -1, 4, 3), (1, 3, 4, 2)):
        coefs = expand(a, c, n)
        val = coefs[k]
        base = f"({'' if a == 1 else a}x{'+' if c > 0 else '-'}{abs(c)})^{n}"
        b.mc(B25, 'th', 'Hệ số trong khai triển', f"Hệ số của $x^{k}$ trong khai triển ${base}$ là:", str(val),
             [str(math.comb(n, k)), str(val + 4), str(-val if val else 3), str(coefs[k - 1] if k >= 1 and coefs[k - 1] != val else val * 2 + 1)],
             f"Số hạng tổng quát: $C_{{{n}}}^{{{k}}}\\cdot({a}x)^{k}\\cdot({c})^{{{n-k}}}={math.comb(n, k)}\\cdot{a**k}\\cdot({c**(n-k)})={val}$, nên hệ số của $x^{k}$ là ${val}$.")
        b.sa(B25, 'th', 'Hệ số trong khai triển', f"Tìm hệ số của $x^{k}$ trong khai triển ${base}$.", val,
             f"Theo công thức nhị thức Newton, hệ số của $x^{k}$ là $C_{{{n}}}^{{{k}}}\\cdot{a}^{{{k}}}\\cdot({c})^{{{n-k}}}={val}$.")
    for (a, c, n) in ((1, 1, 4), (1, 2, 4), (2, 1, 3), (1, 3, 3)):
        tot = (a + c) ** n
        b.mc(B25, 'th', 'Tổng các hệ số', f"Tổng các hệ số trong khai triển $({'' if a == 1 else a}x+{c})^{n}$ bằng:", str(tot),
             [str(2 ** n), str(a ** n + c ** n), str(tot + a), str(tot - 1)],
             f"Thay $x=1$ vào khai triển: tổng các hệ số bằng $({a}+{c})^{n}={tot}$.")
    for (c, n) in ((2, 4), (3, 3), (2, 5), (-1, 4)):
        v = c ** n
        b.mc(B25, 'th', 'Hệ số tự do', f"Hệ số tự do (không chứa $x$) trong khai triển $(x{'+' if c > 0 else '-'}{abs(c)})^{n}$ là:", str(v),
             [str(c * n), str(-v if v else 1), str(v + 1), str(math.comb(n, 2) * c)],
             f"Hệ số tự do là số hạng ứng với $x^0$: $C_{{{n}}}^0\\cdot({c})^{n}={v}$.")
    for n in (3, 4):
        coefs = expand(1, 1, n)
        poly = " + ".join((f"{co}x^{k}" if k > 1 else (f"{co}x" if k == 1 else f"{co}")) for k, co in reversed(list(enumerate(coefs)))).replace("1x^", "x^").replace(" 1x", " x")
        wrong = coefs[:]; wrong[1] += 1
        b.mc(B25, 'th', 'Khai triển $(x+1)^n$', f"Khai triển của $(x+1)^{n}$ là:", M(poly),
             [M(" + ".join((f"{co}x^{k}" if k > 1 else (f"{co}x" if k == 1 else f"{co}")) for k, co in reversed(list(enumerate(wrong)))).replace("1x^", "x^")), M(f"x^{n}+1"), M(f"x^{n}+{n}x^{n-1}+1")],
             f"Hệ số là các số $C_{{{n}}}^k$ ($k=0..{n}$): {', '.join(str(c) for c in coefs)}. Do đó $(x+1)^{n}={poly}$.")
    return b
