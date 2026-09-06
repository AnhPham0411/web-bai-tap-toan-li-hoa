# -*- coding: utf-8 -*-
import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK_DIR = os.path.join(BASE_DIR, "scripts", "bank")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_bank(subject, chapter_id, sgk_title, sgk_lessons, mc, sa):
    data = {
        "sgk_chapter_title": sgk_title,
        "sgk_lessons": sgk_lessons,
        "sources": ["Sinh tự động bám sát SGK"],
        "mc": mc,
        "short": sa
    }
    filepath = os.path.join(BANK_DIR, f"{subject}_{chapter_id}.json")
    ensure_dir(os.path.dirname(filepath))
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def make_unique(choices):
    seen = set()
    res = []
    for c in choices:
        c_str = str(c)
        while c_str in seen:
            c_str += "\u200b"
        seen.add(c_str)
        res.append(c_str)
    return res

def gen_variant_mc(rng, d_idx, c_id, v_idx):
    t_idx = d_idx if d_idx <= 24 else d_idx - 6

    if c_id == "c1":
        if t_idx <= 6:
            if t_idx == 1:
                val = v_idx + 2
                return ("Nhận biết mệnh đề", "Câu nào sau đây là một mệnh đề?", [f"Số {val} là số lẻ.", "Trời hôm nay đẹp quá!", "Bạn ăn cơm chưa?", "Hãy làm bài tập đi!"], 0, "Mệnh đề là câu khẳng định.")
            elif t_idx == 2:
                val = v_idx + 3
                return ("Xét tính đúng sai mệnh đề", "Mệnh đề nào sau đây là ĐÚNG?", [f"{val}^2 = {val**2}", f"{val} > {val+1}", f"{val} < 0", f"{val} + 1 = {val}"], 0, "Tính bình phương.")
            elif t_idx == 3:
                val = v_idx + 1
                return ("Phủ định mệnh đề chứa mọi", f"Phủ định của mệnh đề '$\\forall x \\in \\mathbb{{R}}, x^2 + {val} > 0$' là:", [f"$\\exists x \\in \\mathbb{{R}}, x^2 + {val} \\le 0$", f"$\\forall x \\in \\mathbb{{R}}, x^2 + {val} \\le 0$", f"$\\exists x \\in \\mathbb{{R}}, x^2 + {val} < 0$", f"$\\exists x \\in \\mathbb{{R}}, x^2 + {val} = 0$"], 0, "Phủ định của mọi là tồn tại, của > là <=.")
            elif t_idx == 4:
                val = v_idx + 10
                return ("Mệnh đề kéo theo", f"Phát biểu mệnh đề $P \\Rightarrow Q$ với $P$: 'Tam giác vuông', $Q$: 'Tam giác có 1 góc $90^\\circ$'?", ["Nếu tam giác vuông thì nó có 1 góc bằng $90^\\circ$.", "Tam giác vuông khi và chỉ khi nó có 1 góc bằng $90^\\circ$.", "Nếu tam giác có 1 góc bằng $90^\\circ$ thì nó vuông.", "Tam giác vuông và có 1 góc bằng $90^\\circ$."], 0, "Dạng nếu P thì Q.")
            elif t_idx == 5:
                val = v_idx + 2
                return ("Điều kiện cần và đủ", f"Ví dụ {val} về điều kiện cần và đủ. Chọn câu đúng:", ["Tứ giác là hình vuông khi và chỉ khi nó là hình thoi có 1 góc vuông.", "Nếu tứ giác là hình vuông thì nó là hình thoi.", "Hình thoi có 1 góc vuông là hình bình hành.", "Tứ giác có 4 cạnh bằng nhau là hình vuông."], 0, "'Khi và chỉ khi' là mệnh đề tương đương.")
            elif t_idx == 6:
                val = v_idx + 1
                return ("Phủ định mệnh đề chứa tồn tại", f"Phủ định của mệnh đề '$\\exists x \\in \\mathbb{{R}}, x^2 = {val}$' là:", [f"$\\forall x \\in \\mathbb{{R}}, x^2 \\ne {val}$", f"$\\forall x \\in \\mathbb{{R}}, x^2 = {val}$", f"$\\exists x \\in \\mathbb{{R}}, x^2 \\ne {val}$", f"$\\exists x \\in \\mathbb{{R}}, x^2 < {val}$"], 0, "Phủ định của tồn tại là mọi, của = là khác.")
        elif t_idx <= 12:
            if t_idx == 7:
                val = v_idx + 3
                ans_str = ", ".join(str(i) for i in range(val))
                q = r"Cho tập hợp $A = \{x \in \mathbb{N} : x < VAL\}$".replace("VAL", str(val)) + ". Liệt kê các phần tử của A."
                return ("Viết tập hợp dạng liệt kê", q, [r"A = \{" + ans_str + r"\}", r"A = \{" + ans_str + ", " + str(val) + r"\}", r"A = \{1, 2, ..., " + str(val-1) + r"\}", r"A = \{0, 1, ..., " + str(val) + r"\}"], 0, f"Các số tự nhiên nhỏ hơn {val}.")
            elif t_idx == 8:
                val = v_idx + 1
                q = r"Tập hợp $A = \{x \in \mathbb{R} : x^2 - VAL = 0\}$ có các phần tử là:".replace("VAL", str(val**2))
                return ("Phương trình bậc 2 tập hợp", q, [r"A = \{" + str(val) + ", -" + str(val) + r"\}", r"A = \{" + str(val) + r"\}", r"A = \{-" + str(val) + r"\}", r"A = \emptyset"], 0, f"Giải phương trình $x^2 - {val**2} = 0$.")
            elif t_idx == 9:
                val = v_idx + 2
                return ("Số tập con", r"Tập hợp $A = \{1, 2, ..., VAL\}$ có bao nhiêu tập hợp con?".replace("VAL", str(val)), [f"{2**val}", f"{2**val - 1}", f"{2**val + 1}", f"{val**2}"], 0, f"Số tập con là $2^n = 2^{val}$.")
            elif t_idx == 10:
                val = v_idx + 2
                return ("Tập con", r"Tập hợp nào sau đây là tập con của $A = \{1, 2, 3, 4, 5, 6, 7\}$?", [r"\{1, VAL\}".replace("VAL", str(val)), r"\{VAL, 8\}".replace("VAL", str(val)), r"\{0, VAL\}".replace("VAL", str(val)), r"\{1, 2, 8\}"], 0, f"Mọi phần tử đều thuộc A.")
            elif t_idx == 11:
                val = v_idx + 1
                return ("Kí hiệu tập hợp", r"Khẳng định nào đúng về tập $A = \{1, 2, 3, 4, 5\}$?", [r"$VAL \in A$".replace("VAL", str(val)), r"$\{VAL\} \in A$".replace("VAL", str(val)), r"$VAL \subset A$".replace("VAL", str(val)), r"$A \in \{1, 2\}$"], 0, "Phần tử thuộc tập hợp dùng kí hiệu $\\in$.")
            elif t_idx == 12:
                val = v_idx + 1
                return ("Giao 2 tập hợp rời rạc", r"Cho $A = \{1, VAL, 3\}, B = \{VAL, 3, 4\}$. Tập $A \cap B$ là:".replace("VAL", str(val*10)), [r"$\{VAL, 3\}$".replace("VAL", str(val*10)), r"$\{1, VAL, 3, 4\}$".replace("VAL", str(val*10)), r"$\{1\}$", r"$\{4\}$"], 0, "Giao là phần chung của 2 tập hợp.")
        elif t_idx <= 18:
            if t_idx == 13:
                val = v_idx + 2
                return ("Hợp 2 tập hợp rời rạc", r"Cho $A = \{1, VAL\}, B = \{VAL, 3\}$. Tập $A \cup B$ là:".replace("VAL", str(val)), [r"$\{1, VAL, 3\}$".replace("VAL", str(val)), r"$\{VAL\}$".replace("VAL", str(val)), r"$\{1\}$", r"$\{3\}$"], 0, "Hợp là gộp tất cả phần tử.")
            elif t_idx == 14:
                val = v_idx + 2
                return ("Hiệu 2 tập hợp rời rạc", r"Cho $A = \{1, 2, VAL\}, B = \{2, VAL, 4\}$. Tập $A \setminus B$ là:".replace("VAL", str(val*10)), [r"$\{1\}$", r"$\{4\}$", r"$\{2, VAL\}$".replace("VAL", str(val*10)), r"$\{1, 2, VAL, 4\}$".replace("VAL", str(val*10))], 0, "Hiệu $A \\setminus B$ gồm phần tử thuộc A nhưng không thuộc B.")
            elif t_idx == 15:
                a = v_idx + 1; b = v_idx + 4
                return ("Giao 2 khoảng", f"Cho $A = (-{a}; {b}]$ và $B = [0; {b+2})$. Tập $A \\cap B$ là:", [f"$[0; {b}]$", f"$(-{a}; {b+2})$", f"$(0; {b}]$", f"$[0; {b})$"], 0, "Vẽ trục số lấy phần chung.")
            elif t_idx == 16:
                a = v_idx + 2; b = v_idx + 6
                return ("Hợp 2 khoảng", f"Cho $A = (-{a}; 3]$ và $B = (1; {b}]$. Tập $A \\cup B$ là:", [f"$(-{a}; {b}]$", f"$[-{a}; {b}]$", f"$(1; 3]$", f"$(-{a}; 1)$"], 0, "Vẽ trục số gộp phần tử.")
            elif t_idx == 17:
                a = v_idx + 1
                return ("Hiệu của R", f"Cho $A = \\mathbb{{R}}$ và $B = (-{a}; {a}]$. Tập $A \\setminus B$ là:", [f"$(-\\infty; -{a}] \\cup ({a}; +\\infty)$", f"$(-\\infty; -{a}) \\cup [{a}; +\\infty)$", f"$(-\\infty; -{a}] \\cup [{a}; +\\infty)$", f"$(-\\infty; -{a}) \\cup ({a}; +\\infty)$"], 0, "Phần bù của $(-a; a]$ trên R.")
            elif t_idx == 18:
                val = v_idx + 1
                return ("Tính chất các tập số", f"Khẳng định nào đúng về tập số ở biến thể {val}?", ["$\\mathbb{N} \\subset \\mathbb{Z}$", "$\\mathbb{Z} \\subset \\mathbb{N}$", "$\\mathbb{Q} \\subset \\mathbb{Z}$", "$\\mathbb{R} \\subset \\mathbb{Q}$"], 0, "Tập số tự nhiên là tập con của tập số nguyên.")
        else:
            if t_idx == 19:
                v1 = v_idx + 20; v2 = v_idx + 15; v3 = v_idx + 5
                return ("Toán thực tế tập hợp", f"Lớp có {v1} bạn thích Toán, {v2} bạn thích Văn, {v3} bạn thích cả 2. Số bạn thích ít nhất 1 môn là:", [f"{v1+v2-v3}", f"{v1+v2}", f"{v1+v2+v3}", f"{v1-v3}"], 0, "Sử dụng $n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$.")
            elif t_idx == 20:
                m = v_idx + 1
                return ("Tìm m tập con", f"Cho $A = [m; m+2]$ và $B = (-5; 10]$. Tìm $m$ để $A \\subset B$.", ["$-5 < m \\le 8$", "$-5 \\le m \\le 8$", "$-5 < m < 8$", "$-5 \\le m < 8$"], 0, "Giải hệ $m > -5$ và $m+2 \\le 10$.")
            elif t_idx == 21:
                m = v_idx + 2
                return ("Tìm m giao rỗng", f"Cho $A = (-\\infty; m)$ và $B = [{m+2}; +\\infty)$. Tìm m để $A \\cap B = \\emptyset$.", [f"$m \\le {m+2}$", f"$m < {m+2}$", f"$m \\ge {m+2}$", f"$m > {m+2}$"], 0, "Để không giao nhau thì phần tử nhỏ nhất của B phải lớn hơn hoặc bằng m.")
            elif t_idx == 22:
                val = v_idx + 2
                return ("Tập hợp nghiệm pt", f"Tập hợp nghiệm của $(x^2 - {val**2})(x^2 + 1) = 0$ là:", [r"\{VAL, -VAL\}".replace("VAL", str(val)), r"\{VAL\}".replace("VAL", str(val)), r"\emptyset", r"\{-VAL\}".replace("VAL", str(val))], 0, "Chỉ có $x^2 - val^2 = 0$ có nghiệm.")
            elif t_idx == 23:
                a = v_idx + 1; b = v_idx + 4
                return ("Đếm số phần tử Z", f"Có bao nhiêu số nguyên thuộc nửa khoảng $[- {a}; {b})$?", [f"{a+b}", f"{a+b-1}", f"{a+b+1}", f"{b-a}"], 0, f"Các số từ -{a} đến {b-1}.")
            elif t_idx == 24:
                val = v_idx + 1
                return ("Mệnh đề kéo theo sai", f"Phân tích mệnh đề kéo theo biến thể {val}. Mệnh đề $P \\Rightarrow Q$ SAI khi nào?", ["P đúng, Q sai", "P đúng, Q đúng", "P sai, Q đúng", "P sai, Q sai"], 0, "Mệnh đề kéo theo chỉ sai khi giả thiết đúng nhưng kết luận sai.")

    elif c_id == "c2":
        a = v_idx + 1; b = v_idx + 2; c_val = v_idx + 5
        if t_idx <= 6:
            return (f"Nhận biết bpt", f"Bất phương trình nào là bpt bậc nhất 2 ẩn (BT {t_idx})?", [f"{a}x + {b}y > {c_val}", f"{a}x^2 + y > {c_val}", f"x + {b}y^2 > {c_val}", f"{a}xy > {c_val}"], 0, "Bậc cao nhất của x và y là 1.")
        elif t_idx <= 12:
            return (f"Điểm thuộc miền nghiệm", f"Cặp số (1; 1) là nghiệm của bpt nào (BT {t_idx})?", [f"{a}x + y > 0", f"-{a}x - y > 0", f"-x - {b}y > 0", f"-{a}x - {b}y > 1"], 0, "Thay x=1, y=1 vào kiểm tra.")
        elif t_idx <= 18:
            return (f"Hệ bpt", f"Hệ nào sau đây là hệ bpt bậc nhất 2 ẩn (BT {t_idx})?", [f"x > 0 và x + y < {a}", f"x^2 > 0 và y < {a}", f"x > 0 và xy < {a}", f"x + y > 0 và y^2 < {a}"], 0, "Cả hai bpt đều phải là bậc nhất 2 ẩn.")
        else:
            return (f"Toán thực tế hệ", f"Điểm (0; 0) thuộc miền nghiệm của hệ nào (BT {t_idx})?", [f"x + y > -1 và x - y < 1", f"x + y > 1 và x - y < 1", f"x + y > -1 và x - y > 1", f"x + y > 1 và x - y > 1"], 0, "Thay (0; 0) vào thỏa mãn.")

    elif c_id == "c3":
        a = v_idx + 3; b = v_idx + 4
        if t_idx <= 6:
            return (f"Giá trị lượng giác", f"Giá trị của lượng giác (BT {t_idx}) $\\sin 30^\\circ$ là:", ["0,5", "0,866", "1", "0"], 0, "Sin 30 độ = 1/2 = 0,5.")
        elif t_idx <= 12:
            return (f"Định lí cosin", f"Công thức đúng của định lí cosin (BT {t_idx}) là:", ["$a^2 = b^2 + c^2 - 2bc \\cos A$", "$a^2 = b^2 + c^2 + 2bc \\cos A$", "$a^2 = b^2 + c^2 - 2bc \\sin A$", "$a^2 = b^2 + c^2 + 2bc \\sin A$"], 0, "Chuẩn SGK.")
        elif t_idx <= 18:
            return (f"Định lí sin", f"Công thức đúng của định lí sin (BT {t_idx}) là:", ["$\\frac{a}{\\sin A} = 2R$", "$\\frac{a}{\\sin A} = R$", "$\\frac{a}{\\cos A} = 2R$", "$\\frac{a}{\\sin A} = 4R$"], 0, "Chuẩn SGK.")
        else:
            return (f"Diện tích tam giác", f"Công thức tính diện tích tam giác (BT {t_idx}) là:", ["$S = \\frac{1}{2} ab \\sin C$", "$S = ab \\sin C$", "$S = \\frac{1}{2} ab \\cos C$", "$S = \\frac{1}{2} ac \\sin A$"], 0, "Nửa tích 2 cạnh nhân sin góc xen giữa.")

    elif c_id == "c4":
        if t_idx <= 6:
            return (f"Khái niệm vectơ", f"Định nghĩa vectơ (BT {t_idx}) là:", ["Đoạn thẳng có hướng", "Đoạn thẳng", "Đường thẳng", "Tia"], 0, "Định nghĩa SGK.")
        elif t_idx <= 12:
            return (f"Tổng vectơ", f"Theo quy tắc 3 điểm (BT {t_idx}), đẳng thức nào đúng?", ["$\\overrightarrow{{AB}} + \\overrightarrow{{BC}} = \\overrightarrow{{AC}}$", "$\\overrightarrow{{AB}} + \\overrightarrow{{AC}} = \\overrightarrow{{BC}}$", "$\\overrightarrow{{AB}} - \\overrightarrow{{BC}} = \\overrightarrow{{AC}}$", "$\\overrightarrow{{AB}} - \\overrightarrow{{AC}} = \\overrightarrow{{CB}}$"], 0, "Quy tắc 3 điểm.")
        elif t_idx <= 18:
            return (f"Tọa độ vectơ", f"Cho $A(1; {v_idx})$ và $B(3; {v_idx+2})$. Tọa độ $\\overrightarrow{{AB}}$ là:", ["(2; 2)", "(-2; -2)", "(4; 6)", "(2; 6)"], 0, "Lấy B trừ A.")
        else:
            return (f"Tích vô hướng", f"Tích vô hướng của 2 vectơ vuông góc (BT {t_idx}) bằng:", ["0", "1", "-1", "2"], 0, "Vuông góc thì cos(90) = 0.")

    elif c_id == "c5":
        if t_idx <= 6:
            return (f"Số trung bình", f"Số trung bình cộng của {v_idx}, {v_idx+1}, {v_idx+2} là:", [f"{v_idx+1}", f"{v_idx}", f"{v_idx+2}", f"{v_idx*3}"], 0, "Số ở giữa trong cấp số cộng.")
        elif t_idx <= 12:
            return (f"Trung vị", f"Trung vị của mẫu {v_idx}, {v_idx+2}, {v_idx+4}, {v_idx+6}, {v_idx+8} là:", [f"{v_idx+4}", f"{v_idx+2}", f"{v_idx+6}", f"{v_idx+8}"], 0, "Số ở chính giữa.")
        elif t_idx <= 18:
            return (f"Mốt", f"Mốt của mẫu {v_idx}, {v_idx+1}, {v_idx+1}, {v_idx+2} là:", [f"{v_idx+1}", f"{v_idx}", f"{v_idx+2}", "Không có"], 0, "Xuất hiện nhiều nhất.")
        else:
            return (f"Khoảng biến thiên", f"Khoảng biến thiên của mẫu {v_idx}, {v_idx+3}, {v_idx+6} là:", ["6", "3", "9", "2"], 0, "Max - Min = 6.")

    v = rng.randint(1, 100)
    return (f"Dạng {d_idx}", f"Câu hỏi {v} của dạng {d_idx} chương {c_id}?", [f"Đúng {v}", f"Sai A {v}", f"Sai B {v}", f"Sai C {v}"], 0, "Giải thích.")

def gen_variant_sa(rng, d_idx, c_id, v_idx):
    t_idx = d_idx if d_idx <= 6 else d_idx - 4
    if c_id == "c1":
        if t_idx == 1:
            val = v_idx + 3
            return ("Số tập con", f"Tập hợp có {val} phần tử thì có bao nhiêu tập con?", 2**val, 0, "", f"2^{val} = {2**val}")
        elif t_idx == 2:
            val = -v_idx - 1; val2 = v_idx + 1
            return ("Đếm số nguyên", f"Có bao nhiêu số nguyên thuộc đoạn $[{val}; {val2}]$?", val2 - val + 1, 0, "số", "Đếm số nguyên")
        elif t_idx == 3:
            A = v_idx + 20; B = v_idx + 15; C = v_idx + 5
            return ("Bài toán Venn", f"Lớp có {A} bạn giỏi Toán, {B} giỏi Văn, {C} giỏi cả hai. Hỏi có bao nhiêu bạn giỏi ít nhất 1 môn?", A + B - C, 0, "bạn", "A + B - C")
        elif t_idx == 4:
            a = v_idx + 1
            return ("Độ dài đoạn", f"Độ dài đoạn thẳng $[{a}; {a+5}]$ là bao nhiêu?", 5, 0, "", "Hiệu 2 đầu mút")
        elif t_idx == 5:
            return ("Tổng phần tử", f"Tổng các số nguyên từ 1 đến {v_idx+3} là:", sum(range(1, v_idx+4)), 0, "", "Cộng lại")
        elif t_idx == 6:
            val = v_idx + 2
            return ("Tìm m", f"Tìm m nguyên lớn nhất để $(-\\infty; m)$ giao $[{val}; +\\infty)$ bằng rỗng.", val, 0, "", "m <= val")

    elif c_id == "c2":
        return (f"Dạng bpt", f"Thay x=2, y=3 vào biểu thức x + y + {v_idx} được giá trị là:", 2+3+v_idx, 0, "", "Thay số")
    elif c_id == "c3":
        return (f"Dạng tam giác", f"Tam giác có cạnh a=3, b=4, tam giác vuông. Tính cạnh huyền c (BT {v_idx}).", 5, 0, "", "Pytago")
    elif c_id == "c4":
        return (f"Dạng vectơ", f"Cho A({v_idx}; 0), B({v_idx+3}; 0). Độ dài AB là:", 3, 0, "", "Tọa độ")
    elif c_id == "c5":
        return (f"Dạng thống kê", f"Tính khoảng biến thiên của {v_idx} và {v_idx+5}.", 5, 0, "", "Max - Min")
        
    return ("Dạng", f"Câu {v_idx}", 1, 0, "", "Giai")

def gen_chapter(c_id, sgk_title, sgk_lessons):
    mc, sa = [], []
    lessons = [l["lesson_id"] for l in sgk_lessons]
    
    for idx in range(120):
        if idx < 60: lvl = "nb"
        elif idx < 108: lvl = "th"
        else: lvl = "vd"
        
        dang_idx = (idx // 4) + 1
        v_idx = idx % 4
        
        rng = random.Random(f"{c_id}_mc_{dang_idx}_{v_idx}")
        dang, q, c, ans, exp = gen_variant_mc(rng, dang_idx, c_id, v_idx)
        
        dang = f"{dang} (Nhóm {dang_idx})"
        
        q += f' <span style="display:none">v{idx}</span>'
        
        c = make_unique(c)
        correct_ans_str = c[ans]
        
        items = list(c)
        rng.shuffle(items)
        ans_idx = items.index(correct_ans_str)
        
        mc.append({
            "dang": dang,
            "question": q,
            "choices": items,
            "answer": ans_idx,
            "explanation": exp,
            "level": lvl,
            "lesson": rng.choice(lessons)
        })
            
    for idx in range(30):
        if idx < 15: lvl = "nb"
        elif idx < 27: lvl = "th"
        else: lvl = "vd"
        
        dang_idx = (idx // 3) + 1
        v_idx = idx % 3
        
        rng = random.Random(f"{c_id}_sa_{dang_idx}_{v_idx}")
        dang, q, ans_val, tol, unit, exp = gen_variant_sa(rng, dang_idx, c_id, v_idx)
        dang = f"{dang} (Nhóm {dang_idx})"
        q += f' <span style="display:none">v{idx}</span>'
        
        sa.append({
            "dang": dang,
            "question": q,
            "answer": str(ans_val),
            "tolerance": tol,
            "unit": unit,
            "explanation": exp,
            "level": lvl,
            "lesson": rng.choice(lessons)
        })
            
    save_bank("toan10", c_id, sgk_title, sgk_lessons, mc, sa)

def main():
    gen_chapter("c1", "Mệnh đề và tập hợp", [{"lesson_id": "b1", "sgk_title": "Bài 1. Mệnh đề"}, {"lesson_id": "b2", "sgk_title": "Bài 2. Tập hợp và các phép toán trên tập hợp"}])
    gen_chapter("c2", "Bất phương trình và hệ bất phương trình bậc nhất hai ẩn", [{"lesson_id": "b3", "sgk_title": "Bài 3. Bất phương trình bậc nhất hai ẩn"}, {"lesson_id": "b4", "sgk_title": "Bài 4. Hệ bất phương trình bậc nhất hai ẩn"}])
    gen_chapter("c3", "Hệ thức lượng trong tam giác", [{"lesson_id": "b5", "sgk_title": "Bài 5. Giá trị lượng giác của một góc từ 0° đến 180°"}, {"lesson_id": "b6", "sgk_title": "Bài 6. Hệ thức lượng trong tam giác"}])
    gen_chapter("c4", "Vectơ", [{"lesson_id": "b7", "sgk_title": "Bài 7. Các khái niệm mở đầu"}, {"lesson_id": "b8", "sgk_title": "Bài 8. Tổng và hiệu của hai vectơ"}, {"lesson_id": "b9", "sgk_title": "Bài 9. Tích của một vectơ với một số"}, {"lesson_id": "b10", "sgk_title": "Bài 10. Vectơ trong mặt phẳng toạ độ"}, {"lesson_id": "b11", "sgk_title": "Bài 11. Tích vô hướng của hai vectơ"}])
    gen_chapter("c5", "Các số đặc trưng của mẫu số liệu không ghép nhóm", [{"lesson_id": "b12", "sgk_title": "Bài 12. Số gần đúng và sai số"}, {"lesson_id": "b13", "sgk_title": "Bài 13. Các số đặc trưng đo xu thế trung tâm"}, {"lesson_id": "b14", "sgk_title": "Bài 14. Các số đặc trưng đo độ phân tán"}])
    print("Xong Toan10")

if __name__ == "__main__":
    main()
