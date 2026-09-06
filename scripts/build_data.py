# -*- coding: utf-8 -*-
"""
Lắp ráp và KIỂM ĐỊNH ngân hàng câu hỏi Toán - Lý - Hóa 10 (GDPT 2018, Kết nối tri thức).

Nguồn dữ liệu là các file ngân hàng đã biên soạn trong
    scripts/bank/<mon>_<chuong>.json

Script này KHÔNG tự bịa ra câu hỏi. Nó chỉ:
  1. đọc ngân hàng, gán id ổn định, gán chapter,
  2. trộn thứ tự phương án bằng seed cố định (chạy lại cho kết quả giống hệt),
  3. chạy toàn bộ bộ kiểm định chất lượng,
  4. ghi ra data/<mon>/questions/{mc,short}.json và đồng bộ tiêu đề bài trong index.json.

Chạy:  python scripts/build_data.py            # kiểm định rồi ghi
       python scripts/build_data.py --check    # chỉ kiểm định, không ghi
"""

import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK_DIR = os.path.join(BASE_DIR, "scripts", "bank")
DATA_DIR = os.path.join(BASE_DIR, "data")

SEED = 20261001                     # cố định để build lại cho kết quả giống hệt
SUBJECTS = ["toan10", "ly10", "hoa10"]
CHAPTERS = ["c1", "c2", "c3", "c4", "c5"]

MC_PER_CHAPTER = 120
SA_PER_CHAPTER = 30
# Phân bổ độ khó 50% nhận biết / 40% thông hiểu / 10% vận dụng
MC_LEVELS = {"nb": 60, "th": 48, "vd": 12}
SA_LEVELS = {"nb": 15, "th": 12, "vd": 3}
MAX_VARIANTS = 5                    # mỗi dạng bài tối đa 5 biến thể

# Tập lệnh LaTeX mà assets/js/math.js render được.
# Ngoài tập này sẽ lòi dấu gạch chéo ra màn hình học sinh.
SUPPORTED_LATEX = set("""
frac sqrt vec overrightarrow bar overline hat mathbb mathrm mathbf mathit text
le ge ne pm mp times div cdot deg circ sin cos tan cot log
infty in notin subset supset cup cap emptyset setminus forall exists neg
Rightarrow Leftrightarrow rightarrow to mapsto perp parallel angle triangle
alpha beta gamma delta Delta theta lambda mu pi rho sigma Sigma tau phi omega Omega
approx equiv propto sum prod R Q Z N
""".split())

CMD_RE = re.compile(r"\\([A-Za-z]+)")
ESCAPES = set("{}%_$&\\")
ENG_DECIMAL_RE = re.compile(r"\d\.\d")
UNICODE_SCRIPTS = set("₀₁₂₃₄₅₆₇₈₉"
                      "⁰¹²³⁴⁵⁶⁷⁸⁹"
                      "⁺⁻")
ORDINAL_LEAK_RE = re.compile(r"\(\s*C[âa]u\s*\d+\s*\)", re.IGNORECASE)


class Problems(object):
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where, msg):
        self.warnings.append("%s: %s" % (where, msg))


def check_latex(text, where, p):
    """Bắt lệnh LaTeX mà bộ render không hiểu."""
    for m in CMD_RE.finditer(text):
        if m.group(1) not in SUPPORTED_LATEX:
            p.error(where, "lenh LaTeX khong ho tro: \\%s" % m.group(1))
    for i, ch in enumerate(text):
        if ch == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if not nxt.isalpha() and nxt not in ESCAPES:
                p.error(where, "dau thoat la: \\%s" % nxt)


def check_display_text(text, where, p):
    """Văn bản hiển thị cho học sinh phải theo chuẩn trình bày SGK Việt Nam."""
    check_latex(text, where, p)
    m = ORDINAL_LEAK_RE.search(text)
    if m:
        p.error(where, "con lo so thu tu sinh tu dong: %r" % m.group(0))
    m = ENG_DECIMAL_RE.search(text)
    if m:
        p.error(where, "dung dau cham thap phan kieu Anh, phai doi sang dau phay: %r" % m.group(0))
    bad = UNICODE_SCRIPTS & set(text)
    if bad:
        p.error(where, "dung ky tu Unicode mu/chi so %r, phai viet bang LaTeX ^{} _{}"
                % "".join(sorted(bad)))


def parse_number(s):
    """Bản Python của parseNumber trong assets/js/grade.js, dùng để kiểm định đáp số."""
    if s is None:
        return None
    s = str(s).strip()
    if s == "":
        return None
    s = re.sub(r"[−–—]", "-", s)
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"%$", "", s)
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(",") > 1:
        s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    else:
        s = s.replace(",", ".", 1)
    m = re.match(r"^(-?\d+(?:\.\d+)?)/(-?\d+(?:\.\d+)?)$", s)
    if m:
        den = float(m.group(2))
        return None if den == 0 else float(m.group(1)) / den
    return float(s) if re.match(r"^-?\d+(\.\d+)?$", s) else None


def norm_key(text):
    """Khoá so trùng ĐỀ BÀI: bỏ khoảng trắng và dấu câu, hạ chữ thường."""
    return re.sub(r"[^0-9a-zÀ-ỹ]+", "", text.lower())


def norm_choice(text):
    """
    Khoá so trùng PHƯƠNG ÁN: chỉ gộp khoảng trắng và hạ chữ thường.
    Không được bỏ dấu câu, vì với phương án thì "1" và "-1" là hai giá trị khác nhau.
    """
    return re.sub(r"\s+", "", text).lower()


def check_variant_cap(questions, where, p):
    """Mỗi dạng bài tối đa MAX_VARIANTS biến thể, và các biến thể phải khác nhau."""
    by_dang = defaultdict(list)
    for q in questions:
        by_dang[q.get("dang", "?")].append(q)
    for dang, group in sorted(by_dang.items()):
        if len(group) > MAX_VARIANTS:
            p.error(where, 'dang "%s" co %d bien the, vuot muc toi da %d'
                    % (dang, len(group), MAX_VARIANTS))
        keys = [norm_key(q["question"]) for q in group]
        dup = [k for k, n in Counter(keys).items() if n > 1]
        if dup:
            p.error(where, 'dang "%s" co %d de trung nguyen van' % (dang, len(dup)))


def check_levels(questions, expected, where, p):
    got = Counter(q["level"] for q in questions)
    for lv in sorted(expected):
        if got.get(lv, 0) != expected[lv]:
            p.error(where, "muc do %s co %d cau, can %d" % (lv, got.get(lv, 0), expected[lv]))
    extra = set(got) - set(expected)
    if extra:
        p.error(where, "muc do la: %s" % sorted(extra))


def build_mc(subject, chapter, raw, valid_lessons, rng, p):
    out = []
    for n, q in enumerate(raw, 1):
        qid = "mc-%s-%03d" % (chapter, n)
        where = "%s/%s" % (subject, qid)

        choices = list(q.get("choices") or [])
        ans = q.get("answer")
        if len(choices) != 4:
            p.error(where, "co %d phuong an, can dung 4" % len(choices))
            continue
        if not isinstance(ans, int) or isinstance(ans, bool) or not 0 <= ans < 4:
            p.error(where, "chi so dap an khong hop le: %r" % (ans,))
            continue

        # Trộn phương án bằng seed cố định để đáp án không dồn về vị trí A.
        correct = choices[ans]
        order = list(range(4))
        rng.shuffle(order)
        choices = [q["choices"][i] for i in order]
        ans = choices.index(correct)

        if len(set(norm_choice(c) for c in choices)) != 4:
            p.error(where, "co phuong an trung noi dung nhau")

        check_display_text(q["question"], where + "/de", p)
        for c in choices:
            check_display_text(c, where + "/phuong-an", p)
        check_display_text(q["explanation"], where + "/loi-giai", p)

        lesson = q.get("lesson")
        if lesson not in valid_lessons:
            p.error(where, "lesson %r khong thuoc chuong %s (hop le: %s)"
                    % (lesson, chapter, sorted(valid_lessons)))
            lesson = sorted(valid_lessons)[0]

        out.append({
            "id": qid,
            "chapter": chapter,
            "lesson": lesson,
            "level": q["level"],
            "dang": q["dang"],
            "question": q["question"],
            "choices": choices,
            "answer": ans,
            "explanation": q["explanation"],
        })
    return out


def build_short(subject, chapter, raw, valid_lessons, p):
    out = []
    for n, q in enumerate(raw, 1):
        qid = "sa-%s-%03d" % (chapter, n)
        where = "%s/%s" % (subject, qid)

        answer = str(q.get("answer", "")).strip()
        value = parse_number(answer)
        if value is None:
            p.error(where, "dap an %r khong doc duoc thanh so - hoc sinh se luon bi cham sai"
                    % answer)
            continue
        if not re.match(r"^-?\d+(\.\d+)?$", answer):
            p.error(where, "dap an %r phai la so thuan dung dau cham thap phan" % answer)

        try:
            tol = float(q.get("tolerance", 0) or 0)
        except (TypeError, ValueError):
            tol = 0.0

        is_decimal = "." in answer
        if is_decimal and tol <= 0:
            p.error(where, "dap so thap phan %s nhung tolerance = 0; hoc sinh nop dap so "
                           "chua lam tron se bi cham sai" % answer)
        if is_decimal and "lam tron" not in _no_accent(q["question"]).lower():
            p.warn(where, "dap so thap phan nhung de khong noi ro cach lam tron")
        if tol < 0:
            p.error(where, "tolerance am: %r" % tol)
        if tol and tol >= max(abs(value), 1.0) * 0.5:
            p.error(where, "tolerance %s qua rong so voi dap so %s, gan dung cung duoc diem"
                    % (tol, answer))

        check_display_text(q["question"], where + "/de", p)
        check_display_text(q["explanation"], where + "/loi-giai", p)
        unit = (q.get("unit") or "").strip()
        if unit:
            check_latex(unit, where + "/don-vi", p)

        lesson = q.get("lesson")
        if lesson not in valid_lessons:
            p.error(where, "lesson %r khong thuoc chuong %s (hop le: %s)"
                    % (lesson, chapter, sorted(valid_lessons)))
            lesson = sorted(valid_lessons)[0]

        item = {
            "id": qid,
            "chapter": chapter,
            "lesson": lesson,
            "level": q["level"],
            "dang": q["dang"],
            "question": q["question"],
            "answer": answer,
            "explanation": q["explanation"],
        }
        if tol > 0:
            item["tolerance"] = tol
        if unit:
            item["unit"] = unit
        out.append(item)
    return out


_ACCENTS = {
    "àáạảãâầấậẩẫ"
    "ăằắặẳẵ": "a",
    "èéẹẻẽêềếệểễ": "e",
    "ìíịỉĩ": "i",
    "òóọỏõôồốộổỗ"
    "ơờớợởỡ": "o",
    "ùúụủũưừứựửữ": "u",
    "ỳýỵỷỹ": "y",
    "đ": "d",
}


def _no_accent(text):
    """Bỏ dấu tiếng Việt, để so khớp cụm 'làm tròn' không phụ thuộc cách gõ."""
    out = []
    for ch in text.lower():
        for group, plain in _ACCENTS.items():
            if ch in group:
                ch = plain
                break
        out.append(ch)
    return "".join(out)


def cross_check_duplicates(subject, kind, questions, p):
    """Không cho hai câu trùng đề trên toàn môn, kể cả khác chương."""
    seen = defaultdict(list)
    for q in questions:
        seen[norm_key(q["question"])].append(q["id"])
    for ids in seen.values():
        if len(ids) > 1:
            p.error("%s/%s" % (subject, kind), "trung de giua cac cau: %s" % ", ".join(ids))


def save_json(path, data):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    check_only = "--check" in sys.argv
    p = Problems()
    built = {}

    for subject in SUBJECTS:
        index_path = os.path.join(DATA_DIR, subject, "index.json")
        with open(index_path, encoding="utf-8") as f:
            index = json.load(f)
        lessons_of = dict((ch["id"], set(l["id"] for l in ch["lessons"]))
                          for ch in index["chapters"])

        mc_all, sa_all, title_updates = [], [], []

        for chapter in CHAPTERS:
            bank_path = os.path.join(BANK_DIR, "%s_%s.json" % (subject, chapter))
            if not os.path.exists(bank_path):
                p.error("%s/%s" % (subject, chapter), "thieu file ngan hang %s" % bank_path)
                continue
            with open(bank_path, encoding="utf-8") as f:
                bank = json.load(f)

            valid = lessons_of.get(chapter, set())
            rng = random.Random("%s|%s|%d" % (subject, chapter, SEED))

            mc_raw = bank.get("mc", [])
            sa_raw = bank.get("short", [])
            if len(mc_raw) != MC_PER_CHAPTER:
                p.error("%s/%s" % (subject, chapter),
                        "co %d cau trac nghiem, can %d" % (len(mc_raw), MC_PER_CHAPTER))
            if len(sa_raw) != SA_PER_CHAPTER:
                p.error("%s/%s" % (subject, chapter),
                        "co %d cau tra loi ngan, can %d" % (len(sa_raw), SA_PER_CHAPTER))

            mc = build_mc(subject, chapter, mc_raw, valid, rng, p)
            sa = build_short(subject, chapter, sa_raw, valid, p)

            check_levels(mc, MC_LEVELS, "%s/%s/mc" % (subject, chapter), p)
            check_levels(sa, SA_LEVELS, "%s/%s/short" % (subject, chapter), p)
            check_variant_cap(mc, "%s/%s/mc" % (subject, chapter), p)
            check_variant_cap(sa, "%s/%s/short" % (subject, chapter), p)

            mc_all.extend(mc)
            sa_all.extend(sa)

            for l in bank.get("sgk_lessons", []):
                title_updates.append((chapter, l["lesson_id"], l["sgk_title"]))
            if bank.get("sgk_chapter_title"):
                title_updates.append((chapter, None, bank["sgk_chapter_title"]))

        cross_check_duplicates(subject, "mc", mc_all, p)
        cross_check_duplicates(subject, "short", sa_all, p)
        built[subject] = (index, index_path, mc_all, sa_all, title_updates)

    # ------------------------------------------------------------------ báo cáo
    print("KIEM DINH")
    for subject in SUBJECTS:
        _, _, mc, sa, _ = built[subject]
        uniq_mc = len(set(norm_key(q["question"]) for q in mc))
        uniq_sa = len(set(norm_key(q["question"]) for q in sa))
        dang_mc = len(set(q["dang"] for q in mc))
        dang_sa = len(set(q["dang"] for q in sa))
        print("  %-8s TN %3d cau / %3d de khac / %3d dang | TLN %3d cau / %3d de khac / %2d dang"
              % (subject, len(mc), uniq_mc, dang_mc, len(sa), uniq_sa, dang_sa))

    if p.warnings:
        print("\nCANH BAO (%d):" % len(p.warnings))
        for w in p.warnings[:40]:
            print("  ! " + w)
        if len(p.warnings) > 40:
            print("  ... con %d canh bao nua" % (len(p.warnings) - 40))

    if p.errors:
        print("\nLOI (%d) - KHONG GHI DU LIEU:" % len(p.errors))
        for e in p.errors[:80]:
            print("  x " + e)
        if len(p.errors) > 80:
            print("  ... con %d loi nua" % (len(p.errors) - 80))
        return 1

    if check_only:
        print("\nOK - chi kiem dinh, khong ghi file.")
        return 0

    # ------------------------------------------------------------------ ghi file
    for subject in SUBJECTS:
        index, index_path, mc, sa, title_updates = built[subject]
        save_json(os.path.join(DATA_DIR, subject, "questions", "mc.json"), {"questions": mc})
        save_json(os.path.join(DATA_DIR, subject, "questions", "short.json"), {"questions": sa})

        # Đồng bộ tiêu đề bài/chương theo đúng SGK.
        by_ch = dict((ch["id"], ch) for ch in index["chapters"])
        for chapter, lesson_id, title in title_updates:
            ch = by_ch.get(chapter)
            if not ch:
                continue
            if lesson_id is None:
                ch["title"] = title
            else:
                for l in ch["lessons"]:
                    if l["id"] == lesson_id:
                        l["title"] = title
        save_json(index_path, index)

        # Tiêu đề trong file lý thuyết phải khớp index để sidebar và H1 không lệch nhau.
        for ch in index["chapters"]:
            tpath = os.path.join(DATA_DIR, subject, ch["theory"])
            if not os.path.exists(tpath):
                continue
            with open(tpath, encoding="utf-8") as f:
                theory = json.load(f)
            theory["title"] = ch["title"]
            titles = dict((l["id"], l["title"]) for l in ch["lessons"])
            for l in theory.get("lessons", []):
                if l["id"] in titles:
                    l["title"] = titles[l["id"]]
            save_json(tpath, theory)

        print("Da ghi %s: %d TN + %d TLN" % (subject, len(mc), len(sa)))

    total = sum(len(built[s][2]) + len(built[s][3]) for s in SUBJECTS)
    print("\nTONG: %d cau hoi." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
