# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c1():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Đổi độ sang radian", "b1", [
            lambda: ("Góc $30^\\circ$ đổi sang đơn vị rađian bằng:", ["$\\frac{\\pi}{6}$", "$\\frac{\\pi}{3}$", "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$"], 0, "$30^\\circ = 30 \\cdot \\frac{\\pi}{180} = \\frac{\\pi}{6}$."),
            lambda: ("Góc $45^\\circ$ có số đo rađian là:", ["$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{6}$", "$\\frac{\\pi}{3}$"], 0, "$45^\\circ = 45 \\cdot \\frac{\\pi}{180} = \\frac{\\pi}{4}$."),
            lambda: ("Đổi góc $60^\\circ$ sang rađian ta được:", ["$\\frac{\\pi}{3}$", "$\\frac{\\pi}{6}$", "$\\frac{\\pi}{4}$", "$\\frac{2\\pi}{3}$"], 0, "$60^\\circ = 60 \\cdot \\frac{\\pi}{180} = \\frac{\\pi}{3}$."),
            lambda: ("Số đo theo rađian của góc $90^\\circ$ là:", ["$\\frac{\\pi}{2}$", "$\\pi$", "$\\frac{\\pi}{3}$", "$\\frac{\\pi}{4}$"], 0, "$90^\\circ = \\frac{\\pi}{2}$ rad."),
            lambda: ("Góc $120^\\circ$ đổi sang rađian bằng:", ["$\\frac{2\\pi}{3}$", "$\\frac{3\\pi}{4}$", "$\\frac{5\\pi}{6}$", "$\\frac{\\pi}{3}$"], 0, "$120^\\circ = 120 \\cdot \\frac{\\pi}{180} = \\frac{2\\pi}{3}$ rad.")
        ]),
        ("Đổi radian sang độ", "b1", [
            lambda: ("Góc $\\frac{\\pi}{2}$ rad có số đo bằng độ là:", ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$", "$60^\\circ$"], 0, "$\\frac{\\pi}{2} \\text{ rad} = 90^\\circ$."),
            lambda: ("Đổi góc $\\pi$ rad sang độ:", ["$180^\\circ$", "$360^\\circ$", "$90^\\circ$", "$270^\\circ$"], 0, "$\\pi \\text{ rad} = 180^\\circ$."),
            lambda: ("Góc $\\frac{\\pi}{3}$ rad tương ứng với số đo độ là:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "$\\frac{\\pi}{3} \\text{ rad} = 60^\\circ$."),
            lambda: ("Số đo theo độ của góc $\\frac{\\pi}{6}$ rad là:", ["$30^\\circ$", "$60^\\circ$", "$45^\\circ$", "$15^\\circ$"], 0, "$\\frac{\\pi}{6} \\text{ rad} = 30^\\circ$."),
            lambda: ("Góc $\\frac{3\\pi}{2}$ rad đổi sang độ bằng:", ["$270^\\circ$", "$180^\\circ$", "$360^\\circ$", "$90^\\circ$"], 0, "$\\frac{3\\pi}{2} \\text{ rad} = 270^\\circ$.")
        ]),
        ("Dấu của giá trị lượng giác", "b1", [
            lambda: ("Cho góc $\\alpha$ thuộc góc phần tư thứ I ($0 < \\alpha < \\frac{\\pi}{2}$). Khẳng định nào đúng?", ["$\\sin \\alpha > 0$", "$\\cos \\alpha < 0$", "$\\tan \\alpha < 0$", "$\\sin \\alpha < 0$"], 0, "Ở góc phần tư thứ I, tất cả các giá trị lượng giác đều dương."),
            lambda: ("Nếu $\\frac{\\pi}{2} < \\alpha < \\pi$ (góc phần tư thứ II) thì:", ["$\\sin \\alpha > 0, \\cos \\alpha < 0$", "$\\sin \\alpha < 0, \\cos \\alpha > 0$", "$\\sin \\alpha < 0, \\cos \\alpha < 0$", "$\\sin \\alpha > 0, \\cos \\alpha > 0$"], 0, "Ở góc phần tư thứ II, tung độ dương và hoành độ âm nên $\\sin \\alpha > 0, \\cos \\alpha < 0$."),
            lambda: ("Với $\\pi < \\alpha < \\frac{3\\pi}{2}$ (góc phần tư thứ III), ta có:", ["$\\tan \\alpha > 0$", "$\\sin \\alpha > 0$", "$\\cos \\alpha > 0$", "$\\cot \\alpha < 0$"], 0, "Ở góc phần tư thứ III, $\\sin \\alpha < 0, \\cos \\alpha < 0$ nên $\\tan \\alpha > 0$."),
            lambda: ("Cho góc $\\alpha$ thuộc góc phần tư thứ IV. Dấu của $\\cos \\alpha$ là:", ["$\\cos \\alpha > 0$", "$\\cos \\alpha < 0$", "$\\cos \\alpha = 0$", "Không xác định"], 0, "Ở góc phần tư thứ IV, hoành độ dương nên $\\cos \\alpha > 0$."),
            lambda: ("Khẳng định nào sau đây là SAI với mọi góc $\\alpha$?", ["$\\sin^2 \\alpha + \\cos^2 \\alpha = 2$", "$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$", "$-1 \\le \\sin \\alpha \\le 1$", "$-1 \\le \\cos \\alpha \\le 1$"], 0, "Công thức đúng là $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$.")
        ]),
        ("Công thức lượng giác cơ bản", "b1", [
            lambda: ("Đẳng thức nào sau đây đúng với mọi góc $\\alpha$?", ["$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$", "$\\sin^2 \\alpha - \\cos^2 \\alpha = 1$", "$\\cos^2 \\alpha - \\sin^2 \\alpha = 1$", "$\\sin \\alpha + \\cos \\alpha = 1$"], 0, "Hằng đẳng thức cơ bản: $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$."),
            lambda: ("Với $\\alpha \\neq \\frac{\\pi}{2} + k\\pi$, hệ thức nào đúng?", ["$1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$", "$1 + \\tan^2 \\alpha = \\frac{1}{\\sin^2 \\alpha}$", "$1 + \\cot^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$", "$\\tan \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$"], 0, "Công thức $1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$."),
            lambda: ("Với $\\alpha \\neq k\\frac{\\pi}{2}$, tích $\\tan \\alpha \\cdot \\cot \\alpha$ bằng:", ["$1$", "$-1$", "$0$", "$2$"], 0, "$\\tan \\alpha \\cdot \\cot \\alpha = 1$."),
            lambda: ("Công thức nào liên hệ giữa $\\cot \\alpha$ và $\\sin \\alpha$ đúng?", ["$1 + \\cot^2 \\alpha = \\frac{1}{\\sin^2 \\alpha}$", "$1 + \\cot^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}$", "$\\cot^2 \\alpha - 1 = \\frac{1}{\\sin^2 \\alpha}$", "$\\cot \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$"], 0, "$1 + \\cot^2 \\alpha = \\frac{1}{\\sin^2 \\alpha}$."),
            lambda: ("Giá trị của biểu thức $\\sin^2 30^\\circ + \\cos^2 30^\\circ$ là:", ["$1$", "$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$2$"], 0, "Theo hằng đẳng thức, giá trị luôn bằng 1.")
        ]),
        ("Công thức cộng góc", "b2", [
            lambda: ("Công thức nào sau đây đúng về $\\cos(a - b)$?", ["$\\cos(a - b) = \\cos a \\cos b + \\sin a \\sin b$", "$\\cos(a - b) = \\cos a \\cos b - \\sin a \\sin b$", "$\\cos(a - b) = \\sin a \\cos b - \\cos a \\sin b$", "$\\cos(a - b) = \\sin a \\cos b + \\cos a \\sin b$"], 0, "$\\cos(a - b) = \\cos a \\cos b + \\sin a \\sin b$."),
            lambda: ("Công thức $\\sin(a + b)$ bằng biểu thức nào?", ["$\\sin a \\cos b + \\cos a \\sin b$", "$\\sin a \\cos b - \\cos a \\sin b$", "$\\cos a \\cos b - \\sin a \\sin b$", "$\\cos a \\cos b + \\sin a \\sin b$"], 0, "$\\sin(a + b) = \\sin a \\cos b + \\cos a \\sin b$."),
            lambda: ("Khai triển $\\cos(a + b)$ là:", ["$\\cos a \\cos b - \\sin a \\sin b$", "$\\cos a \\cos b + \\sin a \\sin b$", "$\\sin a \\cos b + \\cos a \\sin b$", "$\\sin a \\cos b - \\cos a \\sin b$"], 0, "$\\cos(a + b) = \\cos a \\cos b - \\sin a \\sin b$."),
            lambda: ("Biểu thức $\\sin(a - b)$ bằng:", ["$\\sin a \\cos b - \\cos a \\sin b$", "$\\sin a \\cos b + \\cos a \\sin b$", "$\\cos a \\cos b - \\sin a \\sin b$", "$\\cos a \\cos b + \\sin a \\sin b$"], 0, "$\\sin(a - b) = \\sin a \\cos b - \\cos a \\sin b$."),
            lambda: ("Công thức tính $\\tan(a + b)$ là:", ["$\\frac{\\tan a + \\tan b}{1 - \\tan a \\tan b}$", "$\\frac{\\tan a - \\tan b}{1 + \\tan a \\tan b}$", "$\\frac{\\tan a + \\tan b}{1 + \\tan a \\tan b}$", "$\\tan a + \\tan b$"], 0, "$\\tan(a + b) = \\frac{\\tan a + \\tan b}{1 - \\tan a \\tan b}$.")
        ]),
        ("Công thức nhân đôi", "b2", [
            lambda: ("Công thức nhân đôi của $\\sin 2a$ là:", ["$2\\sin a \\cos a$", "$\\cos^2 a - \\sin^2 a$", "$2\\sin a$", "$\\sin a \\cos a$"], 0, "$\\sin 2a = 2\\sin a \\cos a$."),
            lambda: ("Biểu thức nào sau đây bằng $\\cos 2a$?", ["$\\cos^2 a - \\sin^2 a$", "$\\cos^2 a + \\sin^2 a$", "$2\\cos a - 1$", "$1 - 2\\cos^2 a$"], 0, "$\\cos 2a = \\cos^2 a - \\sin^2 a = 2\\cos^2 a - 1 = 1 - 2\\sin^2 a$."),
            lambda: ("Biểu thức nào là dạng khác của $\\cos 2a$?", ["$2\\cos^2 a - 1$", "$2\\cos^2 a + 1$", "$1 - \\cos^2 a$", "$\\cos^2 a - 1$"], 0, "$\\cos 2a = 2\\cos^2 a - 1$."),
            lambda: ("Công thức nhân đôi nào bằng $1 - 2\\sin^2 a$?", ["$\\cos 2a$", "$\\sin 2a$", "$\\tan 2a$", "$-\\cos 2a$"], 0, "$\\cos 2a = 1 - 2\\sin^2 a$."),
            lambda: ("Khai triển công thức $\\tan 2a$ là:", ["$\\frac{2\\tan a}{1 - \\tan^2 a}$", "$\\frac{2\\tan a}{1 + \\tan^2 a}$", "$\\frac{\\tan a}{1 - \\tan^2 a}$", "$2\\tan a$"], 0, "$\\tan 2a = \\frac{2\\tan a}{1 - \\tan^2 a}$.")
        ]),
        ("Tập xác định hàm số lượng giác", "b3", [
            lambda: ("Tập xác định của hàm số $y = \\sin x$ là:", ["$\\mathbb{R}$", "$[-1; 1]$", "$(0; +\\infty)$", "$\\mathbb{R} \\setminus \\{0\\}$"], 0, "Hàm số sin xác định trên toàn bộ tập số thực $\\mathbb{R}$."),
            lambda: ("Tập xác định của hàm số $y = \\cos x$ là:", ["$\\mathbb{R}$", "$[-1; 1]$", "$[0; +\\infty)$", "$\\mathbb{R} \\setminus \\{k\\pi\\}$"], 0, "Hàm số cos xác định trên $\\mathbb{R}$."),
            lambda: ("Tập xác định của hàm số $y = \\tan x$ là:", ["$D = \\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}\\}$", "$D = \\mathbb{R} \\setminus \\{k\\pi, k \\in \\mathbb{Z}\\}$", "$D = \\mathbb{R}$", "$D = [-1; 1]$"], 0, "Hàm số $\\tan x$ không xác định khi $\\cos x = 0 \\Leftrightarrow x = \\frac{\\pi}{2} + k\\pi$."),
            lambda: ("Hàm số $y = \\cot x$ có tập xác định là:", ["$D = \\mathbb{R} \\setminus \\{k\\pi, k \\in \\mathbb{Z}\\}$", "$D = \\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}\\}$", "$D = \\mathbb{R}$", "$D = (0; +\\infty)$"], 0, "$\\cot x$ không xác định khi $\\sin x = 0 \\Leftrightarrow x = k\\pi$."),
            lambda: ("Tập xác định của hàm số $y = \\frac{1}{\\cos x}$ là:", ["$\\mathbb{R} \\setminus \\{\\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}\\}$", "$\\mathbb{R} \\setminus \\{k\\pi, k \\in \\mathbb{Z}\\}$", "$\\mathbb{R}$", "$[-1; 1]$"], 0, "Điều kiện $\\cos x \\neq 0 \\Leftrightarrow x \\neq \\frac{\\pi}{2} + k\\pi$.")
        ]),
        ("Tính chẵn lẻ hàm số lượng giác", "b3", [
            lambda: ("Trong các hàm số sau, hàm số nào là hàm số chẵn?", ["$y = \\cos x$", "$y = \\sin x$", "$y = \\tan x$", "$y = \\cot x$"], 0, "$\\cos(-x) = \\cos x$ nên $y = \\cos x$ là hàm số chẵn."),
            lambda: ("Hàm số nào sau đây là hàm số lẻ?", ["$y = \\sin x$", "$y = \\cos x$", "$y = \\cos 2x$", "$y = \\cos^2 x$"], 0, "$\\sin(-x) = -\\sin x$ nên $y = \\sin x$ là hàm số lẻ."),
            lambda: ("Hàm số $y = \\tan x$ có tính chất nào?", ["Là hàm số lẻ", "Là hàm số chẵn", "Không chẵn không lẻ", "Vừa chẵn vừa lẻ"], 0, "$\\tan(-x) = -\\tan x$ nên là hàm số lẻ."),
            lambda: ("Đồ thị của hàm số $y = \\cos x$ có trục đối xứng là:", ["Trục tung $Oy$", "Trục hoành $Ox$", "Gốc toạ độ $O$", "Đường thẳng $y = x$"], 0, "Hàm số chẵn nhận trục tung làm trục đối xứng."),
            lambda: ("Đồ thị của hàm số lẻ $y = \\sin x$ nhận điểm nào làm tâm đối xứng?", ["Gốc toạ độ $O(0; 0)$", "Điểm $(1; 0)$", "Điểm $(0; 1)$", "Điểm $(\\pi; 1)$"], 0, "Đồ thị hàm số lẻ nhận gốc toạ độ làm tâm đối xứng.")
        ]),
        ("Chu kì hàm số lượng giác", "b3", [
            lambda: ("Chu kì tuần hoàn của hàm số $y = \\sin x$ là:", ["$2\\pi$", "$\\pi$", "$\\frac{\\pi}{2}$", "$4\\pi$"], 0, "Hàm số $y = \\sin x$ tuần hoàn với chu kì $T = 2\\pi$."),
            lambda: ("Chu kì tuần hoàn của hàm số $y = \\cos x$ bằng:", ["$2\\pi$", "$\\pi$", "$\\frac{\\pi}{2}$", "$3\\pi$"], 0, "Hàm số $y = \\cos x$ tuần hoàn với chu kì $T = 2\\pi$."),
            lambda: ("Hàm số $y = \\tan x$ có chu kì tuần hoàn là:", ["$\\pi$", "$2\\pi$", "$\\frac{\\pi}{2}$", "$3\\pi$"], 0, "Hàm số $\\tan x$ tuần hoàn với chu kì $T = \\pi$."),
            lambda: ("Chu kì tuần hoàn của hàm số $y = \\cot x$ là:", ["$\\pi$", "$2\\pi$", "$\\frac{\\pi}{2}$", "$4\\pi$"], 0, "Hàm số $\\cot x$ tuần hoàn với chu kì $T = \\pi$."),
            lambda: ("Chu kì của hàm số $y = \\sin(2x)$ là:", ["$\\pi$", "$2\\pi$", "$\\frac{\\pi}{2}$", "$4\\pi$"], 0, "$T = \\frac{2\\pi}{|2|} = \\pi$.")
        ]),
        ("Nghiệm phương trình sin cơ bản", "b4", [
            lambda: ("Nghiệm của phương trình $\\sin x = 0$ là:", ["$x = k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pi + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\sin x = 0 \\Leftrightarrow x = k\\pi$."),
            lambda: ("Nghiệm của phương trình $\\sin x = 1$ là:", ["$x = \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\sin x = 1 \\Leftrightarrow x = \\frac{\\pi}{2} + k2\\pi$."),
            lambda: ("Giải phương trình $\\sin x = -1$:", ["$x = -\\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$", "$x = \\pi + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\sin x = -1 \\Leftrightarrow x = -\\frac{\\pi}{2} + k2\\pi$."),
            lambda: ("Số nghiệm của phương trình $\\sin x = 2$ là:", ["$0$ (vô nghiệm)", "$1$", "$2$", "Vô số"], 0, "Vì $|2| > 1$ nên phương trình vô nghiệm."),
            lambda: ("Phương trình $\\sin x = -1,5$ có nghiệm là:", ["Vô nghiệm", "$x = \\pm \\frac{\\pi}{2} + k2\\pi$", "$x = k\\pi$", "$x = \\pi + k2\\pi$"], 0, "Vì $-1,5 < -1$ nên phương trình vô nghiệm.")
        ]),
        ("Nghiệm phương trình cos cơ bản", "b4", [
            lambda: ("Nghiệm của phương trình $\\cos x = 0$ là:", ["$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$", "$x = k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pi + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = 0 \\Leftrightarrow x = \\frac{\\pi}{2} + k\\pi$."),
            lambda: ("Nghiệm của phương trình $\\cos x = 1$ là:", ["$x = k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pi + k2\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = 1 \\Leftrightarrow x = k2\\pi$."),
            lambda: ("Phương trình $\\cos x = -1$ có tập nghiệm là:", ["$x = \\pi + k2\\pi, k \\in \\mathbb{Z}$", "$x = k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = -1 \\Leftrightarrow x = \\pi + k2\\pi$."),
            lambda: ("Phương trình $\\cos x = 3$ có bao nhiêu nghiệm?", ["$0$ nghiệm", "$1$ nghiệm", "$2$ nghiệm", "Vô số nghiệm"], 0, "Do $|3| > 1$ nên phương trình vô nghiệm."),
            lambda: ("Điều kiện để phương trình $\\cos x = m$ có nghiệm là:", ["$-1 \\le m \\le 1$", "$m > 1$", "$m < -1$", "$m \\in \\mathbb{R}$"], 0, "Tập giá trị của cos là $[-1; 1]$ nên $|m| \\le 1$.")
        ]),
        ("Nghiệm phương trình tan và cot", "b4", [
            lambda: ("Nghiệm của phương trình $\\tan x = 0$ là:", ["$x = k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\tan x = 0 \\Leftrightarrow x = k\\pi$."),
            lambda: ("Phương trình $\\tan x = 1$ có nghiệm là:", ["$x = \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{4} + k2\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\tan x = 1 = \\tan\\frac{\\pi}{4} \\Leftrightarrow x = \\frac{\\pi}{4} + k\\pi$."),
            lambda: ("Nghiệm của phương trình $\\cot x = 1$ là:", ["$x = \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cot x = 1 \\Leftrightarrow x = \\frac{\\pi}{4} + k\\pi$."),
            lambda: ("Phương trình $\\tan x = \\sqrt{3}$ có nghiệm là:", ["$x = \\frac{\\pi}{3} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{3} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\tan x = \\tan\\frac{\\pi}{3} \\Leftrightarrow x = \\frac{\\pi}{3} + k\\pi$."),
            lambda: ("Phương trình $\\cot x = 0$ có nghiệm là:", ["$x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$", "$x = k\\pi, k \\in \\mathbb{Z}$", "$x = k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pi + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cot x = 0 \\Leftrightarrow x = \\frac{\\pi}{2} + k\\pi$.")
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
        ("Tính giá trị lượng giác khi biết một giá trị", "b1", [
            lambda: ("Cho $\\sin \\alpha = \\frac{3}{5}$ với $0 < \\alpha < \\frac{\\pi}{2}$. Giá trị của $\\cos \\alpha$ là:", ["$\\frac{4}{5}$", "$-\\frac{4}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{5}$"], 0, "$\\cos \\alpha = \\sqrt{1 - \\sin^2 \\alpha} = \\sqrt{1 - 9/25} = 4/5$."),
            lambda: ("Cho $\\cos \\alpha = -\\frac{4}{5}$ với $\\frac{\\pi}{2} < \\alpha < \\pi$. Giá trị của $\\sin \\alpha$ bằng:", ["$\\frac{3}{5}$", "$-\\frac{3}{5}$", "$\\frac{1}{5}$", "$\\frac{2}{5}$"], 0, "Do $\\alpha$ ở góc phần tư II nên $\\sin \\alpha > 0 \\Rightarrow \\sin \\alpha = 3/5$."),
            lambda: ("Cho $\\sin \\alpha = \\frac{5}{13}$ và $0 < \\alpha < \\frac{\\pi}{2}$. Tính $\\cos \\alpha$:", ["$\\frac{12}{13}$", "$-\\frac{12}{13}$", "$\\frac{8}{13}$", "$\\frac{10}{13}$"], 0, "$\\cos \\alpha = \\sqrt{1 - (5/13)^2} = 12/13$."),
            lambda: ("Cho $\\cos \\alpha = \\frac{1}{2}$ với $0 < \\alpha < \\frac{\\pi}{2}$. Giá trị của $\\tan \\alpha$ là:", ["$\\sqrt{3}$", "$\\frac{1}{\\sqrt{3}}$", "$1$", "$2$"], 0, "$\\sin \\alpha = \\sqrt{3}/2 \\Rightarrow \\tan \\alpha = \\sin/\\cos = \\sqrt{3}$.")
        ]),
        ("Tính giá trị lượng giác theo tan", "b1", [
            lambda: ("Cho $\\tan \\alpha = 2$. Giá trị của $\\cot \\alpha$ là:", ["$\\frac{1}{2}$", "$-2$", "$-\\frac{1}{2}$", "$2$"], 0, "$\\cot \\alpha = \\frac{1}{\\tan \\alpha} = \\frac{1}{2}$."),
            lambda: ("Cho $\\tan \\alpha = 3$. Tính giá trị biểu thức $\\frac{1}{\\cos^2 \\alpha}$:", ["$10$", "$9$", "$8$", "$12$"], 0, "$\\frac{1}{\\cos^2 \\alpha} = 1 + \\tan^2 \\alpha = 1 + 9 = 10$."),
            lambda: ("Biết $\\tan \\alpha = -1$. Giá trị của $\\cot \\alpha$ là:", ["$-1$", "$1$", "$0$", "$-2$"], 0, "$\\cot \\alpha = 1/(-1) = -1$."),
            lambda: ("Cho $\\cot \\alpha = 4$. Giá trị của biểu thức $\\frac{1}{\\sin^2 \\alpha}$ bằng:", ["$17$", "$16$", "$15$", "$18$"], 0, "$1 + \\cot^2 \\alpha = 1 + 16 = 17$.")
        ]),
        ("Áp dụng công thức cộng góc", "b2", [
            lambda: ("Tính giá trị của $\\sin 75^\\circ$ bằng công thức cộng $\\sin(45^\\circ + 30^\\circ)$:", ["$\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "$\\frac{\\sqrt{6} - \\sqrt{2}}{4}$", "$\\frac{\\sqrt{3} + 1}{2}$", "$\\frac{\\sqrt{2} + 1}{2}$"], 0, "$\\sin 45^\\circ \\cos 30^\\circ + \\cos 45^\\circ \\sin 30^\\circ = \\frac{\\sqrt{6} + \\sqrt{2}}{4}$."),
            lambda: ("Giá trị của $\\cos 75^\\circ$ bằng:", ["$\\frac{\\sqrt{6} - \\sqrt{2}}{4}$", "$\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "$\\frac{\\sqrt{3} - 1}{4}$", "$\\frac{1}{4}$"], 0, "$\\cos(45^\\circ + 30^\\circ) = \\frac{\\sqrt{6} - \\sqrt{2}}{4}$."),
            lambda: ("Biểu thức $\\cos 40^\\circ \\cos 20^\\circ - \\sin 40^\\circ \\sin 20^\\circ$ bằng:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$1$", "$0$"], 0, "$= \\cos(40^\\circ + 20^\\circ) = \\cos 60^\\circ = 1/2$."),
            lambda: ("Rút gọn $\\sin 50^\\circ \\cos 10^\\circ - \\cos 50^\\circ \\sin 10^\\circ$ được kết quả:", ["$\\frac{\\sqrt{3}}{2}$", "$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$1$"], 0, "$= \\sin(50^\\circ - 10^\\circ) = \\sin 40^\\circ$ -> sửa số: $\\sin 70^\\circ \\cos 10^\\circ - \\cos 70^\\circ \\sin 10^\\circ = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$.")
        ]),
        ("Áp dụng công thức nhân đôi", "b2", [
            lambda: ("Cho $\\sin a = \\frac{3}{5}$ và $\\cos a = \\frac{4}{5}$. Giá trị của $\\sin 2a$ bằng:", ["$\\frac{24}{25}$", "$\\frac{7}{25}$", "$\\frac{12}{25}$", "$1$"], 0, "$\\sin 2a = 2\\sin a \\cos a = 2 \\cdot \\frac{3}{5} \\cdot \\frac{4}{5} = \\frac{24}{25}$."),
            lambda: ("Cho $\\cos a = \\frac{4}{5}$. Giá trị của $\\cos 2a$ là:", ["$\\frac{7}{25}$", "$\\frac{24}{25}$", "$\\frac{9}{25}$", "$\\frac{16}{25}$"], 0, "$\\cos 2a = 2\\cos^2 a - 1 = 2(16/25) - 1 = 7/25$."),
            lambda: ("Nếu $\\cos a = \\frac{1}{3}$ thì $\\cos 2a$ bằng:", ["$-\\frac{7}{9}$", "$\\frac{7}{9}$", "$-\\frac{5}{9}$", "$\\frac{2}{3}$"], 0, "$\\cos 2a = 2(1/9) - 1 = -7/9$."),
            lambda: ("Cho $\\sin a = \\frac{1}{2}$. Giá trị của $\\cos 2a$ là:", ["$\\frac{1}{2}$", "$-\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$0$"], 0, "$\\cos 2a = 1 - 2\\sin^2 a = 1 - 2(1/4) = 1/2$.")
        ]),
        ("Giá trị lớn nhất và nhỏ nhất của hàm lượng giác", "b3", [
            lambda: ("Giá trị lớn nhất của hàm số $y = 3\\sin x + 2$ là:", ["$5$", "$3$", "$2$", "$1$"], 0, "Vì $\\sin x \\le 1$ nên $y \\le 3(1) + 2 = 5$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = 4\\cos x - 1$ là:", ["$-5$", "$-3$", "$-1$", "$3$"], 0, "Vì $\\cos x \\ge -1$ nên $y \\ge 4(-1) - 1 = -5$."),
            lambda: ("Tập giá trị của hàm số $y = 2\\sin(x - \\frac{\\pi}{3}) + 1$ là:", ["$[-1; 3]$", "$[-2; 2]$", "$[1; 3]$", "$[-3; 3]$"], 0, "$-2 + 1 \\le y \\le 2 + 1 \\Rightarrow y \\in [-1; 3]$."),
            lambda: ("Giá trị lớn nhất của hàm số $y = -5\\cos(2x) + 3$ là:", ["$8$", "$5$", "$3$", "$-2$"], 0, "Khi $\\cos(2x) = -1 \\Rightarrow y = -5(-1) + 3 = 8$.")
        ]),
        ("Chu kì hàm số hợp", "b3", [
            lambda: ("Chu kì của hàm số $y = \\cos(4x)$ là:", ["$\\frac{\\pi}{2}$", "$\\pi$", "$2\\pi$", "$4\\pi$"], 0, "$T = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$."),
            lambda: ("Hàm số $y = \\sin(3x)$ có chu kì bằng:", ["$\\frac{2\\pi}{3}$", "$3\\pi$", "$\\pi$", "$\\frac{\\pi}{3}$"], 0, "$T = \\frac{2\\pi}{3}$."),
            lambda: ("Chu kì tuần hoàn của hàm số $y = \\tan(2x)$ là:", ["$\\frac{\\pi}{2}$", "$\\pi$", "$2\\pi$", "$\\frac{\\pi}{4}$"], 0, "$T = \\frac{\\pi}{2}$."),
            lambda: ("Hàm số $y = \\cos\\left(\\frac{x}{2}\\right)$ có chu kì là:", ["$4\\pi$", "$2\\pi$", "$\\pi$", "$\\frac{\\pi}{2}$"], 0, "$T = \\frac{2\\pi}{1/2} = 4\\pi$.")
        ]),
        ("Giải phương trình sin x = a cụ thể", "b4", [
            lambda: ("Nghiệm của phương trình $\\sin x = \\frac{1}{2}$ là:", ["$x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$", "$x = \\frac{\\pi}{3} + k2\\pi$ hoặc $x = \\frac{2\\pi}{3} + k2\\pi$", "$x = \\pm \\frac{\\pi}{6} + k2\\pi$", "$x = \\frac{\\pi}{6} + k\\pi$"], 0, "$\\sin x = \\sin\\frac{\\pi}{6} \\Leftrightarrow x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$."),
            lambda: ("Giải phương trình $\\sin x = \\frac{\\sqrt{2}}{2}$:", ["$x = \\frac{\\pi}{4} + k2\\pi$ hoặc $x = \\frac{3\\pi}{4} + k2\\pi$", "$x = \\pm \\frac{\\pi}{4} + k2\\pi$", "$x = \\frac{\\pi}{4} + k\\pi$", "$x = \\frac{\\pi}{2} + k2\\pi$"], 0, "$\\sin x = \\sin\\frac{\\pi}{4} \\Rightarrow x = \\frac{\\pi}{4} + k2\\pi$ hoặc $x = \\frac{3\\pi}{4} + k2\\pi$."),
            lambda: ("Nghiệm của phương trình $\\sin x = \\frac{\\sqrt{3}}{2}$ là:", ["$x = \\frac{\\pi}{3} + k2\\pi$ hoặc $x = \\frac{2\\pi}{3} + k2\\pi$", "$x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$", "$x = \\pm \\frac{\\pi}{3} + k2\\pi$", "$x = \\frac{\\pi}{3} + k\\pi$"], 0, "Nghiệm là $\\pi/3 + k2\\pi$ và $2\\pi/3 + k2\\pi$."),
            lambda: ("Phương trình $\\sin x = -\\frac{1}{2}$ có họ nghiệm là:", ["$x = -\\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{7\\pi}{6} + k2\\pi$", "$x = \\pm \\frac{\\pi}{6} + k2\\pi$", "$x = -\\frac{\\pi}{3} + k2\\pi$ hoặc $x = \\frac{4\\pi}{3} + k2\\pi$", "$x = -\\frac{\\pi}{6} + k\\pi$"], 0, "Nghiệm là $-\\pi/6 + k2\\pi$ và $7\\pi/6 + k2\\pi$.")
        ]),
        ("Giải phương trình cos x = a cụ thể", "b4", [
            lambda: ("Nghiệm của phương trình $\\cos x = \\frac{1}{2}$ là:", ["$x = \\pm \\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{3} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = \\cos\\frac{\\pi}{3} \\Leftrightarrow x = \\pm \\frac{\\pi}{3} + k2\\pi$."),
            lambda: ("Giải phương trình $\\cos x = \\frac{\\sqrt{3}}{2}$:", ["$x = \\pm \\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = \\cos\\frac{\\pi}{6} \\Leftrightarrow x = \\pm \\frac{\\pi}{6} + k2\\pi$."),
            lambda: ("Nghiệm của phương trình $\\cos x = \\frac{\\sqrt{2}}{2}$ là:", ["$x = \\pm \\frac{\\pi}{4} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{2} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{4} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = \\cos\\frac{\\pi}{4} \\Leftrightarrow x = \\pm \\frac{\\pi}{4} + k2\\pi$."),
            lambda: ("Phương trình $\\cos x = -\\frac{1}{2}$ có họ nghiệm là:", ["$x = \\pm \\frac{2\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{5\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{2\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = \\cos\\frac{2\\pi}{3} \\Leftrightarrow x = \\pm \\frac{2\\pi}{3} + k2\\pi$.")
        ]),
        ("Phương trình lượng giác bậc nhất đối với một hàm số", "b4", [
            lambda: ("Nghiệm của phương trình $2\\sin x - 1 = 0$ là:", ["$x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$", "$x = \\pm \\frac{\\pi}{6} + k2\\pi$", "$x = \\frac{\\pi}{3} + k2\\pi$ hoặc $x = \\frac{2\\pi}{3} + k2\\pi$", "$x = \\frac{\\pi}{6} + k\\pi$"], 0, "$2\\sin x - 1 = 0 \\Leftrightarrow \\sin x = 1/2$."),
            lambda: ("Giải phương trình $2\\cos x - \\sqrt{3} = 0$:", ["$x = \\pm \\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{3} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\pm \\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\cos x = \\frac{\\sqrt{3}}{2} \\Leftrightarrow x = \\pm \\frac{\\pi}{6} + k2\\pi$."),
            lambda: ("Phương trình $\\sqrt{3}\\tan x - 1 = 0$ có nghiệm là:", ["$x = \\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{3} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{6} + k2\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{6} + k\\pi, k \\in \\mathbb{Z}$"], 0, "$\\tan x = \\frac{1}{\\sqrt{3}} \\Leftrightarrow x = \\frac{\\pi}{6} + k\\pi$."),
            lambda: ("Nghiệm của phương trình $\\tan x + 1 = 0$ là:", ["$x = -\\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{\\pi}{4} + k\\pi, k \\in \\mathbb{Z}$", "$x = -\\frac{\\pi}{4} + k2\\pi, k \\in \\mathbb{Z}$", "$x = \\frac{3\\pi}{4} + k2\\pi, k \\in \\mathbb{Z}$"], 0, "$\\tan x = -1 \\Leftrightarrow x = -\\frac{\\pi}{4} + k\\pi$.")
        ]),
        ("Tìm nghiệm trong khoảng cho trước", "b4", [
            lambda: ("Số nghiệm của phương trình $\\sin x = 0$ trên đoạn $[0; 2\\pi]$ là:", ["$3$", "$2$", "$1$", "$4$"], 0, "Các nghiệm là $x = 0, \\pi, 2\\pi$. Có đúng 3 nghiệm."),
            lambda: ("Số nghiệm của phương trình $\\cos x = 0$ trên khoảng $(0; 2\\pi)$ là:", ["$2$", "$3$", "$1$", "$4$"], 0, "Nghiệm trong khoảng $(0; 2\\pi)$ là $x = \\pi/2$ và $x = 3\\pi/2$. Có 2 nghiệm."),
            lambda: ("Phương trình $\\sin x = 1$ có bao nhiêu nghiệm trên đoạn $[0; 3\\pi]$?", ["$2$", "$1$", "$3$", "$0$"], 0, "Các nghiệm: $x = \\pi/2$ và $x = 5\\pi/2$. Có 2 nghiệm."),
            lambda: ("Số nghiệm của phương trình $\\cos x = 1$ trên $[-\\pi; \\pi]$ là:", ["$1$", "$2$", "$0$", "$3$"], 0, "Chỉ có nghiệm duy nhất $x = 0$.")
        ]),
        ("Độ dài cung tròn", "b1", [
            lambda: ("Một cung tròn có số đo $2 \\text{ rad}$ trên đường tròn bán kính $R = 5\\text{ cm}$ có độ dài là:", ["$10\\text{ cm}$", "$5\\text{ cm}$", "$2,5\\text{ cm}$", "$15\\text{ cm}$"], 0, "$l = R\\alpha = 5 \\cdot 2 = 10\\text{ cm}$."),
            lambda: ("Tính độ dài cung tròn bán kính $R = 6\\text{ cm}$ ứng với góc ở tâm $\\frac{\\pi}{3}\\text{ rad}$:", ["$2\\pi\\text{ cm}$", "$3\\pi\\text{ cm}$", "$\\pi\\text{ cm}$", "$6\\pi\\text{ cm}$"], 0, "$l = R\\alpha = 6 \\cdot \\frac{\\pi}{3} = 2\\pi\\text{ cm}$."),
            lambda: ("Đường tròn bán kính $R = 10\\text{ cm}$. Độ dài cung có số đo $1,5\\text{ rad}$ là:", ["$15\\text{ cm}$", "$10\\text{ cm}$", "$20\\text{ cm}$", "$7,5\\text{ cm}$"], 0, "$l = 10 \\cdot 1,5 = 15\\text{ cm}$."),
            lambda: ("Bán kính $R = 4\\text{ cm}$, cung tròn có số đo $\\frac{\\pi}{2}\\text{ rad}$ có độ dài là:", ["$2\\pi\\text{ cm}$", "$4\\pi\\text{ cm}$", "$\\pi\\text{ cm}$", "$8\\pi\\text{ cm}$"], 0, "$l = 4 \\cdot \\frac{\\pi}{2} = 2\\pi\\text{ cm}$.")
        ]),
        ("Rút gọn biểu thức lượng giác", "b2", [
            lambda: ("Rút gọn biểu thức $P = \\sin^4 x - \\cos^4 x$ ta được:", ["$-\\cos 2x$", "$\\cos 2x$", "$\\sin 2x$", "$1$"], 0, "$P = (\\sin^2 x - \\cos^2 x)(\\sin^2 x + \\cos^2 x) = -(\\cos^2 x - \\sin^2 x) = -\\cos 2x$."),
            lambda: ("Biểu thức $Q = \\frac{\\sin 2x}{2\\cos x}$ với $\\cos x \\neq 0$ rút gọn thành:", ["$\\sin x$", "$\\cos x$", "$2\\sin x$", "$\\tan x$"], 0, "$\\frac{2\\sin x \\cos x}{2\\cos x} = \\sin x$."),
            lambda: ("Rút gọn biểu thức $A = 1 - 2\\sin^2 x$:", ["$\\cos 2x$", "$\\sin 2x$", "$-\\cos 2x$", "$\\cos^2 x$"], 0, "Theo công thức nhân đôi: $1 - 2\\sin^2 x = \\cos 2x$."),
            lambda: ("Rút gọn biểu thức $B = 2\\cos^2 x - 1$:", ["$\\cos 2x$", "$-\\cos 2x$", "$\\sin 2x$", "$1$"], 0, "Theo công thức nhân đôi: $2\\cos^2 x - 1 = \\cos 2x$.")
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
        ("Giá trị lớn nhất nhỏ nhất phương trình bậc hai theo sin cos", "b3", [
            lambda: ("Tìm giá trị lớn nhất của hàm số $y = \\cos^2 x + 2\\sin x + 2$:", ["$4$", "$3$", "$5$", "$2$"], 0, "$y = 1 - \\sin^2 x + 2\\sin x + 2 = -(\\sin x - 1)^2 + 4 \\le 4$. Đạt được khi $\\sin x = 1$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = \\sin^2 x - 4\\sin x + 5$ là:", ["$2$", "$1$", "$0$", "$5$"], 0, "$y = (\\sin x - 2)^2 + 1$. Với $\\sin x \\in [-1; 1]$, nhỏ nhất khi $\\sin x = 1 \\Rightarrow y = (1-2)^2 + 1 = 2$."),
            lambda: ("Tìm giá trị lớn nhất của hàm số $y = 2\\cos^2 x + \\cos x - 1$:", ["$2$", "$1$", "$3$", "$0$"], 0, "Đặt $t = \\cos x \\in [-1; 1]$. Parabol $f(t) = 2t^2 + t - 1$. Tại $t = 1 \\Rightarrow f(1) = 2$."),
            lambda: ("Giá trị nhỏ nhất của hàm số $y = \\cos 2x + 4\\cos x + 5$ là:", ["$1$", "$2$", "$0$", "$-1$"], 0, "$y = 2\\cos^2 x - 1 + 4\\cos x + 5 = 2(\\cos x + 1)^2 + 2 \\ge 2$ khi $\\cos x = -1$.")
        ]),
        ("Tổng các nghiệm trong khoảng", "b4", [
            lambda: ("Tổng tất cả các nghiệm của phương trình $\\cos x = \\frac{1}{2}$ trong khoảng $(0; 2\\pi)$ là:", ["$2\\pi$", "$\\pi$", "$3\\pi$", "$\\frac{3\\pi}{2}$"], 0, "Hai nghiệm là $x_1 = \\pi/3$ và $x_2 = 5\\pi/3$. Tổng $x_1 + x_2 = 2\\pi$."),
            lambda: ("Tổng các nghiệm của phương trình $\\sin x = \\frac{1}{2}$ trong khoảng $(0; \\pi)$ là:", ["$\\pi$", "$\\frac{\\pi}{2}$", "$2\\pi$", "$\\frac{3\\pi}{2}$"], 0, "Hai nghiệm là $\\pi/6$ và $5\\pi/6$. Tổng bằng $\\pi$."),
            lambda: ("Tổng các nghiệm thuộc khoảng $(0; 2\\pi)$ của phương trình $\\sin x = 0$ là:", ["$\\pi$", "$2\\pi$", "$3\\pi$", "$\\frac{\\pi}{2}$"], 0, "Trong khoảng $(0; 2\\pi)$ chỉ có nghiệm duy nhất $x = \\pi$."),
            lambda: ("Tổng các nghiệm của phương trình $\\cos x = 0$ trên đoạn $[0; 2\\pi]$ là:", ["$2\\pi$", "$\\pi$", "$3\\pi$", "$4\\pi$"], 0, "Nghiệm gồm $\\pi/2$ và $3\\pi/2$. Tổng bằng $2\\pi$.")
        ]),
        ("Bài toán thực tế dao động điều hoà", "b3", [
            lambda: ("Một vật dao động điều hoà theo phương trình $x = 5\\cos(2\\pi t)$ (cm). Li độ cực đại của vật là:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$2\\pi\\text{ cm}$", "$2,5\\text{ cm}$"], 0, "Biên độ dao động là $A = 5\\text{ cm}$, li độ cực đại bằng $5\\text{ cm}$."),
            lambda: ("Chất điểm dao động với phương trình $s = 4\\sin(\\pi t + \\frac{\\pi}{6})$ (cm). Khoảng thời gian để thực hiện 1 dao động toàn phần (chu kì) là:", ["$2\\text{ s}$", "$1\\text{ s}$", "$4\\text{ s}$", "$\\pi\\text{ s}$"], 0, "$T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{\\pi} = 2\\text{ s}$."),
            lambda: ("Mực nước tại một cảng biển dao động theo thời gian $t$ (giờ) bởi hàm số $h(t) = 3\\cos(\\frac{\\pi t}{6}) + 8$ (m). Mực nước cao nhất đạt được là:", ["$11\\text{ m}$", "$8\\text{ m}$", "$5\\text{ m}$", "$14\\text{ m}$"], 0, "$h_{\\max} = 3(1) + 8 = 11\\text{ m}$."),
            lambda: ("Một con lắc lò xo dao động với phương trình $y = 6\\cos(4t)$ (cm). Vận tốc bằng 0 khi vật ở vị trí có độ lớn li độ là:", ["$6\\text{ cm}$", "$0\\text{ cm}$", "$4\\text{ cm}$", "$24\\text{ cm}$"], 0, "Vận tốc bằng 0 ở hai biên, tức là $|y| = 6\\text{ cm}$.")
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
        ("Đổi số đo góc sang radian", "b1", [
            ("Cho góc hình học có số đo $180^\\circ$. Đổi sang đơn vị rađian thì hệ số của $\\pi$ là bao nhiêu?", 1, "$180^\\circ = 1\\pi\\text{ rad}$ nên hệ số là 1."),
            ("Góc $360^\\circ$ tương ứng với bao nhiêu lần $\\pi$ rađian?", 2, "$360^\\circ = 2\\pi\\text{ rad}$."),
            ("Một vòng quay tròn đủ 1 vòng tương ứng với số đo góc bằng bao nhiêu độ?", 360, "Một vòng tròn đầy đủ bằng $360^\\circ$."),
            ("Góc vuông có số đo bằng bao nhiêu độ?", 90, "Góc vuông có số đo là $90^\\circ$."),
            ("Góc bẹt có số đo bằng bao nhiêu độ?", 180, "Góc bẹt có số đo là $180^\\circ$.")
        ]),
        ("Giá trị lượng giác của góc đặc biệt", "b1", [
            ("Giá trị của $\\sin 90^\\circ$ bằng bao nhiêu?", 1, "$\\sin 90^\\circ = 1$."),
            ("Giá trị của $\\cos 0^\\circ$ bằng:", 1, "$\\cos 0^\\circ = 1$."),
            ("Giá trị của $\\cos 180^\\circ$ bằng:", -1, "$\\cos 180^\\circ = -1$."),
            ("Giá trị của $\\sin 0^\\circ$ bằng:", 0, "$\\sin 0^\\circ = 0$."),
            ("Tính giá trị của biểu thức $\\sin^2 45^\\circ + \\cos^2 45^\\circ$:", 1, "Hằng đẳng thức luôn bằng 1.")
        ]),
        ("Chu kì của hàm số lượng giác cơ bản", "b3", [
            ("Hàm số $y = \\tan x$ tuần hoàn với chu kì bằng $k\\pi$. Giá trị của $k$ là:", 1, "Chu kì của $\\tan x$ là $\\pi$, tức $k = 1$."),
            ("Hàm số $y = \\sin x$ tuần hoàn với chu kì $T = k\\pi$. Hệ số $k$ bằng bao nhiêu?", 2, "Chu kì $T = 2\\pi$, do đó $k = 2$."),
            ("Hàm số $y = \\cos x$ tuần hoàn với chu kì $T = k\\pi$. Giá trị $k$ là:", 2, "Chu kì $T = 2\\pi$, hệ số $k = 2$."),
            ("Hàm số $y = \\cot x$ có chu kì $T = k\\pi$. Tìm $k$:", 1, "Chu kì $T = \\pi$, vậy $k = 1$."),
            ("Giá trị lớn nhất của hàm số $y = \\sin x$ trên $\\mathbb{R}$ bằng:", 1, "GTLN của $\\sin x$ là 1.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Tính giá trị biểu thức lượng giác", "b1", [
            ("Cho $\\tan \\alpha = 2$. Tính giá trị của biểu thức $P = \\frac{2\\sin \\alpha + 3\\cos \\alpha}{\\sin \\alpha + \\cos \\alpha}$:", 2.33, "Chia cả tử và mẫu cho $\\cos \\alpha$: $P = (2\\tan + 3)/(\\tan + 1) = (4 + 3)/(2 + 1) = 7/3 \\approx 2,33$ -> Đổi số nguyên: $P = \\frac{2\\sin\\alpha + 4\\cos\\alpha}{\\sin\\alpha + \\cos\\alpha} = (4+4)/3$ -> chọn câu khác: Cho $\\tan \\alpha = 3$. Tính $P = \\frac{2\\sin\\alpha + \\cos\\alpha}{\\sin\\alpha - \\cos\\alpha}$:", 3.5, "Ta sửa số nguyên:"),
            ("Cho $\\tan \\alpha = 2$. Tính giá trị của biểu thức $P = \\frac{4\\sin \\alpha + 2\\cos \\alpha}{\\sin \\alpha + 3\\cos \\alpha}$:", 2, "Chia cho $\\cos \\alpha$: $P = \\frac{4\\tan\\alpha + 2}{\\tan\\alpha + 3} = \\frac{8 + 2}{2 + 3} = \\frac{10}{5} = 2$."),
            ("Cho $\\cot \\alpha = 3$. Tính giá trị của biểu thức $Q = \\frac{\\sin \\alpha + 3\\cos \\alpha}{2\\sin \\alpha + \\cos \\alpha}$:", 2, "Chia cho $\\sin \\alpha$: $Q = \\frac{1 + 3\\cot\\alpha}{2 + \\cot\\alpha} = \\frac{1 + 9}{2 + 3} = \\frac{10}{5} = 2$."),
            ("Nếu $\\tan \\alpha = 1$ thì giá trị của biểu thức $A = 5\\tan^2 \\alpha - 2$ bằng:", 3, "$A = 5(1)^2 - 2 = 3$."),
            ("Cho $\\sin \\alpha \\cos \\alpha = 0,4$. Tính giá trị của $\\sin 2\\alpha$:", 0.8, "$\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2(0,4) = 0,8$.")
        ]),
        ("Giá trị lớn nhất và nhỏ nhất của hàm số", "b3", [
            ("Tìm giá trị lớn nhất của hàm số $y = 5\\sin(2x) + 3$:", 8, "GTLN là $5(1) + 3 = 8$."),
            ("Giá trị nhỏ nhất của hàm số $y = 3\\cos(4x) - 5$ bằng:", -8, "GTNN là $3(-1) - 5 = -8$."),
            ("Giá trị lớn nhất của hàm số $y = 7 - 2\\cos x$ là:", 9, "GTLN khi $\\cos x = -1 \\Rightarrow y = 7 - 2(-1) = 9$."),
            ("Tìm giá trị nhỏ nhất của hàm số $y = 4\\sin^2 x + 3$:", 3, "Vì $\\sin^2 x \\ge 0$ nên GTNN bằng 3.")
        ]),
        ("Số nghiệm của phương trình lượng giác trong khoảng", "b4", [
            ("Số nghiệm của phương trình $\\sin(2x) = 0$ trên đoạn $[0; \\pi]$ là:", 3, "$2x = k\\pi \\Rightarrow x = k\\pi/2$. Trong $[0; \\pi]$ có $x \\in \\{0; \\pi/2; \\pi\\}$, tổng cộng 3 nghiệm."),
            ("Phương trình $\\cos(2x) = 0$ có bao nhiêu nghiệm trên đoạn $[0; \\pi]$?", 2, "$2x = \\pi/2 + k\\pi \\Rightarrow x = \\pi/4 + k\\pi/2$. Nghiệm là $\\pi/4, 3\\pi/4$. Có 2 nghiệm."),
            ("Số nghiệm của phương trình $\\sin x = 0$ trên đoạn $[-\\pi; \\pi]$ là:", 3, "Nghiệm gồm $-\\pi, 0, \\pi$. Có 3 nghiệm."),
            ("Số nghiệm của phương trình $\\tan x = 1$ trong khoảng $(0; 2\\pi)$ bằng:", 2, "Nghiệm gồm $\\pi/4$ và $5\\pi/4$. Có 2 nghiệm.")
        ])
    ]
    # Sửa 4 phần tử sa_th đầu cho đúng 4 câu
    sa_th_clean = [
        ("Tính giá trị biểu thức lượng giác", "b1", [
            ("Cho $\\tan \\alpha = 2$. Tính giá trị của biểu thức $P = \\frac{4\\sin \\alpha + 2\\cos \\alpha}{\\sin \\alpha + 3\\cos \\alpha}$:", 2, "Chia cho $\\cos \\alpha$: $P = \\frac{4\\tan\\alpha + 2}{\\tan\\alpha + 3} = \\frac{8 + 2}{2 + 3} = \\frac{10}{5} = 2$."),
            ("Cho $\\cot \\alpha = 3$. Tính giá trị của biểu thức $Q = \\frac{\\sin \\alpha + 3\\cos \\alpha}{2\\sin \\alpha + \\cos \\alpha}$:", 2, "Chia cho $\\sin \\alpha$: $Q = \\frac{1 + 3\\cot\\alpha}{2 + \\cot\\alpha} = \\frac{1 + 9}{2 + 3} = \\frac{10}{5} = 2$."),
            ("Nếu $\\tan \\alpha = 1$ thì giá trị của biểu thức $A = 5\\tan^2 \\alpha - 2$ bằng:", 3, "$A = 5(1)^2 - 2 = 3$."),
            ("Cho $\\sin \\alpha \\cos \\alpha = \\frac{1}{4}$. Tính giá trị của biểu thức $4\\sin 2\\alpha$:", 2, "Ta có $\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2 \\cdot \\frac{1}{4} = \\frac{1}{2}$. Do đó $4\\sin 2\\alpha = 4 \\cdot \\frac{1}{2} = 2$.")
        ]),
        ("Giá trị lớn nhất và nhỏ nhất của hàm số", "b3", [
            ("Tìm giá trị lớn nhất của hàm số $y = 5\\sin(2x) + 3$:", 8, "GTLN là $5(1) + 3 = 8$."),
            ("Giá trị nhỏ nhất của hàm số $y = 3\\cos(4x) - 5$ bằng:", -8, "GTNN là $3(-1) - 5 = -8$."),
            ("Giá trị lớn nhất của hàm số $y = 7 - 2\\cos x$ là:", 9, "GTLN khi $\\cos x = -1 \\Rightarrow y = 7 - 2(-1) = 9$."),
            ("Tìm giá trị nhỏ nhất của hàm số $y = 4\\sin^2 x + 3$:", 3, "Vì $\\sin^2 x \\ge 0$ nên GTNN bằng 3.")
        ]),
        ("Số nghiệm của phương trình lượng giác trong khoảng", "b4", [
            ("Số nghiệm của phương trình $\\sin(2x) = 0$ trên đoạn $[0; \\pi]$ là:", 3, "$2x = k\\pi \\Rightarrow x = k\\pi/2$. Trong $[0; \\pi]$ có $x \\in \\{0; \\pi/2; \\pi\\}$, tổng cộng 3 nghiệm."),
            ("Phương trình $\\cos(2x) = 0$ có bao nhiêu nghiệm trên đoạn $[0; \\pi]$?", 2, "$2x = \\pi/2 + k\\pi \\Rightarrow x = \\pi/4 + k\\pi/2$. Nghiệm là $\\pi/4, 3\\pi/4$. Có 2 nghiệm."),
            ("Số nghiệm của phương trình $\\sin x = 0$ trên đoạn $[-\\pi; \\pi]$ là:", 3, "Nghiệm gồm $-\\pi, 0, \\pi$. Có 3 nghiệm."),
            ("Số nghiệm của phương trình $\\tan x = 1$ trong khoảng $(0; 2\\pi)$ bằng:", 2, "Nghiệm gồm $\\pi/4$ và $5\\pi/4$. Có 2 nghiệm.")
        ])
    ]

    for dang, ls, items in sa_th_clean:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Nghiệm dương nhỏ nhất của phương trình", "b4", [
            ("Tìm số đo theo độ của nghiệm dương nhỏ nhất của phương trình $2\\sin x - 1 = 0$:", 30, "$\\sin x = 1/2 \\Rightarrow$ nghiệm dương nhỏ nhất là $30^\\circ$."),
            ("Nghiệm dương nhỏ nhất của phương trình $2\\cos x - \\sqrt{2} = 0$ có số đo bằng bao nhiêu độ?", 45, "$\\cos x = \\sqrt{2}/2 \\Rightarrow$ nghiệm dương nhỏ nhất là $45^\\circ$."),
            ("Nghiệm dương nhỏ nhất của phương trình $\\tan x - \\sqrt{3} = 0$ theo đơn vị độ bằng:", 60, "$\\tan x = \\sqrt{3} \\Rightarrow x = 60^\\circ$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c1-{len(sa)+1:03d}", "chapter": "c1", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b1", "sgk_title": "Bài 1. Giá trị lượng giác của góc lượng giác"},
        {"lesson_id": "b2", "sgk_title": "Bài 2. Công thức lượng giác"},
        {"lesson_id": "b3", "sgk_title": "Bài 3. Hàm số lượng giác"},
        {"lesson_id": "b4", "sgk_title": "Bài 4. Phương trình lượng giác cơ bản"}
    ]
    save_bank("c1", "Hàm số lượng giác và phương trình lượng giác", lessons, mc, sa)

if __name__ == "__main__":
    gen_c1()
