# Hệ thống Thẩm định 10 Agent cho Ngân hàng Câu hỏi Toán 10 Implementation Plan

> **For Antigravity:** REQUIRED SUB-SKILL: Load executing-plans to implement this plan task-by-task.

**Goal:** Xây dựng hệ thống thẩm định toàn diện và thực hiện rà soát 100% (750 câu hỏi) môn Toán 10 bằng 10 Agent phân vùng độc lập kết hợp bộ kiểm tra tĩnh, xuất báo cáo kiểm định phân loại lỗi chi tiết (Critical/Warning/Minor).

**Architecture:** Hệ thống áp dụng mô hình 2 tầng (Hybrid 2-Tier): Tầng 1 là Static Validation Engine tự động quét Schema và cú pháp LaTeX; Tầng 2 là 10 Math Auditor Agents xử lý song song 10 phân vùng dữ liệu (mỗi Agent phụ trách chính xác 75 câu của từng chương) để giải toán độc lập, đối chiếu đáp án và thẩm định lời giải; Tầng 3 là Report Aggregator tổng hợp thành Báo cáo Markdown và JSON cấu trúc.

**Tech Stack:** Python 3, JSON, Regex, Git, Markdown.

---

### Task 1: Static Validation Engine (`scripts/audit_static_toan10.py`)

**Files:**
- Create: `scripts/audit_static_toan10.py`
- Test: `tests/test_audit_static.py`

**Step 1: Viết test cho Static Validation Engine**
Kiểm tra phát hiện: thiếu trường schema, `answer` out of bounds (ví dụ âm hoặc > 3), `choices` không đủ 4 phần tử trong trắc nghiệm, lỗi cặp dấu `$`.

**Step 2: Chạy test để xác nhận FAIL**
Run: `python -m unittest tests/test_audit_static.py`
Expected: FAIL (module chưa tồn tại).

**Step 3: Cài đặt `scripts/audit_static_toan10.py`**
Đọc `data/toan10/questions/mc.json` và `short.json`, rà soát các lỗi cú pháp, xuất kết quả sơ bộ dạng JSON log.

**Step 4: Chạy test để xác nhận PASS**
Run: `python -m unittest tests/test_audit_static.py`
Expected: PASS.

**Step 5: Commit**
```bash
git add scripts/audit_static_toan10.py tests/test_audit_static.py
git commit -m "feat(audit): add static validation engine for toan10"
```

---

### Task 2: Data Partitioning & Batch Preparer (`scripts/prepare_agent_batches.py`)

**Files:**
- Create: `scripts/prepare_agent_batches.py`
- Test: `tests/test_agent_batches.py`

**Step 1: Viết test cho module chia dữ liệu 10 Agent**
Kiểm tra dữ liệu đầu vào 750 câu được chia đúng 10 batch, mỗi batch 75 câu, không trùng lặp và tổng số ID gom lại bằng chính xác 750 ID.

**Step 2: Chạy test để xác nhận FAIL**
Run: `python -m unittest tests/test_agent_batches.py`
Expected: FAIL.

**Step 3: Cài đặt `scripts/prepare_agent_batches.py`**
Tự động trích xuất 10 batch dữ liệu theo đúng phân vùng đã chốt ở thiết kế:
- Agent 1: C1 MC 001-075 (75 câu)
- Agent 2: C1 MC 076-120 (45 câu) + C1 Short 001-030 (30 câu)
- Agent 3: C2 MC 001-075 (75 câu)
- Agent 4: C2 MC 076-120 (45 câu) + C2 Short 001-030 (30 câu)
- Agent 5: C3 MC 001-075 (75 câu)
- Agent 6: C3 MC 076-120 (45 câu) + C3 Short 001-030 (30 câu)
- Agent 7: C4 MC 001-075 (75 câu)
- Agent 8: C4 MC 076-120 (45 câu) + C4 Short 001-030 (30 câu)
- Agent 9: C5 MC 001-075 (75 câu)
- Agent 10: C5 MC 076-120 (45 câu) + C5 Short 001-030 (30 câu)

**Step 4: Chạy test để xác nhận PASS**
Run: `python -m unittest tests/test_agent_batches.py`
Expected: PASS.

**Step 5: Commit**
```bash
git add scripts/prepare_agent_batches.py tests/test_agent_batches.py
git commit -m "feat(audit): add 10-agent batch partition preparer"
```

---

### Task 3: Report Aggregator (`scripts/aggregate_audit_reports.py`)

**Files:**
- Create: `scripts/aggregate_audit_reports.py`
- Test: `tests/test_aggregate_reports.py`

**Step 1: Viết test cho Aggregator**
Kiểm tra tổng hợp: đọc các file kết quả audit của Tầng 1 và 10 Agent, kết xuất Markdown và JSON đầy đủ thống kê, cảnh báo nếu thiếu câu hỏi.

**Step 2: Chạy test để xác nhận FAIL**
Run: `python -m unittest tests/test_aggregate_reports.py`
Expected: FAIL.

**Step 3: Cài đặt `scripts/aggregate_audit_reports.py`**
Tạo module kết xuất báo cáo chuẩn hóa `docs/reports/toan10_audit_report.md` và `docs/reports/toan10_audit_report.json`.

**Step 4: Chạy test để xác nhận PASS**
Run: `python -m unittest tests/test_aggregate_reports.py`
Expected: PASS.

**Step 5: Commit**
```bash
git add scripts/aggregate_audit_reports.py tests/test_aggregate_reports.py
git commit -m "feat(audit): add report aggregator module"
```

---

### Task 4: Chạy Static Validation trên 750 câu Toán 10

**Files:**
- Output: `artifacts/audit/static_audit_results.json`

**Step 1: Chạy script Static Validation**
Run: `python scripts/audit_static_toan10.py`
Expected: Quét xong 750 câu, phát hiện danh sách các lỗi cú pháp/LaTeX ban đầu.

---

### Task 5: Thực thi 10 Math Auditor Agents Thẩm định Chi tiết 750 Câu

**Phạm vi thực hiện:**
- Agent 1: Chương 1 MC p1 (75 câu)
- Agent 2: Chương 1 MC p2 + Short (75 câu)
- Agent 3: Chương 2 MC p1 (75 câu)
- Agent 4: Chương 2 MC p2 + Short (75 câu)
- Agent 5: Chương 3 MC p1 (75 câu)
- Agent 6: Chương 3 MC p2 + Short (75 câu)
- Agent 7: Chương 4 MC p1 (75 câu)
- Agent 8: Chương 4 MC p2 + Short (75 câu)
- Agent 9: Chương 5 MC p1 (75 câu)
- Agent 10: Chương 5 MC p2 + Short (75 câu)

Mỗi Agent thực hiện giải toán độc lập, kiểm tra từng câu hỏi, ghi nhận lỗi phân loại theo `CRITICAL`, `WARNING`, `MINOR` kèm đề xuất sửa đổi.

---

### Task 6: Kết xuất Báo cáo Kiểm định Hoàn chỉnh

**Files:**
- Create: `docs/reports/toan10_audit_report.md`
- Create: `docs/reports/toan10_audit_report.json`

**Step 1: Chạy Aggregator để tạo báo cáo tổng hợp**
Run: `python scripts/aggregate_audit_reports.py`
Expected: Sinh file `docs/reports/toan10_audit_report.md` và `docs/reports/toan10_audit_report.json`.

**Step 2: Commit**
```bash
git add docs/reports/toan10_audit_report.md docs/reports/toan10_audit_report.json
git commit -m "docs(audit): generate complete toan10 audit report"
```

---

### Task 7: Kiểm định Chất lượng & Bàn giao (Verification)

**Step 1: Kiểm tra độ phủ (Coverage Check)**
Xác minh 100% 750/750 câu hỏi đã được đọc và thẩm định, không có ID nào bị trùng lặp hoặc bỏ sót.

**Step 2: Báo cáo kết quả và trình bày các lỗi Critical cần người dùng lưu ý.**
