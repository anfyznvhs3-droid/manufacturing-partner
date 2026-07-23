#!/usr/bin/env python3
"""Validate training configuration traceability and return a DOC-READY gate."""

import argparse
import csv
import json
from pathlib import Path


REQUIRED_TESTS = {f"T{index:02d}" for index in range(1, 8)}
TRACE_FIELDS = ("system_id", "bom_revision", "firmware_id", "enclosure_id", "sensor_interface_id", "cable_set_id")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--configuration", required=True, type=Path)
    parser.add_argument("--firmware", required=True, type=Path)
    parser.add_argument("--tests", required=True, type=Path)
    parser.add_argument("--change-control", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    configuration = load_json(args.configuration)
    firmware = load_json(args.firmware)
    change_control = load_json(args.change_control)
    expected = {field: configuration[field] for field in TRACE_FIELDS}
    conflicts = []
    non_passing = []

    if firmware.get("firmware_id") != expected["firmware_id"]:
        conflicts.append({
            "source": "firmware-manifest",
            "field": "firmware_id",
            "expected": expected["firmware_id"],
            "observed": firmware.get("firmware_id"),
        })

    for field, expected_value in expected.items():
        if change_control.get("new_configuration", {}).get(field) != expected_value:
            conflicts.append({
                "source": "change-control",
                "field": field,
                "expected": expected_value,
                "observed": change_control.get("new_configuration", {}).get(field),
            })
    if change_control.get("status") != "approved-training":
        conflicts.append({
            "source": "change-control",
            "field": "status",
            "expected": "approved-training",
            "observed": change_control.get("status"),
        })

    with args.tests.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    test_ids = set()
    for row in rows:
        test_id = row["test_id"]
        test_ids.add(test_id)
        for field, expected_value in expected.items():
            if row.get(field) != expected_value:
                conflicts.append({
                    "source": test_id,
                    "field": field,
                    "expected": expected_value,
                    "observed": row.get(field),
                })
        if row.get("result") != "pass":
            non_passing.append({"test_id": test_id, "result": row.get("result"), "observation": row.get("observation")})

    missing_tests = sorted(REQUIRED_TESTS - test_ids)
    if conflicts:
        decision = "blocked-by-conflict"
    elif missing_tests or non_passing:
        decision = "needs-fact-confirmation"
    else:
        decision = "ready"

    report = {
        "training_evidence": True,
        "decision": decision,
        "conflicts": conflicts,
        "non_passing_tests": non_passing,
        "missing_tests": missing_tests,
        "note": "Synthetic training evidence only. A ready result validates traceability rules, not real product conformity.",
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
