# -*- coding: utf-8 -*-
from .common import make_unique_choices, save_bank

def gen_c4():
    mc, sa = [], []

    # 12 dạng NB x 5 biến thể = 60 câu
    nb_configs = [
        ("Xác định mặt phẳng trong không gian", "b10", [
            lambda: ("Có bao nhiêu mặt phẳng đi qua ba điểm không thẳng hàng?", ["$1$ mặt phẳng duy nhất", "$2$ mặt phẳng", "Vô số mặt phẳng", "$0$ mặt phẳng"], 0, "Qua ba điểm không thẳng hàng xác định duy nhất 1 mặt phẳng."),
            lambda: ("Một mặt phẳng được xác định duy nhất nếu biết:", ["Một đường thẳng và một điểm không thuộc đường thẳng đó", "Hai điểm phân biệt", "Ba điểm thẳng hàng", "Một đường thẳng duy nhất"], 0, "Một đường thẳng và một điểm nằm ngoài nó xác định một mặt phẳng duy nhất."),
            lambda: ("Qua hai đường thẳng cắt nhau có thể xác định được bao nhiêu mặt phẳng?", ["$1$ mặt phẳng", "$2$ mặt phẳng", "Vô số", "$0$"], 0, "Hai đường thẳng cắt nhau xác định duy nhất 1 mặt phẳng."),
            lambda: ("Hai đường thẳng song song phân biệt xác định được bao nhiêu mặt phẳng?", ["$1$ mặt phẳng", "$2$ mặt phẳng", "Vô số", "Không có mặt phẳng nào"], 0, "Hai đường thẳng song song xác định duy nhất 1 mặt phẳng."),
            lambda: ("Yếu tố nào sau đây KHÔNG đủ để xác định duy nhất một mặt phẳng?", ["Ba điểm thẳng hàng", "Ba điểm không thẳng hàng", "Hai đường thẳng cắt nhau", "Hai đường thẳng song song phân biệt"], 0, "Ba điểm thẳng hàng có vô số mặt phẳng đi qua.")
        ]),
        ("Giao tuyến của hai mặt phẳng", "b10", [
            lambda: ("Nếu hai mặt phẳng phân biệt có một điểm chung thì giao tuyến của chúng là:", ["Đường thẳng đi qua điểm chung đó", "Một đoạn thẳng", "Đúng một điểm", "Một tam giác"], 0, "Hai mặt phẳng phân biệt có điểm chung thì cắt nhau theo một đường thẳng đi qua điểm chung."),
            lambda: ("Trong hình chóp S.ABCD đáy là tứ giác lồi, giao tuyến của $(SAC)$ và $(SBD)$ là đường thẳng đi qua S và:", ["Giao điểm của AC và BD", "Điểm A", "Trung điểm của AB", "Điểm D"], 0, "Giao tuyến là $SO$ với $O = AC \\cap BD$."),
            lambda: ("Giao tuyến của mặt phẳng đáy $(ABCD)$ và mặt bên $(SAB)$ của hình chóp $S.ABCD$ là:", ["Đường thẳng AB", "Đường thẳng CD", "Đoạn thẳng SA", "Đường thẳng BC"], 0, "Hai mặt phẳng có chung hai điểm A và B nên giao tuyến là đường thẳng AB."),
            lambda: ("Cho hình tứ diện ABCD. Giao tuyến của hai mặt phẳng $(ABC)$ và $(ACD)$ là:", ["Đường thẳng AC", "Đường thẳng AB", "Đường thẳng CD", "Đường thẳng BC"], 0, "Hai mặt phẳng chung nhau cạnh AC."),
            lambda: ("Hai mặt phẳng phân biệt có thể có bao nhiêu điểm chung không thẳng hàng?", ["$0$", "$1$", "$2$", "$3$"], 0, "Nếu có 3 điểm chung không thẳng hàng thì hai mặt phẳng trùng nhau.")
        ]),
        ("Vị trí tương đối của hai đường thẳng", "b11", [
            lambda: ("Hai đường thẳng không có điểm chung và không cùng thuộc một mặt phẳng gọi là:", ["Hai đường thẳng chéo nhau", "Hai đường thẳng song song", "Hai đường thẳng cắt nhau", "Hai đường thẳng trùng nhau"], 0, "Định nghĩa hai đường thẳng chéo nhau."),
            lambda: ("Hai đường thẳng phân biệt cùng nằm trong một mặt phẳng có thể:", ["Cắt nhau hoặc song song", "Chéo nhau", "Trùng nhau", "Vuông góc mà không cắt nhau"], 0, "Khi đồng phẳng thì chỉ có thể cắt nhau hoặc song song."),
            lambda: ("Trong tứ diện ABCD, hai đường thẳng AB và CD là:", ["Chéo nhau", "Cắt nhau", "Song song", "Trùng nhau"], 0, "Trong tứ diện, hai cạnh đối diện luôn chéo nhau."),
            lambda: ("Số vị trí tương đối có thể có của hai đường thẳng phân biệt trong không gian là:", ["$3$ (cắt nhau, song song, chéo nhau)", "$2$", "$4$", "$1$"], 0, "Có 3 vị trí: cắt nhau, song song, chéo nhau."),
            lambda: ("Khẳng định nào đúng về hai đường thẳng chéo nhau?", ["Chúng không cùng nằm trên bất kì mặt phẳng nào", "Chúng có một điểm chung", "Chúng song song với nhau", "Chúng có thể trùng nhau"], 0, "Hai đường thẳng chéo nhau là không đồng phẳng.")
        ]),
        ("Định lí về ba mặt phẳng cắt nhau", "b11", [
            lambda: ("Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến đó:", ["Hoặc đồng quy, hoặc đôi một song song", "Luôn luôn đồng quy", "Luôn luôn đôi một song song", "Luôn luôn chéo nhau"], 0, "Định lí về giao tuyến của ba mặt phẳng."),
            lambda: ("Cho hai đường thẳng phân biệt $a$ và $b$ cùng song song với đường thẳng $c$. Khi đó:", ["$a \\parallel b$", "a cắt b", "a chéo b", "a trùng b"], 0, "Tính chất bắc cầu: hai đường thẳng phân biệt cùng song song với đường thứ ba thì song song với nhau."),
            lambda: ("Trong hình chóp $S.ABCD$ có đáy là hình bình hành. Giao tuyến của $(SAB)$ và $(SCD)$ là đường thẳng đi qua S và:", ["Song song với AB và CD", "Đi qua giao điểm của AC và BD", "Vuông góc với đáy", "Trùng với SA"], 0, "Do $AB \\parallel CD$ nên giao tuyến qua S và song song với AB, CD."),
            lambda: ("Cho ba mặt phẳng $(P), (Q), (R)$ cắt nhau theo 3 giao tuyến phân biệt. Nếu hai giao tuyến cắt nhau thì:", ["Giao tuyến thứ ba cũng đi qua điểm cắt đó (đồng quy)", "Giao tuyến thứ ba song song với hai giao tuyến kia", "Ba giao tuyến chéo nhau", "Không xác định"], 0, "Nếu hai giao tuyến cắt nhau thì cả 3 giao tuyến đồng quy."),
            lambda: ("Đường thẳng d song song với a, d' song song với a. Khi đó d và d' phân biệt sẽ:", ["Song song với nhau", "Cắt nhau", "Chéo nhau", "Vuông góc"], 0, "$d \\parallel d'$.")
        ]),
        ("Đường thẳng song song với mặt phẳng", "b12", [
            lambda: ("Đường thẳng d song song với mặt phẳng $(P)$ khi:", ["d và $(P)$ không có điểm chung", "d có duy nhất 1 điểm chung với $(P)$", "d nằm trong $(P)$", "d vuông góc với $(P)$"], 0, "Định nghĩa đường thẳng song song với mặt phẳng: không có điểm chung."),
            lambda: ("Điều kiện để đường thẳng $d$ song song với mặt phẳng $(P)$ là:", ["$d$ không nằm trong $(P)$ và $d$ song song với một đường thẳng $a \\subset (P)$", "$d$ có điểm chung với $(P)$", "$d$ cắt một đường thẳng trong $(P)$", "$d \\subset (P)$"], 0, "Định lí nhận biết: $d$ không nằm trong $(P), a \\subset (P), d \\parallel a \\Rightarrow d \\parallel (P)$."),
            lambda: ("Cho đường thẳng $d \\parallel (P)$. Khẳng định nào sau đây là ĐÚNG?", ["d không có điểm chung với $(P)$", "d có vô số điểm chung với $(P)$", "d vuông góc với mọi đường trong $(P)$", "Mọi đường trong $(P)$ đều song song với d"], 0, "$d \\parallel (P) \\Rightarrow d \\cap (P) = \\emptyset$."),
            lambda: ("Nếu đường thẳng d song song với mặt phẳng $(P)$ thì qua d có thể kẻ được bao nhiêu mặt phẳng song song với $(P)$?", ["$1$ mặt phẳng", "Vô số mặt phẳng", "Không có mặt phẳng nào", "$2$ mặt phẳng"], 0, "Có duy nhất một mặt phẳng đi qua d và song song với $(P)$."),
            lambda: ("Cho hình chóp $S.ABCD$ đáy là hình bình hành $ABCD$. Cạnh AB song song với mặt phẳng nào?", ["$(SCD)$", "$(SAD)$", "$(SBC)$", "$(SAB)$"], 0, "Do $AB \\parallel CD$ và $CD \\subset (SCD)$ nên $AB \\parallel (SCD)$.")
        ]),
        ("Hai mặt phẳng song song", "b13", [
            lambda: ("Hai mặt phẳng gọi là song song với nhau nếu:", ["Chúng không có điểm chung", "Chúng có vô số điểm chung", "Chúng vuông góc với nhau", "Giao tuyến của chúng là một đường thẳng"], 0, "Định nghĩa: Hai mặt phẳng song song nếu chúng không có điểm chung."),
            lambda: ("Điều kiện để mặt phẳng $(P)$ song song với mặt phẳng $(Q)$ là:", ["$(P)$ chứa hai đường thẳng cắt nhau cùng song song với $(Q)$", "$(P)$ chứa một đường thẳng song song với $(Q)$", "$(P)$ và $(Q)$ cùng song song với một đường thẳng", "$(P)$ chứa hai đường thẳng song song với nhau"], 0, "Định lí nhận biết hai mặt phẳng song song."),
            lambda: ("Nếu $(P) \\parallel (Q)$ và mặt phẳng $(R)$ cắt $(P)$ theo giao tuyến $a$ thì $(R)$ sẽ cắt $(Q)$ theo giao tuyến $b$ sao cho:", ["$a \\parallel b$", "a cắt b", "a chéo b", "$a \\perp b$"], 0, "Hai mặt phẳng song song bị cắt bởi mặt phẳng thứ ba thì hai giao tuyến song song."),
            lambda: ("Cho mặt phẳng $(P)$ và điểm $A \\notin (P)$. Có bao nhiêu mặt phẳng đi qua A và song song với $(P)$?", ["$1$ mặt phẳng duy nhất", "$2$ mặt phẳng", "Vô số mặt phẳng", "Không có mặt phẳng nào"], 0, "Qua một điểm ngoài mặt phẳng chỉ có duy nhất một mặt phẳng song song với mặt phẳng đó."),
            lambda: ("Nếu $(P) \\parallel (Q)$ và $(Q) \\parallel (R)$ thì:", ["$(P) \\parallel (R)$ (nếu phân biệt)", "$(P)$ cắt $(R)$", "$(P) \\perp (R)$", "$(P)$ chéo $(R)$"], 0, "Tính chất bắc cầu của quan hệ song song giữa hai mặt phẳng.")
        ]),
        ("Định lí Ta-lét trong không gian", "b13", [
            lambda: ("Định lí Ta-lét trong không gian phát biểu rằng ba mặt phẳng đôi một song song:", ["Chắn trên hai cát tuyến bất kì các đoạn thẳng tương ứng tỉ lệ", "Chắn trên hai cát tuyến các đoạn thẳng bằng nhau", "Tạo với hai cát tuyến các góc bằng nhau", "Đồng quy tại một điểm"], 0, "Ba mặt phẳng song song chắn trên hai cát tuyến những đoạn thẳng tương ứng tỉ lệ."),
            lambda: ("Ba mặt phẳng song song $(P), (Q), (R)$ cắt hai đường thẳng $d, d'$ lần lượt tại $A, B, C$ và $A', B', C'$. Tỉ số nào đúng?", ["$\\frac{AB}{BC} = \\frac{A'B'}{B'C'}$", "$\\frac{AB}{A'B'} = \\frac{BC}{AC}$", "$\\frac{AB}{BC} = \\frac{B'C'}{A'B'}$", "$AB \\cdot BC = A'B' \\cdot B'C'$"], 0, "Theo định lí Ta-lét: $\\frac{AB}{BC} = \\frac{A'B'}{B'C'}$."),
            lambda: ("Nếu $AB = BC$ thì trên cát tuyến $d'$ ta có:", ["$A'B' = B'C'$", "$A'B' = 2B'C'$", "$A'B' < B'C'$", "$A'B' > B'C'$"], 0, "Do tỉ lệ bằng 1 nên $A'B' = B'C'$."),
            lambda: ("Cho $AB = 2, BC = 4$ và $A'B' = 3$. Độ dài $B'C'$ bằng:", ["$6$", "$5$", "$4$", "$8$"], 0, "$\\frac{AB}{BC} = \\frac{2}{4} = \\frac{1}{2} \\Rightarrow B'C' = 2 A'B' = 6$."),
            lambda: ("Cho $AB = 3, BC = 3$ và $A'B' = 5$. Độ dài $B'C'$ là:", ["$5$", "$3$", "$10$", "$2,5$"], 0, "Do $AB = BC$ nên $A'B' = B'C' = 5$.")
        ]),
        ("Khái niệm hình lăng trụ và hình hộp", "b13", [
            lambda: ("Các mặt bên của hình lăng trụ là những hình gì?", ["Hình bình hành", "Hình chữ nhật", "Hình thang", "Hình tam giác"], 0, "Các mặt bên của hình lăng trụ luôn là hình bình hành."),
            lambda: ("Hai đáy của hình lăng trụ có tính chất nào sau đây?", ["Là hai đa giác bằng nhau và nằm trên hai mặt phẳng song song", "Là hai đa giác đồng dạng nhưng kích thước khác nhau", "Nằm trên hai mặt phẳng cắt nhau", "Luôn là hình tam giác đều"], 0, "Hai đáy của hình lăng trụ là hai đa giác bằng nhau nằm trên hai mặt phẳng song song."),
            lambda: ("Hình hộp là hình lăng trụ có đáy là:", ["Hình bình hành", "Hình tam giác", "Hình chữ nhật", "Hình thang"], 0, "Hình hộp là hình lăng trụ tứ giác có đáy là hình bình hành."),
            lambda: ("Hình lăng trụ tam giác có bao nhiêu mặt, bao nhiêu cạnh?", ["$5$ mặt, $9$ cạnh", "$6$ mặt, $8$ cạnh", "$5$ mặt, $6$ cạnh", "$4$ mặt, $6$ cạnh"], 0, "Lăng trụ tam giác có 2 đáy + 3 mặt bên = 5 mặt; 3 cạnh bên + 6 cạnh đáy = 9 cạnh."),
            lambda: ("Hình hộp có tất cả bao nhiêu đỉnh và bao nhiêu mặt?", ["$8$ đỉnh, $6$ mặt", "$6$ đỉnh, $8$ mặt", "$8$ đỉnh, $12$ mặt", "$12$ đỉnh, $6$ mặt"], 0, "Hình hộp có 8 đỉnh, 6 mặt (đều là hình bình hành).")
        ]),
        ("Khái niệm phép chiếu song song", "b14", [
            lambda: ("Phép chiếu song song biến ba điểm thẳng hàng thành:", ["Ba điểm thẳng hàng và bảo toàn thứ tự giữa chúng", "Ba điểm không thẳng hàng", "Một tam giác", "Đúng một điểm duy nhất"], 0, "Phép chiếu song song bảo toàn tính thẳng hàng và thứ tự các điểm."),
            lambda: ("Hình chiếu song song của hai đường thẳng song song là:", ["Hai đường thẳng song song hoặc trùng nhau", "Hai đường thẳng cắt nhau", "Hai đường thẳng chéo nhau", "Hai điểm phân biệt"], 0, "Biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau."),
            lambda: ("Phép chiếu song song có bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng không?", ["Có bảo toàn", "Không bảo toàn", "Chỉ bảo toàn khi vuông góc", "Tùy phương chiếu"], 0, "Phép chiếu song song bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng hoặc trên hai đường thẳng song song."),
            lambda: ("Hình chiếu song song của một hình bình hành lên mặt phẳng có thể là:", ["Hình bình hành hoặc một đoạn thẳng", "Hình thang vuông", "Một tam giác", "Một ngũ giác"], 0, "Nếu mặt phẳng hình bình hành không song song phương chiếu thì ra hình bình hành; nếu song song thì suy biến thành đoạn thẳng."),
            lambda: ("Hình chiếu song song của một đoạn thẳng có thể là:", ["Một đoạn thẳng hoặc một điểm", "Một tam giác", "Một tia", "Một đường tròn"], 0, "Biến đoạn thẳng thành đoạn thẳng (hoặc một điểm nếu đoạn thẳng song song phương chiếu).")
        ]),
        ("Hình biểu diễn của các hình phẳng", "b14", [
            lambda: ("Hình biểu diễn của đường tròn trong phép chiếu song song thường là:", ["Hình elip (hoặc đường tròn)", "Hình vuông", "Hình tam giác", "Hình thoi"], 0, "Hình biểu diễn của đường tròn thường là đường elip."),
            lambda: ("Hình biểu diễn của một tam giác đều có thể là:", ["Một tam giác bất kì", "Bắt buộc là tam giác đều", "Một hình vuông", "Một hình thoi"], 0, "Phép chiếu song song không bảo toàn góc nên tam giác đều biểu diễn bởi một tam giác bất kì."),
            lambda: ("Hình biểu diễn của một hình vuông là:", ["Hình bình hành", "Bắt buộc là hình vuông", "Hình thang", "Hình tròn"], 0, "Góc vuông không được bảo toàn nên hình vuông được biểu diễn bởi hình bình hành."),
            lambda: ("Hình biểu diễn của hình thoi là:", ["Hình bình hành", "Hình thang cân", "Hình chữ nhật", "Hình elip"], 0, "Hình thoi biểu diễn bởi hình bình hành."),
            lambda: ("Đoạn thẳng nối trung điểm hai cạnh của tam giác biểu diễn thành:", ["Đường trung bình của tam giác biểu diễn", "Đường cao", "Đường phân giác", "Trung trực"], 0, "Do bảo toàn trung điểm nên trung điểm biểu diễn thành trung điểm.")
        ]),
        ("Điểm thuộc mặt phẳng", "b10", [
            lambda: ("Nếu điểm A thuộc đường thẳng d và đường thẳng d nằm trong mặt phẳng $(P)$ thì:", ["Điểm A thuộc mặt phẳng $(P)$", "Điểm A không thuộc $(P)$", "Đường thẳng d cắt $(P)$", "Không kết luận được"], 0, "$A \\in d \\subset (P) \\Rightarrow A \\in (P)$."),
            lambda: ("Kí hiệu điểm M thuộc mặt phẳng $(P)$ là:", ["$M \\in (P)$", "$M \\subset (P)$", "$M \\parallel (P)$", "$M = (P)$"], 0, "Điểm thuộc mặt phẳng dùng kí hiệu $\\in$."),
            lambda: ("Nếu đường thẳng d có hai điểm phân biệt cùng thuộc $(P)$ thì:", ["Đường thẳng d nằm hoàn toàn trong $(P)$", "d cắt $(P)$ tại hai điểm", "d song song với $(P)$", "d vuông góc với $(P)$"], 0, "Một đường thẳng có hai điểm chung với mặt phẳng thì nằm trọn vẹn trong mặt phẳng đó."),
            lambda: ("Có tối đa bao nhiêu điểm chung giữa một đường thẳng không nằm trong mặt phẳng và mặt phẳng đó?", ["$1$ điểm", "$2$ điểm", "$3$ điểm", "Vô số"], 0, "Nếu không nằm trong mặt phẳng thì đường thẳng cắt mặt phẳng tại tối đa 1 điểm."),
            lambda: ("Khẳng định nào đúng về vị trí của điểm và mặt phẳng?", ["Điểm có thể thuộc hoặc không thuộc mặt phẳng", "Mọi điểm đều thuộc mặt phẳng", "Mọi điểm đều nằm ngoài mặt phẳng", "Điểm luôn là giao tuyến"], 0, "Một điểm hoặc thuộc mặt phẳng hoặc không thuộc mặt phẳng.")
        ]),
        ("Vị trí tương đối của đường thẳng và mặt phẳng", "b12", [
            lambda: ("Có bao nhiêu vị trí tương đối giữa một đường thẳng và một mặt phẳng?", ["$3$ (nằm trong, cắt nhau, song song)", "$2$", "$4$", "$1$"], 0, "Ba vị trí tương đối: $d \\subset (P)$, $d \\cap (P) = \\{M\\}$, $d \\parallel (P)$."),
            lambda: ("Nếu đường thẳng d cắt mặt phẳng $(P)$ thì số điểm chung giữa chúng là:", ["$1$", "$0$", "$2$", "Vô số"], 0, "Đường thẳng cắt mặt phẳng tại đúng 1 điểm chung."),
            lambda: ("Nếu đường thẳng d song song với mặt phẳng $(P)$ thì số điểm chung là:", ["$0$", "$1$", "$2$", "Vô số"], 0, "Song song nghĩa là không có điểm chung nào ($d \\cap (P) = \\emptyset$)."),
            lambda: ("Nếu đường thẳng d nằm trong mặt phẳng $(P)$ thì số điểm chung là:", ["Vô số", "$1$", "$2$", "$0$"], 0, "Mọi điểm của d đều thuộc $(P)$ nên có vô số điểm chung."),
            lambda: ("Cho $d \\parallel a$ với $a \\subset (P)$ và $d$ không nằm trong $(P)$. Vị trí của d và $(P)$ là:", ["$d \\parallel (P)$", "d cắt $(P)$", "$d \\subset (P)$", "d chéo $(P)$"], 0, "Theo định lí nhận biết thì $d \\parallel (P)$.")
        ])
    ]

    for dang, ls, gens in nb_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c4-{len(mc)+1:03d}", "chapter": "c4", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 12 dạng TH x 4 biến thể = 48 câu
    th_configs = [
        ("Tìm thiết diện qua trung điểm hình chóp", "b10", [
            lambda: ("Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Mặt phẳng qua trung điểm M của SA và song song với đáy cắt các cạnh SB, SC, SD lần lượt tại N, P, Q. Tứ giác MNPQ là hình gì?", ["Hình bình hành", "Hình thang vuông", "Hình thoi", "Tam giác"], 0, "Thiết diện song song với mặt đáy là hình bình hành nên MNPQ là hình bình hành."),
            lambda: ("Cho tứ diện ABCD. Gọi M, N lần lượt là trung điểm của AB và AC. Thiết diện của tứ diện cắt bởi mặt phẳng $(DMN)$ là:", ["Tam giác DMN", "Tứ giác", "Hình bình hành", "Đoạn thẳng"], 0, "Mặt phẳng $(DMN)$ đi qua đỉnh D và hai điểm M, N nên thiết diện là tam giác DMN."),
            lambda: ("Hình chóp tứ giác $S.ABCD$. Thiết diện cắt bởi mặt phẳng đi qua đỉnh S và đường chéo BD là:", ["Tam giác SBD", "Tam giác SAC", "Tứ giác SBDC", "Hình thang"], 0, "Thiết diện là tam giác tạo bởi S và BD, tức là tam giác SBD."),
            lambda: ("Cho tứ diện đều ABCD. Mặt phẳng đi qua trung điểm của 4 cạnh AB, BC, CD, DA cắt tứ diện theo thiết diện là:", ["Hình vuông (hoặc hình thoi)", "Tam giác", "Ngũ giác", "Hình chữ nhật lệch"], 0, "Bốn trung điểm của 4 cạnh liên tiếp tạo thành hình vuông/hình thoi.")
        ]),
        ("Chứng minh đường thẳng song song mặt phẳng", "b12", [
            lambda: ("Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi M, N lần lượt là trung điểm của SA và SB. Đường thẳng MN song song với mặt phẳng nào sau đây?", ["$(ABCD)$", "$(SCD)$", "$(SBC)$", "$(SAB)$"], 0, "MN là đường trung bình tam giác SAB nên $MN \\parallel AB$. Do $AB \\subset (ABCD)$ nên $MN \\parallel (ABCD)$."),
            lambda: ("Trong hình chóp $S.ABCD$ đáy hình bình hành, O là tâm đáy. Gọi M là trung điểm SC. Đường thẳng OM song song với mặt phẳng:", ["$(SAD)$", "$(SAB)$", "$(SCD)$", "$(ABCD)$"], 0, "OM là đường trung bình tam giác SAC nên $OM \\parallel SA$. Vì $SA \\subset (SAD)$ nên $OM \\parallel (SAD)$."),
            lambda: ("Cho tứ diện ABCD. Gọi G là trọng tâm tam giác BCD, M là trung điểm AB. Đường thẳng nào song song với $(ABC)$?", ["Không có", "Đường trung tuyến", "Cạnh CD", "Đoạn thẳng qua trung điểm hai cạnh đối song song"], 0, "Đoạn thẳng nối trung điểm hai cạnh song song với một cạnh đáy sẽ song song với mặt phẳng tương ứng."),
            lambda: ("Cho hình chóp $S.ABCD$ đáy $ABCD$ là hình bình hành tâm O. Đường thẳng qua O song song với BC sẽ song song với mặt phẳng:", ["$(SBC)$ và $(SAD)$", "$(SAB)$", "$(SCD)$", "$(ABCD)$"], 0, "Song song với BC thì song song với $(SBC)$ và $(SAD)$.")
        ]),
        ("Chứng minh hai mặt phẳng song song", "b13", [
            lambda: ("Cho hình chóp $S.ABCD$ đáy hình bình hành. Gọi $M, N, P$ lần lượt là trung điểm của $SA, SB, SC$. Mặt phẳng $(MNP)$ song song với mặt phẳng nào?", ["$(ABCD)$", "$(SCD)$", "$(SAD)$", "$(SAB)$"], 0, "$MN \\parallel AB$ và $NP \\parallel BC$ nên $(MNP) \\parallel (ABCD)$."),
            lambda: ("Cho lăng trụ $ABC.A'B'C'$. Mặt phẳng đáy $(ABC)$ song song với mặt phẳng nào?", ["$(A'B'C')$", "$(ABB'A')$", "$(ACC'A')$", "$(BCC'B')$"], 0, "Hai đáy của hình lăng trụ luôn song song với nhau."),
            lambda: ("Trong hình hộp $ABCD.A'B'C'D'$, mặt phẳng $(ABCD)$ song song với mặt phẳng nào?", ["$(A'B'C'D')$", "$(ABB'A')$", "$(AA'C'C)$", "$(BDD'B')$"], 0, "Mặt đáy dưới song song với mặt đáy trên $(A'B'C'D')$."),
            lambda: ("Cho hai hình bình hành ABCD và ABEF không cùng nằm trong một mặt phẳng. Mặt phẳng $(DCE)$ song song với mặt phẳng nào?", ["Không có mặt phẳng song song", "$(ABF)$", "$(ABCD)$", "$(CDEF)$"], 0, "Vì $CD \\parallel AB$ và $EF \\parallel AB$ nên $CD \\parallel EF$, từ đó xét thiết diện tương ứng.")
        ]),
        ("Giao tuyến của hai mặt phẳng chứa hai đường song song", "b11", [
            lambda: ("Hai mặt phẳng $(P)$ và $(Q)$ lần lượt chứa hai đường thẳng song song $a$ và $b$. Nếu $(P)$ cắt $(Q)$ theo giao tuyến $d$ thì:", ["$d \\parallel a$ và $d \\parallel b$", "d cắt a", "d chéo b", "d vuông góc với a"], 0, "Giao tuyến song song với cả a và b."),
            lambda: ("Trong hình chóp $S.ABCD$ đáy là hình thang với $AB \\parallel CD$. Giao tuyến của $(SAB)$ và $(SCD)$ là:", ["Đường thẳng qua S và song song với AB, CD", "Đoạn thẳng SO", "Đường thẳng qua S và giao điểm của AD, BC", "Đường thẳng CD"], 0, "Hai mặt phẳng chứa hai đường thẳng song song nên giao tuyến qua điểm chung S và song song với chúng."),
            lambda: ("Cho hình chóp $S.ABCD$ đáy hình bình hành. Giao tuyến của $(SAD)$ và $(SBC)$ là:", ["Đường thẳng qua S song song với AD và BC", "Đường thẳng SO", "Cạnh SA", "Đường thẳng AB"], 0, "Qua S và song song với $AD, BC$."),
            lambda: ("Cho tứ diện ABCD có M, N là trung điểm AB, AC. Giao tuyến của $(DMN)$ và $(BCD)$ là:", ["Đường thẳng qua D song song với BC và MN", "Đoạn thẳng MN", "Đoạn thẳng BC", "Đường thẳng DN"], 0, "Do $MN \\parallel BC$ nên giao tuyến qua D và song song với MN, BC.")
        ]),
        ("Tính chất trung điểm và song song trong tứ diện", "b11", [
            lambda: ("Cho tứ diện ABCD. Gọi M, N, P, Q lần lượt là trung điểm của AB, BC, CD, DA. Tứ giác MNPQ là:", ["Hình bình hành", "Hình thang vuông", "Tam giác", "Tứ giác không phẳng"], 0, "MN và PQ cùng song song và bằng một nửa AC nên MNPQ là hình bình hành."),
            lambda: ("Trong tứ diện ABCD, các đoạn thẳng nối trung điểm của các cặp cạnh đối diện:", ["Đồng quy tại một điểm (trọng tâm tứ diện)", "Đôi một song song", "Đôi một vuông góc", "Chéo nhau"], 0, "Ba đoạn thẳng nối trung điểm các cạnh đối cắt nhau tại trung điểm của mỗi đoạn."),
            lambda: ("Tứ diện ABCD có bao nhiêu cặp cạnh đối diện chéo nhau?", ["$3$ cặp", "$4$ cặp", "$2$ cặp", "$6$ cặp"], 0, "Ba cặp cạnh đối: (AB, CD), (AC, BD), (AD, BC)."),
            lambda: ("Gọi G là trọng tâm tứ diện ABCD. Tỉ số khoảng cách từ G đến đỉnh và mặt đáy tương ứng là:", ["$3:1$", "$2:1$", "$1:1$", "$4:1$"], 0, "Trọng tâm tứ diện chia đoạn nối đỉnh với trọng tâm mặt đối diện theo tỉ số 3:1.")
        ]),
        ("Tính tỉ số theo định lí Ta-lét không gian", "b13", [
            lambda: ("Ba mặt phẳng song song cắt cát tuyến d tại A, B, C và cát tuyến d' tại A', B', C'. Biết $AB = 3, BC = 6, A'B' = 4$. Độ dài $B'C'$ là:", ["$8$", "$6$", "$12$", "$9$"], 0, "$\\frac{A'B'}{B'C'} = \\frac{AB}{BC} = \\frac{3}{6} = \\frac{1}{2} \\Rightarrow B'C' = 2 A'B' = 8$."),
            lambda: ("Cho $AB/BC = 2/3$ và $A'B' = 6$. Tính $B'C'$:", ["$9$", "$4$", "$10$", "$8$"], 0, "$B'C' = 6 \\times \\frac{3}{2} = 9$."),
            lambda: ("Biết $AB = 4, BC = 2, B'C' = 5$. Độ dài $A'B'$ bằng:", ["$10$", "$8$", "$6$", "$12$"], 0, "$A'B' = B'C' \\times \\frac{AB}{BC} = 5 \\times 2 = 10$."),
            lambda: ("Cho $AB = 5, BC = 10, A'B' = 7$. Tính độ dài $B'C'$:", ["$14$", "$12$", "$10$", "$15$"], 0, "$B'C' = 7 \\times 2 = 14$.")
        ]),
        ("Tìm giao điểm của đường thẳng và mặt phẳng", "b10", [
            lambda: ("Để tìm giao điểm của đường thẳng d và mặt phẳng $(P)$, ta thường:", ["Tìm mặt phẳng $(Q)$ chứa d, rồi tìm giao tuyến $a = (P) \\cap (Q)$, sau đó $d \\cap a$", "Kẻ d vuông góc với $(P)$", "Chiếu d lên $(P)$", "Lấy một điểm bất kì trên d"], 0, "Phương pháp chuẩn: chọn $(Q) \\supset d$, tìm $a = (P) \\cap (Q)$, giao điểm là $M = d \\cap a$."),
            lambda: ("Trong hình chóp $S.ABCD$, O là tâm đáy. Giao điểm của SO và mặt phẳng $(ABCD)$ là:", ["Điểm O", "Điểm S", "Điểm A", "Điểm B"], 0, "O vừa thuộc SO vừa thuộc $(ABCD)$."),
            lambda: ("Cho tứ diện ABCD, M là điểm trên AB. Giao điểm của DM với mặt phẳng $(ABC)$ là:", ["Điểm M", "Điểm D", "Điểm A", "Điểm B"], 0, "Điểm M nằm trên AB nên $M \\in (ABC)$."),
            lambda: ("Cho hình chóp $S.ABCD$. Đường thẳng SA cắt mặt phẳng $(SBC)$ tại điểm nào?", ["Điểm S", "Điểm A", "Điểm B", "Điểm C"], 0, "Điểm chung duy nhất là S.")
        ]),
        ("Thiết diện song song với một đường thẳng", "b12", [
            lambda: ("Mặt phẳng đi qua điểm M và song song với hai đường thẳng chéo nhau $a$ và $b$ cắt các mặt của tứ diện tạo thành thiết diện là:", ["Hình bình hành", "Hình thang vuông", "Tam giác", "Ngũ giác"], 0, "Các cạnh của thiết diện lần lượt song song với a và b nên là hình bình hành."),
            lambda: ("Cắt hình chóp $S.ABCD$ bởi mặt phẳng song song với đáy ta được thiết diện là một đa giác:", ["Đồng dạng với đa giác đáy", "Bằng đa giác đáy", "Luôn là hình chữ nhật", "Tam giác"], 0, "Mặt phẳng song song với đáy cắt các mặt bên tạo thành đa giác đồng dạng với đa giác đáy."),
            lambda: ("Cắt hình lăng trụ bởi mặt phẳng song song với hai đáy ta được thiết diện là:", ["Đa giác bằng hai đa giác đáy", "Đa giác lớn hơn", "Đa giác nhỏ hơn", "Hình bình hành"], 0, "Thiết diện song song với hai đáy bằng chính hai đáy."),
            lambda: ("Cắt hình hộp bởi mặt phẳng song song với một mặt của hình hộp ta được thiết diện là:", ["Hình bình hành bằng mặt đó", "Hình thang", "Tam giác", "Hình thoi"], 0, "Thiết diện bằng mặt song song tương ứng.")
        ]),
        ("Độ dài đoạn thẳng trong phép chiếu song song", "b14", [
            lambda: ("Một đoạn thẳng AB dài 10 cm có hình chiếu song song là A'B'. Nếu AB song song với mặt phẳng chiếu thì độ dài A'B' bằng:", ["$10\\text{ cm}$", "$5\\text{ cm}$", "$20\\text{ cm}$", "$0\\text{ cm}$"], 0, "Khi đoạn thẳng song song với mặt phẳng chiếu thì hình chiếu bằng chính đoạn thẳng đó: 10 cm."),
            lambda: ("Đoạn thẳng AB có trung điểm M. Phép chiếu song song biến A, B, M thành A', B', M'. Điểm M' là:", ["Trung điểm của A'B'", "Điểm nằm ngoài đoạn A'B'", "Trùng với A'", "Trùng với B'"], 0, "Phép chiếu song song bảo toàn trung điểm."),
            lambda: ("Đoạn AB được chia thành 3 phần bằng nhau bởi C và D. Hình chiếu A'B' được chia bởi C' và D' thành:", ["$3$ phần bằng nhau", "Các phần không bằng nhau", "$2$ phần", "$4$ phần"], 0, "Bảo toàn tỉ số các đoạn thẳng trên cùng một đường thẳng."),
            lambda: ("Nếu đoạn thẳng AB vuông góc với phương chiếu (và không song song mặt phẳng chiếu), độ dài A'B' so với AB:", ["Phụ thuộc vào góc nghiêng của mặt phẳng chiếu", "Luôn bằng 0", "Luôn gấp đôi", "Luôn bằng nhau"], 0, "Độ dài thay đổi phụ thuộc góc nghiêng.")
        ]),
        ("Số mặt phẳng đối xứng hoặc song song trong hình hộp", "b13", [
            lambda: ("Trong hình hộp $ABCD.A'B'C'D'$, có bao nhiêu cặp mặt đối diện song song với nhau?", ["$3$ cặp", "$4$ cặp", "$6$ cặp", "$2$ cặp"], 0, "Có 3 cặp mặt đối diện: (ABCD, A'B'C'D'), (ABB'A', CDD'C'), (ADD'A', BCC'B')."),
            lambda: ("Số đường chéo của một hình hộp là:", ["$4$ đường chéo", "$6$ đường chéo", "$8$ đường chéo", "$12$ đường chéo"], 0, "Hình hộp có 4 đường chéo: AC', BD', CA', DB'."),
            lambda: ("Bốn đường chéo của hình hộp có tính chất nào?", ["Cắt nhau tại trung điểm của mỗi đường", "Đôi một vuông góc", "Song song với nhau", "Chéo nhau"], 0, "Bốn đường chéo đồng quy tại tâm hình hộp và cắt nhau tại trung điểm mỗi đường."),
            lambda: ("Số cạnh của hình hộp là:", ["$12$ cạnh", "$8$ cạnh", "$6$ cạnh", "$16$ cạnh"], 0, "Hình hộp có 4 cạnh đáy dưới, 4 cạnh đáy trên, 4 cạnh bên = 12 cạnh.")
        ]),
        ("Tỉ số thể tích đơn giản theo diện tích mặt cắt", "b13", [
            lambda: ("Mặt phẳng qua trung điểm chiều cao và song song với đáy hình chóp chia hình chóp thành hai phần. Diện tích thiết diện bằng bao nhiêu lần diện tích đáy?", ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{1}{8}$"], 0, "Tỉ số đồng dạng bằng $1/2$ nên tỉ số diện tích bằng $(1/2)^2 = 1/4$."),
            lambda: ("Nếu tỉ số khoảng cách từ đỉnh đến thiết diện là $1/3$ thì tỉ số diện tích thiết diện so với đáy là:", ["$\\frac{1}{9}$", "$\\frac{1}{3}$", "$\\frac{1}{6}$", "$\\frac{1}{27}$"], 0, "Tỉ số diện tích bằng bình phương tỉ số đồng dạng: $(1/3)^2 = 1/9$."),
            lambda: ("Cắt hình chóp bởi mặt phẳng song song với đáy sao cho diện tích thiết diện bằng $1/4$ diện tích đáy. Tỉ số khoảng cách từ đỉnh đến thiết diện là:", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{1}{16}$", "$\\frac{1}{8}$"], 0, "Căn bậc hai của $1/4$ là $1/2$."),
            lambda: ("Nếu tỉ số đồng dạng là $2/3$ thì tỉ số diện tích thiết diện so với đáy là:", ["$\\frac{4}{9}$", "$\\frac{2}{3}$", "$\\frac{8}{27}$", "$\\frac{1}{3}$"], 0, "$(2/3)^2 = 4/9$.")
        ]),
        ("Nhận dạng quan hệ song song trong thực tế", "b12", [
            lambda: ("Các thanh xà gồ đỡ mái tôn trong một ngôi nhà thường được đặt:", ["Song song với nhau", "Cắt nhau", "Chéo nhau", "Vuông góc với nhau"], 0, "Các thanh xà gồ được đặt song song để chia đều tải trọng."),
            lambda: ("Hai mép trên và mép dưới của chiếc bảng lớp học biểu diễn hình học là:", ["Hai đường thẳng song song", "Hai đường thẳng cắt nhau", "Hai đường thẳng chéo nhau", "Hai đường thẳng trùng nhau"], 0, "Hai mép đối diện của bảng chữ nhật song song với nhau."),
            lambda: ("Các cột nhà thẳng đứng trong một toà nhà có vị trí tương đối là:", ["Song song với nhau", "Cắt nhau tại trần nhà", "Chéo nhau", "Trùng nhau"], 0, "Các cột đứng song song với nhau."),
            lambda: ("Mặt sàn nhà và mặt trần nhà trong một căn phòng là hình ảnh của:", ["Hai mặt phẳng song song", "Hai mặt phẳng cắt nhau", "Hai mặt phẳng vuông góc", "Hai mặt phẳng trùng nhau"], 0, "Sàn nhà và trần nhà là hai mặt phẳng song song.")
        ])
    ]

    for dang, ls, gens in th_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c4-{len(mc)+1:03d}", "chapter": "c4", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # 3 dạng VD x 4 biến thể = 12 câu
    vd_configs = [
        ("Tính chu vi thiết diện song song đáy", "b13", [
            lambda: ("Cho hình chóp tam giác đều $S.ABC$ có đáy là tam giác đều cạnh 6 cm. Cắt hình chóp bởi mặt phẳng song song với đáy qua trung điểm SA. Chu vi thiết diện bằng:", ["$9\\text{ cm}$", "$18\\text{ cm}$", "$12\\text{ cm}$", "$6\\text{ cm}$"], 0, "Thiết diện là tam giác đều có cạnh bằng một nửa cạnh đáy: $6/2 = 3\\text{ cm}$. Chu vi là $3 \\times 3 = 9\\text{ cm}$."),
            lambda: ("Hình chóp tứ giác đều $S.ABCD$ đáy hình vuông cạnh 8 cm. Mặt phẳng song song với đáy đi qua trung điểm của chiều cao cắt hình chóp theo thiết diện có chu vi là:", ["$16\\text{ cm}$", "$32\\text{ cm}$", "$24\\text{ cm}$", "$8\\text{ cm}$"], 0, "Cạnh thiết diện bằng $8/2 = 4\\text{ cm}$. Chu vi hình vuông thiết diện là $4 \\times 4 = 16\\text{ cm}$."),
            lambda: ("Cho tứ diện đều ABCD cạnh 10 cm. Mặt phẳng song song với $(BCD)$ đi qua điểm M trên AB với $AM = 2\\text{ cm}$. Chu vi tam giác thiết diện là:", ["$6\\text{ cm}$", "$15\\text{ cm}$", "$10\\text{ cm}$", "$30\\text{ cm}$"], 0, "Tỉ số đồng dạng $AM/AB = 2/10 = 1/5$. Cạnh thiết diện là $10 \\times 1/5 = 2\\text{ cm}$. Chu vi bằng $3 \\times 2 = 6\\text{ cm}$."),
            lambda: ("Hình chóp tam giác có chu vi đáy là 24 cm. Mặt phẳng qua điểm chia cạnh bên theo tỉ số $1:2$ (kể từ đỉnh) song song với đáy cắt hình chóp tạo thiết diện có chu vi:", ["$8\\text{ cm}$", "$12\\text{ cm}$", "$16\\text{ cm}$", "$6\\text{ cm}$"], 0, "Tỉ số là $1/3$, chu vi thiết diện là $24 \\times 1/3 = 8\\text{ cm}$.")
        ]),
        ("Diện tích thiết diện của hình lập phương", "b13", [
            lambda: ("Hình lập phương $ABCD.A'B'C'D'$ cạnh $a = 4\\text{ cm}$. Cắt hình lập phương bởi mặt phẳng song song với mặt đáy. Diện tích thiết diện là:", ["$16\\text{ cm}^2$", "$8\\text{ cm}^2$", "$64\\text{ cm}^2$", "$32\\text{ cm}^2$"], 0, "Thiết diện song song với mặt đáy là hình vuông bằng đáy, diện tích bằng $4^2 = 16\\text{ cm}^2$."),
            lambda: ("Hình lập phương cạnh 5 cm. Cắt bởi mặt phẳng song song với đáy thu được thiết diện có diện tích:", ["$25\\text{ cm}^2$", "$20\\text{ cm}^2$", "$125\\text{ cm}^2$", "$50\\text{ cm}^2$"], 0, "$S = 5^2 = 25\\text{ cm}^2$."),
            lambda: ("Một khối gỗ hình hộp chữ nhật có kích thước đáy $6\\text{ cm} \\times 8\\text{ cm}$. Cắt bởi mặt phẳng song song với đáy thì diện tích mặt cắt bằng:", ["$48\\text{ cm}^2$", "$24\\text{ cm}^2$", "$28\\text{ cm}^2$", "$96\\text{ cm}^2$"], 0, "Diện tích mặt cắt bằng diện tích đáy: $6 \\times 8 = 48\\text{ cm}^2$."),
            lambda: ("Hình lập phương cạnh 6 cm. Mặt phẳng song song với một mặt bên cắt khối lập phương tạo thiết diện có diện tích:", ["$36\\text{ cm}^2$", "$24\\text{ cm}^2$", "$216\\text{ cm}^2$", "$72\\text{ cm}^2$"], 0, "Diện tích bằng diện tích mặt bên: $6^2 = 36\\text{ cm}^2$.")
        ]),
        ("Độ dài đoạn thẳng theo tỉ số Ta-lét nâng cao", "b13", [
            lambda: ("Cho hình chóp $S.ABCD$ đáy hình thang có đáy lớn $AB = 12\\text{ cm}$, đáy nhỏ $CD = 6\\text{ cm}$. Gọi M, N lần lượt là trung điểm của SA và SB. Độ dài đoạn MN là:", ["$6\\text{ cm}$", "$3\\text{ cm}$", "$9\\text{ cm}$", "$4\\text{ cm}$"], 0, "MN là đường trung bình tam giác SAB nên $MN = AB/2 = 12/2 = 6\\text{ cm}$."),
            lambda: ("Hình chóp tứ giác đáy hình bình hành $AB = 10\\text{ cm}$. M trên SA sao cho $SM/SA = 2/5$. Đoạn thẳng qua M song song với AB cắt SB tại N. Độ dài MN là:", ["$4\\text{ cm}$", "$2\\text{ cm}$", "$5\\text{ cm}$", "$6\\text{ cm}$"], 0, "$MN = AB \\times 2/5 = 10 \\times 2/5 = 4\\text{ cm}$."),
            lambda: ("Cho tam giác SAB có $AB = 15\\text{ cm}$. Đoạn thẳng $MN \\parallel AB$ với $M \\in SA, N \\in SB$ sao cho $SM/SA = 1/3$. Tính MN:", ["$5\\text{ cm}$", "$3\\text{ cm}$", "$10\\text{ cm}$", "$7,5\\text{ cm}$"], 0, "$MN = 15 \\times 1/3 = 5\\text{ cm}$."),
            lambda: ("Cho hình chóp $S.ABCD$, đáy $AB = 20\\text{ cm}$. Điểm M trên SA thoả mãn $SM/SA = 3/4$. Kẻ $MN \\parallel AB$ ($N \\in SB$). Độ dài MN bằng:", ["$15\\text{ cm}$", "$10\\text{ cm}$", "$5\\text{ cm}$", "$16\\text{ cm}$"], 0, "$MN = 20 \\times 3/4 = 15\\text{ cm}$.")
        ])
    ]

    for dang, ls, gens in vd_configs:
        for gen in gens:
            q, ch, a, ex = gen()
            mc.append({
                "id": f"mc-c4-{len(mc)+1:03d}", "chapter": "c4", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "choices": make_unique_choices(ch), "answer": a, "explanation": ex
            })

    # TLN: 3 dạng NB x 5 = 15 câu, 3 dạng TH x 4 = 12 câu, 1 dạng VD x 3 = 3 câu -> 30 câu
    sa_nb = [
        ("Số đỉnh và số mặt của hình đa diện", "b10", [
            ("Hình tứ diện có tất cả bao nhiêu đỉnh?", 4, "Tứ diện có 4 đỉnh."),
            ("Hình tứ diện có bao nhiêu mặt?", 4, "Tứ diện có 4 mặt (là 4 tam giác)."),
            ("Hình chóp tứ giác có tất cả bao nhiêu mặt?", 5, "1 mặt đáy + 4 mặt bên = 5 mặt."),
            ("Hình hộp có tất cả bao nhiêu đỉnh?", 8, "Hình hộp có 8 đỉnh."),
            ("Hình lăng trụ tam giác có bao nhiêu đỉnh?", 6, "2 đáy mỗi đáy 3 đỉnh, tổng là 6 đỉnh.")
        ]),
        ("Số cạnh của hình không gian", "b10", [
            ("Hình tứ diện có tất cả bao nhiêu cạnh?", 6, "Tứ diện có 6 cạnh."),
            ("Hình chóp tứ giác có tất cả bao nhiêu cạnh?", 8, "4 cạnh đáy + 4 cạnh bên = 8 cạnh."),
            ("Hình hộp có tất cả bao nhiêu cạnh?", 12, "Hình hộp có 12 cạnh."),
            ("Hình lăng trụ tam giác có bao nhiêu cạnh?", 9, "6 cạnh đáy + 3 cạnh bên = 9 cạnh."),
            ("Hình chóp ngũ giác có tất cả bao nhiêu cạnh?", 10, "5 cạnh đáy + 5 cạnh bên = 10 cạnh.")
        ]),
        ("Số mặt đối diện song song trong hình hộp", "b13", [
            ("Hình hộp có bao nhiêu cặp mặt đối diện song song với nhau?", 3, "Có 3 cặp mặt đối diện."),
            ("Số đường chéo của một hình hộp bằng bao nhiêu?", 4, "Hình hộp có 4 đường chéo."),
            ("Hình lập phương có bao nhiêu mặt?", 6, "Hình lập phương có 6 mặt."),
            ("Hình chóp tam giác có bao nhiêu mặt bên?", 3, "Có 3 mặt bên."),
            ("Hình lăng trụ tứ giác có bao nhiêu mặt bên?", 4, "Có 4 mặt bên.")
        ])
    ]
    for dang, ls, items in sa_nb:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c4-{len(sa)+1:03d}", "chapter": "c4", "lesson": ls, "level": "nb",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_th = [
        ("Tính độ dài đoạn thẳng trung bình", "b11", [
            ("Cho tam giác SAB có $AB = 10\\text{ cm}$. M và N là trung điểm của SA và SB. Độ dài MN bằng bao nhiêu cm?", 5, "$MN = AB/2 = 10/2 = 5\\text{ cm}$."),
            ("Trong tứ diện ABCD, $CD = 14\\text{ cm}$. M, N là trung điểm của BC và BD. Độ dài MN bằng:", 7, "$MN = CD/2 = 14/2 = 7\\text{ cm}$."),
            ("Cho hình chóp $S.ABCD$ đáy hình bình hành $AB = 16\\text{ cm}$. Đoạn trung bình MN của tam giác SAB dài bao nhiêu cm?", 8, "$MN = 16/2 = 8\\text{ cm}$."),
            ("Cho $AB = 12\\text{ cm}$. Đường trung bình song song với AB có độ dài là:", 6, "$12/2 = 6\\text{ cm}$.")
        ]),
        ("Tính tỉ số Ta-lét trong không gian", "b13", [
            ("Ba mặt phẳng song song chắn trên cát tuyến d hai đoạn $AB = 4, BC = 8$ và trên cát tuyến d' đoạn $A'B' = 3$. Độ dài $B'C'$ bằng:", 6, "$B'C' = 3 \\times (8/4) = 6$."),
            ("Cho $AB = 2, BC = 6$ và $A'B' = 5$. Tính độ dài $B'C'$:", 15, "$B'C' = 5 \\times (6/2) = 15$."),
            ("Cho $AB = 5, BC = 5$ và $A'B' = 7$. Độ dài $B'C'$ bằng:", 7, "$B'C' = 7$."),
            ("Biết $AB/BC = 1/3$ và $A'B' = 4$. Độ dài $B'C'$ bằng bao nhiêu?", 12, "$B'C' = 4 \\times 3 = 12$.")
        ]),
        ("Chu vi thiết diện tam giác trung điểm", "b13", [
            ("Cho tứ diện đều ABCD có tất cả các cạnh bằng 6 cm. Cắt bởi mặt phẳng song song với (BCD) qua trung điểm AB. Chu vi tam giác thiết diện bằng bao nhiêu cm?", 9, "Mỗi cạnh thiết diện bằng $6/2 = 3\\text{ cm}$. Chu vi bằng $3 \\times 3 = 9\\text{ cm}$."),
            ("Tam giác đáy có chu vi 18 cm. Thiết diện qua trung điểm cạnh bên song song với đáy có chu vi bằng:", 9, "$18/2 = 9\\text{ cm}$."),
            ("Đáy hình chóp có chu vi 20 cm. Chu vi thiết diện song song với đáy qua trung điểm chiều cao là:", 10, "$20/2 = 10\\text{ cm}$."),
            ("Tam giác đều cạnh 8 cm có chu vi là 24 cm. Chu vi thiết diện tỉ số $1/2$ bằng:", 12, "$24/2 = 12\\text{ cm}$.")
        ])
    ]
    for dang, ls, items in sa_th:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c4-{len(sa)+1:03d}", "chapter": "c4", "lesson": ls, "level": "th",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    sa_vd = [
        ("Diện tích hình vuông thiết diện", "b13", [
            ("Hình lập phương có cạnh 4 cm. Diện tích thiết diện cắt bởi mặt phẳng song song với đáy bằng bao nhiêu cm vuông?", 16, "$4^2 = 16\\text{ cm}^2$."),
            ("Hình lập phương có cạnh 5 cm. Diện tích mặt cắt song song với một mặt bên là:", 25, "$5^2 = 25\\text{ cm}^2$."),
            ("Một khối lập phương cạnh 3 cm. Mặt cắt song song đáy có diện tích bằng:", 9, "$3^2 = 9\\text{ cm}^2$.")
        ])
    ]
    for dang, ls, items in sa_vd:
        for q, ans, ex in items:
            sa.append({
                "id": f"sa-c4-{len(sa)+1:03d}", "chapter": "c4", "lesson": ls, "level": "vd",
                "dang": dang, "question": q, "answer": ans, "explanation": ex
            })

    lessons = [
        {"lesson_id": "b10", "sgk_title": "Bài 10. Đường thẳng và mặt phẳng trong không gian"},
        {"lesson_id": "b11", "sgk_title": "Bài 11. Hai đường thẳng song song"},
        {"lesson_id": "b12", "sgk_title": "Bài 12. Đường thẳng và mặt phẳng song song"},
        {"lesson_id": "b13", "sgk_title": "Bài 13. Hai mặt phẳng song song"},
        {"lesson_id": "b14", "sgk_title": "Bài 14. Phép chiếu song song"}
    ]
    save_bank("c4", "Quan hệ song song trong không gian", lessons, mc, sa)

if __name__ == "__main__":
    gen_c4()
