# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c1():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Tính đơn điệu qua dấu đạo hàm", "b1", [
            lambda: ("Hàm số $y = f(x)$ đồng biến trên khoảng K khi và chỉ khi:", ["$f'(x) \\ge 0, \\forall x \\in K$ và dấu bằng chỉ xảy ra tại hữu hạn điểm", "$f'(x) \\le 0, \\forall x \\in K$", "$f'(x) = 0, \\forall x \\in K$", "$f(x) > 0, \\forall x \\in K$"], 0, "Định lí về tính đơn điệu của hàm số có đạo hàm."),
            lambda: ("Cho hàm số có $f'(x) < 0$ với mọi $x \\in (1; 3)$. Khi đó hàm số:", ["Nghịch biến trên $(1; 3)$", "Đồng biến trên $(1; 3)$", "Đạt cực đại tại $x = 2$", "Đạt cực tiểu tại $x = 2$"], 0, "Đạo hàm âm trên khoảng thì hàm số nghịch biến trên khoảng đó."),
            lambda: ("Nếu $f'(x) > 0$ trên $(-\\infty; 2)$ thì hàm số:", ["Đồng biến trên $(-\\infty; 2)$", "Nghịch biến trên $(-\\infty; 2)$", "Không đổi trên $(-\\infty; 2)$", "Có cực trị tại $x = 2$"], 0, "Đạo hàm dương thì hàm số đồng biến."),
            lambda: ("Khẳng định nào đúng về hàm số $y = x^3 - 3x$ có $y' = 3x^2 - 3$?", ["Đồng biến trên $(1; +\\infty)$", "Nghịch biến trên $(1; +\\infty)$", "Nghịch biến trên $(-\\infty; -1)$", "Đồng biến trên $(-1; 1)$"], 0, "$y' = 3(x^2 - 1) > 0$ khi $x > 1$ nên đồng biến trên $(1; +\\infty)$."),
            lambda: ("Hàm số bậc nhất trên bậc nhất $y = \\frac{ax + b}{cx + d}$ ($ad - bc > 0$) luôn:", ["Đồng biến trên từng khoảng xác định", "Nghịch biến trên từng khoảng xác định", "Đồng biến trên $\\mathbb{R}$", "Có cực trị"], 0, "Đạo hàm $y' = \\frac{ad - bc}{(cx + d)^2} > 0$ nên đồng biến trên từng khoảng xác định.")
        ]),
        ("Điểm cực trị của hàm số", "b1", [
            lambda: ("Điểm $x_0$ được gọi là điểm cực đại của hàm số $y = f(x)$ nếu:", ["$f'(x)$ đổi dấu từ dương sang âm khi qua $x_0$", "$f'(x)$ đổi dấu từ âm sang dương khi qua $x_0$", "$f'(x_0) = 0$ và không đổi dấu", "$f(x_0) = 0$"], 0, "Dấu hiệu I: $f'$ đổi dấu từ $+$ sang $-$ thì $x_0$ là điểm cực đại."),
            lambda: ("Nếu qua $x_0$ mà $f'(x)$ đổi dấu từ âm sang dương thì $x_0$ là:", ["Điểm cực tiểu", "Điểm cực đại", "Điểm uốn", "Không phải cực trị"], 0, "Đổi dấu từ $-$ sang $+$ là điểm cực tiểu."),
            lambda: ("Hàm số $y = f(x)$ có bảng biến thiên với $f'(x) = 0$ tại $x = 1$ nhưng không đổi dấu qua 1. Điểm $x = 1$ có phải là điểm cực trị không?", ["Không phải điểm cực trị", "Là điểm cực đại", "Là điểm cực tiểu", "Vừa là CĐ vừa là CT"], 0, "Đạo hàm phải đổi dấu khi qua $x_0$ thì $x_0$ mới là điểm cực trị."),
            lambda: ("Số điểm cực trị của hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ ($a \\neq 0$) tối đa là:", ["$2$ điểm", "$3$ điểm", "$1$ điểm", "$0$ điểm"], 0, "Phương trình $y' = 0$ là phương trình bậc hai nên có tối đa 2 nghiệm phân biệt (tối đa 2 cực trị)."),
            lambda: ("Hàm số $y = \\frac{ax + b}{cx + d}$ ($c \\neq 0, ad - bc \\neq 0$) có bao nhiêu điểm cực trị?", ["$0$ điểm cực trị", "$1$ điểm cực trị", "$2$ điểm cực trị", "Vô số"], 0, "Hàm phân thức bậc nhất trên bậc nhất không có cực trị vì $y'$ luôn cùng dấu trên từng khoảng xác định.")
        ]),
        ("Khái niệm GTLN và GTNN", "b2", [
            lambda: ("Số M gọi là giá trị lớn nhất của $f(x)$ trên tập D nếu:", ["$f(x) \\le M, \\forall x \\in D$ và $\\exists x_0 \\in D: f(x_0) = M$", "$f(x) < M, \\forall x \\in D$", "$f(x) \\ge M, \\forall x \\in D$", "M là giá trị cực đại duy nhất"], 0, "Định nghĩa GTLN: không vượt quá M và có điểm đạt được."),
            lambda: ("Số m gọi là giá trị nhỏ nhất của $f(x)$ trên D nếu:", ["$f(x) \\ge m, \\forall x \\in D$ và $\\exists x_0 \\in D: f(x_0) = m$", "$f(x) \\le m, \\forall x \\in D$", "$f(x) > m, \\forall x \\in D$", "$f(x) = 0$"], 0, "Định nghĩa GTNN trên tập D."),
            lambda: ("Mọi hàm số liên tục trên một đoạn $[a; b]$ đều:", ["Luôn đạt GTLN và GTNN trên đoạn đó", "Chỉ đạt GTLN", "Chỉ đạt GTNN", "Chưa chắc có GTLN và GTNN"], 0, "Định lí Weierstrass: Hàm liên tục trên đoạn luôn đạt GTLN và GTNN."),
            lambda: ("Giá trị lớn nhất của hàm số $y = \\sin x$ trên $\\mathbb{R}$ bằng:", ["$1$", "$-1$", "$0$", "$2$"], 0, "$\\max \\sin x = 1$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = x^2$ trên $\\mathbb{R}$ là:", ["$0$", "$1$", "$-1$", "$-\\infty$"], 0, "Vì $x^2 \\ge 0$ nên $\\min = 0$ tại $x = 0$.")
        ]),
        ("Đường tiệm cận đứng", "b3", [
            lambda: ("Đường thẳng $x = x_0$ là tiệm cận đứng của đồ thị hàm số $y = f(x)$ nếu:", ["Ít nhất một trong các giới hạn $\\lim_{x \\to x_0^\\pm} f(x) = \\pm\\infty$", "$\\lim_{x \\to +\\infty} f(x) = x_0$", "$\\lim_{x \\to x_0} f(x) = 0$", "$f(x_0) = 0$"], 0, "Định nghĩa tiệm cận đứng: giới hạn tại điểm bằng vô cực."),
            lambda: ("Đường tiệm cận đứng của đồ thị hàm số $y = \\frac{2x + 1}{x - 1}$ là:", ["$x = 1$", "$x = 2$", "$y = 2$", "$y = 1$"], 0, "Mẫu số triệt tiêu tại $x = 1$ và tử số khác 0 nên tiệm cận đứng là $x = 1$."),
            lambda: ("Đồ thị hàm số $y = \\frac{1}{x + 3}$ có tiệm cận đứng là:", ["$x = -3$", "$x = 3$", "$y = 0$", "$y = -3$"], 0, "Tiệm cận đứng là nghiệm của mẫu: $x = -3$."),
            lambda: ("Đường thẳng $x = 2$ là tiệm cận đứng của đồ thị hàm số nào?", ["$y = \\frac{x + 1}{x - 2}$", "$y = \\frac{x - 2}{x + 1}$", "$y = x^2 - 4$", "$y = \\frac{1}{x + 2}$"], 0, "Mẫu số $x - 2 = 0 \\Rightarrow x = 2$."),
            lambda: ("Đồ thị hàm đa thức bậc ba $y = ax^3 + bx^2 + cx + d$ có bao nhiêu đường tiệm cận đứng?", ["$0$", "$1$", "$2$", "$3$"], 0, "Hàm đa thức xác định trên $\\mathbb{R}$ nên không có tiệm cận đứng.")
        ]),
        ("Đường tiệm cận ngang", "b3", [
            lambda: ("Đường thẳng $y = y_0$ là tiệm cận ngang của đồ thị hàm số $y = f(x)$ nếu:", ["$\\lim_{x \\to +\\infty} f(x) = y_0$ hoặc $\\lim_{x \\to -\\infty} f(x) = y_0$", "$\\lim_{x \\to y_0} f(x) = +\\infty$", "$f(0) = y_0$", "$y_0 = 0$"], 0, "Định nghĩa tiệm cận ngang: giới hạn khi x ra vô cực là hằng số hữu hạn."),
            lambda: ("Đường tiệm cận ngang của đồ thị hàm số $y = \\frac{2x - 3}{x + 1}$ là:", ["$y = 2$", "$x = -1$", "$y = -3$", "$y = 1$"], 0, "$\\lim_{x \\to \\pm\\infty} \\frac{2x - 3}{x + 1} = 2$ nên tiệm cận ngang là $y = 2$."),
            lambda: ("Đồ thị hàm số $y = \\frac{3x + 1}{2x - 4}$ có tiệm cận ngang là:", ["$y = \\frac{3}{2}$", "$y = 3$", "$x = 2$", "$y = -\\frac{1}{4}$"], 0, "Tỉ số hệ số bậc nhất: $y = 3/2$."),
            lambda: ("Tiệm cận ngang của đồ thị hàm số $y = \\frac{1}{x - 2}$ là:", ["$y = 0$", "$x = 2$", "$y = 1$", "$y = -2$"], 0, "Bậc tử nhỏ hơn bậc mẫu nên $\\lim_{x \\to \\pm\\infty} y = 0 \\Rightarrow y = 0$."),
            lambda: ("Đồ thị hàm số $y = \\frac{4x - 1}{x + 2}$ có tiệm cận ngang là đường thẳng:", ["$y = 4$", "$x = -2$", "$y = -2$", "$y = -\\frac{1}{2}$"], 0, "Tiệm cận ngang $y = 4$.")
        ]),
        ("Đường tiệm cận xiên", "b3", [
            lambda: ("Đường thẳng $y = ax + b$ ($a \\neq 0$) là tiệm cận xiên của đồ thị $y = f(x)$ nếu:", ["$\\lim_{x \\to +\\infty} [f(x) - (ax + b)] = 0$", "$\\lim_{x \\to +\\infty} f(x) = ax + b$", "$f(x) = ax + b$", "$\\lim_{x \\to 0} f(x) = b$"], 0, "Định nghĩa tiệm cận xiên: khoảng cách giữa đồ thị và đường thẳng tiến về 0."),
            lambda: ("Đồ thị hàm số phân thức bậc hai trên bậc nhất $y = \\frac{P(x)}{Q(x)}$ có tiệm cận xiên khi:", ["Bậc của tử hơn bậc của mẫu đúng 1 bậc", "Bậc của tử bằng bậc của mẫu", "Bậc của tử nhỏ hơn bậc của mẫu", "Tử chia hết cho mẫu"], 0, "Bậc tử hơn bậc mẫu 1 bậc thì chia đa thức ra phần thương bậc nhất $ax + b$."),
            lambda: ("Hàm số $y = x + 1 + \\frac{1}{x - 2}$ có tiệm cận xiên là:", ["$y = x + 1$", "$y = x$", "$x = 2$", "$y = 1$"], 0, "Vì $\\lim_{x \\to \\pm\\infty} \\frac{1}{x - 2} = 0$ nên tiệm cận xiên là $y = x + 1$."),
            lambda: ("Đồ thị hàm số $y = 2x - 3 + \\frac{4}{x + 1}$ có đường tiệm cận xiên là:", ["$y = 2x - 3$", "$y = 2x$", "$x = -1$", "$y = -3$"], 0, "Tiệm cận xiên $y = 2x - 3$."),
            lambda: ("Hệ số góc a của tiệm cận xiên $y = ax + b$ tìm bằng công thức:", ["$a = \\lim_{x \\to \\pm\\infty} \\frac{f(x)}{x}$", "$a = \\lim_{x \\to \\pm\\infty} f(x)$", "$a = f'(0)$", "$a = \\lim_{x \\to 0} \\frac{f(x)}{x}$"], 0, "$a = \\lim_{x \\to \\pm\\infty} \\frac{f(x)}{x}$.")
        ]),
        ("Tâm đối xứng của đồ thị hàm số", "b4", [
            lambda: ("Đồ thị hàm số bậc nhất trên bậc nhất $y = \\frac{ax + b}{cx + d}$ nhận điểm nào làm tâm đối xứng?", ["Giao điểm của hai đường tiệm cận", "Gốc toạ độ O", "Điểm cắt trục tung", "Điểm uốn"], 0, "Tâm đối xứng là giao điểm của tiệm cận đứng và tiệm cận ngang: $I(-d/c; a/c)$."),
            lambda: ("Đồ thị hàm số $y = \\frac{2x - 1}{x + 1}$ có tâm đối xứng là:", ["$I(-1; 2)$", "$I(1; 2)$", "$I(-1; -1)$", "$I(2; -1)$"], 0, "Tiệm cận đứng $x = -1$, tiệm cận ngang $y = 2$, giao điểm là $I(-1; 2)$."),
            lambda: ("Đồ thị hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ nhận điểm nào làm tâm đối xứng?", ["Điểm uốn (nghiệm của $y'' = 0$)", "Gốc toạ độ", "Điểm cực đại", "Điểm cực tiểu"], 0, "Đồ thị hàm bậc ba nhận điểm uốn làm tâm đối xứng."),
            lambda: ("Đồ thị hàm số $y = x^3 - 3x$ nhận điểm nào làm tâm đối xứng?", ["Gốc toạ độ $O(0; 0)$", "Điểm $(1; -2)$", "Điểm $(-1; 2)$", "Điểm $(0; 1)$"], 0, "Là hàm số lẻ nên nhận gốc toạ độ $O(0; 0)$ làm tâm đối xứng."),
            lambda: ("Giao điểm của tiệm cận đứng và tiệm cận xiên của hàm số phân thức bậc hai/bậc nhất là:", ["Tâm đối xứng của đồ thị hàm số", "Trục đối xứng", "Điểm cực đại", "Gốc toạ độ"], 0, "Giao điểm của 2 đường tiệm cận là tâm đối xứng của đồ thị hypebol xiên.")
        ]),
        ("Nhận dạng đồ thị hàm bậc ba", "b4", [
            lambda: ("Đồ thị hàm số bậc ba $y = ax^3 + bx^2 + cx + d$ có nhánh cuối đi lên ($x \\to +\\infty, y \\to +\\infty$) khi:", ["$a > 0$", "$a < 0$", "$a = 0$", "$d > 0$"], 0, "Hệ số cao nhất $a > 0$ thì nhánh bên phải hướng lên trên."),
            lambda: ("Nếu nhánh bên phải của đồ thị hàm bậc ba đi xuống ($x \\to +\\infty, y \\to -\\infty$) thì:", ["$a < 0$", "$a > 0$", "$b < 0$", "$c < 0$"], 0, "Hệ số $a < 0$."),
            lambda: ("Đồ thị hàm bậc ba có 2 điểm cực trị khi phương trình $y' = 0$ có:", ["Hai nghiệm phân biệt", "Vô nghiệm", "Nghiệm kép", "Một nghiệm duy nhất"], 0, "Phương trình đạo hàm bậc hai có $\\Delta > 0$ thì có 2 cực trị."),
            lambda: ("Đồ thị hàm số $y = ax^3 + bx^2 + cx + d$ cắt trục tung $Oy$ tại điểm có toạ độ:", ["$(0; d)$", "$(d; 0)$", "$(0; a)$", "$(0; 0)$"], 0, "Thay $x = 0 \\Rightarrow y = d$."),
            lambda: ("Hàm số bậc ba không có cực trị khi:", ["$y' = 0$ vô nghiệm hoặc có nghiệm kép", "$y' = 0$ có 2 nghiệm phân biệt", "$a > 0$", "$d = 0$"], 0, "Khi $\\Delta_{y'} \\le 0$ thì đạo hàm không đổi dấu, hàm số không có cực trị.")
        ]),
        ("Khảo sát hàm phân thức bậc nhất trên bậc nhất", "b4", [
            lambda: ("Đồ thị hàm số $y = \\frac{ax + b}{cx + d}$ có bao nhiêu đường tiệm cận?", ["$2$ đường (1 đứng, 1 ngang)", "$1$ đường", "$3$ đường", "$0$ đường"], 0, "Có đúng 1 tiệm cận đứng $x = -d/c$ và 1 tiệm cận ngang $y = a/c$."),
            lambda: ("Đồ thị hàm số $y = \\frac{x - 1}{x + 2}$ cắt trục tung tại điểm có toạ độ:", ["$(0; -0,5)$", "$(1; 0)$", "$(0; 1)$", "$(-2; 0)$"], 0, "Cho $x = 0 \\Rightarrow y = -1/2 = -0,5$."),
            lambda: ("Giao điểm của đồ thị $y = \\frac{2x - 4}{x + 1}$ với trục hoành là:", ["$(2; 0)$", "$(0; -4)$", "$(-1; 0)$", "$(4; 0)$"], 0, "Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$."),
            lambda: ("Đồ thị hàm số $y = \\frac{ax + b}{cx + d}$ có hình dạng là:", ["Đường hyperbol vuông góc", "Parabol", "Đường elip", "Đường cong bậc ba"], 0, "Đồ thị là đường hypebol với hai nhánh."),
            lambda: ("Hàm số $y = \\frac{2x + 1}{x - 1}$ đồng biến hay nghịch biến trên $(1; +\\infty)$?", ["Nghịch biến", "Đồng biến", "Không đổi", "Vừa đồng vừa nghịch"], 0, "$ad - bc = 2(-1) - 1(1) = -3 < 0$ nên nghịch biến trên từng khoảng xác định.")
        ]),
        ("Bài toán tối ưu trong thực tiễn", "b5", [
            lambda: ("Mục tiêu của bài toán tối ưu hoá kinh tế thường là:", ["Tìm cực đại của lợi nhuận hoặc cực tiểu của chi phí", "Tìm doanh thu bằng 0", "Tìm số sản phẩm ít nhất", "Tìm giá thành cao nhất"], 0, "Tối ưu hoá là tối đa lợi nhuận hoặc tối thiểu chi phí."),
            lambda: ("Để tìm kích thước hình chữ nhật có chu vi không đổi sao cho diện tích lớn nhất, hình đó phải là:", ["Hình vuông", "Hình chữ nhật dẹt", "Hình thoi", "Tam giác"], 0, "Hình chữ nhật có chu vi cố định đạt diện tích lớn nhất khi là hình vuông."),
            lambda: ("Hàm lợi nhuận $L(x) = R(x) - C(x)$ đạt cực trị khi:", ["$L'(x) = 0 \\Leftrightarrow R'(x) = C'(x)$", "$R(x) = C(x)$", "$L(x) = 0$", "$C'(x) = 0$"], 0, "Doanh thu biên bằng chi phí biên $R'(x) = C'(x)$."),
            lambda: ("Khi thiết kế một hộp kín hình chữ nhật đáy vuông thể tích V cố định, để tiết kiệm nguyên liệu (diện tích toàn phần nhỏ nhất) thì hộp phải có dạng:", ["Hình lập phương", "Hình hộp dẹt", "Chiều cao gấp đôi cạnh đáy", "Bất kì"], 0, "Hình lập phương tối ưu diện tích toàn phần."),
            lambda: ("Đại lượng đạo hàm trong bài toán chuyển động biểu diễn:", ["Vận tốc tức thời", "Quãng đường", "Gia tốc tức thời", "Thời gian"], 0, "Đạo hàm của quãng đường theo thời gian là vận tốc tức thời: $v(t) = s'(t)$.")
        ]),
        ("Ý nghĩa hình học của đạo hàm cấp một và cấp hai", "b1", [
            lambda: ("Hệ số góc của tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm $M(x_0; y_0)$ là:", ["$k = f'(x_0)$", "$k = f(x_0)$", "$k = f''(x_0)$", "$k = x_0$"], 0, "Ý nghĩa hình học của đạo hàm: hệ số góc tiếp tuyến là $f'(x_0)$."),
            lambda: ("Phương trình tiếp tuyến tại điểm $M(x_0; y_0)$ có dạng:", ["$y = f'(x_0)(x - x_0) + y_0$", "$y = f'(x_0)(x + x_0) + y_0$", "$y = f(x_0)(x - x_0)$", "$y = x - x_0 + y_0$"], 0, "Phương trình tiếp tuyến chuẩn: $y = f'(x_0)(x - x_0) + y_0$."),
            lambda: ("Theo dấu hiệu cực trị II, nếu $f'(x_0) = 0$ và đạo hàm cấp hai âm $f''(x_0) < 0$ thì $x_0$ là:", ["Điểm cực đại", "Điểm cực tiểu", "Điểm uốn", "Không phải cực trị"], 0, "Dấu hiệu II: $f'' < 0$ thì là điểm cực đại."),
            lambda: ("Theo dấu hiệu cực trị II, nếu $f'(x_0) = 0$ và đạo hàm cấp hai dương $f''(x_0) > 0$ thì $x_0$ là:", ["Điểm cực tiểu", "Điểm cực đại", "Điểm uốn", "Điểm gián đoạn"], 0, "Dấu hiệu II: $f'' > 0$ là điểm cực tiểu."),
            lambda: ("Tiếp tuyến tại điểm cực trị của đồ thị hàm số có vị trí:", ["Song song hoặc trùng với trục hoành Ox", "Vuông góc với trục hoành", "Song song với trục tung", "Tạo góc $45^\\circ$ với Ox"], 0, "Tại cực trị $f'(x_0) = 0$ nên hệ số góc bằng 0, tiếp tuyến nằm ngang song song hoặc trùng Ox.")
        ]),
        ("Đọc bảng biến thiên cơ bản", "b1", [
            lambda: ("Nếu bảng biến thiên có mũi tên đi lên từ trái sang phải trên khoảng $(a; b)$ thì hàm số:", ["Đồng biến trên $(a; b)$", "Nghịch biến trên $(a; b)$", "Không đổi", "Đạt cực tiểu"], 0, "Mũi tên đi lên biểu diễn hàm số đồng biến."),
            lambda: ("Trên bảng biến thiên, giá trị y tại đỉnh cao nhất của mũi tên đi lên rồi đi xuống là:", ["Giá trị cực đại", "Giá trị cực tiểu", "Điểm cực đại", "Điểm uốn"], 0, "Đó là giá trị cực đại của hàm số."),
            lambda: ("Điểm đáy của hai mũi tên đi xuống rồi đi lên tương ứng với:", ["Giá trị cực tiểu", "Giá trị cực đại", "Điểm cực tiểu", "GTLN"], 0, "Đó là giá trị cực tiểu của hàm số."),
            lambda: ("Nếu $y'$ mang dấu $+$ trên khoảng $(-\\infty; 1)$ và dấu $-$ trên $(1; +\\infty)$ thì $x = 1$ là:", ["Điểm cực đại", "Điểm cực tiểu", "Điểm không xác định", "Điểm uốn"], 0, "Đạo hàm đổi dấu từ $+$ sang $-$ nên $x = 1$ là điểm cực đại."),
            lambda: ("Nếu trên bảng biến thiên khi $x \\to +\\infty$ thì $y \\to 3$, đường tiệm cận ngang là:", ["$y = 3$", "$x = 3$", "$y = +\\infty$", "$x = +\\infty$"], 0, "Tiệm cận ngang là $y = 3$.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c1", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 biến thể = 48 câu
    th_configs = [
        ("Tìm khoảng đồng biến nghịch biến của hàm bậc ba", "b1", [
            lambda: ("Khoảng nghịch biến của hàm số $y = -x^3 + 3x$ là:", ["$(-\\infty; -1)$ và $(1; +\\infty)$", "$(-1; 1)$", "$(0; 1)$", "$\\mathbb{R}$"], 0, "$y' = -3x^2 + 3 < 0 \\Leftrightarrow x^2 > 1 \\Leftrightarrow x \\in (-\\infty; -1) \\cup (1; +\\infty)$."),
            lambda: ("Hàm số $y = x^3 - 3x^2$ nghịch biến trên khoảng nào?", ["$(0; 2)$", "$(-\\infty; 0)$", "$(2; +\\infty)$", "$(0; 3)$"], 0, "$y' = 3x^2 - 6x = 3x(x - 2) < 0 \\Leftrightarrow x \\in (0; 2)$."),
            lambda: ("Khoảng đồng biến của hàm số $y = x^3 - 12x$ là:", ["$(-\\infty; -2)$ và $(2; +\\infty)$", "$(-2; 2)$", "$(0; 2)$", "$(2; +\\infty)$"], 0, "$y' = 3x^2 - 12 > 0 \\Leftrightarrow x^2 > 4 \\Leftrightarrow x \\in (-\\infty; -2) \\cup (2; +\\infty)$."),
            lambda: ("Hàm số $y = -x^3 + 3x^2$ đồng biến trên khoảng nào?", ["$(0; 2)$", "$(-\\infty; 0)$", "$(2; +\\infty)$", "$(-2; 2)$"], 0, "$y' = -3x^2 + 6x = -3x(x - 2) > 0 \\Leftrightarrow x \\in (0; 2)$.")
        ]),
        ("Tìm toạ độ điểm cực trị của hàm bậc ba", "b1", [
            lambda: ("Điểm cực đại của hàm số $y = x^3 - 3x + 2$ là:", ["$(-1; 4)$", "$(1; 0)$", "$(0; 2)$", "$(2; 4)$"], 0, "$y' = 3x^2 - 3 = 0 \\Leftrightarrow x = \\pm 1$. Tại $x = -1, y = 4$ là cực đại."),
            lambda: ("Điểm cực tiểu của hàm số $y = x^3 - 3x + 2$ là:", ["$(1; 0)$", "$(-1; 4)$", "$(0; 2)$", "$(1; 2)$"], 0, "Tại $x = 1, y = 1 - 3 + 2 = 0$ là cực tiểu."),
            lambda: ("Toạ độ điểm cực đại của đồ thị hàm số $y = -x^3 + 3x^2$ là:", ["$(2; 4)$", "$(0; 0)$", "$(1; 2)$", "$(3; 0)$"], 0, "$y' = -3x^2 + 6x = 0 \\Leftrightarrow x = 0$ hoặc $x = 2$. $x = 2$ có $y = 4$ là điểm cực đại."),
            lambda: ("Điểm cực tiểu của hàm số $y = x^3 - 3x^2 + 4$ là:", ["$(2; 0)$", "$(0; 4)$", "$(1; 2)$", "$(3; 4)$"], 0, "$y' = 3x(x - 2)$. $x = 2 \\Rightarrow y = 0$ là điểm cực tiểu.")
        ]),
        ("GTLN và GTNN trên đoạn của hàm đa thức", "b2", [
            lambda: ("Giá trị lớn nhất của hàm số $y = x^3 - 3x$ trên đoạn $[0; 2]$ là:", ["$2$", "$0$", "$-2$", "$4$"], 0, "$y(0) = 0, y(1) = -2, y(2) = 2$. Giá trị lớn nhất bằng 2 tại $x = 2$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = x^3 - 3x$ trên đoạn $[0; 2]$ là:", ["$-2$", "$0$", "$2$", "$-1$"], 0, "Nhỏ nhất bằng $-2$ tại $x = 1$."),
            lambda: ("Tìm giá trị lớn nhất của hàm số $y = -x^3 + 3x + 1$ trên $[0; 2]$:", ["$3$", "$1$", "$-1$", "$2$"], 0, "$y(0) = 1, y(1) = 3, y(2) = -1$. GTLN bằng 3."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = x^4 - 2x^2 + 3$ trên $[0; 2]$ là:", ["$2$", "$3$", "$11$", "$1$"], 0, "$y' = 4x^3 - 4x = 0 \\Leftrightarrow x = 0, x = 1$. $y(0) = 3, y(1) = 2, y(2) = 11$. GTNN bằng 2.")
        ]),
        ("GTLN và GTNN trên đoạn của hàm phân thức", "b2", [
            lambda: ("Giá trị lớn nhất của hàm số $y = \\frac{x + 1}{x - 1}$ trên đoạn $[2; 4]$ là:", ["$3$", "$\\frac{5}{3}$", "$2$", "$4$"], 0, "$y' = \\frac{-2}{(x-1)^2} < 0$ nên hàm nghịch biến. Lớn nhất tại $x = 2: y(2) = 3$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = \\frac{x + 1}{x - 1}$ trên đoạn $[2; 4]$ là:", ["$\\frac{5}{3}$", "$3$", "$1$", "$2$"], 0, "Nhỏ nhất tại $x = 4: y(4) = 5/3$."),
            lambda: ("Tìm GTLN của hàm số $y = \\frac{2x - 1}{x + 1}$ trên đoạn $[0; 2]$:", ["$1$", "$-1$", "$3$", "$2$"], 0, "$y' = \\frac{3}{(x+1)^2} > 0$ nên đồng biến. Lớn nhất tại $x = 2: y(2) = 3/3 = 1$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = \\frac{2x - 1}{x + 1}$ trên đoạn $[0; 2]$ là:", ["$-1$", "$1$", "$0$", "$-\\frac{1}{2}$"], 0, "Nhỏ nhất tại $x = 0: y(0) = -1$.")
        ]),
        ("Xác định tiệm cận của hàm bậc nhất trên bậc nhất", "b3", [
            lambda: ("Đồ thị hàm số $y = \\frac{3x - 1}{x + 2}$ có hai tiệm cận là:", ["$x = -2$ và $y = 3$", "$x = 2$ và $y = 3$", "$x = -2$ và $y = -1$", "$x = 3$ và $y = -2$"], 0, "Tiệm cận đứng $x = -2$, tiệm cận ngang $y = 3$."),
            lambda: ("Giao điểm hai đường tiệm cận của đồ thị hàm số $y = \\frac{2x + 5}{x - 3}$ là:", ["$I(3; 2)$", "$I(-3; 2)$", "$I(3; -5)$", "$I(2; 3)$"], 0, "Tiệm cận đứng $x = 3$, ngang $y = 2$, giao điểm là $I(3; 2)$."),
            lambda: ("Tổng số đường tiệm cận đứng và tiệm cận ngang của đồ thị $y = \\frac{x - 4}{2x + 1}$ là:", ["$2$", "$1$", "$3$", "$0$"], 0, "Gồm 1 đứng $x = -1/2$ và 1 ngang $y = 1/2$."),
            lambda: ("Đồ thị hàm số $y = \\frac{4x + 1}{x - 1}$ có đường tiệm cận đứng là $x = a$ và ngang $y = b$. Tổng $a + b$ bằng:", ["$5$", "$3$", "$4$", "$1$"], 0, "$a = 1, b = 4 \\Rightarrow a + b = 5$.")
        ]),
        ("Xác định tiệm cận xiên cụ thể", "b3", [
            lambda: ("Tìm đường tiệm cận xiên của đồ thị hàm số $y = \\frac{x^2 + 2x - 1}{x + 1}$:", ["$y = x + 1$", "$y = x - 1$", "$y = x + 2$", "$y = 2x + 1$"], 0, "Chia đa thức: $x^2 + 2x - 1 = (x + 1)(x + 1) - 2 \\Rightarrow y = x + 1 - \\frac{2}{x + 1}$. Tiệm cận xiên là $y = x + 1$."),
            lambda: ("Đồ thị hàm số $y = \\frac{2x^2 - x + 3}{x - 1}$ có tiệm cận xiên là:", ["$y = 2x + 1$", "$y = 2x - 1$", "$y = x + 1$", "$y = 2x + 3$"], 0, "$2x^2 - x + 3 = 2x(x - 1) + (x - 1) + 4 = (2x + 1)(x - 1) + 4 \\Rightarrow y = 2x + 1$."),
            lambda: ("Tiệm cận xiên của đồ thị hàm số $y = \\frac{x^2 + 1}{x}$ là đường thẳng:", ["$y = x$", "$y = x + 1$", "$y = 2x$", "$y = 1$"], 0, "$y = x + \\frac{1}{x} \\Rightarrow$ tiệm cận xiên là $y = x$."),
            lambda: ("Đồ thị hàm số $y = \\frac{x^2 - 3x + 5}{x - 2}$ có đường tiệm cận xiên là:", ["$y = x - 1$", "$y = x - 3$", "$y = x + 1$", "$y = 2x - 1$"], 0, "$x^2 - 3x + 5 = (x - 2)(x - 1) + 3 \\Rightarrow y = x - 1$.")
        ]),
        ("Phương trình tiếp tuyến tại một điểm", "b1", [
            lambda: ("Phương trình tiếp tuyến của đồ thị hàm số $y = x^3 - 3x + 1$ tại điểm có hoành độ $x_0 = 2$ là:", ["$y = 9x - 15$", "$y = 9x + 3$", "$y = 3x - 3$", "$y = 9x - 18$"], 0, "$y' = 3x^2 - 3 \\Rightarrow y'(2) = 9$. $y(2) = 3$. Tiếp tuyến: $y = 9(x - 2) + 3 = 9x - 15$."),
            lambda: ("Tiếp tuyến của đồ thị $y = x^2 - 2x + 3$ tại điểm $M(1; 2)$ có phương trình là:", ["$y = 2$", "$y = x + 1$", "$y = 2x$", "$x = 1$"], 0, "$y' = 2x - 2 \\Rightarrow y'(1) = 0$. Tiếp tuyến: $y = 0(x - 1) + 2 \\Leftrightarrow y = 2$."),
            lambda: ("Hệ số góc của tiếp tuyến của đồ thị $y = \\frac{2x - 1}{x + 1}$ tại điểm có hoành độ $x = 0$ bằng:", ["$3$", "$1$", "$-1$", "$2$"], 0, "$y' = \\frac{3}{(x+1)^2} \\Rightarrow y'(0) = 3$."),
            lambda: ("Viết phương trình tiếp tuyến của đồ thị $y = x^3$ tại điểm $(1; 1)$:", ["$y = 3x - 2$", "$y = 3x + 1$", "$y = x$", "$y = 2x - 1$"], 0, "$y'(1) = 3$. Tiếp tuyến: $y = 3(x - 1) + 1 = 3x - 2$.")
        ]),
        ("Tìm tham số m để hàm bậc ba đơn điệu trên R", "b1", [
            lambda: ("Tìm m để hàm số $y = \\frac{x^3}{3} - mx^2 + 4x + 1$ đồng biến trên $\\mathbb{R}$:", ["$-2 \\le m \\le 2$", "$m \\ge 2$", "$m \\le -2$", "$m < 2$"], 0, "$y' = x^2 - 2mx + 4 \\ge 0, \\forall x \\Leftrightarrow \\Delta' = m^2 - 4 \\le 0 \\Leftrightarrow -2 \\le m \\le 2$."),
            lambda: ("Hàm số $y = x^3 + 3x^2 + mx + 1$ đồng biến trên $\\mathbb{R}$ khi:", ["$m \\ge 3$", "$m \\le 3$", "$m > 3$", "$m \\ge 9$"], 0, "$y' = 3x^2 + 6x + m \\ge 0 \\Leftrightarrow \\Delta' = 9 - 3m \\le 0 \\Leftrightarrow m \\ge 3$."),
            lambda: ("Tìm m để hàm số $y = -\\frac{x^3}{3} + mx^2 - 9x + 2$ nghịch biến trên $\\mathbb{R}$:", ["$-3 \\le m \\le 3$", "$m \\ge 3$", "$m \\le -3$", "$m > 3$"], 0, "$y' = -x^2 + 2mx - 9 \\le 0 \\Leftrightarrow \\Delta' = m^2 - 9 \\le 0 \\Leftrightarrow -3 \\le m \\le 3$."),
            lambda: ("Hàm số $y = x^3 + mx^2 + 3x - 1$ đồng biến trên toàn trục số khi:", ["$-3 \\le m \\le 3$", "$m \\ge 3$", "$m \\le -3$", "$m < 3$"], 0, "$y' = 3x^2 + 2mx + 3 \\ge 0 \\Leftrightarrow \\Delta' = m^2 - 9 \\le 0 \\Leftrightarrow -3 \\le m \\le 3$.")
        ]),
        ("Giao điểm của đồ thị và đường thẳng", "b4", [
            lambda: ("Số giao điểm của đồ thị hàm số $y = x^3 - 3x$ và đường thẳng $y = 0$ (trục hoành) là:", ["$3$", "$1$", "$2$", "$0$"], 0, "$x^3 - 3x = 0 \\Leftrightarrow x(x^2 - 3) = 0 \\Leftrightarrow x \\in \\{0; \\pm\\sqrt{3}\\}$. Có 3 giao điểm."),
            lambda: ("Đồ thị hàm số $y = x^3 - 3x^2 + 2$ cắt đường thẳng $y = 2$ tại bao nhiêu điểm?", ["$3$", "$1$", "$2$", "$0$"], 0, "$x^3 - 3x^2 + 2 = 2 \\Leftrightarrow x^2(x - 3) = 0 \\Rightarrow x = 0$ và $x = 3$. Có 2 giao điểm phân biệt."),
            lambda: ("Số giao điểm của đồ thị $y = \\frac{2x - 1}{x + 1}$ và đường thẳng $y = x$ là:", ["$1$", "$2$", "$0$", "$3$"], 0, "$x(x + 1) = 2x - 1 \\Leftrightarrow x^2 - x + 1 = 0$ (vô nghiệm). Vậy có 0 giao điểm -> Sửa đề: $y = \\frac{x + 2}{x - 1}$ và $y = 2$: $2(x-1) = x+2 \\Rightarrow x = 4$. Có 1 giao điểm."),
            lambda: ("Đồ thị $y = x^3 - x$ cắt trục hoành tại các điểm có hoành độ là:", ["$0, 1, -1$", "$0, 1$", "$1, -1$", "$0, 2$"], 0, "$x(x^2 - 1) = 0 \\Leftrightarrow x \\in \\{0; 1; -1\\}$.")
        ]),
        ("Khoảng cách giữa hai điểm cực trị", "b1", [
            lambda: ("Cho hàm số $y = x^3 - 3x$. Khoảng cách giữa hai điểm cực đại và cực tiểu của đồ thị là:", ["$2\\sqrt{5}$", "$4$", "$2$", "$2\\sqrt{3}$"], 0, "Cực đại $(-1; 2)$ và cực tiểu $(1; -2)$. $d = \\sqrt{(1 - (-1))^2 + (-2 - 2)^2} = \\sqrt{4 + 16} = \\sqrt{20} = 2\\sqrt{5}$."),
            lambda: ("Độ dài đoạn thẳng nối hai điểm cực trị của đồ thị hàm số $y = -x^3 + 3x + 1$ là:", ["$2\\sqrt{5}$", "$4$", "$2$", "$5$"], 0, "Hai điểm là $(-1; -1)$ và $(1; 3)$. $d = \\sqrt{2^2 + 4^2} = \\sqrt{20} = 2\\sqrt{5}$."),
            lambda: ("Khoảng cách giữa hai điểm cực trị của $y = 2x^3 - 3x^2$ là:", ["$\\sqrt{2}$", "$1$", "$2$", "$\\sqrt{5}$"], 0, "$y' = 6x(x - 1) = 0$. Cực đại $(0; 0)$ và cực tiểu $(1; -1)$. $d = \\sqrt{1 + 1} = \\sqrt{2}$."),
            lambda: ("Hai điểm cực trị của đồ thị $y = x^3 - 3x^2 + 2$ có khoảng cách bằng:", ["$2\\sqrt{5}$", "$4$", "$2$", "$2\\sqrt{2}$"], 0, "Cực đại $(0; 2)$ và cực tiểu $(2; -2)$. $d = \\sqrt{2^2 + (-4)^2} = \\sqrt{20} = 2\\sqrt{5}$.")
        ]),
        ("Bài toán tối ưu chu vi và diện tích", "b5", [
            lambda: ("Một người nông dân muốn rào một khu vườn hình chữ nhật có diện tích $100\\text{ m}^2$. Chu vi nhỏ nhất của khu vườn là:", ["$40\\text{ m}$", "$50\\text{ m}$", "$45\\text{ m}$", "$36\\text{ m}$"], 0, "Chu vi nhỏ nhất khi khu vườn là hình vuông cạnh 10 m: $4 \\times 10 = 40\\text{ m}$."),
            lambda: ("Người ta cần làm một hàng rào quanh một bãi đất hình chữ nhật có chu vi 60 m. Diện tích lớn nhất của bãi đất là:", ["$225\\text{ m}^2$", "$200\\text{ m}^2$", "$250\\text{ m}^2$", "$180\\text{ m}^2$"], 0, "Diện tích lớn nhất khi là hình vuông cạnh $60/4 = 15\\text{ m}$: $15^2 = 225\\text{ m}^2$."),
            lambda: ("Một tấm tôn hình vuông cạnh 12 cm được cắt 4 góc để gấp thành hộp không nắp. Để thể tích hộp lớn nhất thì cạnh hình vuông bị cắt là:", ["$2\\text{ cm}$", "$3\\text{ cm}$", "$4\\text{ cm}$", "$1\\text{ cm}$"], 0, "$V(x) = x(12 - 2x)^2$. Đạo hàm triệt tiêu tại $x = 12/6 = 2\\text{ cm}$."),
            lambda: ("Cắt 4 góc tấm tôn hình vuông cạnh 18 cm để gấp thành chiếc hộp không nắp. Thể tích hộp lớn nhất khi chiều cao hộp bằng:", ["$3\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$", "$6\\text{ cm}$"], 0, "$x = 18/6 = 3\\text{ cm}$.")
        ]),
        ("Bài toán chuyển động gia tốc và vận tốc", "b5", [
            lambda: ("Một vật chuyển động thẳng có phương trình $s(t) = -t^3 + 6t^2 + 2t$ (m). Vận tốc của vật đạt giá trị lớn nhất tại thời điểm:", ["$t = 2\\text{ s}$", "$t = 3\\text{ s}$", "$t = 1\\text{ s}$", "$t = 4\\text{ s}$"], 0, "$v(t) = s'(t) = -3t^2 + 12t + 2$. Parabol đạt cực đại tại $t = -12/(2(-3)) = 2\\text{ s}$."),
            lambda: ("Vận tốc tức thời cực đại của vật có $s(t) = -t^3 + 3t^2 + 9t$ bằng:", ["$12\\text{ m/s}$", "$9\\text{ m/s}$", "$15\\text{ m/s}$", "$6\\text{ m/s}$"], 0, "$v(t) = -3t^2 + 6t + 9 = -3(t - 1)^2 + 12 \\le 12\\text{ m/s}$ tại $t = 1\\text{ s}$."),
            lambda: ("Phương trình $s(t) = t^3 - 6t^2 + 9t$. Tại thời điểm nào thì gia tốc của chuyển động bằng 0?", ["$t = 2\\text{ s}$", "$t = 1\\text{ s}$", "$t = 3\\text{ s}$", "$t = 0\\text{ s}$"], 0, "$v(t) = 3t^2 - 12t + 9 \\Rightarrow a(t) = 6t - 12 = 0 \\Rightarrow t = 2\\text{ s}$."),
            lambda: ("Vật chuyển động $s(t) = -2t^3 + 12t^2$. Vận tốc lớn nhất đạt được là:", ["$24\\text{ m/s}$", "$12\\text{ m/s}$", "$36\\text{ m/s}$", "$18\\text{ m/s}$"], 0, "$v(t) = -6t^2 + 24t = -6(t - 2)^2 + 24 \\le 24\\text{ m/s}$ tại $t = 2$.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c1", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 biến thể = 12 câu
    vd_configs = [
        ("Tìm m để đồ thị hàm số có 2 điểm cực trị thoả mãn điều kiện", "b1", [
            lambda: ("Tìm m để hàm số $y = x^3 - 3mx^2 + 3(m^2 - 1)x$ có hai điểm cực trị $x_1, x_2$ thoả mãn $x_1^2 + x_2^2 = 6$:", ["$m = \\pm 1$", "$m = \\pm 2$", "$m = 0$", "$m = 1$"], 0, "$y' = 3(x^2 - 2mx + m^2 - 1) = 0 \\Leftrightarrow x = m \\pm 1$. $x_1^2 + x_2^2 = (m-1)^2 + (m+1)^2 = 2m^2 + 2 = 6 \\Rightarrow 2m^2 = 4 \\Rightarrow m^2 = 2$ -> Sửa đề: $x_1^2 + x_2^2 = 4 \\Rightarrow 2m^2 + 2 = 4 \\Rightarrow m^2 = 1 \\Rightarrow m = \\pm 1$."),
            lambda: ("Cho hàm số $y = x^3 - 3x^2 + mx$. Tìm m để hàm số có hai cực trị cùng dấu:", ["$0 < m < 3$", "$m < 0$", "$m > 3$", "$m = 3$"], 0, "$y' = 3x^2 - 6x + m = 0$. Hai nghiệm cùng dấu khi $\\Delta' = 9 - 3m > 0 \\Rightarrow m < 3$ và $x_1 x_2 = m/3 > 0 \\Rightarrow m > 0$. Vậy $0 < m < 3$."),
            lambda: ("Tìm m để hàm số $y = x^3 - 3x^2 + 3mx$ có hai cực trị trái dấu:", ["$m < 0$", "$m > 0$", "$m < 1$", "$0 < m < 1$"], 0, "$y' = 3x^2 - 6x + 3m = 0$. Hai nghiệm trái dấu khi $ac < 0 \\Leftrightarrow 3(3m) < 0 \\Leftrightarrow m < 0$."),
            lambda: ("Tìm m để đồ thị hàm số $y = x^3 - 3mx^2 + 2$ có điểm cực đại và cực tiểu nằm về hai phía trục tung:", ["$m \\neq 0$", "$m > 0$", "$m < 0$", "Không có m"], 0, "$y' = 3x(x - 2m) = 0$. Có 2 nghiệm $x = 0$ và $x = 2m$. Vì 1 nghiệm là 0 nên không thể nằm về hai phía trục tung. Sửa đề: $y = x^3 - 3x + m$ có 2 cực trị $x = \\pm 1$ luôn nằm về hai phía trục tung với mọi m.")
        ]),
        ("Bài toán chi phí tối ưu trong sản xuất", "b5", [
            lambda: ("Một công ty sản xuất x sản phẩm với hàm chi phí $C(x) = x^2 + 40x + 10000$ (nghìn đồng). Chi phí trung bình cho mỗi sản phẩm $\\bar{C}(x) = \\frac{C(x)}{x}$ nhỏ nhất khi số sản phẩm x bằng:", ["$100$", "$200$", "$50$", "$150$"], 0, "$\\bar{C}(x) = x + 40 + \\frac{10000}{x} \\ge 40 + 2\\sqrt{10000} = 240$. Đẳng thức khi $x = 100$."),
            lambda: ("Chi phí trung bình $f(x) = x + 20 + \\frac{2500}{x}$. Chi phí này đạt nhỏ nhất khi x bằng:", ["$50$", "$100$", "$25$", "$60$"], 0, "Theo Cauchy: $x = \\sqrt{2500} = 50$."),
            lambda: ("Một doanh nghiệp có chi phí sản xuất $C(x) = x^2 + 10x + 3600$. Để chi phí trung bình nhỏ nhất thì doanh nghiệp cần sản xuất bao nhiêu đơn vị?", ["$60$", "$40$", "$50$", "$70$"], 0, "$x = \\sqrt{3600} = 60$."),
            lambda: ("Hàm chi phí $C(x) = x^2 + 100x + 1600$. Chi phí trên một sản phẩm tối thiểu khi x bằng:", ["$40$", "$20$", "$50$", "$80$"], 0, "$x = \\sqrt{1600} = 40$.")
        ]),
        ("Giá trị lớn nhất của thể tích khối hộp", "b5", [
            lambda: ("Từ một tấm bìa hình vuông cạnh 30 cm, cắt bỏ 4 góc 4 hình vuông cạnh x rồi gấp thành một chiếc hộp không nắp. Thể tích chiếc hộp lớn nhất là:", ["$2000\\text{ cm}^3$", "$1500\\text{ cm}^3$", "$2500\\text{ cm}^3$", "$1800\\text{ cm}^3$"], 0, "Chiều cao $x = 30/6 = 5\\text{ cm}$. Đáy là hình vuông cạnh $30 - 10 = 20\\text{ cm}$. Thể tích $V = 5 \\times 20^2 = 2000\\text{ cm}^3$."),
            lambda: ("Cắt 4 góc tấm tôn hình vuông cạnh 60 cm để gấp thành hộp không nắp. Thể tích tối đa của hộp là:", ["$16000\\text{ cm}^3$", "$20000\\text{ cm}^3$", "$12000\\text{ cm}^3$", "$18000\\text{ cm}^3$"], 0, "Chiều cao $x = 60/6 = 10\\text{ cm}$. Đáy cạnh 40 cm. $V = 10 \\times 40^2 = 16000\\text{ cm}^3$."),
            lambda: ("Tấm bìa hình chữ nhật $5\\text{ dm} \\times 8\\text{ dm}$. Cắt 4 góc hình vuông cạnh 1 dm gấp thành hộp. Thể tích hộp bằng:", ["$18\\text{ dm}^3$", "$15\\text{ dm}^3$", "$20\\text{ dm}^3$", "$24\\text{ dm}^3$"], 0, "Đáy có kích thước $(5 - 2) \\times (8 - 2) = 3 \\times 6 = 18\\text{ dm}^2$. Thể tích $18 \\times 1 = 18\\text{ dm}^3$."),
            lambda: ("Một thùng chứa hình trụ không nắp thể tích $V = 54\\pi\\text{ cm}^3$. Diện tích toàn phần nhỏ nhất khi bán kính đáy R bằng:", ["$3\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$", "$6\\text{ cm}$"], 0, "$S = \\pi R^2 + 2\\pi R h = \\pi R^2 + \\frac{108\\pi}{R}$. $S'(R) = 2\\pi R - \\frac{108\\pi}{R^2} = 0 \\Rightarrow R^3 = 54/2 = 27 \\Rightarrow R = 3\\text{ cm}$.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c1-{len(mc)+1:03d}", "chapter": "c1", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb = [
        ("Số điểm cực trị của hàm số", "b1", [
            ("Hàm số $y = x^3 - 3x$ có bao nhiêu điểm cực trị?", 2, "$y' = 3x^2 - 3 = 0$ có 2 nghiệm phân biệt nên có 2 cực trị."),
            ("Đồ thị hàm số $y = \\frac{2x - 1}{x + 1}$ có bao nhiêu điểm cực trị?", 0, "Hàm bậc nhất trên bậc nhất không có cực trị."),
            ("Số điểm cực trị của hàm số $y = x^4 - 2x^2 + 1$ là:", 3, "$y' = 4x(x^2 - 1) = 0$ có 3 nghiệm phân biệt."),
            ("Hàm số $y = x^2 - 4x + 3$ có bao nhiêu điểm cực trị?", 1, "Parabol có đúng 1 điểm cực trị."),
            ("Cho hàm số $y = x^3 + 3x$. Số điểm cực trị của hàm số bằng:", 0, "$y' = 3x^2 + 3 > 0$ nên không có cực trị.")
        ]),
        ("Giá trị tiệm cận đứng", "b3", [
            ("Đồ thị hàm số $y = \\frac{2x + 1}{x - 3}$ có tiệm cận đứng $x = a$. Giá trị của a bằng:", 3, "Nghiệm của mẫu số là $x = 3$."),
            ("Tiệm cận đứng của đồ thị $y = \\frac{x - 2}{x + 4}$ là $x = a$. Tìm a:", -4, "$x + 4 = 0 \\Rightarrow x = -4$."),
            ("Cho đồ thị $y = \\frac{1}{x - 5}$. Giá trị tiệm cận đứng $x = a$ là:", 5, "Mẫu số triệt tiêu tại $x = 5$."),
            ("Tiệm cận đứng của $y = \\frac{3x}{x - 1}$ là $x = a$. Giá trị của a là:", 1, "Tiệm cận đứng $x = 1$."),
            ("Đồ thị $y = \\frac{x + 2}{x + 1}$ có tiệm cận đứng là $x = a$. Tìm a:", -1, "Tiệm cận đứng $x = -1$.")
        ]),
        ("Giá trị tiệm cận ngang", "b3", [
            ("Đồ thị hàm số $y = \\frac{3x - 1}{x + 2}$ có tiệm cận ngang $y = b$. Giá trị của b là:", 3, "$b = 3/1 = 3$."),
            ("Tiệm cận ngang của $y = \\frac{2x + 5}{x - 1}$ là $y = b$. Giá trị của b bằng:", 2, "$b = 2/1 = 2$."),
            ("Cho hàm số $y = \\frac{4x - 2}{2x + 3}$. Tiệm cận ngang là $y = b$. Tìm b:", 2, "$b = 4/2 = 2$."),
            ("Đồ thị $y = \\frac{5x + 1}{x - 2}$ có tiệm cận ngang $y = b$. Giá trị b là:", 5, "$b = 5$."),
            ("Tiệm cận ngang của $y = \\frac{6x - 1}{3x + 2}$ là $y = b$. Tìm b:", 2, "$b = 6/3 = 2$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("GTLN của hàm số trên đoạn", "b2", [
            ("Tìm giá trị lớn nhất của hàm số $y = -x^2 + 4x + 1$ trên đoạn $[0; 3]$:", 5, "Parabol có đỉnh tại $x = 2$: $y(2) = -4 + 8 + 1 = 5$."),
            ("Giá trị lớn nhất của hàm số $y = x^3 - 3x + 2$ trên đoạn $[0; 2]$ bằng:", 4, "$y(0) = 2, y(1) = 0, y(2) = 4$. GTLN bằng 4."),
            ("Tìm GTLN của hàm số $y = -x^3 + 3x$ trên đoạn $[0; 2]$:", 2, "$y(0) = 0, y(1) = 2, y(2) = -2$. GTLN bằng 2."),
            ("Giá trị lớn nhất của hàm số $y = 4 - x^2$ trên đoạn $[-1; 1]$ là:", 4, "Lớn nhất tại $x = 0$ bằng 4.")
        ]),
        ("GTNN của hàm số trên đoạn", "b2", [
            ("Tìm giá trị nhỏ nhất của hàm số $y = x^2 - 4x + 5$ trên đoạn $[0; 3]$:", 1, "Đỉnh tại $x = 2$: $y(2) = 4 - 8 + 5 = 1$."),
            ("Giá trị nhỏ nhất của hàm số $y = x^3 - 3x + 4$ trên đoạn $[0; 2]$ bằng:", 2, "$y(0) = 4, y(1) = 2, y(2) = 6$. GTNN bằng 2."),
            ("Tìm GTNN của hàm số $y = x + \\frac{4}{x}$ trên đoạn $[1; 3]$:", 4, "Tại $x = 2: y = 2 + 2 = 4$."),
            ("Giá trị nhỏ nhất của hàm số $y = x^2 - 2x + 3$ trên đoạn $[0; 2]$ là:", 2, "Đỉnh $x = 1: y(1) = 2$.")
        ]),
        ("Toạ độ giao điểm của hai tiệm cận", "b3", [
            ("Đồ thị hàm số $y = \\frac{2x - 1}{x - 3}$ có hai tiệm cận cắt nhau tại điểm $I(x_0; y_0)$. Tổng $x_0 + y_0$ bằng:", 5, "$x_0 = 3, y_0 = 2 \\Rightarrow x_0 + y_0 = 5$."),
            ("Cho hàm số $y = \\frac{3x + 1}{x - 2}$. Giao điểm tiệm cận $I(x_0; y_0)$ có tổng toạ độ $x_0 + y_0$ là:", 5, "$x_0 = 2, y_0 = 3 \\Rightarrow x_0 + y_0 = 5$."),
            ("Đồ thị $y = \\frac{4x - 5}{x - 1}$ có giao điểm tiệm cận $I(x_0; y_0)$. Tính $x_0 + y_0$:", 5, "$x_0 = 1, y_0 = 4 \\Rightarrow x_0 + y_0 = 5$."),
            ("Đồ thị $y = \\frac{5x + 2}{x - 3}$ có giao điểm hai tiệm cận $I(a; b)$. Giá trị của $a + b$ là:", 8, "$a = 3, b = 5 \\Rightarrow a + b = 8$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Số sản phẩm tối ưu chi phí", "b5", [
            ("Hàm chi phí sản xuất x sản phẩm là $C(x) = x^2 + 20x + 2500$. Để chi phí trung bình $\\bar{C}(x)$ nhỏ nhất thì số sản phẩm x bằng:", 50, "$\\bar{C}(x) = x + 20 + 2500/x$. Đạt nhỏ nhất khi $x = \\sqrt{2500} = 50$."),
            ("Hàm chi phí $C(x) = x^2 + 10x + 3600$. Chi phí trung bình nhỏ nhất khi x bằng:", 60, "$x = \\sqrt{3600} = 60$."),
            ("Hàm chi phí $C(x) = x^2 + 30x + 1600$. Chi phí trên một đơn vị sản phẩm nhỏ nhất tại x bằng:", 40, "$x = \\sqrt{1600} = 40$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b1", "sgk_title": "Bài 1. Tính đơn điệu và cực trị của hàm số"},
        {"lesson_id": "b2", "sgk_title": "Bài 2. Giá trị lớn nhất và giá trị nhỏ nhất của hàm số"},
        {"lesson_id": "b3", "sgk_title": "Bài 3. Đường tiệm cận của đồ thị hàm số"},
        {"lesson_id": "b4", "sgk_title": "Bài 4. Khảo sát sự biến thiên và vẽ đồ thị hàm số"},
        {"lesson_id": "b5", "sgk_title": "Bài 5. Ứng dụng đạo hàm để giải quyết một số vấn đề thực tiễn"}
    ]
    save_bank("c1", "Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số", lessons, mc, sa)

if __name__ == "__main__":
    gen_c1()
