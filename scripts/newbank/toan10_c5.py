# -*- coding: utf-8 -*-
"""Toán 10 - Chương V: Các số đặc trưng của mẫu số liệu không ghép nhóm."""
import math, random
from fractions import Fraction
from .common import Bank, M, fnum, frac

B12, B13, B14 = 'b12', 'b13', 'b14'

# ---------- thống kê (quy ước SGK: Q1 = trung vị nửa dưới, Q3 = trung vị nửa trên, bỏ trung vị khi n lẻ) ----------
def med(v):
    v = sorted(v); n = len(v)
    return Fraction(v[n // 2]) if n % 2 else Fraction(v[n // 2 - 1] + v[n // 2], 2)
def quart(v):
    v = sorted(v); n = len(v)
    lo = v[: n // 2]; hi = v[(n + 1) // 2:]
    return med(lo), med(v), med(hi)
def mean(v): return Fraction(sum(v), len(v))
def var(v):
    m = mean(v); return sum((Fraction(x) - m) ** 2 for x in v) / len(v)
def nice(fr):
    return (fr.denominator and 100 % fr.denominator == 0)
def d2(fr):  # chuỗi thập phân kiểu VN
    return fnum(float(fr), 2)
def lst(v): return ", ".join(str(x) for x in v)

def datasets():
    rng = random.Random(2026)
    out, seen = [], set()
    tries = 0
    while len(out) < 16 and tries < 200000:
        tries += 1
        n = rng.choice([7, 8, 9, 10])
        v = sorted(rng.randint(2, 20) for _ in range(n))
        key = tuple(v)
        if key in seen: continue
        q1, q2, q3 = quart(v)
        if not (nice(mean(v)) and nice(var(v)) and nice(q1) and nice(q3) and nice(q2)): continue
        if len(set(v)) == len(v): continue          # có giá trị lặp lại (để hỏi mốt)
        from collections import Counter
        c = Counter(v); top = [k for k, t in c.items() if t == max(c.values())]
        if len(top) != 1: continue                   # mốt duy nhất
        if var(v) == 0: continue
        seen.add(key); out.append(v)
    return out

def build():
    b = Bank('toan10', 'c5')
    ds = datasets()
    assert len(ds) >= 14, len(ds)
    from collections import Counter

    # ===== Bài 12: số gần đúng, sai số =====
    for (a, place, exp_) in ((2573, 'trăm', 2600), (12485, 'nghìn', 12000), (4968, 'chục', 4970), (7351, 'trăm', 7400)):
        b.mc(B12, 'nb', 'Quy tròn số nguyên', f"Quy tròn số ${a}$ đến hàng {place} ta được:", M(str(exp_)),
             [M(str(exp_ + {'trăm': 100, 'nghìn': 1000, 'chục': 10}[place])), M(str(exp_ - {'trăm': 100, 'nghìn': 1000, 'chục': 10}[place])), M(str(a))],
             f"Chữ số ngay sau hàng {place} quyết định việc làm tròn (từ 5 trở lên thì tăng một đơn vị, ngược lại giữ nguyên). Kết quả quy tròn của ${a}$ là ${exp_}$.")
        b.sa(B12, 'nb', 'Quy tròn số nguyên', f"Quy tròn số ${a}$ đến hàng {place}. Viết kết quả.", exp_,
             f"Chữ số liền sau hàng {place} quyết định làm tròn lên hay xuống, kết quả là ${exp_}$.")
    for (a, k, res) in ((3.14159, 2, '3,14'), (2.7183, 3, '2,718'), (5.675, 1, '5,7'), (1.4142, 2, '1,41')):
        word = {1: 'phần chục', 2: 'phần trăm', 3: 'phần nghìn'}[k]
        err = abs(a - float(res.replace(',', '.')))
        b.mc(B12, 'nb', 'Quy tròn số thập phân', f"Quy tròn số ${fnum(a, 6)}$ đến hàng {word} ta được:", M(res),
             [M(fnum(float(res.replace(',', '.')) + 10 ** -k, k)), M(fnum(float(res.replace(',', '.')) - 10 ** -k, k)), M(fnum(a, 6))],
             f"Giữ lại {k} chữ số thập phân và xét chữ số liền sau để làm tròn. Kết quả là ${res}$ (sai số tuyệt đối khoảng ${fnum(err, 4)}$).")
    for (a, d, rel) in ((250, 5, 2), (400, 2, 0.5), (80, 4, 5), (1250, 25, 2), (60, 3, 5)):
        assert abs(d / a * 100 - rel) < 1e-9
        relt = fnum(rel, 2)
        b.mc(B12, 'th', 'Sai số tương đối', f"Số gần đúng $a={a}$ có sai số tuyệt đối không vượt quá $d={d}$. Sai số tương đối $\\delta_a$ không vượt quá:", M(f"{relt}\\%"),
             [M(f"{fnum(rel * 2, 2)}\\%"), M(f"{fnum(rel / 2, 3)}\\%"), M(f"{fnum(d, 2)}\\%")],
             f"Sai số tương đối $\\delta_a=\\frac{{\\Delta_a}}{{|a|}}\\le\\frac{{d}}{{|a|}}=\\frac{{{d}}}{{{a}}}={relt}\\%$.")
        b.sa(B12, 'th', 'Sai số tương đối', f"Số gần đúng $a={a}$ có sai số tuyệt đối không vượt quá ${d}$. Tính sai số tương đối tối đa (đơn vị: %).", rel,
             f"$\\delta_a\\le\\frac{{d}}{{|a|}}=\\frac{{{d}}}{{{a}}}={relt}\\%$.", tol=0.01, unit='%')
    for (a, d) in ((2.4, 0.05), (15.6, 0.2), (7.25, 0.01)):
        lo, hi = a - d, a + d
        b.mc(B12, 'th', 'Khoảng chứa giá trị đúng', f"Số gần đúng $a={fnum(a, 2)}$ có sai số tuyệt đối không vượt quá ${fnum(d, 2)}$. Giá trị đúng $\\bar a$ thuộc đoạn:", M(f"[{fnum(lo, 3)};\\ {fnum(hi, 3)}]"),
             [M(f"[{fnum(a - 2 * d, 3)};\\ {fnum(a + 2 * d, 3)}]"), M(f"[{fnum(a, 3)};\\ {fnum(a + d, 3)}]"), M(f"[{fnum(a - d, 3)};\\ {fnum(a, 3)}]")],
             f"Ta có $|\\bar a-a|\\le d$ nên $a-d\\le\\bar a\\le a+d$, tức $\\bar a\\in[{fnum(lo, 3)};\\ {fnum(hi, 3)}]$.")
    for (true, approx) in ((3.14159, 3.14), (2.71828, 2.72), (1.41421, 1.41)):
        e = abs(true - approx)
        b.sa(B12, 'th', 'Sai số tuyệt đối', f"Dùng ${fnum(approx, 2)}$ làm giá trị gần đúng của ${fnum(true, 5)}$. Tính sai số tuyệt đối $\\Delta=|{fnum(true, 5)}-{fnum(approx, 2)}|$ (làm tròn đến hàng phần nghìn).", e,
             f"$\\Delta=|{fnum(true, 5)}-{fnum(approx, 2)}|={fnum(e, 5)}\\approx {fnum(e, 3)}$.", tol=0.001)

    # ===== Bài 13: số trung bình, trung vị, mốt, tứ phân vị =====
    for k, v in enumerate(ds):
        n = len(v); mu = mean(v); q1, q2, q3 = quart(v); c = Counter(v); mode = max(c, key=c.get)
        data_txt = lst(v)
        b.mc(B13, 'nb', 'Số trung bình', f"Cho mẫu số liệu: {data_txt}. Số trung bình cộng của mẫu số liệu là:", M(d2(mu)),
             [M(d2(q2)), M(d2(mu + 1)), M(d2(Fraction(sum(v), n + 1)))],
             f"Số trung bình $\\bar x=\\frac{{x_1+x_2+\\dots+x_n}}{{n}}=\\frac{{{sum(v)}}}{{{n}}}={d2(mu)}$.")
        b.mc(B13, 'nb', 'Mốt', f"Cho mẫu số liệu: {data_txt}. Mốt của mẫu số liệu là:", M(str(mode)),
             [M(str(x)) for x in sorted(set(v)) if x != mode][:6],
             f"Mốt là giá trị xuất hiện nhiều lần nhất. Giá trị ${mode}$ xuất hiện {c[mode]} lần, nhiều hơn mọi giá trị khác nên mốt bằng ${mode}$.")
        b.mc(B13, 'th', 'Trung vị', f"Cho mẫu số liệu (đã sắp xếp): {data_txt}. Trung vị của mẫu số liệu là:", M(d2(q2)),
             [M(d2(mu)), M(str(v[n // 2 - 1] if n % 2 == 0 else v[n // 2 + 1])), M(d2(q2 + 1)), M(d2(q2 - 1))],
             (f"Mẫu có $n={n}$ (lẻ) giá trị đã sắp xếp nên trung vị là giá trị chính giữa, vị trí thứ ${n//2+1}$: ${d2(q2)}$." if n % 2 else
              f"Mẫu có $n={n}$ (chẵn) giá trị nên trung vị là trung bình cộng của hai giá trị chính giữa (vị trí ${n//2}$ và ${n//2+1}$): $\\frac{{{v[n//2-1]}+{v[n//2]}}}{{2}}={d2(q2)}$."))
        b.mc(B13, 'th', 'Tứ phân vị', f"Cho mẫu số liệu (đã sắp xếp): {data_txt}. Tứ phân vị thứ nhất $Q_1$ là:", M(d2(q1)),
             [M(d2(q3)), M(d2(q2)), M(d2(q1 + 1)), M(d2(q1 - 1))],
             f"Trung vị $Q_2={d2(q2)}$. $Q_1$ là trung vị của nửa dưới của mẫu (các giá trị nhỏ hơn $Q_2$, bỏ trung vị nếu $n$ lẻ): " + f"{lst(v[: n // 2])}, nên $Q_1={d2(q1)}$.")
        if k % 2 == 0:
            b.sa(B13, 'nb', 'Số trung bình', f"Cho mẫu số liệu: {data_txt}. Tính số trung bình cộng (làm tròn đến hàng phần trăm).", float(mu),
                 f"Số trung bình $\\bar x=\\frac{{{'+'.join(map(str, v))}}}{{{n}}}=\\frac{{{sum(v)}}}{{{n}}}={d2(mu)}$.", tol=0.01)
        else:
            b.sa(B13, 'th', 'Tứ phân vị', f"Cho mẫu số liệu (đã sắp xếp): {data_txt}. Tính tứ phân vị thứ ba $Q_3$ (làm tròn đến hàng phần trăm).", float(q3),
                 f"$Q_3$ là trung vị của nửa trên của mẫu: {lst(v[(n + 1) // 2:])}, nên $Q_3={d2(q3)}$.", tol=0.01)

    # ===== Bài 14: độ phân tán =====
    for k, v in enumerate(ds):
        n = len(v); mu = mean(v); q1, q2, q3 = quart(v); R = v[-1] - v[0]; iqr = q3 - q1; s2 = var(v); sd = math.sqrt(float(s2))
        data_txt = lst(v)
        b.mc(B14, 'nb', 'Khoảng biến thiên', f"Cho mẫu số liệu: {data_txt}. Khoảng biến thiên của mẫu là:", M(str(R)),
             [M(str(R + 1)), M(str(R - 2)), M(d2(iqr)) if iqr != R else M(str(R + 3)), M(str(v[-1]))],
             f"Khoảng biến thiên $R=x_{{max}}-x_{{min}}={v[-1]}-{v[0]}={R}$.")
        b.mc(B14, 'th', 'Khoảng tứ phân vị', f"Cho mẫu số liệu (đã sắp xếp): {data_txt}. Khoảng tứ phân vị $\\Delta_Q$ bằng:", M(d2(iqr)),
             [M(d2(q3 + q1)), M(str(R)), M(d2(iqr + 1)), M(d2(iqr - 1))],
             f"$Q_1={d2(q1)}$, $Q_3={d2(q3)}$ nên $\\Delta_Q=Q_3-Q_1={d2(iqr)}$.")
        sq = ", ".join(f"({x}-{d2(mu)})^2" for x in v[:3]) + ", \\dots"
        b.mc(B14, 'th', 'Phương sai', f"Cho mẫu số liệu: {data_txt}. Phương sai $s^2$ của mẫu bằng:", M(d2(s2)),
             [M(d2(var(v) * Fraction(n, n - 1))), M(d2(Fraction(sum(x * x for x in v), n))), M(fnum(sd, 2)) if abs(sd - float(s2)) > 0.01 else M(d2(s2 + 2)), M(d2(s2 + 1))],
             f"Số trung bình $\\bar x={d2(mu)}$. Phương sai $s^2=\\frac{{1}}{{n}}\\sum (x_i-\\bar x)^2=\\frac{{1}}{{n}}\\sum x_i^2-\\bar x^2=\\frac{{{sum(x*x for x in v)}}}{{{n}}}-({d2(mu)})^2={d2(s2)}$.")
        b.sa(B14, 'th', 'Phương sai', f"Cho mẫu số liệu: {data_txt}. Tính phương sai của mẫu (làm tròn đến hàng phần trăm).", float(s2),
             f"$\\bar x={d2(mu)}$; $s^2=\\frac{{1}}{{n}}\\sum x_i^2-\\bar x^2=\\frac{{{sum(x*x for x in v)}}}{{{n}}}-({d2(mu)})^2={d2(s2)}$.", tol=0.01)
        if k % 2 == 1:
            b.sa(B14, 'vd', 'Độ lệch chuẩn', f"Cho mẫu số liệu: {data_txt}. Tính độ lệch chuẩn của mẫu (làm tròn đến hàng phần trăm).", sd,
                 f"$s^2={d2(s2)}$ nên độ lệch chuẩn $s=\\sqrt{{s^2}}=\\sqrt{{{d2(s2)}}}\\approx {fnum(sd, 2)}$.", tol=0.01)
            b.mc(B14, 'vd', 'Độ lệch chuẩn', f"Cho mẫu số liệu: {data_txt}. Độ lệch chuẩn của mẫu (làm tròn đến hàng phần trăm) bằng:", M(fnum(sd, 2)),
                 [M(d2(s2)) if abs(sd - float(s2)) > 0.005 else M(fnum(sd + 0.5, 2)), M(fnum(sd + 0.3, 2)), M(fnum(max(sd - 0.4, 0.1), 2)), M(fnum(sd * 2, 2))],
                 f"Phương sai $s^2={d2(s2)}$; độ lệch chuẩn là căn bậc hai của phương sai: $s=\\sqrt{{{d2(s2)}}}\\approx {fnum(sd, 2)}$.")
    # giá trị ngoại lệ
    cases = [([4, 5, 6, 6, 7, 8, 9, 35], 35), ([10, 12, 13, 14, 15, 16, 18, 2], 2), ([20, 22, 23, 25, 26, 27, 28, 60], 60), ([3, 4, 5, 5, 6, 7, 8, 40], 40)]
    for (v, out) in cases:
        v = sorted(v); q1, q2, q3 = quart(v); iqr = q3 - q1
        lo, hi = q1 - Fraction(3, 2) * iqr, q3 + Fraction(3, 2) * iqr
        assert out < lo or out > hi
        rest = [x for x in v if lo <= x <= hi]
        b.mc(B14, 'vd', 'Giá trị ngoại lệ', f"Cho mẫu số liệu: {lst(v)}. Giá trị nào là giá trị ngoại lệ của mẫu?", M(str(out)),
             [M(str(x)) for x in rest if x != out][:4],
             f"$Q_1={d2(q1)}$, $Q_3={d2(q3)}$, $\\Delta_Q={d2(iqr)}$. Ngưỡng ngoại lệ: dưới $Q_1-1,5\\Delta_Q={d2(lo)}$ hoặc trên $Q_3+1,5\\Delta_Q={d2(hi)}$. Chỉ có ${out}$ nằm ngoài khoảng này.")
        b.sa(B14, 'vd', 'Giá trị ngoại lệ', f"Cho mẫu số liệu: {lst(v)}. Tìm giá trị ngoại lệ của mẫu (nếu có).", out,
             f"$\\Delta_Q={d2(iqr)}$; các ngưỡng là ${d2(lo)}$ và ${d2(hi)}$. Giá trị ${out}$ nằm ngoài nên là giá trị ngoại lệ.")
    # khái niệm
    b.mc(B13, 'nb', 'Khái niệm số trung bình', "Số trung bình của mẫu số liệu $x_1, x_2,\\dots,x_n$ được tính bằng công thức:", M('\\bar x=\\frac{x_1+x_2+\\dots+x_n}{n}'),
         [M('\\bar x=\\frac{x_1+x_2+\\dots+x_n}{n+1}'), M('\\bar x=x_1\\cdot x_2\\cdots x_n'), M('\\bar x=\\frac{x_{max}+x_{min}}{2}')],
         "Số trung bình cộng bằng tổng tất cả các giá trị chia cho số giá trị của mẫu.")
    b.mc(B14, 'nb', 'Khái niệm phương sai', "Công thức nào sau đây là công thức tính phương sai $s^2$ của mẫu số liệu $x_1,\\dots,x_n$ có số trung bình $\\bar x$?", M('s^2=\\frac{1}{n}\\sum_{i=1}^{n}(x_i-\\bar x)^2'),
         [M('s^2=\\frac{1}{n}\\sum_{i=1}^{n}(x_i-\\bar x)'), M('s^2=\\sum_{i=1}^{n}(x_i-\\bar x)^2'), M('s^2=\\frac{1}{n}\\sum_{i=1}^{n}x_i')],
         "Phương sai là trung bình cộng của bình phương độ lệch của các giá trị so với số trung bình: $s^2=\\frac{1}{n}\\sum (x_i-\\bar x)^2$.")
    b.mc(B14, 'nb', 'Ý nghĩa độ lệch chuẩn', "Độ lệch chuẩn của mẫu số liệu càng lớn thì:", "Các giá trị của mẫu càng phân tán (cách xa số trung bình)",
         ["Các giá trị của mẫu càng tập trung quanh số trung bình", "Số trung bình của mẫu càng lớn", "Mẫu có càng nhiều giá trị bằng nhau"],
         "Độ lệch chuẩn đo mức độ phân tán của số liệu quanh số trung bình: độ lệch chuẩn càng lớn thì số liệu càng phân tán.")
    return b
