import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from aggregate_audit_reports import compile_audit_report, generate_markdown_report

class TestAggregateReports(unittest.TestCase):
    def test_compile_report_metrics(self):
        sample_static = {
            "total_scanned": 750,
            "mc_count": 600,
            "short_count": 150,
            "defects": []
        }
        # 10 agents with sample outputs
        sample_agent_reports = {}
        for i in range(1, 11):
            sample_agent_reports[f"agent_{i}"] = {
                "agent_id": i,
                "scanned_count": 75,
                "defects": [
                    {
                        "id": f"test-q-{i}",
                        "chapter": f"c{(i+1)//2}",
                        "severity": "CRITICAL" if i == 1 else "WARNING",
                        "type": "wrong_answer" if i == 1 else "latex_warning",
                        "description": f"Error found by agent {i}",
                        "fix_proposal": "Fix details"
                    }
                ] if i <= 2 else []
            }

        compiled = compile_audit_report(sample_static, sample_agent_reports)
        self.assertEqual(compiled['total_scanned'], 750)
        self.assertEqual(compiled['critical_count'], 1)
        self.assertEqual(compiled['warning_count'], 1)
        self.assertEqual(compiled['total_defects'], 2)

        md = generate_markdown_report(compiled)
        self.assertIn("Executive Summary", md)
        self.assertIn("CRITICAL", md)
        self.assertIn("test-q-1", md)

if __name__ == '__main__':
    unittest.main()
