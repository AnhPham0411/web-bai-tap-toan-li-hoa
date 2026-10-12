import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/sample_audit_report.json', 'r', encoding='utf-8') as f:
    rep = json.load(f)

print("=======================================================================")
print("  TRÍCH XUẤT CÂU HỎI THẨM ĐỊNH TỪ GÓC NHÌN HỌC SINH (TOÁN 11 & 12)")
print("=======================================================================\n")

def show_samples(sample_list, qtype_label):
    count = 0
    for q in sample_list:
        if q['_subj'] in ['toan11', 'toan12']:
            count += 1
            subj_title = "TOÁN 11" if q['_subj'] == 'toan11' else "TOÁN 12"
            print(f"--- [Mẫu {count}: {subj_title} - {qtype_label} - ID: {q['id']}] ---")
            print("ĐỀ BÀI:")
            print(q['question'])
            print()
            if 'choices' in q:
                print("CÁC PHƯƠNG ÁN:")
                for i, c in enumerate(q['choices']):
                    mark = "(*) " if i == q['answer'] else "    "
                    print(f"  {mark}{chr(65+i)}. {c}")
                print()
            print(f"ĐÁP ÁN: {q['answer']}")
            print("LỜI GIẢI CHI TIẾT:")
            print(q.get('explanation', 'Không có'))
            print("-" * 65 + "\n")
            if count >= 3:
                break

print(">>> 1. PHẦN TRẮC NGHIỆM KHÁCH QUAN (4 PHƯƠNG ÁN):")
show_samples(rep['sample_mc_highlights'], "Trắc nghiệm")

print("\n>>> 2. PHẦN TRẢ LỜI NGẮN (ĐIỀN ĐÁP SỐ):")
show_samples(rep['sample_short_highlights'], "Trả lời ngắn")
