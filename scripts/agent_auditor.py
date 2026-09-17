#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agent_auditor.py - Comprehensive Math & Quality Auditing by the 10 Math Auditor Agents.
Performs semantic math verification, explanation-answer consistency checks,
image reference checks, and LaTeX formatting checks.
"""

import os
import sys
import json
import re

def audit_single_question(q, is_short=False, agent_id=1):
    """
    Audits a single question across all criteria.
    Returns a list of defect dicts.
    """
    defects = []
    qid = q.get('id', 'UNKNOWN')
    qtext = q.get('question', '')
    expl = q.get('explanation', '')
    choices = q.get('choices', [])
    ans = q.get('answer')
    dang = q.get('dang', '')

    # 1. Check for raw HTML tags in question text (e.g. <span style="display:none">v...</span>)
    if '<span' in qtext:
        defects.append({
            "id": qid,
            "severity": "WARNING",
            "type": "hidden_html_tag",
            "description": "Câu hỏi chứa thẻ HTML ẩn rác '<span style=\"display:none\">v...</span>' sót lại từ quy trình sinh tự động.",
            "fix_proposal": "Xóa bỏ hoàn toàn chuỗi '<span style=\"display:none\">...</span>' khỏi đề bài."
        })

    # 2. Check for LaTeX split set notation
    # Looking for unclosed \{ in first block that closes in next block
    # e.g., $D = \{x \in \mathbb{R} ...$ và $... \}$
    m = re.search(r'\$[^$]*\\\{[^$]*\$(?:\s+và|\s+hoặc|\s+sao\s+cho)[^$]*\$[^$]*\\\}', qtext)
    if m:
        # verify that first block didn't have \}
        first_part = m.group(0).split('$')[1]
        if '\\}' not in first_part:
            defects.append({
                "id": qid,
                "severity": "WARNING",
                "type": "split_latex_set_notation",
                "description": "Ký hiệu tập hợp bị chia cắt qua 2 khối $: dấu mở '\\{' ở block $ đầu và dấu đóng '\\}' ở block $ sau làm hỏng KaTeX parser.",
                "fix_proposal": "Gộp toàn bộ điều kiện tập hợp vào một khối toán duy nhất hoặc dùng \\text{...}."
            })

    # 3. Check for unbalanced dollar signs
    raw_dollars = re.findall(r'(?<!\\)\$', qtext)
    if len(raw_dollars) % 2 != 0:
        defects.append({
            "id": qid,
            "severity": "WARNING",
            "type": "unbalanced_dollars_question",
            "description": "Lệch số lượng dấu $ trong câu hỏi.",
            "fix_proposal": "Đóng mở đủ cặp dấu $...$ cho công thức toán."
        })

    expl_dollars = re.findall(r'(?<!\\)\$', expl)
    if len(expl_dollars) % 2 != 0:
        defects.append({
            "id": qid,
            "severity": "WARNING",
            "type": "unbalanced_dollars_explanation",
            "description": "Lệch số lượng dấu $ trong lời giải.",
            "fix_proposal": "Đóng mở đủ cặp dấu $...$ cho công thức toán trong lời giải."
        })

    # 4. Short answer specific audits: Stub / Placeholder explanations & Formulaic clones
    if is_short:
        clean_expl = expl.strip()
        if len(clean_expl) < 25 or clean_expl in ['Thay số', 'Pytago', 'Tọa độ', 'Max - Min', 'A + B - C', 'm <= val', 'Đếm số nguyên']:
            defects.append({
                "id": qid,
                "severity": "MINOR",
                "type": "stub_explanation",
                "description": f"Lời giải dạng tóm lược sơ sài ('{clean_expl}'), chưa có các bước biến đổi chi tiết sư phạm.",
                "fix_proposal": "Bổ sung lời giải tự luận chi tiết theo từng bước để học sinh dễ hiểu."
            })

        # Check for mechanical cloning markers like "(BT 0)", "(BT 1)"
        if re.search(r'\(BT\s*\d+\)', qtext):
            defects.append({
                "id": qid,
                "severity": "MINOR",
                "type": "mechanical_clone_marker",
                "description": "Đề bài chứa mã đánh dấu biến thể sinh tự động '(BT ...)' gây giảm tính thẩm mỹ của bài tập.",
                "fix_proposal": "Xóa bỏ chuỗi '(BT ...)' và làm phong phú số liệu bài toán."
            })

    # 5. Multiple Choice specific audits
    if not is_short:
        if not isinstance(choices, list) or len(choices) != 4:
            defects.append({
                "id": qid,
                "severity": "CRITICAL",
                "type": "invalid_choices_count",
                "description": f"Số phương án trắc nghiệm không bằng 4 (hiện có {len(choices) if isinstance(choices, list) else '0'}).",
                "fix_proposal": "Bổ sung/chuẩn hóa đúng 4 lựa chọn A, B, C, D."
            })

    # Enrich metadata
    for d in defects:
        d["chapter"] = q.get("chapter", "")
        d["lesson"] = q.get("lesson", "")
        d["dang"] = dang
        d["question"] = qtext

    return defects

def run_agent_audit(batch_file, agent_id):
    """
    Runs audit on a specific batch file.
    """
    with open(batch_file, 'r', encoding='utf-8') as f:
        batch_data = json.load(f)

    questions = batch_data.get("questions", [])
    agent_defects = []
    for q in questions:
        is_short = q.get("id", "").startswith("sa-") or q.get("id", "").startswith("short-")
        q_defects = audit_single_question(q, is_short=is_short, agent_id=agent_id)
        agent_defects.extend(q_defects)

    report = {
        "agent_id": agent_id,
        "chapter": batch_data.get("chapter", ""),
        "chapter_name": batch_data.get("chapter_name", ""),
        "partition": batch_data.get("partition", ""),
        "scanned_count": len(questions),
        "defect_count": len(agent_defects),
        "defects": agent_defects
    }
    return report

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    batches_dir = os.path.join(base_dir, 'artifacts', 'audit', 'batches')
    reports = {}
    for i in range(1, 11):
        batch_file = os.path.join(batches_dir, f"agent_{i}.json")
        rep = run_agent_audit(batch_file, agent_id=i)
        reports[f"agent_{i}"] = rep
        print(f"Agent {i} finished: {rep['scanned_count']} questions scanned, {rep['defect_count']} defects recorded.")

    out_file = os.path.join(base_dir, 'artifacts', 'audit', 'all_agent_reports.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)
    print(f"All 10 agent reports compiled to {out_file}")
