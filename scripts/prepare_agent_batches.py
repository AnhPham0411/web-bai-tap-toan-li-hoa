#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prepare_agent_batches.py - Partitions Toan 10 questions into exactly 10 agent batches.
Each agent receives exactly 75 questions aligned with chapter boundaries.
"""

import os
import sys
import json

CHAPTER_NAMES = {
    "c1": "Mệnh đề và Tập hợp",
    "c2": "Bất phương trình và Hệ bất phương trình bậc nhất hai ẩn",
    "c3": "Hệ thức lượng trong tam giác",
    "c4": "Vectơ",
    "c5": "Các số đặc trưng của mẫu số liệu không ghép nhóm"
}

def create_agent_batches(base_dir):
    """
    Loads mc.json and short.json for toan10, splits into 10 balanced batches of 75 questions.
    Returns dict: {"agent_1": {...}, "agent_2": {...}, ..., "agent_10": {...}}
    """
    mc_path = os.path.join(base_dir, 'data', 'toan10', 'questions', 'mc.json')
    short_path = os.path.join(base_dir, 'data', 'toan10', 'questions', 'short.json')

    with open(mc_path, 'r', encoding='utf-8') as f:
        mc_data = json.load(f).get('questions', [])

    with open(short_path, 'r', encoding='utf-8') as f:
        short_data = json.load(f).get('questions', [])

    # Group by chapter
    mc_by_ch = {}
    for q in mc_data:
        ch = q.get('chapter', 'c1')
        mc_by_ch.setdefault(ch, []).append(q)

    short_by_ch = {}
    for q in short_data:
        ch = q.get('chapter', 'c1')
        short_by_ch.setdefault(ch, []).append(q)

    batches = {}

    for ch_idx in range(1, 6):
        ch_key = f"c{ch_idx}"
        ch_name = CHAPTER_NAMES.get(ch_key, f"Chương {ch_idx}")
        ch_mc = mc_by_ch.get(ch_key, [])
        ch_short = short_by_ch.get(ch_key, [])

        # Agent Odd (1, 3, 5, 7, 9): First 75 MC questions
        agent_odd_id = 2 * ch_idx - 1
        agent_odd_key = f"agent_{agent_odd_id}"
        batches[agent_odd_key] = {
            "agent_id": agent_odd_id,
            "chapter": ch_key,
            "chapter_name": ch_name,
            "partition": "MC Part 1",
            "count": 75,
            "questions": ch_mc[:75]
        }

        # Agent Even (2, 4, 6, 8, 10): Remaining 45 MC questions + 30 Short questions
        agent_even_id = 2 * ch_idx
        agent_even_key = f"agent_{agent_even_id}"
        batches[agent_even_key] = {
            "agent_id": agent_even_id,
            "chapter": ch_key,
            "chapter_name": ch_name,
            "partition": "MC Part 2 + Short",
            "count": len(ch_mc[75:]) + len(ch_short),
            "questions": ch_mc[75:] + ch_short
        }

    return batches

def export_batches(base_dir, out_dir=None):
    """
    Exports each agent batch to a JSON file in artifacts/audit/batches/
    """
    if out_dir is None:
        out_dir = os.path.join(base_dir, 'artifacts', 'audit', 'batches')
    os.makedirs(out_dir, exist_ok=True)

    batches = create_agent_batches(base_dir)
    for agent_key, batch_data in batches.items():
        batch_file = os.path.join(out_dir, f"{agent_key}.json")
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, ensure_ascii=False, indent=2)

    index_file = os.path.join(out_dir, 'manifest.json')
    manifest = {
        agent_key: {
            "agent_id": b["agent_id"],
            "chapter": b["chapter"],
            "chapter_name": b["chapter_name"],
            "partition": b["partition"],
            "count": b["count"],
            "first_id": b["questions"][0]["id"] if b["questions"] else None,
            "last_id": b["questions"][-1]["id"] if b["questions"] else None
        }
        for agent_key, b in batches.items()
    }
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return out_dir

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    out_dir = export_batches(base_dir)
    print(f"Exported 10 agent batches successfully to {out_dir}")
