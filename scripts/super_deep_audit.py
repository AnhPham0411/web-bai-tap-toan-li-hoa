import json
import glob
import os
import re

def audit_deep():
    print("======================================================================")
    print("   KIỂM TRA TOÀN DIỆN HỆ THỐNG DỮ LIỆU & LOGIC (6 MÔN / 4.800 CÂU)")
    print("======================================================================\n")

    with open('data/manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    active_subjects = [s for s in manifest['subjects'] if s.get('available')]
    print(f"-> Môn học đang mở: {len(active_subjects)} môn ({[s['id'] for s in active_subjects]})")

    all_errors = []
    all_warnings = []
    stats = {}

    for subj in active_subjects:
        sid = subj['id']
        spath = subj['path']
        sname = subj['name']
        print(f"\n--- Đang rà soát: {sname} ({sid}) ---")

        # 1. Kiểm tra index.json
        index_path = f"data/{spath}/index.json"
        if not os.path.exists(index_path):
            all_errors.append(f"[{sid}] Thiếu file index: {index_path}")
            continue

        with open(index_path, 'r', encoding='utf-8') as f:
            idx = json.load(f)

        chapters = idx.get('chapters', [])
        ch_ids = [c['id'] for c in chapters]
        print(f"  + Số chương: {len(chapters)} chương ({ch_ids})")

        # Kiểm tra trùng ID chương
        if len(ch_ids) != len(set(ch_ids)):
            all_errors.append(f"[{sid}] Trùng lặp ID chương trong index.json!")

        total_lessons_subj = 0
        # 2. Kiểm tra từng file lý thuyết của từng chương
        for ch in chapters:
            cid = ch['id']
            theory_rel = ch.get('theory')
            if not theory_rel:
                all_errors.append(f"[{sid}][{cid}] Chương không khai báo trường theory!")
                continue

            theory_path = f"data/{spath}/{theory_rel}"
            if not os.path.exists(theory_path):
                all_errors.append(f"[{sid}][{cid}] File lý thuyết không tồn tại: {theory_path}")
                continue

            with open(theory_path, 'r', encoding='utf-8') as f:
                try:
                    tdata = json.load(f)
                except Exception as e:
                    all_errors.append(f"[{sid}][{cid}] Lỗi cú pháp JSON file lý thuyết {theory_path}: {e}")
                    continue

            theory_lessons = tdata.get('lessons', [])
            total_lessons_subj += len(theory_lessons)

            # Khớp danh sách bài học giữa index và file lý thuyết
            idx_lesson_ids = [l['id'] for l in ch.get('lessons', [])]
            t_lesson_ids = [l['id'] for l in theory_lessons]

            if set(idx_lesson_ids) != set(t_lesson_ids):
                all_errors.append(f"[{sid}][{cid}] Không khớp bài học giữa index ({idx_lesson_ids}) và theory ({t_lesson_ids})")

            # Kiểm tra từng block trong từng lesson
            for l in theory_lessons:
                lid = l.get('id')
                ltitle = l.get('title')
                if not lid or not ltitle:
                    all_errors.append(f"[{sid}][{cid}] Bài học thiếu id hoặc title!")

                blocks = l.get('blocks', [])
                if not blocks:
                    all_warnings.append(f"[{sid}][{cid}][{lid}] Bài học không có block nội dung nào!")

                for bidx, b in enumerate(blocks):
                    btype = b.get('type')
                    if not btype:
                        all_errors.append(f"[{sid}][{cid}][{lid}] Block #{bidx} thiếu trường type!")
                    elif btype == 'formula':
                        if 'items' in b:
                            if not isinstance(b['items'], list):
                                all_errors.append(f"[{sid}][{cid}][{lid}] Formula block #{bidx} items không phải là list!")
                            else:
                                for item in b['items']:
                                    if not isinstance(item, dict) or 'math' not in item:
                                        all_errors.append(f"[{sid}][{cid}][{lid}] Formula item #{bidx} thiếu trường math: {item}")
                        elif 'content' not in b and 'math' not in b:
                            all_errors.append(f"[{sid}][{cid}][{lid}] Formula block #{bidx} không có items lẫn content!")
                    elif btype == 'list':
                        if not isinstance(b.get('items'), list):
                            all_errors.append(f"[{sid}][{cid}][{lid}] List block #{bidx} thiếu items mảng!")
                    elif btype == 'table':
                        if not isinstance(b.get('headers'), list) or not isinstance(b.get('rows'), list):
                            all_errors.append(f"[{sid}][{cid}][{lid}] Table block #{bidx} thiếu headers/rows mảng!")

        print(f"  + Tổng số bài lý thuyết: {total_lessons_subj} bài (tất cả file & block hợp lệ)")

        # 3. Kiểm tra các bộ đề trắc nghiệm và tự luận
        qsets = idx.get('questionSets', [])
        total_q_subj = 0
        seen_q_ids = set()

        for qs in qsets:
            qsid = qs['id']
            qtype = qs['type']
            qfile = qs['file']
            qpath = f"data/{spath}/{qfile}"

            if not os.path.exists(qpath):
                all_errors.append(f"[{sid}] Thiếu file bộ đề: {qpath}")
                continue

            with open(qpath, 'r', encoding='utf-8') as f:
                try:
                    qdata = json.load(f)
                except Exception as e:
                    all_errors.append(f"[{sid}] Lỗi cú pháp JSON {qpath}: {e}")
                    continue

            questions = qdata.get('questions', [])
            total_q_subj += len(questions)
            print(f"  + Bộ đề '{qs['title']}' ({qsid}): {len(questions)} câu")

            for i, q in enumerate(questions):
                qid = q.get('id')
                if not qid:
                    all_errors.append(f"[{sid}][{qsid}] Câu hỏi #{i} thiếu ID!")
                elif qid in seen_q_ids:
                    all_errors.append(f"[{sid}][{qsid}] Trùng ID câu hỏi: {qid}!")
                else:
                    seen_q_ids.add(qid)

                # Kiểm tra chapter
                qch = q.get('chapter')
                if qch not in ch_ids:
                    all_errors.append(f"[{sid}][{qsid}][{qid}] Thuộc chương '{qch}' không tồn tại trong index!")

                # Kiểm tra level
                qlv = q.get('level')
                if qlv not in ['nb', 'th', 'vd']:
                    all_errors.append(f"[{sid}][{qsid}][{qid}] Mức độ không hợp lệ: '{qlv}'!")

                # Kiểm tra text
                qtext = q.get('question')
                if not qtext or len(qtext.strip()) == 0:
                    all_errors.append(f"[{sid}][{qsid}][{qid}] Đề bài rỗng!")

                # Kiểm tra LaTeX delimiters
                # Đếm dấu $ lẻ nếu không có escape
                clean_qtext = (qtext or '').replace(r'\$', '')
                if clean_qtext.count('$') % 2 != 0:
                    all_errors.append(f"[{sid}][{qsid}][{qid}] Lệch dấu $ trong question: {qtext[:60]}...")

                # Kiểm tra đáp án
                if qtype == 'multiple-choice':
                    choices = q.get('choices')
                    ans = q.get('answer')
                    if not isinstance(choices, list) or len(choices) != 4:
                        all_errors.append(f"[{sid}][{qsid}][{qid}] Trắc nghiệm không đúng 4 phương án! (có {len(choices) if isinstance(choices, list) else 0})")
                    if not isinstance(ans, int) or ans < 0 or ans > 3:
                        all_errors.append(f"[{sid}][{qsid}][{qid}] Đáp án trắc nghiệm không nằm trong [0, 3]! (ans={ans})")
                elif qtype == 'short-answer':
                    ans = q.get('answer')
                    if ans is None or str(ans).strip() == '':
                        all_errors.append(f"[{sid}][{qsid}][{qid}] Trả lời ngắn thiếu đáp án!")

        stats[sid] = {
            'name': sname,
            'chapters': len(chapters),
            'lessons': total_lessons_subj,
            'questions': total_q_subj
        }

    print("\n======================================================================")
    print("   TỔNG KẾT THỐNG KÊ")
    print("======================================================================")
    grand_q = 0
    grand_l = 0
    for sid, s in stats.items():
        print(f"• {s['name']:<12}: {s['chapters']} chương | {s['lessons']:>2} bài lý thuyết | {s['questions']:>4} câu hỏi")
        grand_q += s['questions']
        grand_l += s['lessons']

    print(f"\n-> TỔNG TOÀN HỆ THỐNG: {len(active_subjects)} môn | {grand_l} bài lý thuyết | {grand_q} câu hỏi")

    print("\n======================================================================")
    print(f"KẾT QUẢ RÀ SOÁT: {len(all_errors)} LỖI, {len(all_warnings)} CẢNH BÁO")
    print("======================================================================")
    if all_errors:
        for err in all_errors[:20]:
            print(f"❌ {err}")
        if len(all_errors) > 20:
            print(f"... và {len(all_errors) - 20} lỗi khác.")
    else:
        print("✅ TOÀN BỘ DỮ LIỆU ĐẠT CHUẨN 100%! KHÔNG CÓ BẤT KỲ LỖI NÀO.")

    return len(all_errors) == 0

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    success = audit_deep()
    sys.exit(0 if success else 1)
