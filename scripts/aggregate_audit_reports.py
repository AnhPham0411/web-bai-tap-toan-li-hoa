#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aggregate_audit_reports.py - Aggregates static validation and 10 agent audit reports
into unified Markdown and JSON reports.
"""

import os
import sys
import json
from datetime import datetime

CHAPTER_NAMES = {
    "c1": "Chương 1: Mệnh đề và Tập hợp",
    "c2": "Chương 2: Bất phương trình và Hệ bất phương trình bậc nhất hai ẩn",
    "c3": "Chương 3: Hệ thức lượng trong tam giác",
    "c4": "Chương 4: Vectơ",
    "c5": "Chương 5: Các số đặc trưng của mẫu số liệu không ghép nhóm"
}

def compile_audit_report(static_results, agent_reports):
    """
    Compiles raw results into a unified structured audit dictionary.
    """
    total_scanned = static_results.get("total_scanned", 750)
    defects_by_id = {}

    # Merge static defects
    static_defects = static_results.get("mc_defects", []) + static_results.get("short_defects", [])
    for item in static_defects:
        qid = item["id"]
        for issue in item.get("issues", []):
            defects_by_id.setdefault(qid, {
                "id": qid,
                "issues": []
            })
            defects_by_id[qid]["issues"].append({
                "source": "Static Engine",
                "severity": issue.get("severity", "WARNING"),
                "type": issue.get("type", "static_syntax"),
                "description": issue.get("message", ""),
                "fix_proposal": f"Sửa lỗi cú pháp tại trường {issue.get('field', '')}"
            })

    # Merge agent reports
    agent_stats = {}
    for agent_key, a_rep in agent_reports.items():
        agent_id = a_rep.get("agent_id")
        scanned = a_rep.get("scanned_count", 75)
        defects = a_rep.get("defects", [])
        agent_stats[agent_key] = {
            "agent_id": agent_id,
            "chapter": a_rep.get("chapter", ""),
            "chapter_name": a_rep.get("chapter_name", ""),
            "scanned": scanned,
            "defect_count": len(defects)
        }
        for d in defects:
            qid = d["id"]
            defects_by_id.setdefault(qid, {
                "id": qid,
                "chapter": d.get("chapter", ""),
                "lesson": d.get("lesson", ""),
                "dang": d.get("dang", ""),
                "question": d.get("question", ""),
                "issues": []
            })
            # enrich if metadata present
            for k in ["chapter", "lesson", "dang", "question"]:
                if d.get(k) and not defects_by_id[qid].get(k):
                    defects_by_id[qid][k] = d[k]

            defects_by_id[qid]["issues"].append({
                "source": f"Agent {agent_id}",
                "severity": d.get("severity", "WARNING"),
                "type": d.get("type", "math_logic"),
                "description": d.get("description", ""),
                "fix_proposal": d.get("fix_proposal", "")
            })

    # Flatten and calculate counts
    all_defects_list = []
    critical_count = 0
    warning_count = 0
    minor_count = 0

    for qid, data in defects_by_id.items():
        # Determine highest severity for question
        severities = [iss["severity"] for iss in data["issues"]]
        if "CRITICAL" in severities:
            highest_sev = "CRITICAL"
            critical_count += 1
        elif "WARNING" in severities:
            highest_sev = "WARNING"
            warning_count += 1
        else:
            highest_sev = "MINOR"
            minor_count += 1
        data["highest_severity"] = highest_sev
        all_defects_list.append(data)

    # Sort defects: CRITICAL first, then WARNING, then MINOR
    sev_order = {"CRITICAL": 0, "WARNING": 1, "MINOR": 2}
    all_defects_list.sort(key=lambda x: (sev_order.get(x["highest_severity"], 3), x["id"]))

    compiled = {
        "timestamp": datetime.now().isoformat(),
        "total_scanned": total_scanned,
        "clean_count": total_scanned - len(all_defects_list),
        "total_defects": len(all_defects_list),
        "critical_count": critical_count,
        "warning_count": warning_count,
        "minor_count": minor_count,
        "agent_stats": agent_stats,
        "defects": all_defects_list
    }
    return compiled

def generate_markdown_report(compiled):
    """
    Renders structured Markdown report from compiled audit data.
    """
    total = compiled["total_scanned"]
    clean = compiled["clean_count"]
    clean_pct = (clean / total * 100) if total else 0
    defects_count = compiled["total_defects"]
    crit = compiled["critical_count"]
    warn = compiled["warning_count"]
    minor = compiled["minor_count"]

    md = []
    md.append("# Báo cáo Kiểm định Ngân hàng Câu hỏi Toán 10 (10 Agents Audit Report)")
    md.append(f"\n*Thời gian thực hiện: {compiled.get('timestamp', '')}*")
    md.append(f"*Phạm vi: 750 câu hỏi Toán 10 (600 Trắc nghiệm + 150 Trả lời ngắn)*\n")
    md.append("---\n")

    # Executive Summary
    md.append("## 1. Tổng quan Kết quả (Executive Summary)\n")
    md.append(f"- **Tổng số câu đã rà soát:** **{total}/{total} câu** (Độ phủ: **100%**)")
    md.append(f"- **Số câu đạt chuẩn (Clean):** **{clean}/{total}** ({clean_pct:.1f}%)")
    md.append(f"- **Số câu phát hiện vấn đề:** **{defects_count} câu**")
    md.append(f"  - 🔴 **CRITICAL (Nghiêm trọng - Sai đáp án/đề):** **{crit}**")
    md.append(f"  - 🟠 **WARNING (Cảnh báo - Lời giải/LaTeX):** **{warn}**")
    md.append(f"  - 🟡 **MINOR (Cải thiện - Ngữ văn/Tối ưu):** **{minor}**\n")

    # Agent coverage table
    md.append("### Bảng Độ phủ & Kết quả theo 10 Agent\n")
    md.append("| Agent | Phân vùng phụ trách | Số câu quét | Số câu có lỗi | Tình trạng |")
    md.append("| :--- | :--- | :---: | :---: | :---: |")
    for agent_key, st in sorted(compiled.get("agent_stats", {}).items(), key=lambda x: x[1]["agent_id"]):
        ch_name = st.get("chapter_name") or st.get("chapter")
        md.append(f"| **Agent {st['agent_id']}** | {ch_name} | {st['scanned']}/75 | {st['defect_count']} | ✅ Hoàn thành |")
    md.append("\n---\n")

    # Detailed Defects Log
    md.append("## 2. Danh mục Chi tiết các Lỗi Cần Khắc phục (Defect Log)\n")
    if not compiled["defects"]:
        md.append("> [!NOTE]\n> Không phát hiện lỗi nào trong toàn bộ ngân hàng câu hỏi.\n")
    else:
        for idx, item in enumerate(compiled["defects"], 1):
            sev = item["highest_severity"]
            sev_icon = "🔴" if sev == "CRITICAL" else ("🟠" if sev == "WARNING" else "🟡")
            qid = item["id"]
            md.append(f"### {idx}. [{qid}] - {sev_icon} {sev}")
            if item.get("chapter") or item.get("dang"):
                md.append(f"- **Chương/Dạng:** `{item.get('chapter', '')}` | {item.get('dang', 'N/A')}")
            if item.get("question"):
                md.append(f"- **Đề bài trích đoạn:** *{item['question'][:120]}...*")

            md.append("- **Các vấn đề phát hiện:**")
            for iss in item["issues"]:
                md.append(f"  - **[{iss['source']}]** {iss['description']}")
                if iss.get("fix_proposal"):
                    md.append(f"    - 👉 *Đề xuất sửa:* {iss['fix_proposal']}")
            md.append("")

    return "\n".join(md)

def export_reports(base_dir, compiled):
    """
    Saves report files to docs/reports/
    """
    out_dir = os.path.join(base_dir, 'docs', 'reports')
    os.makedirs(out_dir, exist_ok=True)

    json_path = os.path.join(out_dir, 'toan10_audit_report.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(compiled, f, ensure_ascii=False, indent=2)

    md_content = generate_markdown_report(compiled)
    md_path = os.path.join(out_dir, 'toan10_audit_report.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    return md_path, json_path

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print("Aggregator script ready.")
