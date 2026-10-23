# -*- coding: utf-8 -*-
"""Hóa học 10 (KNTT): đáp án tính bằng code (cấu hình electron, số oxi hóa, cân bằng nguyên tử, enthalpy)."""
import re, math
from math import gcd
from .common import Bank, fnum
from .phys import fmt, nm, sa

SYMB = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}
ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII'}
EN = {'H': 2.20, 'Li': 0.98, 'Be': 1.57, 'B': 2.04, 'C': 2.55, 'N': 3.04, 'O': 3.44, 'F': 3.98, 'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.90, 'P': 2.19, 'S': 2.58, 'Cl': 3.16, 'K': 0.82, 'Ca': 1.00, 'Br': 2.96}

def F(s):
    """Công thức hoá học -> LaTeX: H2SO4 -> \\mathrm{H_{2}SO_{4}}."""
    return "\\mathrm{" + re.sub(r'(?<=[A-Za-z\)])(\d+)', r'_{\1}', s) + "}"

def Fi(s, ch):
    """Ion: Fi('Fe','3+') -> \\mathrm{Fe}^{3+}."""
    return F(s) + "^{" + ch + "}"

def cfg_list(z):
    order = [(1, 's', 2), (2, 's', 2), (2, 'p', 6), (3, 's', 2), (3, 'p', 6), (4, 's', 2)]
    out, left = [], z
    for (n, l, cap) in order:
        if left <= 0: break
        e = min(cap, left); out.append((n, l, e)); left -= e
    assert left == 0
    return out

def cfg(z):
    return " ".join(f"{n}{l}^{{{e}}}" for (n, l, e) in cfg_list(z))

def shells(z): return max(n for (n, l, e) in cfg_list(z))
def valence(z):
    n = shells(z); return sum(e for (m, l, e) in cfg_list(z) if m == n)

def pick(correct, pool, k=3):
    seen, out = {correct}, []
    for x in pool:
        if x not in seen: seen.add(x); out.append(x)
        if len(out) >= k: break
    assert len(out) == k, (correct, pool)
    return out

# --- đếm nguyên tử để kiểm cân bằng phương trình ---
def count_atoms(formula):
    def parse(s, i=0):
        res = {}
        while i < len(s):
            c = s[i]
            if c == '(':
                sub, i = parse(s, i + 1)
                m = re.match(r'\d+', s[i:]); k = int(m.group()) if m else 1
                if m: i += len(m.group())
                for a, v in sub.items(): res[a] = res.get(a, 0) + v * k
            elif c == ')':
                return res, i + 1
            else:
                m = re.match(r'([A-Z][a-z]?)(\d*)', s[i:])
                a, k = m.group(1), int(m.group(2) or 1)
                res[a] = res.get(a, 0) + k; i += len(m.group())
        return res, i
    return parse(formula)[0]

def side(items):
    tot = {}
    for (k, f) in items:
        for a, v in count_atoms(f).items(): tot[a] = tot.get(a, 0) + k * v
    return tot

def eq_str(left, right):
    return " + ".join((str(k) if k != 1 else "") + F(f) for k, f in left) + " \\rightarrow " + " + ".join((str(k) if k != 1 else "") + F(f) for k, f in right)

# ======================== CHƯƠNG 1 ========================
def c1():
    b = Bank('hoa10', 'c1')
    # --- Thành phần nguyên tử ---
    els = [('Na', 11, 23), ('Mg', 12, 24), ('Al', 13, 27), ('Cl', 17, 35), ('K', 19, 39), ('Ca', 20, 40), ('O', 8, 16), ('N', 7, 14), ('C', 6, 12), ('Fe', 26, 56), ('Cu', 29, 64), ('Zn', 30, 65)]
    for (s, z, a) in els:
        n = a - z
        nm(b, 'b1', 'nb', 'Số neutron', f"Nguyên tử {s} có số hiệu nguyên tử $Z={z}$ và số khối $A={a}$. Số neutron trong hạt nhân là:", n, [z, a, a + z, n + 1], '', f"Số neutron bằng hiệu giữa số khối và số hiệu nguyên tử: $N=A-Z={a}-{z}={n}$.", nd=0)
        sa(b, 'b1', 'nb', 'Số neutron', f"Nguyên tử {s} có $Z={z}$, $A={a}$. Tính số neutron trong hạt nhân.", n, f"$N=A-Z={a}-{z}={n}$.")
    for (s, z, a) in els[:8]:
        b.mc('b1', 'nb', 'Số hạt', f"Nguyên tử {s} có $Z={z}$ và $A={a}$ (nguyên tử trung hoà điện). Số electron của nguyên tử là:", str(z), [str(a), str(a - z), str(a + z)], f"Nguyên tử trung hoà điện nên số electron bằng số proton, bằng $Z={z}$.")
    for (z, n) in ((11, 12), (17, 18), (13, 14), (19, 20), (26, 30), (20, 20), (12, 12)):
        S, d = 2 * z + n, 2 * z - n
        nm(b, 'b1', 'vd', 'Tổng số hạt', f"Nguyên tử X có tổng số hạt (proton, neutron, electron) là {S}, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là {d}. Số hiệu nguyên tử $Z$ của X là:", z, [n, S - z, (S + d) / 2, z + 1], '', f"Gọi $p=e=Z$, số neutron $N$. Ta có $2Z+N={S}$ và $2Z-N={d}$. Cộng hai vế: $4Z={S+d}\\Rightarrow Z={z}$ (và $N={n}$).", nd=0)
        sa(b, 'b1', 'vd', 'Tổng số hạt', f"Nguyên tử X có tổng số hạt là {S}, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là {d}. Tính số khối $A$ của X.", z + n, f"$2Z+N={S}$ và $2Z-N={d}$ nên $Z={z}$, $N={n}$; số khối $A=Z+N={z+n}$.")
    # --- đồng vị ---
    for (iso, ans) in (([(35, 75), (37, 25)], 35.5), ([(10, 20), (11, 80)], 10.8), ([(63, 69), (65, 31)], 63.62), ([(1, 99), (2, 1)], 1.01), ([(24, 79), (25, 10), (26, 11)], 24.32), ([(12, 99), (13, 1)], 12.01)):
        avg = sum(a * p for a, p in iso) / 100
        assert abs(avg - ans) < 1e-9
        desc = ", ".join(f"${a}$ ({p}%)" for a, p in iso)
        nm(b, 'b1', 'th', 'Nguyên tử khối trung bình', f"Nguyên tố X có các đồng vị với số khối (phần trăm số nguyên tử): {desc}. Nguyên tử khối trung bình của X là:", avg, [sum(a for a, _ in iso) / len(iso), max(a for a, _ in iso), avg + 0.5, avg - 0.5], '', f"$\\bar A=\\dfrac{{" + "+".join(f"{a}\\times{p}" for a, p in iso) + f"}}{{100}}={fnum(avg)}$.")
        sa(b, 'b1', 'th', 'Nguyên tử khối trung bình', f"Nguyên tố X có các đồng vị: {desc}. Tính nguyên tử khối trung bình của X (làm tròn đến hai chữ số thập phân).", avg, f"$\\bar A=\\dfrac{{" + "+".join(f"{a}\\times{p}" for a, p in iso) + f"}}{{100}}={fnum(avg)}$.")
    for (a1, a2, abar, p1) in ((35, 37, 35.5, 75), (10, 11, 10.8, 20), (63, 65, 63.5, 75), (79, 81, 79.2, 90)):
        assert abs((a2 - abar) / (a2 - a1) * 100 - p1) < 1e-6
        nm(b, 'b1', 'vd', 'Phần trăm đồng vị', f"Nguyên tố X có hai đồng vị bền có số khối {a1} và {a2}, nguyên tử khối trung bình là {fnum(abar)}. Phần trăm số nguyên tử của đồng vị {a1}X là:", p1, [100 - p1, p1 / 2, 50, (100 - p1) / 2], '%', f"Gọi $x$ là phần trăm đồng vị {a1}: ${a1}x+{a2}(100-x)={fnum(abar*100)}\\Rightarrow x={p1}$. Vậy đồng vị {a1} chiếm ${p1}\\%$.", nd=1)
    # lý thuyết
    for (st, ok, ws, ex) in (
        ("Hạt nào sau đây mang điện tích dương trong nguyên tử?", "Proton", ["Neutron", "Electron", "Photon"], "Proton mang điện tích $+1$; electron mang điện tích $-1$; neutron không mang điện."),
        ("Hạt nào trong nguyên tử không mang điện?", "Neutron", ["Proton", "Electron", "Ion"], "Neutron là hạt không mang điện, nằm trong hạt nhân cùng với proton."),
        ("Khối lượng nguyên tử tập trung chủ yếu ở:", "Hạt nhân", ["Lớp vỏ electron", "Lớp electron ngoài cùng", "Khoảng không gian giữa hạt nhân và vỏ"], "Khối lượng của electron rất nhỏ so với proton và neutron nên khối lượng nguyên tử tập trung ở hạt nhân."),
        ("Đồng vị là những nguyên tử có cùng:", "Số proton nhưng khác số neutron", ["Số neutron nhưng khác số proton", "Số khối nhưng khác số proton", "Số electron lớp ngoài cùng nhưng khác số proton"], "Các đồng vị của một nguyên tố có cùng $Z$ (cùng số proton) nhưng khác số neutron nên khác số khối $A$."),
        ("Số hiệu nguyên tử $Z$ của một nguyên tố cho biết:", "Số proton trong hạt nhân", ["Số neutron trong hạt nhân", "Tổng số proton và neutron", "Số lớp electron"], "Số hiệu nguyên tử $Z$ bằng số proton trong hạt nhân (và bằng số electron của nguyên tử trung hoà)."),
        ("Số khối $A$ của nguyên tử được tính bằng:", "Tổng số proton và số neutron", ["Tổng số proton và số electron", "Hiệu số neutron và proton", "Số proton"], "$A=Z+N$: số khối bằng tổng số proton và neutron trong hạt nhân.")):
        b.mc('b1', 'nb', 'Lý thuyết', st, ok, ws, ex)
    # --- Cấu hình electron ---
    zs = [3, 4, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20]
    for z in zs:
        s = SYMB[z]
        wrong = [cfg(w) for w in [z - 1, z + 1, z - 2, z + 2, z - 3, z + 3] if 1 <= w <= 20][:3]
        b.mc('b2', 'th', 'Cấu hình electron', f"Cấu hình electron của nguyên tử {s} ($Z={z}$) là:", f"${cfg(z)}$", [f"${w}$" for w in wrong], f"Điền {z} electron lần lượt vào các phân lớp theo thứ tự mức năng lượng tăng dần (1s, 2s, 2p, 3s, 3p, 4s): ${cfg(z)}$.")
        nl = shells(z); ne = valence(z)
        nm(b, 'b2', 'nb', 'Số lớp electron', f"Nguyên tử {s} ($Z={z}$) có bao nhiêu lớp electron?", nl, [nl + 1, nl - 1 if nl > 1 else nl + 2, z, ne], '', f"Cấu hình ${cfg(z)}$ có lớp lớn nhất là $n={nl}$ nên nguyên tử có {nl} lớp electron.", nd=0)
        nm(b, 'b2', 'th', 'Số electron lớp ngoài cùng', f"Số electron ở lớp ngoài cùng của nguyên tử {s} ($Z={z}$) là:", ne, [ne + 1, nl, z, 8 - ne if 8 - ne != ne else ne + 2], '', f"Cấu hình ${cfg(z)}$: lớp ngoài cùng $n={nl}$ có {ne} electron.", nd=0)
        sa(b, 'b2', 'th', 'Số electron lớp ngoài cùng', f"Viết cấu hình electron của nguyên tử {s} ($Z={z}$) rồi cho biết nguyên tử có bao nhiêu electron ở lớp ngoài cùng.", ne, f"Cấu hình electron: ${cfg(z)}$. Lớp ngoài cùng ($n={nl}$) có {ne} electron.")
        if z not in (10, 18):
            kind = 'kim loại' if z in (3, 4, 11, 12, 13, 19, 20) else 'phi kim'
            other = 'phi kim' if kind == 'kim loại' else 'kim loại'
            b.mc('b2', 'th', 'Tính chất theo số electron lớp ngoài cùng', f"Nguyên tử {s} ($Z={z}$) có {ne} electron ở lớp ngoài cùng, nên {s} là:", kind, [other, 'khí hiếm', 'chưa xác định được'], f"Nguyên tử có " + ("1, 2, 3 electron lớp ngoài cùng (trừ H, He, B) thường là kim loại." if kind == 'kim loại' else "5, 6, 7 electron lớp ngoài cùng thường là phi kim.") + f" {s} có {ne} electron ngoài cùng nên là {kind}.")
    for z in (2, 10, 18):
        pass
    b.mc('b2', 'nb', 'Khí hiếm', "Nguyên tử của nguyên tố nào sau đây có 8 electron ở lớp ngoài cùng và bền vững?", "Ar ($Z=18$)", ["Cl ($Z=17$)", "K ($Z=19$)", "S ($Z=16$)"], f"Ar có cấu hình ${cfg(18)}$ với 8 electron ở lớp ngoài cùng, là khí hiếm bền vững.")
    # ion
    for (z, ch, nmv) in ((11, 1, 'cation'), (12, 2, 'cation'), (13, 3, 'cation'), (19, 1, 'cation'), (20, 2, 'cation'), (9, -1, 'anion'), (17, -1, 'anion'), (8, -2, 'anion'), (16, -2, 'anion'), (7, -3, 'anion')):
        s = SYMB[z]; ne = z - ch
        sign = ('+' if ch > 0 else '-'); mag = abs(ch)
        ionlatex = F(s) + "^{" + (str(mag) if mag > 1 else '') + sign + "}"
        nm(b, 'b2', 'th', 'Số electron của ion', f"Ion ${ionlatex}$ (nguyên tử {s} có $Z={z}$) có bao nhiêu electron?", ne, [z, z + mag if ch > 0 else z - mag, ne + 2, ne - 1], '', f"Nguyên tử {s} có {z} electron; " + (f"{nmv} tạo thành do nhường {mag} electron nên còn {z}-{mag}={ne} electron." if ch > 0 else f"{nmv} tạo thành do nhận thêm {mag} electron nên có {z}+{mag}={ne} electron."), nd=0)
        sa(b, 'b2', 'th', 'Số electron của ion', f"Tính số electron của ion ${ionlatex}$ biết nguyên tử {s} có $Z={z}$.", ne, f"Số electron $={z}{'-' if ch>0 else '+'}{mag}={ne}$.")
    for (ne, ch, z) in ((18, -2, 16), (10, -3, 7), (18, -1, 17), (10, 2, 12), (10, 3, 13), (18, 1, 19)):
        mag = abs(ch); sign = '+' if ch > 0 else '-'
        ionlatex = "X^{" + (str(mag) if mag > 1 else '') + sign + "}"
        nm(b, 'b2', 'vd', 'Tìm Z từ ion', f"Ion ${ionlatex}$ có {ne} electron. Số hiệu nguyên tử $Z$ của X là:", z, [ne, ne + mag, ne - mag, z + 1] if True else [], '', f"Ion " + ("mang điện dương: đã mất electron nên " if ch > 0 else "mang điện âm: đã nhận electron nên ") + f"$Z={ne}{'+' if ch>0 else '-'}{mag}={z}$.", nd=0)
    for n in (1, 2, 3, 4):
        nm(b, 'b2', 'nb', 'Số electron tối đa trong lớp', f"Lớp electron thứ {n} ($n={n}$) chứa tối đa bao nhiêu electron?", 2 * n * n, [n * n, 2 * n, 8 if n != 2 else 18, 2 * n * n + 2], '', f"Số electron tối đa của lớp thứ $n$ là $2n^2=2\\times{n}^2={2*n*n}$.", nd=0)
    for (l, e, o) in (('s', 2, 1), ('p', 6, 3), ('d', 10, 5), ('f', 14, 7)):
        nm(b, 'b2', 'nb', 'Số electron tối đa trong phân lớp', f"Phân lớp {l} chứa tối đa bao nhiêu electron?", e, [e + 2, e - 2 if e > 2 else 4, o, 2 * e], '', f"Phân lớp {l} có {o} orbital, mỗi orbital chứa tối đa 2 electron nên chứa tối đa ${o}\\times2={e}$ electron.", nd=0)
        nm(b, 'b2', 'nb', 'Số orbital trong phân lớp', f"Phân lớp {l} có bao nhiêu orbital?", o, [e, o + 2, o - 1 if o > 1 else 3, 2 * o + 1 if 2 * o + 1 != o else 9], '', f"Phân lớp s, p, d, f lần lượt có 1, 3, 5, 7 orbital; phân lớp {l} có {o} orbital.", nd=0)
    return b

# ======================== CHƯƠNG 2 ========================
def c2():
    b = Bank('hoa10', 'c2')
    for z in (3, 4, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20):
        s = SYMB[z]; p = shells(z); g = valence(z)
        ans = f"Chu kì {p}, nhóm {ROMAN[g]}A"
        pool = [f"Chu kì {p}, nhóm {ROMAN[min(8, g + 1)]}A", f"Chu kì {p + 1}, nhóm {ROMAN[g]}A", f"Chu kì {g}, nhóm {ROMAN[p]}A", f"Chu kì {max(1, p - 1)}, nhóm {ROMAN[g]}A", f"Chu kì {p}, nhóm {ROMAN[max(1, g - 1)]}A"]
        b.mc('b3', 'th', 'Vị trí trong bảng tuần hoàn', f"Nguyên tố {s} ($Z={z}$) ở vị trí nào trong bảng tuần hoàn?", ans, pick(ans, pool), f"Cấu hình ${cfg(z)}$: có {p} lớp electron nên ở chu kì {p}; {g} electron ngoài cùng (nguyên tố s, p) nên ở nhóm {ROMAN[g]}A.")
        sa(b, 'b3', 'th', 'Số thứ tự chu kì', f"Nguyên tố {s} có $Z={z}$. Hỏi {s} thuộc chu kì mấy?", p, f"Cấu hình ${cfg(z)}$ có {p} lớp electron nên {s} thuộc chu kì {p}.")
    for z in (3, 11, 12, 13, 15, 16, 17, 19):
        s = SYMB[z]; g = valence(z)
        sa(b, 'b3', 'th', 'Số thứ tự nhóm A', f"Nguyên tố {s} có $Z={z}$. {s} thuộc nhóm A thứ mấy? (nhập số, ví dụ nhóm IA nhập 1)", g, f"Nguyên tố nhóm A có số thứ tự nhóm bằng số electron lớp ngoài cùng: ${cfg(z)}$ có {g} electron ngoài cùng nên thuộc nhóm {ROMAN[g]}A.")
    for (c, n) in ((1, 2), (2, 8), (3, 8), (4, 18), (5, 18), (6, 32), (7, 32)):
        nm(b, 'b3', 'nb', 'Số nguyên tố trong chu kì', f"Chu kì {c} của bảng tuần hoàn có bao nhiêu nguyên tố?", n, [n + 2, n - 2 if n > 2 else 8, 18 if n != 18 else 8, 32 if n != 32 else 18], '', f"Số nguyên tố trong các chu kì 1, 2, 3, 4, 5, 6, 7 lần lượt là 2, 8, 8, 18, 18, 32, 32. Chu kì {c} có {n} nguyên tố.", nd=0)
    # oxide cao nhất / hydride
    OX = {11: ('Na2O', 'bazơ'), 12: ('MgO', 'bazơ'), 13: ('Al2O3', 'lưỡng tính'), 14: ('SiO2', 'axit'), 15: ('P2O5', 'axit'), 16: ('SO3', 'axit'), 17: ('Cl2O7', 'axit')}
    for z, (ox, tc) in OX.items():
        s = SYMB[z]
        pool = [F(o) for o in ('Na2O', 'MgO', 'Al2O3', 'SiO2', 'P2O5', 'SO3', 'Cl2O7', 'SO2', 'P2O3', 'ClO2') if o != ox]
        b.mc('b4', 'th', 'Oxide cao nhất', f"Công thức oxide ứng với hoá trị cao nhất của nguyên tố {s} ($Z={z}$) là:", f"${F(ox)}$", [f"${p}$" for p in pick(F(ox), pool)], f"{s} thuộc nhóm {ROMAN[z-10 if z>=11 else 0]}A nên hoá trị cao nhất với oxygen bằng {z-10}; oxide cao nhất là ${F(ox)}$.")
        b.mc('b4', 'th', 'Tính chất oxide', f"Oxide cao nhất của {s} ($Z={z}$) là ${F(ox)}$. Đó là oxide:", {'bazơ': 'bazơ', 'axit': 'axit', 'lưỡng tính': 'lưỡng tính'}[tc], pick(tc, ['bazơ', 'axit', 'lưỡng tính', 'trung tính']), f"Trong chu kì 3, từ Na đến Cl tính bazơ của oxide giảm dần, tính axit tăng dần: ${F(ox)}$ là oxide {tc}.")
    HY = {14: 'SiH4', 15: 'PH3', 16: 'H2S', 17: 'HCl'}
    for z, h in HY.items():
        s = SYMB[z]
        pool = [F(x) for x in ('SiH4', 'PH3', 'H2S', 'HCl', 'SH4', 'PH5', 'H3S', 'H2Cl') if x != h]
        b.mc('b4', 'th', 'Hợp chất khí với hydrogen', f"Công thức hợp chất khí với hydrogen của nguyên tố {s} ($Z={z}$) là:", f"${F(h)}$", [f"${p}$" for p in pick(F(h), pool)], f"{s} thuộc nhóm {ROMAN[z-10]}A nên hoá trị trong hợp chất khí với hydrogen là $8-{z-10}={18-z}$; công thức là ${F(h)}$.")
    # xác định nguyên tố từ % khối lượng trong hợp chất khí với H
    for (h, Rs, ar, pct, x) in (('RH3', 'N', 14, 82.35, 3), ('RH4', 'C', 12, 75.0, 4), ('RH2', 'S', 32, 94.12, 2), ('HR', 'Cl', 35.5, 97.26, 1)):
        mm = ar + x * 1.0
        calc = ar / mm * 100
        assert abs(calc - pct) < 0.01, (Rs, calc)
        pool = ['N', 'C', 'S', 'Cl', 'P', 'Si', 'O', 'F']
        b.mc('b4', 'vd', 'Xác định nguyên tố', f"Nguyên tố R tạo hợp chất khí với hydrogen có công thức ${F(h)}$, trong đó R chiếm ${fnum(pct)}\\%$ về khối lượng. R là nguyên tố:", Rs, pick(Rs, pool), f"Gọi nguyên tử khối của R là $M$: $\\dfrac{{M}}{{M+{x}}}={fnum(pct/100,4)}\\Rightarrow M\\approx{fnum(ar)}$, ứng với nguyên tố {Rs}.")
    # xu hướng
    per3 = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']
    for grp in (['Na', 'Mg', 'Al', 'Si'], ['Mg', 'Al', 'P', 'S'], ['Na', 'Al', 'S', 'Cl'], ['Mg', 'Si', 'P', 'Cl']):
        small, big = grp[0], grp[-1]
        b.mc('b4', 'th', 'Bán kính nguyên tử trong chu kì', f"Trong các nguyên tử {', '.join(grp)} (cùng chu kì 3), nguyên tử có bán kính lớn nhất là:", small, pick(small, [x for x in grp[1:]]), f"Trong một chu kì, theo chiều tăng điện tích hạt nhân bán kính nguyên tử giảm dần; {small} đứng đầu nên có bán kính lớn nhất.")
        b.mc('b4', 'th', 'Độ âm điện trong chu kì', f"Trong các nguyên tố {', '.join(grp)} (cùng chu kì 3), nguyên tố có độ âm điện lớn nhất là:", big, pick(big, grp[:-1]), f"Trong một chu kì, theo chiều tăng điện tích hạt nhân độ âm điện tăng dần; {big} đứng cuối nên có độ âm điện lớn nhất.")
        b.mc('b4', 'th', 'Tính kim loại trong chu kì', f"Trong các nguyên tố {', '.join(grp)} (cùng chu kì 3), nguyên tố có tính kim loại mạnh nhất là:", small, pick(small, grp[1:]), f"Trong một chu kì, tính kim loại giảm dần từ trái sang phải; {small} đứng đầu nên có tính kim loại mạnh nhất.")
        b.mc('b4', 'th', 'Tính phi kim trong chu kì', f"Trong các nguyên tố {', '.join(grp)} (cùng chu kì 3), nguyên tố có tính phi kim mạnh nhất là:", big, pick(big, grp[:-1]), f"Trong một chu kì, tính phi kim tăng dần từ trái sang phải; {big} đứng cuối nên có tính phi kim mạnh nhất.")
    for grp in (['Li', 'Na', 'K'], ['F', 'Cl', 'Br'], ['Be', 'Mg', 'Ca']):
        top, bottom = grp[0], grp[-1]
        b.mc('b4', 'th', 'Bán kính nguyên tử trong nhóm', f"Trong các nguyên tử {', '.join(grp)} (cùng nhóm A), nguyên tử có bán kính lớn nhất là:", bottom, pick(bottom, grp[:-1] + ['H', 'He']), f"Trong một nhóm A, từ trên xuống dưới số lớp electron tăng nên bán kính nguyên tử tăng; {bottom} ở dưới cùng nên lớn nhất.")
        b.mc('b4', 'th', 'Độ âm điện trong nhóm', f"Trong các nguyên tố {', '.join(grp)} (cùng nhóm A), nguyên tố có độ âm điện lớn nhất là:", top, pick(top, grp[1:] + ['H', 'He']), f"Trong một nhóm A, từ trên xuống dưới độ âm điện giảm dần; {top} ở trên cùng nên có độ âm điện lớn nhất.")
    for (a, c) in (('Na', 'Mg'), ('Mg', 'Al'), ('Cl', 'S'), ('P', 'S')):
        pass
    b.mc('b4', 'nb', 'Độ âm điện lớn nhất', "Nguyên tố có độ âm điện lớn nhất trong bảng tuần hoàn là:", "F", ["Cl", "O", "N"], "Fluorine (F) có độ âm điện lớn nhất (3,98) trong các nguyên tố.")
    b.mc('b3', 'nb', 'Nguyên tố s, p', "Nguyên tố thuộc nhóm A là các nguyên tố:", "s và p", ["d và f", "chỉ nguyên tố d", "chỉ nguyên tố f"], "Nhóm A gồm các nguyên tố s và p; nhóm B gồm các nguyên tố d và f.")
    b.mc('b3', 'nb', 'Chu kì', "Các nguyên tố trong cùng một chu kì có cùng:", "Số lớp electron", ["Số electron lớp ngoài cùng", "Số proton", "Số neutron"], "Số thứ tự chu kì bằng số lớp electron nên các nguyên tố cùng chu kì có cùng số lớp electron.")
    b.mc('b3', 'nb', 'Nhóm A', "Các nguyên tố trong cùng một nhóm A có cùng:", "Số electron lớp ngoài cùng", ["Số lớp electron", "Số proton", "Số khối"], "Các nguyên tố cùng nhóm A có cùng số electron lớp ngoài cùng nên có tính chất hoá học tương tự nhau.")
    return b

# ======================== CHƯƠNG 3 ========================
def c3():
    b = Bank('hoa10', 'c3')
    ION = [('NaCl', 'Na', 'Cl'), ('KBr', 'K', 'Br'), ('MgO', 'Mg', 'O'), ('LiF', 'Li', 'F'), ('CaCl2', 'Ca', 'Cl'), ('NaF', 'Na', 'F'), ('K2O', 'K', 'O'), ('CaO', 'Ca', 'O')]
    NONP = [('H2', 'H', 'H'), ('Cl2', 'Cl', 'Cl'), ('N2', 'N', 'N'), ('O2', 'O', 'O'), ('CH4', 'C', 'H'), ('Br2', 'Br', 'Br')]
    POL = [('HCl', 'H', 'Cl'), ('H2O', 'H', 'O'), ('NH3', 'H', 'N'), ('CO2', 'C', 'O'), ('HBr', 'H', 'Br'), ('SO2', 'S', 'O'), ('CCl4', 'C', 'Cl')]
    def dchi(a, c): return round(abs(EN[a] - EN[c]), 2)
    allc = [(f, a, c, 'ion') for f, a, c in ION] + [(f, a, c, 'cht phân cực') for f, a, c in POL] + [(f, a, c, 'cht không cực') for f, a, c in NONP]
    names = {'ion': 'Liên kết ion', 'cht phân cực': 'Liên kết cộng hoá trị phân cực', 'cht không cực': 'Liên kết cộng hoá trị không cực'}
    for f, a, c, kind in allc:
        d = dchi(a, c)
        if kind == 'ion': assert d >= 1.7, f
        elif kind == 'cht phân cực': assert 0.4 <= d < 1.7, f
        else: assert d < 0.4, f
        rng = "$\\Delta\\chi\\ge1{,}7$" if kind == 'ion' else ("$0{,}4\\le\\Delta\\chi<1{,}7$" if kind == 'cht phân cực' else "$0\\le\\Delta\\chi<0{,}4$")
        ex = f"Hiệu độ âm điện $\\Delta\\chi=|{fnum(EN[a])}-{fnum(EN[c])}|={fnum(d)}$ nên thuộc khoảng {rng}: {names[kind].lower()}."
        if a == c: ex = f"Hai nguyên tử giống nhau nên $\\Delta\\chi=0<0{{,}}4$: {names[kind].lower()}."
        b.mc('b5', 'th', 'Loại liên kết', f"Cho độ âm điện: " + ", ".join(sorted({f"{x} ({fnum(EN[x])})" for x in (a, c)})) + f". Liên kết trong phân tử/hợp chất ${F(f)}$ là:", names[kind], pick(names[kind], list(names.values()) + ['Liên kết hydrogen']), ex)
    # nhận định: chất có liên kết ion
    for kindq, pool_ok, pool_bad in (('ion', [f for f, _, _ in ION], [f for f, _, _ in POL + NONP]), ('cộng hoá trị', [f for f, _, _ in POL + NONP], [f for f, _, _ in ION])):
        for i in range(3):
            ok = pool_ok[i * 2 % len(pool_ok)]
            wrong = [pool_bad[(i + j) % len(pool_bad)] for j in range(3)]
            b.mc('b5', 'th', 'Nhận biết chất', f"Chất nào sau đây có liên kết {kindq} (liên kết chủ yếu giữa các nguyên tử trong chất)?", f"${F(ok)}$", [f"${F(w)}$" for w in wrong], f"{F(ok)} " + ("được tạo từ kim loại điển hình và phi kim điển hình ($\\Delta\\chi\\ge1{,}7$) nên là hợp chất ion." if kindq == 'ion' else "được tạo từ các phi kim nên liên kết là liên kết cộng hoá trị.").replace('{F(ok)} ', ''))
    # tạo ion
    for z in (3, 4, 11, 12, 13, 19, 20):
        s = SYMB[z]; e = valence(z)
        ans = f"${F(s)}^{{{e if e>1 else ''}+}}$"
        pool = [f"${F(s)}^{{{k if k>1 else ''}+}}$" for k in (1, 2, 3) if k != e] + [f"${F(s)}^{{{e if e>1 else ''}-}}$"]
        b.mc('b5', 'th', 'Sự tạo thành ion dương', f"Khi nguyên tử {s} ($Z={z}$) đạt cấu hình bền vững của khí hiếm, nó tạo thành ion nào?", ans, pick(ans, pool), f"{s} có {e} electron ở lớp ngoài cùng (${cfg(z)}$) nên nhường {e} electron để tạo ion ${F(s)}^{{{e if e>1 else ''}+}}$.")
    for z in (7, 8, 9, 15, 16, 17):
        s = SYMB[z]; e = 8 - valence(z)
        ans = f"${F(s)}^{{{e if e>1 else ''}-}}$"
        pool = [f"${F(s)}^{{{k if k>1 else ''}-}}$" for k in (1, 2, 3) if k != e] + [f"${F(s)}^{{{e if e>1 else ''}+}}$"]
        b.mc('b5', 'th', 'Sự tạo thành ion âm', f"Khi nguyên tử {s} ($Z={z}$) đạt cấu hình bền vững của khí hiếm, nó tạo thành ion nào?", ans, pick(ans, pool), f"{s} có {8-e} electron ở lớp ngoài cùng (${cfg(z)}$) nên nhận thêm {e} electron để đủ 8 electron, tạo ion ${F(s)}^{{{e if e>1 else ''}-}}$.")
    # công thức hợp chất ion
    CAT = {'Na': 1, 'K': 1, 'Mg': 2, 'Ca': 2, 'Al': 3}; AN = {'Cl': 1, 'F': 1, 'O': 2, 'S': 2, 'N': 3}
    for (c, a) in (('Na', 'Cl'), ('Mg', 'Cl'), ('Al', 'O'), ('Ca', 'O'), ('Na', 'O'), ('Al', 'Cl'), ('Mg', 'N'), ('K', 'S'), ('Ca', 'F'), ('Al', 'S')):
        x, y = CAT[c], AN[a]; l = x * y // gcd(x, y)
        nc, na = l // x, l // y
        ans = F(c + (str(nc) if nc > 1 else '') + a + (str(na) if na > 1 else ''))
        wrong = [F(c + (str(x) if x > 1 else '') + a + (str(y) if y > 1 else '')), F(c + (str(y) if y > 1 else '') + a + (str(x) if x > 1 else '')), F(c + a), F(c + '2' + a + '3'), F(c + '3' + a + '2')]
        if nc == na == 1: wrong = [F(c + '2' + a), F(c + a + '2'), F(c + '2' + a + '2'), F(c + '3' + a)]
        wrong += [F(c + (str(i) if i > 1 else '') + a + (str(j) if j > 1 else '')) for i in (1, 2, 3) for j in (1, 2, 3)]
        b.mc('b5', 'vd', 'Công thức hợp chất ion', f"Hợp chất tạo bởi ion ${Fi(c, str(x)+'+' if x>1 else '+')}$ và ion ${Fi(a, str(y)+'-' if y>1 else '-')}$ có công thức là:", f"${ans}$", [f"${w}$" for w in pick(ans, wrong)], f"Hợp chất trung hoà điện: tổng điện tích dương $=$ tổng điện tích âm. Số ion {c}: ${nc}$, số ion {a}: ${na}$ (${nc}\\times{x}={na}\\times{y}$) nên công thức là ${ans}$.")
    # liên kết CHT
    LW = [('H2O', 8, 2, 2, 'H-O'), ('NH3', 8, 3, 1, ''), ('CH4', 8, 4, 0, ''), ('HCl', 8, 1, 3, ''), ('Cl2', 14, 1, 6, ''), ('N2', 10, 3, 2, ''), ('O2', 12, 2, 4, ''), ('CO2', 16, 4, 4, ''), ('H2', 2, 1, 0, '')]
    for (f, V, B, L, _) in LW:
        # V: tổng electron hoá trị; B: tổng số cặp electron dùng chung; L: số cặp electron không liên kết
        assert (V - 2 * B) % 2 == 0 and (V - 2 * B) // 2 == L, f
        nm(b, 'b5', 'th', 'Số cặp electron dùng chung', f"Trong phân tử ${F(f)}$, tổng số cặp electron dùng chung giữa các nguyên tử là:", B, [L, B + 1, V // 2, B + 2 if B + 2 != L else B + 3], '', f"Tổng số electron hoá trị là {V}. Theo cấu trúc Lewis của ${F(f)}$, có {B} cặp electron dùng chung và {L} cặp electron chưa tham gia liên kết ($2\\times{B}+2\\times{L}={V}$).", nd=0)
        sa(b, 'b5', 'th', 'Số cặp electron không liên kết', f"Trong phân tử ${F(f)}$, có bao nhiêu cặp electron hoá trị chưa tham gia liên kết (tính cho cả phân tử)?", L, f"Tổng electron hoá trị là {V} ({V//2} cặp); có {B} cặp dùng chung nên còn ${V//2}-{B}={L}$ cặp chưa liên kết.")
    b.mc('b5', 'nb', 'Liên kết ba', "Phân tử nào sau đây có liên kết ba giữa hai nguyên tử?", f"${F('N2')}$", [f"${F('O2')}$", f"${F('Cl2')}$", f"${F('H2')}$"], "Mỗi nguyên tử N có 5 electron hoá trị, cần góp chung 3 electron nên trong phân tử $\\mathrm{N_{2}}$ có liên kết ba giữa hai nguyên tử N.")
    b.mc('b5', 'nb', 'Quy tắc octet', "Theo quy tắc octet, khi tạo liên kết hoá học các nguyên tử có xu hướng:", "Đạt cấu hình 8 electron ở lớp ngoài cùng (giống khí hiếm)", ["Mất hết electron lớp ngoài cùng", "Nhận thêm càng nhiều electron càng tốt", "Giữ nguyên số electron lớp ngoài cùng"], "Quy tắc octet: nguyên tử nhường, nhận hoặc dùng chung electron để lớp ngoài cùng có 8 electron (hoặc 2 electron với H, He).")
    b.mc('b5', 'nb', 'Tính chất hợp chất ion', "Tính chất nào sau đây đặc trưng của hợp chất ion ở điều kiện thường?", "Ở trạng thái rắn, nhiệt độ nóng chảy cao", ["Thường là chất khí", "Tan tốt trong dung môi không phân cực", "Dễ bay hơi"], "Hợp chất ion là chất rắn, bền vững, có nhiệt độ nóng chảy và nhiệt độ sôi cao do lực hút tĩnh điện mạnh.")
    # b6
    for (st, ok, ws, ex) in (
        ("Liên kết hydrogen được hình thành giữa nguyên tử H (liên kết với nguyên tử có độ âm điện lớn) với nguyên tử nào sau đây?", "F, O, N còn cặp electron chưa liên kết", ["C, Si", "Na, K", "Ar, Ne"], "Liên kết hydrogen thường hình thành giữa H (đã liên kết với F, O, N) với nguyên tử F, O, N khác có cặp electron chưa liên kết."),
        ("Chất nào sau đây có liên kết hydrogen giữa các phân tử?", f"${F('H2O')}$", [f"${F('CH4')}$", f"${F('H2')}$", f"${F('CO2')}$"], "Nước có H liên kết với O (độ âm điện lớn) nên giữa các phân tử nước có liên kết hydrogen; CH₄, H₂, CO₂ không có."),
        ("Chất nào sau đây có liên kết hydrogen giữa các phân tử?", f"${F('NH3')}$", [f"${F('CH4')}$", f"${F('N2')}$", f"${F('CO2')}$"], "Trong NH₃, H liên kết với N (độ âm điện lớn), nguyên tử N còn cặp electron chưa liên kết nên giữa các phân tử NH₃ có liên kết hydrogen."),
        ("Nước có nhiệt độ sôi cao hơn nhiều so với $\\mathrm{H_{2}S}$ chủ yếu là do:", "Giữa các phân tử nước có liên kết hydrogen", ["Nước có phân tử khối lớn hơn", "Nước có liên kết ion", "Nước có liên kết ba"], "Liên kết hydrogen giữa các phân tử $\\mathrm{H_{2}O}$ mạnh hơn nhiều so với lực van der Waals giữa các phân tử $\\mathrm{H_{2}S}$ nên nước sôi ở nhiệt độ cao hơn."),
        ("Tương tác van der Waals xuất hiện giữa:", "Các phân tử (kể cả không phân cực) ở khoảng cách đủ gần", ["Chỉ giữa các ion trái dấu", "Chỉ giữa các phân tử có liên kết hydrogen", "Chỉ giữa các nguyên tử kim loại"], "Tương tác van der Waals là lực hút yếu giữa các phân tử (do lưỡng cực tạm thời hoặc vĩnh viễn), có ở mọi phân tử."),
        ("So với liên kết cộng hoá trị, liên kết hydrogen và tương tác van der Waals:", "Yếu hơn nhiều", ["Mạnh hơn nhiều", "Có độ bền tương đương", "Luôn mạnh hơn liên kết ion"], "Liên kết hydrogen và tương tác van der Waals là các tương tác yếu giữa các phân tử, yếu hơn nhiều so với liên kết cộng hoá trị."),
        ("Khi các phân tử khí hiếm như He, Ar hoá lỏng, lực liên kết giữa các nguyên tử chủ yếu là:", "Tương tác van der Waals", ["Liên kết ion", "Liên kết cộng hoá trị", "Liên kết kim loại"], "Khí hiếm tồn tại ở dạng nguyên tử đơn, giữa chúng chỉ có tương tác van der Waals yếu nên rất khó hoá lỏng."),
        ("Nhiệt độ sôi của các chất $\\mathrm{CH_{4}}$, $\\mathrm{C_{2}H_{6}}$, $\\mathrm{C_{3}H_{8}}$ tăng theo chiều phân tử khối tăng chủ yếu do:", "Tương tác van der Waals giữa các phân tử tăng", ["Liên kết hydrogen tăng", "Liên kết ion tăng", "Liên kết cộng hoá trị bền hơn"], "Các chất này không có liên kết hydrogen; phân tử khối tăng làm tương tác van der Waals mạnh hơn nên nhiệt độ sôi tăng.")):
        b.mc('b6', 'nb', 'Lý thuyết', st, ok, ws, ex)
    return b

# ======================== CHƯƠNG 4 ========================
OXN = [
    # (hợp chất LaTeX, nguyên tố, số nguyên tử X, [(số oxi hoá, số nguyên tử) của các nguyên tố còn lại], điện tích cả ion, đáp án)
    ('H2SO4', 'S', 1, [(1, 2), (-2, 4)], 0, 6), ('SO2', 'S', 1, [(-2, 2)], 0, 4), ('H2S', 'S', 1, [(1, 2)], 0, -2), ('SO3', 'S', 1, [(-2, 3)], 0, 6),
    ('NH3', 'N', 1, [(1, 3)], 0, -3), ('NO', 'N', 1, [(-2, 1)], 0, 2), ('NO2', 'N', 1, [(-2, 2)], 0, 4), ('HNO3', 'N', 1, [(1, 1), (-2, 3)], 0, 5), ('N2O', 'N', 2, [(-2, 1)], 0, 1),
    ('HCl', 'Cl', 1, [(1, 1)], 0, -1), ('HClO', 'Cl', 1, [(1, 1), (-2, 1)], 0, 1), ('KClO3', 'Cl', 1, [(1, 1), (-2, 3)], 0, 5), ('HClO4', 'Cl', 1, [(1, 1), (-2, 4)], 0, 7),
    ('KMnO4', 'Mn', 1, [(1, 1), (-2, 4)], 0, 7), ('MnO2', 'Mn', 1, [(-2, 2)], 0, 4), ('K2MnO4', 'Mn', 1, [(1, 2), (-2, 4)], 0, 6),
    ('K2Cr2O7', 'Cr', 2, [(1, 2), (-2, 7)], 0, 6), ('Cr2O3', 'Cr', 2, [(-2, 3)], 0, 3), ('CrCl3', 'Cr', 1, [(-1, 3)], 0, 3),
    ('Fe2O3', 'Fe', 2, [(-2, 3)], 0, 3), ('FeO', 'Fe', 1, [(-2, 1)], 0, 2), ('FeCl3', 'Fe', 1, [(-1, 3)], 0, 3),
    ('CO2', 'C', 1, [(-2, 2)], 0, 4), ('CO', 'C', 1, [(-2, 1)], 0, 2), ('CH4', 'C', 1, [(1, 4)], 0, -4), ('CaCO3', 'C', 1, [(2, 1), (-2, 3)], 0, 4),
    ('H3PO4', 'P', 1, [(1, 3), (-2, 4)], 0, 5), ('PH3', 'P', 1, [(1, 3)], 0, -3), ('P2O5', 'P', 2, [(-2, 5)], 0, 5),
]
def c4():
    b = Bank('hoa10', 'c4')
    for (f, x, nx, others, ch, ans) in OXN:
        val = (ch - sum(o * k for o, k in others)) / nx
        assert val == ans, (f, val)
        pool = [str(v) for v in (ans + 1, ans - 1, ans + 2, ans - 2, -ans, 2 * ans if ans else 3)]
        def sg(v): return ('+' if v > 0 else ('−' if v < 0 else '')) + str(abs(v))
        pool = [sg(int(p)) for p in pool]
        known = " + ".join(f"({'+' if o > 0 else ''}{o})\\times{k}" for o, k in others)
        b.mc('b7', 'th', 'Số oxi hoá', f"Số oxi hoá của nguyên tố {x} trong hợp chất ${F(f)}$ là:", sg(ans), pick(sg(ans), pool), f"Tổng số oxi hoá trong hợp chất bằng 0: ${'' if nx == 1 else str(nx) + chr(92) + 'cdot '}x + {known} = 0\\Rightarrow x={'+' if ans > 0 else ''}{ans}$.")
        sa(b, 'b7', 'th', 'Số oxi hoá', f"Xác định số oxi hoá của nguyên tố {x} trong ${F(f)}$ (nhập số, kể cả dấu).", ans, f"Tổng số oxi hoá bằng 0: ${'' if nx == 1 else nx}x + {known} = 0\\Rightarrow x={ans}$.")
    ions = [('NH4', '+', 'N', 1, [(1, 4)], 1, -3), ('NO3', '-', 'N', 1, [(-2, 3)], -1, 5), ('SO4', '2-', 'S', 1, [(-2, 4)], -2, 6), ('MnO4', '-', 'Mn', 1, [(-2, 4)], -1, 7), ('Cr2O7', '2-', 'Cr', 2, [(-2, 7)], -2, 6), ('ClO3', '-', 'Cl', 1, [(-2, 3)], -1, 5), ('PO4', '3-', 'P', 1, [(-2, 4)], -3, 5), ('CO3', '2-', 'C', 1, [(-2, 3)], -2, 4)]
    for (f, c, x, nx, others, ch, ans) in ions:
        val = (ch - sum(o * k for o, k in others)) / nx
        assert val == ans, f
        def sg(v): return ('+' if v > 0 else ('−' if v < 0 else '')) + str(abs(v))
        pool = [sg(v) for v in (ans + 1, ans - 1, ans + 2, ans - 2, -ans)]
        known = " + ".join(f"({o})\\times{k}" for o, k in others)
        b.mc('b7', 'vd', 'Số oxi hoá trong ion', f"Số oxi hoá của nguyên tố {x} trong ion ${Fi(f, c)}$ là:", sg(ans), pick(sg(ans), pool), f"Tổng số oxi hoá bằng điện tích của ion: ${nx}x + {known} = {ch}\\Rightarrow x={'+' if ans>0 else ''}{ans}$.")
    # phản ứng oxi hoá - khử
    RX = [
        ([(2, 'Na'), (1, 'Cl2')], [(2, 'NaCl')], 'Na', 'Cl2', 2), ([(1, 'Zn'), (2, 'HCl')], [(1, 'ZnCl2'), (1, 'H2')], 'Zn', 'HCl', 2),
        ([(1, 'Fe'), (1, 'CuSO4')], [(1, 'FeSO4'), (1, 'Cu')], 'Fe', 'CuSO4', 2), ([(2, 'Mg'), (1, 'O2')], [(2, 'MgO')], 'Mg', 'O2', 4),
        ([(1, 'Cu'), (2, 'AgNO3')], [(1, 'Cu(NO3)2'), (2, 'Ag')], 'Cu', 'AgNO3', 2), ([(2, 'Al'), (3, 'Cl2')], [(2, 'AlCl3')], 'Al', 'Cl2', 6),
        ([(1, 'H2'), (1, 'CuO')], [(1, 'Cu'), (1, 'H2O')], 'H2', 'CuO', 2), ([(1, 'C'), (1, 'O2')], [(1, 'CO2')], 'C', 'O2', 4),
        ([(1, 'Fe2O3'), (3, 'CO')], [(2, 'Fe'), (3, 'CO2')], 'CO', 'Fe2O3', 6), ([(1, 'Cl2'), (2, 'NaBr')], [(2, 'NaCl'), (1, 'Br2')], 'NaBr', 'Cl2', 2),
        ([(2, 'FeCl2'), (1, 'Cl2')], [(2, 'FeCl3')], 'FeCl2', 'Cl2', 2),
    ]
    for (L, R, red, oxd, ne) in RX:
        assert side(L) == side([(k, f) for k, f in R]), eq_str(L, R)
        eq = eq_str(L, R)
        reag = [f for _, f in L]
        pool = reag + [f for _, f in R]
        oxd_ans, red_ans = F(oxd), F(red)
        species = list(dict.fromkeys([f for _, f in L] + [f for _, f in R]))
        def mkopts(ok):
            pool = [f"${F(x)}$" for x in species if x != ok] + ["Cả hai chất tham gia đều là chất khử", "Cả hai chất tham gia đều là chất oxi hoá", "Không có chất nào thay đổi số oxi hoá"]
            if ok == red: pool = [p for p in pool if 'oxi hoá' not in p or 'Không' in p] + pool
            return pick(f"${F(ok)}$", pool)
        b.mc('b8', 'th', 'Chất khử', f"Trong phản ứng ${eq}$, chất khử là:", f"${red_ans}$", mkopts(red), f"Chất khử là chất nhường electron (số oxi hoá tăng). Trong phản ứng này ${red_ans}$ bị oxi hoá nên là chất khử.")
        b.mc('b8', 'th', 'Chất oxi hoá', f"Trong phản ứng ${eq}$, chất oxi hoá là:", f"${oxd_ans}$", mkopts(oxd), f"Chất oxi hoá là chất nhận electron (số oxi hoá giảm). Trong phản ứng này ${oxd_ans}$ bị khử nên là chất oxi hoá.")
        nm(b, 'b8', 'vd', 'Số electron trao đổi', f"Với phản ứng ${eq}$ (đã cân bằng), tổng số electron mà chất khử nhường là:", ne, [ne + 1, max(1, ne - 1), ne * 2, ne // 2 if ne // 2 not in (0, ne) else ne + 3], '', f"Xác định sự thay đổi số oxi hoá theo hệ số đã cân bằng: chất khử nhường tổng cộng ${ne}$ electron, bằng số electron chất oxi hoá nhận.", nd=0)
    nonredox = [([(1, 'NaOH'), (1, 'HCl')], [(1, 'NaCl'), (1, 'H2O')]), ([(1, 'CaCO3')], [(1, 'CaO'), (1, 'CO2')]), ([(1, 'BaCl2'), (1, 'H2SO4')], [(1, 'BaSO4'), (2, 'HCl')]), ([(1, 'CuO'), (2, 'HCl')], [(1, 'CuCl2'), (1, 'H2O')]), ([(1, 'CaO'), (1, 'H2O')], [(1, 'Ca(OH)2')]), ([(1, 'Na2CO3'), (2, 'HCl')], [(2, 'NaCl'), (1, 'H2O'), (1, 'CO2')])]
    for (L, R) in nonredox: assert side(L) == side(R), eq_str(L, R)
    for i in range(0, len(RX), 2):
        red_r = RX[i]; others = [nonredox[(i + j) % len(nonredox)] for j in range(3)]
        b.mc('b7', 'th', 'Nhận biết phản ứng oxi hoá - khử', "Phản ứng nào sau đây là phản ứng oxi hoá - khử?", f"${eq_str(red_r[0], red_r[1])}$", [f"${eq_str(l, r)}$" for l, r in others], f"Phản ứng ${eq_str(red_r[0], red_r[1])}$ có sự thay đổi số oxi hoá của các nguyên tố nên là phản ứng oxi hoá - khử; ba phản ứng còn lại không có nguyên tố nào thay đổi số oxi hoá (phản ứng trao đổi / phân huỷ không đổi số oxi hoá).")
    # cân bằng
    BAL = [
        ([(4, 'Al'), (3, 'O2')], [(2, 'Al2O3')]), ([(2, 'Fe'), (3, 'Cl2')], [(2, 'FeCl3')]), ([(3, 'Cu'), (8, 'HNO3')], [(3, 'Cu(NO3)2'), (2, 'NO'), (4, 'H2O')]),
        ([(1, 'Cu'), (2, 'H2SO4')], [(1, 'CuSO4'), (1, 'SO2'), (2, 'H2O')]), ([(2, 'KMnO4'), (16, 'HCl')], [(2, 'KCl'), (2, 'MnCl2'), (5, 'Cl2'), (8, 'H2O')]),
        ([(2, 'Fe'), (6, 'H2SO4')], [(1, 'Fe2(SO4)3'), (3, 'SO2'), (6, 'H2O')]), ([(10, 'FeSO4'), (2, 'KMnO4'), (8, 'H2SO4')], [(5, 'Fe2(SO4)3'), (2, 'MnSO4'), (1, 'K2SO4'), (8, 'H2O')]),
        ([(1, 'C'), (4, 'HNO3')], [(1, 'CO2'), (4, 'NO2'), (2, 'H2O')]), ([(2, 'Al'), (6, 'HCl')], [(2, 'AlCl3'), (3, 'H2')]), ([(2, 'Na'), (2, 'H2O')], [(2, 'NaOH'), (1, 'H2')]),
    ]
    for (L, R) in BAL:
        assert side(L) == side(R), eq_str(L, R)
        unb = " + ".join(F(f) for _, f in L) + " \\rightarrow " + " + ".join(F(f) for _, f in R)
        tot = sum(k for k, _ in L) + sum(k for k, _ in R)
        nm(b, 'b8', 'vd', 'Tổng hệ số cân bằng', f"Cân bằng phản ứng oxi hoá - khử (hệ số là các số nguyên tối giản): ${unb}$. Tổng các hệ số của phương trình đã cân bằng là:", tot, [tot + 1, tot - 1, tot + 2, tot - 2], '', f"Phương trình đã cân bằng: ${eq_str(L, R)}$. Tổng hệ số $=" + "+".join(str(k) for k, _ in L + R) + f"={tot}$.", nd=0)
        k0, f0 = L[1] if len(L) > 1 else L[0]
        pool = [k0 + 1, k0 + 2, max(1, k0 - 1), k0 * 2]
        nm(b, 'b8', 'vd', 'Hệ số chất tham gia', f"Cân bằng phản ứng ${unb}$. Hệ số của ${F(f0)}$ trong phương trình đã cân bằng (hệ số nguyên tối giản) là:", k0, pool, '', f"Phương trình đã cân bằng: ${eq_str(L, R)}$. Hệ số của ${F(f0)}$ là ${k0}$.", nd=0)
        sa(b, 'b8', 'vd', 'Tổng hệ số cân bằng', f"Cân bằng phản ứng ${unb}$ với hệ số nguyên tối giản. Tính tổng các hệ số.", tot, f"Phương trình: ${eq_str(L, R)}$; tổng hệ số là ${'+'.join(str(k) for k, _ in L+R)}={tot}$.")
    # tính toán 
    V = 24.79
    for (el, M_, m, n_e, name) in (('Mg', 24, 2.4, 2, 'Mg'), ('Fe', 56, 5.6, 2, 'Fe'), ('Zn', 65, 6.5, 2, 'Zn'), ('Al', 27, 2.7, 3, 'Al'), ('Mg', 24, 4.8, 2, 'Mg'), ('Al', 27, 5.4, 3, 'Al')):
        n = m / M_; nh2 = n * n_e / 2; v = round(nh2 * V, 2)
        nm(b, 'b8', 'vd', 'Thể tích khí H2', f"Cho {fnum(m)} g {name} tác dụng hết với dung dịch HCl dư. Thể tích khí $\\mathrm{{H_{{2}}}}$ thu được ở điều kiện chuẩn (25 °C, 1 bar; 1 mol khí chiếm 24,79 L) là: (làm tròn đến hai chữ số thập phân)", v, [round(n * V, 2), round(nh2 * 22.4, 2), round(nh2 * V * 2, 2), round(n * n_e * V, 2)], 'L', f"$n_{{{name}}}={fnum(m)}:{M_}={fnum(n,3)}$ mol. Mỗi mol {name} nhường {n_e} mol electron, mỗi mol $\\mathrm{{H_{{2}}}}$ nhận 2 mol electron nên $n_{{H_2}}={fnum(nh2,4)}$ mol; $V={fnum(nh2,4)}\\times24{{,}}79={fnum(v)}$ L.")
        sa(b, 'b8', 'vd', 'Số mol electron', f"{fnum(m)} g {name} nhường bao nhiêu mol electron khi bị oxi hoá hoàn toàn thành ion kim loại? (làm tròn đến hai chữ số thập phân)", round(n * n_e, 2), f"$n_{{{name}}}={fnum(m)}:{M_}={fnum(n,3)}$ mol; số mol electron nhường $={fnum(n,3)}\\times{n_e}={fnum(n*n_e,3)}$ mol.")
    for (st, ok, ws, ex) in (
        ("Chất khử là chất:", "Nhường electron (số oxi hoá tăng)", ["Nhận electron (số oxi hoá tăng)", "Nhường electron (số oxi hoá giảm)", "Nhận electron (số oxi hoá giảm)"], "Chất khử nhường electron nên số oxi hoá của nó tăng; quá trình đó gọi là sự oxi hoá."),
        ("Chất oxi hoá là chất:", "Nhận electron (số oxi hoá giảm)", ["Nhường electron (số oxi hoá giảm)", "Nhận electron (số oxi hoá tăng)", "Nhường electron (số oxi hoá tăng)"], "Chất oxi hoá nhận electron nên số oxi hoá giảm; quá trình đó gọi là sự khử."),
        ("Số oxi hoá của đơn chất (như $\\mathrm{O_{2}}$, $\\mathrm{Fe}$, $\\mathrm{Cl_{2}}$) bằng:", "0", ["+1", "−1", "Bằng số electron lớp ngoài cùng"], "Trong đơn chất, nguyên tử không chênh lệch độ âm điện nên số oxi hoá bằng 0."),
        ("Quá trình $\\mathrm{Fe}\\rightarrow\\mathrm{Fe}^{3+}+3e$ là:", "Sự oxi hoá", ["Sự khử", "Sự trung hoà", "Sự thuỷ phân"], "Fe nhường electron, số oxi hoá tăng từ 0 lên +3 nên là sự oxi hoá."),
        ("Quá trình $\\mathrm{Cu}^{2+}+2e\\rightarrow\\mathrm{Cu}$ là:", "Sự khử", ["Sự oxi hoá", "Sự trung hoà", "Sự thuỷ phân"], "$\\mathrm{Cu}^{2+}$ nhận electron, số oxi hoá giảm từ +2 xuống 0 nên là sự khử.")):
        b.mc('b7', 'nb', 'Lý thuyết', st, ok, ws, ex)
    return b

# ======================== CHƯƠNG 5 ========================
def c5():
    b = Bank('hoa10', 'c5')
    for dh in (-92, -285.8, -890.3, +178.3, +92.2, -393.5, +571.6, -46):
        kind = 'toả nhiệt' if dh < 0 else 'thu nhiệt'
        other = 'thu nhiệt' if dh < 0 else 'toả nhiệt'
        sg = ('−' if dh < 0 else '+') + fnum(abs(dh), 1)
        b.mc('b9', 'nb', 'Phản ứng toả/thu nhiệt', f"Một phản ứng có $\\Delta_rH^0_{{298}}={sg}$ kJ. Phản ứng này là phản ứng:", kind, [other, 'không có sự trao đổi nhiệt', 'chỉ xảy ra ở nhiệt độ cao'], "Phản ứng có $\\Delta_rH<0$ là phản ứng toả nhiệt; $\\Delta_rH>0$ là phản ứng thu nhiệt. Ở đây " + f"$\\Delta_rH={sg}$ kJ nên là phản ứng {kind}.")
    # Q = n × |ΔH|
    CASES = [('C(s) + O2(g) -> CO2(g)', 'C', 12, -393.5, [6, 12, 24, 3]), ('CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)', 'CH4', 16, -890.3, [8, 16, 32, 4]), ('H2(g) + 1/2 O2(g) -> H2O(l)', 'H2', 2, -285.8, [1, 2, 4, 6]), ('CaCO3(s) -> CaO(s) + CO2(g)', 'CaCO3', 100, +178.3, [50, 100, 200, 25])]
    for (rx, sub, M_, dh, ms) in CASES:
        rxl = rx.replace(' -> ', ' \\rightarrow ')
        rxl = re.sub(r'([A-Za-z][A-Za-z0-9]*)\((s|g|l)\)', lambda m: F(m.group(1)) + f"({m.group(2)})", rxl)
        for m in ms:
            n = m / M_; Q = round(abs(dh) * n, 2)
            what = 'toả ra' if dh < 0 else 'thu vào'
            sg = ('−' if dh < 0 else '+') + fnum(abs(dh), 1)
            nm(b, 'b10', 'vd', 'Nhiệt lượng theo khối lượng chất', f"Cho phản ứng ${rxl}$, $\\Delta_rH^0_{{298}}={sg}$ kJ (tính theo 1 mol ${F(sub)}$). Nhiệt lượng {what} khi phản ứng hoàn toàn {fnum(m)} g ${F(sub)}$ (M = {M_} g/mol) là:", Q, [abs(dh), round(abs(dh) * m, 2), round(abs(dh) / n, 2), round(abs(dh) * n * 2, 2)], 'kJ', f"$n_{{{sub}}}={fnum(m)}:{M_}={fnum(n,3)}$ mol. Nhiệt lượng {what} $=n\\times|\\Delta_rH|={fnum(n,3)}\\times{fnum(abs(dh),1)}={fnum(Q)}$ kJ.")
            if abs(Q - round(Q, 2)) < 1e-9:
                sa(b, 'b10', 'vd', 'Nhiệt lượng theo khối lượng chất', f"Phản ứng ${rxl}$ có $\\Delta_rH^0_{{298}}={sg}$ kJ (tính theo 1 mol ${F(sub)}$, M = {M_} g/mol). Tính nhiệt lượng {what} khi phản ứng hết {fnum(m)} g ${F(sub)}$ (kJ, làm tròn đến hai chữ số thập phân).", Q, f"$n={fnum(m)}:{M_}={fnum(n,3)}$ mol; $Q=n\\times|\\Delta_rH|={fnum(n,3)}\\times{fnum(abs(dh),1)}={fnum(Q)}$ kJ.", 'kJ')
    # từ nhiệt tạo thành
    DF = {'CO2(g)': -393.5, 'H2O(l)': -285.8, 'H2O(g)': -241.8, 'CH4(g)': -74.6, 'CaO(s)': -635.1, 'CaCO3(s)': -1206.9, 'Fe2O3(s)': -824.2, 'CO(g)': -110.5, 'NH3(g)': -45.9, 'NO(g)': 90.3, 'Al2O3(s)': -1675.7, 'Fe(s)': 0, 'O2(g)': 0, 'Al(s)': 0}
    R = [
        ([(1, 'CaCO3(s)')], [(1, 'CaO(s)'), (1, 'CO2(g)')]),
        ([(1, 'CH4(g)'), (2, 'O2(g)')], [(1, 'CO2(g)'), (2, 'H2O(l)')]),
        ([(1, 'Fe2O3(s)'), (3, 'CO(g)')], [(2, 'Fe(s)'), (3, 'CO2(g)')]),
        ([(2, 'Al(s)'), (1, 'Fe2O3(s)')], [(1, 'Al2O3(s)'), (2, 'Fe(s)')]),
        ([(4, 'NH3(g)'), (5, 'O2(g)')], [(4, 'NO(g)'), (6, 'H2O(g)')]),
    ]
    def st(f): return re.sub(r'\((s|g|l)\)', '', f)
    for (L, Rt) in R:
        assert side([(k, st(f)) for k, f in L]) == side([(k, st(f)) for k, f in Rt]), L
        dh = round(sum(k * DF[f] for k, f in Rt) - sum(k * DF[f] for k, f in L), 1)
        wrong1 = -dh
        wrong2 = round(sum(DF[f] for k, f in Rt) - sum(DF[f] for k, f in L), 1)
        wrong3 = round(sum(k * DF[f] for k, f in L) - sum(k * DF[f] for k, f in Rt), 1)
        eq = " + ".join((str(k) if k > 1 else '') + F(st(f)) + f"({f[-2]})" for k, f in L) + " \\rightarrow " + " + ".join((str(k) if k > 1 else '') + F(st(f)) + f"({f[-2]})" for k, f in Rt)
        table = "; ".join(f"$\\Delta_fH^0_{{298}}({F(st(f))})={fnum(DF[f],1)}$" for f in dict.fromkeys(f for k, f in L + Rt) if DF[f] != 0)
        calc = f"$\\Delta_rH=" + "+".join(f"{k}\\times({fnum(DF[f],1)})" for k, f in Rt) + "-(" + "+".join(f"{k}\\times({fnum(DF[f],1)})" for k, f in L) + f")={fnum(dh,1)}$ kJ"
        nm(b, 'b10', 'vd', 'Tính ΔrH từ nhiệt tạo thành', f"Cho phản ứng ${eq}$. Biết (kJ/mol): {table}; nhiệt tạo thành chuẩn của đơn chất bền bằng 0. $\\Delta_rH^0_{{298}}$ của phản ứng (kJ) là:", dh, [wrong1, wrong2, wrong3, dh + 100], 'kJ', f"$\\Delta_rH^0_{{298}}=\\sum\\Delta_fH^0(\\text{{sản phẩm}})-\\sum\\Delta_fH^0(\\text{{chất đầu}})$ (nhân hệ số). {calc}.", nd=1)
        sa(b, 'b10', 'vd', 'Tính ΔrH từ nhiệt tạo thành', f"Cho phản ứng ${eq}$. Biết (kJ/mol): {table}. Tính $\\Delta_rH^0_{{298}}$ (kJ).", dh, f"$\\Delta_rH=\\sum\\Delta_fH(\\text{{sản phẩm}})-\\sum\\Delta_fH(\\text{{chất đầu}})$. {calc}.", 'kJ')
    # từ năng lượng liên kết
    EB = [
        ('H2 + Cl2 -> 2HCl', "H–H: 436, Cl–Cl: 243, H–Cl: 431", 436 + 243 - 2 * 431, "436 + 243 - 2×431"),
        ('N2 + 3H2 -> 2NH3', "N≡N: 945, H–H: 436, N–H: 391", 945 + 3 * 436 - 6 * 391, "945 + 3×436 - 6×391"),
        ('H2 + F2 -> 2HF', "H–H: 436, F–F: 159, H–F: 565", 436 + 159 - 2 * 565, "436 + 159 - 2×565"),
        ('H2 + Br2 -> 2HBr', "H–H: 436, Br–Br: 193, H–Br: 366", 436 + 193 - 2 * 366, "436 + 193 - 2×366"),
        ('2H2 + O2 -> 2H2O', "H–H: 436, O=O: 498, O–H: 464", 2 * 436 + 498 - 4 * 464, "2×436 + 498 - 4×464"),
        ('CH4 + Cl2 -> CH3Cl + HCl', "C–H: 414, Cl–Cl: 243, C–Cl: 339, H–Cl: 431", 414 + 243 - 339 - 431, "(414 + 243) - (339 + 431)"),
    ]
    for (rx, eb, dh, calc) in EB:
        def side_tex(t):
            out = []
            for term in t.split(' + '):
                m = re.match(r'(\d*)(.+)', term)
                out.append(m.group(1) + F(m.group(2)))
            return " + ".join(out)
        l_, r_ = rx.split(' -> ')
        rxl = side_tex(l_) + " \\rightarrow " + side_tex(r_)
        nm(b, 'b10', 'vd', 'Tính ΔrH từ năng lượng liên kết', f"Cho phản ứng ${rxl}$ (các chất ở thể khí). Năng lượng liên kết (kJ/mol): {eb}. $\\Delta_rH^0_{{298}}$ của phản ứng (kJ) là:", dh, [-dh, dh + 100, dh - 100, abs(dh) + 50], 'kJ', f"$\\Delta_rH=\\sum E_b(\\text{{chất đầu}})-\\sum E_b(\\text{{sản phẩm}})={calc}={dh}$ kJ.", nd=0)
        sa(b, 'b10', 'vd', 'Tính ΔrH từ năng lượng liên kết', f"Cho phản ứng ${rxl}$ (chất khí). Năng lượng liên kết (kJ/mol): {eb}. Tính $\\Delta_rH^0_{{298}}$ (kJ).", dh, f"$\\Delta_rH=\\sum E_b(\\text{{chất đầu}})-\\sum E_b(\\text{{sản phẩm}})={calc}={dh}$ kJ.", 'kJ')
    # Q = mcΔT
    for (m, dT) in ((200, 10), (100, 20), (500, 5), (250, 8)):
        Q = m * 4.18 * dT / 1000
        nm(b, 'b9', 'vd', 'Nhiệt lượng làm nóng nước', f"Nhiệt lượng cần để làm {m} g nước tăng thêm {dT} °C là bao nhiêu kJ? (biết nhiệt dung riêng của nước là 4,18 J/(g·K))", Q, [m * 4.18 * dT, m * dT / 1000, Q * 2, Q / 2], 'kJ', f"$Q=mc\\Delta T={m}\\times4{{,}}18\\times{dT}={fnum(m*4.18*dT)}$ J $={fnum(Q)}$ kJ.")
    for (st_, ok, ws, ex) in (
        ("Điều kiện chuẩn để xác định biến thiên enthalpy là:", "Áp suất 1 bar, nhiệt độ 25 °C (298 K)", ["Áp suất 1 atm, nhiệt độ 0 °C", "Áp suất 2 bar, nhiệt độ 25 °C", "Áp suất 1 bar, nhiệt độ 100 °C"], "Điều kiện chuẩn: áp suất 1 bar (chất khí), nồng độ 1 mol/L (dung dịch), nhiệt độ thường chọn là 25 °C (298 K)."),
        ("Phản ứng toả nhiệt có:", "$\\Delta_rH<0$", ["$\\Delta_rH>0$", "$\\Delta_rH=0$", "Không xác định được dấu của $\\Delta_rH$"], "Phản ứng toả nhiệt giải phóng nhiệt ra môi trường nên enthalpy của hệ giảm: $\\Delta_rH<0$."),
        ("Phản ứng thu nhiệt có:", "$\\Delta_rH>0$", ["$\\Delta_rH<0$", "$\\Delta_rH=0$", "Luôn xảy ra tự phát"], "Phản ứng thu nhiệt hấp thụ nhiệt từ môi trường nên $\\Delta_rH>0$."),
        ("Phản ứng nào sau đây thường là phản ứng toả nhiệt?", "Đốt cháy than, khí gas", ["Nung đá vôi $\\mathrm{CaCO_{3}}$", "Hoà tan muối ăn khiến nước lạnh đi", "Quang hợp của cây xanh"], "Các phản ứng đốt cháy nhiên liệu đều toả nhiệt; nung đá vôi, quang hợp là các quá trình thu nhiệt."),
        ("Nhiệt tạo thành chuẩn của đơn chất bền (như $\\mathrm{O_{2}}$, $\\mathrm{Fe}$) bằng:", "0", ["+100 kJ/mol", "−100 kJ/mol", "Bằng năng lượng liên kết"], "Theo quy ước, nhiệt tạo thành chuẩn của đơn chất bền ở điều kiện chuẩn bằng 0."),
        ("Đơn vị thường dùng của biến thiên enthalpy phản ứng là:", "kJ hoặc kJ/mol", ["kg", "mol/L", "Pa"], "Biến thiên enthalpy của phản ứng được biểu diễn bằng kJ (hoặc kJ/mol)."),
        ("Phản ứng có $\\Delta_rH^0_{298}=-393{,}5$ kJ cho biết khi 1 mol C cháy hoàn toàn thành $\\mathrm{CO_{2}}$:", "Toả ra 393,5 kJ nhiệt", ["Thu vào 393,5 kJ nhiệt", "Toả ra 39,35 kJ nhiệt", "Không có sự trao đổi nhiệt"], "$\\Delta_rH<0$ nên phản ứng toả nhiệt; giá trị tuyệt đối cho biết lượng nhiệt toả ra là 393,5 kJ.")):
        b.mc('b9', 'nb', 'Lý thuyết', st_, ok, ws, ex)
    return b
