#!/usr/bin/env python3
"""Score human-reviewed atomic-fact extraction judgments."""

import argparse
import json
from pathlib import Path


def prepare_labels(label_payload: dict | list[dict]) -> list[dict]:
    """Inherit a dataset-level label status without overwriting row-level decisions."""
    if isinstance(label_payload, list):
        return label_payload
    default_status = label_payload.get("label_status")
    return [
        {"label_status": default_status, **label}
        for label in label_payload.get("labels", [])
    ]


def score_judgments(labels: list[dict], judgments: list[dict], allow_source_anchored: bool = False) -> dict:
    """Score only human-ratified labels unless explicit training mode is enabled."""
    eligible_statuses = {"human-ratified"}
    if allow_source_anchored:
        eligible_statuses.add("pending-human-ratification")
    eligible = [label for label in labels if label.get("label_status") in eligible_statuses]
    if not eligible:
        raise ValueError("No eligible human-ratified labels. Do not report factual accuracy from candidate labels.")

    labels_by_id = {label["label_id"]: label for label in eligible}
    judgments_by_id = {judgment.get("label_id"): judgment for judgment in judgments}
    missing_judgments = sorted(set(labels_by_id) - set(judgments_by_id))
    if missing_judgments:
        raise ValueError(f"Missing judgments for eligible labels: {', '.join(missing_judgments)}")

    relevant = [judgments_by_id[label_id] for label_id in labels_by_id]
    reported = [row for row in relevant if row.get("reported") is True]
    fully_correct = [
        row for row in reported
        if row.get("value_match") is True and row.get("evidence_page_match") is True
    ]
    unknown_preserved = [row for row in relevant if row.get("unknown_reported") is not True]
    eligible_count = len(eligible)
    reported_count = len(reported)

    return {
        "result_scope": (
            "training-source-anchored-not-human-factual-accuracy"
            if allow_source_anchored else "human-ratified-factual-accuracy"
        ),
        "eligible_label_count": eligible_count,
        "reported_count": reported_count,
        "fully_correct_count": len(fully_correct),
        "fact_precision_percent": round(100 * len(fully_correct) / reported_count, 1) if reported_count else 0.0,
        "fact_recall_percent": round(100 * len(fully_correct) / eligible_count, 1),
        "unknown_preservation_percent": round(100 * len(unknown_preserved) / eligible_count, 1),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", required=True, type=Path)
    parser.add_argument("--judgments", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--allow-source-anchored-training", action="store_true")
    args = parser.parse_args()
    label_payload = json.loads(args.labels.read_text(encoding="utf-8"))
    judgment_payload = json.loads(args.judgments.read_text(encoding="utf-8"))
    labels = prepare_labels(label_payload)
    judgments = judgment_payload.get("judgments", judgment_payload)
    report = score_judgments(labels, judgments, args.allow_source_anchored_training)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
