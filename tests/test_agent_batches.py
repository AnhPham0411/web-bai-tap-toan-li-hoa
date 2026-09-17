import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from prepare_agent_batches import create_agent_batches

class TestAgentBatches(unittest.TestCase):
    def test_batches_structure(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        batches = create_agent_batches(base_dir)

        # Must have exactly 10 batches
        self.assertEqual(len(batches), 10)

        total_questions = 0
        all_ids = []
        for agent_idx in range(1, 11):
            agent_key = f"agent_{agent_idx}"
            self.assertIn(agent_key, batches)
            batch = batches[agent_key]
            self.assertEqual(batch['agent_id'], agent_idx)
            self.assertEqual(len(batch['questions']), 75)
            total_questions += len(batch['questions'])
            for q in batch['questions']:
                all_ids.append(q['id'])

        # Total questions must be 750
        self.assertEqual(total_questions, 750)
        # All IDs must be unique
        self.assertEqual(len(all_ids), len(set(all_ids)))

if __name__ == '__main__':
    unittest.main()
