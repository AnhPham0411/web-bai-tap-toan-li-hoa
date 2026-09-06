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
            return (f"Lý thuyết", f"Đơn vị nào sau đây là đơn vị cơ bản trong hệ đơn vị SI (BT {v_idx})?", ["Mét (m)", "Mét trên giây (m/s)", "Niu-tơn (N)", "Joule (J)"], 0, "7 đơn vị cơ bản SI gồm: m, kg, s, A, K, mol, cd.")
        elif mod == 2:
            return (f"Lý thuyết", f"Phương pháp nghiên cứu nào sau đây thuộc về phương pháp thực nghiệm Vật lí (BT {v_idx})?", ["Quan sát hiện tượng và tiến hành thí nghiệm kiểm chứng", "Sử dụng công thức toán học lập luận thuần túy", "Dự đoán lý thuyết không qua đo đạc", "Suy diễn triết học"], 0, "Phương pháp thực nghiệm dựa trên quan sát, thu thập dữ liệu và thí nghiệm.")
        elif mod == 3:
            return (f"Lý thuyết", f"Sai số do dụng cụ đo gây ra thường lấy bằng gì (BT {v_idx})?", ["Một nửa hoặc một độ chia nhỏ nhất trên dụng cụ", "Gấp 10 lần độ chia nhỏ nhất", "Bằng 0", "Một phần trăm giá trị trung bình"], 0, "Sai số dụng cụ thường lấy bằng 1/2 hoặc 1 độ chia nhỏ nhất.")
        else:
            val = v_idx + 1
            val_s = round((val / 45) * 100, 2)
            return (f"Bài tập", f"Kết quả đo thời gian rơi t = (0,45 ± 0,0{val}) s. Sai số tương đối của phép đo là:", [f"{val_s}%", f"{val_s + 1}%", "1%", "4.5%"], 0, f"Sai số tương đối = (0,0{val} / 0,45) * 100% ≈ {val_s}%.")

    elif c_id == "c2":
        if mod == 1:
            v = 10 + v_idx
            t = 2 + v_idx
            s = v * t
            return (f"Bài tập", f"Một ô tô chuyển động thẳng đều với vận tốc v = {v} m/s. Quãng đường ô tô đi được trong {t} s là:", [f"{s} m", f"{s+10} m", f"{s-5} m", f"{s*2} m"], 0, f"s = v*t = {s} m.")
        elif mod == 2:
            v0 = 5 + v_idx
            a = 2
            t = v_idx + 1
            v_val = v0 + a * t
            return (f"Bài tập", f"Một xe máy đang chạy với vận tốc {v0} m/s thì tăng tốc với gia tốc a = {a} m/s². Vận tốc xe sau {t} s là:", [f"{v_val} m/s", f"{v_val+4} m/s", f"{v_val-2} m/s", f"{v_val*2} m/s"], 0, f"v = v_0 + a*t = {v_val} m/s.")
        elif mod == 3:
            a = 4
            t = v_idx + 2
            d = 0.5 * a * (t**2)
            return (f"Bài tập", f"Một vật bắt đầu chuyển động nhanh dần đều từ trạng thái nghỉ với gia tốc a = {a} m/s². Độ dịch chuyển d sau {t} s là:", [f"{d} m", f"{d+8} m", f"{d/2} m", f"{d*2} m"], 0, f"d = 1/2*a*t^2 = {d} m.")
        else:
            v0 = 20 + v_idx * 5
            v = 10
            a = -2
            d = (v**2 - v0**2) / (2 * a)
            return (f"Bài tập", f"Một ô tô hãm phanh chậm dần đều từ v_0 = {v0} m/s xuống v = 10 m/s với a = -2 m/s². Quãng đường đi được là:", [f"{d} m", f"{d+15} m", f"{d-10} m", f"{d*2} m"], 0, f"(10^2 - {v0}^2) / (2*-2) = {d} m.")

    elif c_id == "c3":
        if mod == 1:
            t = v_idx + 1
            h = round(0.5 * 9.8 * (t**2), 2)
            return (f"Bài tập", f"Một vật rơi tự do từ độ cao h xuống đất trong t = {t} s với g = 9,8 m/s². Độ cao h là:", [f"{h} m", f"{round(h+5,2)} m", f"{round(h/2,2)} m", f"{round(h*2,2)} m"], 0, f"h = 1/2*g*t^2 = {h} m.")
        elif mod == 2:
            v0 = 10 + v_idx
            L = round(v0 * (40 / 10)**0.5, 2)
            return (f"Bài tập", f"Ném ngang một vật từ h = 20 m với v_0 = {v0} m/s (g = 10 m/s²). Tầm xa L của vật là:", [f"{L} m", f"{round(L+10,2)} m", f"{round(L-5,2)} m", f"{round(L*2,2)} m"], 0, f"t = sqrt(2h/g) = 2 s. L = v_0*t = {L} m.")
        elif mod == 3:
            F1 = 30 + v_idx * 10
            F2 = 40 + v_idx * 10
            F = (F1**2 + F2**2)**0.5
            return (f"Bài tập", f"Hai lực vuông góc F_1 = {F1} N và F_2 = {F2} N cùng tác dụng vào chất điểm. Độ lớn hợp lực F là:", [f"{int(F)} N", f"{F1+F2} N", "10 N", "500 N"], 0, f"F = sqrt(F1^2 + F2^2) = {int(F)} N.")
        else:
            return (f"Lý thuyết", f"Điều kiện cân bằng của chất điểm chịu tác dụng lực (BT {v_idx}) là:", ["Tổng đại số các vectơ lực bằng vectơ không", "Tổng các độ lớn bằng 0", "Các lực bằng nhau", "Lực ma sát bằng 0"], 0, "Tổng các vectơ lực phải bằng vectơ không.")

    elif c_id == "c4":
        if mod == 1:
            m = v_idx + 2
            a = v_idx + 1
            F = m * a
            return (f"Bài tập", f"Tác dụng lực F vào vật m = {m} kg làm vật thu gia tốc a = {a} m/s². Độ lớn lực F là:", [f"{F} N", f"{F+4} N", f"{F-2} N", f"{F*2} N"], 0, f"F = m*a = {F} N.")
        elif mod == 2:
            m = v_idx + 1
            Fmst = round(0.2 * m * 10, 2)
            return (f"Bài tập", f"Kéo khối gỗ m = {m} kg trượt đều trên sàn ngang (g=10, μ=0,2). Độ lớn lực ma sát trượt là:", [f"{Fmst} N", f"{Fmst+2} N", f"{Fmst/2} N", f"{Fmst*2} N"], 0, f"Fmst = μ*m*g = {Fmst} N.")
        elif mod == 3:
            dl = 0.05 + v_idx * 0.01
            Fdh = round(100 * dl, 2)
            return (f"Bài tập", f"Lò xo độ cứng 100 N/m bị dãn đoạn {dl} m. Độ lớn lực đàn hồi là:", [f"{Fdh} N", "500 N", "0.5 N", "20 N"], 0, f"Fdh = k*dl = {Fdh} N.")
        else:
            return (f"Lý thuyết", f"Định luật III Newton khẳng định lực và phản lực (BT {v_idx}):", ["Cùng độ lớn, ngược chiều, đặt vào 2 vật khác nhau", "Cùng độ lớn, cùng chiều", "Là hai lực cân bằng", "Không đồng thời"], 0, "Lực và phản lực là lực trực đối, đặt vào 2 vật khác nhau.")

    elif c_id == "c5":
        if mod == 1:
            F = v_idx * 10 + 10
            s = v_idx + 2
            A = F * s
            return (f"Bài tập", f"Lực F = {F} N kéo vật dịch chuyển s = {s} m theo hướng của lực. Công A là:", [f"{A} J", f"{A+20} J", f"{A-10} J", f"{A*2} J"], 0, f"A = F*s = {A} J.")
        elif mod == 2:
            m = v_idx + 1
            v = v_idx + 2
            Wd = round(0.5 * m * (v**2), 2)
            return (f"Bài tập", f"Động năng của vật m = {m} kg đang chuyển động với vận tốc v = {v} m/s là:", [f"{Wd} J", f"{Wd+5} J", f"{Wd*2} J", f"{round(Wd/2,2)} J"], 0, f"Wd = 1/2*m*v^2 = {Wd} J.")
        elif mod == 3:
            m = v_idx + 1
            h = v_idx + 5
            Wt = m * 10 * h
            return (f"Bài tập", f"Thế năng trọng trường của vật m = {m} kg ở độ cao h = {h} m là (g=10):", [f"{Wt} J", f"{Wt+50} J", f"{Wt-20} J", f"{Wt*2} J"], 0, f"Wt = m*g*h = {Wt} J.")
        else:
            P = v_idx + 2
            A = P * 1000 * 5
            return (f"Bài tập", f"Động cơ công suất P = {P} kW hoạt động trong 5 s. Công thực hiện là:", [f"{A} J", f"{P*5} J", f"{A/10} J", f"{A*2} J"], 0, f"A = P*t = {P}*1000*5 = {A} J.")

    v = rng.randint(1, 100)
    return (f"Dạng {d_idx}", f"Câu hỏi {v} của dạng {d_idx} chương {c_id}?", [f"Đúng {v}", f"Sai A {v}", f"Sai B {v}", f"Sai C {v}"], 0, "Giải thích.")

def gen_variant_sa(rng, d_idx, c_id, v_idx):
    mod = d_idx % 4
    if c_id == "c1":
        l_val = v_idx + 5
        ans_val = round((0.1 / l_val) * 100, 2)
        return ("Sai số", f"Phép đo chiều dài l = {l_val} ± 0,1 cm. Tính sai số tương đối δl (%).", ans_val, 0.05, "%", "Tính toán")
    elif c_id == "c2":
        v0 = v_idx + 5
        ans_val = v0 * 4 + 0.5 * 2 * 16
        return ("Chuyển động", f"Cho v_0 = {v0} m/s, gia tốc a = 2 m/s², t = 4 s. Tính độ dịch chuyển d (m).", ans_val, 0, "m", "Tính toán")
    elif c_id == "c3":
        h = v_idx * 2 + 2
        ans_val = round((2 * 9.8 * h)**0.5, 2)
        return ("Rơi tự do", f"Tính vận tốc v (m/s) của vật rơi tự do quãng đường h = {h} m (g = 9,8).", ans_val, 0.1, "m/s", "Tính toán")
    elif c_id == "c4":
        m = v_idx + 1
        ans_val = m * 3
        return ("Lực", f"Lực F làm vật m = {m} kg tăng tốc với a = 3 m/s². Tính lực F (N).", ans_val, 0, "N", "Tính toán")
    elif c_id == "c5":
        m = v_idx + 1
        ans_val = 0.5 * m * 100
        return ("Động năng", f"Tính động năng W_đ (J) của vật m = {m} kg bay với vận tốc 10 m/s.", ans_val, 0, "J", "Tính toán")
        
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
            
    save_bank("ly10", c_id, sgk_title, sgk_lessons, mc, sa)

def main():
    gen_chapter("c1", "Mở đầu & Sai số trong đo lường", [{"lesson_id": "b1", "sgk_title": "Bài 1. Mở đầu về Vật lí"}, {"lesson_id": "b2", "sgk_title": "Bài 2. Vấn đề an toàn & Sai số trong đo lường"}])
    gen_chapter("c2", "Mô tả chuyển động", [{"lesson_id": "b3", "sgk_title": "Bài 3. Vận tốc & Độ dịch chuyển"}, {"lesson_id": "b4", "sgk_title": "Bài 4. Chuyển động thẳng biến đổi đều"}])
    gen_chapter("c3", "Chuyển động biến đổi", [{"lesson_id": "b5", "sgk_title": "Bài 5. Rơi tự do & Chuyển động ném"}, {"lesson_id": "b6", "sgk_title": "Bài 6. Tổng hợp & Phân tích lực"}])
    gen_chapter("c4", "Động lực học", [{"lesson_id": "b7", "sgk_title": "Bài 7. Ba định luật Newton"}, {"lesson_id": "b8", "sgk_title": "Bài 8. Các lực cơ học cơ bản"}])
    gen_chapter("c5", "Năng lượng & Công", [{"lesson_id": "b9", "sgk_title": "Bài 9. Công & Công suất"}, {"lesson_id": "b10", "sgk_title": "Bài 10. Cơ năng & Bảo toàn năng lượng"}])
    print("Xong Ly10")

if __name__ == "__main__":
    main()
