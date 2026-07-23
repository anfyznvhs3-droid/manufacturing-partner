import copy
import pathlib
import sys
import unittest

SCRIPT_DIR = pathlib.Path(__file__).resolve().parents[3] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_multisource_intake import validate_payload  # RED: module does not exist yet.


def source(index: int) -> dict:
    return {
        "source_id": f"SRC-{index:02d}",
        "source_owner_id": f"ENG-{index:02d}",
        "artifact_type": "test-record",
        "received_at": "2026-07-23T09:00:00+09:00",
        "authored_or_revision": "REV-A",
        "scope": "training-device/rev-b",
        "configuration_id": "CFG-REV-B",
        "evidence_level": "controlled-internal",
        "original_record_locator": f"intake://SRC-{index:02d}",
    }


VALID_BATCH = {
    "contract": "operator-intake/v1",
    "intake_batch_id": "INT-2026-001",
    "operator": {"operator_id": "OP-01"},
    "sources": [source(1), source(2)],
    "claims": [
        {
            "claim_id": "CLM-001",
            "statement": "Firmware revision is FW-0.8.1.",
            "source_ids": ["SRC-01"],
        }
    ],
    "confirmation_queue": [
        {
            "queue_id": "CQ-001",
            "source_id": "SRC-02",
            "request": "Confirm test configuration identifier.",
        }
    ],
}


class ValidateMultisourceIntakeTests(unittest.TestCase):
    def test_accepts_one_operator_with_traceable_sources(self):
        result = validate_payload(VALID_BATCH)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["source_count"], 2)

    def test_rejects_more_than_twenty_sources(self):
        payload = copy.deepcopy(VALID_BATCH)
        payload["sources"] = [source(index) for index in range(1, 22)]
        result = validate_payload(payload)
        self.assertFalse(result["valid"])
        self.assertIn("source-count-out-of-range", result["errors"])

    def test_rejects_untraceable_claim_and_confirmation(self):
        payload = copy.deepcopy(VALID_BATCH)
        payload["claims"][0]["source_ids"] = ["SRC-99"]
        payload["confirmation_queue"][0]["source_id"] = "SRC-98"
        result = validate_payload(payload)
        self.assertFalse(result["valid"])
        self.assertIn("claim-references-unknown-source:CLM-001:SRC-99", result["errors"])
        self.assertIn("confirmation-references-unknown-source:CQ-001:SRC-98", result["errors"])


if __name__ == "__main__":
    unittest.main()
