# -*- coding: utf-8 -*-
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANK_DIR = os.path.join(BASE_DIR, "scripts", "bank")

def make_unique_choices(choices):
    assert len(choices) == 4, f"Cần đúng 4 phương án, nhận {len(choices)}"
    clean = [str(c).strip() for c in choices]
    assert len(set(clean)) == 4, f"Có phương án trùng nhau: {clean}"
    return clean

def save_bank(chapter_id, sgk_title, sgk_lessons, mc, sa):
    assert len(mc) == 120, f"MC cần 120 câu, hiện có {len(mc)}"
    assert len(sa) == 30, f"SA cần 30 câu, hiện có {len(sa)}"

    data = {
        "sgk_chapter_title": sgk_title,
        "sgk_lessons": sgk_lessons,
        "sources": ["Biên soạn theo chương trình GDPT 2018 SGK Kết nối tri thức"],
        "mc": mc,
        "short": sa
    }
    filepath = os.path.join(BANK_DIR, f"toan12_{chapter_id}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"-> Tao thanh cong toan12_{chapter_id}.json ({len(mc)} TN, {len(sa)} TLN)")
