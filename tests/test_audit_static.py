import unittest
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from audit_static_toan10 import validate_question, check_latex_syntax

class TestStaticAudit(unittest.TestCase):
    def test_valid_mc_question(self):
        valid_q = {
            "id": "mc-c1-001",
            "chapter": "c1",
            "lesson": "b1",
            "level": "nb",
            "dang": "Nhận biết",
            "question": "Trong các câu sau, câu nào là mệnh đề?",
            "choices": ["A", "B", "C", "D"],
            "answer": 1,
            "explanation": "Lời giải chi tiết."
        }
        issues = validate_question(valid_q, is_short=False)
        self.assertEqual(len(issues), 0)

    def test_missing_field_mc(self):
        invalid_q = {
            "id": "mc-c1-002",
            "question": "Câu hỏi thiếu trường",
            "choices": ["A", "B", "C", "D"],
            "answer": 0
        }
        issues = validate_question(invalid_q, is_short=False)
        missing_types = [issue['type'] for issue in issues]
        self.assertIn("missing_field", missing_types)

    def test_invalid_choices_count(self):
        invalid_q = {
            "id": "mc-c1-003",
            "chapter": "c1",
            "lesson": "b1",
            "level": "nb",
            "dang": "Nhận biết",
            "question": "Câu hỏi có 3 lựa chọn",
            "choices": ["A", "B", "C"],
            "answer": 0,
            "explanation": "Lời giải."
        }
        issues = validate_question(invalid_q, is_short=False)
        types = [i['type'] for i in issues]
        self.assertIn("invalid_choices_count", types)

    def test_invalid_answer_bound(self):
        invalid_q = {
            "id": "mc-c1-004",
            "chapter": "c1",
            "lesson": "b1",
            "level": "nb",
            "dang": "Nhận biết",
            "question": "Câu hỏi đáp án ngoài biên",
            "choices": ["A", "B", "C", "D"],
            "answer": 4,
            "explanation": "Lời giải."
        }
        issues = validate_question(invalid_q, is_short=False)
        types = [i['type'] for i in issues]
        self.assertIn("invalid_answer_bound", types)

    def test_unbalanced_latex_dollars(self):
        text = "Cho tam giác $ABC có góc $A = 60^\\circ$."
        has_error, msg = check_latex_syntax(text)
        self.assertTrue(has_error)
        self.assertIn("unbalanced", msg.lower())

if __name__ == '__main__':
    unittest.main()
