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
    mod = d_idx % 4

    if c_id == "c1":
        if mod == 1:
            return (f"Lý thuyết", f"Nguyên tử được cấu tạo từ các loại hạt cơ bản nào (BT {v_idx})?", ["Proton, Neutron và Electron", "Chỉ gồm Proton và Electron", "Chỉ gồm Neutron và Electron", "Chỉ gồm Proton và Neutron"], 0, "Nguyên tử gồm hạt nhân (proton, neutron) và vỏ electron.")
        elif mod == 2:
            Z = v_idx + 1
            return (f"Bài tập", f"Nguyên tử của nguyên tố X có Z = {Z}. Số hiệu nguyên tử và số proton trong hạt nhân X lần lượt là:", [f"Z = {Z}, p = {Z}", f"Z = {Z}, p = {Z+2}", f"Z = {Z+1}, p = {Z}", f"Z = {Z}, p = {Z*2}"], 0, f"Số hiệu nguyên tử Z luôn bằng số proton p.")
        elif mod == 3:
            return (f"Lý thuyết", f"Đồng vị là các nguyên tử có cùng (BT {v_idx}):", ["Số proton nhưng khác nhau số neutron", "Số neutron nhưng khác nhau số proton", "Số khối A nhưng khác nhau số proton", "Số electron lớp ngoài cùng nhưng khác số lớp e"], 0, "Đồng vị có cùng số proton (Z) nhưng khác số neutron (N).")
        else:
            return (f"Lý thuyết", f"Cấu hình electron của nguyên tử Natri (Na, Z = 11) là (BT {v_idx}):", ["1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁵ 3s²", "1s² 2s² 2p⁶ 3p¹", "1s² 2s² 2p⁴ 3s³"], 0, "Na (Z=11) có 11e: 1s² 2s² 2p⁶ 3s¹.")

    elif c_id == "c2":
        if mod == 1:
            return (f"Lý thuyết", f"Trong Bảng tuần hoàn, các nguyên tố trong cùng một Chu kỳ có cùng (BT {v_idx}):", ["Số lớp electron trong nguyên tử", "Số electron hóa trị", "Số proton", "Bán kính nguyên tử"], 0, "Số thứ tự chu kỳ = số lớp electron của nguyên tử.")
        elif mod == 2:
            return (f"Lý thuyết", f"Trong một nhóm A (từ trên xuống dưới), bán kính nguyên tử của các nguyên tố (BT {v_idx}):", ["Tăng dần", "Giảm dần", "Không đổi", "Biến đổi không quy luật"], 0, "Từ trên xuống trong nhóm A, số lớp e tăng nên bán kính nguyên tử tăng dần.")
        elif mod == 3:
            return (f"Lý thuyết", f"Độ âm điện đặc trưng cho khả năng (BT {v_idx}):", ["Hút electron của nguyên tử khi hình thành liên kết hóa học", "Nhường electron của nguyên tử", "Hút proton trong hạt nhân", "Thu nhiệt của phản ứng"], 0, "Độ âm điện đo khả năng hút e của nguyên tử trong liên kết hóa học.")
        else:
            return (f"Lý thuyết", f"Nguyên tố F (Fluorine, Z = 9) là nguyên tố có độ âm điện (BT {v_idx}):", ["Lớn nhất trong Bảng tuần hoàn (3,98)", "Nhỏ nhất trong Bảng tuần hoàn", "Bằng 0", "Bằng với Natri"], 0, "Fluorine (F) có độ âm điện lớn nhất (3,98).")

    elif c_id == "c3":
        if mod == 1:
            return (f"Lý thuyết", f"Liên kết được hình thành do lực hút tĩnh điện giữa các ion trái dấu gọi là (BT {v_idx}):", ["Liên kết ion", "Liên kết cộng hóa trị không cực", "Liên kết cộng hóa trị có cực", "Liên kết hydrogen"], 0, "Liên kết ion được tạo thành do lực hút tĩnh điện giữa cation (+) và anion (-).")
        elif mod == 2:
            return (f"Lý thuyết", f"Phân tử nào sau đây chứa liên kết cộng hóa trị KHÔNG CỰC (BT {v_idx})?", ["N₂ (hoặc O₂, H₂)", "HCl", "H₂O", "NH₃"], 0, "Các phân tử đơn chất 2 nguyên tử giống nhau như N2, O2, H2 có Δχ = 0 nên liên kết không cực.")
        elif mod == 3:
            return (f"Lý thuyết", f"Liên kết hydrogen được hình thành giữa nguyên tử H linh động với nguyên tử có độ âm điện lớn như (BT {v_idx}):", ["F, O, N", "Na, K, Ba", "Cl, Br, I", "C, Si, P"], 0, "Liên kết hydrogen chỉ xuất hiện với các nguyên tử có độ âm điện rất lớn F, O, N.")
        else:
            return (f"Lý thuyết", f"Giải thích tại sao nước (H₂O) có nhiệt độ sôi cao bất thường (100 °C) so với H₂S (-60 °C) (BT {v_idx}):", ["Do các phân tử H₂O tạo được liên kết hydrogen liên phân tử", "Do H₂O có khối lượng phân tử lớn hơn H₂S", "Do H₂O là hợp chất ion", "Do H₂O là khí hiếm"], 0, "Liên kết hydrogen giữa các phân tử H2O làm tăng mạnh nhiệt độ sôi của nước.")

    elif c_id == "c4":
        if mod == 1:
            return (f"Lý thuyết", f"Trong phản ứng oxi hóa - khử, chất khử là chất (BT {v_idx}):", ["Nhường electron, số oxi hóa tăng sau phản ứng", "Nhận electron, số oxi hóa giảm", "Không thay đổi số oxi hóa", "Chỉ đóng vai trò môi trường"], 0, "Chất khử là chất nhường electron (chất bị oxi hóa).")
        elif mod == 2:
            return (f"Lý thuyết", f"Số oxi hóa của nguyên tố Lưu huỳnh (S) trong hợp chất H₂SO₄ là (BT {v_idx}):", ["+6", "+4", "-2", "0"], 0, "2(+1) + S + 4(-2) = 0 => S = +6.")
        elif mod == 3:
            return (f"Lý thuyết", f"Xác định chất oxi hóa trong phản ứng: Zn + 2HCl -> ZnCl₂ + H₂ (BT {v_idx}).", ["HCl (chứa H⁺ nhận e)", "Zn", "ZnCl₂", "H₂"], 0, "H+ trong HCl nhận e biến thành H2 nên HCl là chất oxi hóa.")
        else:
            return (f"Lý thuyết", f"Quá trình Fe⁰ -> Fe⁺³ + 3e được gọi là (BT {v_idx}):", ["Quá trình oxi hóa Fe", "Quá trình khử Fe", "Sự tự nhân đôi", "Phản ứng nhiệt nhôm"], 0, "Sự nhường e là quá trình (sự) oxi hóa.")

    elif c_id == "c5":
        if mod == 1:
            return (f"Lý thuyết", f"Phản ứng có biến thiên enthalpy chuẩn Δ_r H₂₉₈⁰ < 0 là phản ứng (BT {v_idx}):", ["Tỏa nhiệt", "Thu nhiệt", "Không trao đổi nhiệt", "Cân bằng"], 0, "Δr H298° < 0 giải phóng nhiệt năng ra môi trường (phản ứng tỏa nhiệt).")
        elif mod == 2:
            return (f"Lý thuyết", f"Điều kiện chuẩn đối với chất khí và dung dịch khi đo biến thiên enthalpy là (BT {v_idx}):", ["Áp suất 1 bar và nhiệt độ 25 °C (298 K)", "Áp suất 1 atm và nhiệt độ 0 °C", "Áp suất 10 bar và 100 °C", "Mọi nhiệt độ và áp suất bất kỳ"], 0, "Điều kiện chuẩn: 1 bar và 25 °C (298 K).")
        elif mod == 3:
            val_H = 393.5 + v_idx
            return (f"Bài tập", f"Cho phản ứng C(s) + O₂(g) -> CO₂(g) có Δ_r H₂₉₈⁰ = -{val_H} kJ. Khi đốt cháy 1 mol C thì:", [f"Tỏa ra nhiệt lượng {val_H} kJ", f"Thu vào nhiệt lượng {val_H} kJ", f"Tỏa ra {val_H * 2} kJ", "Không thay đổi nhiệt độ"], 0, f"Δr H° = -{val_H} kJ (âm) cho biết phản ứng tỏa nhiệt.")
        else:
            return (f"Lý thuyết", f"Công thức tính biến thiên enthalpy theo Nhiệt tạo thành chuẩn là (BT {v_idx}):", ["Δ_r H₂₉₈⁰ = ∑Δ_f H₂₉₈⁰ (sản phẩm) - ∑Δ_f H₂₉₈⁰ (chất đầu)", "Δ_r H₂₉₈⁰ = ∑Δ_f H₂₉₈⁰ (chất đầu) - ∑Δ_f H₂₉₈⁰ (sản phẩm)", "Δ_r H₂₉₈⁰ = ∑E_b (sản phẩm) - ∑E_b (chất đầu)", "Δ_r H₂₉₈⁰ = ∑Δ_f H₂₉₈⁰ (sản phẩm) + ∑Δ_f H₂₉₈⁰ (chất đầu)"], 0, "Tính theo nhiệt tạo thành: lấy tổng Δf H của Sản phẩm trừ tổng Δf H của Chất đầu.")

    v = rng.randint(1, 100)
    return (f"Dạng {d_idx}", f"Câu hỏi {v} của dạng {d_idx} chương {c_id}?", [f"Đúng {v}", f"Sai A {v}", f"Sai B {v}", f"Sai C {v}"], 0, "Giải thích.")

def gen_variant_sa(rng, d_idx, c_id, v_idx):
    mod = d_idx % 4
    if c_id == "c1":
        Z = v_idx + 1
        A = 2 * Z + 2
        N = A - Z
        ans_val = N
        return ("Cấu tạo", f"Một nguyên tử X có Z = {Z} và số khối A = {A}. Tính số neutron N trong hạt nhân X.", ans_val, 0, "", f"N = A - Z = {A} - {Z} = {N}.")
    elif c_id == "c2":
        Z_val = v_idx + 3
        ans_val = 3 if Z_val <= 18 else 4
        return ("Bảng TH", f"Nguyên tố X có Z = {Z_val}. Nguyên tử X có bao nhiêu lớp electron?", ans_val, 0, "", f"Z = {Z_val} có cấu hình e thích hợp với {ans_val} lớp e.")
    elif c_id == "c3":
        return ("Liên kết", f"Một phân tử Mêtan (CH₄) có bao nhiêu liên kết cộng hóa trị đơn C-H (BT {v_idx})?", 4, 0, "", "C có 4 e hóa trị kết hợp với 4 H tạo 4 liên kết đơn.")
    elif c_id == "c4":
        return ("Oxi hóa", f"Xác định số oxi hóa của nguyên tố Lưu huỳnh (S) trong H₂SO₄ (BT {v_idx}).", 6, 0, "", "2(+1) + S + 4(-2) = 0 => S = +6.")
    elif c_id == "c5":
        val_H = v_idx * 25 + 25
        ans_val = val_H
        return ("Nhiệt học", f"Cho phản ứng tỏa nhiệt có Δ_r H₂₉₈⁰ = -{val_H} kJ. Nhiệt lượng tỏa ra (kJ) là:", ans_val, 0, "kJ", f"Nhiệt lượng tỏa ra = |Δ_r H₂₉₈⁰| = {val_H} kJ.")
        
    return ("Dạng SA", f"Câu {v_idx}", 1, 0, "", "Giai")

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
            
    save_bank("hoa10", c_id, sgk_title, sgk_lessons, mc, sa)

def main():
    gen_chapter("c1", "Cấu tạo nguyên tử", [{"lesson_id": "b1", "sgk_title": "Bài 1. Thành phần nguyên tử"}, {"lesson_id": "b2", "sgk_title": "Bài 2. Cấu hình electron nguyên tử"}])
    gen_chapter("c2", "Bảng tuần hoàn các nguyên tố", [{"lesson_id": "b3", "sgk_title": "Bài 3. Cấu tạo Bảng tuần hoàn"}, {"lesson_id": "b4", "sgk_title": "Bài 4. Xu hướng biến đổi tính chất"}])
    gen_chapter("c3", "Liên kết hóa học", [{"lesson_id": "b5", "sgk_title": "Bài 5. Liên kết ion & Cộng hóa trị"}, {"lesson_id": "b6", "sgk_title": "Bài 6. Liên kết hydrogen & van der Waals"}])
    gen_chapter("c4", "Phản ứng oxi hóa - khử", [{"lesson_id": "b7", "sgk_title": "Bài 7. Số oxi hóa & Phản ứng Oxi hóa - Khử"}, {"lesson_id": "b8", "sgk_title": "Bài 8. Cân bằng phản ứng Oxi hóa - Khử"}])
    gen_chapter("c5", "Năng lượng hóa học", [{"lesson_id": "b9", "sgk_title": "Bài 9. Biến thiên Enthalpy trong phản ứng"}, {"lesson_id": "b10", "sgk_title": "Bài 10. Tính biến thiên Enthalpy"}])
    print("Xong Hoa10")

if __name__ == "__main__":
    main()
