# -*- coding: utf-8 -*-
"""Toán 10 - Chương I: Mệnh đề và tập hợp (đáp án kiểm bằng tính toán trên tập hữu hạn)."""
import math
from itertools import combinations
from .common import Bank, M

B1, B2 = 'b1', 'b2'

def S(xs):
    xs = sorted(xs)
    return "$\\{" + ", ".join(map(str, xs)) + "\\}$" if xs else "$\\emptyset$"

def build():
    b = Bank('toan10', 'c1')
    sets = [({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}), ({1, 3, 5, 7, 9}, {1, 2, 3, 4, 5}), ({2, 4, 6, 8}, {1, 2, 3, 4}), ({0, 1, 2, 3}, {2, 3, 4, 5, 6}), ({1, 2, 4, 8}, {2, 4, 6, 8, 10})]
    for (A, B) in sets:
        a, bb = S(A), S(B)
        for sym, name, op in (("\\cap", "giao", lambda x, y: x & y), ("\\cup", "hợp", lambda x, y: x | y), ("\\setminus", "hiệu", lambda x, y: x - y)):
            r = op(A, B)
            wrong = []
            for w in (A | B, A & B, A - B, B - A, A ^ B, A):
                if w != r and S(w) not in [S(x) for x in wrong]: wrong.append(w)
            b.mc(B1, 'nb', f"Phép toán {name}", f"Cho $A={a[1:-1]}$ và $B={bb[1:-1]}$. Tìm $A {sym} B$.", S(r), [S(w) for w in wrong[:3]],
                 f"{ {'giao':'Giao gồm các phần tử thuộc cả hai tập','hợp':'Hợp gồm các phần tử thuộc ít nhất một trong hai tập','hiệu':'Hiệu $A\\setminus B$ gồm các phần tử thuộc $A$ nhưng không thuộc $B$'}[name] }. Ta được $A {sym} B={S(r)[1:-1]}$.")
        b.sa(B1, 'th', 'Đếm phần tử của hợp', f"Cho $A={a[1:-1]}$ và $B={bb[1:-1]}$. Tính số phần tử của $A\\cup B$.", len(A | B),
             f"Dùng $n(A\\cup B)=n(A)+n(B)-n(A\\cap B)={len(A)}+{len(B)}-{len(A&B)}={len(A|B)}$.")
    for n in (2, 3, 4, 5):
        b.mc(B1, 'nb', 'Số tập con', f"Tập hợp có {n} phần tử có bao nhiêu tập con?", str(2 ** n), [str(2 * n), str(n * n), str(2 ** n - 1)],
             f"Tập có $n$ phần tử có $2^n$ tập con. Với $n={n}$: $2^{n}={2**n}$.")
        b.sa(B1, 'nb', 'Số tập con', f"Một tập hợp có {n} phần tử. Hỏi tập đó có bao nhiêu tập con?", 2 ** n, f"Số tập con của tập có {n} phần tử là $2^{n}={2**n}$ (kể cả tập rỗng và chính nó).")
    for n in (3, 4, 5):
        b.mc(B1, 'th', 'Số tập con khác rỗng', f"Tập hợp có {n} phần tử có bao nhiêu tập con khác rỗng?", str(2 ** n - 1), [str(2 ** n), str(2 ** n - 2), str(2 * n - 1)],
             f"Có $2^{n}={2**n}$ tập con, bỏ tập rỗng còn ${2**n-1}$ tập con khác rỗng.")
    for (n, k) in ((4, 2), (5, 3), (6, 2)):
        b.mc(B1, 'vd', 'Số tập con có k phần tử', f"Tập hợp có {n} phần tử có bao nhiêu tập con gồm đúng {k} phần tử?", str(math.comb(n, k)), [str(2 ** n), str(math.perm(n, k)), str(math.comb(n, k) + 1)],
             f"Mỗi tập con gồm {k} phần tử ứng với một cách chọn {k} phần tử trong {n}: $C_{{{n}}}^{{{k}}}={math.comb(n, k)}$.")
    for (a, c) in ((1, 5), (2, 8), (-2, 3), (0, 6)):
        els = list(range(a, c + 1))
        b.mc(B1, 'nb', 'Liệt kê tập hợp', f"Tập hợp $X=\\{{x\\in\\mathbb{{Z}}\\mid {a}\\le x\\le {c}\\}}$ có bao nhiêu phần tử?", str(len(els)), [str(len(els) - 1), str(len(els) + 1), str(c - a - 1) if c - a - 1 != len(els) else str(len(els) + 2)],
             f"Các số nguyên từ ${a}$ đến ${c}$ gồm ${c}-({a})+1={len(els)}$ số, nên $X$ có ${len(els)}$ phần tử.")
        b.sa(B1, 'nb', 'Đếm số nguyên trong đoạn', f"Có bao nhiêu số nguyên $x$ thoả mãn ${a}\\le x\\le {c}$?", len(els), f"Số các số nguyên là $c-a+1={c}-({a})+1={len(els)}$.")
    for (lo, hi, d) in ((1, 30, 3), (1, 50, 7), (10, 60, 5)):
        els = [x for x in range(lo, hi + 1) if x % d == 0]
        b.mc(B1, 'th', 'Đếm bội trong khoảng', f"Tập hợp các số nguyên từ {lo} đến {hi} chia hết cho ${d}$ có bao nhiêu phần tử?", str(len(els)), [str(len(els) + 1), str(len(els) - 1), str(hi // d + 2)],
             f"Các số chia hết cho ${d}$ trong đoạn là {', '.join(map(str, els[:3]))}, ..., {els[-1]}: có ${len(els)}$ số.")
    for (a1, a2, a3) in ((3, 5, 8), (4, 6, 9)):
        pass
    # Giao hai khoảng
    for (a, c, d, e) in ((-2, 3, 1, 6), (0, 5, 2, 9), (-4, 1, -1, 4)):
        lo, hi = max(a, d), min(c, e)
        b.mc(B1, 'th', 'Giao hai đoạn', f"Cho $A=[{a};{c}]$ và $B=[{d};{e}]$. Khi đó $A\\cap B$ là:", f"$[{lo};{hi}]$", [f"$[{min(a, d)};{max(c, e)}]$", f"$[{a};{c}]$", f"$[{d};{e}]$", f"$[{lo - 1};{hi}]$"],
             f"Giao gồm các số thuộc cả hai đoạn: cận dưới là $\\max\\{{{a},{d}\\}}={lo}$, cận trên là $\\min\\{{{c},{e}\\}}={hi}$, nên $A\\cap B=[{lo};{hi}]$.")
        b.mc(B1, 'th', 'Hợp hai đoạn giao nhau', f"Cho $A=[{a};{c}]$ và $B=[{d};{e}]$. Khi đó $A\\cup B$ là:", f"$[{min(a, d)};{max(c, e)}]$", [f"$[{lo};{hi}]$", f"$[{a};{e}]$ " if (a, e) != (min(a, d), max(c, e)) else f"$[{a - 1};{e}]$", f"$[{min(a, d)};{max(c, e) + 1}]$"],
             f"Hai đoạn giao nhau nên hợp là một đoạn từ $\\min\\{{{a},{d}\\}}={min(a, d)}$ đến $\\max\\{{{c},{e}\\}}={max(c, e)}$.")
    # ===== Bài 2: mệnh đề =====
    b.mc(B2, 'nb', 'Mệnh đề phủ định', "Phủ định của mệnh đề \"$\\forall x\\in\\mathbb{R},\\ x^2\\ge0$\" là:", "$\\exists x\\in\\mathbb{R},\\ x^2<0$", ["$\\forall x\\in\\mathbb{R},\\ x^2<0$", "$\\exists x\\in\\mathbb{R},\\ x^2\\ge0$", "$\\forall x\\in\\mathbb{R},\\ x^2\\le0$"],
         "Phủ định của \"với mọi\" là \"tồn tại\" và đổi $\\ge$ thành $<$, nên ta có $\\exists x,\\ x^2<0$.")
    b.mc(B2, 'nb', 'Mệnh đề phủ định', "Phủ định của mệnh đề \"$\\exists x\\in\\mathbb{N},\\ x^2=2$\" là:", "$\\forall x\\in\\mathbb{N},\\ x^2\\ne2$", ["$\\exists x\\in\\mathbb{N},\\ x^2\\ne2$", "$\\forall x\\in\\mathbb{N},\\ x^2=2$", "$\\exists x\\in\\mathbb{N},\\ x^2>2$"],
         "Phủ định của \"tồn tại\" là \"với mọi\" và đổi $=$ thành $\\ne$.")
    for (n, d) in ((12, 3), (15, 5), (21, 7), (14, 4), (9, 2)):
        tr = n % d == 0
        b.mc(B2, 'nb', 'Tính đúng sai của mệnh đề', f"Mệnh đề \"${n}$ chia hết cho ${d}$\" là mệnh đề:", "Đúng" if tr else "Sai", ["Sai" if tr else "Đúng", "Không phải mệnh đề", "Vừa đúng vừa sai"],
             f"Ta có ${n}={d}\\times{n//d}" + (f"$, nên ${n}$ chia hết cho ${d}$: mệnh đề đúng." if tr else f"+{n%d}$ (dư ${n%d}$), nên ${n}$ không chia hết cho ${d}$: mệnh đề sai."))
    for (pp, qq, tp, tq) in (("$2$ là số nguyên tố", "$4$ là số nguyên tố", True, False), ("$3<5$", "$5<3$", True, False), ("$9$ là số chính phương", "$9$ là số nguyên tố", True, False), ("$7$ là số lẻ", "$7$ là số nguyên tố", True, True)):
        imp = (not tp) or tq
        b.mc(B2, 'th', 'Mệnh đề kéo theo', f"Xét mệnh đề kéo theo $P\\Rightarrow Q$ với $P$: \"{pp}\" và $Q$: \"{qq}\". Mệnh đề đó là:", "Đúng" if imp else "Sai", ["Sai" if imp else "Đúng", "Không xác định được", "Không phải mệnh đề"],
             f"$P$ " + ("đúng" if tp else "sai") + f", $Q$ " + ("đúng" if tq else "sai") + ". " + ("$P\\Rightarrow Q$ chỉ sai khi $P$ đúng và $Q$ sai; ở đây không xảy ra, nên mệnh đề đúng." if imp else "$P$ đúng mà $Q$ sai nên $P\\Rightarrow Q$ sai."))
    b.mc(B2, 'nb', 'Mệnh đề đảo', "Mệnh đề đảo của mệnh đề \"Nếu $a=b$ thì $a^2=b^2$\" là:", "Nếu $a^2=b^2$ thì $a=b$", ["Nếu $a\\ne b$ thì $a^2\\ne b^2$", "Nếu $a^2\\ne b^2$ thì $a\\ne b$", "Nếu $a=b$ thì $a^2\\ne b^2$"],
         "Mệnh đề đảo của $P\\Rightarrow Q$ là $Q\\Rightarrow P$: hoán đổi giả thiết và kết luận.")
    b.mc(B2, 'th', 'Mệnh đề đảo đúng/sai', "Mệnh đề đảo của \"Nếu $a=b$ thì $a^2=b^2$\" có đúng không?", "Sai, vì có thể $a=-b$", ["Đúng với mọi $a,b$", "Đúng khi $a,b$ dương", "Không xét được"],
         "Mệnh đề đảo \"Nếu $a^2=b^2$ thì $a=b$\" sai, ví dụ $a=2,\\ b=-2$ thì $a^2=b^2$ nhưng $a\\ne b$.")
    b.mc(B2, 'nb', 'Điều kiện cần và đủ', "Mệnh đề \"$P\\Leftrightarrow Q$\" được phát biểu là:", "$P$ là điều kiện cần và đủ để có $Q$", ["$P$ là điều kiện cần để có $Q$", "$P$ là điều kiện đủ để có $Q$", "$P$ và $Q$ cùng sai"],
         "$P\\Leftrightarrow Q$ nghĩa là $P\\Rightarrow Q$ và $Q\\Rightarrow P$ cùng đúng, tức $P$ là điều kiện cần và đủ để có $Q$.")
    for (lo, hi, rule, txt) in ((1, 10, lambda x: x * x > x, "$x^2>x$"), (2, 9, lambda x: x % 2 == 0, "$x$ là số chẵn"), (1, 6, lambda x: x < 5, "$x<5$")):
        allt = all(rule(x) for x in range(lo, hi + 1))
        ex = any(rule(x) for x in range(lo, hi + 1))
        b.mc(B2, 'vd', 'Mệnh đề với mọi', f"Xét mệnh đề \"$\\forall x\\in\\mathbb{{Z}},\\ {lo}\\le x\\le {hi}\\Rightarrow$ {txt}\". Mệnh đề này:", "Đúng" if allt else "Sai", ["Sai" if allt else "Đúng", "Không xác định", "Không phải mệnh đề"],
             ("Kiểm tra từng giá trị thấy đều thoả mãn nên mệnh đề đúng." if allt else f"Có giá trị trong đoạn không thoả mãn (ví dụ {next(x for x in range(lo, hi + 1) if not rule(x))}) nên mệnh đề sai."))
    return b
