#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_banks_deep.py - Kiểm tra toán học, cú pháp LaTeX và đáp án chuyên sâu.
Quét toàn bộ ngân hàng câu hỏi trong data/*/questions/ và scripts/bank/.
"""

import os
import sys
import json
import re
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent

# Các lệnh LaTeX không tương thích với math.js
UNSUPPORTED_LATEX = [
    r'\begin{cases}', r'\end{cases}',
    r'\begin{matrix}', r'\end{matrix}',
    r'\begin{aligned}', r'\end{aligned}',
    r'\over ',
    r'\pmatrix',
]

def check_latex(text, context=""):
    errors = []
    if not isinstance(text, str):
        return errors

    # 1. Đếm dấu $
    dollars = re.findall(r'(?<!\\)\$', text)
    if len(dollars) % 2 != 0:
        errors.append(f"Dấu $ không cân xứng ({len(dollars)} dấu $) trong {context}")

    # 2. Khối math $...$
    math_blocks = re.findall(r'\$(.*?)\$', text, flags=re.DOTALL)
    for b in math_blocks:
        if b.count('{') != b.count('}'):
            errors.append(f"Ngoặc nhọn không cân xứng trong '${b[:40]}...' ({context})")
        for bad in UNSUPPORTED_LATEX:
            if bad in b:
                errors.append(f"Cú pháp LaTeX '{bad}' không được math.js hỗ trợ trong '${b[:40]}...' ({context})")
        # Kiểm tra dấu gạch chéo ngược lẻ
        odd_slash = re.search(r'\\[^a-zA-Z0-9_\{\}\%\\\,\;\:\$\s]', b)
        if odd_slash:
            char = odd_slash.group(0)
            errors.append(f"Ký tự escape lạ '{char}' trong '${b[:40]}...' ({context})")

    return errors

def audit_question(q, is_short=False, source=""):
    qid = q.get('id', 'NO_ID')
    issues = []

    # Kiểm tra trường bắt buộc
    for f in ['id', 'chapter', 'lesson', 'level', 'dang', 'question', 'answer', 'explanation']:
        if f not in q or q[f] is None:
            issues.append(f"[{qid}] Thiếu trường bắt buộc '{f}'")

    qtext = str(q.get('question', ''))
    expl = str(q.get('explanation', ''))
    ans = q.get('answer')

    # Kiểm tra LaTeX trong đề bài và lời giải
    issues.extend(check_latex(qtext, f"{qid} (question)"))
    issues.extend(check_latex(expl, f"{qid} (explanation)"))

    if not is_short:
        # TRẮC NGHIỆM
        choices = q.get('choices')
        if not isinstance(choices, list) or len(choices) != 4:
            issues.append(f"[{qid}] choices phải có đúng 4 phương án, hiện có {len(choices) if isinstance(choices, list) else 'không phải list'}")
        else:
            # Kiểm tra trùng lặp phương án
            normalized_choices = [str(c).strip().replace(' ', '') for c in choices]
            if len(set(normalized_choices)) < 4:
                issues.append(f"[{qid}] Có phương án trắc nghiệm bị trùng lặp: {choices}")

            # Kiểm tra LaTeX trong từng phương án
            for i, c in enumerate(choices):
                issues.extend(check_latex(str(c), f"{qid} choice[{i}]"))

        if not isinstance(ans, int) or ans < 0 or ans > 3:
            issues.append(f"[{qid}] answer trắc nghiệm phải là số nguyên 0..3, hiện là: {ans}")
        else:
            # Kiểm tra độ nhất quán trong lời giải (ví dụ lời giải ghi "Đáp án B" nhưng answer lại là 0 (A))
            ans_letters = ['A', 'B', 'C', 'D']
            # Tìm xem có ghi rõ ràng "Đáp án A", "chọn A", "Đáp án đúng là A"
            match = re.search(r'(?:Đáp án|Chọn|đáp án đúng là|đáp án:?)\s+([A-D])\b', expl, re.IGNORECASE)
            if match:
                stated_key = match.group(1).upper()
                expected_key = ans_letters[ans]
                if stated_key != expected_key:
                    issues.append(f"[{qid}] Lời giải ghi đáp án {stated_key} nhưng trường answer lại chỉ định {expected_key} ({ans})")

    else:
        # TRẢ LỜI NGẮN
        if ans is None:
            issues.append(f"[{qid}] answer không được để trống")
        else:
            # Phải là số hoặc chuỗi số
            try:
                float(str(ans).replace(',', '.'))
            except ValueError:
                issues.append(f"[{qid}] answer không phải là số hợp lệ: '{ans}'")

    return issues

def audit_file(filepath, is_short=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', data) if isinstance(data, dict) else data
    if not isinstance(questions, list):
        return [f"File {filepath} không chứa danh sách questions"]

    all_issues = []
    for q in questions:
        issues = audit_question(q, is_short=is_short, source=str(filepath))
        all_issues.extend(issues)
    return all_issues

def main():
    print("=" * 60)
    print("BAT DAU AUDIT CHUYEN SAU TOAN HOC & LATEX CAC BO DE")
    print("=" * 60)

    total_issues = 0

    subjects = ['toan10', 'ly10', 'hoa10', 'toan9', 'toan11', 'toan12']
    for subj in subjects:
        mc_file = ROOT / 'data' / subj / 'questions' / 'mc.json'
        short_file = ROOT / 'data' / subj / 'questions' / 'short.json'

        print(f"\n--- Đang kiểm tra môn: {subj} ---")
        if mc_file.exists():
            issues_mc = audit_file(mc_file, is_short=False)
            print(f"  Trắc nghiệm ({mc_file.name}): {len(issues_mc)} vấn đề")
            for iss in issues_mc[:10]:
                print(f"    - {iss}")
            if len(issues_mc) > 10:
                print(f"    ... và {len(issues_mc) - 10} vấn đề khác")
            total_issues += len(issues_mc)

        if short_file.exists():
            issues_short = audit_file(short_file, is_short=True)
            print(f"  Trả lời ngắn ({short_file.name}): {len(issues_short)} vấn đề")
            for iss in issues_short[:10]:
                print(f"    - {iss}")
            if len(issues_short) > 10:
                print(f"    ... và {len(issues_short) - 10} vấn đề khác")
            total_issues += len(issues_short)

    print("\n" + "=" * 60)
    if total_issues == 0:
        print("KET QUA: 100% HOAN HAO - 0 LOI DUOC PHAT HIEN!")
    else:
        print(f"KET QUA: Phat hien tong cong {total_issues} van de can xu ly!")
    print("=" * 60)
    return 0 if total_issues == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
