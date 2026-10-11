# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

# ==============================================================================
# CHƯƠNG 4: HỆ THỨC LƯỢNG TRONG TAM GIÁC VUÔNG
# ==============================================================================
def gen_c4():
    mc, sa = [], []

    nb_configs = [
        ("Định nghĩa tỉ số sin góc nhọn", "b11", [
            lambda: ("Trong tam giác vuông, tỉ số giữa cạnh đối và cạnh huyền của góc nhọn $\\alpha$ là:", ["$\\sin \\alpha$", "$\\cos \\alpha$", "$\\tan \\alpha$", "$\\cot \\alpha$"], 0, "Theo định nghĩa, $\\sin \\alpha = \\frac{\\text{cạnh đối}}{\\text{cạnh huyền}}$."),
            lambda: ("Tỉ số lượng giác $\\sin B$ trong tam giác $ABC$ vuông tại $A$ được tính bằng:", ["$\\frac{AC}{BC}$", "$\\frac{AB}{BC}$", "$\\frac{AC}{AB}$", "$\\frac{AB}{AC}$"], 0, "$\\sin B = \\frac{\\text{cạnh đối}}{\\text{cạnh huyền}} = \\frac{AC}{BC}$."),
            lambda: ("Cho tam giác vuông $MNP$ vuông tại $M$. Tỉ số $\\sin N$ bằng:", ["$\\frac{MP}{NP}$", "$\\frac{MN}{NP}$", "$\\frac{MP}{MN}$", "$\\frac{MN}{MP}$"], 0, "$\\sin N = \\frac{MP}{NP}$."),
            lambda: ("Khẳng định nào đúng về tỉ số sin của một góc nhọn trong tam giác vuông?", ["Bằng cạnh đối chia cho cạnh huyền", "Bằng cạnh kề chia cho cạnh huyền", "Bằng cạnh đối chia cho cạnh kề", "Bằng cạnh kề chia cho cạnh đối"], 0, "Sin đi học: đối trên huyền."),
            lambda: ("Đại lượng $\\frac{\\text{cạnh đối}}{\\text{cạnh huyền}}$ của góc nhọn trong tam giác vuông gọi là:", ["Sin của góc đó", "Côsin của góc đó", "Tang của góc đó", "Côtang của góc đó"], 0, "Đây là định nghĩa sin của góc nhọn.")
        ]),
        ("Định nghĩa tỉ số cos góc nhọn", "b11", [
            lambda: ("Tỉ số giữa cạnh kề và cạnh huyền của góc nhọn $\\alpha$ trong tam giác vuông là:", ["$\\cos \\alpha$", "$\\sin \\alpha$", "$\\tan \\alpha$", "$\\cot \\alpha$"], 0, "Theo định nghĩa, $\\cos \\alpha = \\frac{\\text{cạnh kề}}{\\text{cạnh huyền}}$."),
            lambda: ("Trong tam giác $ABC$ vuông tại $A$, tỉ số $\\cos B$ bằng:", ["$\\frac{AB}{BC}$", "$\\frac{AC}{BC}$", "$\\frac{AB}{AC}$", "$\\frac{AC}{AB}$"], 0, "$\\cos B = \\frac{AB}{BC}$ (cạnh kề chia cạnh huyền)."),
            lambda: ("Cho tam giác vuông $DEF$ vuông tại $D$. Tỉ số $\\cos E$ được tính là:", ["$\\frac{DE}{EF}$", "$\\frac{DF}{EF}$", "$\\frac{DE}{DF}$", "$\\frac{DF}{DE}$"], 0, "$\\cos E = \\frac{DE}{EF}$."),
            lambda: ("Công thức nào đúng để tính côsin của góc nhọn trong tam giác vuông?", ["Bằng cạnh kề chia cho cạnh huyền", "Bằng cạnh đối chia cho cạnh huyền", "Bằng cạnh đối chia cho cạnh kề", "Bằng cạnh kề chia cho cạnh đối"], 0, "Cos khóc nhè: kề trên huyền."),
            lambda: ("Tỉ số $\\frac{\\text{cạnh kề}}{\\text{cạnh huyền}}$ của một góc nhọn xác định tỉ số lượng giác nào?", ["Côsin", "Sin", "Tang", "Côtang"], 0, "Đây là định nghĩa côsin của góc nhọn.")
        ]),
        ("Định nghĩa tỉ số tan góc nhọn", "b11", [
            lambda: ("Tỉ số giữa cạnh đối và cạnh kề của góc nhọn $\\alpha$ trong tam giác vuông là:", ["$\\tan \\alpha$", "$\\cot \\alpha$", "$\\sin \\alpha$", "$\\cos \\alpha$"], 0, "$\\tan \\alpha = \\frac{\\text{cạnh đối}}{\\text{cạnh kề}}$."),
            lambda: ("Trong tam giác $ABC$ vuông tại $A$, tỉ số $\\tan B$ bằng:", ["$\\frac{AC}{AB}$", "$\\frac{AB}{AC}$", "$\\frac{AC}{BC}$", "$\\frac{AB}{BC}$"], 0, "$\\tan B = \\frac{AC}{AB}$."),
            lambda: ("Cho tam giác vuông $HIK$ vuông tại $H$. Tỉ số $\\tan I$ được tính bằng:", ["$\\frac{HK}{HI}$", "$\\frac{HI}{HK}$", "$\\frac{HK}{IK}$", "$\\frac{HI}{IK}$"], 0, "$\\tan I = \\frac{HK}{HI}$."),
            lambda: ("Biểu thức $\\frac{\\text{cạnh đối}}{\\text{cạnh kề}}$ của một góc nhọn trong tam giác vuông xác định:", ["Tang của góc đó", "Côtang của góc đó", "Sin của góc đó", "Côsin của góc đó"], 0, "Tang đoàn kết: đối trên kề."),
            lambda: ("Tỉ số lượng giác nào bằng thương của cạnh đối chia cho cạnh kề?", ["Tang", "Côtang", "Sin", "Côsin"], 0, "Đó là tỉ số tang.")
        ]),
        ("Định nghĩa tỉ số cot góc nhọn", "b11", [
            lambda: ("Tỉ số giữa cạnh kề và cạnh đối của góc nhọn $\\alpha$ trong tam giác vuông là:", ["$\\cot \\alpha$", "$\\tan \\alpha$", "$\\cos \\alpha$", "$\\sin \\alpha$"], 0, "$\\cot \\alpha = \\frac{\\text{cạnh kề}}{\\text{cạnh đối}}$."),
            lambda: ("Trong tam giác $ABC$ vuông tại $A$, tỉ số $\\cot B$ bằng:", ["$\\frac{AB}{AC}$", "$\\frac{AC}{AB}$", "$\\frac{AB}{BC}$", "$\\frac{AC}{BC}$"], 0, "$\\cot B = \\frac{AB}{AC}$."),
            lambda: ("Cho tam giác vuông $MNP$ vuông tại $M$. Tỉ số $\\cot N$ bằng:", ["$\\frac{MN}{MP}$", "$\\frac{MP}{MN}$", "$\\frac{MN}{NP}$", "$\\frac{MP}{NP}$"], 0, "$\\cot N = \\frac{MN}{MP}$."),
            lambda: ("Thương của cạnh kề chia cho cạnh đối của góc nhọn gọi là:", ["Côtang của góc đó", "Tang của góc đó", "Sin của góc đó", "Côsin của góc đó"], 0, "Côtang kết đoàn: kề trên đối."),
            lambda: ("Đại lượng $\\frac{\\cos \\alpha}{\\sin \\alpha}$ với góc nhọn $\\alpha$ bằng tỉ số nào?", ["$\\cot \\alpha$", "$\\tan \\alpha$", "$\\sin \\alpha$", "$\\cos \\alpha$"], 0, "$\\cot \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$.")
        ]),
        ("Giá trị sin 30 độ", "b11", [
            lambda: ("Giá trị lượng giác của $\\sin 30^\\circ$ bằng:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$1$"], 0, "Góc đặc biệt: $\\sin 30^\\circ = 1/2$."),
            lambda: ("Tính giá trị của biểu thức $\\sin 30^\\circ$:", ["$0,5$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$1$"], 0, "$\\sin 30^\\circ = 0,5 = 1/2$."),
            lambda: ("Khẳng định nào đúng về giá trị của $\\sin 30^\\circ$?", ["Bằng $\\frac{1}{2}$", "Bằng $\\frac{\\sqrt{3}}{2}$", "Bằng $\\frac{\\sqrt{2}}{2}$", "Bằng 1"], 0, "$\\sin 30^\\circ = 1/2$."),
            lambda: ("Góc nhọn có sin bằng $\\frac{1}{2}$ có số đo là:", ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$"], 0, "Góc đó là $30^\\circ$."),
            lambda: ("Cho góc $\\alpha = 30^\\circ$. Khi đó giá trị của $\\sin \\alpha$ là:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{3}}{3}$", "$\\sqrt{3}$"], 0, "$\\sin 30^\\circ = 1/2$.")
        ]),
        ("Giá trị cos 60 độ", "b11", [
            lambda: ("Giá trị lượng giác của $\\cos 60^\\circ$ bằng:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$0$"], 0, "Góc đặc biệt: $\\cos 60^\\circ = 1/2$."),
            lambda: ("Tính giá trị của biểu thức $\\cos 60^\\circ$:", ["$0,5$", "$\\frac{\\sqrt{3}}{2}$", "$1$", "$\\frac{\\sqrt{2}}{2}$"], 0, "$\\cos 60^\\circ = 0,5$."),
            lambda: ("Khẳng định nào đúng về giá trị của $\\cos 60^\\circ$?", ["Bằng $\\frac{1}{2}$", "Bằng $\\frac{\\sqrt{3}}{2}$", "Bằng $\\frac{\\sqrt{3}}{3}$", "Bằng 0"], 0, "$\\cos 60^\\circ = 1/2$."),
            lambda: ("Góc nhọn có côsin bằng $\\frac{1}{2}$ có số đo bằng:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$0^\\circ$"], 0, "Đó là góc $60^\\circ$."),
            lambda: ("Cho góc $\\beta = 60^\\circ$. Giá trị của $\\cos \\beta$ là:", ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$1$"], 0, "$\\cos 60^\\circ = 1/2$.")
        ]),
        ("Giá trị tan 45 độ", "b11", [
            lambda: ("Giá trị của $\\tan 45^\\circ$ bằng:", ["$1$", "$\\sqrt{3}$", "$\\frac{\\sqrt{3}}{3}$", "$0$"], 0, "Tam giác vuông cân có góc $45^\\circ$, hai cạnh góc vuông bằng nhau nên $\\tan 45^\\circ = 1$."),
            lambda: ("Tính giá trị của biểu thức $\\tan 45^\\circ$ thu được:", ["$1$", "$\\frac{1}{2}$", "$\\sqrt{2}$", "$\\frac{\\sqrt{2}}{2}$"], 0, "$\\tan 45^\\circ = 1$."),
            lambda: ("Góc nhọn nào có giá trị tang bằng 1?", ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$90^\\circ$"], 0, "Góc $45^\\circ$ có $\\tan 45^\\circ = 1$."),
            lambda: ("Giá trị của $\\cot 45^\\circ$ bằng:", ["$1$", "$\\sqrt{3}$", "$\\frac{\\sqrt{3}}{3}$", "$0$"], 0, "$\\cot 45^\\circ = 1 / \\tan 45^\\circ = 1$."),
            lambda: ("Khẳng định nào đúng về $\\tan 45^\\circ$?", ["Bằng 1", "Bằng $\\sqrt{3}$", "Bằng $\\frac{1}{\\sqrt{3}}$", "Bằng 0"], 0, "$\\tan 45^\\circ = 1$.")
        ]),
        ("Đẳng thức lượng giác cơ bản", "b11", [
            lambda: ("Với mọi góc nhọn $\\alpha$, giá trị của $\\sin^2 \\alpha + \\cos^2 \\alpha$ bằng:", ["$1$", "$0$", "$2$", "$-1$"], 0, "Đẳng thức lượng giác cơ bản: $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$."),
            lambda: ("Tính giá trị của biểu thức $\\sin^2 25^\\circ + \\cos^2 25^\\circ$:", ["$1$", "$2$", "$0$", "$0,5$"], 0, "$\\sin^2 25^\\circ + \\cos^2 25^\\circ = 1$."),
            lambda: ("Biểu thức $\\sin^2 40^\\circ + \\cos^2 40^\\circ$ có giá trị bằng:", ["$1$", "$\\sin 80^\\circ$", "$\\cos 80^\\circ$", "$0$"], 0, "Bằng 1."),
            lambda: ("Kết quả của phép tính $\\sin^2 70^\\circ + \\cos^2 70^\\circ$ là:", ["$1$", "$2$", "$-1$", "$0$"], 0, "Bằng 1."),
            lambda: ("Đẳng thức nào sau đây luôn đúng với góc nhọn x?", ["$\\sin^2 x + \\cos^2 x = 1$", "$\\sin^2 x - \\cos^2 x = 1$", "$\\sin x + \\cos x = 1$", "$\\sin^2 x + \\cos^2 x = 2$"], 0, "$\\sin^2 x + \\cos^2 x = 1$.")
        ]),
        ("Tích tan và cot", "b11", [
            lambda: ("Với góc nhọn $\\alpha$, tích $\\tan \\alpha \\cdot \\cot \\alpha$ bằng:", ["$1$", "$0$", "$2$", "$\\sin \\alpha$"], 0, "Vì $\\cot \\alpha = 1/\\tan \\alpha$ nên tích bằng 1."),
            lambda: ("Tính giá trị của $\\tan 35^\\circ \\cdot \\cot 35^\\circ$:", ["$1$", "$0$", "$2$", "$0,5$"], 0, "Tích của tang và côtang cùng một góc luôn bằng 1."),
            lambda: ("Biểu thức $\\tan 50^\\circ \\cdot \\cot 50^\\circ$ có giá trị là:", ["$1$", "$2$", "$0$", "$-1$"], 0, "Bằng 1."),
            lambda: ("Kết quả của $\\tan 65^\\circ \\cdot \\cot 65^\\circ$ bằng:", ["$1$", "$\\tan 130^\\circ$", "$0$", "$\\cot 130^\\circ$"], 0, "Bằng 1."),
            lambda: ("Khẳng định nào đúng về tích $\\tan x \\cdot \\cot x$ với góc nhọn x?", ["Luôn bằng 1", "Luôn bằng 0", "Thay đổi theo x", "Luôn bằng 2"], 0, "Luôn bằng 1.")
        ]),
        ("Hệ thức cạnh và góc qua sin", "b12", [
            lambda: ("Trong tam giác vuông $ABC$ vuông tại $A$ có cạnh huyền a, cạnh góc vuông b tính theo $\\sin B$ là:", ["$b = a \\cdot \\sin B$", "$b = a \\cdot \\cos B$", "$b = a \\cdot \\tan B$", "$b = a / \\sin B$"], 0, "Cạnh góc vuông bằng cạnh huyền nhân sin góc đối: $b = a \\cdot \\sin B$."),
            lambda: ("Công thức nào đúng để tính cạnh góc vuông qua cạnh huyền và góc đối?", ["Cạnh góc vuông = Cạnh huyền $\\times$ sin góc đối", "Cạnh góc vuông = Cạnh huyền $\\times$ cos góc đối", "Cạnh góc vuông = Cạnh huyền $\\times$ tan góc đối", "Cạnh góc vuông = Cạnh huyền / sin góc đối"], 0, "Theo hệ thức lượng trong tam giác vuông."),
            lambda: ("Trong tam giác vuông $MNP$ vuông tại $M$, cạnh $MP$ tính theo cạnh huyền $NP$ và góc $N$ là:", ["$MP = NP \\cdot \\sin N$", "$MP = NP \\cdot \\cos N$", "$MP = NP \\cdot \\tan N$", "$MP = NP / \\sin N$"], 0, "$MP$ đối diện góc $N$ nên $MP = NP \\cdot \\sin N$."),
            lambda: ("Cho tam giác vuông $ABC$ (vuông tại $A$). Độ dài cạnh $AC$ được tính bằng:", ["$BC \\cdot \\sin B$", "$BC \\cdot \\cos B$", "$BC \\cdot \\tan B$", "$AB \\cdot \\sin B$"], 0, "$AC = BC \\cdot \\sin B$."),
            lambda: ("Hệ thức giữa cạnh góc vuông c và cạnh huyền a với góc C trong tam giác vuông là:", ["$c = a \\cdot \\cos C$", "$c = a \\cdot \\sin C$", "$c = a \\cdot \\tan C$", "$c = a / \\cos C$"], 0, "$c$ kề với góc $C$ nên $c = a \\cdot \\cos C$.")
        ]),
        ("Hệ thức cạnh và góc qua tan", "b12", [
            lambda: ("Trong tam giác vuông $ABC$ vuông tại $A$, cạnh góc vuông b tính theo cạnh c và góc B là:", ["$b = c \\cdot \\tan B$", "$b = c \\cdot \\cot B$", "$b = c \\cdot \\sin B$", "$b = c \\cdot \\cos B$"], 0, "Cạnh góc vuông này bằng cạnh góc vuông kia nhân tang góc đối: $b = c \\cdot \\tan B$."),
            lambda: ("Cho tam giác vuông có hai cạnh góc vuông $b, c$. Hệ thức nào sau đây đúng?", ["$b = c \\cdot \\tan B$", "$b = c / \\tan B$", "$b = c \\cdot \\sin B$", "$b = c \\cdot \\cos B$"], 0, "$b = c \\cdot \\tan B$."),
            lambda: ("Trong tam giác $ABC$ vuông tại $A$, cạnh $AC$ được tính theo cạnh $AB$ và góc $C$ là:", ["$AC = AB \\cdot \\cot C$", "$AC = AB \\cdot \\tan C$", "$AC = AB \\cdot \\sin C$", "$AC = AB \\cdot \\cos C$"], 0, "$AC = AB \\cdot \\cot C$ (nhân với côtang góc kề)."),
            lambda: ("Hệ thức nào sau đây tính cạnh góc vuông qua cạnh góc vuông kia và góc kề?", ["Bằng cạnh góc vuông kia nhân côtang góc kề", "Bằng cạnh góc vuông kia nhân tang góc kề", "Bằng cạnh góc vuông kia nhân sin góc kề", "Bằng cạnh góc vuông kia nhân côsin góc kề"], 0, "Cạnh góc vuông = Cạnh kia $\\times \\cot$ góc kề."),
            lambda: ("Trong tam giác vuông $DEF$ vuông tại $D$, cạnh $DF$ tính theo $DE$ và góc $E$ là:", ["$DF = DE \\cdot \\tan E$", "$DF = DE \\cdot \\cot E$", "$DF = DE / \\tan E$", "$DF = DE \\cdot \\sin E$"], 0, "$DF = DE \\cdot \\tan E$.")
        ]),
        ("Hai góc phụ nhau", "b11", [
            lambda: ("Nếu hai góc $\\alpha$ và $\\beta$ phụ nhau ($\\alpha + \\beta = 90^\\circ$) thì:", ["$\\sin \\alpha = \\cos \\beta$", "$\\sin \\alpha = \\sin \\beta$", "$\\tan \\alpha = \\tan \\beta$", "$\\cos \\alpha = -\\cos \\beta$"], 0, "Hai góc phụ nhau thì sin góc này bằng cosin góc kia."),
            lambda: ("Cho $\\alpha + \\beta = 90^\\circ$. Đẳng thức nào sau đây đúng?", ["$\\tan \\alpha = \\cot \\beta$", "$\\tan \\alpha = \\tan \\beta$", "$\\cot \\alpha = \\cos \\beta$", "$\\sin \\alpha = \\tan \\beta$"], 0, "Hai góc phụ nhau thì tang góc này bằng côtang góc kia."),
            lambda: ("Giá trị của $\\cos 70^\\circ$ bằng giá trị lượng giác nào sau đây?", ["$\\sin 20^\\circ$", "$\\sin 70^\\circ$", "$\\cos 20^\\circ$", "$\\tan 20^\\circ$"], 0, "Vì $70^\\circ + 20^\\circ = 90^\\circ$ nên $\\cos 70^\\circ = \\sin 20^\\circ$."),
            lambda: ("Giá trị của $\\tan 80^\\circ$ bằng:", ["$\\cot 10^\\circ$", "$\\tan 10^\\circ$", "$\\sin 10^\\circ$", "$\\cos 10^\\circ$"], 0, "Vì $80^\\circ + 10^\\circ = 90^\\circ$ nên $\\tan 80^\\circ = \\cot 10^\\circ$."),
            lambda: ("Cho góc $\\alpha = 15^\\circ$. Giá trị $\\sin 15^\\circ$ bằng:", ["$\\cos 75^\\circ$", "$\\cos 15^\\circ$", "$\\sin 75^\\circ$", "$\\tan 75^\\circ$"], 0, "Vì $15^\\circ + 75^\\circ = 90^\\circ$ nên $\\sin 15^\\circ = \\cos 75^\\circ$.")
        ])
    ]
    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c4-{len(mc)+1:03d}", "chapter": "c4", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    th_configs = [
        ("Tính tỉ số lượng giác trong tam giác cụ thể", "b11", [
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $AB = 3\\text{ cm}$, $AC = 4\\text{ cm}$. Giá trị của $\\sin B$ là:", ["$\\frac{4}{5}$", "$\\frac{3}{5}$", "$\\frac{4}{3}$", "$\\frac{3}{4}$"], 0, "Cạnh huyền $BC = \\sqrt{3^2 + 4^2} = 5$. Do đó $\\sin B = AC / BC = 4/5$."),
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}$, $AC = 8\\text{ cm}$. Giá trị của $\\cos B$ bằng:", ["$\\frac{3}{5}$", "$\\frac{4}{5}$", "$\\frac{3}{4}$", "$\\frac{4}{3}$"], 0, "Cạnh huyền $BC = 10$. Do đó $\\cos B = AB / BC = 6/10 = 3/5$."),
            lambda: ("Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}$, $AC = 12\\text{ cm}$. Giá trị $\\tan B$ là:", ["$\\frac{12}{5}$", "$\\frac{5}{12}$", "$\\frac{12}{13}$", "$\\frac{5}{13}$"], 0, "$\\tan B = AC / AB = 12/5$."),
            lambda: ("Tam giác vuông có hai cạnh góc vuông là 9 và 12. Cạnh huyền có độ dài bằng:", ["$15$", "$18$", "$21$", "$13$"], 0, "$\\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15$.")
        ]),
        ("Tính cạnh góc vuông khi biết cạnh huyền và góc", "b12", [
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $BC = 10\\text{ cm}$ và $\\angle B = 30^\\circ$. Độ dài cạnh $AC$ là:", ["$5\\text{ cm}$", "$5\\sqrt{3}\\text{ cm}$", "$10\\sqrt{3}\\text{ cm}$", "$8\\text{ cm}$"], 0, "$AC = BC \\cdot \\sin 30^\\circ = 10 \\cdot 0,5 = 5\\text{ cm}$."),
            lambda: ("Cho tam giác $ABC$ vuông tại $A$ có $BC = 12\\text{ cm}$ và $\\angle B = 60^\\circ$. Độ dài cạnh $AB$ bằng:", ["$6\\text{ cm}$", "$6\\sqrt{3}\\text{ cm}$", "$12\\sqrt{3}\\text{ cm}$", "$4\\text{ cm}$"], 0, "$AB = BC \\cdot \\cos 60^\\circ = 12 \\cdot 0,5 = 6\\text{ cm}$."),
            lambda: ("Tam giác vuông có cạnh huyền bằng $16\\text{ cm}$ và một góc nhọn bằng $30^\\circ$. Cạnh góc vuông đối diện góc đó dài:", ["$8\\text{ cm}$", "$8\\sqrt{3}\\text{ cm}$", "$4\\text{ cm}$", "$12\\text{ cm}$"], 0, "$b = 16 \\cdot \\sin 30^\\circ = 8\\text{ cm}$."),
            lambda: ("Tính cạnh góc vuông đối diện góc $30^\\circ$ trong tam giác vuông có cạnh huyền bằng $20\\text{ cm}$:", ["$10\\text{ cm}$", "$10\\sqrt{3}\\text{ cm}$", "$5\\text{ cm}$", "$15\\text{ cm}$"], 0, "$20 \\cdot \\sin 30^\\circ = 10\\text{ cm}$.")
        ]),
        ("Tính cạnh góc vuông khi biết cạnh kề và góc 45 độ", "b12", [
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}$ và $\\angle B = 45^\\circ$. Độ dài cạnh $AC$ là:", ["$6\\text{ cm}$", "$6\\sqrt{2}\\text{ cm}$", "$3\\text{ cm}$", "$12\\text{ cm}$"], 0, "Tam giác vuông cân tại A nên $AC = AB = 6\\text{ cm}$."),
            lambda: ("Cho tam giác $ABC$ vuông tại $A$ có $AB = 8\\text{ cm}$ và $\\angle C = 45^\\circ$. Độ dài cạnh $AC$ bằng:", ["$8\\text{ cm}$", "$8\\sqrt{2}\\text{ cm}$", "$4\\text{ cm}$", "$16\\text{ cm}$"], 0, "Vì $\\angle C = 45^\\circ$ nên tam giác vuông cân $\\Rightarrow AC = AB = 8\\text{ cm}$."),
            lambda: ("Một tam giác vuông có một góc nhọn bằng $45^\\circ$ và một cạnh góc vuông bằng $5\\text{ cm}$. Cạnh góc vuông còn lại dài:", ["$5\\text{ cm}$", "$5\\sqrt{2}\\text{ cm}$", "$2,5\\text{ cm}$", "$10\\text{ cm}$"], 0, "Hai cạnh góc vuông bằng nhau và bằng $5\\text{ cm}$."),
            lambda: ("Độ dài cạnh góc vuông của tam giác vuông cân có cạnh huyền bằng $6\\sqrt{2}\\text{ cm}$ là:", ["$6\\text{ cm}$", "$3\\text{ cm}$", "$12\\text{ cm}$", "$6\\sqrt{2}\\text{ cm}$"], 0, "$a = 6\\sqrt{2} / \\sqrt{2} = 6\\text{ cm}$.")
        ]),
        ("Tính cos khi biết sin", "b11", [
            lambda: ("Cho góc nhọn $\\alpha$ có $\\sin \\alpha = \\frac{3}{5}$. Giá trị của $\\cos \\alpha$ là:", ["$\\frac{4}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{5}$", "$\\frac{3}{4}$"], 0, "$\\cos \\alpha = \\sqrt{1 - (3/5)^2} = 4/5$."),
            lambda: ("Biết $\\sin x = \\frac{5}{13}$ với góc nhọn x. Giá trị của $\\cos x$ bằng:", ["$\\frac{12}{13}$", "$\\frac{8}{13}$", "$\\frac{1}{13}$", "$\\frac{12}{5}$"], 0, "$\\cos x = \\sqrt{1 - 25/169} = \\sqrt{144/169} = 12/13$."),
            lambda: ("Cho góc nhọn $\\beta$ có $\\cos \\beta = \\frac{4}{5}$. Giá trị của $\\sin \\beta$ là:", ["$\\frac{3}{5}$", "$\\frac{1}{5}$", "$\\frac{2}{5}$", "$\\frac{4}{3}$"], 0, "$\\sin \\beta = \\sqrt{1 - 16/25} = 3/5$."),
            lambda: ("Biết góc nhọn $\\alpha$ thoả mãn $\\sin \\alpha = 0,8$. Giá trị của $\\cos \\alpha$ bằng:", ["$0,6$", "$0,2$", "$0,4$", "$0,5$"], 0, "$\\cos \\alpha = \\sqrt{1 - 0,64} = \\sqrt{0,36} = 0,6$.")
        ]),
        ("Tính tan khi biết sin và cos", "b11", [
            lambda: ("Cho góc nhọn $\\alpha$ có $\\sin \\alpha = \\frac{3}{5}$ và $\\cos \\alpha = \\frac{4}{5}$. Giá trị $\\tan \\alpha$ bằng:", ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{3}{5}$", "$\\frac{4}{5}$"], 0, "$\\tan \\alpha = \\sin \\alpha / \\cos \\alpha = (3/5)/(4/5) = 3/4$."),
            lambda: ("Biết $\\sin x = \\frac{5}{13}$ và $\\cos x = \\frac{12}{13}$. Giá trị của $\\tan x$ là:", ["$\\frac{5}{12}$", "$\\frac{12}{5}$", "$\\frac{5}{13}$", "$\\frac{12}{13}$"], 0, "$\\tan x = 5/12$."),
            lambda: ("Cho góc nhọn có $\\sin \\alpha = 0,6$ và $\\cos \\alpha = 0,8$. Giá trị $\\cot \\alpha$ bằng:", ["$\\frac{4}{3}$", "$\\frac{3}{4}$", "$1$", "$0,8$"], 0, "$\\cot \\alpha = \\cos / \\sin = 0,8 / 0,6 = 4/3$."),
            lambda: ("Biết $\\tan \\alpha = 2$. Giá trị của $\\cot \\alpha$ bằng:", ["$\\frac{1}{2}$", "$2$", "$-2$", "$\\frac{1}{4}$"], 0, "$\\cot \\alpha = 1 / \\tan \\alpha = 1/2$.")
        ]),
        ("Ứng dụng thực tế tính chiều cao cây", "b12", [
            lambda: ("Một cái cây có bóng trên mặt đất dài 12 m khi góc tạo bởi tia nắng mặt trời và mặt đất bằng $45^\\circ$. Chiều cao của cây là:", ["$12\\text{ m}$", "$12\\sqrt{3}\\text{ m}$", "$6\\text{ m}$", "$24\\text{ m}$"], 0, "Chiều cao $h = 12 \\cdot \\tan 45^\\circ = 12\\text{ m}$."),
            lambda: ("Bóng của một cột cờ trên mặt đất dài 15 m khi góc nghiêng tia nắng bằng $45^\\circ$. Chiều cao của cột cờ là:", ["$15\\text{ m}$", "$15\\sqrt{3}\\text{ m}$", "$7,5\\text{ m}$", "$30\\text{ m}$"], 0, "Chiều cao $h = 15 \\cdot 1 = 15\\text{ m}$."),
            lambda: ("Một người đứng cách chân toà nhà 30 m và nhìn thấy đỉnh toà nhà dưới góc $45^\\circ$. Chiều cao toà nhà (bỏ qua chiều cao người) là:", ["$30\\text{ m}$", "$30\\sqrt{3}\\text{ m}$", "$15\\text{ m}$", "$60\\text{ m}$"], 0, "$h = 30 \\cdot \\tan 45^\\circ = 30\\text{ m}$."),
            lambda: ("Bóng của một tháp cao dài 20 m khi tia sáng mặt trời chiếu nghiêng một góc $45^\\circ$. Chiều cao của ngọn tháp bằng:", ["$20\\text{ m}$", "$20\\sqrt{3}\\text{ m}$", "$10\\text{ m}$", "$40\\text{ m}$"], 0, "Chiều cao $h = 20 \\cdot 1 = 20\\text{ m}$.")
        ]),
        ("Hệ thức lượng trong tam giác vuông: định lí đường cao", "b12", [
            lambda: ("Tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 4\\text{ cm}$ và $CH = 9\\text{ cm}$. Độ dài $AH$ là:", ["$6\\text{ cm}$", "$5\\text{ cm}$", "$7\\text{ cm}$", "$8\\text{ cm}$"], 0, "$AH^2 = BH \\cdot CH = 4 \\cdot 9 = 36 \\Rightarrow AH = 6\\text{ cm}$."),
            lambda: ("Trong tam giác vuông có hình chiếu hai cạnh góc vuông trên cạnh huyền là 1 cm và 4 cm. Độ dài đường cao ứng với cạnh huyền là:", ["$2\\text{ cm}$", "$4\\text{ cm}$", "$5\\text{ cm}$", "$1\\text{ cm}$"], 0, "$h = \\sqrt{1 \\cdot 4} = 2\\text{ cm}$."),
            lambda: ("Cho tam giác vuông có hai hình chiếu trên cạnh huyền là 9 cm và 16 cm. Đường cao ứng với cạnh huyền dài:", ["$12\\text{ cm}$", "$15\\text{ cm}$", "$25\\text{ cm}$", "$10\\text{ cm}$"], 0, "$h = \\sqrt{9 \\cdot 16} = 3 \\cdot 4 = 12\\text{ cm}$."),
            lambda: ("Tam giác vuông có hình chiếu hai cạnh góc vuông là 2 cm và 8 cm. Đường cao kẻ từ đỉnh góc vuông bằng:", ["$4\\text{ cm}$", "$16\\text{ cm}$", "$6\\text{ cm}$", "$10\\text{ cm}$"], 0, "$h = \\sqrt{2 \\cdot 8} = 4\\text{ cm}$.")
        ]),
        ("Hệ thức lượng cạnh góc vuông và hình chiếu", "b12", [
            lambda: ("Tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 2\\text{ cm}$, $BC = 8\\text{ cm}$. Độ dài cạnh $AB$ là:", ["$4\\text{ cm}$", "$16\\text{ cm}$", "$2\\sqrt{3}\\text{ cm}$", "$6\\text{ cm}$"], 0, "$AB^2 = BH \\cdot BC = 2 \\cdot 8 = 16 \\Rightarrow AB = 4\\text{ cm}$."),
            lambda: ("Trong tam giác vuông $ABC$ vuông tại $A$ có cạnh huyền $BC = 9\\text{ cm}$ và $BH = 4\\text{ cm}$. Cạnh góc vuông $AB$ dài:", ["$6\\text{ cm}$", "$36\\text{ cm}$", "$5\\text{ cm}$", "$8\\text{ cm}$"], 0, "$AB = \\sqrt{BH \\cdot BC} = \\sqrt{4 \\cdot 9} = 6\\text{ cm}$."),
            lambda: ("Cho tam giác vuông có cạnh huyền bằng 25 cm và hình chiếu cạnh góc vuông là 9 cm. Cạnh góc vuông đó dài:", ["$15\\text{ cm}$", "$12\\text{ cm}$", "$16\\text{ cm}$", "$20\\text{ cm}$"], 0, "$c = \\sqrt{9 \\cdot 25} = 3 \\cdot 5 = 15\\text{ cm}$."),
            lambda: ("Hình chiếu của cạnh góc vuông trên cạnh huyền dài 4 cm, cạnh huyền dài 16 cm. Cạnh góc vuông đó bằng:", ["$8\\text{ cm}$", "$64\\text{ cm}$", "$6\\text{ cm}$", "$12\\text{ cm}$"], 0, "$c = \\sqrt{4 \\cdot 16} = 8\\text{ cm}$.")
        ]),
        ("Tính diện tích tam giác vuông theo tỉ số lượng giác", "b12", [
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}$, $AC = 8\\text{ cm}$. Diện tích tam giác $ABC$ là:", ["$24\\text{ cm}^2$", "$48\\text{ cm}^2$", "$14\\text{ cm}^2$", "$20\\text{ cm}^2$"], 0, "$S = \\frac{1}{2} \\cdot 6 \\cdot 8 = 24\\text{ cm}^2$."),
            lambda: ("Diện tích của tam giác vuông có hai cạnh góc vuông là 5 cm và 10 cm bằng:", ["$25\\text{ cm}^2$", "$50\\text{ cm}^2$", "$15\\text{ cm}^2$", "$20\\text{ cm}^2$"], 0, "$S = \\frac{1}{2} \\cdot 5 \\cdot 10 = 25\\text{ cm}^2$."),
            lambda: ("Tam giác vuông cân có cạnh góc vuông bằng 4 cm. Diện tích tam giác bằng:", ["$8\\text{ cm}^2$", "$16\\text{ cm}^2$", "$4\\text{ cm}^2$", "$12\\text{ cm}^2$"], 0, "$S = \\frac{1}{2} \\cdot 4 \\cdot 4 = 8\\text{ cm}^2$."),
            lambda: ("Một tam giác vuông có cạnh huyền bằng 10 cm và đường cao ứng với cạnh huyền là 4 cm. Diện tích tam giác là:", ["$20\\text{ cm}^2$", "$40\\text{ cm}^2$", "$14\\text{ cm}^2$", "$24\\text{ cm}^2$"], 0, "$S = \\frac{1}{2} \\cdot 10 \\cdot 4 = 20\\text{ cm}^2$.")
        ]),
        ("Rút gọn biểu thức lượng giác phụ nhau", "b11", [
            lambda: ("Giá trị của biểu thức $P = \\sin 25^\\circ - \\cos 65^\\circ$ bằng:", ["$0$", "$1$", "$2\\sin 25^\\circ$", "$-1$"], 0, "Vì $25^\\circ + 65^\\circ = 90^\\circ$ nên $\\cos 65^\\circ = \\sin 25^\\circ \\Rightarrow P = 0$."),
            lambda: ("Tính giá trị của biểu thức $Q = \\tan 40^\\circ - \\cot 50^\\circ$:", ["$0$", "$1$", "$2$", "$-1$"], 0, "Vì $\\cot 50^\\circ = \\tan 40^\\circ$ nên hiệu bằng 0."),
            lambda: ("Kết quả của phép tính $\\cos 15^\\circ - \\sin 75^\\circ$ là:", ["$0$", "$1$", "$\\sqrt{3}$", "$0,5$"], 0, "$\\cos 15^\\circ = \\sin 75^\\circ \\Rightarrow$ hiệu bằng 0."),
            lambda: ("Biểu thức $\\frac{\\sin 20^\\circ}{\\cos 70^\\circ}$ có giá trị bằng:", ["$1$", "$0$", "$\\tan 20^\\circ$", "$\\cot 70^\\circ$"], 0, "Vì $\\sin 20^\\circ = \\cos 70^\\circ$ nên thương bằng 1.")
        ]),
        ("Tính góc nhọn khi biết hai cạnh góc vuông", "b11", [
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $AB = 3$ và $AC = 3\\sqrt{3}$. Số đo góc $\\angle B$ là:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$90^\\circ$"], 0, "$\\tan B = AC / AB = 3\\sqrt{3} / 3 = \\sqrt{3} \\Rightarrow \\angle B = 60^\\circ$."),
            lambda: ("Cho tam giác $ABC$ vuông tại $A$ có $AB = 4\\sqrt{3}$ và $AC = 4$. Số đo góc $\\angle B$ bằng:", ["$30^\\circ$", "$60^\\circ$", "$45^\\circ$", "$15^\\circ$"], 0, "$\\tan B = AC / AB = 4 / (4\\sqrt{3}) = 1/\\sqrt{3} \\Rightarrow \\angle B = 30^\\circ$."),
            lambda: ("Tam giác vuông có hai cạnh góc vuông bằng nhau thì các góc nhọn có số đo là:", ["$45^\\circ$", "$30^\\circ$", "$60^\\circ$", "$50^\\circ$"], 0, "Tam giác vuông cân có hai góc nhọn bằng $45^\\circ$."),
            lambda: ("Trong tam giác vuông, nếu cạnh đối bằng nửa cạnh huyền thì góc đối có số đo:", ["$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$"], 0, "$\\sin = 1/2 \\Rightarrow$ góc bằng $30^\\circ$.")
        ]),
        ("Tính độ dài thang dựa vào tường", "b12", [
            lambda: ("Một chiếc thang dài L dựa vào tường tạo với mặt đất góc $60^\\circ$. Chân thang cách tường 3 m. Độ dài thang là:", ["$6\\text{ m}$", "$3\\sqrt{3}\\text{ m}$", "$3\\text{ m}$", "$12\\text{ m}$"], 0, "Khoảng cách $d = L \\cdot \\cos 60^\\circ \\Rightarrow 3 = L \\cdot 0,5 \\Rightarrow L = 6\\text{ m}$."),
            lambda: ("Một thang dựa vào tường có góc nghiêng so với mặt đất bằng $60^\\circ$. Biết chân thang cách tường 2 m. Chiều dài thang bằng:", ["$4\\text{ m}$", "$2\\sqrt{3}\\text{ m}$", "$2\\text{ m}$", "$8\\text{ m}$"], 0, "$L = 2 / \\cos 60^\\circ = 4\\text{ m}$."),
            lambda: ("Chiếc thang dài 4 m dựa vào tường có chân thang cách tường 2 m. Góc tạo bởi thang và mặt đất là:", ["$60^\\circ$", "$30^\\circ$", "$45^\\circ$", "$75^\\circ$"], 0, "$\\cos \\alpha = 2/4 = 1/2 \\Rightarrow \\alpha = 60^\\circ$."),
            lambda: ("Một thang dài 5 m dựa vào tường có chân thang cách tường $2,5\\text{ m}$. Góc nghiêng của thang so với mặt đất bằng:", ["$60^\\circ$", "$45^\\circ$", "$30^\\circ$", "$50^\\circ$"], 0, "$\\cos \\alpha = 2,5 / 5 = 1/2 \\Rightarrow \\alpha = 60^\\circ$.")
        ])
    ]
    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c4-{len(mc)+1:03d}", "chapter": "c4", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    vd_configs = [
        ("Bài toán hai góc ngắm nâng cao", "b12", [
            lambda: ("Để tính chiều cao cột ăng-ten khi ngắm từ hai điểm trên mặt đất với góc nâng khác nhau, ta áp dụng:", ["Hệ thức lượng giữa cạnh và góc trong tam giác vuông", "Công thức chu vi hình tròn", "Định lí về góc nội tiếp", "Bất đẳng thức Cauchy"], 0, "Quy về việc giải hai tam giác vuông có chung đường cao cột ăng-ten."),
            lambda: ("Một máy bay đang bay ở độ cao h. Người quan sát nhìn thấy máy bay dưới góc nâng $\\alpha$. Khoảng cách từ người đến vị trí chiếu đứng của máy bay là:", ["$h \\cdot \\cot \\alpha$", "$h \\cdot \\tan \\alpha$", "$h \\cdot \\sin \\alpha$", "$h / \\sin \\alpha$"], 0, "Khoảng cách trên mặt đất là cạnh kề: $d = h \\cdot \\cot \\alpha$."),
            lambda: ("Từ đài quan sát ngắm hai chiếc thuyền trên biển thẳng hàng với chân đài. Ta tính khoảng cách giữa hai thuyền bằng cách:", ["Lấy hiệu khoảng cách từ chân đài đến từng thuyền", "Cộng khoảng cách hai thuyền", "Nhân hai khoảng cách", "Không tính được"], 0, "Khoảng cách giữa hai thuyền bằng hiệu hai khoảng cách từ chân đài đến mỗi thuyền."),
            lambda: ("Một khinh khí cầu đang bay. Góc nâng ngắm khinh khí cầu từ điểm A là $45^\\circ$, khoảng cách từ A đến vị trí mặt đất dưới khinh khí cầu là 100 m. Độ cao của khinh khí cầu là:", ["$100\\text{ m}$", "$100\\sqrt{3}\\text{ m}$", "$50\\text{ m}$", "$200\\text{ m}$"], 0, "Độ cao $h = 100 \\cdot \\tan 45^\\circ = 100\\text{ m}$.")
        ]),
        ("Chứng minh hệ thức lượng giác", "b11", [
            lambda: ("Giá trị của biểu thức $M = (1 - \\sin \\alpha)(1 + \\sin \\alpha) - \\cos^2 \\alpha$ bằng:", ["$0$", "$1$", "$-1$", "$2$"], 0, "$M = (1 - \\sin^2 \\alpha) - \\cos^2 \\alpha = \\cos^2 \\alpha - \\cos^2 \\alpha = 0$."),
            lambda: ("Rút gọn biểu thức $N = (1 - \\cos x)(1 + \\cos x) - \\sin^2 x$ ta được:", ["$0$", "$1$", "$2\\sin^2 x$", "$-1$"], 0, "$1 - \\cos^2 x - \\sin^2 x = \\sin^2 x - \\sin^2 x = 0$."),
            lambda: ("Biểu thức $K = \\tan^2 \\alpha - \\frac{1}{\\cos^2 \\alpha}$ có giá trị bằng:", ["$-1$", "$1$", "$0$", "$2$"], 0, "Ta có $1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha} \\Rightarrow \\tan^2 \\alpha - \\frac{1}{\\cos^2 \\alpha} = -1$."),
            lambda: ("Tính giá trị của $H = \\cot^2 \\alpha - \\frac{1}{\\sin^2 \\alpha}$:", ["$-1$", "$1$", "$0$", "$2$"], 0, "$1 + \\cot^2 \\alpha = \\frac{1}{\\sin^2 \\alpha} \\Rightarrow H = -1$.")
        ]),
        ("Bán kính đường tròn ngoại tiếp tam giác vuông", "b12", [
            lambda: ("Tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}$, $AC = 8\\text{ cm}$. Bán kính đường tròn ngoại tiếp tam giác là:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$4\\text{ cm}$", "$3\\text{ cm}$"], 0, "Cạnh huyền $BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Bán kính ngoại tiếp $R = BC / 2 = 5\\text{ cm}$."),
            lambda: ("Cho tam giác vuông có hai cạnh góc vuông là 5 cm và 12 cm. Bán kính đường tròn ngoại tiếp tam giác là:", ["$6,5\\text{ cm}$", "$13\\text{ cm}$", "$6\\text{ cm}$", "$7\\text{ cm}$"], 0, "Cạnh huyền bằng 13 cm $\\Rightarrow R = 13/2 = 6,5\\text{ cm}$."),
            lambda: ("Tam giác vuông có cạnh huyền bằng 16 cm. Bán kính đường tròn ngoại tiếp tam giác bằng:", ["$8\\text{ cm}$", "$16\\text{ cm}$", "$4\\text{ cm}$", "$12\\text{ cm}$"], 0, "$R = a / 2 = 16 / 2 = 8\\text{ cm}$."),
            lambda: ("Bán kính đường tròn ngoại tiếp tam giác vuông cân có cạnh góc vuông bằng $4\\sqrt{2}\\text{ cm}$ là:", ["$4\\text{ cm}$", "$8\\text{ cm}$", "$2\\text{ cm}$", "$4\\sqrt{2}\\text{ cm}$"], 0, "Cạnh huyền bằng $4\\sqrt{2} \\cdot \\sqrt{2} = 8\\text{ cm} \\Rightarrow R = 4\\text{ cm}$.")
        ])
    ]
    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c4-{len(mc)+1:03d}", "chapter": "c4", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    sa_nb = [
        ("Tính cạnh góc vuông cân", "b12", [
            ("Tam giác vuông cân tại A có $AB = 5\\text{ cm}$. Độ dài cạnh AC bằng bao nhiêu cm?", 5, "$AC = AB = 5\\text{ cm}$."),
            ("Cho tam giác vuông cân tại A có $AB = 7\\text{ cm}$. Cạnh AC dài bao nhiêu cm?", 7, "$AC = 7\\text{ cm}$."),
            ("Độ dài cạnh góc vuông thứ hai của tam giác vuông cân có một cạnh góc vuông bằng 9 cm là:", 9, "Bằng 9 cm."),
            ("Tam giác ABC vuông cân tại A có $AB = 11\\text{ cm}$. Cạnh AC dài:", 11, "$AC = 11\\text{ cm}$."),
            ("Cạnh góc vuông của tam giác vuông cân có cạnh bằng 15 cm là:", 15, "Bằng 15 cm.")
        ]),
        ("Tính tích đường cao và cạnh huyền", "b12", [
            ("Tam giác ABC vuông tại A có hai cạnh góc vuông là 3 và 4. Tích của đường cao AH và cạnh huyền BC bằng:", 12, "$AH \\cdot BC = AB \\cdot AC = 3 \\cdot 4 = 12$."),
            ("Cho tam giác vuông có hai cạnh góc vuông là 6 và 8. Tích đường cao ứng với cạnh huyền và cạnh huyền là:", 48, "$AB \\cdot AC = 6 \\cdot 8 = 48$."),
            ("Hai cạnh góc vuông của một tam giác vuông là 5 và 12. Tích cạnh huyền và đường cao bằng:", 60, "$5 \\cdot 12 = 60$."),
            ("Tam giác vuông có hai cạnh góc vuông dài 2 cm và 9 cm. Tích đường cao và cạnh huyền là:", 18, "$2 \\cdot 9 = 18$."),
            ("Tính tích của cạnh huyền và đường cao trong tam giác vuông có hai cạnh góc vuông là 4 và 5:", 20, "$4 \\cdot 5 = 20$.")
        ]),
        ("Tính tan 45 độ nguyên", "b11", [
            ("Tính giá trị của biểu thức $P = 7 \\cdot \\tan 45^\\circ$:", 7, "Vì $\\tan 45^\\circ = 1$ nên giá trị bằng 7."),
            ("Giá trị của $8 \\cdot \\cot 45^\\circ$ bằng bao nhiêu?", 8, "Vì $\\cot 45^\\circ = 1$ nên bằng 8."),
            ("Tính kết quả của $10 \\cdot \\tan 45^\\circ$:", 10, "Bằng 10."),
            ("Biểu thức $15 \\cdot \\tan 45^\\circ$ có giá trị là:", 15, "Bằng 15."),
            ("Tính $20 \\cdot \\cot 45^\\circ$ thu được:", 20, "Bằng 20.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c4-{len(sa)+1:03d}", "chapter": "c4", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Tính cạnh góc vuông theo góc 30 độ", "b12", [
            ("Tam giác vuông có cạnh huyền bằng 10 cm và một góc nhọn bằng $30^\\circ$. Cạnh góc vuông đối diện góc đó dài bao nhiêu cm?", 5, "$c = 10 \\cdot \\sin 30^\\circ = 5\\text{ cm}$."),
            ("Một tam giác vuông có cạnh huyền bằng 14 cm. Cạnh đối diện góc $30^\\circ$ có độ dài là:", 7, "$14 \\cdot 0,5 = 7\\text{ cm}$."),
            ("Tính cạnh đối diện góc $30^\\circ$ trong tam giác vuông có cạnh huyền bằng 18 cm:", 9, "$18 \\cdot 0,5 = 9\\text{ cm}$."),
            ("Cạnh huyền bằng 24 cm. Cạnh góc vuông đối diện góc $30^\\circ$ dài bao nhiêu cm?", 12, "$24 \\cdot 0,5 = 12\\text{ cm}$.")
        ]),
        ("Tính bình phương đường cao", "b12", [
            ("Tam giác vuông có hình chiếu hai cạnh góc vuông trên cạnh huyền là 4 cm và 9 cm. Bình phương đường cao ứng với cạnh huyền bằng:", 36, "$AH^2 = 4 \\cdot 9 = 36$."),
            ("Hình chiếu hai cạnh góc vuông trên cạnh huyền là 2 cm và 8 cm. Bình phương đường cao bằng:", 16, "$2 \\cdot 8 = 16$."),
            ("Cho hai hình chiếu trên cạnh huyền là 3 cm và 12 cm. Giá trị $AH^2$ bằng:", 36, "$3 \\cdot 12 = 36$."),
            ("Tính bình phương đường cao của tam giác vuông có hai hình chiếu trên cạnh huyền là 5 cm và 20 cm:", 100, "$5 \\cdot 20 = 100$.")
        ]),
        ("Tính giá trị biểu thức sin bình cộng cos bình", "b11", [
            ("Tính giá trị của biểu thức $A = 5 \\cdot (\\sin^2 35^\\circ + \\cos^2 35^\\circ)$:", 5, "Vì $\\sin^2 + \\cos^2 = 1$ nên giá trị bằng 5."),
            ("Giá trị của $B = 8 \\cdot (\\sin^2 50^\\circ + \\cos^2 50^\\circ)$ bằng bao nhiêu?", 8, "Bằng 8."),
            ("Tính $C = 12 \\cdot (\\sin^2 15^\\circ + \\cos^2 15^\\circ)$:", 12, "Bằng 12."),
            ("Biểu thức $D = 25 \\cdot (\\sin^2 72^\\circ + \\cos^2 72^\\circ)$ có giá trị là:", 25, "Bằng 25.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c4-{len(sa)+1:03d}", "chapter": "c4", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Tính cạnh huyền tam giác vuông nguyên", "b12", [
            ("Tam giác vuông có hai cạnh góc vuông là 6 cm và 8 cm. Độ dài cạnh huyền bằng bao nhiêu cm?", 10, "$\\sqrt{6^2 + 8^2} = 10\\text{ cm}$."),
            ("Tính độ dài cạnh huyền của tam giác vuông có hai cạnh góc vuông là 9 cm và 12 cm:", 15, "$\\sqrt{9^2 + 12^2} = 15\\text{ cm}$."),
            ("Một tam giác vuông có hai cạnh góc vuông dài 12 cm và 16 cm. Cạnh huyền dài bao nhiêu cm?", 20, "$\\sqrt{12^2 + 16^2} = 20\\text{ cm}$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c4-{len(sa)+1:03d}", "chapter": "c4", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b11", "sgk_title": "Bài 11. Tỉ số lượng giác của góc nhọn"},
        {"lesson_id": "b12", "sgk_title": "Bài 12. Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng"}
    ]
    save_bank("c4", "Hệ thức lượng trong tam giác vuông", lessons, mc, sa)
