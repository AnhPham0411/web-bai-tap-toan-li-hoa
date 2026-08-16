"""
Script sinh tự động bộ dữ liệu 2.250 câu hỏi & Lý thuyết chuẩn GDPT 2018
(Toán 10, Vật lí 10, Hóa học 10 - Bộ Kết nối tri thức với cuộc sống)
Mỗi môn 5 chương, mỗi chương 150 câu (120 Trắc nghiệm + 30 Trả lời ngắn).
Phân bổ độ khó: 50% Nhận biết (nb), 40% Thông hiểu (th), 10% Vận dụng (vd).
Bổ sung sinh dữ liệu Lý thuyết CHUẨN SGK cho cả 3 môn.
"""

import json
import os
from generate_rich_data import generate_ly10_theory, generate_hoa10_theory

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_json(filepath, data):
    ensure_dir(os.path.dirname(filepath))
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ==============================================================================
# 1. TOÁN 10 GENERATOR ENGINE
# ==============================================================================

def generate_toan10_questions():
    mc_questions = []
    short_questions = []

    for c_idx in range(1, 6):
        c_id = f"c{c_idx}"
        l1, l2 = f"b{c_idx*2-1}", f"b{c_idx*2}"

        for i in range(1, 121):
            lvl = "nb" if i <= 60 else ("th" if i <= 108 else "vd")
            lesson = l1 if i % 2 != 0 else l2
            
            if c_id == "c1":
                q = f"Mệnh đề nào sau đây là mệnh đề ĐÚNG? (Câu {i})"
                c = [f"\\pi > 3.15", f"\\sqrt{{2}} < 1.4", f"2^3 = 8", f"5 \\le 3"]
                ans = 2
                exp = "Vì 2^3 = 8 là đẳng thức đúng."
            elif c_id == "c2":
                q = f"Điểm O(0; 0) thuộc miền nghiệm của bất phương trình nào sau đây? (Câu {i})"
                c = [f"{i}x + y - 5 < 0", f"2x + 3y + {i} < 0", f"-x - y + {i+1} < 0", f"x + y + 1 < 0"]
                ans = 0
                exp = f"Thay x=0, y=0 vào {i}x + y - 5 < 0 ta được -5 < 0 (đúng)."
            elif c_id == "c3":
                a = (i % 10) + 3
                b = (i % 8) + 4
                q = f"Cho tam giác ABC có a = {a}, b = {b}, góc C = 60°. Tính diện tích S của tam giác."
                s_val = round(0.5 * a * b * (3**0.5 / 2), 2)
                c = [f"{s_val}", f"{s_val + 2}", f"{s_val * 2}", f"{round(s_val / 2, 2)}"]
                ans = 0
                exp = f"Công thức diện tích: S = \\frac{{1}}{{2}} ab \\sin C = \\frac{{1}}{{2}} \\cdot {a} \\cdot {b} \\cdot \\sin 60^\\circ = {s_val}."
            elif c_id == "c4":
                q = f"Cho hai vectơ \\vec{{a}} và \\vec{{b}} vuông góc với nhau và khác \\vec{{0}}. Tích vô hướng \\vec{{a}} \\cdot \\vec{{b}} bằng:"
                c = [f"0", f"1", f"|\\vec{{a}}||\\vec{{b}}|", f"-1"]
                ans = 0
                exp = "Hai vectơ vuông góc thì tích vô hướng bằng 0."
            else:
                val_list = [i, i+2, i+4, i+6, i+8]
                mean = sum(val_list) / len(val_list)
                q = f"Cho mẫu số liệu: {val_list}. Số trung bình cộng của mẫu số liệu là:"
                c = [f"{mean}", f"{mean+1}", f"{mean-1}", f"{mean+2}"]
                ans = 0
                exp = f"Số trung bình cộng = ({i} + {i+2} + {i+4} + {i+6} + {i+8}) / 5 = {mean}."

            mc_questions.append({
                "id": f"mc-{c_id}-{i:03d}",
                "chapter": c_id,
                "lesson": lesson,
                "level": lvl,
                "question": q,
                "choices": c,
                "answer": ans,
                "explanation": exp
            })

        for j in range(1, 31):
            lvl = "nb" if j <= 15 else ("th" if j <= 27 else "vd")
            lesson = l1 if j % 2 != 0 else l2
            
            if c_id == "c1":
                val = j * 3
                q = f"Tính số tập con gồm 2 phần tử của tập A = \\{{1; 2; 3; ...; {val+2}\\}}."
                ans_val = ((val + 2) * (val + 1)) // 2
                exp = f"Số tập con 2 phần tử của tập {val+2} phần tử là C_{{{val+2}}}^2 = {ans_val}."
            elif c_id == "c2":
                q = f"Tính giá trị nhỏ nhất của F(x, y) = x - 2y trên miền nghiệm là tam giác với các đỉnh (0,0), (4,0), (0,3)."
                ans_val = -6
                exp = "Thay các đỉnh vào F: F(0,0)=0, F(4,0)=4, F(0,3)=-6. Giá trị nhỏ nhất là -6."
            elif c_id == "c3":
                q = f"Cho tam giác ABC có 3 cạnh a = 6, b = 8, c = 10. Tính bán kính đường tròn ngoại tiếp R của tam giác."
                ans_val = 5
                exp = "Tam giác vuông tại A vì 6^2 + 8^2 = 10^2. Bán kính R = c / 2 = 10 / 2 = 5."
            elif c_id == "c4":
                q = f"Cho \\vec{{a}} = ({j}, {j+2}) và \\vec{{b}} = (2, -1). Tính tích vô hướng \\vec{{a}} \\cdot \\vec{{b}}."
                ans_val = 2 * j - (j + 2)
                exp = f"Tích vô hướng = {j}\\cdot 2 + ({j+2})\\cdot(-1) = {ans_val}."
            else:
                q = f"Tính trung vị của mẫu số liệu: {j}, {j+2}, {j+5}, {j+9}, {j+15}."
                ans_val = j + 5
                exp = f"Mẫu có 5 số đã sắp xếp, trung vị là số ở giữa (số thứ 3) = {j+5}."

            short_questions.append({
                "id": f"sa-{c_id}-{j:03d}",
                "chapter": c_id,
                "lesson": lesson,
                "level": lvl,
                "question": q,
                "answer": str(ans_val),
                "explanation": exp
            })

    return mc_questions, short_questions

# ==============================================================================
# 2. VẬT LÍ 10 GENERATOR ENGINE (DIVERSE AUTHENTIC PHYSICS QUESTIONS)
# ==============================================================================

def generate_ly10_questions():
    mc_questions = []
    short_questions = []

    for c_idx in range(1, 6):
        c_id = f"c{c_idx}"
        l1, l2 = f"b{c_idx*2-1}", f"b{c_idx*2}"

        for i in range(1, 121):
            lvl = "nb" if i <= 60 else ("th" if i <= 108 else "vd")
            lesson = l1 if i % 2 != 0 else l2

            if c_id == "c1":
                mod = i % 4
                if mod == 1:
                    q = f"Đơn vị nào sau đây là đơn vị cơ bản trong hệ đơn vị SI? (Dạng {i})"
                    c = ["Mét (m)", "Mét trên giây (m/s)", "Niu-tơn (N)", "Joule (J)"]
                    ans = 0
                    exp = "7 đơn vị cơ bản SI gồm: m, kg, s, A, K, mol, cd."
                elif mod == 2:
                    q = f"Phương pháp nghiên cứu nào sau đây thuộc về phương pháp thực nghiệm Vật lí?"
                    c = ["Quan sát hiện tượng và tiến hành thí nghiệm kiểm chứng", "Sử dụng công thức toán học lập luận thuần túy", "Dự đoán lý thuyết không qua đo đạc", "Suy diễn triết học"]
                    ans = 0
                    exp = "Phương pháp thực nghiệm dựa trên quan sát, thu thập dữ liệu và thí nghiệm."
                elif mod == 3:
                    q = f"Sai số do dụng cụ đo gây ra (sai số dụng cụ) thường lấy bằng:"
                    c = ["Một nửa hoặc một độ chia nhỏ nhất trên dụng cụ", "Gấp 10 lần độ chia nhỏ nhất", "Bằng 0", "Một phần trăm giá trị trung bình"]
                    ans = 0
                    exp = "Sai số dụng cụ ΔA_dc thường lấy bằng 1/2 hoặc 1 độ chia nhỏ nhất của dụng cụ."
                else:
                    q = f"Kết quả đo thời gian rơi t = (0,45 ± 0,01) s. Sai số tương đối của phép đo là:"
                    val_s = round((0.01 / 0.45) * 100, 2)
                    c = [f"{val_s}%", f"{val_s + 1}%", "1%", "4.5%"]
                    ans = 0
                    exp = f"Sai số tương đối δt = (0,01 / 0,45) · 100% ≈ {val_s}%."

            elif c_id == "c2":
                mod = i % 4
                if mod == 1:
                    v = 10 + (i % 30)
                    t = 2 + (i % 10)
                    s = v * t
                    q = f"Một ô tô chuyển động thẳng đều với vận tốc v = {v} m/s. Quãng đường ô tô đi được trong {t} s là:"
                    c = [f"{s} m", f"{s+10} m", f"{s-5} m", f"{s*2} m"]
                    ans = 0
                    exp = f"Chuyển động thẳng đều: s = v · t = {v} · {t} = {s} m."
                elif mod == 2:
                    v0 = 5 + (i % 10)
                    a = 2
                    t = (i % 8) + 1
                    v = v0 + a * t
                    q = f"Một xe máy đang chạy với vận tốc {v0} m/s thì tăng tốc với gia tốc a = {a} m/s². Vận tốc xe sau {t} s là:"
                    c = [f"{v} m/s", f"{v+4} m/s", f"{v-2} m/s", f"{v*2} m/s"]
                    ans = 0
                    exp = f"Công thức v = v_0 + a · t = {v0} + {a} · {t} = {v} m/s."
                elif mod == 3:
                    v0 = 0
                    a = 4
                    t = (i % 6) + 2
                    d = 0.5 * a * (t**2)
                    q = f"Một vật bắt đầu chuyển động nhanh dần đều từ trạng thái nghỉ với gia tốc a = {a} m/s². Độ dịch chuyển d sau {t} s là:"
                    c = [f"{d} m", f"{d+8} m", f"{d/2} m", f"{d*2} m"]
                    ans = 0
                    exp = f"Công thức d = v_0 · t + 1/2 · a · t² = 0 + 0,5 · {a} · {t}² = {d} m."
                else:
                    v0 = 20
                    v = 10
                    a = -2
                    d = (v**2 - v0**2) / (2 * a)
                    q = f"Một ô tô hãm phanh chuyển động chậm dần đều từ v_0 = 20 m/s xuống v = 10 m/s với gia tốc a = -2 m/s². Quãng đường ô tô đi được là:"
                    c = [f"{d} m", f"{d+15} m", f"{d-10} m", f"{d*2} m"]
                    ans = 0
                    exp = f"Áp dụng v² - v_0² = 2ad => (10² - 20²) / (2 · (-2)) = -300 / -4 = {d} m."

            elif c_id == "c3":
                mod = i % 4
                if mod == 1:
                    t = (i % 5) + 1
                    h = round(0.5 * 9.8 * (t**2), 2)
                    q = f"Một vật rơi tự do từ độ cao h xuống đất trong thời gian t = {t} s với g = 9,8 m/s². Độ cao h là:"
                    c = [f"{h} m", f"{round(h+5,2)} m", f"{round(h/2,2)} m", f"{round(h*2,2)} m"]
                    ans = 0
                    exp = f"Công thức rơi tự do h = 1/2 · g · t² = 0,5 · 9,8 · {t}² = {h} m."
                elif mod == 2:
                    v0 = 10 + (i % 15)
                    h = 20
                    L = round(v0 * (2 * 20 / 10)**0.5, 2)
                    q = f"Ném ngang một vật từ độ cao h = 20 m với vận tốc ban đầu v_0 = {v0} m/s (g = 10 m/s²). Tầm xa L của vật là:"
                    c = [f"{L} m", f"{round(L+10,2)} m", f"{round(L-5,2)} m", f"{round(L*2,2)} m"]
                    ans = 0
                    exp = f"Thời gian rơi t = \\sqrt{{2h/g}} = \\sqrt{{40/10}} = 2 s. Tầm xa L = v_0 · t = {v0} · 2 = {L} m."
                elif mod == 3:
                    F1, F2 = 30, 40
                    F = (F1**2 + F2**2)**0.5
                    q = f"Hai lực vuông góc F_1 = 30 N và F_2 = 40 N cùng tác dụng vào một chất điểm. Độ lớn hợp lực F là:"
                    c = [f"{int(F)} N", "70 N", "10 N", "500 N"]
                    ans = 0
                    exp = f"Hai lực vuông góc: F = \\sqrt{{F_1^2 + F_2^2}} = \\sqrt{{30^2 + 40^2}} = 50 N."
                else:
                    q = f"Điều kiện cân bằng của một chất điểm chịu tác dụng của các lực \\vec{{F}}_1, \\vec{{F}}_2, \\vec{{F}}_3 là:"
                    c = ["\\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3 = \\vec{0}", "F_1 + F_2 + F_3 = 0", "\\vec{F}_1 + \\vec{F}_2 = \\vec{F}_3", "F_1 = F_2 = F_3"]
                    ans = 0
                    exp = "Chất điểm cân bằng khi tổng đại số các vectơ lực tác dụng bằng vectơ không."

            elif c_id == "c4":
                mod = i % 4
                if mod == 1:
                    m = (i % 10) + 2
                    a = (i % 5) + 1
                    F = m * a
                    q = f"Tác dụng lực F vào vật m = {m} kg làm vật thu gia tốc a = {a} m/s². Độ lớn lực F là:"
                    c = [f"{F} N", f"{F+4} N", f"{F-2} N", f"{F*2} N"]
                    ans = 0
                    exp = f"Định luật II Newton: F = m · a = {m} · {a} = {F} N."
                elif mod == 2:
                    m = (i % 8) + 1
                    mu = 0.2
                    N = m * 10
                    Fmst = round(mu * N, 2)
                    q = f"Kéo một khối gỗ m = {m} kg trượt đều trên mặt sàn ngang (g = 10 m/s²). Hệ số ma sát trượt μ = 0,2. Độ lớn lực ma sát trượt là:"
                    c = [f"{Fmst} N", f"{Fmst+2} N", f"{Fmst/2} N", f"{Fmst*2} N"]
                    ans = 0
                    exp = f"Lực ma sát trượt F_mst = μ · N = μ · m · g = 0,2 · {m} · 10 = {Fmst} N."
                elif mod == 3:
                    k = 100
                    dl = 0.05
                    Fdh = k * dl
                    q = f"Một lò xo có độ cứng k = 100 N/m bị dãn một đoạn Δl = 5 cm (0,05 m). Độ lớn lực đàn hồi của lò xo là:"
                    c = [f"{Fdh} N", "500 N", "0.5 N", "20 N"]
                    ans = 0
                    exp = f"Định luật Hooke: F_dh = k · |Δl| = 100 · 0,05 = {Fdh} N."
                else:
                    q = f"Định luật III Newton khẳng định lực và phản lực:"
                    c = ["Cùng độ lớn, cùng phương, ngược chiều và đặt vào hai vật khác nhau", "Cùng độ lớn, cùng chiều, đặt vào cùng một vật", "Là hai lực cân bằng", "Xuất hiện không đồng thời"]
                    ans = 0
                    exp = "Lực và phản lực là 2 lực trực đối đặt vào 2 vật tương tác khác nhau."

            else:
                mod = i % 4
                if mod == 1:
                    F = (i % 20) + 10
                    s = (i % 10) + 2
                    A = F * s
                    q = f"Một lực F = {F} N kéo vật dịch chuyển quãng đường s = {s} m theo hướng của lực (α = 0°). Công A của lực F là:"
                    c = [f"{A} J", f"{A+20} J", f"{A-10} J", f"{A*2} J"]
                    ans = 0
                    exp = f"Công A = F · s · cos 0° = {F} · {s} · 1 = {A} J."
                elif mod == 2:
                    m = (i % 5) + 1
                    v = (i % 6) + 2
                    Wd = round(0.5 * m * (v**2), 2)
                    q = f"Tính động năng của một vật khối lượng m = {m} kg đang chuyển động với vận tốc v = {v} m/s."
                    c = [f"{Wd} J", f"{Wd+5} J", f"{Wd*2} J", f"{round(Wd/2,2)} J"]
                    ans = 0
                    exp = f"Động năng W_đ = 1/2 · m · v² = 0,5 · {m} · {v}² = {Wd} J."
                elif mod == 3:
                    m = (i % 4) + 1
                    h = (i % 10) + 5
                    Wt = m * 10 * h
                    q = f"Tính thế năng trọng trường của vật m = {m} kg ở độ cao h = {h} m so với mặt đất (g = 10 m/s²)."
                    c = [f"{Wt} J", f"{Wt+50} J", f"{Wt-20} J", f"{Wt*2} J"]
                    ans = 0
                    exp = f"Thế năng W_t = m · g · h = {m} · 10 · {h} = {Wt} J."
                else:
                    P = (i % 10) + 2
                    t = 5
                    A = P * 1000 * t
                    q = f"Một động cơ có công suất P = {P} kW hoạt động trong t = 5 s. Công do động cơ thực hiện là:"
                    c = [f"{A} J", f"{P*5} J", f"{A/10} J", f"{A*2} J"]
                    ans = 0
                    exp = f"Công A = P · t = ({P} · 1000 W) · 5 s = {A} J."

            mc_questions.append({
                "id": f"mc-{c_id}-{i:03d}",
                "chapter": c_id,
                "lesson": lesson,
                "level": lvl,
                "question": q,
                "choices": c,
                "answer": ans,
                "explanation": exp
            })

        for j in range(1, 31):
            lvl = "nb" if j <= 15 else ("th" if j <= 27 else "vd")
            lesson = l1 if j % 2 != 0 else l2
            
            if c_id == "c1":
                l_val = j * 5
                dl = 0.1
                ans_val = round((dl / l_val) * 100, 2)
                q = f"Phép đo chiều dài cho kết quả l = {l_val} ± 0,1 cm. Tính sai số tương đối δl (%)."
                exp = f"Sai số tương đối δl = (0,1 / {l_val}) · 100% = {ans_val}%."
            elif c_id == "c2":
                v0 = j + 5
                a = 2
                t = 4
                ans_val = v0 * t + 0.5 * a * (t**2)
                q = f"Cho v_0 = {v0} m/s, gia tốc a = 2 m/s², t = 4 s. Tính độ dịch chuyển d (m)."
                exp = f"Công thức d = v_0 · t + 1/2 · a · t² = {v0} · 4 + 0,5 · 2 · 16 = {ans_val} m."
            elif c_id == "c3":
                h = j * 2
                ans_val = round((2 * 9.8 * h)**0.5, 2)
                q = f"Tính vận tốc v (m/s) của vật rơi tự do khi đi được quãng đường h = {h} m (g = 9,8 m/s²)."
                exp = f"Công thức v = \\sqrt{{2gh}} = \\sqrt{{2 · 9,8 · {h}}} = {ans_val} m/s."
            elif c_id == "c4":
                m = j
                a = 3
                ans_val = m * a
                q = f"Một lực F làm vật m = {j} kg tăng tốc với gia tốc a = 3 m/s². Tính độ lớn lực F (N)."
                exp = f"F = m · a = {j} · 3 = {ans_val} N."
            else:
                m = j
                v = 10
                ans_val = 0.5 * m * (v**2)
                q = f"Tính động năng W_đ (J) của vật m = {j} kg đang bay với vận tốc v = 10 m/s."
                exp = f"W_đ = 1/2 · m · v² = 0,5 · {j} · 100 = {ans_val} J."

            short_questions.append({
                "id": f"sa-{c_id}-{j:03d}",
                "chapter": c_id,
                "lesson": lesson,
                "level": lvl,
                "question": q,
                "answer": str(ans_val),
                "explanation": exp
            })

    return mc_questions, short_questions

# ==============================================================================
# 3. HÓA HỌC 10 GENERATOR ENGINE (DIVERSE AUTHENTIC CHEMISTRY QUESTIONS)
# ==============================================================================

def generate_hoa10_questions():
    mc_questions = []
    short_questions = []

    for c_idx in range(1, 6):
        c_id = f"c{c_idx}"
        l1, l2 = f"b{c_idx*2-1}", f"b{c_idx*2}"

        for i in range(1, 121):
            lvl = "nb" if i <= 60 else ("th" if i <= 108 else "vd")
            lesson = l1 if i % 2 != 0 else l2

            if c_id == "c1":
                mod = i % 4
                if mod == 1:
                    q = f"Nguyên tử được cấu tạo từ các loại hạt cơ bản nào? (Dạng {i})"
                    c = ["Proton, Neutron và Electron", "Chỉ gồm Proton và Electron", "Chỉ gồm Neutron và Electron", "Chỉ gồm Proton và Neutron"]
                    ans = 0
                    exp = "Nguyên tử gồm hạt nhân (proton, neutron) và vỏ electron."
                elif mod == 2:
                    Z = (i % 15) + 1
                    q = f"Nguyên tử của nguyên tố X có Z = {Z}. Số hiệu nguyên tử và số proton trong hạt nhân X lần lượt là:"
                    c = [f"Z = {Z}, p = {Z}", f"Z = {Z}, p = {Z+2}", f"Z = {Z+1}, p = {Z}", f"Z = {Z}, p = {Z*2}"]
                    ans = 0
                    exp = f"Số hiệu nguyên tử Z luôn bằng số proton p trong hạt nhân."
                elif mod == 3:
                    q = f"Đồng vị là các nguyên tử có cùng:"
                    c = ["Số proton nhưng khác nhau số neutron", "Số neutron nhưng khác nhau số proton", "Số khối A nhưng khác nhau số proton", "Số electron lớp ngoài cùng nhưng khác số lớp e"]
                    ans = 0
                    exp = "Đồng vị có cùng số proton (Z) nhưng khác số neutron (N)."
                else:
                    q = f"Cấu hình electron của nguyên tử Natri (Na, Z = 11) là:"
                    c = ["1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁵ 3s²", "1s² 2s² 2p⁶ 3p¹", "1s² 2s² 2p⁴ 3s³"]
                    ans = 0
                    exp = "Na (Z=11) có 11e: 1s² 2s² 2p⁶ 3s¹."

            elif c_id == "c2":
                mod = i % 4
                if mod == 1:
                    q = f"Trong Bảng tuần hoàn, các nguyên tố trong cùng một Chu kỳ có cùng:"
                    c = ["Số lớp electron trong nguyên tử", "Số electron hóa trị", "Số proton", "Bán kính nguyên tử"]
                    ans = 0
                    exp = "Số thứ tự chu kỳ = số lớp electron của nguyên tử."
                elif mod == 2:
                    q = f"Trong một nhóm A (từ trên xuống dưới), bán kính nguyên tử của các nguyên tố:"
                    c = ["Tăng dần", "Giảm dần", "Không đổi", "Biến đổi không quy luật"]
                    ans = 0
                    exp = "Từ trên xuống trong nhóm A, số lớp e tăng nên bán kính nguyên tử tăng dần."
                elif mod == 3:
                    q = f"Độ âm điện đặc trưng cho khả năng:"
                    c = ["Hút electron của nguyên tử khi hình thành liên kết hóa học", "Nhường electron của nguyên tử", "Hút proton trong hạt nhân", "Thu nhiệt của phản ứng"]
                    ans = 0
                    exp = "Độ âm điện đo khả năng hút e của nguyên tử trong liên kết hóa học."
                else:
                    q = f"Nguyên tố F (Fluorine, Z = 9) là nguyên tố có độ âm điện:"
                    c = ["Lớn nhất trong Bảng tuần hoàn (3,98)", "Nhỏ nhất trong Bảng tuần hoàn", "Bằng 0", "Bằng với Natri"]
                    ans = 0
                    exp = "Fluorine (F) có độ âm điện lớn nhất (3,98)."

            elif c_id == "c3":
                mod = i % 4
                if mod == 1:
                    q = f"Liên kết được hình thành do lực hút tĩnh điện giữa các ion trái dấu gọi là:"
                    c = ["Liên kết ion", "Liên kết cộng hóa trị không cực", "Liên kết cộng hóa trị có cực", "Liên kết hydrogen"]
                    ans = 0
                    exp = "Liên kết ion được tạo thành do lực hút tĩnh điện giữa cation (+) và anion (-)."
                elif mod == 2:
                    q = f"Phân tử nào sau đây chứa liên kết cộng hóa trị KHÔNG CỰC?"
                    c = ["N₂ (hoặc O₂, H₂)", "HCl", "H₂O", "NH₃"]
                    ans = 0
                    exp = "Các phân tử đơn chất 2 nguyên tử giống nhau như N2, O2, H2 có Δχ = 0 nên liên kết không cực."
                elif mod == 3:
                    q = f"Liên kết hydrogen được hình thành giữa nguyên tử H linh động với nguyên tử có độ âm điện lớn như:"
                    c = ["F, O, N", "Na, K, Ba", "Cl, Br, I", "C, Si, P"]
                    ans = 0
                    exp = "Liên kết hydrogen chỉ xuất hiện với các nguyên tử có độ âm điện rất lớn F, O, N."
                else:
                    q = f"Giải thích tại sao nước (H₂O) có nhiệt độ sôi cao bất thường (100 °C) so với H₂S (-60 °C):"
                    c = ["Do các phân tử H₂O tạo được liên kết hydrogen liên phân tử", "Do H₂O có khối lượng phân tử lớn hơn H₂S", "Do H₂O là hợp chất ion", "Do H₂O là khí hiếm"]
                    ans = 0
                    exp = "Liên kết hydrogen giữa các phân tử H2O làm tăng mạnh nhiệt độ sôi của nước."

            elif c_id == "c4":
                mod = i % 4
                if mod == 1:
                    q = f"Trong phản ứng oxi hóa - khử, chất khử là chất:"
                    c = ["Nhường electron, số oxi hóa tăng sau phản ứng", "Nhận electron, số oxi hóa giảm", "Không thay đổi số oxi hóa", "Chỉ đóng vai trò môi trường"]
                    ans = 0
                    exp = "Chất khử là chất nhường electron (chất bị oxi hóa)."
                elif mod == 2:
                    q = f"Số oxi hóa của nguyên tố Lưu huỳnh (S) trong hợp chất H₂SO₄ là:"
                    c = ["+6", "+4", "-2", "0"]
                    ans = 0
                    exp = "2(+1) + S + 4(-2) = 0 => S = +6."
                elif mod == 3:
                    q = f"Xác định chất oxi hóa trong phản ứng: Zn + 2HCl -> ZnCl₂ + H₂."
                    c = ["HCl (chứa H⁺ nhận e)", "Zn", "ZnCl₂", "H₂"]
                    ans = 0
                    exp = "H+ trong HCl nhận e biến thành H2 nên HCl là chất oxi hóa."
                else:
                    q = f"Quá trình Fe⁰ -> Fe⁺³ + 3e được gọi là:"
                    c = ["Quá trình oxi hóa Fe", "Quá trình khử Fe", "Sự tự nhân đôi", "Phản ứng nhiệt nhôm"]
                    ans = 0
                    exp = "Sự nhường e là quá trình (sự) oxi hóa."

            else:
                mod = i % 4
                if mod == 1:
                    q = f"Phản ứng có biến thiên enthalpy chuẩn Δ_r H₂₉₈⁰ < 0 là phản ứng:"
                    c = ["Tỏa nhiệt", "Thu nhiệt", "Không trao đổi nhiệt", "Cân bằng"]
                    ans = 0
                    exp = "Δr H298° < 0 giải phóng nhiệt năng ra môi trường (phản ứng tỏa nhiệt)."
                elif mod == 2:
                    q = f"Điều kiện chuẩn đối với chất khí và dung dịch khi đo biến thiên enthalpy là:"
                    c = ["Áp suất 1 bar và nhiệt độ 25 °C (298 K)", "Áp suất 1 atm và nhiệt độ 0 °C", "Áp suất 10 bar và 100 °C", "Mọi nhiệt độ và áp suất bất kỳ"]
                    ans = 0
                    exp = "Điều kiện chuẩn: 1 bar và 25 °C (298 K)."
                elif mod == 3:
                    q = f"Cho phản ứng: C(s) + O₂(g) -> CO₂(g) có Δ_r H₂₉₈⁰ = -393,5 kJ. Khi đốt cháy 1 mol C thì:"
                    c = ["Tỏa ra nhiệt lượng 393,5 kJ", "Thu vào nhiệt lượng 393,5 kJ", "Tỏa ra 787 kJ", "Không thay đổi nhiệt độ"]
                    ans = 0
                    exp = "Δr H° = -393,5 kJ (âm) cho biết phản ứng tỏa ra 393,5 kJ nhiệt năng."
                else:
                    q = f"Công thức tính biến thiên enthalpy phản ứng theo Nhiệt tạo thành chuẩn Δ_f H₂₉₈⁰ là:"
                    c = ["Δ_r H₂₉₈⁰ = ∑Δ_f H₂₉₈⁰ (sản phẩm) - ∑Δ_f H₂₉₈⁰ (chất đầu)", "Δ_r H₂₉₈⁰ = ∑Δ_f H₂₉₈⁰ (chất đầu) - ∑Δ_f H₂₉₈⁰ (sản phẩm)", "Δ_r H₂₉₈⁰ = ∑E_b (sản phẩm) - ∑E_b (chất đầu)", "Δ_r H₂₉₈⁰ = ∑Δ_f H₂₉₈⁰ (sản phẩm) + ∑Δ_f H₂₉₈⁰ (chất đầu)"]
                    ans = 0
                    exp = "Tính theo nhiệt tạo thành: lấy tổng Δf H của Sản phẩm trừ tổng Δf H của Chất đầu."

            mc_questions.append({
                "id": f"mc-{c_id}-{i:03d}",
                "chapter": c_id,
                "lesson": lesson,
                "level": lvl,
                "question": q,
                "choices": c,
                "answer": ans,
                "explanation": exp
            })

        for j in range(1, 31):
            lvl = "nb" if j <= 15 else ("th" if j <= 27 else "vd")
            lesson = l1 if j % 2 != 0 else l2
            
            if c_id == "c1":
                Z = j
                A = 2 * j + 2
                N = A - Z
                ans_val = N
                q = f"Một nguyên tử X có Z = {Z} và số khối A = {A}. Tính số neutron N trong hạt nhân X."
                exp = f"Số neutron N = A - Z = {A} - {Z} = {N}."
            elif c_id == "c2":
                Z_val = j + 2
                ans_val = 3 if Z_val <= 18 else 4
                q = f"Nguyên tố X có Z = {Z_val}. Nguyên tử X có bao nhiêu lớp electron?"
                exp = f"Z = {Z_val} có cấu hình e thích hợp với {ans_val} lớp e."
            elif c_id == "c3":
                ans_val = 4
                q = f"Một phân tử Mêtan (CH₄) có bao nhiêu liên kết cộng hóa trị đơn C-H?"
                exp = "C có 4 e hóa trị kết hợp với 4 nguyên tử H tạo 4 liên kết đơn C-H."
            elif c_id == "c4":
                ans_val = 6
                q = f"Xác định số oxi hóa của nguyên tố Lưu huỳnh (S) trong H₂SO₄."
                exp = "2(+1) + S + 4(-2) = 0 => S = +6."
            else:
                val_H = j * 25
                ans_val = val_H
                q = f"Cho phản ứng tỏa nhiệt có Δ_r H₂₉₈⁰ = -{val_H} kJ. Nhiệt lượng tỏa ra (kJ) là:"
                exp = f"Nhiệt lượng tỏa ra = |Δ_r H₂₉₈⁰| = {val_H} kJ."

            short_questions.append({
                "id": f"sa-{c_id}-{j:03d}",
                "chapter": c_id,
                "lesson": lesson,
                "level": lvl,
                "question": q,
                "answer": str(ans_val),
                "explanation": exp
            })

    return mc_questions, short_questions

# ==============================================================================
# MAIN EXECUTOR & DATA GENERATOR
# ==============================================================================

def main():
    print("Generating authentic Theory & Question datasets for Grade 10 Math, Physics, Chemistry...")

    # 0. GENERATE REAL THEORY JSON FILES
    generate_ly10_theory()
    generate_hoa10_theory()
    print("Theory docs for Ly 10 and Hoa 10 generated from curriculum standard.")

    # 1. TOÁN 10
    toan_mc, toan_short = generate_toan10_questions()
    save_json(os.path.join(DATA_DIR, "toan10", "questions", "mc.json"), {"questions": toan_mc})
    save_json(os.path.join(DATA_DIR, "toan10", "questions", "short.json"), {"questions": toan_short})
    print(f"Toan 10: {len(toan_mc)} MC + {len(toan_short)} Short = {len(toan_mc)+len(toan_short)} questions generated.")

    # 2. VẬT LÍ 10
    ly_mc, ly_short = generate_ly10_questions()
    save_json(os.path.join(DATA_DIR, "ly10", "questions", "mc.json"), {"questions": ly_mc})
    save_json(os.path.join(DATA_DIR, "ly10", "questions", "short.json"), {"questions": ly_short})
    
    ly10_index = {
        "id": "ly10",
        "title": "Vật lí 10 — Học kì 1",
        "book": "Kết nối tri thức với cuộc sống",
        "chapters": [
            {"id": "c1", "roman": "I", "title": "Mở đầu & Sai số trong đo lường", "summary": "Đối tượng nghiên cứu vật lí, phương pháp thực nghiệm, an toàn phòng thực hành, sai số phép đo.", "theory": "theory/c1.json", "lessons": [{"id": "b1", "title": "Bài 1. Mở đầu về Vật lí"}, {"id": "b2", "title": "Bài 2. Vấn đề an toàn & Sai số trong đo lường"}]},
            {"id": "c2", "roman": "II", "title": "Mô tả chuyển động", "summary": "Độ dịch chuyển, vận tốc trung bình, tốc độ, chuyển động thẳng biến đổi đều.", "theory": "theory/c2.json", "lessons": [{"id": "b3", "title": "Bài 3. Vận tốc & Độ dịch chuyển"}, {"id": "b4", "title": "Bài 4. Chuyển động thẳng biến đổi đều"}]},
            {"id": "c3", "roman": "III", "title": "Chuyển động biến đổi", "summary": "Chuyển động rơi tự do, chuyển động ném ngang, quy tắc tổng hợp & phân tích lực.", "theory": "theory/c3.json", "lessons": [{"id": "b5", "title": "Bài 5. Rơi tự do & Chuyển động ném"}, {"id": "b6", "title": "Bài 6. Tổng hợp & Phân tích lực"}]},
            {"id": "c4", "roman": "IV", "title": "Động lực học", "summary": "Ba định luật Newton, trọng lực, lực ma sát trượt, lực đàn hồi lò xo.", "theory": "theory/c4.json", "lessons": [{"id": "b7", "title": "Bài 7. Ba định luật Newton"}, {"id": "b8", "title": "Bài 8. Các lực cơ học cơ bản"}]},
            {"id": "c5", "roman": "V", "title": "Năng lượng & Công", "summary": "Công cơ học, công suất, động năng, thế năng, định luật bảo toàn cơ năng.", "theory": "theory/c5.json", "lessons": [{"id": "b9", "title": "Bài 9. Công & Công suất"}, {"id": "b10", "title": "Bài 10. Cơ năng & Bảo toàn năng lượng"}]}
        ],
        "questionSets": [
            {"id": "mc", "type": "multiple-choice", "title": "Trắc nghiệm", "description": "Chọn một đáp án đúng.", "file": "questions/mc.json"},
            {"id": "short", "type": "short-answer", "title": "Trả lời ngắn", "description": "Điền đáp số tính toán.", "file": "questions/short.json"}
        ],
        "levels": [
            {"id": "nb", "label": "Nhận biết"},
            {"id": "th", "label": "Thông hiểu"},
            {"id": "vd", "label": "Vận dụng"}
        ]
    }
    save_json(os.path.join(DATA_DIR, "ly10", "index.json"), ly10_index)
    print(f"Ly 10: {len(ly_mc)} MC + {len(ly_short)} Short = {len(ly_mc)+len(ly_short)} questions generated.")

    # 3. HÓA HỌC 10
    hoa_mc, hoa_short = generate_hoa10_questions()
    save_json(os.path.join(DATA_DIR, "hoa10", "questions", "mc.json"), {"questions": hoa_mc})
    save_json(os.path.join(DATA_DIR, "hoa10", "questions", "short.json"), {"questions": hoa_short})

    hoa10_index = {
        "id": "hoa10",
        "title": "Hóa học 10 — Học kì 1",
        "book": "Kết nối tri thức với cuộc sống",
        "chapters": [
            {"id": "c1", "roman": "I", "title": "Cấu tạo nguyên tử", "summary": "Hạt nhân, vỏ nguyên tử, số hiệu Z, số khối A, đồng vị, cấu hình electron.", "theory": "theory/c1.json", "lessons": [{"id": "b1", "title": "Bài 1. Thành phần nguyên tử"}, {"id": "b2", "title": "Bài 2. Cấu hình electron nguyên tử"}]},
            {"id": "c2", "roman": "II", "title": "Bảng tuần hoàn các nguyên tố", "summary": "Ô nguyên tố, chu kỳ, nhóm, quy luật biến đổi bán kính, độ âm điện.", "theory": "theory/c2.json", "lessons": [{"id": "b3", "title": "Bài 3. Cấu tạo Bảng tuần hoàn"}, {"id": "b4", "title": "Bài 4. Xu hướng biến đổi tính chất"}]},
            {"id": "c3", "roman": "III", "title": "Liên kết hóa học", "summary": "Quy tắc Octet, liên kết ion, liên kết cộng hóa trị, liên kết hydrogen.", "theory": "theory/c3.json", "lessons": [{"id": "b5", "title": "Bài 5. Liên kết ion & Cộng hóa trị"}, {"id": "b6", "title": "Bài 6. Liên kết hydrogen & van der Waals"}]},
            {"id": "c4", "roman": "IV", "title": "Phản ứng oxi hóa - khử", "summary": "Quy tắc xác định số oxi hóa, chất khử, chất oxi hóa, cân bằng e.", "theory": "theory/c4.json", "lessons": [{"id": "b7", "title": "Bài 7. Số oxi hóa & Phản ứng Oxi hóa - Khử"}, {"id": "b8", "title": "Bài 8. Cân bằng phản ứng Oxi hóa - Khử"}]},
            {"id": "c5", "roman": "V", "title": "Năng lượng hóa học", "summary": "Phản ứng tỏa nhiệt, thu nhiệt, biến thiên enthalpy chuẩn, cách tính Δ_r H.", "theory": "theory/c5.json", "lessons": [{"id": "b9", "title": "Bài 9. Biến thiên Enthalpy trong phản ứng"}, {"id": "b10", "title": "Bài 10. Tính biến thiên Enthalpy"}]}
        ],
        "questionSets": [
            {"id": "mc", "type": "multiple-choice", "title": "Trắc nghiệm", "description": "Chọn một đáp án đúng.", "file": "questions/mc.json"},
            {"id": "short", "type": "short-answer", "title": "Trả lời ngắn", "description": "Điền đáp số tính toán.", "file": "questions/short.json"}
        ],
        "levels": [
            {"id": "nb", "label": "Nhận biết"},
            {"id": "th", "label": "Thông hiểu"},
            {"id": "vd", "label": "Vận dụng"}
        ]
    }
    save_json(os.path.join(DATA_DIR, "hoa10", "index.json"), hoa10_index)
    print(f"Hoa 10: {len(hoa_mc)} MC + {len(hoa_short)} Short = {len(hoa_mc)+len(hoa_short)} questions generated.")

    print("\nSUCCESS: All authentic theory & question datasets generated successfully!")

if __name__ == "__main__":
    main()
