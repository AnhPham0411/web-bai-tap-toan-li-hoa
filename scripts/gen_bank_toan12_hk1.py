# -*- coding: utf-8 -*-
"""
Master runner để sinh toàn diện ngân hàng câu hỏi Toán 12 Học kì 1 (Chương 1 - 3).
Chuẩn chương trình GDPT 2018 (SGK Kết nối tri thức với cuộc sống).
Mỗi chương gồm:
- 120 câu Trắc nghiệm (60 nb / 48 th / 12 vd)
- 30 câu Trả lời ngắn (15 nb / 12 th / 3 vd)
Tổng cộng: 450 câu hỏi.
"""
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.toan12_builder.c1 import gen_c1
from scripts.toan12_builder.c2 import gen_c2
from scripts.toan12_builder.c3 import gen_c3

def main():
    print("BAT DAU SINH NGAN HANG CAU HOI TOAN 12 HK1 (3 CHUONG)...")
    gen_c1()
    gen_c2()
    gen_c3()
    print("HOAN TAT SINH NGAN HANG CAU HOI TOAN 12 HK1 (450 CAU HOI)!")

if __name__ == "__main__":
    main()
