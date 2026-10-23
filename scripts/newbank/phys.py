# -*- coding: utf-8 -*-
"""Tiện ích chung cho Lý/Hóa: định dạng số kiểu Việt Nam, sinh đáp án nhiễu từ lỗi hay gặp."""
from fractions import Fraction
from .common import fnum

def fmt(x, u='', nd=2):
    s = fnum(float(x), nd)
    return f"{s} {u}".strip()

def nm(b, lesson, level, dang, stem, correct, cands, u, expl, nd=2):
    """Trắc nghiệm đáp án số: đáp án nhiễu là các giá trị `cands` (lỗi thường gặp), tự bổ sung bội số nếu thiếu."""
    if len(expl) < 60 and expl.startswith("$"): expl = "Áp dụng công thức, ta có: " + expl
    if len(expl) < 60 and not expl.startswith("$") and not expl.startswith("Áp dụng"): expl = "Lời giải: " + expl
    c = fmt(correct, u, nd)
    seen, ws = {c}, []
    extra = [correct * f for f in (2, 0.5, 1.5, 3, 4, 0.25, 1.25, 5)]
    for x in list(cands) + extra:
        s = fmt(x, u, nd)
        if s in seen: continue
        if float(x) <= 0 and float(correct) > 0: continue
        seen.add(s); ws.append(s)
        if len(ws) >= 3: break
    b.mc(lesson, level, dang, stem, c, ws, expl)

def sa(b, lesson, level, dang, stem, ans, expl, u=None):
    if len(expl) < 60 and expl.startswith("$"): expl = "Áp dụng công thức, ta có: " + expl
    if len(expl) < 60 and not expl.startswith("$") and not expl.startswith("Áp dụng"): expl = "Lời giải: " + expl
    a = float(ans)
    ex = abs(a - round(a)) < 1e-9
    assert abs(a - round(a, 2)) < 1e-9, f"đáp số không tròn 2 chữ số: {stem[:60]} = {a}"
    b.sa(lesson, level, dang, stem, a, expl, tol=None if ex else 0.01, unit=u)
