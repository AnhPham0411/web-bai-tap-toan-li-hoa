"""
Script sinh Dữ liệu Lý thuyết & Bài tập THẬT chuẩn GDPT 2018 cho Vật lí 10 và Hóa học 10.
Nội dung biên soạn chi tiết, chính xác theo SGK Kết nối tri thức với cuộc sống.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ==============================================================================
# 1. LÝ THUYẾT VẬT LÍ 10 (FULL REAL CONTENT - 5 CHAPTERS)
# ==============================================================================

def generate_ly10_theory():
    ly_theory = {
        "c1": {
            "chapterId": "c1",
            "title": "Mở đầu & Sai số trong đo lường",
            "lessons": [
                {
                    "id": "b1",
                    "title": "Bài 1. Mở đầu về Vật lí",
                    "blocks": [
                        { "type": "heading", "text": "1. Đối tượng nghiên cứu và mục tiêu của Vật lí" },
                        {
                            "type": "definition",
                            "title": "Đối tượng nghiên cứu của Vật lí",
                            "content": "Vật lí là ngành khoa học tự nhiên nghiên cứu về các dạng vận động của vật chất (cơ, nhiệt, điện, từ, quang, hạt nhân...) và năng lượng."
                        },
                        {
                            "type": "text",
                            "content": "Mục tiêu chính của Vật lí là khám phá ra các quy luật tổng quát điều khiển sự vận động của thế giới tự nhiên, từ các hạt cận nguyên tử đến toàn bộ vũ trụ."
                        },
                        {
                            "type": "heading", "text": "2. Phương pháp nghiên cứu Vật lí" },
                        {
                            "type": "list",
                            "title": "Hai phương pháp nghiên cứu chính",
                            "items": [
                                "Phương pháp thực nghiệm: Dựa trên quan sát, tiến hành thí nghiệm kiểm chứng để rút ra quy luật vật lí.",
                                "Phương pháp lý thuyết: Dựa trên lập luận toán học, suy luận logic từ các nguyên lý đã biết để dự đoán hiện tượng mới."
                            ]
                        },
                        {
                            "type": "heading", "text": "3. Quy tắc an toàn trong phòng thực hành" },
                        {
                            "type": "note",
                            "content": "Tuyệt đối tuân thủ hướng dẫn của giáo viên: Kiểm tra thiết bị điện trước khi cắm, không chạm tay ướt vào nguồn điện, ngắt điện ngay khi xảy ra sự cố chập cháy."
                        }
                    ]
                },
                {
                    "id": "b2",
                    "title": "Bài 2. Vấn đề an toàn & Sai số trong đo lường",
                    "blocks": [
                        { "type": "heading", "text": "1. Phép đo các đại lượng vật lí" },
                        {
                            "type": "definition",
                            "title": "Phép đo trực tiếp và gián tiếp",
                            "content": "Phép đo trực tiếp là so sánh đại lượng cần đo với đại lượng cùng loại bằng dụng cụ đo (dùng thước đo chiều dài, cân đo khối lượng).\nPhép đo gián tiếp là xác định đại lượng cần đo thông qua công thức liên hệ với các đại lượng đo trực tiếp (tính vận tốc v = s / t)."
                        },
                        { "type": "heading", "text": "2. Sai số phép đo" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Giá trị trung bình", "math": "\\bar{A} = \\frac{A_1 + A_2 + ... + A_n}{n}" },
                                { "label": "Sai số tuyệt đối trung bình", "math": "\\bar{\\Delta A} = \\frac{|\\bar{A} - A_1| + |\\bar{A} - A_2| + ... + |\\bar{A} - A_n|}{n}" },
                                { "label": "Sai số tuyệt đối phép đo", "math": "\\Delta A = \\bar{\\Delta A} + \\Delta A_{dc}" },
                                { "label": "Sai số tương đối", "math": "\\delta A = \\frac{\\Delta A}{\\bar{A}} \\cdot 100\\%" }
                            ]
                        },
                        {
                            "type": "theorem",
                            "title": "Cách ghi kết quả phép đo",
                            "content": "Kết quả đo đại lượng A được biểu diễn dưới dạng: A = \\bar{A} \\pm \\Delta A (trong đó \\Delta A thường lấy đến 1 hoặc 2 chữ số có nghĩa)."
                        },
                        {
                            "type": "example",
                            "question": "Đo chiều dài một chiếc bàn n lần được giá trị trung bình \\bar{l} = 1,250 m và sai số tuyệt đối \\Delta l = 0,005 m. Tính sai số tương đối \\delta l và ghi kết quả phép đo.",
                            "solution": "\\delta l = (\\Delta l / \\bar{l}) \\cdot 100\\% = (0,005 / 1,250) \\cdot 100\\% = 0,4\\%.\nKết quả đo: l = 1,250 \\pm 0,005 m."
                        }
                    ]
                }
            ]
        },
        "c2": {
            "chapterId": "c2",
            "title": "Mô tả chuyển động",
            "lessons": [
                {
                    "id": "b3",
                    "title": "Bài 3. Vận tốc & Độ dịch chuyển",
                    "blocks": [
                        { "type": "heading", "text": "1. Độ dịch chuyển và Quãng đường đi được" },
                        {
                            "type": "definition",
                            "title": "Độ dịch chuyển",
                            "content": "Độ dịch chuyển \\vec{d} là một đại lượng vectơ nối từ vị trí đầu đến vị trí cuối của chuyển động. Độ lớn của độ dịch chuyển d là khoảng cách giữa điểm đầu và điểm cuối."
                        },
                        {
                            "type": "note",
                            "content": "Khi vật chuyển động thẳng và không đổi chiều thì độ lớn độ dịch chuyển bằng quãng đường đi được (d = s). Nếu vật đổi chiều hoặc chuyển động cong thì d < s."
                        },
                        { "type": "heading", "text": "2. Vận tốc và Tốc độ" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Tốc độ trung bình", "math": "v_{tb} = \\frac{s}{\\Delta t}" },
                                { "label": "Vận tốc trung bình", "math": "\\vec{v}_{tb} = \\frac{\\Delta \\vec{d}}{\\Delta t}" }
                            ]
                        },
                        {
                            "type": "example",
                            "question": "Một xe đi từ A đến B dài 60 km mất 1 giờ, rồi quay lại A mất 1,5 giờ. Tính tốc độ trung bình và vận tốc trung bình của xe trong cả chuyến đi.",
                            "solution": "Tổng quãng đường s = 60 + 60 = 120 km. Tổng thời gian t = 1 + 1,5 = 2,5 h.\nTốc độ trung bình v_tb = 120 / 2,5 = 48 km/h.\nVị trí đầu và cuối trùng nhau nên độ dịch chuyển d = 0 => Vận tốc trung bình = 0 km/h."
                        }
                    ]
                },
                {
                    "id": "b4",
                    "title": "Bài 4. Chuyển động thẳng biến đổi đều",
                    "blocks": [
                        { "type": "heading", "text": "1. Gia tốc" },
                        {
                            "type": "definition",
                            "title": "Gia tốc",
                            "content": "Gia tốc \\vec{a} là đại lượng đặc trưng cho tốc độ biến thiên của vận tốc theo thời gian: \\vec{a} = \\frac{\\Delta \\vec{v}}{\\Delta t} = \\frac{\\vec{v} - \\vec{v}_0}{t - t_0}. Đơn vị: m/s²."
                        },
                        { "type": "heading", "text": "2. Các phương trình của chuyển động thẳng biến đổi đều" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Vận tốc", "math": "v = v_0 + a \\cdot t" },
                                { "label": "Độ dịch chuyển", "math": "d = v_0 \\cdot t + \\frac{1}{2} a \\cdot t^2" },
                                { "label": "Công thức độc lập thời gian", "math": "v^2 - v_0^2 = 2 \\cdot a \\cdot d" }
                            ]
                        },
                        {
                            "type": "note",
                            "content": "Chuyển động nhanh dần đều: a và v_0 cùng dấu (a \\cdot v_0 > 0).\nChuyển động chậm dần đều: a và v_0 ngược dấu (a \\cdot v_0 < 0)."
                        },
                        {
                            "type": "example",
                            "question": "Một ô tô hãm phanh với gia tốc a = −2 m/s² từ vận tốc v_0 = 20 m/s. Tính quãng đường ô tô đi được cho đến khi dừng lại.",
                            "solution": "Khi dừng lại v = 0 m/s. Áp dụng v² − v_0² = 2ad:\n0² − 20² = 2 · (−2) · d => −400 = −4d => d = 100 m."
                        }
                    ]
                }
            ]
        },
        "c3": {
            "chapterId": "c3",
            "title": "Chuyển động biến đổi & Động học nâng cao",
            "lessons": [
                {
                    "id": "b5",
                    "title": "Bài 5. Rơi tự do & Chuyển động ném",
                    "blocks": [
                        { "type": "heading", "text": "1. Sự rơi tự do" },
                        {
                            "type": "definition",
                            "title": "Chuyển động rơi tự do",
                            "content": "Sự rơi tự do là sự rơi chỉ chịu tác dụng của trọng lực. Chuyển động rơi tự do là chuyển động thẳng nhanh dần đều theo phương thẳng đứng, hướng từ trên xuống dưới."
                        },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Vận tốc rơi tự do", "math": "v = g \\cdot t" },
                                { "label": "Quãng đường / Độ cao", "math": "h = \\frac{1}{2} g \\cdot t^2" },
                                { "label": "Vận tốc theo độ cao", "math": "v = \\sqrt{2g h}" }
                            ]
                        },
                        {
                            "type": "heading", "text": "2. Chuyển động ném ngang" },
                            {
                                "type": "text",
                                "content": "Chuyển động ném ngang gồm 2 thành phần độc lập:\n- Theo phương nằm ngang Ox: Chuyển động thẳng đều với v_x = v_0, x = v_0 · t.\n- Theo phương thẳng đứng Oy: Chuyển động rơi tự do với v_y = g · t, y = 1/2 · g · t²."
                            },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Phương trình quỹ đạo", "math": "y = \\frac{g}{2 v_0^2} x^2 \\text{ (dạng một nhánh Parabol)}" },
                                { "label": "Tầm xa ném ngang", "math": "L = v_0 \\sqrt{\\frac{2h}{g}}" }
                            ]
                        }
                    ]
                },
                {
                    "id": "b6",
                    "title": "Bài 6. Tổng hợp & Phân tích lực",
                    "blocks": [
                        { "type": "heading", "text": "1. Lực và Hợp lực" },
                        {
                            "type": "definition",
                            "title": "Tổng hợp lực",
                            "content": "Tổng hợp lực là thay thế nhiều lực tác dụng đồng thời vào một vật bằng một lực duy nhất có tác dụng giống hệt các lực đó. Lực thay thế gọi là hợp lực \\vec{F} = \\vec{F}_1 + \\vec{F}_2 + ..."
                        },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Quy tắc hình bình hành", "math": "F^2 = F_1^2 + F_2^2 + 2 F_1 F_2 \\cos \\alpha" },
                                { "label": "Hai lực cùng chiều (α = 0°)", "math": "F = F_1 + F_2" },
                                { "label": "Hai lực ngược chiều (α = 180°)", "math": "F = |F_1 - F_2|" },
                                { "label": "Hai lực vuông góc (α = 90°)", "math": "F = \\sqrt{F_1^2 + F_2^2}" }
                            ]
                        },
                        {
                            "type": "definition",
                            "title": "Điều kiện cân bằng của chất điểm",
                            "content": "Một chất điểm cân bằng khi hợp lực của tất cả các lực tác dụng lên nó bằng không: \\sum \\vec{F} = \\vec{0}."
                        }
                    ]
                }
            ]
        },
        "c4": {
            "chapterId": "c4",
            "title": "Ba định luật Newton & Các lực cơ học",
            "lessons": [
                {
                    "id": "b7",
                    "title": "Bài 7. Ba định luật Newton",
                    "blocks": [
                        { "type": "heading", "text": "1. Định luật I Newton (Quán tính)" },
                        {
                            "type": "theorem",
                            "title": "Nội dung Định luật I Newton",
                            "content": "Nếu một vật không chịu tác dụng của lực nào hoặc chịu tác dụng của các lực có hợp lực bằng không, thì vật đang đứng yên sẽ tiếp tục đứng yên, vật đang chuyển động sẽ tiếp tục chuyển động thẳng đều."
                        },
                        { "type": "heading", "text": "2. Định luật II Newton" },
                        {
                            "type": "theorem",
                            "title": "Nội dung Định luật II Newton",
                            "content": "Gia tốc của một vật cùng hướng với lực tác dụng lên vật. Độ lớn của gia tốc tỉ lệ thuận với độ lớn của lực và tỉ lệ nghịch với khối lượng của vật: \\vec{a} = \\frac{\\vec{F}}{m} \\Rightarrow \\vec{F} = m \\cdot \\vec{a}."
                        },
                        { "type": "heading", "text": "3. Định luật III Newton" },
                        {
                            "type": "theorem",
                            "title": "Nội dung Định luật III Newton",
                            "content": "Trong mọi trường hợp, khi vật A tác dụng lên vật B một lực thì vật B cũng tác dụng lại vật A một lực. Hai lực này là hai lực trực đối: \\vec{F}_{AB} = -\\vec{F}_{BA} (cùng độ lớn, cùng phương, ngược chiều, đặt vào 2 vật khác nhau)."
                        }
                    ]
                },
                {
                    "id": "b8",
                    "title": "Bài 8. Các lực cơ học cơ bản",
                    "blocks": [
                        { "type": "heading", "text": "1. Trọng lực và Trọng lượng" },
                        {
                            "type": "text",
                            "content": "Trọng lực \\vec{P} là lực hút của Trái Đất tác dụng lên vật: \\vec{P} = m \\cdot \\vec{g}. Trọng lượng P = m · g là độ lớn của trọng lực."
                        },
                        { "type": "heading", "text": "2. Lực ma sát trượt" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Lực ma sát trượt", "math": "F_{mst} = \\mu \\cdot N" }
                            ]
                        },
                        {
                            "type": "note",
                            "content": "μ là hệ số ma sát trượt (không có đơn vị), N là độ lớn áp lực của vật lên mặt tiếp xúc."
                        },
                        { "type": "heading", "text": "3. Lực đàn hồi của lò xo (Định luật Hooke)" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Định luật Hooke", "math": "F_{dh} = k \\cdot |\\Delta l|" }
                            ]
                        },
                        {
                            "type": "text",
                            "content": "k là độ cứng của lò xo (N/m), Δl = l − l_0 là độ biến dạng của lò xo."
                        }
                    ]
                }
            ]
        },
        "c5": {
            "chapterId": "c5",
            "title": "Năng lượng & Công",
            "lessons": [
                {
                    "id": "b9",
                    "title": "Bài 9. Công & Công suất",
                    "blocks": [
                        { "type": "heading", "text": "1. Công cơ học" },
                        {
                            "type": "definition",
                            "title": "Công của lực không đổi",
                            "content": "Khi lực \\vec{F} không đổi tác dụng vào vật làm vật dịch chuyển quãng đường s theo hướng hợp với \\vec{F} một góc \\alpha thì công thực hiện là: A = F \\cdot s \\cdot \\cos \\alpha. Đơn vị: Joule (J)."
                        },
                        {
                            "type": "list",
                            "title": "Các trường hợp của góc α",
                            "items": [
                                "α < 90°: cos α > 0 => A > 0 (Công phát động).",
                                "α = 90°: cos α = 0 => A = 0 (Lực không sinh công).",
                                "α > 90°: cos α < 0 => A < 0 (Công cản)."
                            ]
                        },
                        { "type": "heading", "text": "2. Công suất" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Công suất trung bình", "math": "P = \\frac{A}{t} = F \\cdot v" }
                            ]
                        },
                        {
                            "type": "text",
                            "content": "Công suất là đại lượng đặc trưng cho tốc độ thực hiện công. Đơn vị: Watt (W), 1 kW = 1000 W, 1 HP (mã lực) ≈ 746 W."
                        }
                    ]
                },
                {
                    "id": "b10",
                    "title": "Bài 10. Cơ năng & Bảo toàn năng lượng",
                    "blocks": [
                        { "type": "heading", "text": "1. Động năng và Thế năng" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Động năng", "math": "W_d = \\frac{1}{2} m \\cdot v^2" },
                                { "label": "Thế năng trọng trường", "math": "W_t = m \\cdot g \\cdot h" },
                                { "label": "Cơ năng", "math": "W = W_d + W_t = \\frac{1}{2} m \\cdot v^2 + m \\cdot g \\cdot h" }
                            ]
                        },
                        { "type": "heading", "text": "2. Định luật bảo toàn cơ năng" },
                        {
                            "type": "theorem",
                            "title": "Định luật bảo toàn cơ năng",
                            "content": "Khi một vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực (không có lực cản, lực ma sát) thì cơ năng của vật là một đại lượng bảo toàn: W = W_d + W_t = \\text{hằng số}."
                        },
                        {
                            "type": "example",
                            "question": "Thả rơi một vật 1 kg từ độ cao h = 20 m xuống đất với g = 10 m/s². Tính vận tốc của vật ngay trước khi chạm đất.",
                            "solution": "Chọn gốc thế năng tại mặt đất. Bảo toàn cơ năng:\nW_đđầu + W_tđầu = W_đcuối + W_tcuối\n0 + mgh = 1/2 · m · v² + 0\n=> v = \\sqrt{2gh} = \\sqrt{2 \\cdot 10 \\cdot 20} = \\sqrt{400} = 20 m/s."
                        }
                    ]
                }
            ]
        }
    }

    for c_id, doc in ly_theory.items():
        save_json(os.path.join(DATA_DIR, "ly10", "theory", f"{c_id}.json"), doc)

# ==============================================================================
# 2. LÝ THUYẾT HÓA HỌC 10 (FULL REAL CONTENT - 5 CHAPTERS)
# ==============================================================================

def generate_hoa10_theory():
    hoa_theory = {
        "c1": {
            "chapterId": "c1",
            "title": "Cấu tạo nguyên tử",
            "lessons": [
                {
                    "id": "b1",
                    "title": "Bài 1. Thành phần nguyên tử",
                    "blocks": [
                        { "type": "heading", "text": "1. Thành phần cấu tạo nguyên tử" },
                        {
                            "type": "definition",
                            "title": "Cấu tạo nguyên tử",
                            "content": "Nguyên tử gồm hạt nhân nằm ở tâm (chứa proton mang điện +1, neutron không mang điện) và vỏ nguyên tử chứa các electron (mang điện -1) chuyển động xung quanh hạt nhân."
                        },
                        {
                            "type": "table",
                            "title": "Đặc tính các hạt cấu tạo nguyên tử",
                            "headers": ["Hạt", "Kí hiệu", "Điện tích tương đối", "Khối lượng (amu)"],
                            "rows": [
                                ["Proton", "p", "+1", "1,00727 ≈ 1"],
                                ["Neutron", "n", "0", "1,00866 ≈ 1"],
                                ["Electron", "e", "-1", "0,00055 ≈ 0"]
                            ]
                        },
                        { "type": "heading", "text": "2. Điện tích hạt nhân và Số khối" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Số hiệu nguyên tử", "math": "Z = p = e" },
                                { "label": "Số khối", "math": "A = Z + N" },
                                { "label": "Kí hiệu nguyên tử", "math": "_{Z}^{A}\\text{X}" }
                            ]
                        },
                        { "type": "heading", "text": "3. Đồng vị & Khối lượng nguyên tử trung bình" },
                        {
                            "type": "definition",
                            "title": "Đồng vị",
                            "content": "Đồng vị là các nguyên tử của cùng một nguyên tố hóa học, có cùng số proton (Z) nhưng khác nhau về số neutron (N), dẫn đến số khối (A) khác nhau."
                        },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Khối lượng nguyên tử trung bình", "math": "\\bar{A} = \\frac{A_1 \\cdot x + A_2 \\cdot y + ...}{100}" }
                            ]
                        }
                    ]
                },
                {
                    "id": "b2",
                    "title": "Bài 2. Cấu hình electron nguyên tử",
                    "blocks": [
                        { "type": "heading", "text": "1. Lớp và Phân lớp electron" },
                        {
                            "type": "text",
                            "content": "Các electron sắp xếp thành từng lớp từ gần hạt nhân ra xa: Lớp K (n=1), Lớp L (n=2), Lớp M (n=3), Lớp N (n=4).\nCác phân lớp kí hiệu s, p, d, f với số electron tối đa tương ứng là: s² (2e), p⁶ (6e), d¹⁰ (10e), f¹⁴ (14e)."
                        },
                        { "type": "heading", "text": "2. Quy tắc viết cấu hình electron" },
                        {
                            "type": "list",
                            "title": "Trật tự mức năng lượng",
                            "items": [
                                "1s 2s 2p 3s 3p 4s 3d 4p 5s...",
                                "Lưu ý: Phân lớp 4s có mức năng lượng thấp hơn 3d nên e được điền vào 4s trước 3d."
                            ]
                        },
                        {
                            "type": "example",
                            "question": "Viết cấu hình electron của nguyên tử Fe (Z = 26).",
                            "solution": "Trật tự năng lượng: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶.\nSắp xếp lại theo lớp từ trong ra ngoài: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s² (hoặc viết gọn [Ar] 3d⁶ 4s²)."
                        }
                    ]
                }
            ]
        },
        "c2": {
            "chapterId": "c2",
            "title": "Bảng tuần hoàn các nguyên tố hóa học",
            "lessons": [
                {
                    "id": "b3",
                    "title": "Bài 3. Bảng tuần hoàn các nguyên tố",
                    "blocks": [
                        { "type": "heading", "text": "1. Nguyên tắc sắp xếp trong Bảng tuần hoàn" },
                        {
                            "type": "list",
                            "title": "3 nguyên tắc cơ bản",
                            "items": [
                                "Các nguyên tố được sắp xếp theo chiều tăng dần của điện tích hạt nhân nguyên tử.",
                                "Các nguyên tố có cùng số lớp electron được xếp vào cùng một hàng (Chu kỳ).",
                                "Các nguyên tố có cùng số electron hóa trị được xếp vào cùng một cột (Nhóm)."
                            ]
                        },
                        { "type": "heading", "text": "2. Cấu tạo Bảng tuần hoàn" },
                        {
                            "type": "text",
                            "content": "- Ô nguyên tố: Cho biết Z, kí hiệu, tên nguyên tố, khối lượng nguyên tử, độ âm điện...\n- Chu kỳ: Có 7 chu kỳ (chu kỳ 1, 2, 3 là chu kỳ nhỏ; 4, 5, 6, 7 là chu kỳ lớn).\n- Nhóm: Gồm nhóm A (nguyên tố s, p) và nhóm B (nguyên tố d, f)."
                        }
                    ]
                },
                {
                    "id": "b4",
                    "title": "Bài 4. Xu hướng biến đổi tính chất",
                    "blocks": [
                        { "type": "heading", "text": "1. Bán kính nguyên tử và Độ âm điện" },
                        {
                            "type": "theorem",
                            "title": "Quy luật biến đổi trong Bảng tuần hoàn",
                            "content": "- Trong 1 Chu kỳ (từ trái qua phải): Bán kính nguyên tử giảm dần, Độ âm điện tăng dần, Tính kim loại giảm dần, Tính phi kim tăng dần.\n- Trong 1 Nhóm A (từ trên xuống dưới): Bán kính nguyên tử tăng dần, Độ âm điện giảm dần, Tính kim loại tăng dần, Tính phi kim giảm dần."
                        },
                        { "type": "heading", "text": "2. Định luật tuần hoàn" },
                        {
                            "type": "definition",
                            "title": "Định luật tuần hoàn",
                            "content": "Tính chất của các nguyên tố và đơn chất, cũng như thành phần và tính chất của các hợp chất tạo nên từ chúng biến đổi tuần hoàn theo chiều tăng của điện tích hạt nhân nguyên tử."
                        }
                    ]
                }
            ]
        },
        "c3": {
            "chapterId": "c3",
            "title": "Liên kết hóa học",
            "lessons": [
                {
                    "id": "b5",
                    "title": "Bài 5. Liên kết ion & Liên kết cộng hóa trị",
                    "blocks": [
                        { "type": "heading", "text": "1. Quy tắc Octet (8 electron)" },
                        {
                            "type": "definition",
                            "title": "Quy tắc Octet",
                            "content": "Trong quá trình hình thành liên kết hóa học, các nguyên tử có xu hướng nhường, nhận hoặc góp chung electron để đạt được cấu hình electron bền vững của khí hiếm với 8 electron lớp ngoài cùng (hoặc 2 electron với Helium)."
                        },
                        { "type": "heading", "text": "2. Phân loại liên kết dựa trên Độ âm điện (Δχ)" },
                        {
                            "type": "table",
                            "title": "Phân loại liên kết theo hiệu độ âm điện Δχ",
                            "headers": ["Hiệu độ âm điện Δχ", "Loại liên kết", "Ví dụ"],
                            "rows": [
                                ["0,0 ≤ Δχ < 0,4", "Liên kết cộng hóa trị không cực", "H₂, O₂, N₂"],
                                ["0,4 ≤ Δχ < 1,7", "Liên kết cộng hóa trị có cực", "HCl, H₂O, NH₃"],
                                ["Δχ ≥ 1,7", "Liên kết ion", "NaCl, CaO, KBr"]
                            ]
                        }
                    ]
                },
                {
                    "id": "b6",
                    "title": "Bài 6. Liên kết hydrogen & Tương tác van der Waals",
                    "blocks": [
                        { "type": "heading", "text": "1. Liên kết hydrogen" },
                        {
                            "type": "definition",
                            "title": "Liên kết hydrogen",
                            "content": "Liên kết hydrogen là một loại liên kết yếu được hình thành giữa nguyên tử H (đã liên kết với nguyên tử có độ âm điện lớn như F, O, N) với một nguyên tử có độ âm điện lớn khác (F, O, N) còn cặp electron chưa liên kết."
                        },
                        {
                            "type": "note",
                            "content": "Liên kết hydrogen làm tăng nhiệt độ sôi và nhiệt độ nóng chảy của các chất như H₂O, HF, NH₃, C₂H₅OH so với các chất không có liên kết hydrogen."
                        }
                    ]
                }
            ]
        },
        "c4": {
            "chapterId": "c4",
            "title": "Phản ứng oxi hóa - khử",
            "lessons": [
                {
                    "id": "b7",
                    "title": "Bài 7. Số oxi hóa & Phản ứng Oxi hóa - Khử",
                    "blocks": [
                        { "type": "heading", "text": "1. Số oxi hóa" },
                        {
                            "type": "list",
                            "title": "Quy tắc xác định số oxi hóa",
                            "items": [
                                "Số oxi hóa của nguyên tố trong đơn chất bằng 0 (ví dụ: Cu⁰, O₂⁰).",
                                "Trong hợp chất: H thường là +1, O thường là -2, Kim loại kiềm (nhóm IA) là +1, kiềm thổ (IIA) là +2, Al là +3.",
                                "Tổng số oxi hóa của các nguyên tử trong phân tử bằng 0, trong ion bằng điện tích của ion đó."
                            ]
                        },
                        { "type": "heading", "text": "2. Khái niệm Phản ứng Oxi hóa - Khử" },
                        {
                            "type": "theorem",
                            "title": "Khái niệm quan trọng",
                            "content": "- Chất khử (chất bị oxi hóa): Nhường electron, số oxi hóa TĂNG sau phản ứng.\n- Chất oxi hóa (chất bị khử): Nhận electron, số oxi hóa GIẢM sau phản ứng.\n- Quá trình oxi hóa: Sự nhường electron.\n- Quá trình khử: Sự nhận electron."
                        }
                    ]
                },
                {
                    "id": "b8",
                    "title": "Bài 8. Cân bằng phản ứng Oxi hóa - Khử",
                    "blocks": [
                        { "type": "heading", "text": "1. Phương pháp thăng bằng electron" },
                        {
                            "type": "list",
                            "title": "4 bước cân bằng",
                            "items": [
                                "Bước 1: Xác định số oxi hóa của các nguyên tố thay đổi số oxi hóa.",
                                "Bước 2: Viết quá trình oxi hóa và quá trình khử.",
                                "Bước 3: Tìm hệ số thích hợp sao cho Tổng số electron nhường = Tổng số electron nhận.",
                                "Bước 4: Đặt hệ số vào phương trình và hoàn thành cân bằng."
                            ]
                        },
                        {
                            "type": "example",
                            "question": "Cân bằng phản ứng: Cu + HNO₃(đặc) -> Cu(NO₃)₂ + NO₂ + H₂O.",
                            "solution": "Cu⁰ -> Cu⁺² + 2e (Chất khử, nhường 2e)\nN⁺⁵ + 1e -> N⁺⁴ (Chất oxi hóa, nhận 1e)\nNhân hệ số: 1 × (nhường 2e) và 2 × (nhận 1e).\nPhương trình: Cu + 4HNO₃ -> Cu(NO₃)₂ + 2NO₂ + 2H₂O."
                        }
                    ]
                }
            ]
        },
        "c5": {
            "chapterId": "c5",
            "title": "Năng lượng hóa học & Enthalpy",
            "lessons": [
                {
                    "id": "b9",
                    "title": "Bài 9. Biến thiên Enthalpy trong phản ứng",
                    "blocks": [
                        { "type": "heading", "text": "1. Phản ứng tỏa nhiệt và Thu nhiệt" },
                        {
                            "type": "definition",
                            "title": "Phản ứng tỏa nhiệt và thu nhiệt",
                            "content": "Phản ứng tỏa nhiệt là phản ứng giải phóng năng lượng dưới dạng nhiệt ra môi trường (Δr H₂₉₈⁰ < 0).\nPhản ứng thu nhiệt là phản ứng hấp thụ năng lượng dưới dạng nhiệt từ môi trường (Δr H₂₉₈⁰ > 0)."
                        },
                        { "type": "heading", "text": "2. Biến thiên Enthalpy chuẩn" },
                        {
                            "type": "text",
                            "content": "Biến thiên enthalpy chuẩn của phản ứng kí hiệu là Δr H₂₉₈⁰, tính ở điều kiện chuẩn: nhiệt độ 25 °C (298 K) và áp suất 1 bar."
                        }
                    ]
                },
                {
                    "id": "b10",
                    "title": "Bài 10. Tính biến thiên Enthalpy",
                    "blocks": [
                        { "type": "heading", "text": "1. Tính theo Nhiệt tạo thành chuẩn Δf H₂₉₈⁰" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Công thức tính theo Δf H", "math": "\\Delta_r H_{298}^0 = \\sum \\Delta_f H_{298}^0 (SP) - \\sum \\Delta_f H_{298}^0 (CĐ)" }
                            ]
                        },
                        { "type": "heading", "text": "2. Tính theo Năng lượng liên kết E_b (cho phản ứng thể khí)" },
                        {
                            "type": "formula",
                            "items": [
                                { "label": "Công thức tính theo E_b", "math": "\\Delta_r H_{298}^0 = \\sum E_b (CĐ) - \\sum E_b (SP)" }
                            ]
                        }
                    ]
                }
            ]
        }
    }

    for c_id, doc in hoa_theory.items():
        save_json(os.path.join(DATA_DIR, "hoa10", "theory", f"{c_id}.json"), doc)

# ==============================================================================
# MAIN EXECUTOR
# ==============================================================================

if __name__ == "__main__":
    generate_ly10_theory()
    generate_hoa10_theory()
    print("Generated full authentic Theory JSON files for Physics 10 and Chemistry 10 successfully!")
