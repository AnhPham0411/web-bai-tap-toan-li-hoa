#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_static_toan10.py - Static Validation Engine for Toan 10 Question Bank.
Scans for schema integrity, missing fields, choices/answer bounds, and LaTeX syntax anomalies.
"""

import os
import sys
import json
import re

def check_latex_syntax(text):
    """
    Checks for unbalanced dollar signs and common LaTeX malformations.
    Returns (has_error: bool, message: str).
    """
    if not isinstance(text, str):
        return False, ""

    # Count unescaped dollar signs
    # Negative lookbehind for backslash: (?<!\\)\$
    dollars = re.findall(r'(?<!\\)\$', text)
    if len(dollars) % 2 != 0:
        return True, f"Unbalanced LaTeX dollar signs (found {len(dollars)})"

    # Check for curly brace balance inside math blocks $...$
    math_blocks = re.findall(r'\$(.*?)\$', text, flags=re.DOTALL)
    for block in math_blocks:
        open_braces = block.count('{')
        close_braces = block.count('}')
        if open_braces != close_braces:
            return True, f"Unbalanced curly braces in LaTeX: '{{{open_braces}}}' vs '{{{close_braces}}}' in '${block[:30]}...$'"
        if r'\over ' in block or block.endswith(r'\over'):
            return True, f"Deprecated LaTeX \\over command found in '${block[:30]}...$'"

    return False, ""

def validate_question(q, is_short=False):
    """
    Validates a single question dictionary.
    Returns a list of issue dicts: [{severity, type, message, field}]
    """
    issues = []
    qid = q.get('id', 'UNKNOWN_ID')

    # 1. Required fields
    required_common = ['id', 'chapter', 'lesson', 'level', 'dang', 'question', 'answer', 'explanation']
    if not is_short:
        required_common.append('choices')

    for field in required_common:
        if field not in q or q[field] is None:
            issues.append({
                "severity": "CRITICAL",
                "type": "missing_field",
                "field": field,
                "message": f"Missing required field '{field}' in {qid}"
            })
        elif isinstance(q[field], str) and not q[field].strip():
            issues.append({
                "severity": "CRITICAL",
                "type": "empty_field",
                "field": field,
                "message": f"Field '{field}' is empty in {qid}"
            })

    # 2. Specific checks for Multiple Choice
    if not is_short and 'choices' in q:
        choices = q['choices']
        if not isinstance(choices, list) or len(choices) != 4:
            issues.append({
                "severity": "CRITICAL",
                "type": "invalid_choices_count",
                "field": "choices",
                "message": f"Multiple choice must have exactly 4 choices, found {len(choices) if isinstance(choices, list) else 'not a list'} in {qid}"
            })
        else:
            # Check for duplicate choices
            clean_choices = [str(c).strip() for c in choices]
            if len(set(clean_choices)) < len(clean_choices):
                issues.append({
                    "severity": "CRITICAL",
                    "type": "duplicate_choices",
                    "field": "choices",
                    "message": f"Duplicate choice values detected in {qid}"
                })

        if 'answer' in q and q['answer'] is not None:
            ans = q['answer']
            if not isinstance(ans, int) or ans < 0 or ans > 3:
                issues.append({
                    "severity": "CRITICAL",
                    "type": "invalid_answer_bound",
                    "field": "answer",
                    "message": f"Answer index must be integer in range 0..3, got {ans} in {qid}"
                })

    # 3. Specific checks for Short Answer
    if is_short and 'answer' in q:
        ans = q['answer']
        if ans is None or (isinstance(ans, str) and not str(ans).strip()):
            issues.append({
                "severity": "CRITICAL",
                "type": "empty_short_answer",
                "field": "answer",
                "message": f"Short answer is empty in {qid}"
            })

    # 4. LaTeX checks across all string fields
    text_fields = ['question', 'explanation']
    if not is_short and isinstance(q.get('choices'), list):
        for idx, ch in enumerate(q['choices']):
            if isinstance(ch, str):
                has_err, msg = check_latex_syntax(ch)
                if has_err:
                    issues.append({
                        "severity": "WARNING",
                        "type": "latex_syntax_error",
                        "field": f"choices[{idx}]",
                        "message": f"{msg} in {qid}"
                    })

    for field in text_fields:
        val = q.get(field)
        if isinstance(val, str):
            has_err, msg = check_latex_syntax(val)
            if has_err:
                issues.append({
                    "severity": "WARNING",
                    "type": "latex_syntax_error",
                    "field": field,
                    "message": f"{msg} in {qid}"
                })

    return issues

def scan_questions_file(file_path, is_short=False):
    """
    Reads a questions JSON file and validates each question.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    results = []
    for q in questions:
        q_issues = validate_question(q, is_short=is_short)
        if q_issues:
            results.append({
                "id": q.get('id', 'UNKNOWN'),
                "issues": q_issues
            })
    return questions, results

def run_static_audit(base_dir):
    """
    Runs static audit for toan10 mc.json and short.json.
    """
    mc_path = os.path.join(base_dir, 'data', 'toan10', 'questions', 'mc.json')
    short_path = os.path.join(base_dir, 'data', 'toan10', 'questions', 'short.json')

    mc_questions, mc_issues = scan_questions_file(mc_path, is_short=False)
    short_questions, short_issues = scan_questions_file(short_path, is_short=True)

    summary = {
        "mc_count": len(mc_questions),
        "short_count": len(short_questions),
        "total_scanned": len(mc_questions) + len(short_questions),
        "mc_defect_count": len(mc_issues),
        "short_defect_count": len(short_issues),
        "total_defect_count": len(mc_issues) + len(short_issues),
        "mc_defects": mc_issues,
        "short_defects": short_issues
    }
    return summary

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    res = run_static_audit(base_dir)
    out_dir = os.path.join(base_dir, 'artifacts', 'audit')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'static_audit_results.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f"Static audit completed. Scanned: {res['total_scanned']} questions. Defects found: {res['total_defect_count']}")
    print(f"Results saved to: {out_file}")
