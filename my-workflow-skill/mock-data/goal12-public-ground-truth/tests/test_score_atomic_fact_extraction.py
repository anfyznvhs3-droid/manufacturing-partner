import pathlib
import sys
import unittest

SCRIPT_DIR = pathlib.Path(__file__).resolve().parents[3] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from score_atomic_fact_extraction import prepare_labels, score_judgments


class ScoreAtomicFactExtractionTests(unittest.TestCase):
    def test_scores_value_and_page_match_separately(self):
        labels = [
            {"label_id": "L-01", "label_status": "human-ratified"},
            {"label_id": "L-02", "label_status": "human-ratified"},
            {"label_id": "L-03", "label_status": "human-ratified"},
        ]
        judgments = [
            {"label_id": "L-01", "reported": True, "value_match": True, "evidence_page_match": True, "unknown_reported": False},
            {"label_id": "L-02", "reported": True, "value_match": True, "evidence_page_match": False, "unknown_reported": False},
            {"label_id": "L-03", "reported": False, "value_match": False, "evidence_page_match": False, "unknown_reported": True},
        ]
        result = score_judgments(labels, judgments)
        self.assertEqual(result["eligible_label_count"], 3)
        self.assertEqual(result["reported_count"], 2)
        self.assertEqual(result["fully_correct_count"], 1)
        self.assertEqual(result["fact_precision_percent"], 50.0)
        self.assertEqual(result["fact_recall_percent"], 33.3)
        self.assertEqual(result["unknown_preservation_percent"], 66.7)

    def test_refuses_candidate_labels_without_explicit_training_mode(self):
        labels = [{"label_id": "L-01", "label_status": "pending-human-ratification"}]
        judgments = [{"label_id": "L-01", "reported": True, "value_match": True, "evidence_page_match": True, "unknown_reported": False}]
        with self.assertRaises(ValueError):
            score_judgments(labels, judgments)

    def test_inherits_dataset_candidate_status_only_for_training_mode(self):
        label_payload = {
            "label_status": "pending-human-ratification",
            "labels": [{"label_id": "L-01"}],
        }
        labels = prepare_labels(label_payload)
        result = score_judgments(
            labels,
            [{"label_id": "L-01", "reported": True, "value_match": True, "evidence_page_match": True, "unknown_reported": False}],
            allow_source_anchored=True,
        )
        self.assertEqual(result["result_scope"], "training-source-anchored-not-human-factual-accuracy")


if __name__ == "__main__":
    unittest.main()
