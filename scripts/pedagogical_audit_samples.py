import json
import random
import glob
import re

def sample_and_audit():
    random.seed(42)  # Đảm bảo tính tái lập

    mc_questions = []
    short_questions = []

    # Thu thập tất cả câu hỏi từ 6 môn
    for p in glob.glob('data/*/questions/mc.json'):
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
            subj = p.split('\\')[1] if '\\' in p else p.split('/')[1]
            for q in data['questions']:
                q['_subj'] = subj
                mc_questions.append(q)

    for p in glob.glob('data/*/questions/short.json'):
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
            subj = p.split('\\')[1] if '\\' in p else p.split('/')[1]
            for q in data['questions']:
                q['_subj'] = subj
                short_questions.append(q)

    # Bốc ngẫu nhiên 100 câu Trắc nghiệm và 100 câu Trả lời ngắn
    sample_mc = random.sample(mc_questions, min(100, len(mc_questions)))
    sample_short = random.sample(short_questions, min(100, len(short_questions)))

    print(f"=== ĐÃ BỐC {len(sample_mc)} CÂU TRẮC NGHIỆM VÀ {len(sample_short)} CÂU TRẢ LỜI NGẮN ===")

    # Phân tích 100 câu trắc nghiệm
    mc_issues = []
    mc_by_subj = {}
    for q in sample_mc:
        s = q['_subj']
        mc_by_subj[s] = mc_by_subj.get(s, 0) + 1
        # 1. Kiểm tra độ dài đề bài
        if len(q['question'].strip()) < 10:
            mc_issues.append((q['id'], 'Đề bài quá ngắn hoặc thiếu thông tin'))
        # 2. Kiểm tra các phương án có bị trùng lặp không
        choices = [c.strip() for c in q['choices']]
        if len(set(choices)) < 4:
            mc_issues.append((q['id'], f'Có phương án trùng lặp: {choices}'))
        # 3. Kiểm tra đáp án đúng có rỗng không
        if not choices[q['answer']]:
            mc_issues.append((q['id'], 'Phương án đúng bị rỗng'))
        # 4. Kiểm tra lời giải
        if not q.get('explanation'):
            mc_issues.append((q['id'], 'Thiếu lời giải chi tiết'))

    # Phân tích 100 câu trả lời ngắn
    short_issues = []
    short_by_subj = {}
    for q in sample_short:
        s = q['_subj']
        short_by_subj[s] = short_by_subj.get(s, 0) + 1
        if len(q['question'].strip()) < 10:
            short_issues.append((q['id'], 'Đề bài quá ngắn'))
        ans = str(q.get('answer', '')).strip()
        if not ans:
            short_issues.append((q['id'], 'Đáp án rỗng'))
        # Thử parse đáp số thành float hoặc fraction
        try:
            if '/' in ans:
                num, den = ans.split('/')
                val = float(num) / float(den)
            else:
                val = float(ans.replace(',', '.'))
        except Exception:
            short_issues.append((q['id'], f'Đáp số không phải số hợp lệ: {ans}'))

    report = {
        'mc_count': len(sample_mc),
        'short_count': len(sample_short),
        'mc_by_subj': mc_by_subj,
        'short_by_subj': short_by_subj,
        'mc_issues': mc_issues,
        'short_issues': short_issues,
        'sample_mc_highlights': sample_mc[:10],
        'sample_short_highlights': sample_short[:10]
    }

    with open('scripts/sample_audit_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("\nPhân bố 100 câu Trắc nghiệm theo môn:", mc_by_subj)
    print("Vấn đề phát hiện ở 100 câu Trắc nghiệm:", len(mc_issues))
    print("\nPhân bố 100 câu Trả lời ngắn theo môn:", short_by_subj)
    print("Vấn đề phát hiện ở 100 câu Trả lời ngắn:", len(short_issues))

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    sample_and_audit()
