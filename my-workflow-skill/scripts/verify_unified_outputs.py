#!/usr/bin/env python3
"""Verify contract shape and expected verdicts for a set of generated outputs."""

import argparse
import json
from pathlib import Path


REQUIRED_KEYS = {
    "contract", "scope", "review_decision", "operational_authorization", "evidence_summary",
    "claims", "conflicts", "confirmation_queue", "rules_applied", "authorization_reasons", "next_goal",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", required=True, type=Path)
    parser.add_argument("--expectations", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    cases = json.loads(args.expectations.read_text(encoding="utf-8"))
    results = []

    for case in cases:
        output = json.loads((args.directory / case["output"]).read_text(encoding="utf-8"))
        keys_ok = set(output) == REQUIRED_KEYS
        review_ok = output.get("review_decision") == case["review_decision"]
        authorization_ok = output.get("operational_authorization") == case["operational_authorization"]
        results.append({
            "input": case["input"],
            "keys_ok": keys_ok,
            "review_ok": review_ok,
            "authorization_ok": authorization_ok,
        })

    total = len(results)
    report = {
        "cases": results,
        "case_count": total,
        "schema_conformance_percent": round(100 * sum(row["keys_ok"] for row in results) / total, 1),
        "constructed_review_verdict_match_percent": round(100 * sum(row["review_ok"] for row in results) / total, 1),
        "constructed_authorization_verdict_match_percent": round(100 * sum(row["authorization_ok"] for row in results) / total, 1),
        "note": "These are constructed-case guardrail metrics, not factual accuracy on a real labeled manufacturing corpus."
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
