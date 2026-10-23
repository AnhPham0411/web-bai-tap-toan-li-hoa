# -*- coding: utf-8 -*-
"""Vật lí 10 (KNTT): mỗi câu tính bằng code từ công thức, đáp án nhiễu là các lỗi thường gặp."""
import math
from fractions import Fraction as F
from .common import Bank, fnum
from .phys import fmt, nm, sa

def c1():
    b = Bank('ly10', 'c1')
    # ---- lý thuyết (b1) ----
    T = [
     ('nb', 'Đối tượng nghiên cứu', "Vật lí học nghiên cứu chủ yếu về:", "Các dạng vận động của vật chất và năng lượng", ["Sự sống và quá trình trao đổi chất", "Các phản ứng hoá học giữa các chất", "Cấu trúc xã hội của loài người"], "Vật lí học nghiên cứu các dạng vận động của vật chất (cơ, nhiệt, điện, quang, hạt nhân...) và năng lượng."),
     ('nb', 'Phương pháp nghiên cứu', "Phương pháp thực nghiệm trong Vật lí có các bước chính nào?", "Quan sát, đặt giả thuyết, làm thí nghiệm kiểm tra, rút ra kết luận", ["Chỉ cần suy luận lí thuyết rồi kết luận", "Chỉ ghi chép lại số liệu có sẵn", "Chọn kết quả phù hợp với mong muốn rồi báo cáo"], "Phương pháp thực nghiệm: quan sát hiện tượng, đề xuất giả thuyết, thiết kế và tiến hành thí nghiệm, phân tích số liệu và rút ra kết luận."),
     ('nb', 'Phương pháp nghiên cứu', "Phương pháp lí thuyết trong Vật lí dựa chủ yếu vào:", "Ngôn ngữ toán học và suy luận logic để dự đoán tính chất, quy luật", ["Việc đo đạc trực tiếp bằng dụng cụ", "Việc quan sát bằng mắt thường", "Ý kiến số đông của người quan sát"], "Phương pháp lí thuyết dùng toán học và suy luận logic để xây dựng mô hình, dự đoán quy luật; kết quả vẫn phải được kiểm chứng bằng thực nghiệm."),
     ('nb', 'Đơn vị SI', "Đơn vị nào sau đây là đơn vị cơ bản trong hệ SI?", "Kilôgam (kg)", ["Niutơn (N)", "Jun (J)", "Oát (W)"], "Bảy đơn vị cơ bản của SI: mét (m), kilôgam (kg), giây (s), ampe (A), kenvin (K), mol, canđêla (cd). N, J, W là đơn vị dẫn xuất."),
     ('nb', 'Đơn vị SI', "Đơn vị của lực trong hệ SI là:", "Niutơn (N)", ["Jun (J)", "Oát (W)", "Paxcan (Pa)"], "Lực có đơn vị niutơn, kí hiệu N; $1\\ \\text{N}=1\\ \\text{kg}\\cdot\\text{m/s}^2$."),
     ('nb', 'Đơn vị SI', "Đơn vị của công suất trong hệ SI là:", "Oát (W)", ["Jun (J)", "Niutơn (N)", "Mét trên giây (m/s)"], "Công suất $\\mathcal{P}=\\dfrac{A}{t}$ có đơn vị jun trên giây, gọi là oát (W)."),
     ('nb', 'Thứ nguyên', "Thứ nguyên của vận tốc là:", "$LT^{-1}$", ["$L^2T^{-1}$", "$LT^{-2}$", "$LT$"], "Vận tốc = độ dài / thời gian nên thứ nguyên là $L\\cdot T^{-1}$."),
     ('th', 'Thứ nguyên', "Thứ nguyên của gia tốc là:", "$LT^{-2}$", ["$LT^{-1}$", "$L^2T^{-2}$", "$L^{-1}T^{2}$"], "Gia tốc = vận tốc / thời gian nên thứ nguyên là $LT^{-1}/T=LT^{-2}$."),
     ('th', 'Thứ nguyên', "Thứ nguyên của lực (theo $M$, $L$, $T$) là:", "$MLT^{-2}$", ["$MLT^{-1}$", "$ML^2T^{-2}$", "$ML^{-1}T^{-2}$"], "Lực $F=ma$ nên thứ nguyên là khối lượng nhân gia tốc: $M\\cdot LT^{-2}=MLT^{-2}$."),
     ('nb', 'An toàn thí nghiệm', "Khi làm thí nghiệm với dụng cụ điện, biện pháp an toàn nào sau đây là ĐÚNG?", "Kiểm tra dây dẫn, cách điện và ngắt nguồn điện trước khi lắp hoặc sửa mạch", ["Dùng tay ướt để cắm phích điện cho nhanh", "Sửa mạch khi nguồn điện vẫn đang bật", "Bỏ qua việc kiểm tra dây dẫn nếu thấy vội"], "Phải kiểm tra cách điện, ngắt nguồn trước khi thao tác và không chạm vào thiết bị điện bằng tay ướt."),
     ('nb', 'An toàn thí nghiệm', "Biển báo có hình tia lửa điện và dấu hiệu nguy hiểm thường cảnh báo:", "Nguy cơ bị điện giật", ["Chất dễ cháy", "Chất độc hại cho hô hấp", "Khu vực cấm hút thuốc"], "Biển cảnh báo có tia lửa điện (mũi tên gấp khúc) là biển báo nguy hiểm về điện, có nguy cơ bị điện giật."),
     ('nb', 'Đại lượng vectơ', "Đại lượng nào sau đây là đại lượng vectơ?", "Lực", ["Khối lượng", "Thời gian", "Nhiệt độ"], "Lực có độ lớn, phương và chiều nên là đại lượng vectơ; khối lượng, thời gian, nhiệt độ chỉ có độ lớn (đại lượng vô hướng)."),
     ('nb', 'Phân loại đại lượng', "Đại lượng nào sau đây là đại lượng vô hướng?", "Quãng đường", ["Độ dịch chuyển", "Vận tốc", "Gia tốc"], "Quãng đường chỉ có độ lớn nên là đại lượng vô hướng; độ dịch chuyển, vận tốc, gia tốc có hướng nên là vectơ."),
    ]
    for (lv, dg, st, ok, ws, ex) in T:
        b.mc('b1', lv, dg, st, ok, ws, ex)
    # ---- đổi đơn vị (b1) ----
    for v in (18, 36, 54, 72, 90, 108):
        nm(b, 'b1', 'nb', 'Đổi đơn vị', f"Đổi {v} km/h sang m/s.", v / 3.6, [v * 3.6, v / 6, v / 1.6], 'm/s', f"$1\\ \\text{{km/h}}=\\dfrac{{1000}}{{3600}}\\ \\text{{m/s}}=\\dfrac{{1}}{{3{{,}}6}}\\ \\text{{m/s}}$ nên ${v}\\ \\text{{km/h}}=\\dfrac{{{v}}}{{3{{,}}6}}={fnum(v/3.6)}\\ \\text{{m/s}}$.")
        sa(b, 'b1', 'nb', 'Đổi đơn vị', f"Một xe chạy với tốc độ {v} km/h. Tốc độ đó bằng bao nhiêu m/s?", v / 3.6, f"Chia cho $3{{,}}6$: ${v}:3{{,}}6={fnum(v/3.6)}$ m/s.", 'm/s')
    for v in (5, 10, 15, 20, 25, 30):
        nm(b, 'b1', 'nb', 'Đổi đơn vị', f"Đổi {v} m/s sang km/h.", v * 3.6, [v / 3.6, v * 6, v * 1.6], 'km/h', f"Nhân với $3{{,}}6$: ${v}\\times3{{,}}6={fnum(v*3.6)}$ km/h.")
    for (h, m_, s_) in ((1, 30, 0), (2, 15, 0), (0, 45, 30), (1, 0, 45)):
        tot = h * 3600 + m_ * 60 + s_
        nm(b, 'b1', 'nb', 'Đổi đơn vị thời gian', f"Đổi {h} h {m_} min {s_} s sang đơn vị giây (s).", tot, [h * 60 + m_ + s_, tot / 60, h * 3600 + m_ + s_], 's', f"${h}\\ \\text{{h}}={h*3600}$ s; ${m_}\\ \\text{{min}}={m_*60}$ s; cộng với ${s_}$ s được ${tot}$ s.", nd=0)
    for (cm, ) in ((250,), (35,), (1200,), (75,)):
        nm(b, 'b1', 'nb', 'Đổi đơn vị độ dài', f"Đổi {cm} cm sang mét (m).", cm / 100, [cm / 10, cm / 1000, cm * 100], 'm', f"$1\\ \\text{{cm}}=0{{,}}01\\ \\text{{m}}$ nên ${cm}\\ \\text{{cm}}={fnum(cm/100)}\\ \\text{{m}}$.")
    for g in (250, 500, 1500, 80):
        nm(b, 'b1', 'nb', 'Đổi đơn vị khối lượng', f"Đổi {g} g sang kilôgam (kg).", g / 1000, [g / 100, g / 10, g * 1000], 'kg', f"$1\\ \\text{{g}}=0{{,}}001\\ \\text{{kg}}$ nên ${g}\\ \\text{{g}}={fnum(g/1000,3)}\\ \\text{{kg}}$.", nd=3)
    # ---- sai số (b2) ----
    sets = [((2.0, 2.2, 2.1, 2.1), 'g_t'), ((10.2, 10.4, 10.3, 10.1), 't'), ((4.5, 4.7, 4.6, 4.6), 'l'), ((1.20, 1.24, 1.22, 1.22), 'l')]
    names = [("chiều dài", "cm"), ("thời gian rơi", "s"), ("chiều dài bàn", "m"), ("đường kính", "cm")]
    for ((vals, _), (nmx, un)) in zip(sets, names):
        mean = sum(F(str(v)) for v in vals) / len(vals)
        dev = sum(abs(F(str(v)) - mean) for v in vals) / len(vals)
        vs = "; ".join(fnum(v, 2) for v in vals)
        nm(b, 'b2', 'th', 'Giá trị trung bình', f"Đo {nmx} bốn lần được các kết quả ({un}): {vs}. Giá trị trung bình là:", float(mean), [vals[0], max(vals), float(mean) + 0.05], un, f"$\\bar{{A}}=\\dfrac{{{' + '.join(fnum(v,2) for v in vals)}}}{{4}}={fnum(float(mean),3)}$ ({un}).", nd=3) if False else nm(b, 'b2', 'th', 'Giá trị trung bình', f"Đo {nmx} bốn lần được các kết quả ({un}): {vs}. Giá trị trung bình là:", float(mean), [vals[0], max(vals), float(mean) + 0.05], un, f"Giá trị trung bình $\\bar{{A}}=\\dfrac{{{' + '.join(fnum(v,2) for v in vals)}}}{{4}}={fnum(float(mean),3)}$ ({un}).", nd=3)
        nm(b, 'b2', 'th', 'Sai số tuyệt đối trung bình', f"Đo {nmx} bốn lần được các kết quả ({un}): {vs}. Sai số tuyệt đối trung bình $\\overline{{\\Delta A}}$ (chỉ tính sai số ngẫu nhiên) là:", float(dev), [float(dev) * 2, float(mean) - min(vals), max(vals) - float(mean) + 0.05], un, f"Giá trị trung bình là ${fnum(float(mean),3)}$. Các sai số tuyệt đối từng lần: " + ", ".join(fnum(float(abs(F(str(v)) - mean)), 3) for v in vals) + f". Trung bình của chúng là ${fnum(float(dev),3)}$ ({un}).", nd=3)
        if float(dev).is_integer() or abs(float(dev) - round(float(dev), 2)) < 1e-9:
            sa(b, 'b2', 'th', 'Sai số tuyệt đối trung bình', f"Đo {nmx} bốn lần được các kết quả ({un}): {vs}. Tính sai số tuyệt đối trung bình (làm tròn đến hai chữ số thập phân).", float(dev), f"Giá trị trung bình ${fnum(float(mean),3)}$; sai số từng lần: " + ", ".join(fnum(float(abs(F(str(v)) - mean)), 3) for v in vals) + f"; trung bình là ${fnum(float(dev),3)}$.", un)
    for (A, d) in ((50, 1), (20, 1), (25, 1), (40, 2), (200, 4), (10, 0.5), (8, 0.2), (60, 3)):
        r = d / A * 100
        nm(b, 'b2', 'th', 'Sai số tương đối', f"Kết quả đo $A=({A}\\pm{fnum(d)})$ (đơn vị). Sai số tương đối của phép đo là:", r, [d / A, A / d, d * A], '%', f"$\\delta A=\\dfrac{{\\Delta A}}{{\\bar A}}\\cdot100\\%=\\dfrac{{{fnum(d)}}}{{{A}}}\\cdot100\\%={fnum(r)}\\%$.")
        sa(b, 'b2', 'th', 'Sai số tương đối', f"Đo $A=({A}\\pm{fnum(d)})$ (đơn vị). Tính sai số tương đối (đơn vị %).", r, f"$\\delta A=\\dfrac{{\\Delta A}}{{\\bar A}}\\cdot100\\%=\\dfrac{{{fnum(d)}}}{{{A}}}\\cdot100\\%={fnum(r)}\\%$.", '%')
    for (l1, d1, l2, d2) in ((10.0, 0.1, 5.0, 0.1), (20.5, 0.2, 4.5, 0.1), (8.0, 0.05, 2.0, 0.05), (15.0, 0.2, 10.0, 0.3)):
        tot, dt = l1 + l2, d1 + d2
        nm(b, 'b2', 'vd', 'Sai số của tổng', f"Đo hai đoạn $l_1=({fnum(l1)}\\pm{fnum(d1)})$ cm và $l_2=({fnum(l2)}\\pm{fnum(d2)})$ cm. Chiều dài $L=l_1+l_2$ có sai số tuyệt đối là:", dt, [abs(d1 - d2), d1 * d2, dt / 2], 'cm', f"Với tổng, sai số tuyệt đối bằng tổng các sai số tuyệt đối: $\\Delta L=\\Delta l_1+\\Delta l_2={fnum(d1)}+{fnum(d2)}={fnum(dt)}$ cm.", nd=2)
        nm(b, 'b2', 'vd', 'Sai số của hiệu', f"Đo $l_1=({fnum(l1)}\\pm{fnum(d1)})$ cm và $l_2=({fnum(l2)}\\pm{fnum(d2)})$ cm. Sai số tuyệt đối của hiệu $d=l_1-l_2$ là:", dt, [abs(d1 - d2), d1 * d2, dt * 2], 'cm', f"Với hiệu, sai số tuyệt đối vẫn bằng tổng các sai số tuyệt đối: $\\Delta d=\\Delta l_1+\\Delta l_2={fnum(dt)}$ cm.", nd=2)
    for (da, db) in ((2, 3), (1, 2), (3, 4), (2, 5)):
        nm(b, 'b2', 'vd', 'Sai số của tích', f"Diện tích $S=a\\cdot b$ với sai số tương đối của $a$ là ${da}\\%$ và của $b$ là ${db}\\%$. Sai số tương đối của $S$ là:", da + db, [da * db, abs(da - db), (da + db) / 2], '%', f"Với tích, sai số tương đối bằng tổng các sai số tương đối: $\\delta S=\\delta a+\\delta b={da}\\%+{db}\\%={da+db}\\%$.")
        sa(b, 'b2', 'vd', 'Sai số của thương', f"Vận tốc $v=\\dfrac{{s}}{{t}}$ với sai số tương đối của $s$ là ${da}\\%$ và của $t$ là ${db}\\%$. Tính sai số tương đối của $v$ (%).", da + db, f"Với thương, sai số tương đối cũng bằng tổng: $\\delta v=\\delta s+\\delta t={da}\\%+{db}\\%={da+db}\\%$.", '%')
    b.mc('b2', 'nb', 'Phân loại sai số', "Sai số hệ thống là sai số:", "Có xu hướng làm kết quả lệch về một phía, thường do dụng cụ hoặc phương pháp đo", ["Xuất hiện hoàn toàn ngẫu nhiên, lúc lệch lên lúc lệch xuống", "Chỉ do người đo đọc nhầm số liệu", "Luôn bằng không nếu đo nhiều lần"], "Sai số hệ thống làm kết quả lệch có hệ thống về một phía (ví dụ kim chỉ không bị lệch vạch 0); sai số ngẫu nhiên mới có thể giảm bằng cách đo nhiều lần.")
    b.mc('b2', 'nb', 'Phân loại sai số', "Để giảm sai số ngẫu nhiên, ta nên:", "Đo nhiều lần rồi lấy giá trị trung bình", ["Chỉ đo một lần nhưng đo thật cẩn thận", "Chọn kết quả lần đo đầu tiên", "Bỏ các kết quả khác với mong đợi"], "Sai số ngẫu nhiên có thể giảm bằng cách lặp lại phép đo nhiều lần và lấy trung bình.")
    b.mc('b2', 'nb', 'Sai số dụng cụ', "Sai số dụng cụ của một thước thường được lấy bằng:", "Một nửa độ chia nhỏ nhất hoặc một độ chia nhỏ nhất của thước", ["Gấp đôi độ chia lớn nhất", "Bằng không", "Đúng bằng giá trị đo được"], "Sai số dụng cụ thường lấy bằng một độ chia nhỏ nhất (hoặc nửa độ chia nhỏ nhất) của dụng cụ.")
    return b

def c2():
    b = Bank('ly10', 'c2')
    # ---- b3: độ dịch chuyển, vận tốc ----
    for (a, c, d) in ((3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)):
        nm(b, 'b3', 'th', 'Độ dịch chuyển', f"Một người đi {a} m về hướng đông rồi đi tiếp {c} m về hướng bắc. Độ lớn độ dịch chuyển của người đó là:", d, [a + c, abs(c - a), (a + c) / 2], 'm', f"Hai đoạn vuông góc nên $d=\\sqrt{{{a}^2+{c}^2}}=\\sqrt{{{a*a+c*c}}}={d}$ m.")
        nm(b, 'b3', 'th', 'Quãng đường', f"Một người đi {a} m về hướng đông rồi đi tiếp {c} m về hướng bắc. Quãng đường người đó đã đi là:", a + c, [d, abs(c - a), a * c], 'm', f"Quãng đường là tổng độ dài các đoạn đã đi: ${a}+{c}={a+c}$ m.")
    for L in (50, 100, 200, 400):
        nm(b, 'b3', 'th', 'Đi và về', f"Một người chạy từ A đến B cách nhau {L} m rồi chạy ngược về A. Độ dịch chuyển của người đó là:", 0, [L, 2 * L, L / 2], 'm', f"Điểm đầu và điểm cuối trùng nhau (cùng ở A) nên độ dịch chuyển bằng $0$, còn quãng đường là ${2*L}$ m.") if False else \
        b.mc('b3', 'th', 'Đi và về', f"Một người chạy từ A đến B cách nhau {L} m rồi chạy ngược về A. Độ dịch chuyển và quãng đường của người đó lần lượt là:", f"0 m và {2*L} m", [f"{L} m và {L} m", f"{2*L} m và 0 m", f"{L} m và {2*L} m"], f"Điểm đầu và điểm cuối trùng nhau nên độ dịch chuyển bằng $0$; quãng đường là ${L}+{L}={2*L}$ m.")
    for (s1, t1, s2, t2) in ((60, 1, 90, 1.5), (80, 2, 40, 1), (30, 0.5, 120, 2), (100, 2, 50, 1)):
        avg = (s1 + s2) / (t1 + t2); wrong = (s1 / t1 + s2 / t2) / 2
        if abs(avg - wrong) < 1e-9: continue
        nm(b, 'b3', 'vd', 'Tốc độ trung bình', f"Một xe đi {s1} km trong {fnum(t1)} h rồi đi tiếp {s2} km trong {fnum(t2)} h theo cùng một hướng. Tốc độ trung bình trên cả quãng đường là:", avg, [wrong, s1 / t1, s2 / t2], 'km/h', f"$v_{{tb}}=\\dfrac{{s_1+s_2}}{{t_1+t_2}}=\\dfrac{{{s1}+{s2}}}{{{fnum(t1)}+{fnum(t2)}}}={fnum(avg)}$ km/h (không phải trung bình cộng hai tốc độ).")
    for (d, t) in ((100, 20), (300, 60), (90, 15), (120, 8), (36, 6)):
        nm(b, 'b3', 'nb', 'Vận tốc', f"Một vật chuyển động thẳng đều, trong {t} s có độ dịch chuyển {d} m. Vận tốc của vật là:", d / t, [d * t, t / d, d + t], 'm/s', f"$v=\\dfrac{{d}}{{t}}=\\dfrac{{{d}}}{{{t}}}={fnum(d/t)}$ m/s.")
        sa(b, 'b3', 'nb', 'Vận tốc', f"Một vật chuyển động thẳng đều, trong {t} s có độ dịch chuyển {d} m. Tính vận tốc của vật (m/s).", d / t, f"$v=\\dfrac{{d}}{{t}}={fnum(d/t)}$ m/s.", 'm/s')
    for (v, t) in ((5, 20), (12, 15), (20, 30), (15, 40)):
        nm(b, 'b3', 'nb', 'Quãng đường chuyển động thẳng đều', f"Một xe chuyển động thẳng đều với vận tốc {v} m/s. Quãng đường xe đi được sau {t} s là:", v * t, [v / t, v + t, v * t / 2], 'm', f"$s=vt={v}\\times{t}={v*t}$ m.")
    for (x1, x2, t) in ((10, 40, 5), (0, 90, 15), (20, 80, 10), (100, 40, 20)):
        v = (x2 - x1) / t
        nm(b, 'b3', 'th', 'Đồ thị toạ độ - thời gian', f"Đồ thị toạ độ - thời gian của một vật là đoạn thẳng đi qua điểm $(0;{x1})$ và điểm $({t};{x2})$ (toạ độ tính bằng m, thời gian tính bằng s). Vận tốc của vật là:", v, [x2 / t, abs(v) * 2, x1 / t if x1 else v + 1], 'm/s', f"Độ dốc của đồ thị $x$-$t$ chính là vận tốc: $v=\\dfrac{{x_2-x_1}}{{t}}=\\dfrac{{{x2}-{x1}}}{{{t}}}={fnum(v)}$ m/s.")
    for (d, v1, v2) in ((100, 6, 4), (180, 10, 8), (240, 12, 8), (90, 5, 4)):
        t = d / (v1 + v2)
        nm(b, 'b3', 'vd', 'Hai vật gặp nhau (ngược chiều)', f"Hai xe xuất phát cùng lúc từ hai điểm cách nhau {d} m và chạy ngược chiều lại gần nhau với vận tốc {v1} m/s và {v2} m/s. Thời gian đến lúc hai xe gặp nhau là:", t, [d / abs(v1 - v2), d / v1, d / v2], 's', f"Tốc độ lại gần nhau là $v_1+v_2={v1+v2}$ m/s nên $t=\\dfrac{{d}}{{v_1+v_2}}=\\dfrac{{{d}}}{{{v1+v2}}}={fnum(t)}$ s.")
        t2 = d / (v1 - v2)
        nm(b, 'b3', 'vd', 'Hai vật đuổi nhau', f"Xe A ở phía sau xe B {d} m, cả hai chạy cùng chiều với vận tốc {v1} m/s (xe A) và {v2} m/s (xe B), xuất phát cùng lúc. Thời gian xe A đuổi kịp xe B là:", t2, [d / (v1 + v2), d / v1, d / v2], 's', f"Tốc độ đuổi kịp là $v_1-v_2={v1-v2}$ m/s nên $t=\\dfrac{{d}}{{v_1-v_2}}=\\dfrac{{{d}}}{{{v1-v2}}}={fnum(t2)}$ s.")
    # ---- b4: chuyển động thẳng biến đổi đều ----
    for (v0, a, t) in ((2, 3, 4), (5, 2, 6), (10, 1.5, 8), (0, 4, 5), (3, 0.5, 10)):
        v = v0 + a * t
        nm(b, 'b4', 'nb', 'Vận tốc tức thời', f"Một vật bắt đầu có vận tốc {fnum(v0)} m/s và chuyển động thẳng nhanh dần đều với gia tốc {fnum(a)} m/s². Vận tốc sau {t} s là:", v, [v0 + a, a * t, v0 * a * t if v0 else v + a], 'm/s', f"$v=v_0+at={fnum(v0)}+{fnum(a)}\\times{t}={fnum(v)}$ m/s.")
        s = v0 * t + a * t * t / 2
        nm(b, 'b4', 'th', 'Quãng đường nhanh dần đều', f"Một vật bắt đầu có vận tốc {fnum(v0)} m/s và chuyển động thẳng nhanh dần đều với gia tốc {fnum(a)} m/s². Quãng đường đi được sau {t} s là:", s, [v0 * t + a * t * t, v * t, a * t * t / 2 + v0], 'm', f"$s=v_0t+\\dfrac{{1}}{{2}}at^2={fnum(v0)}\\times{t}+\\dfrac{{1}}{{2}}\\times{fnum(a)}\\times{t}^2={fnum(s)}$ m.")
        sa(b, 'b4', 'th', 'Quãng đường nhanh dần đều', f"Vật có vận tốc đầu {fnum(v0)} m/s, chuyển động thẳng nhanh dần đều với gia tốc {fnum(a)} m/s². Tính quãng đường đi được sau {t} s (m).", s, f"$s=v_0t+\\dfrac{{1}}{{2}}at^2={fnum(s)}$ m.", 'm')
    for (v0, v, t) in ((0, 20, 5), (4, 16, 6), (10, 40, 10), (6, 30, 8)):
        a = (v - v0) / t
        nm(b, 'b4', 'nb', 'Gia tốc', f"Vận tốc của một vật tăng đều từ {v0} m/s lên {v} m/s trong {t} s. Gia tốc của vật là:", a, [(v + v0) / t, v / t if v0 else a * 2, (v - v0) * t], 'm/s²', f"$a=\\dfrac{{v-v_0}}{{t}}=\\dfrac{{{v}-{v0}}}{{{t}}}={fnum(a)}$ m/s².")
        sa(b, 'b4', 'nb', 'Gia tốc', f"Vận tốc của một vật tăng đều từ {v0} m/s lên {v} m/s trong {t} s. Tính gia tốc của vật (m/s²).", a, f"$a=\\dfrac{{v-v_0}}{{t}}={fnum(a)}$ m/s².", 'm/s²')
    for (v0, a) in ((20, 2), (30, 5), (10, 1), (24, 3), (15, 2.5)):
        t = v0 / a; s = v0 * v0 / (2 * a)
        nm(b, 'b4', 'th', 'Thời gian dừng', f"Ô tô đang chạy với vận tốc {v0} m/s thì hãm phanh, chuyển động thẳng chậm dần đều với độ lớn gia tốc {fnum(a)} m/s² đến khi dừng. Thời gian từ lúc hãm phanh đến khi dừng là:", t, [v0 * a, v0 * v0 / a, v0 / (2 * a)], 's', f"Lúc dừng $v=0$: $0=v_0-at\\Rightarrow t=\\dfrac{{v_0}}{{a}}=\\dfrac{{{v0}}}{{{fnum(a)}}}={fnum(t)}$ s.")
        nm(b, 'b4', 'vd', 'Quãng đường phanh', f"Ô tô đang chạy với vận tốc {v0} m/s thì hãm phanh, chuyển động thẳng chậm dần đều với độ lớn gia tốc {fnum(a)} m/s² đến khi dừng. Quãng đường ô tô đi được kể từ lúc hãm phanh là:", s, [v0 * v0 / a, v0 * t, v0 * v0 * a / 2], 'm', f"Từ $v^2-v_0^2=2as$ với $v=0$ và $a=-{fnum(a)}$: $s=\\dfrac{{v_0^2}}{{2a}}=\\dfrac{{{v0}^2}}{{2\\times{fnum(a)}}}={fnum(s)}$ m.")
        sa(b, 'b4', 'vd', 'Quãng đường phanh', f"Ô tô chạy {v0} m/s thì hãm phanh với gia tốc có độ lớn {fnum(a)} m/s² cho đến khi dừng. Tính quãng đường phanh (m).", s, f"$s=\\dfrac{{v_0^2}}{{2a}}=\\dfrac{{{v0}^2}}{{2\\times{fnum(a)}}}={fnum(s)}$ m.", 'm')
    for (v0, a, s) in ((2, 3, 20), (0, 2, 25), (4, 6, 8), (5, 4, 30)):
        v = math.sqrt(v0 * v0 + 2 * a * s)
        if abs(v - round(v, 2)) > 1e-9: continue
        nm(b, 'b4', 'vd', 'Công thức độc lập thời gian', f"Một vật có vận tốc đầu {v0} m/s, chuyển động thẳng nhanh dần đều với gia tốc {a} m/s². Vận tốc của vật sau khi đi được {s} m là:", v, [v0 + a * s, math.sqrt(2 * a * s) + v0, v * v], 'm/s', f"$v^2=v_0^2+2as={v0}^2+2\\times{a}\\times{s}={fnum(v*v)}$ nên $v={fnum(v)}$ m/s.")
    for (v0, a, n) in ((2, 4, 3), (5, 2, 4), (0, 6, 5), (10, 2, 3)):
        sn = v0 + a * (n - 0.5)
        nm(b, 'b4', 'vd', 'Quãng đường trong giây thứ n', f"Vật chuyển động thẳng nhanh dần đều với vận tốc đầu {v0} m/s và gia tốc {a} m/s². Quãng đường vật đi được trong giây thứ {n} là:", sn, [v0 * n + a * n * n / 2, a * n * n / 2, v0 + a * n], 'm', f"Quãng đường trong giây thứ {n} bằng quãng đường trong {n} s trừ quãng đường trong {n-1} s: $s={fnum(v0*n+a*n*n/2)}-{fnum(v0*(n-1)+a*(n-1)**2/2)}={fnum(sn)}$ m.")
    for (v1, t1, v2, t2) in ((10, 4, 10, 6), (6, 5, 6, 10), (8, 2, 8, 3)):
        pass
    for (vmax, t1, t2) in ((10, 4, 6), (12, 5, 5), (20, 10, 20), (8, 2, 6)):
        s = vmax * t1 / 2 + vmax * t2
        nm(b, 'b4', 'vd', 'Đồ thị vận tốc - thời gian', f"Một vật bắt đầu chuyển động nhanh dần đều từ nghỉ đến vận tốc {vmax} m/s trong {t1} s, sau đó chuyển động thẳng đều trong {t2} s. Quãng đường vật đi được trong cả quá trình là:", s, [vmax * (t1 + t2), vmax * t1 / 2, vmax * t2], 'm', f"Giai đoạn nhanh dần đều: $s_1=\\dfrac{{{vmax}\\times{t1}}}{{2}}={fnum(vmax*t1/2)}$ m; giai đoạn đều: $s_2={vmax}\\times{t2}={vmax*t2}$ m; tổng $s={fnum(s)}$ m (bằng diện tích dưới đồ thị).")
    b.mc('b4', 'nb', 'Dấu của gia tốc', "Một vật chuyển động thẳng chậm dần đều. Nhận xét nào sau đây đúng?", "Gia tốc ngược chiều với vận tốc", ["Gia tốc cùng chiều với vận tốc", "Gia tốc luôn bằng không", "Vận tốc không đổi theo thời gian"], "Chuyển động chậm dần đều có độ lớn vận tốc giảm, nên vectơ gia tốc ngược chiều với vectơ vận tốc.")
    b.mc('b4', 'nb', 'Dấu của gia tốc', "Một vật chuyển động thẳng nhanh dần đều. Nhận xét nào sau đây đúng?", "Gia tốc cùng chiều với vận tốc", ["Gia tốc ngược chiều với vận tốc", "Gia tốc bằng không", "Độ lớn vận tốc giảm đều"], "Chuyển động nhanh dần đều có độ lớn vận tốc tăng, nên gia tốc cùng chiều với vận tốc.")
    b.mc('b3', 'nb', 'Đồ thị', "Trên đồ thị độ dịch chuyển - thời gian, vật chuyển động thẳng đều được biểu diễn bằng:", "Đường thẳng xiên góc", ["Đường thẳng nằm ngang", "Đường parabol", "Đường tròn"], "Chuyển động thẳng đều có $x=x_0+vt$ là hàm bậc nhất của $t$ nên đồ thị là đường thẳng xiên góc (độ dốc là vận tốc).")
    return b

def c3():
    b = Bank('ly10', 'c3')
    g = 10
    for t in (1, 2, 3, 4, 5):
        nm(b, 'b5', 'nb', 'Rơi tự do - quãng đường', f"Một vật rơi tự do không vận tốc đầu, lấy $g=10$ m/s². Quãng đường vật rơi được sau {t} s là:", g * t * t / 2, [g * t, g * t * t, g * t * t / 4], 'm', f"$h=\\dfrac{{1}}{{2}}gt^2=\\dfrac{{1}}{{2}}\\times10\\times{t}^2={fnum(g*t*t/2)}$ m.")
        nm(b, 'b5', 'nb', 'Rơi tự do - vận tốc', f"Một vật rơi tự do không vận tốc đầu, lấy $g=10$ m/s². Vận tốc của vật sau {t} s là:", g * t, [g * t * t / 2, g * t * t, g / t], 'm/s', f"$v=gt=10\\times{t}={g*t}$ m/s.")
        sa(b, 'b5', 'nb', 'Rơi tự do - vận tốc', f"Vật rơi tự do không vận tốc đầu, $g=10$ m/s². Tính vận tốc sau {t} s (m/s).", g * t, f"$v=gt=10\\times{t}={g*t}$ m/s.", 'm/s')
    for h in (5, 20, 45, 80, 125):
        t = math.sqrt(2 * h / g); v = g * t
        nm(b, 'b5', 'th', 'Rơi tự do - thời gian', f"Thả rơi tự do một vật từ độ cao {h} m, lấy $g=10$ m/s². Thời gian rơi là:", t, [h / g, 2 * h / g, math.sqrt(h / g)], 's', f"$h=\\dfrac{{1}}{{2}}gt^2\\Rightarrow t=\\sqrt{{\\dfrac{{2h}}{{g}}}}=\\sqrt{{\\dfrac{{2\\times{h}}}{{10}}}}={fnum(t)}$ s.")
        nm(b, 'b5', 'th', 'Rơi tự do - vận tốc chạm đất', f"Thả rơi tự do một vật từ độ cao {h} m, lấy $g=10$ m/s². Vận tốc của vật khi chạm đất là:", v, [g * h, h / 2, v / 2], 'm/s', f"$v=\\sqrt{{2gh}}=\\sqrt{{2\\times10\\times{h}}}={fnum(v)}$ m/s.")
        sa(b, 'b5', 'th', 'Rơi tự do - thời gian', f"Thả rơi tự do một vật từ độ cao {h} m, $g=10$ m/s². Tính thời gian rơi (s).", t, f"$t=\\sqrt{{\\dfrac{{2h}}{{g}}}}={fnum(t)}$ s.", 's')
    for t in (3, 4, 5, 6):
        d = g * (2 * t - 1) / 2
        nm(b, 'b5', 'vd', 'Quãng đường giây cuối', f"Một vật rơi tự do (lấy $g=10$ m/s²) chạm đất sau {t} s. Quãng đường vật rơi được trong giây cuối cùng là:", d, [g * t * t / 2, g * t, g * (t - 1)], 'm', f"Quãng đường giây cuối $=\\dfrac{{1}}{{2}}g\\,t^2-\\dfrac{{1}}{{2}}g\\,(t-1)^2={fnum(g*t*t/2)}-{fnum(g*(t-1)**2/2)}={fnum(d)}$ m.")
    for (v0, tt, h, v) in ((15, 2, 20, 25), (6, 0.8, 3.2, 10), (30, 4, 80, 50), (12, 1.6, 12.8, 20), (9, 1.2, 7.2, 15), (8, 0.6, 1.8, 10)):
        L = v0 * tt
        nm(b, 'b5', 'th', 'Ném ngang - thời gian', f"Ném ngang một vật từ độ cao {fnum(h)} m với vận tốc đầu {v0} m/s, lấy $g=10$ m/s². Thời gian vật bay trong không khí là:", tt, [h / g, math.sqrt(h / g), 2 * h / g], 's', f"$t=\\sqrt{{\\dfrac{{2h}}{{g}}}}=\\sqrt{{\\dfrac{{2\\times{fnum(h)}}}{{10}}}}={fnum(tt)}$ s.")
        nm(b, 'b5', 'th', 'Ném ngang - tầm xa', f"Ném ngang một vật từ độ cao {fnum(h)} m với vận tốc đầu {v0} m/s, lấy $g=10$ m/s². Tầm bay xa của vật là:", L, [v0 * h / g, v0 * math.sqrt(h / g), v0 * tt * 2], 'm', f"Thời gian bay $t=\\sqrt{{2h/g}}={fnum(tt)}$ s; tầm xa $L=v_0t={v0}\\times{fnum(tt)}={fnum(L)}$ m.")
        nm(b, 'b5', 'vd', 'Ném ngang - vận tốc chạm đất', f"Ném ngang một vật từ độ cao {fnum(h)} m với vận tốc đầu {v0} m/s, lấy $g=10$ m/s². Độ lớn vận tốc của vật khi chạm đất là:", v, [v0 + g * tt, g * tt, v0], 'm/s', f"Thành phần ngang $v_x={v0}$ m/s; thành phần đứng $v_y=gt={fnum(g*tt)}$ m/s; $v=\\sqrt{{v_x^2+v_y^2}}={fnum(v)}$ m/s.")
        sa(b, 'b5', 'th', 'Ném ngang - tầm xa', f"Ném ngang một vật từ độ cao {fnum(h)} m với vận tốc đầu {v0} m/s, $g=10$ m/s². Tính tầm bay xa (m).", L, f"$t=\\sqrt{{2h/g}}={fnum(tt)}$ s, $L=v_0t={fnum(L)}$ m.", 'm')
    for v0 in (10, 20, 30, 40):
        nm(b, 'b5', 'th', 'Ném thẳng đứng lên - độ cao cực đại', f"Ném một vật thẳng đứng lên cao với vận tốc {v0} m/s, lấy $g=10$ m/s². Độ cao cực đại so với điểm ném là:", v0 * v0 / 20, [v0 * v0 / 10, v0 / g, v0 * v0], 'm', f"Tại điểm cao nhất $v=0$: $H=\\dfrac{{v_0^2}}{{2g}}=\\dfrac{{{v0}^2}}{{20}}={fnum(v0*v0/20)}$ m.")
        nm(b, 'b5', 'th', 'Ném thẳng đứng lên - thời gian lên', f"Ném một vật thẳng đứng lên cao với vận tốc {v0} m/s, lấy $g=10$ m/s². Thời gian vật đi lên đến điểm cao nhất là:", v0 / g, [v0 * g, 2 * v0 / g, v0 / (2 * g)], 's', f"$v=v_0-gt=0\\Rightarrow t=\\dfrac{{v_0}}{{g}}=\\dfrac{{{v0}}}{{10}}={fnum(v0/g)}$ s.")
    for v0 in (10, 20, 40):
        nm(b, 'b5', 'vd', 'Ném xiên - độ cao cực đại', f"Ném một vật từ mặt đất với vận tốc đầu {v0} m/s theo phương hợp với phương ngang góc $30^\\circ$, lấy $g=10$ m/s². Độ cao cực đại của vật là:", v0 * v0 / 80, [v0 * v0 / 20, v0 * v0 / 40, v0 * v0 / 160], 'm', f"Thành phần thẳng đứng $v_{{0y}}=v_0\\sin30^\\circ={fnum(v0/2)}$ m/s; $H=\\dfrac{{v_{{0y}}^2}}{{2g}}=\\dfrac{{{fnum(v0/2)}^2}}{{20}}={fnum(v0*v0/80, 3)}$ m.", nd=3)
    for v0 in (10, 20, 30):
        nm(b, 'b5', 'vd', 'Ném xiên 45° - tầm xa', f"Ném một vật từ mặt đất với vận tốc đầu {v0} m/s theo phương hợp với phương ngang góc $45^\\circ$, lấy $g=10$ m/s². Tầm bay xa của vật là:", v0 * v0 / g, [v0 * v0 / 20, v0 * v0 / 2, v0 * g], 'm', f"$L=\\dfrac{{v_0^2\\sin2\\alpha}}{{g}}=\\dfrac{{{v0}^2\\times1}}{{10}}={fnum(v0*v0/g)}$ m (với $\\alpha=45^\\circ$ thì $\\sin2\\alpha=1$).")
    # ---- b6: tổng hợp lực ----
    for (a, c, d) in ((3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20)):
        nm(b, 'b6', 'th', 'Tổng hợp hai lực vuông góc', f"Hai lực đồng quy có độ lớn {a} N và {c} N, vuông góc với nhau. Độ lớn hợp lực là:", d, [a + c, abs(c - a), a * c], 'N', f"$F=\\sqrt{{F_1^2+F_2^2}}=\\sqrt{{{a}^2+{c}^2}}={d}$ N.")
        sa(b, 'b6', 'th', 'Tổng hợp hai lực vuông góc', f"Hai lực đồng quy vuông góc có độ lớn {a} N và {c} N. Tính độ lớn hợp lực (N).", d, f"$F=\\sqrt{{{a}^2+{c}^2}}={d}$ N.", 'N')
    for (a, c) in ((6, 9), (10, 14), (4, 11), (7, 12)):
        nm(b, 'b6', 'nb', 'Hai lực cùng phương', f"Hai lực cùng phương, cùng chiều có độ lớn {a} N và {c} N tác dụng lên cùng một vật. Độ lớn hợp lực là:", a + c, [abs(c - a), a * c, (a + c) / 2], 'N', f"Hai lực cùng phương, cùng chiều nên $F=F_1+F_2={a}+{c}={a+c}$ N.")
        nm(b, 'b6', 'nb', 'Hai lực ngược chiều', f"Hai lực cùng phương, ngược chiều có độ lớn {a} N và {c} N tác dụng lên cùng một vật. Độ lớn hợp lực là:", abs(c - a), [a + c, a * c, (a + c) / 2], 'N', f"Hai lực ngược chiều nên $F=|F_1-F_2|=|{a}-{c}|={abs(c-a)}$ N.")
        lo, hi = abs(c - a), a + c
        mid = (lo + hi) // 2
        b.mc('b6', 'vd', 'Giới hạn của hợp lực', f"Hai lực đồng quy có độ lớn {a} N và {c} N. Hợp lực của chúng KHÔNG THỂ có độ lớn bằng:", f"{hi + 3} N", [f"{mid} N", f"{lo + 1} N", f"{hi - 1} N"], f"Độ lớn hợp lực thoả $|F_1-F_2|\\le F\\le F_1+F_2$, tức ${lo}\\le F\\le {hi}$ (N). Giá trị {hi+3} N vượt quá {hi} N nên không thể xảy ra.")
    for F1 in (10, 20, 30, 50):
        nm(b, 'b6', 'vd', 'Hai lực bằng nhau hợp góc 120°', f"Hai lực đồng quy có cùng độ lớn {F1} N, hợp với nhau góc $120^\\circ$. Độ lớn hợp lực là:", F1, [2 * F1, F1 * math.sqrt(2), F1 / 2], 'N', f"Với hai lực bằng nhau hợp góc $120^\\circ$: $F=2F_1\\cos\\dfrac{{120^\\circ}}{{2}}=2\\times{F1}\\times\\cos60^\\circ={F1}$ N.")
    for F in (20, 40, 100, 60):
        nm(b, 'b6', 'th', 'Phân tích lực', f"Một lực $F={F}$ N có phương hợp với phương ngang góc $60^\\circ$. Thành phần của lực theo phương ngang là:", F / 2, [F * math.sqrt(3) / 2, F, F * 2], 'N', f"$F_x=F\\cos60^\\circ={F}\\times0{{,}}5={fnum(F/2)}$ N.") if False else \
        nm(b, 'b6', 'th', 'Phân tích lực', f"Một lực $F={F}$ N có phương hợp với phương ngang góc $60^\\circ$. Thành phần của lực theo phương ngang là:", F / 2, [F, F * 2, F / 4], 'N', f"$F_x=F\\cos60^\\circ={F}\\times0{{,}}5={fnum(F/2)}$ N.")
    for P in (20, 40, 100, 60):
        nm(b, 'b6', 'vd', 'Phân tích trọng lực trên mặt phẳng nghiêng', f"Vật trọng lượng {P} N đặt trên mặt phẳng nghiêng góc $30^\\circ$ so với phương ngang. Thành phần của trọng lực theo phương song song với mặt phẳng nghiêng là:", P / 2, [P, P * 2, P / 4], 'N', f"Thành phần dọc theo mặt phẳng nghiêng $P_x=P\\sin30^\\circ={P}\\times0{{,}}5={fnum(P/2)}$ N.")
    b.mc('b6', 'nb', 'Quy tắc hình bình hành', "Hợp của hai lực đồng quy được xác định bằng quy tắc nào?", "Quy tắc hình bình hành", ["Quy tắc nhân đôi lực", "Quy tắc cộng độ lớn hai lực", "Quy tắc đòn bẩy"], "Hợp lực của hai lực đồng quy là đường chéo (xuất phát từ điểm đồng quy) của hình bình hành dựng trên hai lực đó.")
    b.mc('b6', 'nb', 'Điều kiện cân bằng', "Điều kiện cân bằng của một chất điểm chịu tác dụng của nhiều lực là:", "Hợp lực của các lực tác dụng lên chất điểm bằng không", ["Tổng độ lớn các lực bằng không", "Các lực luôn có độ lớn bằng nhau", "Các lực luôn cùng phương cùng chiều"], "Chất điểm cân bằng khi vectơ hợp lực tác dụng lên nó bằng $\\vec 0$.")
    return b

def c4():
    b = Bank('ly10', 'c4')
    for (m, a) in ((2, 3), (5, 2), (10, 0.5), (4, 2.5), (0.5, 8)):
        Fo = m * a
        nm(b, 'b7', 'nb', 'Định luật II Newton - lực', f"Vật khối lượng {fnum(m)} kg chuyển động với gia tốc {fnum(a)} m/s². Hợp lực tác dụng lên vật là:", Fo, [m / a, a / m, Fo * 2], 'N', f"$F=ma={fnum(m)}\\times{fnum(a)}={fnum(Fo)}$ N.")
        nm(b, 'b7', 'nb', 'Định luật II Newton - gia tốc', f"Hợp lực {fnum(Fo)} N tác dụng lên vật khối lượng {fnum(m)} kg. Gia tốc của vật là:", a, [Fo * m, m / Fo, Fo], 'm/s²', f"$a=\\dfrac{{F}}{{m}}=\\dfrac{{{fnum(Fo)}}}{{{fnum(m)}}}={fnum(a)}$ m/s².")
        sa(b, 'b7', 'nb', 'Định luật II Newton - gia tốc', f"Hợp lực {fnum(Fo)} N tác dụng lên vật khối lượng {fnum(m)} kg. Tính gia tốc của vật (m/s²).", a, f"$a=\\dfrac{{F}}{{m}}={fnum(a)}$ m/s².", 'm/s²')
        nm(b, 'b7', 'nb', 'Định luật II Newton - khối lượng', f"Dưới tác dụng của hợp lực {fnum(Fo)} N, một vật thu gia tốc {fnum(a)} m/s². Khối lượng của vật là:", m, [Fo * a, a / Fo, Fo], 'kg', f"$m=\\dfrac{{F}}{{a}}=\\dfrac{{{fnum(Fo)}}}{{{fnum(a)}}}={fnum(m)}$ kg.")
    for (m, F, fc) in ((2, 10, 4), (5, 30, 10), (10, 50, 20), (4, 22, 6)):
        a = (F - fc) / m
        nm(b, 'b7', 'th', 'Hợp lực có lực cản', f"Vật khối lượng {m} kg chịu lực kéo {F} N và lực cản {fc} N (cùng phương, ngược chiều). Gia tốc của vật là:", a, [F / m, (F + fc) / m, (F - fc) * m], 'm/s²', f"Hợp lực $F_{{hl}}={F}-{fc}={F-fc}$ N; $a=\\dfrac{{F_{{hl}}}}{{m}}=\\dfrac{{{F-fc}}}{{{m}}}={fnum(a)}$ m/s².")
    for (m, F, t) in ((2, 6, 4), (5, 10, 3), (4, 8, 5), (10, 20, 6)):
        a = F / m; v = a * t; s = a * t * t / 2
        nm(b, 'b7', 'vd', 'Vận tốc sau thời gian t', f"Vật khối lượng {m} kg đang đứng yên, chịu tác dụng của lực không đổi {F} N (bỏ qua ma sát). Vận tốc của vật sau {t} s là:", v, [F * t, F * t * m, a * t * t / 2], 'm/s', f"$a=\\dfrac{{F}}{{m}}={fnum(a)}$ m/s²; $v=at={fnum(a)}\\times{t}={fnum(v)}$ m/s.")
        nm(b, 'b7', 'vd', 'Quãng đường sau thời gian t', f"Vật khối lượng {m} kg đang đứng yên, chịu tác dụng của lực không đổi {F} N (bỏ qua ma sát). Quãng đường vật đi được sau {t} s là:", s, [v * t, a * t, F * t * t / 2], 'm', f"$a=\\dfrac{{F}}{{m}}={fnum(a)}$ m/s²; $s=\\dfrac{{1}}{{2}}at^2={fnum(s)}$ m.")
        sa(b, 'b7', 'vd', 'Quãng đường sau thời gian t', f"Vật {m} kg đứng yên chịu lực không đổi {F} N, bỏ qua ma sát. Tính quãng đường đi được sau {t} s (m).", s, f"$a=F/m={fnum(a)}$ m/s²; $s=\\dfrac{{1}}{{2}}at^2={fnum(s)}$ m.", 'm')
    for (m, v0, v, t) in ((1000, 20, 0, 5), (800, 15, 0, 3), (60, 6, 0, 2), (2, 10, 0, 4)):
        Fo = m * (v0 - v) / t
        nm(b, 'b7', 'vd', 'Lực hãm', f"Vật khối lượng {m} kg đang chuyển động với vận tốc {v0} m/s thì chịu lực hãm không đổi và dừng lại sau {t} s. Độ lớn lực hãm là:", Fo, [m * v0, m * v0 * t, Fo / 2], 'N', f"Gia tốc có độ lớn $a=\\dfrac{{v_0-v}}{{t}}=\\dfrac{{{v0}}}{{{t}}}={fnum(v0/t)}$ m/s²; $F=ma={m}\\times{fnum(v0/t)}={fnum(Fo)}$ N.")
    for m in (2, 5, 10, 60):
        nm(b, 'b8', 'nb', 'Trọng lực', f"Vật khối lượng {m} kg, lấy $g=10$ m/s². Trọng lượng của vật là:", m * 10, [m / 10, m * 9.8 + 1, m * 100], 'N', f"$P=mg={m}\\times10={m*10}$ N.")
        sa(b, 'b8', 'nb', 'Trọng lực', f"Vật có khối lượng {m} kg, lấy $g=10$ m/s². Tính trọng lượng của vật (N).", m * 10, f"$P=mg={m}\\times10={m*10}$ N.", 'N')
    for (k, dl) in ((100, 2), (200, 5), (50, 10), (400, 3)):
        Fd = k * dl / 100
        nm(b, 'b8', 'th', 'Lực đàn hồi', f"Lò xo có độ cứng $k={k}$ N/m bị dãn {dl} cm. Độ lớn lực đàn hồi của lò xo là:", Fd, [k * dl, k / dl, k * dl / 10], 'N', f"Đổi $\\Delta\\ell={dl}$ cm $=0{{,}}0{dl if dl>=10 else str(dl).zfill(1)}$ m" if False else f"Đổi $\\Delta\\ell={dl}$ cm $={fnum(dl/100)}$ m; $F=k\\Delta\\ell={k}\\times{fnum(dl/100)}={fnum(Fd)}$ N.")
        sa(b, 'b8', 'th', 'Lực đàn hồi', f"Lò xo độ cứng {k} N/m bị dãn {dl} cm. Tính độ lớn lực đàn hồi (N).", Fd, f"$F=k\\Delta\\ell={k}\\times{fnum(dl/100)}={fnum(Fd)}$ N.", 'N')
    for (Fd, dl) in ((10, 5), (6, 3), (12, 4), (20, 10)):
        k = Fd / (dl / 100)
        nm(b, 'b8', 'th', 'Độ cứng lò xo', f"Treo vật làm lò xo dãn {dl} cm thì lực đàn hồi là {Fd} N. Độ cứng của lò xo là:", k, [Fd * dl, Fd / dl, k / 100], 'N/m', f"$k=\\dfrac{{F}}{{\\Delta\\ell}}=\\dfrac{{{Fd}}}{{{fnum(dl/100)}}}={fnum(k)}$ N/m.")
    for (k1, k2) in ((100, 100), (200, 100), (300, 200)):
        nm(b, 'b8', 'vd', 'Ghép lò xo song song', f"Hai lò xo có độ cứng {k1} N/m và {k2} N/m được ghép song song. Độ cứng tương đương của hệ là:", k1 + k2, [k1 * k2 / (k1 + k2), abs(k1 - k2) + 1, (k1 + k2) / 2], 'N/m', f"Ghép song song thì $k=k_1+k_2={k1}+{k2}={k1+k2}$ N/m.")
        nm(b, 'b8', 'vd', 'Ghép lò xo nối tiếp', f"Hai lò xo có độ cứng {k1} N/m và {k2} N/m được ghép nối tiếp. Độ cứng tương đương của hệ là:", k1 * k2 / (k1 + k2), [k1 + k2, abs(k1 - k2) + 1, (k1 + k2) / 2], 'N/m', f"Ghép nối tiếp thì $\\dfrac{{1}}{{k}}=\\dfrac{{1}}{{k_1}}+\\dfrac{{1}}{{k_2}}\\Rightarrow k=\\dfrac{{k_1k_2}}{{k_1+k_2}}=\\dfrac{{{k1}\\times{k2}}}{{{k1+k2}}}={fnum(k1*k2/(k1+k2))}$ N/m.")
    for (m, mu) in ((10, 0.2), (20, 0.1), (5, 0.4), (50, 0.3)):
        N = m * 10; fms = mu * N
        nm(b, 'b8', 'th', 'Lực ma sát trượt', f"Vật khối lượng {m} kg trượt trên mặt phẳng ngang có hệ số ma sát trượt $\\mu={fnum(mu)}$, lấy $g=10$ m/s². Độ lớn lực ma sát trượt là:", fms, [mu * m, N / mu, fms * 2], 'N', f"Áp lực $N=mg={N}$ N; $F_{{ms}}=\\mu N={fnum(mu)}\\times{N}={fnum(fms)}$ N.")
    for (m, F, mu) in ((10, 40, 0.2), (5, 30, 0.4), (20, 100, 0.25), (4, 24, 0.5)):
        fms = mu * m * 10; a = (F - fms) / m
        nm(b, 'b8', 'vd', 'Kéo vật có ma sát', f"Kéo vật khối lượng {m} kg trên mặt phẳng ngang bằng lực nằm ngang {F} N. Hệ số ma sát trượt $\\mu={fnum(mu)}$, lấy $g=10$ m/s². Gia tốc của vật là:", a, [F / m, (F + fms) / m, (F - mu * m) / m], 'm/s²', f"$F_{{ms}}=\\mu mg={fnum(fms)}$ N; $a=\\dfrac{{F-F_{{ms}}}}{{m}}=\\dfrac{{{F}-{fnum(fms)}}}{{{m}}}={fnum(a)}$ m/s².")
        sa(b, 'b8', 'vd', 'Kéo vật có ma sát', f"Kéo vật {m} kg trên mặt phẳng ngang bằng lực ngang {F} N, hệ số ma sát trượt {fnum(mu)}, $g=10$ m/s². Tính gia tốc (m/s²).", a, f"$F_{{ms}}=\\mu mg={fnum(fms)}$ N; $a=(F-F_{{ms}})/m={fnum(a)}$ m/s².", 'm/s²')
    for mu in (0.25, 0.5, 0.1):
        a = 10 * (0.6 - mu * 0.8)
        nm(b, 'b8', 'vd', 'Mặt phẳng nghiêng có ma sát', f"Vật trượt xuống mặt phẳng nghiêng góc $\\alpha$ ($\\sin\\alpha=0{{,}}6$; $\\cos\\alpha=0{{,}}8$) có hệ số ma sát $\\mu={fnum(mu)}$, lấy $g=10$ m/s². Gia tốc của vật là:", a, [10 * 0.6, 10 * (0.6 + mu * 0.8), 10 * (0.8 - mu * 0.6)], 'm/s²', f"$a=g(\\sin\\alpha-\\mu\\cos\\alpha)=10\\times(0{{,}}6-{fnum(mu)}\\times0{{,}}8)={fnum(a)}$ m/s².")
    for (m, a) in ((60, 2), (50, 1), (70, 3)):
        nm(b, 'b8', 'vd', 'Lực nén trong thang máy (đi lên nhanh dần)', f"Người khối lượng {m} kg đứng trong thang máy đang đi lên nhanh dần đều với gia tốc {a} m/s². Lấy $g=10$ m/s². Lực nén của người lên sàn thang máy là:", m * (10 + a), [m * (10 - a), m * 10, m * a], 'N', f"Theo định luật II Newton: $N-mg=ma\\Rightarrow N=m(g+a)={m}\\times({10}+{a})={m*(10+a)}$ N.")
        nm(b, 'b8', 'vd', 'Lực nén trong thang máy (đi xuống nhanh dần)', f"Người khối lượng {m} kg đứng trong thang máy đang đi xuống nhanh dần đều với gia tốc {a} m/s². Lấy $g=10$ m/s². Lực nén của người lên sàn thang máy là:", m * (10 - a), [m * (10 + a), m * 10, m * a], 'N', f"Chiều dương hướng xuống: $mg-N=ma\\Rightarrow N=m(g-a)={m}\\times({10}-{a})={m*(10-a)}$ N.")
    for Fv in (20, 45, 80):
        nm(b, 'b7', 'nb', 'Định luật III Newton', f"Một người đẩy tường bằng lực {Fv} N. Theo định luật III Newton, tường đẩy người với lực có độ lớn:", Fv, [0, Fv / 2, Fv * 2], 'N', "Lực và phản lực luôn trực đối: cùng độ lớn, cùng phương, ngược chiều và đặt vào hai vật khác nhau, nên tường đẩy người một lực bằng ".replace("bằng ", f"bằng {Fv} N.")) if False else \
        b.mc('b7', 'nb', 'Định luật III Newton', f"Một người đẩy tường bằng lực {Fv} N. Theo định luật III Newton, tường đẩy người với lực có độ lớn là:", f"{Fv} N", [f"0 N", f"{Fv//2 if Fv%2==0 else Fv+1} N", f"{Fv*2} N"], f"Lực và phản lực luôn cùng độ lớn, ngược chiều, đặt vào hai vật khác nhau; vậy tường đẩy người một lực {Fv} N.")
    b.mc('b7', 'nb', 'Định luật I Newton', "Theo định luật I Newton, một vật không chịu tác dụng của lực nào (hoặc các lực cân bằng) sẽ:", "Đứng yên hoặc chuyển động thẳng đều", ["Chuyển động nhanh dần đều", "Chuyển động tròn đều", "Dừng lại sau một thời gian"], "Định luật I Newton (quán tính): khi hợp lực bằng không, vật đang đứng yên thì tiếp tục đứng yên, đang chuyển động thì tiếp tục chuyển động thẳng đều.")
    b.mc('b7', 'nb', 'Quán tính', "Mức quán tính của một vật được đo bằng đại lượng nào?", "Khối lượng", ["Vận tốc", "Thể tích", "Trọng lượng"], "Khối lượng là số đo mức quán tính của vật: khối lượng càng lớn thì càng khó thay đổi vận tốc.")
    b.mc('b8', 'nb', 'Ma sát', "Lực ma sát trượt KHÔNG phụ thuộc vào yếu tố nào sau đây?", "Diện tích tiếp xúc", ["Áp lực của vật lên bề mặt", "Vật liệu và tình trạng bề mặt tiếp xúc", "Hệ số ma sát trượt"], "$F_{ms}=\\mu N$ chỉ phụ thuộc áp lực $N$ và hệ số ma sát $\\mu$ (phụ thuộc vật liệu, tình trạng bề mặt), không phụ thuộc diện tích tiếp xúc.")
    return b

def c5():
    b = Bank('ly10', 'c5')
    for (Fo, s, al, cs) in ((20, 10, 0, 1), (20, 10, 60, 0.5), (40, 5, 60, 0.5), (50, 4, 0, 1), (30, 6, 60, 0.5), (10, 8, 180, -1), (20, 10, 90, 0)):
        A = Fo * s * cs
        nm(b, 'b9', 'th', 'Công của một lực', f"Lực {Fo} N tác dụng lên vật làm vật dịch chuyển {s} m; góc giữa lực và hướng dịch chuyển là ${al}^\\circ$. Công của lực là:", A, [Fo * s, Fo * s * 0.5 if cs != 0.5 else Fo * s * 2, Fo / s], 'J', f"$A=Fs\\cos\\alpha={Fo}\\times{s}\\times\\cos{al}^\\circ={fnum(A)}$ J.") if A != 0 else \
        b.mc('b9', 'th', 'Công của một lực', f"Lực {Fo} N tác dụng lên vật làm vật dịch chuyển {s} m; góc giữa lực và hướng dịch chuyển là ${al}^\\circ$. Công của lực là:", "0 J", [f"{Fo*s} J", f"{Fo*s//2} J", f"{Fo//2} J"], f"$A=Fs\\cos90^\\circ=0$ J: lực vuông góc với hướng dịch chuyển nên không sinh công.")
    for (A, t) in ((600, 20), (1200, 30), (500, 10), (3000, 60)):
        P = A / t
        nm(b, 'b9', 'nb', 'Công suất', f"Một máy thực hiện công {A} J trong {t} s. Công suất của máy là:", P, [A * t, t / A, P * 2], 'W', f"$\\mathcal P=\\dfrac{{A}}{{t}}=\\dfrac{{{A}}}{{{t}}}={fnum(P)}$ W.")
        sa(b, 'b9', 'nb', 'Công suất', f"Máy thực hiện công {A} J trong {t} s. Tính công suất của máy (W).", P, f"$\\mathcal P=\\dfrac{{A}}{{t}}={fnum(P)}$ W.", 'W')
    for (P, t) in ((200, 30), (50, 60), (1500, 10), (100, 120)):
        nm(b, 'b9', 'th', 'Công từ công suất', f"Động cơ có công suất {P} W hoạt động trong {t} s. Công động cơ thực hiện là:", P * t, [P / t, t / P, P * t / 2], 'J', f"$A=\\mathcal P t={P}\\times{t}={P*t}$ J.")
    for (Fo, v) in ((500, 10), (2000, 15), (1200, 20), (300, 5)):
        nm(b, 'b9', 'th', 'Công suất theo lực và vận tốc', f"Xe chuyển động thẳng đều với vận tốc {v} m/s, lực kéo của động cơ là {Fo} N. Công suất của động cơ là:", Fo * v, [Fo / v, Fo + v, Fo * v / 2], 'W', f"$\\mathcal P=Fv={Fo}\\times{v}={Fo*v}$ W.")
    for (Pi, Pt) in ((80, 100), (450, 500), (30, 50), (600, 800)):
        H = Pi / Pt * 100
        nm(b, 'b9', 'vd', 'Hiệu suất', f"Máy tiêu thụ công suất {Pt} W và cho công suất có ích {Pi} W. Hiệu suất của máy là:", H, [Pt / Pi * 100 if Pt / Pi * 100 < 100 else 100 - H, 100 - H, H / 2], '%', f"$H=\\dfrac{{\\mathcal P_{{ci}}}}{{\\mathcal P_{{tp}}}}\\cdot100\\%=\\dfrac{{{Pi}}}{{{Pt}}}\\cdot100\\%={fnum(H)}\\%$.")
    for kwh in (1, 2, 0.5):
        nm(b, 'b9', 'nb', 'Đổi đơn vị công', f"{fnum(kwh)} kWh bằng bao nhiêu jun (J)?", kwh * 3.6e6, [kwh * 1000, kwh * 3600, kwh * 3.6e5], 'J', f"$1\\ \\text{{kWh}}=1000\\ \\text{{W}}\\times3600\\ \\text{{s}}=3{{,}}6\\times10^6$ J nên {fnum(kwh)} kWh $={fnum(kwh*3.6e6, 0)}$ J.", nd=0)
    for (m, v) in ((2, 3), (4, 5), (1, 10), (10, 2), (0.5, 8)):
        W = m * v * v / 2
        nm(b, 'b10', 'nb', 'Động năng', f"Vật khối lượng {fnum(m)} kg chuyển động với vận tốc {v} m/s. Động năng của vật là:", W, [m * v, m * v * v, m * v * v / 4], 'J', f"$W_đ=\\dfrac{{1}}{{2}}mv^2=\\dfrac{{1}}{{2}}\\times{fnum(m)}\\times{v}^2={fnum(W)}$ J.")
        sa(b, 'b10', 'nb', 'Động năng', f"Vật {fnum(m)} kg chuyển động với vận tốc {v} m/s. Tính động năng của vật (J).", W, f"$W_đ=\\dfrac{{1}}{{2}}mv^2={fnum(W)}$ J.", 'J')
    for (m, h) in ((2, 5), (0.5, 20), (10, 3), (4, 12)):
        W = m * 10 * h
        nm(b, 'b10', 'nb', 'Thế năng trọng trường', f"Vật khối lượng {fnum(m)} kg ở độ cao {h} m so với mặt đất (chọn mốc thế năng tại mặt đất), lấy $g=10$ m/s². Thế năng của vật là:", W, [m * h, m * 9.8 * h * 2, W / 2], 'J', f"$W_t=mgh={fnum(m)}\\times10\\times{h}={fnum(W)}$ J.")
    for h in (5, 20, 45, 80):
        v = math.sqrt(2 * 10 * h)
        nm(b, 'b10', 'th', 'Bảo toàn cơ năng - vật rơi', f"Thả rơi một vật từ độ cao {h} m so với mặt đất, bỏ qua sức cản không khí, lấy $g=10$ m/s². Vận tốc của vật khi chạm đất là:", v, [10 * h, h / 2, v / 2], 'm/s', f"Cơ năng bảo toàn: $mgh=\\dfrac{{1}}{{2}}mv^2\\Rightarrow v=\\sqrt{{2gh}}=\\sqrt{{2\\times10\\times{h}}}={fnum(v)}$ m/s.")
    for (v0, h1) in ((20, 0), (10, 0), (30, 0)):
        H = v0 * v0 / 20
        nm(b, 'b10', 'th', 'Bảo toàn cơ năng - ném lên', f"Ném một vật từ mặt đất thẳng đứng lên cao với vận tốc {v0} m/s, bỏ qua sức cản, lấy $g=10$ m/s². Độ cao cực đại vật đạt được là:", H, [v0 * v0 / 10, v0 / 10, v0 * v0], 'm', f"Cơ năng bảo toàn: $\\dfrac{{1}}{{2}}mv_0^2=mgH\\Rightarrow H=\\dfrac{{v_0^2}}{{2g}}=\\dfrac{{{v0}^2}}{{20}}={fnum(H)}$ m.")
    for (h, h2) in ((20, 5), (45, 20), (80, 35), (30, 10)):
        v = math.sqrt(2 * 10 * (h - h2))
        nm(b, 'b10', 'vd', 'Bảo toàn cơ năng - vận tốc tại độ cao h2', f"Vật được thả rơi không vận tốc đầu từ độ cao {h} m, bỏ qua sức cản, lấy $g=10$ m/s². Vận tốc của vật khi ở độ cao {h2} m là:", v, [math.sqrt(2 * 10 * h), 10 * (h - h2), math.sqrt(2 * 10 * h2)], 'm/s', f"Bảo toàn cơ năng giữa hai vị trí: $v=\\sqrt{{2g(h-h_2)}}=\\sqrt{{2\\times10\\times{h-h2}}}={fnum(v)}$ m/s.")
    for (m, v0, v, s) in ((2, 2, 6, 4), (1, 4, 8, 6), (4, 3, 5, 8), (5, 0, 4, 10)):
        dW = m * (v * v - v0 * v0) / 2; Fo = dW / s
        nm(b, 'b10', 'vd', 'Định lí động năng', f"Vật khối lượng {m} kg tăng vận tốc từ {v0} m/s lên {v} m/s trên quãng đường {s} m dưới tác dụng của lực không đổi cùng hướng chuyển động. Độ lớn lực đó là:", Fo, [m * (v - v0) / s, dW, Fo * 2], 'N', f"Theo định lí động năng: $Fs=\\dfrac{{1}}{{2}}m(v^2-v_0^2)={fnum(dW)}$ J nên $F=\\dfrac{{{fnum(dW)}}}{{{s}}}={fnum(Fo)}$ N.")
    for (m, v, s) in ((1000, 20, 40), (800, 10, 20), (2000, 15, 45), (500, 12, 36)):
        Fc = m * v * v / 2 / s
        nm(b, 'b10', 'vd', 'Lực hãm trung bình', f"Ô tô khối lượng {m} kg đang chạy với vận tốc {v} m/s thì hãm phanh và dừng lại sau khi đi thêm {s} m. Độ lớn lực hãm trung bình là:", Fc, [m * v * v / s, m * v / s, Fc / 2], 'N', f"Định lí động năng: $0-\\dfrac{{1}}{{2}}mv^2=-F_hs\\Rightarrow F_h=\\dfrac{{mv^2}}{{2s}}=\\dfrac{{{m}\\times{v}^2}}{{2\\times{s}}}={fnum(Fc)}$ N.")
    for (m, h1, h2) in ((2, 10, 4), (5, 8, 3), (1, 20, 5), (4, 6, 1)):
        A = m * 10 * (h1 - h2)
        nm(b, 'b9', 'vd', 'Công của trọng lực', f"Vật khối lượng {m} kg rơi từ độ cao {h1} m xuống độ cao {h2} m, lấy $g=10$ m/s². Công của trọng lực là:", A, [-A, m * 10 * h1, m * (h1 - h2)], 'J', f"$A=mg(h_1-h_2)={m}\\times10\\times({h1}-{h2})={A}$ J (dương vì vật đi xuống).")
    b.mc('b9', 'nb', 'Đơn vị công', "Đơn vị nào sau đây KHÔNG phải đơn vị của công?", "Oát (W)", ["Jun (J)", "Niutơn nhân mét (N·m)", "Kilôoát giờ (kWh)"], "Oát (W) là đơn vị của công suất. Công đo bằng jun (J), $1\\ \\text{J}=1\\ \\text{N}\\cdot\\text{m}$, hoặc kWh.")
    b.mc('b9', 'nb', 'Công cản', "Khi lực tác dụng ngược chiều với hướng dịch chuyển của vật thì công của lực đó:", "Âm", ["Dương", "Bằng không", "Luôn bằng độ lớn lực"], "Góc giữa lực và dịch chuyển là $180^\\circ$ nên $\\cos\\alpha=-1$, công $A=-Fs<0$ (công cản).")
    b.mc('b10', 'nb', 'Cơ năng', "Cơ năng của vật chuyển động trong trọng trường (chỉ chịu tác dụng của trọng lực) bằng:", "Tổng động năng và thế năng trọng trường", ["Hiệu của động năng và thế năng", "Tích của động năng và thế năng", "Chỉ bằng động năng"], "Cơ năng $W=W_đ+W_t$; khi chỉ có trọng lực sinh công thì cơ năng bảo toàn.")
    return b
