# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

# ==============================================================================
# CHƯƠNG 2: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN
# ==============================================================================
def gen_c2():
    mc, sa = [], []

    nb_configs = [
        ("Khái niệm phương trình tích", "b4", [
            lambda: ("Phương trình nào sau đây có dạng phương trình tích?", ["$(x - 1)(2x + 3) = 0$", "$x^2 + 3x + 2 = 0$", "$\\frac{x - 1}{x + 2} = 0$", "$2x - 1 = 0$"], 0, "Phương trình tích có dạng $A(x) \\cdot B(x) = 0$."),
            lambda: ("Trong các phương trình sau, đâu là phương trình tích?", ["$(2x - 4)(x + 5) = 0$", "$2x^2 - 4x = 5$", "$\\frac{1}{x} + x = 0$", "$x(x + 1) = 2$"], 0, "Dạng $A(x) \\cdot B(x) = 0$ với vế phải bằng 0."),
            lambda: ("Chỉ ra phương trình tích trong các phương trình dưới đây:", ["$(3x + 1)(x - 2) = 0$", "$3x^2 - 5 = 0$", "$\\frac{3x + 1}{x - 2} = 0$", "$3x + 1 = x - 2$"], 0, "Phương trình tích có dạng tích các nhân tử bằng 0."),
            lambda: ("Phương trình nào sau đây là phương trình tích đối với ẩn x?", ["$(x + 3)(4 - x) = 0$", "$x^2 - 9 = 4$", "$x + 3 = 4 - x$", "$\\frac{x + 3}{4 - x} = 1$"], 0, "Dạng $(x + 3)(4 - x) = 0$ là phương trình tích."),
            lambda: ("Dạng phương trình $A(x) \\cdot B(x) = 0$ được gọi là:", ["Phương trình tích", "Phương trình bậc nhất", "Phương trình chứa ẩn ở mẫu", "Phương trình vô nghiệm"], 0, "Đây là định nghĩa phương trình tích.")
        ]),
        ("Nghiệm phương trình tích đơn giản", "b4", [
            lambda: ("Nghiệm của phương trình $(x - 2)(x + 3) = 0$ là:", ["$x = 2$ hoặc $x = -3$", "$x = -2$ hoặc $x = 3$", "$x = 2$ hoặc $x = 3$", "$x = -2$ hoặc $x = -3$"], 0, "$x - 2 = 0 \\Rightarrow x = 2$ hoặc $x + 3 = 0 \\Rightarrow x = -3$."),
            lambda: ("Phương trình $(x - 5)(x - 1) = 0$ có tập nghiệm là:", ["$\\{1; 5\\}$", "$\\{-1; -5\\}$", "$\\{1; -5\\}$", "$\\{-1; 5\\}$"], 0, "Nghiệm là $x = 1$ và $x = 5$."),
            lambda: ("Tập nghiệm của phương trình $(2x - 4)(x + 1) = 0$ là:", ["$\\{2; -1\\}$", "$\\{-2; 1\\}$", "$\\{4; -1\\}$", "$\\{2; 1\\}$"], 0, "$2x - 4 = 0 \\Rightarrow x = 2$ hoặc $x + 1 = 0 \\Rightarrow x = -1$."),
            lambda: ("Giải phương trình tích $(x + 4)(x - 6) = 0$ thu được nghiệm:", ["$x = -4$ hoặc $x = 6$", "$x = 4$ hoặc $x = -6$", "$x = 4$ hoặc $x = 6$", "$x = -4$ hoặc $x = -6$"], 0, "Nghiệm là $x = -4$ và $x = 6$."),
            lambda: ("Các nghiệm của phương trình $x(x - 7) = 0$ là:", ["$x = 0$ hoặc $x = 7$", "$x = 7$", "$x = 0$ hoặc $x = -7$", "$x = -7$"], 0, "$x = 0$ hoặc $x - 7 = 0 \\Rightarrow x = 7$.")
        ]),
        ("Điều kiện xác định của phương trình chứa ẩn ở mẫu", "b4", [
            lambda: ("Điều kiện xác định của phương trình $\\frac{1}{x - 3} = 2$ là:", ["$x \\ne 3$", "$x \\ne -3$", "$x > 3$", "$x \\ge 3$"], 0, "Mẫu thức phải khác 0: $x - 3 \\ne 0 \\Leftrightarrow x \\ne 3$."),
            lambda: ("Tìm ĐKXĐ của phương trình $\\frac{2x + 1}{x + 4} = 0$:", ["$x \\ne -4$", "$x \\ne 4$", "$x \\ne -1/2$", "$x > -4$"], 0, "Mẫu thức khác 0: $x + 4 \\ne 0 \\Leftrightarrow x \\ne -4$."),
            lambda: ("Phương trình $\\frac{x}{x - 5} = 1$ xác định khi và chỉ khi:", ["$x \\ne 5$", "$x \\ne -5$", "$x \\ne 0$", "$x > 5$"], 0, "Mẫu $x - 5 \\ne 0 \\Leftrightarrow x \\ne 5$."),
            lambda: ("Điều kiện để phương trình $\\frac{3}{2x - 6} = 1$ có nghĩa là:", ["$x \\ne 3$", "$x \\ne -3$", "$x \\ne 6$", "$x > 3$"], 0, "$2x - 6 \\ne 0 \\Leftrightarrow x \\ne 3$."),
            lambda: ("ĐKXĐ của phương trình phân thức $\\frac{x - 1}{x + 2} = \\frac{3}{x - 2}$ là:", ["$x \\ne 2$ và $x \\ne -2$", "$x \\ne 2$", "$x \\ne -2$", "$x \\ne 1$"], 0, "Các mẫu phải khác 0: $x \\ne 2$ và $x \\ne -2$.")
        ]),
        ("Quy đồng và khử mẫu phương trình phân thức", "b4", [
            lambda: ("Mẫu thức chung của hai phân thức $\\frac{1}{x - 1}$ và $\\frac{1}{x + 1}$ là:", ["$(x - 1)(x + 1)$", "$x - 1$", "$x + 1$", "$x^2 + 1$"], 0, "MTC là tích $(x - 1)(x + 1) = x^2 - 1$."),
            lambda: ("Khi quy đồng mẫu số của $\\frac{x}{x - 2} = 3$, phương trình sau khi khử mẫu là:", ["$x = 3(x - 2)$", "$x = 3$", "$x = x - 2$", "$x = 3x - 2$"], 0, "Khử mẫu: $x = 3(x - 2)$."),
            lambda: ("Khử mẫu phương trình $\\frac{x + 1}{2} = \\frac{x - 1}{3}$ ta được:", ["$3(x + 1) = 2(x - 1)$", "$2(x + 1) = 3(x - 1)$", "$x + 1 = x - 1$", "$6(x + 1) = x - 1$"], 0, "Quy đồng MTC là 6: $3(x + 1) = 2(x - 1)$."),
            lambda: ("Phương trình nào là kết quả khử mẫu của $\\frac{2}{x} = 1$ (với $x \\ne 0$)?", ["$x = 2$", "$2x = 1$", "$x = 1$", "$x = 1/2$"], 0, "Nhân hai vế với x: $2 = x \\Leftrightarrow x = 2$."),
            lambda: ("Sau khi khử mẫu của $\\frac{x - 3}{x - 1} = 0$ với ĐKXĐ $x \\ne 1$, ta được phương trình:", ["$x - 3 = 0$", "$x - 1 = 0$", "$x - 3 = x - 1$", "$x = 1$"], 0, "Tử số bằng 0: $x - 3 = 0$.")
        ]),
        ("Khái niệm bất đẳng thức cơ bản", "b5", [
            lambda: ("Khẳng định nào sau đây là một bất đẳng thức đúng?", ["$5 > 3$", "$3 > 5$", "$2 < -1$", "$-4 > 0$"], 0, "Hiệu $5 - 3 = 2 > 0$ nên $5 > 3$ là đúng."),
            lambda: ("Trong các khẳng định sau, bất đẳng thức nào sai?", ["$-3 > -2$", "$-2 < 0$", "$4 > 1$", "$-5 < -1$"], 0, "Vì -3 nhỏ hơn -2 nên $-3 > -2$ là sai."),
            lambda: ("Hệ thức nào sau đây biểu diễn bất đẳng thức không nghiêm ngặt?", ["$a \\le b$", "$a < b$", "$a > b$", "$a = b$"], 0, "BĐT có dấu $\\le$ hoặc $\\ge$ là BĐT không nghiêm ngặt."),
            lambda: ("Với mọi số thực a, khẳng định nào sau đây luôn đúng?", ["$a^2 \\ge 0$", "$a^2 > 0$", "$a > 0$", "$a < 0$"], 0, "Bình phương của một số thực luôn không âm: $a^2 \\ge 0$."),
            lambda: ("Cho bất đẳng thức $m < n$. Vế trái của bất đẳng thức là:", ["$m$", "$n$", "$m - n$", "$m + n$"], 0, "Vế trái là m, vế phải là n.")
        ]),
        ("Tính chất cộng của bất đẳng thức", "b5", [
            lambda: ("Cho $a < b$. Khi cộng hai vế với số 4 ta được bất đẳng thức:", ["$a + 4 < b + 4$", "$a + 4 > b + 4$", "$a + 4 = b + 4$", "$a - 4 > b - 4$"], 0, "Cộng cùng một số thì BĐT không đổi chiều."),
            lambda: ("Nếu $x > y$ thì khẳng định nào sau đây đúng?", ["$x - 2 > y - 2$", "$x - 2 < y - 2$", "$x + 2 < y + 2$", "$x - 2 = y - 2$"], 0, "Trừ cùng một số thì BĐT giữ nguyên chiều."),
            lambda: ("Cho $m \\le n$. Khi cộng cả hai vế với -5 ta được:", ["$m - 5 \\le n - 5$", "$m - 5 \\ge n - 5$", "$m + 5 \\le n - 5$", "$m - 5 > n - 5$"], 0, "Bất đẳng thức giữ nguyên chiều: $m - 5 \\le n - 5$."),
            lambda: ("Từ $a + 3 < b + 3$, áp dụng tính chất cộng suy ra:", ["$a < b$", "$a > b$", "$a = b$", "$a \\ge b$"], 0, "Trừ cả hai vế cho 3: $a < b$."),
            lambda: ("Cộng số -1 vào hai vế của bất đẳng thức $2 < 5$ ta được:", ["$1 < 4$", "$1 > 4$", "$3 < 6$", "$1 = 4$"], 0, "$2 + (-1) < 5 + (-1) \\Leftrightarrow 1 < 4$.")
        ]),
        ("Tính chất nhân bất đẳng thức với số dương", "b5", [
            lambda: ("Cho $a < b$. Khi nhân hai vế với số dương 3 ta được:", ["$3a < 3b$", "$3a > 3b$", "$3a = 3b$", "$-3a < -3b$"], 0, "Nhân với số dương thì BĐT không đổi chiều."),
            lambda: ("Nếu $x > y$ và $c > 0$ thì khẳng định nào sau đây đúng?", ["$cx > cy$", "$cx < cy$", "$cx = cy$", "$cx \\le cy$"], 0, "Nhân hai vế với số dương c giữ nguyên chiều BĐT."),
            lambda: ("Cho $m \\ge n$. Nhân cả hai vế với 5 ta được:", ["$5m \\ge 5n$", "$5m \\le 5n$", "$5m > 5n$", "$m \\ge 5n$"], 0, "Nhân với 5 > 0 thì chiều BĐT giữ nguyên."),
            lambda: ("Từ bất đẳng thức $2x < 4$, chia cả hai vế cho số dương 2 ta được:", ["$x < 2$", "$x > 2$", "$x = 2$", "$x \\le 2$"], 0, "Chia cho số dương giữ nguyên chiều: $x < 2$."),
            lambda: ("Nhân số $\\frac{1}{2}$ vào hai vế của $a > b$ ta được kết quả:", ["$\\frac{1}{2}a > \\frac{1}{2}b$", "$\\frac{1}{2}a < \\frac{1}{2}b$", "$a > 2b$", "$2a > b$"], 0, "Chiều BĐT giữ nguyên vì $1/2 > 0$.")
        ]),
        ("Tính chất nhân bất đẳng thức với số âm", "b5", [
            lambda: ("Cho $a < b$. Khi nhân hai vế với số âm -2 ta được:", ["$-2a > -2b$", "$-2a < -2b$", "$-2a = -2b$", "$2a > 2b$"], 0, "Nhân với số âm thì BĐT phải đổi chiều."),
            lambda: ("Nếu $x > y$ và nhân cả hai vế với -1 ta được bất đẳng thức:", ["$-x < -y$", "$-x > -y$", "$-x = -y$", "$x < -y$"], 0, "Nhân với -1 đổi chiều BĐT: $-x < -y$."),
            lambda: ("Cho $m \\le n$. Khi chia cả hai vế cho số âm -3 ta được:", ["$-\\frac{m}{3} \\ge -\\frac{n}{3}$", "$-\\frac{m}{3} \\le -\\frac{n}{3}$", "$\\frac{m}{3} \\ge \\frac{n}{3}$", "$-\\frac{m}{3} > -\\frac{n}{3}$"], 0, "Chia cho số âm đổi chiều BĐT: $-\\frac{m}{3} \\ge -\\frac{n}{3}$."),
            lambda: ("Từ bất đẳng thức $-3x < 9$, chia cả hai vế cho -3 ta được:", ["$x > -3$", "$x < -3$", "$x > 3$", "$x < 3$"], 0, "Chia cho -3 và đổi chiều: $x > -3$."),
            lambda: ("Nhân cả hai vế của $a \\ge b$ với số âm -4 thu được:", ["$-4a \\le -4b$", "$-4a \\ge -4b$", "$-4a < -4b$", "$4a \\le 4b$"], 0, "Đổi chiều BĐT từ $\\ge$ sang $\\le$.")
        ]),
        ("Khái niệm bất phương trình bậc nhất một ẩn", "b6", [
            lambda: ("Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn x?", ["$2x - 3 > 0$", "$x^2 + 1 > 0$", "$\\frac{1}{x} - 2 < 0$", "$0x + 5 > 0$"], 0, "BPT bậc nhất một ẩn có dạng $ax + b > 0$ với $a \\ne 0$."),
            lambda: ("Trong các bất phương trình sau, đâu là bất phương trình bậc nhất một ẩn?", ["$3 - 4x \\le 0$", "$x^2 - 4 \\ge 0$", "$2x + y > 1$", "$\\sqrt{x} < 2$"], 0, "$3 - 4x \\le 0$ là BPT bậc nhất một ẩn x."),
            lambda: ("Chỉ ra bất phương trình bậc nhất một ẩn y trong các câu sau:", ["$5y + 2 < 0$", "$y^3 + 1 > 0$", "$\\frac{2}{y} \\ge 3$", "$y^2 - 2y < 0$"], 0, "BPT bậc nhất ẩn y có dạng $ay + b < 0$ ($a \\ne 0$)."),
            lambda: ("Bất phương trình nào sau đây không phải là bất phương trình bậc nhất một ẩn?", ["$x^2 - 1 > 0$", "$2x - 5 > 0$", "$-x + 3 \\le 0$", "$4x \\ge 8$"], 0, "$x^2 - 1 > 0$ có bậc 2 nên không phải bậc nhất."),
            lambda: ("Hệ số a và b của bất phương trình bậc nhất $-2x + 7 \\ge 0$ là:", ["$a = -2, b = 7$", "$a = 2, b = 7$", "$a = -2, b = -7$", "$a = 7, b = -2$"], 0, "Hệ số trước x là a = -2, hệ số tự do là b = 7.")
        ]),
        ("Nhận biết nghiệm của bất phương trình bậc nhất", "b6", [
            lambda: ("Số nào sau đây là một nghiệm của bất phương trình $x - 2 > 3$?", ["$6$", "$5$", "$4$", "$3$"], 0, "$x > 5$. Số 6 > 5 nên là nghiệm."),
            lambda: ("Giá trị nào của x thoả mãn bất phương trình $2x + 1 \\le 5$?", ["$2$", "$3$", "$4$", "$5$"], 0, "$2x \\le 4 \\Leftrightarrow x \\le 2$. Giá trị x = 2 thoả mãn."),
            lambda: ("Trong các số sau, số nào không phải là nghiệm của $x + 4 < 7$?", ["$4$", "$2$", "$1$", "$0$"], 0, "$x < 3$. Số 4 không thoả mãn $4 < 3$."),
            lambda: ("Kiểm tra xem số nào là nghiệm của bất phương trình $3x \\ge 12$:", ["$4$", "$3$", "$2$", "$1$"], 0, "$x \\ge 4$. Số 4 thoả mãn dấu bằng."),
            lambda: ("Số 0 là nghiệm của bất phương trình nào sau đây?", ["$2x + 3 > 0$", "$2x - 3 > 0$", "$x - 1 \\ge 0$", "$3x + 1 < 0$"], 0, "Thay x = 0: $2(0) + 3 = 3 > 0$ (đúng).")
        ]),
        ("Quy tắc chuyển vế trong bất phương trình", "b6", [
            lambda: ("Khi chuyển vế hạng tử trong bất phương trình, ta phải làm gì?", ["Đổi dấu hạng tử đó", "Giữ nguyên dấu hạng tử", "Đổi chiều bất phương trình", "Nhân với -1"], 0, "Quy tắc chuyển vế: Chuyển một hạng tử từ vế này sang vế kia thì phải đổi dấu hạng tử đó."),
            lambda: ("Chuyển vế số -3 trong bất phương trình $x - 3 > 5$ ta được:", ["$x > 5 + 3$", "$x > 5 - 3$", "$x < 5 + 3$", "$x < 5 - 3$"], 0, "Chuyển -3 sang vế phải đổi thành +3: $x > 5 + 3$."),
            lambda: ("Chuyển hạng tử 2x trong bất phương trình $5x < 2x + 6$ sang vế trái ta được:", ["$5x - 2x < 6$", "$5x + 2x < 6$", "$5x - 2x > 6$", "$3x > 6$"], 0, "Chuyển 2x sang vế trái thành -2x: $5x - 2x < 6$."),
            lambda: ("Áp dụng quy tắc chuyển vế cho $x + 7 \\le 10$ ta được:", ["$x \\le 10 - 7$", "$x \\le 10 + 7$", "$x \\ge 10 - 7$", "$x > 3$"], 0, "Chuyển +7 thành -7: $x \\le 10 - 7$."),
            lambda: ("Biến đổi nào sau đây đúng khi chuyển vế $4 - x > 2$:", ["$-x > 2 - 4$", "$-x > 2 + 4$", "$x > 2 - 4$", "$x > 4 - 2$"], 0, "Chuyển 4 sang vế phải thành -4: $-x > 2 - 4$.")
        ]),
        ("Biểu diễn tập nghiệm trên trục số", "b6", [
            lambda: ("Hình vẽ biểu diễn các điểm từ 3 về bên phải kể cả điểm 3 là tập nghiệm của:", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x < 3$"], 0, "Từ 3 về bên phải và lấy cả điểm 3 là $x \\ge 3$."),
            lambda: ("Tập nghiệm $x < 2$ được biểu diễn trên trục số là:", ["Các điểm bên trái điểm 2 và không lấy điểm 2", "Các điểm bên phải điểm 2", "Các điểm bên trái điểm 2 kể cả điểm 2", "Chỉ điểm 2"], 0, "Nghiệm $x < 2$ là phần trục số bên trái điểm 2 (dùng ngoặc tròn)."),
            lambda: ("Kí hiệu ngoặc vuông $[$ trên trục số tại điểm a hướng về bên phải biểu diễn tập nghiệm:", ["$x \\ge a$", "$x > a$", "$x \\le a$", "$x < a$"], 0, "Ngoặc vuông biểu thị lấy cả điểm mút: $x \\ge a$."),
            lambda: ("Tập nghiệm của bất phương trình $x > -1$ trên trục số bao gồm:", ["Các điểm bên phải điểm -1 và bỏ điểm -1", "Các điểm bên trái điểm -1", "Điểm -1", "Toàn bộ trục số"], 0, "Các điểm lớn hơn -1 nằm bên phải điểm -1."),
            lambda: ("Biểu diễn tập nghiệm $x \\le 0$ trên trục số là phần:", ["Bên trái gốc toạ độ O kể cả điểm O", "Bên phải gốc toạ độ O", "Toàn bộ trục số trừ điểm O", "Không có điểm nào"], 0, "Tập nghiệm $x \\le 0$ gồm các số không dương nằm bên trái và gồm cả điểm O.")
        ])
    ]
    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c2-{len(mc)+1:03d}", "chapter": "c2", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    th_configs = [
        ("Giải phương trình tích bậc hai", "b4", [
            lambda: ("Tổng các nghiệm của phương trình $(2x - 6)(x + 2) = 0$ là:", ["$1$", "$5$", "$-1$", "$3$"], 0, "Nghiệm là $x = 3$ và $x = -2$. Tổng hai nghiệm là $3 + (-2) = 1$."),
            lambda: ("Phương trình $(x - 4)(2x + 8) = 0$ có tích các nghiệm là:", ["$-16$", "$16$", "$0$", "$-8$"], 0, "Nghiệm là $x = 4$ và $x = -4$. Tích hai nghiệm là $4 \\cdot (-4) = -16$."),
            lambda: ("Giải phương trình $(3x - 9)(x + 1) = 0$. Nghiệm lớn hơn là:", ["$3$", "$-1$", "$9$", "$1$"], 0, "Hai nghiệm là 3 và -1. Nghiệm lớn hơn là 3."),
            lambda: ("Số nghiệm phân biệt của phương trình $(x^2 - 4)(x - 2) = 0$ là:", ["$2$", "$3$", "$1$", "$0$"], 0, "$(x - 2)(x + 2)(x - 2) = 0 \\Leftrightarrow x = 2$ hoặc $x = -2$. Có đúng 2 nghiệm phân biệt.")
        ]),
        ("Giải phương trình chứa ẩn ở mẫu đơn giản", "b4", [
            lambda: ("Nghiệm của phương trình $\\frac{x + 4}{x - 1} = 2$ là:", ["$x = 6$", "$x = 5$", "$x = 4$", "$x = 3$"], 0, "ĐKXĐ: $x \\ne 1$. Quy đồng: $x + 4 = 2(x - 1) \\Leftrightarrow x + 4 = 2x - 2 \\Leftrightarrow x = 6$."),
            lambda: ("Giải phương trình $\\frac{2x - 1}{x + 2} = 1$ ta được nghiệm:", ["$x = 3$", "$x = 2$", "$x = 1$", "$x = -3$"], 0, "ĐKXĐ: $x \\ne -2$. Quy đồng: $2x - 1 = x + 2 \\Leftrightarrow x = 3$."),
            lambda: ("Nghiệm của phương trình $\\frac{3x}{x - 2} = 4$ là:", ["$x = 8$", "$x = 6$", "$x = 4$", "$x = 2$"], 0, "ĐKXĐ: $x \\ne 2$. Quy đồng: $3x = 4(x - 2) \\Leftrightarrow 3x = 4x - 8 \\Leftrightarrow x = 8$."),
            lambda: ("Phương trình $\\frac{x - 2}{x + 1} = 0$ có nghiệm là:", ["$x = 2$", "$x = -1$", "$x = 0$", "Vô nghiệm"], 0, "ĐKXĐ: $x \\ne -1$. Tử bằng 0: $x - 2 = 0 \\Leftrightarrow x = 2$ (thoả mãn).")
        ]),
        ("Phương trình phân thức có nghiệm ngoại lai", "b4", [
            lambda: ("Số nghiệm của phương trình $\\frac{x^2 - 9}{x - 3} = 0$ là:", ["$1$", "$2$", "$0$", "Vô số"], 0, "ĐKXĐ: $x \\ne 3$. Tử bằng 0: $x^2 = 9 \\Leftrightarrow x = \\pm 3$. Nghiệm $x = 3$ bị loại do ĐKXĐ, chỉ còn $x = -3$. Vậy có 1 nghiệm."),
            lambda: ("Phương trình $\\frac{x - 2}{x - 2} = 0$ có tập nghiệm là:", ["Rỗng (vô nghiệm)", "$\\{2\\}$", "$\\mathbb{R}$", "$\\mathbb{R} \\setminus \\{2\\}$"], 0, "ĐKXĐ: $x \\ne 2$. Khi đó $\\frac{x-2}{x-2} = 1 \\ne 0$. Phương trình vô nghiệm."),
            lambda: ("Số nghiệm thực của phương trình $\\frac{x^2 - 4}{x + 2} = 0$ là:", ["$1$", "$2$", "$0$", "$3$"], 0, "ĐKXĐ: $x \\ne -2$. Tử bằng 0: $x = \\pm 2$. Nghiệm $x = -2$ bị loại, chỉ còn $x = 2$. Có 1 nghiệm."),
            lambda: ("Giải phương trình $\\frac{x(x - 1)}{x - 1} = 0$. Nghiệm của phương trình là:", ["$x = 0$", "$x = 1$", "$x = 0$ hoặc $x = 1$", "Vô nghiệm"], 0, "ĐKXĐ: $x \\ne 1$. Rút gọn: $x = 0$ (thoả mãn).")
        ]),
        ("So sánh hai biểu thức áp dụng tính chất cộng BĐT", "b5", [
            lambda: ("Cho $a < b$. So sánh hai biểu thức $2a + 5$ và $2b + 5$:", ["$2a + 5 < 2b + 5$", "$2a + 5 > 2b + 5$", "$2a + 5 = 2b + 5$", "Không so sánh được"], 0, "Vì 2 > 0 nên $2a < 2b$. Cộng 5 vào hai vế: $2a + 5 < 2b + 5$."),
            lambda: ("Cho $x > y$. So sánh $3x - 1$ và $3y - 1$:", ["$3x - 1 > 3y - 1$", "$3x - 1 < 3y - 1$", "$3x - 1 = 3y - 1$", "Không xác định"], 0, "Nhân 3 > 0 rồi trừ 1: $3x - 1 > 3y - 1$."),
            lambda: ("Cho $m \\le n$. Khẳng định nào sau đây đúng?", ["$m - 4 \\le n - 4$", "$m - 4 \\ge n - 4$", "$m + 4 > n + 4$", "$4 - m \\le 4 - n$"], 0, "Trừ 4 vào hai vế giữ nguyên chiều BĐT: $m - 4 \\le n - 4$."),
            lambda: ("Biết $a + 2 < b + 2$, kết luận nào sau đây đúng?", ["$a - 5 < b - 5$", "$a - 5 > b - 5$", "$a + 5 > b + 5$", "$a = b$"], 0, "Từ $a + 2 < b + 2 \\Rightarrow a < b \\Rightarrow a - 5 < b - 5$.")
        ]),
        ("So sánh hai biểu thức áp dụng tính chất nhân BĐT", "b5", [
            lambda: ("Cho $a < b$. So sánh $-3a$ và $-3b$:", ["$-3a > -3b$", "$-3a < -3b$", "$-3a = -3b$", "$3a < -3b$"], 0, "Nhân với số âm -3 đổi chiều BĐT: $-3a > -3b$."),
            lambda: ("Cho $x > y$. So sánh $-2x + 1$ và $-2y + 1$:", ["$-2x + 1 < -2y + 1$", "$-2x + 1 > -2y + 1$", "$-2x + 1 = -2y + 1$", "Không so sánh được"], 0, "Nhân -2 đổi chiều: $-2x < -2y$. Cộng 1: $-2x + 1 < -2y + 1$."),
            lambda: ("Cho $m < n$. Khẳng định nào sau đây đúng?", ["$5 - m > 5 - n$", "$5 - m < 5 - n$", "$5 - m = 5 - n$", "$-m < -n$"], 0, "Nhân -1: $-m > -n$. Cộng 5: $5 - m > 5 - n$."),
            lambda: ("Nếu $-4a > -4b$ thì kết luận đúng về a và b là:", ["$a < b$", "$a > b$", "$a = b$", "$a \\le b$"], 0, "Chia cả hai vế cho số âm -4 và đổi chiều: $a < b$.")
        ]),
        ("Giải bất phương trình bậc nhất cơ bản", "b6", [
            lambda: ("Nghiệm của bất phương trình $2x - 6 > 0$ là:", ["$x > 3$", "$x < 3$", "$x > -3$", "$x < -3$"], 0, "$2x > 6 \\Leftrightarrow x > 3$."),
            lambda: ("Tập nghiệm của bất phương trình $3x + 9 \\le 0$ là:", ["$x \\le -3$", "$x \\ge -3$", "$x \\le 3$", "$x < -3$"], 0, "$3x \\le -9 \\Leftrightarrow x \\le -3$."),
            lambda: ("Giải bất phương trình $4x - 8 \\ge 0$ ta được:", ["$x \\ge 2$", "$x \\le 2$", "$x > 2$", "$x \\ge -2$"], 0, "$4x \\ge 8 \\Leftrightarrow x \\ge 2$."),
            lambda: ("Nghiệm của bất phương trình $5x - 15 < 0$ là:", ["$x < 3$", "$x > 3$", "$x < -3$", "$x \\le 3$"], 0, "$5x < 15 \\Leftrightarrow x < 3$.")
        ]),
        ("Giải bất phương trình đổi chiều khi chia số âm", "b6", [
            lambda: ("Nghiệm của bất phương trình $-2x < 6$ là:", ["$x > -3$", "$x < -3$", "$x > 3$", "$x < 3$"], 0, "Chia cho -2 và đổi chiều: $x > 6 / (-2) = -3$."),
            lambda: ("Giải bất phương trình $-3x \\ge -12$ ta được:", ["$x \\le 4$", "$x \\ge 4$", "$x \\le -4$", "$x > 4$"], 0, "Chia cho -3 đổi chiều: $x \\le (-12)/(-3) = 4$."),
            lambda: ("Tập nghiệm của bất phương trình $4 - 2x > 0$ là:", ["$x < 2$", "$x > 2$", "$x < -2$", "$x > -2$"], 0, "$-2x > -4 \\Leftrightarrow x < 2$."),
            lambda: ("Nghiệm của bất phương trình $-5x + 10 \\le 0$ là:", ["$x \\ge 2$", "$x \\le 2$", "$x \\ge -2$", "$x < 2$"], 0, "$-5x \\le -10 \\Leftrightarrow x \\ge 2$.")
        ]),
        ("Giải bất phương trình chứa phân số", "b6", [
            lambda: ("Nghiệm của bất phương trình $\\frac{x - 1}{2} \\ge 3$ là:", ["$x \\ge 7$", "$x \\le 7$", "$x \\ge 6$", "$x \\ge 5$"], 0, "Nhân 2: $x - 1 \\ge 6 \\Leftrightarrow x \\ge 7$."),
            lambda: ("Giải bất phương trình $\\frac{2x + 1}{3} < 3$ ta được:", ["$x < 4$", "$x > 4$", "$x < 5$", "$x < 3$"], 0, "$2x + 1 < 9 \\Leftrightarrow 2x < 8 \\Leftrightarrow x < 4$."),
            lambda: ("Tập nghiệm của bất phương trình $\\frac{x}{4} - 1 \\le 1$ là:", ["$x \\le 8$", "$x \\ge 8$", "$x \\le 4$", "$x \\le 2$"], 0, "$x/4 \\le 2 \\Leftrightarrow x \\le 8$."),
            lambda: ("Nghiệm của bất phương trình $\\frac{3 - x}{2} > 1$ là:", ["$x < 1$", "$x > 1$", "$x < -1$", "$x > -1$"], 0, "$3 - x > 2 \\Leftrightarrow -x > -1 \\Leftrightarrow x < 1$.")
        ]),
        ("Tìm số nguyên nhỏ nhất thoả mãn bất phương trình", "b6", [
            lambda: ("Số nguyên nhỏ nhất thoả mãn bất phương trình $2x > 5$ là:", ["$3$", "$2$", "$4$", "$1$"], 0, "$x > 2,5$. Số nguyên nhỏ nhất là 3."),
            lambda: ("Tìm số nguyên nhỏ nhất thoả mãn $3x \\ge 8$:", ["$3$", "$2$", "$4$", "$5$"], 0, "$x \\ge 8/3 \\approx 2,67$. Số nguyên nhỏ nhất là 3."),
            lambda: ("Số nguyên dương nhỏ nhất thoả mãn $x - 4 > 0$ là:", ["$5$", "$4$", "$6$", "$3$"], 0, "$x > 4$. Số nguyên dương nhỏ nhất là 5."),
            lambda: ("Giá trị nguyên nhỏ nhất của x thoả mãn $4x > 11$ là:", ["$3$", "$2$", "$4$", "$1$"], 0, "$x > 11/4 = 2,75$. Số nguyên nhỏ nhất là 3.")
        ]),
        ("Giải bất phương trình có dấu ngoặc", "b6", [
            lambda: ("Nghiệm của bất phương trình $2(x - 1) - (x + 2) < 3$ là:", ["$x < 7$", "$x > 7$", "$x < 5$", "$x < 1$"], 0, "$2x - 2 - x - 2 < 3 \\Leftrightarrow x - 4 < 3 \\Leftrightarrow x < 7$."),
            lambda: ("Giải bất phương trình $3(x + 1) \\ge 2(x - 1)$ ta được:", ["$x \\ge -5$", "$x \\le -5$", "$x \\ge 5$", "$x \\le 5$"], 0, "$3x + 3 \\ge 2x - 2 \\Leftrightarrow x \\ge -5$."),
            lambda: ("Tập nghiệm của bất phương trình $4(x - 2) < 2x$ là:", ["$x < 4$", "$x > 4$", "$x < 2$", "$x < -4$"], 0, "$4x - 8 < 2x \\Leftrightarrow 2x < 8 \\Leftrightarrow x < 4$."),
            lambda: ("Nghiệm của bất phương trình $5(x - 1) \\ge 3(x + 1)$ là:", ["$x \\ge 4$", "$x \\le 4$", "$x \\ge 2$", "$x \\le 2$"], 0, "$5x - 5 \\ge 3x + 3 \\Leftrightarrow 2x \\ge 8 \\Leftrightarrow x \\ge 4$.")
        ]),
        ("Biểu diễn tập nghiệm trên trục số hình học", "b6", [
            lambda: ("Tập nghiệm của bất phương trình $-x \\le 2$ được biểu diễn là:", ["$x \\ge -2$", "$x \\le -2$", "$x \\ge 2$", "$x \\le 2$"], 0, "Nhân -1 đổi chiều: $x \\ge -2$."),
            lambda: ("Bất phương trình nào sau đây có tập nghiệm là nửa khoảng $[3; +\\infty)$?", ["$x \\ge 3$", "$x > 3$", "$x \\le 3$", "$x < 3$"], 0, "Lấy từ 3 đến vô cực gồm cả 3 là $x \\ge 3$."),
            lambda: ("Tập hợp các số thực nhỏ hơn -1 được viết dưới dạng khoảng là:", ["$(-\\infty; -1)$", "$[-1; +\\infty)$", "$(-\\infty; -1]$", "$(-1; +\\infty)$"], 0, "Khoảng $(-\\infty; -1)$ biểu diễn các số nhỏ hơn -1."),
            lambda: ("Tập nghiệm của bất phương trình $2x \\le 6$ biểu diễn trên trục số gồm:", ["Các điểm bên trái điểm 3 kể cả 3", "Các điểm bên phải điểm 3", "Chỉ điểm 3", "Không có điểm nào"], 0, "$x \\le 3$ gồm các điểm bên trái và gồm cả điểm 3.")
        ]),
        ("Bất đẳng thức Cauchy đơn giản cho hai số dương", "b5", [
            lambda: ("Với $x > 0$, giá trị nhỏ nhất của biểu thức $P = x + \\frac{4}{x}$ là:", ["$4$", "$2$", "$8$", "$1$"], 0, "Theo BĐT Cauchy: $x + 4/x \\ge 2\\sqrt{x \\cdot 4/x} = 2(2) = 4$. Đẳng thức khi $x = 2$."),
            lambda: ("Cho $a > 0$. Giá trị nhỏ nhất của $Q = a + \\frac{9}{a}$ bằng:", ["$6$", "$9$", "$3$", "$12$"], 0, "Theo BĐT Cauchy: $a + 9/a \\ge 2\\sqrt{a \\cdot 9/a} = 2(3) = 6$."),
            lambda: ("Với $y > 0$, biểu thức $M = y + \\frac{1}{y}$ đạt giá trị nhỏ nhất bằng:", ["$2$", "$1$", "$4$", "$0$"], 0, "$y + 1/y \\ge 2\\sqrt{y \\cdot 1/y} = 2$. Đẳng thức khi $y = 1$."),
            lambda: ("Cho $b > 0$. Giá trị nhỏ nhất của $b + \\frac{16}{b}$ là:", ["$8$", "$16$", "$4$", "$10$"], 0, "$b + 16/b \\ge 2\\sqrt{16} = 8$. Đẳng thức khi $b = 4$.")
        ])
    ]
    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c2-{len(mc)+1:03d}", "chapter": "c2", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    vd_configs = [
        ("Tìm số nghiệm nguyên dương của bất phương trình", "b6", [
            lambda: ("Số nghiệm nguyên dương của bất phương trình $\\frac{2x - 1}{3} < 3$ là:", ["$4$", "$3$", "$5$", "$2$"], 0, "$2x - 1 < 9 \\Leftrightarrow 2x < 10 \\Leftrightarrow x < 5$. Nghiệm nguyên dương là $x \\in \\{1; 2; 3; 4\\}$ (4 nghiệm)."),
            lambda: ("Có bao nhiêu số nguyên dương x thoả mãn bất phương trình $3x - 5 < 10$:", ["$4$", "$5$", "$3$", "$2$"], 0, "$3x < 15 \\Leftrightarrow x < 5$. Các nghiệm nguyên dương là 1, 2, 3, 4 (4 số)."),
            lambda: ("Số nghiệm nguyên dương của bất phương trình $\\frac{x + 2}{2} \\le 3$ là:", ["$4$", "$3$", "$5$", "$6$"], 0, "$x + 2 \\le 6 \\Leftrightarrow x \\le 4$. Nghiệm nguyên dương là 1, 2, 3, 4 (4 nghiệm)."),
            lambda: ("Tìm số các số nguyên dương thoả mãn $4x - 7 < 9$:", ["$3$", "$4$", "$2$", "$5$"], 0, "$4x < 16 \\Leftrightarrow x < 4$. Nghiệm nguyên dương là 1, 2, 3 (3 số).")
        ]),
        ("Giải phương trình chứa ẩn ở mẫu hai phân thức", "b4", [
            lambda: ("Nghiệm của phương trình $\\frac{1}{x - 1} + \\frac{1}{x + 1} = \\frac{4}{x^2 - 1}$ là:", ["$x = 2$", "$x = 1$", "$x = -1$", "Vô nghiệm"], 0, "ĐKXĐ: $x \\ne \\pm 1$. Quy đồng: $(x + 1) + (x - 1) = 4 \\Leftrightarrow 2x = 4 \\Leftrightarrow x = 2$ (thoả mãn)."),
            lambda: ("Giải phương trình $\\frac{2}{x - 2} - \\frac{1}{x + 2} = \\frac{7}{x^2 - 4}$ ta được:", ["$x = 1$", "$x = 2$", "$x = -2$", "$x = 3$"], 0, "ĐKXĐ: $x \\ne \\pm 2$. $2(x + 2) - (x - 2) = 7 \\Leftrightarrow 2x + 4 - x + 2 = 7 \\Leftrightarrow x + 6 = 7 \\Leftrightarrow x = 1$."),
            lambda: ("Nghiệm của phương trình $\\frac{1}{x - 3} + \\frac{1}{x + 3} = \\frac{6}{x^2 - 9}$ là:", ["Vô nghiệm", "$x = 3$", "$x = -3$", "$x = 0$"], 0, "Quy đồng: $2x = 6 \\Leftrightarrow x = 3$. Vì ĐKXĐ $x \\ne 3$ nên nghiệm bị loại, phương trình vô nghiệm."),
            lambda: ("Phương trình $\\frac{3}{x - 1} - \\frac{2}{x + 1} = \\frac{5}{x^2 - 1}$ có nghiệm là:", ["$x = 0$", "$x = 1$", "$x = -1$", "$x = 2$"], 0, "$3(x + 1) - 2(x - 1) = 5 \\Leftrightarrow 3x + 3 - 2x + 2 = 5 \\Leftrightarrow x + 5 = 5 \\Leftrightarrow x = 0$ (thoả mãn).")
        ]),
        ("Tìm tham số m để bất phương trình vô nghiệm", "b6", [
            lambda: ("Tìm m để bất phương trình $(m - 2)x > 3$ vô nghiệm:", ["$m = 2$", "$m > 2$", "$m < 2$", "$m = 0$"], 0, "Khi $m = 2$, BPT trở thành $0x > 3$ (vô lý với mọi x) nên BPT vô nghiệm."),
            lambda: ("Giá trị của k để bất phương trình $(k + 1)x > 5$ vô nghiệm là:", ["$k = -1$", "$k = 1$", "$k = 0$", "$k > -1$"], 0, "Khi $k = -1$, BPT trở thành $0x > 5$ (vô nghiệm)."),
            lambda: ("Tìm tham số m để bất phương trình $(2m - 4)x \\ge 1$ vô nghiệm:", ["$m = 2$", "$m = -2$", "$m > 2$", "$m = 0$"], 0, "Khi $2m - 4 = 0 \\Leftrightarrow m = 2$, BPT trở thành $0x \\ge 1$ (vô nghiệm)."),
            lambda: ("Bất phương trình $(a - 3)x < -2$ vô nghiệm khi a bằng:", ["$a = 3$", "$a > 3$", "$a < 3$", "$a = 0$"], 0, "Khi $a = 3$, BPT thành $0x < -2$ (vô nghiệm).")
        ])
    ]
    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c2-{len(mc)+1:03d}", "chapter": "c2", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    sa_nb = [
        ("Nghiệm nguyên lớn nhất thoả mãn BPT", "b6", [
            ("Tìm số nguyên lớn nhất thoả mãn bất phương trình $x < 5$:", 4, "Số nguyên lớn nhất nhỏ hơn 5 là 4."),
            ("Số nguyên lớn nhất thoả mãn bất phương trình $x < 8$ là:", 7, "Số nguyên lớn nhất nhỏ hơn 8 là 7."),
            ("Tìm số nguyên x lớn nhất sao cho $x < 10$:", 9, "Số nguyên lớn nhất là 9."),
            ("Số nguyên lớn nhất thoả mãn bất phương trình $x < 12$ là:", 11, "Số nguyên lớn nhất là 11."),
            ("Tìm giá trị nguyên lớn nhất của x thoả mãn $x < 3$:", 2, "Số nguyên lớn nhất nhỏ hơn 3 là 2.")
        ]),
        ("Nghiệm dương của phương trình tích", "b4", [
            ("Tìm nghiệm dương của phương trình $(x - 4)(x + 5) = 0$:", 4, "Nghiệm dương là $x = 4$."),
            ("Nghiệm nguyên dương của phương trình $(x - 7)(x + 2) = 0$ là:", 7, "Nghiệm dương là $x = 7$."),
            ("Phương trình $(x - 3)(x + 6) = 0$ có nghiệm dương bằng:", 3, "Nghiệm dương là $x = 3$."),
            ("Tìm nghiệm dương của phương trình $(x - 9)(x + 1) = 0$:", 9, "Nghiệm dương là $x = 9$."),
            ("Giá trị nghiệm dương của phương trình $(x - 5)(x + 8) = 0$ là:", 5, "Nghiệm dương là $x = 5$.")
        ]),
        ("ĐKXĐ giá trị làm mẫu bằng 0", "b4", [
            ("Giá trị nào của x làm cho mẫu thức của phân thức $\\frac{1}{x - 6}$ bằng 0?", 6, "$x - 6 = 0 \\Leftrightarrow x = 6$."),
            ("Tìm giá trị của x để mẫu thức của $\\frac{2}{x - 8}$ triệt tiêu (bằng 0):", 8, "$x - 8 = 0 \\Leftrightarrow x = 8$."),
            ("Mẫu thức của phân thức $\\frac{5}{x - 3}$ bằng 0 khi x bằng:", 3, "$x - 3 = 0 \\Leftrightarrow x = 3$."),
            ("Tìm x để mẫu của $\\frac{1}{2x - 10}$ bằng 0:", 5, "$2x - 10 = 0 \\Leftrightarrow x = 5$."),
            ("Giá trị của x làm mẫu thức của $\\frac{4}{x - 7}$ không xác định là:", 7, "Mẫu bằng 0 khi $x = 7$.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Nghiệm của phương trình phân thức", "b4", [
            ("Giải phương trình $\\frac{2x}{x - 1} = 3$. Nghiệm của phương trình bằng:", 3, "$2x = 3(x - 1) \\Rightarrow 2x = 3x - 3 \\Rightarrow x = 3$."),
            ("Nghiệm của phương trình $\\frac{3x}{x + 1} = 2$ là:", 2, "$3x = 2(x + 1) \\Rightarrow 3x = 2x + 2 \\Rightarrow x = 2$."),
            ("Giải phương trình $\\frac{4x - 2}{x} = 3$ ta được nghiệm là:", 2, "$4x - 2 = 3x \\Rightarrow x = 2$."),
            ("Nghiệm của phương trình $\\frac{x + 6}{x} = 4$ bằng bao nhiêu?", 2, "$x + 6 = 4x \\Rightarrow 3x = 6 \\Rightarrow x = 2$.")
        ]),
        ("Số nghiệm nguyên dương của bất phương trình", "b6", [
            ("Số các số nguyên dương thoả mãn $2x \\le 8$ là:", 4, "$x \\le 4$. Các số nguyên dương là 1, 2, 3, 4 (4 số)."),
            ("Có bao nhiêu số nguyên dương x thoả mãn bất phương trình $3x \\le 15$:", 5, "$x \\le 5$. Có 5 số nguyên dương là 1, 2, 3, 4, 5."),
            ("Số nghiệm nguyên dương của bất phương trình $x + 2 \\le 8$ là:", 6, "$x \\le 6$. Có 6 số nguyên dương."),
            ("Tìm số các số nguyên dương thoả mãn $4x \\le 12$:", 3, "$x \\le 3$. Có 3 số nguyên dương là 1, 2, 3.")
        ]),
        ("Nghiệm nguyên của phương trình tích", "b4", [
            ("Nghiệm nguyên lớn hơn của phương trình $(x - 5)(x - 2) = 0$ là:", 5, "Hai nghiệm là 2 và 5. Nghiệm lớn hơn là 5."),
            ("Tìm nghiệm nguyên lớn hơn của phương trình $(x - 8)(x - 3) = 0$:", 8, "Nghiệm lớn hơn là 8."),
            ("Nghiệm nguyên dương của phương trình $(x - 6)(x + 4) = 0$ bằng:", 6, "Nghiệm nguyên dương là 6."),
            ("Phương trình $(x - 10)(x - 1) = 0$ có nghiệm lớn bằng:", 10, "Nghiệm lớn là 10.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Giá trị nhỏ nhất Cauchy", "b5", [
            ("Cho $x > 0$. Giá trị nhỏ nhất của biểu thức $A = x + \\frac{4}{x}$ là:", 4, "Theo BĐT Cauchy: GTNN bằng $2\\sqrt{4} = 4$."),
            ("Với $a > 0$, giá trị nhỏ nhất của $B = a + \\frac{9}{a}$ bằng bao nhiêu?", 6, "Theo BĐT Cauchy: GTNN bằng $2\\sqrt{9} = 6$."),
            ("Tìm giá trị nhỏ nhất của biểu thức $C = x + \\frac{16}{x}$ với $x > 0$:", 8, "Theo BĐT Cauchy: GTNN bằng $2\\sqrt{16} = 8$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c2-{len(sa)+1:03d}", "chapter": "c2", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b4", "sgk_title": "Bài 4. Phương trình quy về phương trình bậc nhất một ẩn"},
        {"lesson_id": "b5", "sgk_title": "Bài 5. Bất đẳng thức và tính chất"},
        {"lesson_id": "b6", "sgk_title": "Bài 6. Bất phương trình bậc nhất một ẩn"}
    ]
    save_bank("c2", "Phương trình và bất phương trình bậc nhất một ẩn", lessons, mc, sa)
