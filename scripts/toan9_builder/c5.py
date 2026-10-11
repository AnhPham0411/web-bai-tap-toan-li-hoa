# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

# ==============================================================================
# CHƯƠNG 5: ĐƯỜNG TRÒN
# ==============================================================================
def gen_c5():
    mc, sa = [], []

    # 12 dạng NB x 5 câu = 60 câu
    nb_configs = [
        ("Vị trí của điểm đối với đường tròn", "b13", [
            lambda: ("Cho đường tròn $(O; 5\\text{ cm})$ và điểm $M$ có $OM = 3\\text{ cm}$. Vị trí của điểm $M$ so với đường tròn là:", ["Điểm $M$ nằm bên trong đường tròn", "Điểm $M$ nằm trên đường tròn", "Điểm $M$ nằm bên ngoài đường tròn", "Điểm $M$ trùng với tâm $O$"], 0, "Vì $OM = 3\\text{ cm} < R = 5\\text{ cm}$ nên điểm $M$ nằm bên trong đường tròn."),
            lambda: ("Cho đường tròn $(O; 4\\text{ cm})$ và điểm $A$ thoả mãn $OA = 6\\text{ cm}$. Điểm $A$ có vị trí:", ["Nằm bên ngoài đường tròn", "Nằm bên trong đường tròn", "Nằm trên đường tròn", "Là tâm đường tròn"], 0, "Vì $OA = 6\\text{ cm} > R = 4\\text{ cm}$ nên điểm $A$ nằm bên ngoài đường tròn."),
            lambda: ("Điểm $B$ được gọi là nằm trên đường tròn $(O; R)$ khi và chỉ khi khoảng cách $OB$ bằng:", ["$R$", "Lớn hơn $R$", "Nhỏ hơn $R$", "$2R$"], 0, "Theo định nghĩa, điểm nằm trên đường tròn khi khoảng cách từ điểm đó đến tâm bằng bán kính."),
            lambda: ("Cho đường tròn tâm $O$ bán kính $7\\text{ cm}$. Khoảng cách từ tâm đến điểm $K$ là $7\\text{ cm}$. Khi đó:", ["Điểm $K$ nằm trên đường tròn", "Điểm $K$ nằm trong đường tròn", "Điểm $K$ nằm ngoài đường tròn", "Điểm $K$ trùng với tâm $O$"], 0, "Vì $OK = R = 7\\text{ cm}$ nên $K$ thuộc đường tròn."),
            lambda: ("Điểm $P$ nằm bên trong đường tròn $(O; R)$ khi hệ thức nào sau đây được thoả mãn?", ["$OP < R$", "$OP > R$", "$OP = R$", "$OP \\ge R$"], 0, "Điểm nằm bên trong đường tròn khi khoảng cách đến tâm nhỏ hơn bán kính: $OP < R$.")
        ]),
        ("Khái niệm đường tròn và hình tròn", "b13", [
            lambda: ("Hình tròn tâm $O$ bán kính $R$ là hình gồm các điểm $M$ trong mặt phẳng thoả mãn:", ["$OM \\le R$", "$OM = R$", "$OM < R$", "$OM > R$"], 0, "Hình tròn bao gồm đường tròn và tất cả các điểm nằm bên trong đường tròn: $OM \\le R$."),
            lambda: ("Tập hợp tất cả các điểm cách điểm $O$ cố định một khoảng bằng $R$ ($R > 0$) gọi là:", ["Đường tròn tâm $O$ bán kính $R$", "Hình tròn tâm $O$ bán kính $R$", "Hình quạt tròn", "Hình vành khuyên"], 0, "Đó là định nghĩa đường tròn tâm $O$ bán kính $R$."),
            lambda: ("Đường tròn có bao nhiêu trục đối xứng?", ["Vô số trục đối xứng", "1 trục đối xứng", "2 trục đối xứng", "Không có trục đối xứng"], 0, "Bất kì đường thẳng nào đi qua tâm đều là trục đối xứng của đường tròn."),
            lambda: ("Tâm đối xứng của một đường tròn là:", ["Chính tâm của đường tròn đó", "Một điểm bất kì trên đường tròn", "Điểm nằm ngoài đường tròn", "Không có tâm đối xứng"], 0, "Tâm đối xứng của đường tròn chính là tâm của nó."),
            lambda: ("Đoạn thẳng nối hai điểm bất kì trên đường tròn được gọi là:", ["Dây cung của đường tròn", "Đường kính của đường tròn", "Bán kính của đường tròn", "Tiếp tuyến của đường tròn"], 0, "Đoạn thẳng nối hai điểm phân biệt thuộc đường tròn gọi là dây của đường tròn.")
        ]),
        ("Đường kính là dây lớn nhất", "b14", [
            lambda: ("Trong các dây của một đường tròn $(O; R)$, dây có độ dài lớn nhất là:", ["Đường kính", "Bán kính", "Dây vuông góc với bán kính", "Dây bất kì"], 0, "Định lí: Trong một đường tròn, đường kính là dây lớn nhất (có độ dài bằng $2R$)."),
            lambda: ("Độ dài của dây lớn nhất trong đường tròn bán kính $R$ bằng:", ["$2R$", "$R$", "$R\\sqrt{2}$", "$\\pi R$"], 0, "Dây lớn nhất là đường kính có độ dài $2R$."),
            lambda: ("Cho đường tròn $(O; 6\\text{ cm})$. Dây lớn nhất của đường tròn này có độ dài là:", ["$12\\text{ cm}$", "$6\\text{ cm}$", "$3\\text{ cm}$", "$18\\text{ cm}$"], 0, "Độ dài dây lớn nhất là đường kính $d = 2R = 2 \\times 6 = 12\\text{ cm}$."),
            lambda: ("Khẳng định nào đúng về độ dài dây cung $AB$ trong đường tròn $(O; R)$?", ["$AB \\le 2R$", "$AB > 2R$", "$AB = 2R$", "$AB < R$"], 0, "Mọi dây của đường tròn đều có độ dài không vượt quá đường kính: $AB \\le 2R$."),
            lambda: ("Khi dây cung $AB$ của đường tròn $(O)$ đi qua tâm $O$ thì $AB$ được gọi là:", ["Đường kính của đường tròn", "Bán kính của đường tròn", "Tiếp tuyến của đường tròn", "Cát tuyến của đường tròn"], 0, "Dây đi qua tâm chính là đường kính.")
        ]),
        ("Đường kính vuông góc với dây", "b14", [
            lambda: ("Trong một đường tròn, đường kính vuông góc với một dây thì:", ["Đi qua trung điểm của dây ấy", "Song song với dây ấy", "Bằng một nửa dây ấy", "Không cắt dây ấy"], 0, "Định lí: Trong một đường tròn, đường kính vuông góc với một dây thì đi qua trung điểm của dây ấy."),
            lambda: ("Cho đường tròn $(O)$, đường kính $AB$ vuông góc với dây $CD$ tại $H$. Khi đó:", ["$H$ là trung điểm của $CD$", "$H$ là trung điểm của $AB$", "$CD = AB$", "$CD = 2AB$"], 0, "Đường kính vuông góc với một dây thì đi qua trung điểm của dây đó."),
            lambda: ("Trong một đường tròn, đường kính đi qua trung điểm của một dây không đi qua tâm thì:", ["Vuông góc với dây ấy", "Song song với dây ấy", "Bằng dây ấy", "Cắt dây ấy tạo góc $45^\\circ$"], 0, "Định lí đảo: Đường kính đi qua trung điểm của dây không đi qua tâm thì vuông góc với dây đó."),
            lambda: ("Cho dây $MN$ không đi qua tâm $O$. Gọi $I$ là trung điểm của $MN$. Khẳng định nào đúng?", ["$OI \\perp MN$", "$OI \\parallel MN$", "$OI = MN$", "$OI = 2MN$"], 0, "Đoạn thẳng nối tâm với trung điểm của dây không đi qua tâm thì vuông góc với dây đó."),
            lambda: ("Đường thẳng đi qua tâm của đường tròn và vuông góc với một dây sẽ:", ["Chia dây đó thành hai đoạn bằng nhau", "Bằng một nửa dây đó", "Trùng với dây đó", "Song song với tiếp tuyến"], 0, "Đường thẳng qua tâm vuông góc với dây thì đi qua trung điểm của dây.")
        ]),
        ("Liên hệ giữa cung và dây", "b14", [
            lambda: ("Trong một đường tròn, hai cung bị chắn giữa hai dây song song thì:", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Không bằng nhau"], 0, "Định lí: Hai cung bị chắn giữa hai dây song song thì bằng nhau."),
            lambda: ("Trong một đường tròn, với hai cung nhỏ, cung lớn hơn căng dây:", ["Lớn hơn", "Nhỏ hơn", "Bằng nhau", "Gấp đôi"], 0, "Trong một đường tròn, cung lớn hơn căng dây lớn hơn."),
            lambda: ("Với hai cung nhỏ trong một đường tròn, hai dây bằng nhau căng hai cung:", ["Bằng nhau", "Không bằng nhau", "Bù nhau", "Phụ nhau"], 0, "Hai dây bằng nhau thì căng hai cung bằng nhau."),
            lambda: ("Khẳng định nào đúng về mối quan hệ giữa dây và cung trong một đường tròn?", ["Dây lớn hơn căng cung lớn hơn (với hai cung nhỏ)", "Dây lớn hơn căng cung nhỏ hơn", "Hai dây khác nhau luôn căng hai cung bằng nhau", "Dây luôn dài hơn cung"], 0, "Với hai cung nhỏ trong một đường tròn, dây lớn hơn căng cung lớn hơn."),
            lambda: ("Cho hai cung nhỏ $AB$ và $CD$ của đường tròn $(O)$. Nếu cung $AB$ bằng cung $CD$ thì:", ["$AB = CD$", "$AB > CD$", "$AB < CD$", "$AB = 2CD$"], 0, "Hai cung nhỏ bằng nhau thì căng hai dây bằng nhau: $AB = CD$.")
        ]),
        ("Liên hệ giữa dây và khoảng cách từ tâm đến dây", "b14", [
            lambda: ("Trong một đường tròn, hai dây bằng nhau thì:", ["Cách đều tâm", "Không cách đều tâm", "Luôn vuông góc với nhau", "Luôn song song với nhau"], 0, "Định lí: Trong một đường tròn, hai dây bằng nhau thì cách đều tâm."),
            lambda: ("Trong một đường tròn, hai dây cách đều tâm thì:", ["Bằng nhau", "Vuông góc với nhau", "Song song với nhau", "Có độ dài gấp đôi nhau"], 0, "Định lí đảo: Hai dây cách đều tâm thì bằng nhau."),
            lambda: ("Trong hai dây của một đường tròn, dây nào lớn hơn thì dây đó:", ["Gần tâm hơn", "Xa tâm hơn", "Cách đều tâm", "Đi qua tâm"], 0, "Dây lớn hơn thì khoảng cách từ tâm đến dây đó nhỏ hơn (gần tâm hơn)."),
            lambda: ("Cho hai dây $AB$ và $CD$ của đường tròn $(O)$ có khoảng cách đến tâm lần lượt là $d_1, d_2$. Nếu $d_1 < d_2$ thì:", ["$AB > CD$", "$AB < CD$", "$AB = CD$", "$AB = 2CD$"], 0, "Dây gần tâm hơn thì có độ dài lớn hơn: $d_1 < d_2 \\Rightarrow AB > CD$."),
            lambda: ("Nếu dây $AB$ gần tâm hơn dây $CD$ trong cùng một đường tròn thì:", ["Độ dài dây $AB$ lớn hơn độ dài dây $CD$", "Độ dài dây $AB$ nhỏ hơn độ dài dây $CD$", "Hai dây bằng nhau", "Không so sánh được"], 0, "Dây càng gần tâm thì càng dài, do đó $AB > CD$.")
        ]),
        ("Công thức chu vi đường tròn", "b15", [
            lambda: ("Công thức tính chu vi đường tròn bán kính $R$ là:", ["$C = 2\\pi R$", "$C = \\pi R^2$", "$C = 2\\pi R^2$", "$C = 4\\pi R$"], 0, "Chu vi đường tròn bán kính $R$ là $C = 2\\pi R$."),
            lambda: ("Nếu gọi $d$ là đường kính đường tròn, công thức tính chu vi là:", ["$C = \\pi d$", "$C = 2\\pi d$", "$C = \\pi d^2$", "$C = \\frac{\\pi d}{2}$"], 0, "Vì $d = 2R$ nên chu vi là $C = \\pi d$."),
            lambda: ("Khi bán kính của đường tròn tăng lên 2 lần thì chu vi của nó tăng lên:", ["2 lần", "4 lần", "Không đổi", "8 lần"], 0, "Vì $C = 2\\pi R$ tỉ lệ thuận bậc nhất với $R$, nên khi $R$ tăng 2 lần thì chu vi tăng 2 lần."),
            lambda: ("Chu vi của đường tròn có bán kính $R = 5\\text{ cm}$ bằng:", ["$10\\pi\\text{ cm}$", "$25\\pi\\text{ cm}$", "$5\\pi\\text{ cm}$", "$20\\pi\\text{ cm}$"], 0, "$C = 2\\pi R = 2\\pi \\times 5 = 10\\pi\\text{ cm}$."),
            lambda: ("Đường tròn có đường kính $8\\text{ cm}$ thì có chu vi là:", ["$8\\pi\\text{ cm}$", "$16\\pi\\text{ cm}$", "$64\\pi\\text{ cm}$", "$4\\pi\\text{ cm}$"], 0, "$C = \\pi d = 8\\pi\\text{ cm}$.")
        ]),
        ("Công thức diện tích hình tròn", "b15", [
            lambda: ("Công thức tính diện tích hình tròn bán kính $R$ là:", ["$S = \\pi R^2$", "$S = 2\\pi R$", "$S = 2\\pi R^2$", "$S = 4\\pi R^2$"], 0, "Diện tích hình tròn bán kính $R$ là $S = \\pi R^2$."),
            lambda: ("Khi bán kính đường tròn tăng lên gấp 3 lần thì diện tích hình tròn tăng lên:", ["9 lần", "3 lần", "6 lần", "27 lần"], 0, "Vì $S = \\pi R^2$, nên bán kính tăng 3 lần thì diện tích tăng $3^2 = 9$ lần."),
            lambda: ("Diện tích hình tròn có bán kính $R = 4\\text{ cm}$ bằng:", ["$16\\pi\\text{ cm}^2$", "$8\\pi\\text{ cm}^2$", "$4\\pi\\text{ cm}^2$", "$64\\pi\\text{ cm}^2$"], 0, "$S = \\pi R^2 = \\pi \\times 4^2 = 16\\pi\\text{ cm}^2$."),
            lambda: ("Tính diện tích hình tròn có đường kính $d = 6\\text{ cm}$:", ["$9\\pi\\text{ cm}^2$", "$36\\pi\\text{ cm}^2$", "$6\\pi\\text{ cm}^2$", "$12\\pi\\text{ cm}^2$"], 0, "Bán kính $R = d/2 = 3\\text{ cm}$. Diện tích $S = \\pi \\times 3^2 = 9\\pi\\text{ cm}^2$."),
            lambda: ("Công thức tính diện tích hình tròn theo đường kính $d$ là:", ["$S = \\frac{\\pi d^2}{4}$", "$S = \\pi d^2$", "$S = \\frac{\\pi d^2}{2}$", "$S = 2\\pi d$"], 0, "Thay $R = d/2$ vào công thức ta được $S = \\pi (d/2)^2 = \\frac{\\pi d^2}{4}$.")
        ]),
        ("Vị trí tương đối của đường thẳng và đường tròn khi d < R", "b16", [
            lambda: ("Nếu khoảng cách $d$ từ tâm $O$ đến đường thẳng $\\Delta$ nhỏ hơn bán kính $R$ ($d < R$) thì:", ["Đường thẳng cắt đường tròn tại 2 điểm", "Đường thẳng tiếp xúc với đường tròn", "Đường thẳng không cắt đường tròn", "Đường thẳng đi qua tâm"], 0, "Khi $d < R$, đường thẳng cắt đường tròn tại hai điểm phân biệt."),
            lambda: ("Đường thẳng cắt đường tròn tại 2 điểm phân biệt được gọi là:", ["Cát tuyến của đường tròn", "Tiếp tuyến của đường tròn", "Đường kính của đường tròn", "Trục đối xứng"], 0, "Đường thẳng cắt đường tròn tại 2 điểm phân biệt gọi là cát tuyến."),
            lambda: ("Cho đường tròn $(O; 6\\text{ cm})$ và khoảng cách từ tâm đến đường thẳng $a$ là $4\\text{ cm}$. Số điểm chung của $a$ và $(O)$ là:", ["2", "1", "0", "Vô số"], 0, "Vì $d = 4\\text{ cm} < R = 6\\text{ cm}$ nên đường thẳng cắt đường tròn tại 2 điểm."),
            lambda: ("Khi đường thẳng và đường tròn có 2 điểm chung thì mối liên hệ giữa $d$ và $R$ là:", ["$d < R$", "$d = R$", "$d > R$", "$d \\ge R$"], 0, "Có 2 điểm chung khi và chỉ khi $d < R$."),
            lambda: ("Đường thẳng đi qua tâm của đường tròn cắt đường tròn tại:", ["2 điểm phân biệt", "1 điểm duy nhất", "Không cắt điểm nào", "Vô số điểm"], 0, "Đường thẳng qua tâm có $d = 0 < R$ nên cắt đường tròn tại 2 điểm phân biệt (đối xứng qua tâm).")
        ]),
        ("Đường thẳng tiếp xúc với đường tròn và tiếp tuyến", "b16", [
            lambda: ("Đường thẳng $\\Delta$ tiếp xúc với đường tròn $(O; R)$ khi khoảng cách $d$ từ $O$ đến $\\Delta$ thoả mãn:", ["$d = R$", "$d < R$", "$d > R$", "$d = 2R$"], 0, "Đường thẳng tiếp xúc với đường tròn khi và chỉ khi khoảng cách từ tâm đến đường thẳng bằng bán kính ($d = R$)."),
            lambda: ("Đường thẳng chỉ có đúng 1 điểm chung với đường tròn được gọi là:", ["Tiếp tuyến của đường tròn", "Cát tuyến của đường tròn", "Đường kính của đường tròn", "Dây cung của đường tròn"], 0, "Đường thẳng tiếp xúc với đường tròn tại 1 điểm gọi là tiếp tuyến."),
            lambda: ("Điểm chung duy nhất giữa tiếp tuyến và đường tròn được gọi là:", ["Tiếp điểm", "Tâm tiếp xúc", "Giao điểm kép", "Đỉnh tiếp tuyến"], 0, "Điểm chung đó được gọi là tiếp điểm."),
            lambda: ("Cho đường tròn $(O; 5\\text{ cm})$ và đường thẳng $d$. Nếu khoảng cách từ $O$ đến $d$ là $5\\text{ cm}$ thì $d$ là:", ["Tiếp tuyến của đường tròn", "Cát tuyến của đường tròn", "Đường thẳng không cắt đường tròn", "Đường kính"], 0, "Vì $d = R = 5\\text{ cm}$ nên đường thẳng là tiếp tuyến."),
            lambda: ("Số điểm chung của tiếp tuyến với đường tròn là:", ["1", "2", "0", "Vô số"], 0, "Tiếp tuyến có đúng 1 điểm chung với đường tròn.")
        ]),
        ("Tính chất của tiếp tuyến và hai tiếp tuyến cắt nhau", "b16", [
            lambda: ("Nếu một đường thẳng là tiếp tuyến của một đường tròn thì nó:", ["Vuông góc với bán kính đi qua tiếp điểm", "Song song với bán kính đi qua tiếp điểm", "Đi qua tâm của đường tròn", "Trùng với bán kính"], 0, "Tính chất tiếp tuyến: Tiếp tuyến vuông góc với bán kính đi qua tiếp điểm."),
            lambda: ("Cho hai tiếp tuyến $MA$ và $MB$ của đường tròn $(O)$ ($A, B$ là các tiếp điểm). Khẳng định nào sau đây đúng?", ["$MA = MB$", "$MA > MB$", "$MA < MB$", "$MA = 2MB$"], 0, "Tính chất hai tiếp tuyến cắt nhau: Điểm xuất phát cách đều hai tiếp điểm ($MA = MB$)."),
            lambda: ("Từ điểm $M$ nằm ngoài đường tròn $(O)$, kẻ hai tiếp tuyến $MA$ và $MB$ ($A, B$ là tiếp điểm). Tia $MO$ là:", ["Tia phân giác của góc AMB", "Đường trung tuyến của tam giác AMB", "Đường thẳng vuông góc với AB tại M", "Tiếp tuyến thứ ba"], 0, "Tia $MO$ là tia phân giác của góc tạo bởi hai tiếp tuyến $\\angle AMB$."),
            lambda: ("Từ điểm $M$ nằm ngoài đường tròn kẻ hai tiếp tuyến $MA, MB$. Tia $OM$ là:", ["Tia phân giác của góc AOB", "Tia phân giác của góc MAB", "Đường cao tam giác OAB", "Tiếp tuyến của đường tròn"], 0, "Tia $OM$ là tia phân giác của góc ở tâm $\\angle AOB$."),
            lambda: ("Đoạn thẳng nối tâm $O$ và điểm $M$ ngoài đường tròn (với hai tiếp tuyến $MA, MB$) có tính chất:", ["Là đường trung trực của đoạn thẳng AB", "Song song với đoạn thẳng AB", "Bằng đoạn thẳng AB", "Không cắt đoạn thẳng AB"], 0, "Đoạn thẳng $OM$ là đường trung trực của dây tiếp xúc $AB$.")
        ]),
        ("Vị trí tương đối của hai đường tròn", "b17", [
            lambda: ("Hai đường tròn phân biệt $(O; R)$ và $(O'; r)$ cắt nhau thì số điểm chung của chúng là:", ["2", "1", "0", "Vô số"], 0, "Hai đường tròn cắt nhau có đúng 2 điểm chung phân biệt."),
            lambda: ("Hai đường tròn $(O; R)$ và $(O'; r)$ tiếp xúc ngoài khi khoảng cách đoạn nối tâm $d = OO'$ thoả mãn:", ["$d = R + r$", "$d = R - r$", "$d > R + r$", "$d < R - r$"], 0, "Hai đường tròn tiếp xúc ngoài khi khoảng cách nối tâm bằng tổng hai bán kính: $d = R + r$."),
            lambda: ("Hai đường tròn $(O; R)$ và $(O'; r)$ ($R > r$) tiếp xúc trong khi khoảng cách nối tâm $d = OO'$ bằng:", ["$d = R - r$", "$d = R + r$", "$d > R - r$", "$d < R - r$"], 0, "Hai đường tròn tiếp xúc trong khi khoảng cách nối tâm bằng hiệu hai bán kính: $d = R - r$."),
            lambda: ("Hai đường tròn ở ngoài nhau khi khoảng cách nối tâm $d$ thoả mãn:", ["$d > R + r$", "$d = R + r$", "$d < R + r$", "$d = R - r$"], 0, "Hai đường tròn ở ngoài nhau khi khoảng cách nối tâm lớn hơn tổng hai bán kính: $d > R + r$."),
            lambda: ("Hai đường tròn $(O; R)$ và $(O'; r)$ không giao nhau thì số điểm chung của chúng là:", ["0", "1", "2", "Vô số"], 0, "Không giao nhau nghĩa là không có điểm chung nào (0 điểm chung).")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c5-{len(mc)+1:03d}", "chapter": "c5", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 câu = 48 câu
    th_configs = [
        ("Tính khoảng cách từ tâm đến dây cung", "b14", [
            lambda: ("Cho đường tròn $(O; 10\\text{ cm})$ và dây $AB = 16\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây $AB$ là:", ["$6\\text{ cm}$", "$8\\text{ cm}$", "$5\\text{ cm}$", "$7\\text{ cm}$"], 0, "Kẻ $OH \\perp AB \\Rightarrow H$ là trung điểm $AB \\Rightarrow AH = 8\\text{ cm}$. Trong tam giác vuông $OAH$: $OH = \\sqrt{OA^2 - AH^2} = \\sqrt{10^2 - 8^2} = 6\\text{ cm}$."),
            lambda: ("Cho đường tròn $(O; 5\\text{ cm})$ và dây $CD = 8\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây $CD$ bằng:", ["$3\\text{ cm}$", "$4\\text{ cm}$", "$2\\text{ cm}$", "$5\\text{ cm}$"], 0, "Nửa dây là $4\\text{ cm}$. Khoảng cách $d = \\sqrt{5^2 - 4^2} = 3\\text{ cm}$."),
            lambda: ("Đường tròn tâm $O$ bán kính $13\\text{ cm}$ có dây cung dài $24\\text{ cm}$. Khoảng cách từ tâm đến dây đó là:", ["$5\\text{ cm}$", "$12\\text{ cm}$", "$7\\text{ cm}$", "$8\\text{ cm}$"], 0, "Nửa độ dài dây là $12\\text{ cm}$. Khoảng cách từ tâm là $\\sqrt{13^2 - 12^2} = \\sqrt{25} = 5\\text{ cm}$."),
            lambda: ("Cho đường tròn $(O; 25\\text{ cm})$ có dây cung dài $40\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây cung này là:", ["$15\\text{ cm}$", "$20\\text{ cm}$", "$10\\text{ cm}$", "$18\\text{ cm}$"], 0, "Nửa dây là $20\\text{ cm}$. Khoảng cách là $\\sqrt{25^2 - 20^2} = 15\\text{ cm}$.")
        ]),
        ("Tính độ dài dây cung khi biết bán kính và khoảng cách", "b14", [
            lambda: ("Cho đường tròn $(O; 5\\text{ cm})$, khoảng cách từ tâm $O$ đến dây $CD$ bằng $3\\text{ cm}$. Độ dài dây $CD$ là:", ["$8\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$", "$10\\text{ cm}$"], 0, "Kẻ $OK \\perp CD \\Rightarrow CK = \\sqrt{R^2 - OK^2} = \\sqrt{5^2 - 3^2} = 4\\text{ cm}$. Độ dài dây $CD = 2CK = 8\\text{ cm}$."),
            lambda: ("Đường tròn $(O; 10\\text{ cm})$ có khoảng cách từ tâm đến một dây bằng $6\\text{ cm}$. Độ dài của dây đó bằng:", ["$16\\text{ cm}$", "$8\\text{ cm}$", "$12\\text{ cm}$", "$14\\text{ cm}$"], 0, "Nửa dây là $\\sqrt{10^2 - 6^2} = 8\\text{ cm}$. Độ dài dây là $2 \\times 8 = 16\\text{ cm}$."),
            lambda: ("Cho đường tròn $(O; 15\\text{ cm})$. Một dây có khoảng cách đến tâm bằng $9\\text{ cm}$ thì có độ dài là:", ["$24\\text{ cm}$", "$12\\text{ cm}$", "$18\\text{ cm}$", "$20\\text{ cm}$"], 0, "Nửa dây là $\\sqrt{15^2 - 9^2} = 12\\text{ cm}$. Độ dài dây là $24\\text{ cm}$."),
            lambda: ("Đường tròn $(O; 17\\text{ cm})$ có khoảng cách từ tâm đến dây $MN$ bằng $8\\text{ cm}$. Chiều dài dây $MN$ là:", ["$30\\text{ cm}$", "$15\\text{ cm}$", "$25\\text{ cm}$", "$28\\text{ cm}$"], 0, "Nửa dây là $\\sqrt{17^2 - 8^2} = 15\\text{ cm}$. Chiều dài dây $MN = 2 \\times 15 = 30\\text{ cm}$.")
        ]),
        ("Tính độ dài cung tròn", "b15", [
            lambda: ("Độ dài cung $60^\\circ$ của đường tròn bán kính $R = 6\\text{ cm}$ là:", ["$2\\pi\\text{ cm}$", "$3\\pi\\text{ cm}$", "$4\\pi\\text{ cm}$", "$6\\pi\\text{ cm}$"], 0, "Công thức: $l = \\frac{\\pi R n}{180} = \\frac{\\pi \\times 6 \\times 60}{180} = 2\\pi\\text{ cm}$."),
            lambda: ("Độ dài cung $90^\\circ$ của đường tròn bán kính $R = 8\\text{ cm}$ bằng:", ["$4\\pi\\text{ cm}$", "$2\\pi\\text{ cm}$", "$8\\pi\\text{ cm}$", "$6\\pi\\text{ cm}$"], 0, "$l = \\frac{\\pi \\times 8 \\times 90}{180} = 4\\pi\\text{ cm}$."),
            lambda: ("Tính độ dài của cung $120^\\circ$ trên đường tròn bán kính $R = 9\\text{ cm}$:", ["$6\\pi\\text{ cm}$", "$3\\pi\\text{ cm}$", "$9\\pi\\text{ cm}$", "$12\\pi\\text{ cm}$"], 0, "$l = \\frac{\\pi \\times 9 \\times 120}{180} = 6\\pi\\text{ cm}$."),
            lambda: ("Cung có số đo $30^\\circ$ của đường tròn có bán kính $12\\text{ cm}$ dài bao nhiêu cm?", ["$2\\pi\\text{ cm}$", "$4\\pi\\text{ cm}$", "$\\pi\\text{ cm}$", "$3\\pi\\text{ cm}$"], 0, "$l = \\frac{\\pi \\times 12 \\times 30}{180} = 2\\pi\\text{ cm}$.")
        ]),
        ("Tính diện tích hình quạt tròn", "b15", [
            lambda: ("Diện tích hình quạt tròn bán kính $R = 6\\text{ cm}$, cung $90^\\circ$ là:", ["$9\\pi\\text{ cm}^2$", "$18\\pi\\text{ cm}^2$", "$6\\pi\\text{ cm}^2$", "$36\\pi\\text{ cm}^2$"], 0, "$S_q = \\frac{\\pi R^2 n}{360} = \\frac{\\pi \\times 6^2 \\times 90}{360} = 9\\pi\\text{ cm}^2$."),
            lambda: ("Một hình quạt tròn có bán kính $R = 6\\text{ cm}$ ứng với cung $60^\\circ$. Diện tích hình quạt tròn đó là:", ["$6\\pi\\text{ cm}^2$", "$12\\pi\\text{ cm}^2$", "$3\\pi\\text{ cm}^2$", "$18\\pi\\text{ cm}^2$"], 0, "$S_q = \\frac{\\pi \\times 36 \\times 60}{360} = 6\\pi\\text{ cm}^2$."),
            lambda: ("Tính diện tích hình quạt tròn bán kính $R = 4\\text{ cm}$ có số đo cung là $45^\\circ$:", ["$2\\pi\\text{ cm}^2$", "$4\\pi\\text{ cm}^2$", "$8\\pi\\text{ cm}^2$", "$\\pi\\text{ cm}^2$"], 0, "$S_q = \\frac{\\pi \\times 16 \\times 45}{360} = 2\\pi\\text{ cm}^2$."),
            lambda: ("Hình quạt tròn có bán kính $R = 10\\text{ cm}$ và cung $36^\\circ$ có diện tích bằng:", ["$10\\pi\\text{ cm}^2$", "$20\\pi\\text{ cm}^2$", "$5\\pi\\text{ cm}^2$", "$25\\pi\\text{ cm}^2$"], 0, "$S_q = \\frac{\\pi \\times 100 \\times 36}{360} = 10\\pi\\text{ cm}^2$.")
        ]),
        ("Tính diện tích hình vành khuyên", "b15", [
            lambda: ("Diện tích hình vành khuyên giới hạn bởi hai đường tròn đồng tâm có bán kính $R_1 = 5\\text{ cm}$ và $R_2 = 4\\text{ cm}$ là:", ["$9\\pi\\text{ cm}^2$", "$1\\pi\\text{ cm}^2$", "$41\\pi\\text{ cm}^2$", "$20\\pi\\text{ cm}^2$"], 0, "$S_{vk} = \\pi (R_1^2 - R_2^2) = \\pi (5^2 - 4^2) = \\pi (25 - 16) = 9\\pi\\text{ cm}^2$."),
            lambda: ("Cho hai đường tròn đồng tâm có bán kính $R = 10\\text{ cm}$ và $r = 8\\text{ cm}$. Diện tích hình vành khuyên giữa chúng là:", ["$36\\pi\\text{ cm}^2$", "$18\\pi\\text{ cm}^2$", "$64\\pi\\text{ cm}^2$", "$100\\pi\\text{ cm}^2$"], 0, "$S_{vk} = \\pi (10^2 - 8^2) = \\pi (100 - 64) = 36\\pi\\text{ cm}^2$."),
            lambda: ("Hình vành khuyên được tạo bởi hai đường tròn bán kính $R_1 = 13\\text{ cm}$ và $R_2 = 12\\text{ cm}$ có diện tích là:", ["$25\\pi\\text{ cm}^2$", "$5\\pi\\text{ cm}^2$", "$50\\pi\\text{ cm}^2$", "$1\\pi\\text{ cm}^2$"], 0, "$S = \\pi (13^2 - 12^2) = \\pi (169 - 144) = 25\\pi\\text{ cm}^2$."),
            lambda: ("Hai đường tròn đồng tâm có bán kính lần lượt là $6\\text{ cm}$ và $2\\text{ cm}$. Diện tích phần mặt phẳng nằm giữa hai đường tròn là:", ["$32\\pi\\text{ cm}^2$", "$16\\pi\\text{ cm}^2$", "$40\\pi\\text{ cm}^2$", "$8\\pi\\text{ cm}^2$"], 0, "$S = \\pi (6^2 - 2^2) = \\pi (36 - 4) = 32\\pi\\text{ cm}^2$.")
        ]),
        ("Xác định vị trí tương đối qua số liệu khoảng cách d và R", "b16", [
            lambda: ("Đường tròn $(O; 7\\text{ cm})$ và đường thẳng $\\Delta$ có khoảng cách từ tâm $d = 9\\text{ cm}$. Số điểm chung của $\\Delta$ và $(O)$ là:", ["$0$", "$1$", "$2$", "Vô số"], 0, "Vì khoảng cách $d = 9\\text{ cm} > R = 7\\text{ cm}$ nên đường thẳng và đường tròn không giao nhau (0 điểm chung)."),
            lambda: ("Cho đường tròn $(O; 8\\text{ cm})$ và khoảng cách từ tâm đến đường thẳng $m$ là $5\\text{ cm}$. Vị trí tương đối của $m$ và $(O)$ là:", ["Cắt nhau tại 2 điểm", "Tiếp xúc nhau", "Không giao nhau", "Trùng nhau"], 0, "Vì $d = 5\\text{ cm} < R = 8\\text{ cm}$ nên đường thẳng cắt đường tròn tại 2 điểm."),
            lambda: ("Đường tròn bán kính $R = 6\\text{ cm}$ có khoảng cách đến đường thẳng $d$ là $6\\text{ cm}$. Khẳng định nào đúng?", ["Đường thẳng tiếp xúc với đường tròn", "Đường thẳng cắt đường tròn", "Đường thẳng không cắt đường tròn", "Đường thẳng qua tâm đường tròn"], 0, "Vì khoảng cách $d = R = 6\\text{ cm}$ nên đường thẳng tiếp xúc với đường tròn."),
            lambda: ("Khoảng cách từ tâm $O$ của đường tròn $(O; 10\\text{ cm})$ đến đường thẳng $a$ là $12\\text{ cm}$. Khi đó đường thẳng $a$ và đường tròn $(O)$:", ["Không có điểm chung nào", "Có đúng 1 điểm chung", "Có 2 điểm chung phân biệt", "Có vô số điểm chung"], 0, "Vì $d > R$ nên không có điểm chung.")
        ]),
        ("Tính độ dài đoạn tiếp tuyến từ một điểm ngoài đường tròn", "b16", [
            lambda: ("Cho đường tròn $(O; 6\\text{ cm})$ và điểm $M$ sao cho $OM = 10\\text{ cm}$. Kẻ tiếp tuyến $MA$ ($A$ là tiếp điểm). Độ dài $MA$ là:", ["$8\\text{ cm}$", "$6\\text{ cm}$", "$16\\text{ cm}$", "$4\\text{ cm}$"], 0, "Tam giác $OAM$ vuông tại $A$ nên $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{10^2 - 6^2} = 8\\text{ cm}$."),
            lambda: ("Từ điểm $M$ cách tâm đường tròn $(O; 5\\text{ cm})$ một khoảng $13\\text{ cm}$, kẻ tiếp tuyến $MT$ ($T$ là tiếp điểm). Độ dài tiếp tuyến $MT$ là:", ["$12\\text{ cm}$", "$8\\text{ cm}$", "$10\\text{ cm}$", "$14\\text{ cm}$"], 0, "$MT = \\sqrt{13^2 - 5^2} = \\sqrt{144} = 12\\text{ cm}$."),
            lambda: ("Cho đường tròn $(O; 8\\text{ cm})$ và điểm $A$ ngoài đường tròn có $OA = 17\\text{ cm}$. Kẻ tiếp tuyến $AB$ với đường tròn. Độ dài $AB$ là:", ["$15\\text{ cm}$", "$12\\text{ cm}$", "$9\\text{ cm}$", "$16\\text{ cm}$"], 0, "$AB = \\sqrt{17^2 - 8^2} = \\sqrt{289 - 64} = 15\\text{ cm}$."),
            lambda: ("Điểm $P$ có khoảng cách đến tâm đường tròn $(O; 3\\text{ cm})$ bằng $5\\text{ cm}$. Độ dài đoạn tiếp tuyến kẻ từ $P$ đến đường tròn là:", ["$4\\text{ cm}$", "$2\\text{ cm}$", "$8\\text{ cm}$", "$6\\text{ cm}$"], 0, "Độ dài đoạn tiếp tuyến là $\\sqrt{5^2 - 3^2} = 4\\text{ cm}$.")
        ]),
        ("Tính góc ở tâm và số đo cung bị chắn", "b14", [
            lambda: ("Góc ở tâm $\\angle AOB = 50^\\circ$ chắn cung nhỏ $AB$. Số đo của cung nhỏ $AB$ là:", ["$50^\\circ$", "$100^\\circ$", "$25^\\circ$", "$130^\\circ$"], 0, "Số đo của cung nhỏ bằng số đo của góc ở tâm chắn cung đó: sđ $\\text{cung } AB = 50^\\circ$."),
            lambda: ("Góc ở tâm $\\angle AOB = 70^\\circ$ chắn cung nhỏ $AB$. Số đo của cung lớn $AB$ bằng:", ["$290^\\circ$", "$70^\\circ$", "$110^\\circ$", "$140^\\circ$"], 0, "Số đo cung lớn bằng $360^\\circ - 70^\\circ = 290^\\circ$."),
            lambda: ("Cung nhỏ $MN$ của đường tròn $(O)$ có số đo bằng $80^\\circ$. Số đo góc ở tâm $\\angle MON$ tương ứng là:", ["$80^\\circ$", "$40^\\circ$", "$160^\\circ$", "$100^\\circ$"], 0, "Góc ở tâm bằng số đo cung nhỏ bị chắn: $\\angle MON = 80^\\circ$."),
            lambda: ("Cho đường tròn $(O)$ có góc ở tâm $\\angle COD = 110^\\circ$. Số đo cung nhỏ $CD$ bằng:", ["$110^\\circ$", "$55^\\circ$", "$220^\\circ$", "$70^\\circ$"], 0, "Số đo cung nhỏ bằng đúng số đo góc ở tâm chắn cung đó: $110^\\circ$.")
        ]),
        ("Tam giác nội tiếp đường tròn có cạnh là đường kính", "b14", [
            lambda: ("Tam giác $ABC$ nội tiếp đường tròn $(O)$ có cạnh $BC$ là đường kính của đường tròn. Tam giác $ABC$ là:", ["Tam giác vuông tại $A$", "Tam giác đều", "Tam giác cân tại $A$", "Tam giác vuông tại $B$"], 0, "Định lí: Tam giác có một cạnh là đường kính của đường tròn ngoại tiếp thì tam giác đó vuông tại đỉnh đối diện với đường kính."),
            lambda: ("Cho tam giác $MNP$ nội tiếp đường tròn đường kính $NP$. Khẳng định nào sau đây đúng?", ["$\\angle M = 90^\\circ$", "$\\angle N = 90^\\circ$", "$\\angle P = 90^\\circ$", "Tam giác MNP cân tại M"], 0, "Góc nhìn đường kính $NP$ là góc vuông: $\\angle NMP = 90^\\circ$."),
            lambda: ("Tam giác $DEF$ nội tiếp đường tròn $(O)$ đường kính $EF = 10\\text{ cm}$. Nếu $DE = 6\\text{ cm}$ thì độ dài cạnh $DF$ là:", ["$8\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$", "$5\\text{ cm}$"], 0, "Vì tam giác $DEF$ vuông tại $D$, theo Pythagore: $DF = \\sqrt{EF^2 - DE^2} = \\sqrt{10^2 - 6^2} = 8\\text{ cm}$."),
            lambda: ("Tam giác $ABC$ có cạnh $BC = 2R$ là đường kính của đường tròn ngoại tiếp. Biết $AB = AC$. Tam giác $ABC$ là:", ["Tam giác vuông cân tại $A$", "Tam giác đều", "Tam giác vuông tại $B$", "Tam giác tù"], 0, "Tam giác vừa vuông tại $A$ vừa có $AB = AC$ nên là tam giác vuông cân tại $A$.")
        ]),
        ("Tính khoảng cách nối tâm hai đường tròn tiếp xúc", "b17", [
            lambda: ("Hai đường tròn $(O; 7\\text{ cm})$ và $(O'; 3\\text{ cm})$ tiếp xúc ngoài nhau. Đoạn nối tâm $OO'$ bằng:", ["$10\\text{ cm}$", "$4\\text{ cm}$", "$5\\text{ cm}$", "$21\\text{ cm}$"], 0, "Hai đường tròn tiếp xúc ngoài có khoảng cách nối tâm $d = R + r = 7 + 3 = 10\\text{ cm}$."),
            lambda: ("Hai đường tròn $(O; 8\\text{ cm})$ và $(O'; 5\\text{ cm})$ tiếp xúc trong nhau. Đoạn nối tâm $OO'$ bằng:", ["$3\\text{ cm}$", "$13\\text{ cm}$", "$4\\text{ cm}$", "$1,5\\text{ cm}$"], 0, "Hai đường tròn tiếp xúc trong có khoảng cách nối tâm $d = R - r = 8 - 5 = 3\\text{ cm}$."),
            lambda: ("Cho hai đường tròn bán kính $R = 9\\text{ cm}$ và $r = 4\\text{ cm}$ tiếp xúc ngoài. Chiều dài đoạn nối tâm là:", ["$13\\text{ cm}$", "$5\\text{ cm}$", "$36\\text{ cm}$", "$18\\text{ cm}$"], 0, "$d = R + r = 9 + 4 = 13\\text{ cm}$."),
            lambda: ("Đoạn nối tâm hai đường tròn bán kính $12\\text{ cm}$ và $7\\text{ cm}$ khi chúng tiếp xúc trong nhau là:", ["$5\\text{ cm}$", "$19\\text{ cm}$", "$8,5\\text{ cm}$", "$10\\text{ cm}$"], 0, "$d = R - r = 12 - 7 = 5\\text{ cm}$.")
        ]),
        ("Xác định số điểm chung của hai đường tròn qua R, r và d", "b17", [
            lambda: ("Hai đường tròn $(O; 5\\text{ cm})$ và $(O'; 3\\text{ cm})$ có khoảng cách nối tâm $OO' = 7\\text{ cm}$. Số điểm chung của hai đường tròn là:", ["$2$", "$1$", "$0$", "Vô số"], 0, "Vì $R - r = 2 < d = 7 < R + r = 8$ nên hai đường tròn cắt nhau tại 2 điểm."),
            lambda: ("Cho hai đường tròn $(O; 6\\text{ cm})$ và $(O'; 2\\text{ cm})$ có đoạn nối tâm $OO' = 10\\text{ cm}$. Hai đường tròn này có bao nhiêu điểm chung?", ["$0$", "$1$", "$2$", "Vô số"], 0, "Vì $d = 10 > R + r = 8$ nên hai đường tròn ở ngoài nhau, có 0 điểm chung."),
            lambda: ("Cho hai đường tròn $(O; 9\\text{ cm})$ và $(O'; 4\\text{ cm})$ có $OO' = 5\\text{ cm}$. Số điểm chung của hai đường tròn là:", ["$1$", "$2$", "$0$", "Vô số"], 0, "Vì $d = R - r = 9 - 4 = 5\\text{ cm}$ nên hai đường tròn tiếp xúc trong, có 1 điểm chung duy nhất."),
            lambda: ("Hai đường tròn có bán kính $4\\text{ cm}$ và $3\\text{ cm}$, khoảng cách giữa hai tâm là $1\\text{ cm}$. Vị trí tương đối của chúng là:", ["Tiếp xúc trong", "Tiếp xúc ngoài", "Cắt nhau", "Ở ngoài nhau"], 0, "Vì $d = R - r = 4 - 3 = 1\\text{ cm}$ nên hai đường tròn tiếp xúc trong.")
        ]),
        ("Tính góc tạo bởi hai tiếp tuyến cắt nhau", "b16", [
            lambda: ("Từ điểm $M$ ngoài đường tròn $(O)$, kẻ hai tiếp tuyến $MA, MB$. Biết góc ở tâm $\\angle AOB = 120^\\circ$. Góc $\\angle AMB$ bằng:", ["$60^\\circ$", "$120^\\circ$", "$30^\\circ$", "$90^\\circ$"], 0, "Tứ giác $OAMB$ có $\\angle A = \\angle B = 90^\\circ$ nên $\\angle AMB = 180^\\circ - \\angle AOB = 180^\\circ - 120^\\circ = 60^\\circ$."),
            lambda: ("Từ điểm $M$ kẻ hai tiếp tuyến $MA, MB$ tới đường tròn $(O)$. Biết $\\angle AMB = 50^\\circ$. Số đo góc ở tâm $\\angle AOB$ là:", ["$130^\\circ$", "$50^\\circ$", "$65^\\circ$", "$100^\\circ$"], 0, "Tổng hai góc đối diện bằng $180^\\circ$: $\\angle AOB = 180^\\circ - 50^\\circ = 130^\\circ$."),
            lambda: ("Cho hai tiếp tuyến $MA, MB$ tạo với nhau một góc $\\angle AMB = 80^\\circ$. Góc giữa bán kính $OA$ và tia $OM$ bằng:", ["$50^\\circ$", "$40^\\circ$", "$100^\\circ$", "$80^\\circ$"], 0, "Tia $MO$ là phân giác nên $\\angle AMO = 40^\\circ$. Tam giác $OAM$ vuông tại $A$ có $\\angle AOM = 90^\\circ - 40^\\circ = 50^\\circ$."),
            lambda: ("Từ điểm $P$ nằm ngoài đường tròn kẻ hai tiếp tuyến $PA, PB$. Biết góc $\\angle APB = 90^\\circ$. Tứ giác $OAPB$ là hình gì?", ["Hình vuông", "Hình chữ nhật có hai cạnh không bằng nhau", "Hình thang cân", "Hình thoi không là hình vuông"], 0, "Tứ giác có 3 góc vuông và hai cạnh kề bằng nhau ($OA = OB = R$) nên là hình vuông.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c5-{len(mc)+1:03d}", "chapter": "c5", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 câu = 12 câu
    vd_configs = [
        ("Tính độ dài dây cung đặc biệt liên quan góc và bán kính", "b14", [
            lambda: ("Dây $AB$ của đường tròn $(O; R)$ có khoảng cách đến tâm $O$ bằng $R / 2$. Độ dài dây $AB$ theo $R$ là:", ["$R\\sqrt{3}$", "$R$", "$R\\sqrt{2}$", "$2R$"], 0, "Kẻ $OH \\perp AB$ thì $AH = \\sqrt{R^2 - (R/2)^2} = \\sqrt{3R^2/4} = \\frac{R\\sqrt{3}}{2}$. Do đó $AB = 2AH = R\\sqrt{3}$."),
            lambda: ("Trong đường tròn $(O; R)$, góc ở tâm $\\angle AOB = 90^\\circ$. Độ dài dây $AB$ bằng:", ["$R\\sqrt{2}$", "$R\\sqrt{3}$", "$2R$", "$R$"], 0, "Tam giác $OAB$ vuông cân tại $O$ nên $AB = \\sqrt{OA^2 + OB^2} = \\sqrt{R^2 + R^2} = R\\sqrt{2}$."),
            lambda: ("Trong đường tròn $(O; R)$, tam giác $OAB$ là tam giác đều. Độ dài dây $AB$ bằng:", ["$R$", "$R\\sqrt{3}$", "$R\\sqrt{2}$", "$2R$"], 0, "Vì tam giác $OAB$ đều nên ba cạnh bằng nhau: $AB = OA = OB = R$."),
            lambda: ("Cho đường tròn $(O; 6\\text{ cm})$. Dây $CD$ có khoảng cách từ tâm đến dây bằng $3\\text{ cm}$. Chiều dài dây $CD$ là:", ["$6\\sqrt{3}\\text{ cm}$", "$3\\sqrt{3}\\text{ cm}$", "$6\\text{ cm}$", "$12\\text{ cm}$"], 0, "Nửa dây là $\\sqrt{6^2 - 3^2} = \\sqrt{27} = 3\\sqrt{3}\\text{ cm}$. Vậy $CD = 6\\sqrt{3}\\text{ cm}$.")
        ]),
        ("Tính bán kính đường tròn nội tiếp tam giác vuông", "b16", [
            lambda: ("Tam giác vuông có hai cạnh góc vuông là 6 và 8 (cạnh huyền là 10). Bán kính đường tròn nội tiếp $r$ bằng:", ["$2$", "$1$", "$3$", "$4$"], 0, "Công thức bán kính đường tròn nội tiếp tam giác vuông: $r = \\frac{a + b - c}{2} = \\frac{6 + 8 - 10}{2} = 2$."),
            lambda: ("Tam giác vuông có hai cạnh góc vuông lần lượt là $3\\text{ cm}$ và $4\\text{ cm}$. Bán kính đường tròn nội tiếp tam giác là:", ["$1\\text{ cm}$", "$2\\text{ cm}$", "$0,5\\text{ cm}$", "$1,5\\text{ cm}$"], 0, "Cạnh huyền là $5\\text{ cm}$. Bán kính nội tiếp $r = \\frac{3 + 4 - 5}{2} = 1\\text{ cm}$."),
            lambda: ("Tam giác vuông có các cạnh là 5, 12, 13. Bán kính đường tròn nội tiếp tam giác bằng:", ["$2$", "$3$", "$1$", "$4$"], 0, "Bán kính $r = \\frac{5 + 12 - 13}{2} = \\frac{4}{2} = 2$."),
            lambda: ("Cho tam giác vuông có hai cạnh góc vuông là 8 và 15. Bán kính đường tròn nội tiếp của tam giác là:", ["$3$", "$2$", "$4$", "$5$"], 0, "Cạnh huyền là $\\sqrt{8^2 + 15^2} = 17$. Bán kính $r = \\frac{8 + 15 - 17}{2} = \\frac{6}{2} = 3$.")
        ]),
        ("Ứng dụng thực tế về chu vi bánh xe và quãng đường", "b15", [
            lambda: ("Bánh xe đạp có đường kính $65\\text{ cm}$. Lấy $\\pi \\approx 3,14$. Khi bánh xe quay được 1000 vòng thì xe đi được quãng đường xấp xỉ:", ["$2041\\text{ m}$", "$1020\\text{ m}$", "$4082\\text{ m}$", "$650\\text{ m}$"], 0, "Chu vi bánh xe $C = \\pi d = 3,14 \\times 0,65\\text{ m} = 2,041\\text{ m}$. Quãng đường sau 1000 vòng là $1000 \\times 2,041 = 2041\\text{ m}$."),
            lambda: ("Một bánh xe có bán kính $0,25\\text{ m}$. Lấy $\\pi \\approx 3,14$. Sau khi lăn được 200 vòng thì bánh xe đi được quãng đường là:", ["$314\\text{ m}$", "$157\\text{ m}$", "$628\\text{ m}$", "$200\\text{ m}$"], 0, "Chu vi bánh xe $C = 2 \\times 3,14 \\times 0,25 = 1,57\\text{ m}$. Quãng đường $S = 200 \\times 1,57 = 314\\text{ m}$."),
            lambda: ("Bánh xe ô tô có đường kính $0,8\\text{ m}$. Lấy $\\pi \\approx 3,14$. Khi ô tô đi được quãng đường $2512\\text{ m}$ thì bánh xe đã quay khoảng:", ["$1000\\text{ vòng}$", "$500\\text{ vòng}$", "$2000\\text{ vòng}$", "$800\\text{ vòng}$"], 0, "Chu vi bánh xe $C = 3,14 \\times 0,8 = 2,512\\text{ m}$. Số vòng quay là $2512 / 2,512 = 1000\\text{ vòng}$."),
            lambda: ("Một con lăn hình trụ có bán kính $0,5\\text{ m}$. Lấy $\\pi \\approx 3,14$. Khi con lăn quay trọn 100 vòng trên mặt đất thì nó đã di chuyển được:", ["$314\\text{ m}$", "$628\\text{ m}$", "$157\\text{ m}$", "$500\\text{ m}$"], 0, "Chu vi $C = 2 \\times 3,14 \\times 0,5 = 3,14\\text{ m}$. Quãng đường $100 \\times 3,14 = 314\\text{ m}$.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c5-{len(mc)+1:03d}", "chapter": "c5", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb_configs = [
        ("Tính đường kính từ bán kính", "b13", [
            lambda: ("Cho đường tròn có bán kính $R = 5\\text{ cm}$. Độ dài đường kính của đường tròn là bao nhiêu cm?", 10, "Đường kính $d = 2R = 2 \\times 5 = 10\\text{ cm}$."),
            lambda: ("Một hình tròn có bán kính $R = 7\\text{ cm}$. Đường kính của hình tròn này bằng bao nhiêu cm?", 14, "Đường kính $d = 2R = 2 \\times 7 = 14\\text{ cm}$."),
            lambda: ("Đường tròn $(O)$ có bán kính $R = 12\\text{ cm}$. Dây lớn nhất của đường tròn có độ dài bao nhiêu cm?", 24, "Dây lớn nhất là đường kính: $2 \\times 12 = 24\\text{ cm}$."),
            lambda: ("Cho đường tròn tâm $O$ có bán kính $R = 15\\text{ cm}$. Đường kính của đường tròn là bao nhiêu cm?", 30, "$d = 2 \\times 15 = 30\\text{ cm}$."),
            lambda: ("Bán kính đường tròn bằng $20\\text{ cm}$. Độ dài đường kính của đường tròn đó là bao nhiêu cm?", 40, "$d = 2 \\times 20 = 40\\text{ cm}$.")
        ]),
        ("Số điểm chung của tiếp tuyến với đường tròn", "b16", [
            lambda: ("Số điểm chung của một tiếp tuyến với đường tròn là:", 1, "Tiếp tuyến tiếp xúc với đường tròn tại đúng 1 điểm duy nhất."),
            lambda: ("Một đường thẳng tiếp xúc với đường tròn tại bao nhiêu điểm?", 1, "Tiếp xúc tại đúng 1 điểm duy nhất."),
            lambda: ("Số tiếp điểm của một tiếp tuyến đối với đường tròn là:", 1, "Có đúng 1 tiếp điểm duy nhất."),
            lambda: ("Khi khoảng cách từ tâm đến đường thẳng bằng bán kính thì số giao điểm là:", 1, "Đường thẳng tiếp xúc với đường tròn nên có đúng 1 điểm chung."),
            lambda: ("Đường thẳng $\\Delta$ có $d = R$ so với đường tròn $(O)$. Số điểm chung của $\\Delta$ và $(O)$ là:", 1, "Có 1 điểm chung duy nhất.")
        ]),
        ("Số đo cung nửa đường tròn", "b14", [
            lambda: ("Số đo của cung nửa đường tròn bằng bao nhiêu độ?", 180, "Số đo của nửa đường tròn bằng $180^\\circ$."),
            lambda: ("Một góc ở tâm chắn nửa đường tròn có số đo bằng bao nhiêu độ?", 180, "Góc ở tâm là góc bẹt có số đo $180^\\circ$."),
            lambda: ("Đường kính chia đường tròn thành hai cung, mỗi cung có số đo bao nhiêu độ?", 180, "Mỗi cung nửa đường tròn có số đo $180^\\circ$."),
            lambda: ("Cung bị chắn bởi một đường kính của đường tròn có số đo bằng bao nhiêu độ?", 180, "Cung nửa đường tròn có số đo $180^\\circ$."),
            lambda: ("Hai đầu mút của một đường kính chia đường tròn thành hai cung, số đo mỗi cung là bao nhiêu độ?", 180, "Số đo mỗi cung bằng $180^\\circ$.")
        ])
    ]

    for dang, ls, gens in sa_nb_configs:
        for gen in gens:
            q, ans, ex = gen()
            sa.append({
                "id": f"sa-c5-{len(sa)+1:03d}", "chapter": "c5", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th_configs = [
        ("Tính khoảng cách từ tâm đến dây cung nguyên", "b14", [
            lambda: ("Đường tròn $(O; 5\\text{ cm})$ có dây $AB = 6\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây $AB$ bằng bao nhiêu cm?", 4, "Nửa dây là $3\\text{ cm}$. Khoảng cách là $\\sqrt{5^2 - 3^2} = 4\\text{ cm}$."),
            lambda: ("Đường tròn $(O; 10\\text{ cm})$ có dây cung dài $16\\text{ cm}$. Khoảng cách từ tâm đến dây này bằng bao nhiêu cm?", 6, "Nửa dây là $8\\text{ cm}$. Khoảng cách: $\\sqrt{10^2 - 8^2} = 6\\text{ cm}$."),
            lambda: ("Cho đường tròn $(O; 13\\text{ cm})$ và dây cung dài $10\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây là bao nhiêu cm?", 12, "Nửa dây là $5\\text{ cm}$. Khoảng cách: $\\sqrt{13^2 - 5^2} = 12\\text{ cm}$."),
            lambda: ("Đường tròn $(O; 25\\text{ cm})$ có dây cung dài $48\\text{ cm}$. Khoảng cách từ tâm $O$ đến dây đó là bao nhiêu cm?", 7, "Nửa dây là $24\\text{ cm}$. Khoảng cách: $\\sqrt{25^2 - 24^2} = 7\\text{ cm}$.")
        ]),
        ("Tính khoảng cách nối tâm hai đường tròn tiếp xúc ngoài", "b17", [
            lambda: ("Cho hai đường tròn tiếp xúc ngoài có bán kính là $4\\text{ cm}$ và $6\\text{ cm}$. Đoạn nối tâm $OO'$ dài bao nhiêu cm?", 10, "Đoạn nối tâm: $d = R + r = 4 + 6 = 10\\text{ cm}$."),
            lambda: ("Hai đường tròn tiếp xúc ngoài có bán kính lần lượt là $7\\text{ cm}$ và $8\\text{ cm}$. Khoảng cách giữa hai tâm bằng bao nhiêu cm?", 15, "Khoảng cách nối tâm: $7 + 8 = 15\\text{ cm}$."),
            lambda: ("Cho hai đường tròn tiếp xúc ngoài có bán kính $9\\text{ cm}$ và $11\\text{ cm}$. Độ dài đoạn nối tâm là bao nhiêu cm?", 20, "$d = 9 + 11 = 20\\text{ cm}$."),
            lambda: ("Khoảng cách nối tâm của hai đường tròn tiếp xúc ngoài có bán kính $12\\text{ cm}$ và $13\\text{ cm}$ bằng bao nhiêu cm?", 25, "$d = 12 + 13 = 25\\text{ cm}$.")
        ]),
        ("Độ dài đoạn tiếp tuyến vuông góc", "b16", [
            lambda: ("Cho đường tròn $(O; 3\\text{ cm})$ và điểm $M$ có $OM = 5\\text{ cm}$. Độ dài đoạn tiếp tuyến $MA$ bằng bao nhiêu cm?", 4, "$MA = \\sqrt{5^2 - 3^2} = 4\\text{ cm}$."),
            lambda: ("Từ điểm $A$ cách tâm đường tròn bán kính $6\\text{ cm}$ một khoảng $10\\text{ cm}$, kẻ tiếp tuyến $AB$. Độ dài $AB$ bằng bao nhiêu cm?", 8, "$AB = \\sqrt{10^2 - 6^2} = 8\\text{ cm}$."),
            lambda: ("Điểm $K$ cách tâm đường tròn bán kính $5\\text{ cm}$ một đoạn $13\\text{ cm}$. Chiều dài đoạn tiếp tuyến từ $K$ đến đường tròn là bao nhiêu cm?", 12, "Độ dài đoạn tiếp tuyến: $\\sqrt{13^2 - 5^2} = 12\\text{ cm}$."),
            lambda: ("Cho đường tròn $(O; 8\\text{ cm})$ và điểm $P$ thoả mãn $OP = 17\\text{ cm}$. Kẻ tiếp tuyến $PT$. Độ dài $PT$ bằng bao nhiêu cm?", 15, "$PT = \\sqrt{17^2 - 8^2} = 15\\text{ cm}$.")
        ])
    ]

    for dang, ls, gens in sa_th_configs:
        for gen in gens:
            q, ans, ex = gen()
            sa.append({
                "id": f"sa-c5-{len(sa)+1:03d}", "chapter": "c5", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd_configs = [
        ("Tính bán kính đường tròn nội tiếp tam giác vuông nguyên", "b16", [
            lambda: ("Tam giác vuông có hai cạnh góc vuông là 6 và 8 (cạnh huyền là 10). Bán kính đường tròn nội tiếp bằng bao nhiêu?", 2, "Bán kính: $r = (6 + 8 - 10) / 2 = 2$."),
            lambda: ("Tam giác vuông có hai cạnh góc vuông là 5 và 12 (cạnh huyền là 13). Bán kính đường tròn nội tiếp bằng bao nhiêu?", 2, "Bán kính: $r = (5 + 12 - 13) / 2 = 2$."),
            lambda: ("Tam giác vuông có hai cạnh góc vuông là 8 và 15 (cạnh huyền là 17). Bán kính đường tròn nội tiếp của tam giác bằng bao nhiêu?", 3, "Bán kính: $r = (8 + 15 - 17) / 2 = 3$.")
        ])
    ]

    for dang, ls, gens in sa_vd_configs:
        for gen in gens:
            q, ans, ex = gen()
            sa.append({
                "id": f"sa-c5-{len(sa)+1:03d}", "chapter": "c5", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b13", "sgk_title": "Bài 13. Mở đầu về đường tròn"},
        {"lesson_id": "b14", "sgk_title": "Bài 14. Cung và dây của một đường tròn"},
        {"lesson_id": "b15", "sgk_title": "Bài 15. Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên"},
        {"lesson_id": "b16", "sgk_title": "Bài 16. Vị trí tương đối của đường thẳng và đường tròn"},
        {"lesson_id": "b17", "sgk_title": "Bài 17. Vị trí tương đối của hai đường tròn"}
    ]
    save_bank("c5", "Đường tròn", lessons, mc, sa)
