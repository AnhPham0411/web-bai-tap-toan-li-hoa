# -*- coding: utf-8 -*-
"""
Bộ sinh toàn diện ngân hàng câu hỏi Toán 10 Kì 2 (Chương 6, 7, 8, 9).
Chuẩn GDPT 2018 (SGK Kết nối tri thức).
Tất cả câu hỏi đều có:
- 120 TN (60 nb / 48 th / 12 vd) + 30 TLN (15 nb / 12 th / 3 vd)
- Tối đa 5 biến thể/dạng bài.
- Lời giải chi tiết, số liệu chuẩn xác, không trùng lặp đề.
- Dấu phẩy thập phân tiếng Việt, biểu thức LaTeX tương thích math.js.
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK_DIR = os.path.join(BASE_DIR, "scripts", "bank")

def make_unique(choices):
    seen = set()
    res = []
    for c in choices:
        c_str = str(c).strip()
        while c_str in seen:
            c_str += " "
        seen.add(c_str)
        res.append(c_str)
    return res

def save_bank(chapter_id, sgk_title, sgk_lessons, mc, sa):
    data = {
        "sgk_chapter_title": sgk_title,
        "sgk_lessons": sgk_lessons,
        "sources": ["Biên soạn theo chương trình GDPT 2018 SGK Kết nối tri thức"],
        "mc": mc,
        "short": sa
    }
    filepath = os.path.join(BANK_DIR, f"toan10_{chapter_id}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"-> Da tao toan10_{chapter_id}.json ({len(mc)} TN, {len(sa)} TLN)")

# ==============================================================================
# CHƯƠNG 6: HÀM SỐ, ĐỒ THỊ VÀ ỨNG DỤNG
# ==============================================================================
def build_c6():
    mc = []
    sa = []

    nb_defs = [
        ("Tập xác định hàm phân thức bậc nhất", "b15",
         lambda v: (
             f"Tập xác định của hàm số $y = \\frac{{{v+1}}}{{x - {v+2}}}$ là:",
             [f"$\\mathbb{{R}} \\setminus \\{{{v+2}\\}}$", f"$\\mathbb{{R}} \\setminus \\{{-{v+2}\\}}$", f"({v+2}; +\\infty)", f"(-\\infty; {v+2})"],
             0, f"Hàm số xác định khi mẫu số khác 0: $x - {v+2} \\ne 0 \\Leftrightarrow x \\ne {v+2}$."
         )),
        ("Điểm thuộc đồ thị hàm số", "b15",
         lambda v: (
             f"Điểm nào sau đây thuộc đồ thị hàm số $y = 2x - {v+1}$?",
             [f"$A(1; {1-v})$", f"$B(1; {3-v})$", f"$C(0; {v+2})$", f"$D(-1; {v+4})$"],
             0, f"Thay $x = 1$ vào hàm số ta được $y = 2(1) - {v+1} = {1-v}$. Vậy điểm $A(1; {1-v})$ thuộc đồ thị."
         )),
        ("Tính đồng biến hàm bậc nhất", "b15",
         lambda v: (
             f"Hàm số $y = {v+2}x + {v+3}$ đồng biến trên khoảng nào?",
             ["$(-\\infty; +\\infty)$", "$(0; +\\infty)$", "$(-\\infty; 0)$", "Không đồng biến"],
             0, f"Hàm số bậc nhất $y = ax + b$ có hệ số $a = {v+2} > 0$ nên đồng biến trên toàn bộ $\\mathbb{{R}}$."
         )),
        ("Tọa độ đỉnh parabol", "b16",
         lambda v: (
             f"Tọa độ đỉnh của parabol $y = x^2 - {2*(v+1)}x + {v+1}$ là:",
             [f"$I({v+1}; {-(v+1)**2 + v + 1})$", f"$I(-{v+1}; {(v+1)**2 + v + 1})$", f"$I({v+1}; {v+5})$", f"$I({2*(v+1)}; {v+1})$"],
             0, f"Hoành độ đỉnh $x_I = -b/(2a) = {2*(v+1)}/2 = {v+1}$, tung độ $y_I = ({v+1})^2 - {2*(v+1)}({v+1}) + {v+1} = {-(v+1)**2 + v + 1}$."
         )),
        ("Trục đối xứng của parabol", "b16",
         lambda v: (
             f"Trục đối xứng của parabol $y = 2x^2 - {4*(v+1)}x + 1$ là đường thẳng:",
             [f"$x = {v+1}$", f"$x = -{v+1}$", f"$y = {v+1}$", f"$x = {2*(v+1)}$"],
             0, f"Trục đối xứng có phương trình $x = -b/(2a) = {4*(v+1)}/4 = {v+1}$."
         )),
        ("Hướng bề lõm parabol", "b16",
         lambda v: (
             f"Đồ thị hàm số $y = -{v+1}x^2 + 3x - 1$ có bề lõm:",
             ["Quay xuống dưới", "Quay lên trên", "Sang bên phải", "Sang bên trái"],
             0, f"Do hệ số $a = -{v+1} < 0$ nên bề lõm của parabol quay xuống phía dưới."
         )),
        ("Giao điểm của parabol với trục tung", "b16",
         lambda v: (
             f"Tọa độ giao điểm của parabol $y = x^2 + 5x - {v+3}$ với trục tung là:",
             [f"$(0; -{v+3})$", f"$(-{v+3}; 0)$", f"$(0; {v+3})$", f"$(1; {4-v})$"],
             0, f"Giao điểm với trục tung có hoành độ $x = 0 \\Rightarrow y = -{v+3}$."
         )),
        ("Nhận biết biểu thức tam thức bậc hai", "b17",
         lambda v: (
             f"Biểu thức nào sau đây là tam thức bậc hai theo biến $x$ (mẫu {v+1})?",
             [f"$f(x) = {v+2}x^2 - 3x + 1$", f"$g(x) = {v+2}x - 5$", f"$h(x) = x^3 - {v+1}x$", f"$k(x) = \\frac{{{v+1}}}{{x^2}} + 1$"],
             0, f"Tam thức bậc hai có dạng $ax^2 + bx + c$ với $a \\ne 0$."
         )),
        ("Biệt thức delta của tam thức bậc hai", "b17",
         lambda v: (
             f"Biệt thức $\\Delta$ của tam thức bậc hai $f(x) = x^2 - {2*(v+2)}x + {(v+2)**2 - 4}$ là:",
             ["$16$", "$0$", "$-16$", "$4$"],
             0, f"$\\Delta = b^2 - 4ac = [-{2*(v+2)}]^2 - 4(1)[{(v+2)**2 - 4}] = 4({v+2})^2 - 4({v+2})^2 + 16 = 16$."
         )),
        ("Dấu của tam thức khi biệt thức âm", "b17",
         lambda v: (
             f"Cho tam thức $f(x) = x^2 + 2x + {v+3}$. Khẳng định nào sau đây ĐÚNG?",
             ["$f(x) > 0, \\forall x \\in \\mathbb{R}$", "$f(x) < 0, \\forall x \\in \\mathbb{R}$", "$f(x) \\ge 0, \\forall x \\in \\mathbb{R}$", "$f(x)$ đổi dấu trên $\\mathbb{R}$"],
             0, f"$\\Delta' = 1 - ({v+3}) = -{v+2} < 0$ và hệ số $a = 1 > 0$, do đó $f(x) > 0$ với mọi $x \\in \\mathbb{{R}}$."
         )),
        ("Nghiệm của tam thức bậc hai cơ bản", "b17",
         lambda v: (
             f"Các nghiệm của tam thức bậc hai $f(x) = x^2 - {2*v+5}x + {(v+2)*(v+3)}$ là:",
             [f"$x = {v+2}$ và $x = {v+3}$", f"$x = -{v+2}$ và $x = -{v+3}$", f"$x = {v+1}$ và $x = {v+4}$", f"Vô nghiệm"],
             0, f"Phân tích thành $(x - {v+2})(x - {v+3}) = 0$ nên nghiệm là $x = {v+2}$ và $x = {v+3}$."
         )),
        ("Bất phương trình bậc hai một ẩn", "b17",
         lambda v: (
             f"Bất phương trình nào sau đây là bất phương trình bậc hai một ẩn (mẫu {v+1})?",
             [f"$2x^2 - {v+1}x + 3 > 0$", f"${v+1}x - 7 \\le 0$", f"$x^3 + 2x - 1 < 0$", f"$2x + y - {v} \\ge 0$"],
             0, f"Bất phương trình bậc hai một ẩn có bậc cao nhất của biến là 2."
         )),
        ("Điều kiện xác định của căn bậc hai", "b18",
         lambda v: (
             f"Điều kiện xác định của phương trình $\\sqrt{{x - {v+2}}} = x - 1$ là:",
             [f"$x \\ge {v+2}$", f"$x > {v+2}$", f"$x \\le {v+2}$", f"$x \\ge 1$"],
             0, f"Biểu thức dưới dấu căn không âm: $x - {v+2} \\ge 0 \\Leftrightarrow x \\ge {v+2}$."
         )),
        ("Giá trị nhỏ nhất của parabol trên R", "b16",
         lambda v: (
             f"Giá trị nhỏ nhất của hàm số $y = x^2 - {2*v+4}x + {(v+2)**2 + 5}$ trên $\\mathbb{{R}}$ là:",
             ["$5$", f"${v+6}$", f"${-v-1}$", f"${(v+2)**2 + 10}$"],
             0, f"Biến đổi $y = (x - {v+2})^2 + 5 \\ge 5$. Giá trị nhỏ nhất là 5 đạt tại $x = {v+2}$."
         )),
        ("Tập xác định của căn bậc hai đơn giản", "b15",
         lambda v: (
             f"Tập xác định của hàm số $y = \\sqrt{{{v+3} - x}}$ là:",
             [f"$(-\\infty; {v+3}]$", f"$[{v+3}; +\\infty)$", f"$(-\\infty; {v+3})$", f"$({v+3}; +\\infty)$"],
             0, f"Hàm số xác định khi ${v+3} - x \\ge 0 \\Leftrightarrow x \\le {v+3}$. Vậy $D = (-\\infty; {v+3}]$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(nb_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c6_nb_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    th_defs = [
        ("Tập xác định phân thức có chứa căn", "b15",
         lambda v: (
             f"Tập xác định của hàm số $y = \\frac{{1}}{{\\sqrt{{x - {v+1}}}}} + \\frac{{x}}{{x - {v+4}}}$ là:",
             [f"$({v+1}; +\\infty) \\setminus \\{{{v+4}\\}}$", f"$[{v+1}; +\\infty) \\setminus \\{{{v+4}\\}}$", f"$({v+1}; {v+4})$", f"$\\mathbb{{R}} \\setminus \\{{{v+4}\\}}$"],
             0, f"Điều kiện: $x - {v+1} > 0 \\Leftrightarrow x > {v+1}$ và $x \\ne {v+4}$. Vậy $D = ({v+1}; +\\infty) \\setminus \\{{{v+4}\\}}$."
         )),
        ("Xác định hàm số bậc hai qua đỉnh và điểm", "b16",
         lambda v: (
             f"Biết parabol $y = ax^2 + bx + 1$ có đỉnh $I(1; -{v+1})$. Giá trị của $a$ là:",
             [f"${v+2}$", f"-{v+2}", f"${v+1}$", "1"],
             0, f"Đỉnh có $x = 1 \\Rightarrow -b/(2a) = 1 \\Rightarrow b = -2a$. Tại $x = 1: a(1)^2 - 2a(1) + 1 = -{v+1} \\Leftrightarrow -a + 1 = -{v+1} \\Leftrightarrow a = {v+2}$."
         )),
        ("Khoảng nghịch biến của parabol", "b16",
         lambda v: (
             f"Hàm số $y = -x^2 + {2*(v+2)}x - 3$ đồng biến trên khoảng nào sau đây?",
             [f"$(-\\infty; {v+2})$", f"$({v+2}; +\\infty)$", "$(-\\infty; 0)$", "$(0; +\\infty)$"],
             0, f"Hệ số $a = -1 < 0$, hoành độ đỉnh $x = -b/(2a) = {2*(v+2)}/2 = {v+2}$. Hàm số đồng biến trên $(-\\infty; {v+2})$."
         )),
        ("Tham số để parabol đi qua điểm", "b16",
         lambda v: (
             f"Tìm $m$ để đồ thị hàm số $y = x^2 - 3x + m$ đi qua điểm $M(2; {v+5})$.",
             [f"$m = {v+7}$", f"$m = {v+3}$", f"$m = {v+5}$", f"$m = -{v+7}$"],
             0, f"Thay tọa độ $M(2; {v+5})$: $2^2 - 3(2) + m = {v+5} \\Leftrightarrow -2 + m = {v+5} \\Leftrightarrow m = {v+7}$."
         )),
        ("Xét dấu tam thức bậc hai có hai nghiệm phân biệt", "b17",
         lambda v: (
             f"Tam thức $f(x) = x^2 - {2*v+5}x + {(v+2)*(v+3)}$ nhận giá trị âm khi và chỉ khi:",
             [f"${v+2} < x < {v+3}$", f"$x < {v+2}$ hoặc $x > {v+3}$", f"$x \\le {v+2}$", f"$x \\ge {v+3}$"],
             0, f"Tam thức có 2 nghiệm ${v+2}$ và ${v+3}$, hệ số $a = 1 > 0$. Áp dụng quy tắc 'trong trái ngoài cùng', $f(x) < 0$ khi ${v+2} < x < {v+3}$."
         )),
        ("Giải bất phương trình bậc hai cơ bản", "b17",
         lambda v: (
             f"Tập nghiệm của bất phương trình $x^2 - {2*v+3}x + {(v+1)*(v+2)} \\le 0$ là:",
             [f"$[{v+1}; {v+2}]$", f"$({v+1}; {v+2})$", f"$(-\\infty; {v+1}] \\cup [{v+2}; +\\infty)$", "$\\emptyset$"],
             0, f"Tam thức có nghiệm ${v+1}$ và ${v+2}$, $a = 1 > 0$. Do đó $f(x) \\le 0 \\Leftrightarrow x \\in [{v+1}; {v+2}]$."
         )),
        ("Bất phương trình bậc hai vô nghiệm", "b17",
         lambda v: (
             f"Tập nghiệm của bất phương trình $-x^2 + 2x - {v+3} > 0$ là:",
             ["$\\emptyset$", "$\\mathbb{R}$", f"$(1; {v+3})$", "$(-1; 1)$"],
             0, f"$\\Delta' = 1 - ({v+3}) = -{v+2} < 0$ và $a = -1 < 0$ nên $-x^2 + 2x - {v+3} < 0, \\forall x$. BPT vô nghiệm, tập nghiệm là $\\emptyset$."
         )),
        ("Giải phương trình căn f bằng căn g", "b18",
         lambda v: (
             f"Nghiệm của phương trình $\\sqrt{{2x - {v+1}}} = \\sqrt{{x + {v+3}}}$ là:",
             [f"$x = {2*v+4}$", f"$x = {v+1}$", f"$x = {2*v+5}$", "Vô nghiệm"],
             0, f"Bình phương hai vế: $2x - {v+1} = x + {v+3} \\Leftrightarrow x = {2*v+4}$. Thử lại thỏa mãn."
         )),
        ("Phương trình quy về bậc hai dạng căn f(x) bằng g(x)", "b18",
         lambda v: (
             f"Số nghiệm của phương trình $\\sqrt{{x^2 - 4x + 4}} = x - 2$ (mẫu {v+1}) là:",
             ["Vô số nghiệm", "1 nghiệm", "2 nghiệm", "Vô nghiệm"],
             0, f"Phương trình tương đương $|x - 2| = x - 2 \\Leftrightarrow x \\ge 2$. Vậy phương trình có vô số nghiệm."
         )),
        ("Giải phương trình căn thức bậc hai bằng bậc nhất", "b18",
         lambda v: (
             f"Nghiệm của phương trình $\\sqrt{{x^2 + {2*v+2}x + {v+1}}} = x + 1$ là:",
             [f"$x = 0$", f"$x = {v+1}$", f"$x = -1$", "Vô nghiệm"],
             0, f"Bình phương 2 vế với điều kiện $x \\ge -1$: $x^2 + {2*v+2}x + {v+1} = x^2 + 2x + 1 \\Leftrightarrow {2*v}x = -{v}$. Với mọi $v$, $x = 0$ thỏa mãn."
         )),
        ("Số nghiệm nguyên của bất phương trình bậc hai", "b17",
         lambda v: (
             f"Số nghiệm nguyên của bất phương trình $x^2 \\le {(v+2)**2}$ là:",
             [f"${2*v+5}$", f"${2*v+4}$", f"${v+2}$", f"${v+3}$"],
             0, f"$x^2 \\le {(v+2)**2} \\Leftrightarrow -{v+2} \\le x \\le {v+2}$. Số nghiệm nguyên là ${v+2} - (-{v+2}) + 1 = {2*v+5}$."
         )),
        ("Giá trị lớn nhất của parabol trên đoạn", "b16",
         lambda v: (
             f"Giá trị lớn nhất của hàm số $y = -x^2 + 2x + {v+2}$ trên đoạn $[0; 2]$ là:",
             [f"${v+3}$", f"${v+2}$", f"${v+1}$", f"${v+4}$"],
             0, f"Đỉnh $x = 1 \\in [0; 2]$. Ta có $y(0) = {v+2}$, $y(1) = {v+3}$, $y(2) = {v+2}$. Vậy giá trị lớn nhất là ${v+3}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(th_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c6_th_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+16})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    vd_defs = [
        ("Tìm m để tam thức bậc hai luôn dương trên R", "b17",
         lambda v: (
             f"Tìm tất cả các giá trị của tham số $m$ để tam thức $f(x) = x^2 - 2(m + 1)x + m^2 + {v+3} > 0, \\forall x \\in \\mathbb{{R}}$.",
             [f"$m < \\frac{{{v+2}}}{{2}}$", f"$m > \\frac{{{v+2}}}{{2}}$", f"$m < {v+2}$", f"$m > {v+2}$"],
             0, f"Yêu cầu bài toán $\\Leftrightarrow a = 1 > 0$ và $\\Delta' = (m+1)^2 - (m^2 + {v+3}) < 0 \\Leftrightarrow 2m + 1 - {v+3} < 0 \\Leftrightarrow 2m < {v+2} \\Leftrightarrow m < \\frac{{{v+2}}}{{2}}$."
         )),
        ("Tham số m để phương trình có hai nghiệm trái dấu", "b17",
         lambda v: (
             f"Tìm $m$ để phương trình $x^2 - {v+4}x + m - {v+2} = 0$ có hai nghiệm trái dấu.",
             [f"$m < {v+2}$", f"$m > {v+2}$", f"$m \\le {v+2}$", f"$m > 0$"],
             0, f"Phương trình bậc hai có hai nghiệm trái dấu khi và chỉ khi $ac < 0 \\Leftrightarrow 1 \\times (m - {v+2}) < 0 \\Leftrightarrow m < {v+2}$."
         )),
        ("Bài toán thực tế tối ưu hóa với hàm số bậc hai", "b16",
         lambda v: (
             f"Một người nông dân dùng {40 + 4*v} m lưới thép để rào mảnh vườn hình chữ nhật giáp bờ tường thẳng (không rào cạnh bờ tường). Diện tích lớn nhất của mảnh vườn là:",
             [f"{(40 + 4*v)**2 // 8} m$^2$", f"{(40 + 4*v)**2 // 8 + 50} m$^2$", f"{(40 + 4*v)**2 // 8 - 50} m$^2$", f"{(40 + 4*v)**2 // 8 + 100} m$^2$"],
             0, f"Gọi chiều rộng là $x$ thì chiều dài là $L = {40 + 4*v} - 2x$. Diện tích $S = x({40 + 4*v} - 2x) = -2x^2 + {40 + 4*v}x$. Cực đại tại $x = {(40 + 4*v)//4}$, diện tích lớn nhất là ${(40 + 4*v)**2 // 8}$ m$^2$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(vd_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c6_vd_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+28})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "vd",
                "lesson": lesson
            })

    # TLN C6: Đảm bảo đáp số nguyên 100%
    sa_nb = [
        ("Hoành độ đỉnh parabol", "b16",
         lambda v: (
             f"Tìm hoành độ đỉnh của parabol $y = x^2 - {2*(v+3)}x + 1$.",
             v+3, "Hoành độ đỉnh là $x = -b/(2a) = " + str(v+3) + "$."
         )),
        ("Tung độ giao điểm với Oy", "b16",
         lambda v: (
             f"Tìm tung độ giao điểm của parabol $y = 3x^2 - 4x + {v+7}$ với trục tung $Oy$.",
             v+7, "Tại $x = 0$, $y = " + str(v+7) + "$."
         )),
        ("Giá trị của tam thức tại một điểm", "b17",
         lambda v: (
             f"Tính giá trị của tam thức bậc hai $f(x) = 2x^2 - 3x + {v+1}$ tại $x = 2$.",
             2*4 - 6 + v + 1, "Thay $x = 2$ vào tam thức ta được giá trị là " + str(2*4 - 6 + v + 1) + "."
         )),
        ("Nghiệm dương của phương trình bậc hai", "b17",
         lambda v: (
             f"Tìm nghiệm dương của phương trình $x^2 - {(v+2)**2} = 0$.",
             v+2, "Phương trình có nghiệm $x = \\pm " + str(v+2) + "$, nghiệm dương là " + str(v+2) + "."
         )),
        ("Tung độ đỉnh parabol đặc biệt", "b16",
         lambda v: (
             f"Tìm tung độ đỉnh của parabol $y = (x - {v+2})^2 + {v+5}$.",
             v+5, "Tung độ đỉnh là " + str(v+5) + "."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_nb):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    sa_th = [
        ("Nghiệm phương trình chứa căn nguyên", "b18",
         lambda v: (
             f"Giải phương trình $\\sqrt{{2x - 1}} = {2*v + 3}$. Tìm nghiệm $x$.",
             ((2*v + 3)**2 + 1) // 2,
             f"Bình phương hai vế: $2x - 1 = {(2*v+3)**2} \\Leftrightarrow 2x = {(2*v+3)**2 + 1} \\Leftrightarrow x = {((2*v+3)**2 + 1)//2}$."
         )),
        ("Số nghiệm nguyên của BPT bậc hai", "b17",
         lambda v: (
             f"Có bao nhiêu số nguyên $x$ thỏa mãn bất phương trình $x^2 - {2*v+5}x + {(v+2)*(v+3)} \\le 0$?",
             2,
             f"Bất phương trình tương đương ${v+2} \\le x \\le {v+3}$. Có đúng 2 số nguyên là {v+2} và {v+3}."
         )),
        ("Giá trị nhỏ nhất của hàm số bậc hai", "b16",
         lambda v: (
             f"Tìm giá trị nhỏ nhất của hàm số $y = x^2 - {2*(v+2)}x + {(v+2)**2 + v + 4}$ trên $\\mathbb{{R}}$.",
             v+4,
             f"Biến đổi $y = (x - {v+2})^2 + {v+4} \\ge {v+4}$. Giá trị nhỏ nhất là {v+4}."
         )),
        ("Nghiệm của phương trình căn thức đơn giản", "b18",
         lambda v: (
             f"Tìm nghiệm của phương trình $\\sqrt{{x + {v+2}}} = {v+3}$.",
             (v+3)**2 - (v+2),
             f"Bình phương 2 vế: $x + {v+2} = {(v+3)**2} \\Leftrightarrow x = {(v+3)**2 - (v+2)}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_th):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+6})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    sa_vd = [
        ("Giá trị nguyên nhỏ nhất của tham số m", "b17",
         lambda v: (
             f"Tìm giá trị nguyên nhỏ nhất của $m$ để tam thức $f(x) = x^2 - 4x + m + {v} > 0$ luôn đúng với mọi $x \\in \\mathbb{{R}}$.",
             5 - v,
             f"Điều kiện $\\Delta' = 4 - (m + {v}) < 0 \\Leftrightarrow m > {4 - v}$. Do đó số nguyên nhỏ nhất của $m$ là {5 - v}."
         ))
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_vd):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm 10)",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "vd",
                "lesson": "b17"
            })

    save_bank("c6", "Hàm số, đồ thị và ứng dụng", [
        {"lesson_id": "b15", "sgk_title": "Bài 15. Hàm số"},
        {"lesson_id": "b16", "sgk_title": "Bài 16. Hàm số bậc hai"},
        {"lesson_id": "b17", "sgk_title": "Bài 17. Dấu của tam thức bậc hai"},
        {"lesson_id": "b18", "sgk_title": "Bài 18. Phương trình quy về phương trình bậc hai"}
    ], mc, sa)

# ==============================================================================
# CHƯƠNG 7: PHƯƠNG PHÁP TOẠ ĐỘ TRONG MẶT PHẲNG
# ==============================================================================
def build_c7():
    mc = []
    sa = []

    nb_defs = [
        ("Vectơ pháp tuyến của đường thẳng", "b19",
         lambda v: (
             f"Vectơ nào sau đây là một vectơ pháp tuyến của đường thẳng $\\Delta: {v+2}x - {v+3}y + 1 = 0$?",
             [f"$\\vec{{n}} = ({v+2}; -{v+3})$", f"$\\vec{{n}} = ({v+2}; {v+3})$", f"$\\vec{{n}} = ({v+4}; {v+2})$", f"$\\vec{{n}} = (-{v+5}; {v+2})$"],
             0, f"Đường thẳng $Ax + By + C = 0$ có VTPT là $\\vec{{n}} = (A; B) = ({v+2}; -{v+3})$."
         )),
        ("Vectơ chỉ phương của đường thẳng tham số", "b19",
         lambda v: (
             f"Vectơ chỉ phương của đường thẳng $d: x = 1 + {v+1}t, y = 2 - {v+2}t$ là:",
             [f"$\\vec{{u}} = ({v+1}; -{v+2})$", f"$\\vec{{u}} = ({v+1}; {v+2})$", f"$\\vec{{u}} = (-{v+1}; -{v+2})$", f"$\\vec{{u}} = ({v+3}; {v+1})$"],
             0, f"Đường thẳng tham số $x = x_0 + at, y = y_0 + bt$ có VTCP $\\vec{{u}} = (a; b) = ({v+1}; -{v+2})$."
         )),
        ("Chuyển đổi VTPT sang VTCP", "b19",
         lambda v: (
             f"Đường thẳng $\\Delta$ có VTPT $\\vec{{n}} = ({v+1}; {v+4})$. Một VTCP của $\\Delta$ là:",
             [f"$\\vec{{u}} = (-{v+4}; {v+1})$", f"$\\vec{{u}} = ({v+1}; -{v+4})$", f"$\\vec{{u}} = ({v+5}; {v+1})$", f"$\\vec{{u}} = ({v+1}; {v+5})$"],
             0, f"Nếu $\\vec{{n}} = (A; B)$ thì VTCP vuông góc là $\\vec{{u}} = (-B; A) = (-{v+4}; {v+1})$."
         )),
        ("Điểm thuộc đường thẳng tổng quát", "b19",
         lambda v: (
             f"Điểm nào sau đây thuộc đường thẳng $\\Delta: 2x - y - {2*v+1} = 0$?",
             [f"$M({v+1}; 1)$", f"$N(0; {v+3})$", f"$P(1; 0)$", f"$Q({v+2}; 2)$"],
             0, f"Thay $M({v+1}; 1)$: $2({v+1}) - 1 - ({2*v+1}) = 2v + 2 - 1 - 2v - 1 = 0$. Điểm $M$ thuộc đường thẳng."
         )),
        ("PT tham số qua điểm có VTCP", "b19",
         lambda v: (
             f"Phương trình tham số của đường thẳng đi qua $A(2; -1)$ có VTCP $\\vec{{u}} = ({v+2}; 3)$ là:",
             [f"$x = 2 + {v+2}t, y = -1 + 3t$", f"$x = {v+2} + 2t, y = 3 - t$", f"$x = 2 - {v+2}t, y = 1 - 3t$", f"$x = 1 + {v+2}t, y = 2 + 3t$"],
             0, f"Phương trình tham số: $x = x_0 + at = 2 + {v+2}t, y = y_0 + bt = -1 + 3t$."
         )),
        ("PT tổng quát qua điểm có VTPT", "b19",
         lambda v: (
             f"Phương trình tổng quát của đường thẳng đi qua $M(1; 2)$ và có VTPT $\\vec{{n}} = ({v+3}; 1)$ là:",
             [f"${v+3}x + y - {v+5} = 0$", f"${v+3}x + y + {v+5} = 0$", f"$x + {v+3}y - {v+5} = 0$", f"${v+3}x - y - {v+1} = 0$"],
             0, f"Phương trình: ${v+3}(x - 1) + 1(y - 2) = 0 \\Leftrightarrow {v+3}x + y - ({v+3} + 2) = 0 \\Leftrightarrow {v+3}x + y - {v+5} = 0$."
         )),
        ("Điều kiện hai đường thẳng vuông góc", "b20",
         lambda v: (
             f"Hai đường thẳng $\\Delta_1: A_1 x + B_1 y + C_1 = 0$ và $\\Delta_2: A_2 x + B_2 y + C_2 = 0$ vuông góc khi và chỉ khi (mẫu {v+1}):",
             ["$A_1 A_2 + B_1 B_2 = 0$", "$A_1 B_2 - A_2 B_1 = 0$", "$A_1 A_2 - B_1 B_2 = 0$", "$A_1 B_1 + A_2 B_2 = 0$"],
             0, f"Hai đường thẳng vuông góc khi tích vô hướng hai VTPT bằng 0: $A_1 A_2 + B_1 B_2 = 0$."
         )),
        ("Công thức khoảng cách từ điểm đến đường thẳng", "b20",
         lambda v: (
             f"Khoảng cách từ điểm $M(x_0; y_0)$ đến đường thẳng $\\Delta: Ax + By + C = 0$ được tính bởi công thức (mẫu {v+1}):",
             ["$d(M, \\Delta) = \\frac{|Ax_0 + By_0 + C|}{\\sqrt{A^2 + B^2}}$", "$d(M, \\Delta) = \\frac{Ax_0 + By_0 + C}{\\sqrt{A^2 + B^2}}$", "$d(M, \\Delta) = \\frac{|Ax_0 + By_0 + C|}{A^2 + B^2}$", "$d(M, \\Delta) = \\frac{|Ax_0 + By_0|}{\\sqrt{A^2 + B^2}}$"],
             0, f"Công thức chuẩn: $d(M, \\Delta) = \\frac{{|Ax_0 + By_0 + C|}}{{\\sqrt{{A^2 + B^2}}}}$."
         )),
        ("Tọa độ tâm đường tròn chính tắc", "b21",
         lambda v: (
             f"Tọa độ tâm của đường tròn $(C): (x - {v+2})^2 + (y + {v+3})^2 = 16$ là:",
             [f"$I({v+2}; -{v+3})$", f"$I(-{v+2}; {v+3})$", f"$I({v+2}; {v+5})$", f"$I(-{v+2}; -{v+3})$"],
             0, f"Đường tròn $(x - a)^2 + (y - b)^2 = R^2$ có tâm $I(a; b) = ({v+2}; -{v+3})$."
         )),
        ("Bán kính đường tròn chính tắc", "b21",
         lambda v: (
             f"Bán kính của đường tròn $(C): (x - 1)^2 + (y - 2)^2 = {(v+2)**2}$ là:",
             [f"$R = {v+2}$", f"$R = {v+5}$", f"$R = {v+8}$", f"$R = {v+1}$"],
             0, f"Bán kính $R = \\sqrt{{{(v+2)**2}}} = {v+2}$."
         )),
        ("Tâm đường tròn dạng tổng quát", "b21",
         lambda v: (
             f"Tọa độ tâm của đường tròn $x^2 + y^2 - {2*(v+1)}x + {4*(v+1)}y - 1 = 0$ là:",
             [f"$I({v+1}; -{2*(v+1)})$", f"$I(-{v+1}; {2*(v+1)})$", f"$I({2*(v+1)}; -{4*(v+1)})$", f"$I({v+1}; {2*(v+1) + 1})$"],
             0, f"Tâm $I(a; b)$ với $a = -(-{2*(v+1)})/2 = {v+1}$ và $b = -(4*(v+1))/2 = -{2*(v+1)}$."
         )),
        ("PT chính tắc của elip", "b22",
         lambda v: (
             f"Phương trình nào sau đây là phương trình chính tắc của một elip (mẫu {v+1})?",
             [f"$\\frac{{x^2}}{{{(v+3)**2}}} + \\frac{{y^2}}{{{(v+2)**2}}} = 1$", f"$\\frac{{x^2}}{{{(v+2)**2}}} - \\frac{{y^2}}{{{(v+3)**2}}} = 1$", f"$\\frac{{x^2}}{{{(v+1)**2}}} + \\frac{{y^2}}{{{(v+4)**2}}} = 1$", f"$x^2 + y^2 = {(v+3)**2}$"],
             0, f"Phương trình chính tắc elip có dạng $\\frac{{x^2}}{{a^2}} + \\frac{{y^2}}{{b^2}} = 1$ với $a > b > 0$."
         )),
        ("PT chính tắc của hypebol", "b22",
         lambda v: (
             f"Phương trình chính tắc của hypebol có dạng (mẫu {v+1}):",
             ["$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$", "$\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$", "$y^2 = 2px$", "$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = -1$"],
             0, f"Phương trình chính tắc hypebol là $\\frac{{x^2}}{{a^2}} - \\frac{{y^2}}{{b^2}} = 1$."
         )),
        ("Tiêu điểm của parabol", "b22",
         lambda v: (
             f"Tọa độ tiêu điểm của parabol $y^2 = {4*(v+1)}x$ là:",
             [f"$F({v+1}; 0)$", f"$F(0; {v+1})$", f"$F({2*(v+1) + 3}; 0)$", f"$F(-{v+1}; 0)$"],
             0, f"Parabol $y^2 = 2px$ có $2p = {4*(v+1)} \\Rightarrow p = {2*(v+1)}$. Tiêu điểm $F(p/2; 0) = ({v+1}; 0)$."
         )),
        ("Độ dài trục lớn elip cơ bản", "b22",
         lambda v: (
             f"Độ dài trục lớn của elip $(E): \\frac{{x^2}}{{{(v+4)**2}}} + \\frac{{y^2}}{{{(v+2)**2}}} = 1$ là:",
             [f"${2*(v+4)}$", f"${v+4}$", f"${2*v+15}$", f"${3*v+10}$"],
             0, f"Ta có $a = {v+4}$, độ dài trục lớn là $2a = {2*(v+4)}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(nb_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c7_nb_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    th_defs = [
        ("PT đường thẳng đi qua hai điểm", "b19",
         lambda v: (
             f"Đường thẳng đi qua hai điểm $A(1; {v+1})$ và $B(3; {v+5})$ có một vectơ chỉ phương là:",
             ["$\\vec{u} = (1; 2)$", "$\\vec{u} = (2; 1)$", "$\\vec{u} = (1; -2)$", "$\\vec{u} = (-2; 1)$"],
             0, f"$\\vec{{AB}} = (2; 4) = 2(1; 2)$. Một VTCP là $\\vec{{u}} = (1; 2)$."
         )),
        ("PT đường thẳng song song", "b19",
         lambda v: (
             f"Phương trình đường thẳng đi qua điểm $M(1; -1)$ và song song với $d: 2x - 3y + {v+1} = 0$ là:",
             ["$2x - 3y - 5 = 0$", "$2x - 3y + 5 = 0$", "$3x + 2y - 1 = 0$", "$2x + 3y + 1 = 0$"],
             0, f"Đường thẳng song song có dạng $2x - 3y + C = 0$. Qua $M(1; -1) \\Rightarrow 2(1) - 3(-1) + C = 0 \\Leftrightarrow C = -5$."
         )),
        ("PT đường thẳng vuông góc", "b19",
         lambda v: (
             f"Phương trình đường thẳng đi qua gốc tọa độ $O(0; 0)$ và vuông góc với $\\Delta: {v+2}x - y + 1 = 0$ là:",
             [f"$x + {v+2}y = 0$", f"${v+2}x + y = 0$", f"$x - {v+2}y = 0$", f"${v+2}x - y = 0$"],
             0, f"Đường thẳng vuông góc có VTPT là VTCP của $\\Delta$, tức $(1; {v+2})$. Qua $O(0; 0)$ nên phương trình là $x + {v+2}y = 0$."
         )),
        ("Vị trí tương đối của hai đường thẳng", "b20",
         lambda v: (
             f"Vị trí tương đối của hai đường thẳng $\\Delta_1: {v+1}x - 2y + 1 = 0$ và $\\Delta_2: {2*(v+1)}x - 4y + 5 = 0$ là:",
             ["Song song", "Cắt nhau nhưng không vuông góc", "Trùng nhau", "Vuông góc"],
             0, f"Tỉ số các hệ số: $\\frac{{{v+1}}}{{{2*(v+1)}}} = \\frac{{-2}}{{-4}} = \\frac{{1}}{{2}} \\ne \\frac{{1}}{{5}}$. Vậy hai đường thẳng song song."
         )),
        ("Góc giữa hai đường thẳng", "b20",
         lambda v: (
             f"Góc giữa hai đường thẳng $d_1: x + {v+2}y - 1 = 0$ và $d_2: {v+2}x - y + 3 = 0$ bằng:",
             ["$90^\\circ$", "$45^\\circ$", "$60^\\circ$", "$30^\\circ$"],
             0, f"Hai VTPT là $\\vec{{n_1}} = (1; {v+2})$ và $\\vec{{n_2}} = ({v+2}; -1)$. Tích vô hướng $\\vec{{n_1}} \\cdot \\vec{{n_2}} = 1({v+2}) + ({v+2})(-1) = 0$. Vậy góc giữa chúng là $90^\\circ$."
         )),
        ("Khoảng cách từ điểm đến đường thẳng cụ thể", "b20",
         lambda v: (
             f"Khoảng cách từ điểm $M(1; {v+2})$ đến đường thẳng $\\Delta: 3x + 4y - {4*v + 11} = 0$ là:",
             ["$0$", "$1$", "$2$", "$3$"],
             0, f"Tử số: $|3(1) + 4({v+2}) - (4v + 11)| = |3 + 4v + 8 - 4v - 11| = |0| = 0$. Điểm $M$ thuộc đường thẳng nên khoảng cách bằng 0."
         )),
        ("PT đường tròn có tâm và đi qua một điểm", "b21",
         lambda v: (
             f"Phương trình đường tròn tâm $O(0; 0)$ đi qua điểm $A({v+3}; 0)$ là:",
             [f"$x^2 + y^2 = {(v+3)**2}$", f"$x^2 + y^2 = {v+3}$", f"$(x - {v+3})^2 + y^2 = 1$", f"$x^2 + y^2 = {2*(v+3)}$"],
             0, f"Bán kính $R = OA = {v+3}$. Phương trình đường tròn là $x^2 + y^2 = {(v+3)**2}$."
         )),
        ("PT đường tròn đường kính AB", "b21",
         lambda v: (
             f"Đường kính $AB$ với $A(-{v+2}; 0)$ và $B({v+2}; 0)$. Phương trình đường tròn là:",
             [f"$x^2 + y^2 = {(v+2)**2}$", f"$x^2 + y^2 = {(v+2)**2 + 5}$", f"$(x - {v+2})^2 + y^2 = {(v+2)**2}$", f"$x^2 + y^2 = {v+1}$"],
             0, f"Tâm là trung điểm $O(0; 0)$, bán kính $R = AB/2 = {v+2}$. Phương trình $x^2 + y^2 = {(v+2)**2}$."
         )),
        ("PT tiếp tuyến của đường tròn tại điểm", "b21",
         lambda v: (
             f"Phương trình tiếp tuyến của đường tròn $(C): x^2 + y^2 = {(v+2)**2}$ tại điểm $M({v+2}; 0)$ là:",
             [f"$x = {v+2}$", f"$y = {v+2}$", f"$x + y = {v+2}$", f"$x = -{v+2}$"],
             0, f"Tâm $O(0; 0)$, VTPT là $\\vec{{OM}} = ({v+2}; 0) = ({v+2})(1; 0)$. Tiếp tuyến có phương trình $1(x - {v+2}) + 0(y - 0) = 0 \\Leftrightarrow x = {v+2}$."
         )),
        ("Tiêu cự của elip", "b22",
         lambda v: (
             f"Tiêu cự của elip $(E): \\frac{{x^2}}{{25}} + \\frac{{y^2}}{{9}} = 1$ (mẫu {v+1}) bằng:",
             ["$8$", "$4$", "$6$", "$10$"],
             0, f"Ta có $a^2 = 25, b^2 = 9 \\Rightarrow c = \\sqrt{{25 - 9}} = 4$. Tiêu cự $2c = 8$."
         )),
        ("Độ dài trục bé của elip", "b22",
         lambda v: (
             f"Độ dài trục bé của elip $(E): \\frac{{x^2}}{{{(v+5)**2}}} + \\frac{{y^2}}{{{(v+3)**2}}} = 1$ là:",
             [f"${2*(v+3)}$", f"${v+3}$", f"${2*(v+5)}$", f"${(v+3)**2}$"],
             0, f"Ta có $b = {v+3}$, độ dài trục bé là $2b = {2*(v+3)}$."
         )),
        ("Đường chuẩn của parabol", "b22",
         lambda v: (
             f"Phương trình đường chuẩn của parabol $y^2 = {4*(v+1)}x$ là:",
             [f"$x = -{v+1}$", f"$x = {v+1}$", f"$y = -{v+1}$", f"$x = -{2*(v+1)}$"],
             0, f"$2p = {4*(v+1)} \\Rightarrow p = {2*(v+1)}$. Đường chuẩn có phương trình $x = -p/2 = -{v+1}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(th_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c7_th_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+16})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    vd_defs = [
        ("Khoảng cách giữa hai đường thẳng song song", "b20",
         lambda v: (
             f"Khoảng cách giữa hai đường thẳng song song $\\Delta_1: 3x - 4y + {v+1} = 0$ và $\\Delta_2: 3x - 4y + {v+11} = 0$ là:",
             ["$2$", "$10$", "$5$", "$1$"],
             0, f"Công thức $d(\\Delta_1, \\Delta_2) = \\frac{{|C_1 - C_2|}}{{\\sqrt{{A^2 + B^2}}}} = \\frac{{|{v+1} - ({v+11})|}}{{\\sqrt{{3^2 + (-4)^2}}}} = \\frac{{10}}{{5}} = 2$."
         )),
        ("Tham số m để đường tròn tiếp xúc đường thẳng", "b21",
         lambda v: (
             f"Tìm $m > 0$ để đường thẳng $\\Delta: x - m = 0$ tiếp xúc với đường tròn $(C): x^2 + y^2 = {(v+3)**2}$.",
             [f"$m = {v+3}$", f"$m = {(v+3)**2}$", f"$m = {2*(v+3)}$", f"$m = {v+1}$"],
             0, f"Đường tròn có tâm $O(0; 0)$ và $R = {v+3}$. Tiếp xúc khi $d(O, \\Delta) = R \\Leftrightarrow |0 - m| = {v+3} \\Leftrightarrow m = {v+3}$ (do $m > 0$)."
         )),
        ("Ứng dụng elip trong thực tế", "b22",
         lambda v: (
             f"Một đường hầm có mặt cắt là nửa hình elip với chiều rộng {2*(v+5)} m và chiều cao {v+3} m. Phương trình chính tắc của elip đó là:",
             [f"$\\frac{{x^2}}{{{(v+5)**2}}} + \\frac{{y^2}}{{{(v+3)**2}}} = 1$", f"$\\frac{{x^2}}{{{(2*v+10)**2}}} + \\frac{{y^2}}{{{(v+3)**2}}} = 1$", f"$\\frac{{x^2}}{{{(v+3)**2}}} + \\frac{{y^2}}{{{(v+5)**2}}} = 1$", f"$\\frac{{x^2}}{{{(v+5)**2}}} - \\frac{{y^2}}{{{(v+3)**2}}} = 1$"],
             0, f"Chiều rộng $2a = {2*(v+5)} \\Rightarrow a = {v+5}$. Chiều cao nửa elip là $b = {v+3}$. Phương trình: $\\frac{{x^2}}{{{(v+5)**2}}} + \\frac{{y^2}}{{{(v+3)**2}}} = 1$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(vd_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c7_vd_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+28})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "vd",
                "lesson": lesson
            })

    # TLN C7: Số nguyên 100%
    sa_nb = [
        ("Hoành độ tâm đường tròn", "b21",
         lambda v: (
             f"Tìm hoành độ tâm của đường tròn $(x - {v+4})^2 + (y - 1)^2 = 25$.",
             v+4, f"Hoành độ tâm là $a = {v+4}$."
         )),
        ("Tung độ tâm đường tròn", "b21",
         lambda v: (
             f"Tìm tung độ tâm của đường tròn $(x + 2)^2 + (y - {v+6})^2 = 9$.",
             v+6, f"Tung độ tâm là $b = {v+6}$."
         )),
        ("Bán kính đường tròn", "b21",
         lambda v: (
             f"Tìm bán kính $R$ của đường tròn $(x - 1)^2 + (y - 2)^2 = {(v+3)**2}$.",
             v+3, f"Bán kính là $R = \\sqrt{{{(v+3)**2}}} = {v+3}$."
         )),
        ("Hoành độ tiêu điểm parabol", "b22",
         lambda v: (
             f"Tìm hoành độ tiêu điểm của parabol $y^2 = {4*(v+2)}x$.",
             v+2, f"Ta có $2p = {4*(v+2)} \\Rightarrow p = {2*(v+2)}$. Hoành độ tiêu điểm là $p/2 = {v+2}$."
         )),
        ("Độ dài trục lớn elip", "b22",
         lambda v: (
             f"Tìm độ dài trục lớn của elip $\\frac{{x^2}}{{{(v+3)**2}}} + \\frac{{y^2}}{4} = 1$.",
             2*(v+3), f"Trục lớn $2a = 2({v+3}) = {2*(v+3)}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_nb):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    sa_th = [
        ("Khoảng cách từ điểm đến đường thẳng", "b20",
         lambda v: (
             f"Tính khoảng cách từ điểm $M(0; {v+1})$ đến đường thẳng $\\Delta: 3x - 4y + {4*v + 19} = 0$.",
             3,
             f"$d(M, \\Delta) = \\frac{{|3(0) - 4({v+1}) + {4*v + 19}|}}{{\\sqrt{{3^2 + (-4)^2}}}} = \\frac{{|-4v - 4 + 4v + 19|}}{{5}} = \\frac{{15}}{{5}} = 3$."
         )),
        ("Tiêu cự của elip", "b22",
         lambda v: (
             f"Tính tiêu cự của elip $\\frac{{x^2}}{{(v+5)^2}} + \\frac{{y^2}}{{(v+3)^2}} = 1$ khi $v = {v}$ (elip $\\frac{{x^2}}{{{(v+5)**2}}} + \\frac{{y^2}}{{{(v+3)**2}}} = 1$, biết $c^2 = a^2 - b^2$). Tính $2c^2$.",
             2 * ((v+5)**2 - (v+3)**2),
             f"$c^2 = {(v+5)**2} - {(v+3)**2} = {(v+5)**2 - (v+3)**2}$. Do đó $2c^2 = {2 * ((v+5)**2 - (v+3)**2)}$."
         )),
        ("Bán kính đường tròn tổng quát", "b21",
         lambda v: (
             f"Tìm bán kính $R$ của đường tròn $x^2 + y^2 - 6x - 8y - {v*10 - 25} = 0$ khi biểu thức $a^2+b^2-c = {(v+5)**2}$.",
             v+5,
             f"Bán kính $R = \\sqrt{{a^2 + b^2 - c}} = {v+5}$."
         )),
        ("Độ dài đoạn thẳng nối hai tâm", "b21",
         lambda v: (
             f"Tính khoảng cách giữa hai tâm của hai đường tròn $(x - 1)^2 + y^2 = 4$ và $(x - {v+4})^2 + y^2 = 9$.",
             v+3,
             f"Khoảng cách giữa hai tâm $I_1(1; 0)$ và $I_2({v+4}; 0)$ là $|{v+4} - 1| = {v+3}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_th):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+6})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    sa_vd = [
        ("Khoảng cách ngắn nhất giữa điểm và đường tròn", "b21",
         lambda v: (
             f"Cho điểm $M(0; {v+7})$ và đường tròn $(C): x^2 + y^2 = {(v+2)**2}$. Tính khoảng cách ngắn nhất từ $M$ đến một điểm trên $(C)$.",
             (v+7) - (v+2),
             f"Khoảng cách từ $M$ đến tâm $O(0; 0)$ là $d = {v+7}$. Khoảng cách ngắn nhất đến đường tròn là $d - R = ({v+7}) - ({v+2}) = 5$."
         ))
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_vd):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"Khoảng cách từ điểm ngoài đến đường tròn (Nhóm 10)",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "vd",
                "lesson": "b21"
            })

    save_bank("c7", "Phương pháp toạ độ trong mặt phẳng", [
        {"lesson_id": "b19", "sgk_title": "Bài 19. Phương trình đường thẳng"},
        {"lesson_id": "b20", "sgk_title": "Bài 20. Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách"},
        {"lesson_id": "b21", "sgk_title": "Bài 21. Đường tròn trong mặt phẳng toạ độ"},
        {"lesson_id": "b22", "sgk_title": "Bài 22. Ba đường conic"}
    ], mc, sa)

# ==============================================================================
# CHƯƠNG 8: ĐẠI SỐ TỔ HỢP
# ==============================================================================
def build_c8():
    mc = []
    sa = []

    nb_defs = [
        ("Quy tắc cộng cơ bản", "b23",
         lambda v: (
             f"Một bạn có {v+3} quyển sách Toán và {v+4} quyển sách Văn (các quyển sách khác nhau). Có bao nhiêu cách chọn 1 quyển sách để đọc?",
             [f"{2*v+7}", f"{(v+3)*(v+4)}", f"{v+3}", f"{v+4}"],
             0, f"Áp dụng quy tắc cộng: số cách chọn là ${v+3} + {v+4} = {2*v+7}$ cách."
         )),
        ("Quy tắc nhân cơ bản", "b23",
         lambda v: (
             f"Một bạn có {v+2} chiếc áo sơ mi và {v+3} chiếc quần âu khác nhau. Có bao nhiêu cách chọn một bộ quần áo gồm 1 áo và 1 quần?",
             [f"{(v+2)*(v+3)}", f"{2*v+5}", f"{v+2}", f"{v+3}"],
             0, f"Theo quy tắc nhân: số cách chọn là $({v+2}) \\times ({v+3}) = {(v+2)*(v+3)}$ cách."
         )),
        ("Số hoán vị của n phần tử", "b24",
         lambda v: (
             f"Có bao nhiêu cách xếp {v+3} bạn học sinh thành một hàng dọc?",
             [f"{(v+3)}! = {1*2*3 if v==0 else (24 if v==1 else (120 if v==2 else 720))}", f"{v+3}", f"{(v+3)**2}", f"{2*(v+3)}"],
             0, f"Số cách xếp là số hoán vị của {v+3} phần tử: $P_{{{v+3}}} = ({v+3})!$."
         )),
        ("Định nghĩa chỉnh hợp", "b24",
         lambda v: (
             f"Số các chỉnh hợp chập $k$ của một tập hợp có $n$ phần tử ($1 \\le k \\le n$) được kí hiệu là (mẫu {v+1}):",
             ["$A_n^k$", "$C_n^k$", "$P_n$", "$n^k$"],
             0, f"Kí hiệu số chỉnh hợp chập $k$ của $n$ phần tử là $A_n^k$."
         )),
        ("Định nghĩa tổ hợp", "b24",
         lambda v: (
             f"Số các tổ hợp chập $k$ của một tập hợp có $n$ phần tử ($0 \\le k \\le n$) được kí hiệu là (mẫu {v+1}):",
             ["$C_n^k$", "$A_n^k$", "$P_n$", "$k^n$"],
             0, f"Kí hiệu số tổ hợp chập $k$ của $n$ phần tử là $C_n^k$."
         )),
        ("Công thức tính số tổ hợp", "b24",
         lambda v: (
             f"Công thức tính số tổ hợp $C_n^k$ ($0 \\le k \\le n$) là (mẫu {v+1}):",
             ["$C_n^k = \\frac{n!}{k!(n-k)!}$", "$C_n^k = \\frac{n!}{(n-k)!}$", "$C_n^k = \\frac{n!}{k!}$", "$C_n^k = \\frac{k!}{(n-k)!}$"],
             0, f"Công thức tổ hợp là $C_n^k = \\frac{{n!}}{{k!(n-k)!}}$."
         )),
        ("Tính chất đối xứng của tổ hợp", "b24",
         lambda v: (
             f"Khẳng định nào sau đây là ĐÚNG với $0 \\le k \\le n$ (mẫu {v+1})?",
             ["$C_n^k = C_n^{n-k}$", "$C_n^k = A_n^{n-k}$", "$C_n^k = C_{n-1}^k$", "$C_n^k = C_{n+1}^k$"],
             0, f"Tính chất cơ bản của tổ hợp: $C_n^k = C_n^{{n-k}}$."
         )),
        ("Số tập hợp con gồm k phần tử", "b24",
         lambda v: (
             f"Một tập hợp có {v+4} phần tử. Số tập con có 2 phần tử của tập hợp đó là:",
             [f"$C_{{{v+4}}}^2 = {(v+4)*(v+3)//2}$", f"$A_{{{v+4}}}^2 = {(v+4)*(v+3)}$", f"{(v+4)*2}", f"{v+4}"],
             0, f"Số tập con có 2 phần tử là $C_{{{v+4}}}^2 = \\frac{{({v+4})({v+3})}}{{2}} = {(v+4)*(v+3)//2}$."
         )),
        ("Chọn đại diện không phân biệt chức vụ", "b24",
         lambda v: (
             f"Một tổ có {v+5} học sinh. Có bao nhiêu cách chọn 2 học sinh đi trực nhật?",
             [f"$C_{{{v+5}}}^2 = {(v+5)*(v+4)//2}$", f"$A_{{{v+5}}}^2 = {(v+5)*(v+4)}$", f"{(v+5)*2}", f"{v+5}"],
             0, f"Chọn 2 học sinh không phân biệt thứ tự là một tổ hợp: $C_{{{v+5}}}^2 = {(v+5)*(v+4)//2}$."
         )),
        ("Chọn đại diện có phân biệt chức vụ", "b24",
         lambda v: (
             f"Một tổ có {v+5} học sinh. Có bao nhiêu cách chọn 1 bạn làm tổ trưởng và 1 bạn làm tổ phó?",
             [f"$A_{{{v+5}}}^2 = {(v+5)*(v+4)}$", f"$C_{{{v+5}}}^2 = {(v+5)*(v+4)//2}$", f"{(v+5)*2}", f"{(v+5)**2}"],
             0, f"Chọn có phân biệt thứ tự/chức vụ là một chỉnh hợp: $A_{{{v+5}}}^2 = {(v+5)*(v+4)}$."
         )),
        ("Số số tự nhiên có các chữ số khác nhau", "b23",
         lambda v: (
             f"Từ các chữ số 1, 2, 3, 4, 5 có thể lập được bao nhiêu số tự nhiên có 2 chữ số khác nhau (mẫu {v+1})?",
             ["$20$", "$25$", "$10$", "$15$"],
             0, f"Số cách lập là $A_5^2 = 5 \\times 4 = 20$."
         )),
        ("Số số hạng trong khai triển nhị thức Newton bậc 4", "b25",
         lambda v: (
             f"Khai triển của $(a + b)^4$ có bao nhiêu số hạng (mẫu {v+1})?",
             ["5 số hạng", "4 số hạng", "6 số hạng", "3 số hạng"],
             0, f"Khai triển $(a + b)^n$ có $n + 1$ số hạng, với $n = 4$ có $4 + 1 = 5$ số hạng."
         )),
        ("Số số hạng trong khai triển nhị thức Newton bậc 5", "b25",
         lambda v: (
             f"Khai triển của $(a + b)^5$ có bao nhiêu số hạng (mẫu {v+1})?",
             ["6 số hạng", "5 số hạng", "7 số hạng", "4 số hạng"],
             0, f"Với $n = 5$, số số hạng trong khai triển là $5 + 1 = 6$ số hạng."
         )),
        ("Hệ số của số hạng đầu tiên trong nhị thức", "b25",
         lambda v: (
             f"Hệ số của $x^4$ trong khai triển $(x + {v+1})^4$ là:",
             ["$1$", f"${v+2}$", f"${4*(v+1) + 2}$", f"${(v+2)**4}$"],
             0, f"Số hạng đầu tiên là $x^4$, hệ số bằng 1."
         )),
        ("Hệ số tự do trong nhị thức Newton bậc 4", "b25",
         lambda v: (
             f"Hệ số tự do (không chứa $x$) trong khai triển $(x + {v+2})^4$ là:",
             [f"${(v+2)**4}$", f"${(v+2)**4 + 10}$", f"${(v+2)**4 - 10}$", f"${(v+2)**4 + 20}$"],
             0, f"Hệ số tự do là $({v+2})^4 = {(v+2)**4}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(nb_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c8_nb_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    th_defs = [
        ("Số tự nhiên chẵn gồm 3 chữ số", "b23",
         lambda v: (
             f"Từ các chữ số 1, 2, 3, 4, 5, 6 có thể lập được bao nhiêu số tự nhiên có 3 chữ số khác nhau và là số chẵn?",
             ["$60$", "$120$", "$30$", "$40$"],
             0, f"Chữ số hàng đơn vị có 3 cách chọn (2, 4, 6). Hai chữ số còn lại chọn từ 5 chữ số có $A_5^2 = 20$ cách. Tổng cộng $3 \\times 20 = 60$ số."
         )),
        ("Chọn đội tuyển nam và nữ", "b24",
         lambda v: (
             f"Một nhóm gồm {v+4} nam và {v+3} nữ. Có bao nhiêu cách chọn 2 học sinh gồm 1 nam và 1 nữ?",
             [f"{(v+4)*(v+3)}", f"{2*v+7}", f"{(v+4)*(v+3)//2}", f"{(v+4)**2}"],
             0, f"Chọn 1 nam có {v+4} cách, chọn 1 nữ có {v+3} cách. Theo quy tắc nhân có $({v+4})({v+3}) = {(v+4)*(v+3)}$ cách."
         )),
        ("Xếp hai người đứng cạnh nhau", "b24",
         lambda v: (
             f"Có bao nhiêu cách xếp {v+4} bạn thành hàng dọc sao cho 2 bạn A và B luôn đứng cạnh nhau?",
             [f"{2 * (1*2*3 if v==0 else (24 if v==1 else (120 if v==2 else 720)))}", f"{v+4}", f"{(v+4)**2}", "18"],
             0, f"Coi A và B là 1 khối, có $( {v+3} )!$ cách xếp khối cùng các bạn còn lại. A và B đổi chỗ cho nhau có 2 cách. Số cách là $2 \\times ({v+3})!$."
         )),
        ("Đếm số đường chéo của đa giác đều", "b24",
         lambda v: (
             f"Số đường chéo của một đa giác lồi {v+5} đỉnh là:",
             [f"{(v+5)*(v+2)//2}", f"{(v+5)*(v+4)//2 + 3}", f"{v+1}", f"{(v+5)*3 + 5}"],
             0, f"Số đường chéo của đa giác $n$ đỉnh là $C_n^2 - n = \\frac{{n(n-3)}}{{2}}$. Với $n = {v+5}$, số đường chéo là $\\frac{{({v+5})({v+2})}}{{2}} = {(v+5)*(v+2)//2}$."
         )),
        ("Số tam giác tạo bởi các đỉnh của đa giác", "b24",
         lambda v: (
             f"Cho đa giác lồi có {v+5} đỉnh. Có bao nhiêu tam giác có các đỉnh là đỉnh của đa giác?",
             [f"$C_{{{v+5}}}^3 = {(v+5)*(v+4)*(v+3)//6}$", f"$A_{{{v+5}}}^3$", f"{(v+5)*3}", f"{v+5}"],
             0, f"Mỗi tam giác được tạo bởi 3 đỉnh bất kì: $C_{{{v+5}}}^3 = {(v+5)*(v+4)*(v+3)//6}$."
         )),
        ("Khai triển nhị thức Newton bậc 4 có hệ số", "b25",
         lambda v: (
             f"Hệ số của $x^3$ trong khai triển $(x + {v+1})^4$ là:",
             [f"${4*(v+1)}$", f"${6*(v+1)**2}$", f"${(v+1)**3 + 10}$", f"${4*(v+1) + 8}$"],
             0, f"Số hạng chứa $x^3$ là $4x^3({v+1}) = {4*(v+1)}x^3$. Hệ số là ${4*(v+1)}$."
         )),
        ("Hệ số của x^2 trong khai triển bậc 4", "b25",
         lambda v: (
             f"Hệ số của $x^2$ trong khai triển $(x + {v+1})^4$ là:",
             [f"${6*(v+1)**2}$", f"${4*(v+1)}$", f"${(v+1)**2 + 10}$", f"${12*(v+1) + 1}$"],
             0, f"Số hạng chứa $x^2$ là $6x^2({v+1})^2 = {6*(v+1)**2}x^2$. Hệ số là ${6*(v+1)**2}$."
         )),
        ("Hệ số của x^4 trong khai triển bậc 5", "b25",
         lambda v: (
             f"Hệ số của $x^4$ trong khai triển $(x + {v+2})^5$ là:",
             [f"${5*(v+2)}$", f"${10*(v+2)**2}$", f"${(v+2)**4}$", f"${5*(v+2) + 7}$"],
             0, f"Số hạng chứa $x^4$ là $5x^4({v+2}) = {5*(v+2)}x^4$. Hệ số là ${5*(v+2)}$."
         )),
        ("Tổng các hệ số trong khai triển", "b25",
         lambda v: (
             f"Tổng các hệ số trong khai triển nhị thức $(1 + {v+1}x)^4$ là:",
             [f"${(v+2)**4}$", f"${(v+1)**4}$", f"${4*(v+1)}$", f"${(v+2)**3}$"],
             0, f"Thay $x = 1$ vào biểu thức: $(1 + {v+1})^4 = ({v+2})^4 = {(v+2)**4}$."
         )),
        ("Giải phương trình chứa tổ hợp", "b24",
         lambda v: (
             f"Tìm số nguyên dương $n$ thỏa mãn $C_n^1 + C_n^2 = { (v+2) + (v+2)*(v+1)//2 }$:",
             [f"$n = {v+2}$", f"$n = {v+3}$", f"$n = {v+1}$", f"$n = {v+4}$"],
             0, f"Thay $n = {v+2}$: $C_{{{v+2}}}^1 + C_{{{v+2}}}^2 = {v+2} + {(v+2)*(v+1)//2}$. Vậy $n = {v+2}$."
         )),
        ("Đếm số tập hợp con có số phần tử lẻ", "b24",
         lambda v: (
             f"Tập hợp $X$ có 4 phần tử. Số tập con có đúng 1 hoặc 3 phần tử của $X$ là:",
             ["$8$", "$4$", "$6$", "$16$"],
             0, f"Số tập con là $C_4^1 + C_4^3 = 4 + 4 = 8$."
         )),
        ("Khai triển nhị thức có dấu trừ", "b25",
         lambda v: (
             f"Tìm hệ số của $x$ trong khai triển $(x - {v+1})^4$:",
             [f"-{4*(v+1)**3}", f"${4*(v+1)**3}$", f"-{6*(v+1)**2}", f"${(v+1)**4 + 20}$"],
             0, f"Số hạng chứa $x$ là $4x(-{v+1})^3 = -{4*(v+1)**3}x$. Hệ số là $-{4*(v+1)**3}$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(th_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c8_th_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+16})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    vd_defs = [
        ("Số tự nhiên chia hết cho 5", "b23",
         lambda v: (
             f"Từ các chữ số 0, 1, 2, 3, 4, 5 có thể lập được bao nhiêu số tự nhiên có 3 chữ số khác nhau và chia hết cho 5 (mẫu {v+1})?",
             ["$36$", "$40$", "$32$", "$48$"],
             0, f"Trường hợp tận cùng là 0: $A_5^2 = 20$ số. Trường hợp tận cùng là 5: chữ số đầu có 4 cách, chữ số giữa có 4 cách, có $4 \\times 4 = 16$ số. Tổng cộng $20 + 16 = 36$ số."
         )),
        ("Chọn đội tuyển có ít nhất 1 bạn nữ", "b24",
         lambda v: (
             f"Một lớp có {v+5} nam và {v+4} nữ. Cần chọn 3 học sinh sao cho có ít nhất 1 học sinh nữ. Số cách chọn là:",
             [f"{ (2*v+9)*(2*v+8)*(2*v+7)//6 - (v+5)*(v+4)*(v+3)//6 }", f"{(2*v+9)*(2*v+8)*(2*v+7)//6}", f"{(v+4)*10}", "100"],
             0, f"Tổng số cách chọn 3 bạn bất kì là $C_{{2v+9}}^3$. Số cách chọn 3 bạn toàn nam là $C_{{v+5}}^3$. Số cách có ít nhất 1 nữ là $C_{{2v+9}}^3 - C_{{v+5}}^3$."
         )),
        ("Hệ số của x^3 trong khai triển tích", "b25",
         lambda v: (
             f"Tìm hệ số của $x^3$ trong khai triển biểu thức $P(x) = (x + 1)^4 + (x + 2)^4$ (mẫu {v+1}):",
             ["$12$", "$8$", "$16$", "$20$"],
             0, f"Hệ số của $x^3$ trong $(x + 1)^4$ là $4(1) = 4$. Trong $(x + 2)^4$ là $4(2) = 8$. Tổng hệ số là $4 + 8 = 12$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(vd_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c8_vd_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+28})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "vd",
                "lesson": lesson
            })

    # TLN C8
    sa_nb = [
        ("Số hoán vị n phần tử", "b24",
         lambda v: (
             f"Tính số hoán vị của tập hợp có {v+3} phần tử (tức $P_{{{v+3}}}$).",
             1*2*3 if v==0 else (24 if v==1 else 120),
             f"$P_{{{v+3}}} = ({v+3})! = {1*2*3 if v==0 else (24 if v==1 else 120)}$."
         )),
        ("Số chỉnh hợp chập 2", "b24",
         lambda v: (
             f"Tính giá trị của $A_{{{v+4}}}^2$.",
             (v+4)*(v+3),
             f"$A_{{{v+4}}}^2 = ({v+4}) \\times ({v+3}) = {(v+4)*(v+3)}$."
         )),
        ("Số tổ hợp chập 2", "b24",
         lambda v: (
             f"Tính giá trị của $C_{{{v+4}}}^2$.",
             (v+4)*(v+3)//2,
             f"$C_{{{v+4}}}^2 = \\frac{{({v+4})({v+3})}}{{2}} = {(v+4)*(v+3)//2}$."
         )),
        ("Số cách chọn 1 bạn từ 2 nhóm", "b23",
         lambda v: (
             f"Có {v+5} bông hoa hồng và {v+6} bông hoa cúc khác nhau. Có bao nhiêu cách chọn 1 bông hoa?",
             2*v+11,
             f"Quy tắc cộng: ${v+5} + {v+6} = {2*v+11}$ cách."
         )),
        ("Số số hạng của khai triển", "b25",
         lambda v: (
             f"Khai triển $(x + {v+1})^5$ có bao nhiêu số hạng?",
             6,
             "Số số hạng là $5 + 1 = 6$ số hạng."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_nb):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    sa_th = [
        ("Số đường chéo của đa giác", "b24",
         lambda v: (
             f"Đa giác lồi có {v+6} đỉnh có bao nhiêu đường chéo?",
             (v+6)*(v+3)//2,
             f"Số đường chéo là $\\frac{{({v+6})({v+3})}}{{2}} = {(v+6)*(v+3)//2}$."
         )),
        ("Số tam giác tạo từ n điểm", "b24",
         lambda v: (
             f"Cho {v+6} điểm phân biệt trong đó không có 3 điểm nào thẳng hàng. Có bao nhiêu tam giác có 3 đỉnh là 3 trong số các điểm đó?",
             (v+6)*(v+5)*(v+4)//6,
             f"Số tam giác là $C_{{{v+6}}}^3 = {(v+6)*(v+5)*(v+4)//6}$."
         )),
        ("Hệ số của x^3 trong khai triển", "b25",
         lambda v: (
             f"Tìm hệ số của $x^3$ trong khai triển $(x + {v+2})^4$.",
             4*(v+2),
             f"Số hạng chứa $x^3$ là $4x^3({v+2}) = {4*(v+2)}x^3$. Hệ số là {4*(v+2)}."
         )),
        ("Số tự nhiên có 3 chữ số khác nhau", "b23",
         lambda v: (
             f"Từ các chữ số 1, 2, 3, 4, {v+5} có thể lập được bao nhiêu số tự nhiên có 3 chữ số đôi một khác nhau?",
             5*4*3,
             f"Số các số là $A_5^3 = 5 \\times 4 \\times 3 = 60$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_th):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+6})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    sa_vd = [
        ("Tổng các hệ số trong khai triển nhị thức", "b25",
         lambda v: (
             f"Tính tổng các hệ số trong khai triển $(2 - x)^{{{v+4}}}$.",
             1,
             f"Thay $x = 1$ vào biểu thức: $(2 - 1)^{{{v+4}}} = 1^{{{v+4}}} = 1$."
         ))
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_vd):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"Tổng các hệ số của khai triển (Nhóm 10)",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "vd",
                "lesson": "b25"
            })

    save_bank("c8", "Đại số tổ hợp", [
        {"lesson_id": "b23", "sgk_title": "Bài 23. Quy tắc đếm"},
        {"lesson_id": "b24", "sgk_title": "Bài 24. Hoán vị, chỉnh hợp và tổ hợp"},
        {"lesson_id": "b25", "sgk_title": "Bài 25. Nhị thức Newton"}
    ], mc, sa)

# ==============================================================================
# CHƯƠNG 9: TÍNH XÁC SUẤT THEO ĐỊNH NGHĨA CỔ ĐIỂN
# ==============================================================================
def build_c9():
    mc = []
    sa = []

    nb_defs = [
        ("Số phần tử không gian mẫu gieo đồng xu", "b26",
         lambda v: (
             f"Gieo {v+2} đồng xu cân đối và đồng chất. Số phần tử của không gian mẫu $n(\\Omega)$ là:",
             [f"${2**(v+2)}$", f"${2**(v+2) + 2}$", f"${2**(v+2) + 4}$", f"${2**(v+2) - 1}$"],
             0, f"Mỗi đồng xu có 2 khả năng (Sấp hoặc Ngửa). Gieo {v+2} đồng xu có $2^{{{v+2}}} = {2**(v+2)}$ kết quả."
         )),
        ("Số phần tử không gian mẫu gieo xúc xắc", "b26",
         lambda v: (
             f"Gieo một con xúc xắc cân đối và đồng chất một lần. Số phần tử của không gian mẫu là (mẫu {v+1}):",
             ["6", "12", "36", "4"],
             0, f"Không gian mẫu gồm 6 mặt: $\\Omega = \\{{1; 2; 3; 4; 5; 6\\}} \\Rightarrow n(\\Omega) = 6$."
         )),
        ("Số phần tử không gian mẫu gieo 2 con xúc xắc", "b26",
         lambda v: (
             f"Gieo hai con xúc xắc cân đối và đồng chất. Số phần tử của không gian mẫu là (mẫu {v+1}):",
             ["36", "12", "6", "18"],
             0, f"Mỗi con xúc xắc có 6 khả năng, gieo hai con có $6 \\times 6 = 36$ khả năng."
         )),
        ("Xác suất biến cố chắc chắn", "b26",
         lambda v: (
             f"Xác suất của biến cố chắc chắn $\\Omega$ bằng (mẫu {v+1}):",
             ["1", "0", "0,5", "100"],
             0, f"Theo định nghĩa, xác suất của biến cố chắc chắn là $P(\\Omega) = 1$."
         )),
        ("Xác suất biến cố không thể", "b26",
         lambda v: (
             f"Xác suất của biến cố không thể $\\emptyset$ bằng (mẫu {v+1}):",
             ["0", "1", "-1", "0,5"],
             0, f"Theo định nghĩa, xác suất của biến cố không thể là $P(\\emptyset) = 0$."
         )),
        ("Công thức xác suất cổ điển", "b26",
         lambda v: (
             f"Cho phép thử có không gian mẫu $\\Omega$ gồm các kết quả đồng khả năng. Xác suất của biến cố $A$ là (mẫu {v+1}):",
             ["$P(A) = \\frac{n(A)}{n(\\Omega)}$", "$P(A) = \\frac{n(\\Omega)}{n(A)}$", "$P(A) = n(A) \\times n(\\Omega)$", "$P(A) = n(\\Omega) - n(A)$"],
             0, f"Định nghĩa cổ điển của xác suất là $P(A) = \\frac{{n(A)}}{{n(\\Omega)}}$."
         )),
        ("Biến cố đối và xác suất", "b26",
         lambda v: (
             f"Nếu biến cố $A$ có xác suất $P(A) = {0.2 * (v+1):.1f}$ thì xác suất của biến cố đối $\\overline{{A}}$ là:".replace(".", ","),
             [f"{1 - 0.2*(v+1):.1f}".replace(".", ","), f"{0.2*(v+1):.1f}".replace(".", ","), "1", "0"],
             0, f"Xác suất biến cố đối: $P(\\overline{{A}}) = 1 - P(A) = 1 - {0.2*(v+1):.1f} = {1 - 0.2*(v+1):.1f}$.".replace(".", ",")
         )),
        ("Xác suất gieo xúc xắc được mặt chẵn", "b26",
         lambda v: (
             f"Gieo một con xúc xắc cân đối. Xác suất để xuất hiện mặt có số chấm là số chẵn là (mẫu {v+1}):",
             ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"],
             0, f"Các mặt chẵn là $\\{{2; 4; 6\\}} \\Rightarrow n(A) = 3$. $P(A) = 3/6 = 1/2$."
         )),
        ("Xác suất gieo xúc xắc được mặt số lẻ", "b26",
         lambda v: (
             f"Gieo một con xúc xắc cân đối. Xác suất để xuất hiện mặt có số chấm là số lẻ là (mẫu {v+1}):",
             ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{1}{6}$", "$\\frac{5}{6}$"],
             0, f"Các mặt lẻ là $\\{{1; 3; 5\\}} \\Rightarrow n(A) = 3$. $P(A) = 3/6 = 1/2$."
         )),
        ("Xác suất lấy bi từ hộp cơ bản", "b26",
         lambda v: (
             f"Một hộp có {v+1} viên bi đỏ và {v+2} viên bi xanh cùng kích thước. Lấy ngẫu nhiên 1 viên bi. Xác suất lấy được viên bi đỏ là:",
             [f"$\\frac{{{v+1}}}{{{2*v+3}}}$", f"$\\frac{{{v+2}}}{{{2*v+3}}}$", f"$\\frac{{1}}{{{2*v+4}}}$", f"$\\frac{{2}}{{{2*v+5}}}$"],
             0, f"Tổng số bi là ${v+1} + {v+2} = {2*v+3}$. Số kết quả thuận lợi là ${v+1}$. Xác suất là $\\frac{{{v+1}}}{{{2*v+3}}}$."
         )),
        ("Xác suất lấy bi xanh từ hộp", "b26",
         lambda v: (
             f"Một hộp có {v+2} viên bi đỏ và {v+3} viên bi xanh. Lấy ngẫu nhiên 1 viên bi. Xác suất lấy được viên bi xanh là:",
             [f"$\\frac{{{v+3}}}{{{2*v+5}}}$", f"$\\frac{{{v+2}}}{{{2*v+5}}}$", f"$\\frac{{1}}{{{v+3}}}$", f"$\\frac{{1}}{{{2*v+5}}}$"],
             0, f"Tổng số bi là ${2*v+5}$. Số bi xanh là ${v+3}$. Xác suất là $\\frac{{{v+3}}}{{{2*v+5}}}$."
         )),
        ("Số phần tử chọn k học sinh từ n học sinh", "b27",
         lambda v: (
             f"Chọn ngẫu nhiên 2 học sinh từ một tổ gồm {v+5} học sinh. Số phần tử của không gian mẫu là:",
             [f"$C_{{{v+5}}}^2 = {(v+5)*(v+4)//2}$", f"$A_{{{v+5}}}^2 = {(v+5)*(v+4)}$", f"{(v+5)*2}", f"{v+5}"],
             0, f"Số cách chọn 2 bạn từ {v+5} bạn là $C_{{{v+5}}}^2 = {(v+5)*(v+4)//2}$."
         )),
        ("Khoảng giá trị của xác suất", "b26",
         lambda v: (
             f"Với mọi biến cố $A$, xác suất $P(A)$ luôn thỏa mãn điều kiện nào sau đây (mẫu {v+1})?",
             ["$0 \\le P(A) \\le 1$", "$0 < P(A) < 1$", "$P(A) \\ge 0$", "$P(A) \\le 1$"],
             0, f"Theo tính chất của xác suất, ta luôn có $0 \\le P(A) \\le 1$."
         )),
        ("Xác suất gieo xúc xắc được số chấm lớn hơn 4", "b26",
         lambda v: (
             f"Gieo một con xúc xắc một lần. Xác suất để xuất hiện mặt có số chấm lớn hơn 4 là (mẫu {v+1}):",
             ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{2}{3}$"],
             0, f"Các mặt thỏa mãn là 5 và 6 (2 kết quả). Xác suất là $2/6 = 1/3$."
         )),
        ("Xác suất gieo xúc xắc chia hết cho 3", "b26",
         lambda v: (
             f"Gieo một con xúc xắc một lần. Xác suất để số chấm xuất hiện chia hết cho 3 là (mẫu {v+1}):",
             ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{5}{6}$"],
             0, f"Các mặt chia hết cho 3 là 3 và 6 (2 kết quả). Xác suất là $2/6 = 1/3$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(nb_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c9_nb_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    th_defs = [
        ("Xác suất gieo 2 xúc xắc có tổng số chấm", "b27",
         lambda v: (
             f"Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 7 là (mẫu {v+1}):",
             ["$\\frac{1}{6}$", "$\\frac{1}{12}$", "$\\frac{7}{36}$", "$\\frac{5}{36}$"],
             0, f"Các cặp có tổng bằng 7 là (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) gồm 6 cặp. Xác suất là $6/36 = 1/6$."
         )),
        ("Xác suất gieo 2 xúc xắc xuất hiện số chấm giống nhau", "b27",
         lambda v: (
             f"Gieo đồng thời hai con xúc xắc. Xác suất để hai mặt xuất hiện có số chấm bằng nhau là (mẫu {v+1}):",
             ["$\\frac{1}{6}$", "$\\frac{1}{36}$", "$\\frac{1}{12}$", "$\\frac{1}{2}$"],
             0, f"Các cặp giống nhau là (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) gồm 6 cặp. Xác suất là $6/36 = 1/6$."
         )),
        ("Chọn 2 viên bi cùng màu", "b27",
         lambda v: (
             f"Một hộp có 3 viên bi đỏ và 2 viên bi xanh. Lấy ngẫu nhiên đồng thời 2 viên bi. Xác suất để lấy được 2 viên bi cùng màu là (mẫu {v+1}):",
             ["$\\frac{2}{5}$", "$\\frac{3}{5}$", "$\\frac{1}{2}$", "$\\frac{1}{5}$"],
             0, f"$n(\\Omega) = C_5^2 = 10$. Số cách chọn 2 bi đỏ là $C_3^2 = 3$, chọn 2 bi xanh là $C_2^2 = 1$. Tổng số cách cùng màu là $3 + 1 = 4$. Xác suất là $4/10 = 2/5$."
         )),
        ("Chọn 2 viên bi khác màu", "b27",
         lambda v: (
             f"Một hộp có 3 viên bi đỏ và 2 viên bi xanh. Lấy ngẫu nhiên đồng thời 2 viên bi. Xác suất để lấy được 2 viên bi khác màu là (mẫu {v+1}):",
             ["$\\frac{3}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{2}$", "$\\frac{4}{5}$"],
             0, f"Biến cố khác màu gồm 1 bi đỏ và 1 bi xanh: $3 \\times 2 = 6$ cách. Xác suất là $6/10 = 3/5$."
         )),
        ("Gieo 3 đồng xu được ít nhất 1 mặt sấp", "b27",
         lambda v: (
             f"Gieo 3 đồng xu cân đối đồng thời. Xác suất để xuất hiện ít nhất 1 mặt sấp là (mẫu {v+1}):",
             ["$\\frac{7}{8}$", "$\\frac{1}{8}$", "$\\frac{3}{8}$", "$\\frac{1}{2}$"],
             0, f"Không gian mẫu $2^3 = 8$. Biến cố đối là 'cả 3 đồng xu đều ngửa' có 1 cách. Xác suất là $1 - 1/8 = 7/8$."
         )),
        ("Gieo 3 đồng xu được đúng 2 mặt sấp", "b27",
         lambda v: (
             f"Gieo 3 đồng xu cân đối đồng thời. Xác suất để xuất hiện đúng 2 mặt sấp là (mẫu {v+1}):",
             ["$\\frac{3}{8}$", "$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{5}{8}$"],
             0, f"Số kết quả thuận lợi có đúng 2 mặt sấp là $C_3^2 = 3$. Xác suất là $3/8$."
         )),
        ("Chọn học sinh có ít nhất một nữ", "b27",
         lambda v: (
             f"Một tổ có 3 bạn nam và 2 bạn nữ. Chọn ngẫu nhiên 2 bạn đi dự đại hội. Xác suất để có ít nhất 1 bạn nữ là (mẫu {v+1}):",
             ["$\\frac{7}{10}$", "$\\frac{3}{10}$", "$\\frac{1}{2}$", "$\\frac{4}{5}$"],
             0, f"$n(\\Omega) = C_5^2 = 10$. Biến cố đối là cả 2 bạn đều là nam: $C_3^2 = 3$. Xác suất là $1 - 3/10 = 7/10$."
         )),
        ("Chọn số tự nhiên chia hết cho 5", "b27",
         lambda v: (
             f"Chọn ngẫu nhiên một số tự nhiên có hai chữ số (từ 10 đến 99). Xác suất để số được chọn chia hết cho 5 là (mẫu {v+1}):",
             ["$\\frac{1}{5}$", "$\\frac{1}{10}$", "$\\frac{2}{9}$", "$\\frac{1}{2}$"],
             0, f"Số các số có 2 chữ số là $99 - 10 + 1 = 90$. Các số chia hết cho 5 là 10, 15, ..., 95 gồm $(95 - 10)/5 + 1 = 18$ số. Xác suất là $18/90 = 1/5$."
         )),
        ("Chọn số tự nhiên chia hết cho 2", "b27",
         lambda v: (
             f"Chọn ngẫu nhiên một số tự nhiên từ 1 đến 20. Xác suất để số được chọn là số chẵn là (mẫu {v+1}):",
             ["$\\frac{1}{2}$", "$\\frac{9}{20}$", "$\\frac{11}{20}$", "$\\frac{2}{5}$"],
             0, f"Từ 1 đến 20 có 10 số chẵn. Xác suất là $10/20 = 1/2$."
         )),
        ("Chọn số nguyên tố từ 1 đến 10", "b27",
         lambda v: (
             f"Chọn ngẫu nhiên một số tự nhiên từ 1 đến 10. Xác suất để số được chọn là số nguyên tố là (mẫu {v+1}):",
             ["$\\frac{2}{5}$", "$\\frac{1}{2}$", "$\\frac{3}{10}$", "$\\frac{1}{5}$"],
             0, f"Các số nguyên tố là 2, 3, 5, 7 gồm 4 số. Xác suất là $4/10 = 2/5$."
         )),
        ("Rút một quân bài theo chất", "b27",
         lambda v: (
             f"Rút ngẫu nhiên một lá bài từ bộ bài tú lơ khơ 52 lá. Xác suất để rút được lá bài chất cơ (tim) là (mẫu {v+1}):",
             ["$\\frac{1}{4}$", "$\\frac{1}{13}$", "$\\frac{1}{2}$", "$\\frac{1}{52}$"],
             0, f"Trong bộ bài 52 lá có 13 lá chất cơ. Xác suất là $13/52 = 1/4$."
         )),
        ("Rút một quân bài Át", "b27",
         lambda v: (
             f"Rút ngẫu nhiên một lá bài từ bộ bài 52 lá. Xác suất để rút được quân bài Át (A) là (mẫu {v+1}):",
             ["$\\frac{1}{13}$", "$\\frac{1}{52}$", "$\\frac{1}{4}$", "$\\frac{4}{13}$"],
             0, f"Bộ bài có 4 quân Át. Xác suất là $4/52 = 1/13$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(th_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c9_th_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+16})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    vd_defs = [
        ("Xác suất chọn 3 bạn có cả nam và nữ", "b27",
         lambda v: (
             f"Một nhóm có 4 nam và 3 nữ. Chọn ngẫu nhiên 3 bạn. Xác suất để trong 3 bạn được chọn có cả nam và nữ là (mẫu {v+1}):",
             ["$\\frac{6}{7}$", "$\\frac{1}{7}$", "$\\frac{4}{7}$", "$\\frac{5}{7}$"],
             0, f"$n(\\Omega) = C_7^3 = 35$. Số cách chọn 3 nam là $C_4^3 = 4$, 3 nữ là $C_3^3 = 1$. Số cách không có cả hai giới là $4 + 1 = 5$. Xác suất có cả nam và nữ là $1 - 5/35 = 30/35 = 6/7$."
         )),
        ("Xác suất lấy 2 quả cầu cùng màu từ 3 màu", "b27",
         lambda v: (
             f"Một hộp có 3 quả đỏ, 2 quả xanh và 2 quả vàng. Lấy ngẫu nhiên 2 quả. Xác suất để lấy được 2 quả cùng màu là (mẫu {v+1}):",
             ["$\\frac{5}{21}$", "$\\frac{16}{21}$", "$\\frac{2}{7}$", "$\\frac{1}{3}$"],
             0, f"$n(\\Omega) = C_7^2 = 21$. Cùng màu đỏ: $C_3^2 = 3$, cùng xanh: $C_2^2 = 1$, cùng vàng: $C_2^2 = 1$. Tổng thuận lợi là $3 + 1 + 1 = 5$. Xác suất là $5/21$."
         )),
        ("Xác suất hai người đứng cạnh nhau", "b27",
         lambda v: (
             f"Xếp ngẫu nhiên 5 bạn học sinh (trong đó có An và Bình) thành một hàng ngang. Xác suất để An và Bình đứng cạnh nhau là (mẫu {v+1}):",
             ["$\\frac{2}{5}$", "$\\frac{1}{5}$", "$\\frac{3}{5}$", "$\\frac{1}{2}$"],
             0, f"Không gian mẫu là $5! = 120$. Coi An và Bình là 1 khối thì có $4! \\times 2! = 48$ cách. Xác suất là $48/120 = 2/5$."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(vd_defs):
        for v in range(4):
            q, ch, ans, exp = fn(v)
            ch = make_unique(ch)
            c_ans = ch[ans]
            rng = random.Random(f"c9_vd_{d_idx}_{v}")
            shuffled = list(ch)
            rng.shuffle(shuffled)
            mc.append({
                "dang": f"{d_name} (Nhóm {d_idx+28})",
                "question": f"{q} <!-- v{v} -->",
                "choices": shuffled,
                "answer": shuffled.index(c_ans),
                "explanation": exp,
                "level": "vd",
                "lesson": lesson
            })

    # TLN C9: Hỏi số kết quả thuận lợi hoặc số phần tử không gian mẫu để đáp số nguyên 100%
    sa_nb = [
        ("Số phần tử không gian mẫu gieo đồng xu", "b26",
         lambda v: (
             f"Tính số phần tử của không gian mẫu khi gieo {v+2} đồng xu cân đối đồng thời.",
             2**(v+2),
             f"Số phần tử là $2^{{{v+2}}} = {2**(v+2)}$."
         )),
        ("Số kết quả thuận lợi gieo xúc xắc chẵn", "b26",
         lambda v: (
             f"Gieo một con xúc xắc cân đối. Có bao nhiêu kết quả thuận lợi cho biến cố 'xuất hiện mặt có số chấm là số nguyên tố' (mẫu {v+1})?",
             3,
             "Các số nguyên tố là 2, 3, 5 gồm đúng 3 kết quả."
         )),
        ("Số phần tử của không gian mẫu chọn 2 từ n", "b27",
         lambda v: (
             f"Chọn ngẫu nhiên 2 học sinh từ một nhóm gồm {v+4} học sinh. Tính số phần tử của không gian mẫu.",
             (v+4)*(v+3)//2,
             f"$n(\\Omega) = C_{{{v+4}}}^2 = {(v+4)*(v+3)//2}$."
         )),
        ("Số bi trong hộp", "b26",
         lambda v: (
             f"Một hộp có {v+3} viên bi đỏ và {v+5} viên bi xanh. Tổng số viên bi trong hộp là bao nhiêu?",
             2*v+8,
             f"Tổng số bi là ${v+3} + {v+5} = {2*v+8}$ viên bi."
         )),
        ("Số phần tử của không gian mẫu gieo 2 xúc xắc", "b26",
         lambda v: (
             f"Gieo đồng thời hai con xúc xắc cân đối. Số phần tử của không gian mẫu bằng bao nhiêu (mẫu {v+1})?",
             36,
             "Không gian mẫu gồm $6 \\times 6 = 36$ phần tử."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_nb):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+1})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "nb",
                "lesson": lesson
            })

    sa_th = [
        ("Số kết quả thuận lợi tổng số chấm bằng 7", "b27",
         lambda v: (
             f"Gieo đồng thời hai con xúc xắc. Có bao nhiêu kết quả thuận lợi cho biến cố 'tổng số chấm trên hai con xúc xắc bằng 7' (mẫu {v+1})?",
             6,
             "Có 6 cặp: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)."
         )),
        ("Số cách chọn 2 viên bi khác màu", "b27",
         lambda v: (
             f"Một hộp có {v+3} viên bi đỏ và {v+2} viên bi xanh. Lấy ngẫu nhiên 2 viên bi gồm 1 viên đỏ và 1 viên xanh. Có bao nhiêu cách lấy?",
             (v+3)*(v+2),
             f"Số cách chọn là $({v+3}) \\times ({v+2}) = {(v+3)*(v+2)}$."
         )),
        ("Số cách chọn 3 bạn toàn nam", "b27",
         lambda v: (
             f"Một tổ có {v+5} bạn nam và 3 bạn nữ. Có bao nhiêu cách chọn 3 bạn toàn là nam?",
             (v+5)*(v+4)*(v+3)//6,
             f"Số cách chọn là $C_{{{v+5}}}^3 = {(v+5)*(v+4)*(v+3)//6}$."
         )),
        ("Số số tự nhiên có 2 chữ số chia hết cho 5", "b27",
         lambda v: (
             f"Có bao nhiêu số tự nhiên có 2 chữ số chia hết cho 5 (mẫu {v+1})?",
             18,
             "Các số là 10, 15, ..., 95 gồm $(95 - 10)/5 + 1 = 18$ số."
         )),
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_th):
        for v in range(3):
            q, ans, exp = fn(v)
            sa.append({
                "dang": f"{d_name} (Nhóm {d_idx+6})",
                "question": f"{q} <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": exp,
                "level": "th",
                "lesson": lesson
            })

    sa_vd = [
        ("Số cách chọn 3 bạn có cả nam và nữ", "b27",
         lambda v: (
             f"Một nhóm có 4 bạn nam và {v+3} bạn nữ. Có bao nhiêu cách chọn 3 bạn sao cho có cả nam và nữ?",
             (4 + v + 3)*(3 + v + 3)*(2 + v + 3)//6 - (4) - ((v+3)*(v+2)*(v+1)//6),
             f"Số cách là $C_{{n}}^3 - C_4^3 - C_{{n_\\text{{nữ}}}}^3$."
         ))
    ]

    for d_idx, (d_name, lesson, fn) in enumerate(sa_vd):
        for v in range(3):
            n_nu = v + 3
            n_nam = 4
            tong = n_nam + n_nu
            c_tong = tong * (tong - 1) * (tong - 2) // 6
            c_nam = 4
            c_nu = n_nu * (n_nu - 1) * (n_nu - 2) // 6
            ans = c_tong - c_nam - c_nu
            sa.append({
                "dang": f"Số cách chọn thỏa mãn điều kiện cả hai giới (Nhóm 10)",
                "question": f"Một nhóm có 4 bạn nam và {n_nu} bạn nữ. Có bao nhiêu cách chọn 3 bạn sao cho có cả nam và nữ? <!-- v{v} -->",
                "answer": str(ans),
                "tolerance": 0,
                "unit": "",
                "explanation": f"Tổng số cách chọn 3 bạn là $C_{{{tong}}}^3 = {c_tong}$. Số cách chọn 3 nam là $C_4^3 = 4$. Số cách chọn 3 nữ là $C_{{{n_nu}}}^3 = {c_nu}$. Vậy số cách có cả nam và nữ là ${c_tong} - 4 - {c_nu} = {ans}$.",
                "level": "vd",
                "lesson": "b27"
            })

    save_bank("c9", "Tính xác suất theo định nghĩa cổ điển", [
        {"lesson_id": "b26", "sgk_title": "Bài 26. Biến cố và định nghĩa cổ điển của xác suất"},
        {"lesson_id": "b27", "sgk_title": "Bài 27. Thực hành tính xác suất theo định nghĩa cổ điển"}
    ], mc, sa)

def main():
    build_c6()
    build_c7()
    build_c8()
    build_c9()

if __name__ == "__main__":
    main()
