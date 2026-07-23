#!/usr/bin/env python3
"""Calculate raw agreement, Cohen's kappa, and disagreements for two reviewers."""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    needed = {"id", "reviewer_a", "reviewer_b"}
    if not rows or not needed.issubset(rows[0]):
        print("CSV must contain id, reviewer_a, reviewer_b columns.", file=sys.stderr)
        return 2

    pairs = []
    incomplete = []
    for row in rows:
        a = row["reviewer_a"].strip()
        b = row["reviewer_b"].strip()
        if not a or not b:
            incomplete.append(row["id"])
        else:
            pairs.append((row["id"], a, b))

    if not pairs:
        print("No completed reviewer pairs.", file=sys.stderr)
        return 2

    labels_a = Counter(a for _, a, _ in pairs)
    labels_b = Counter(b for _, _, b in pairs)
    total = len(pairs)
    observed = sum(a == b for _, a, b in pairs) / total
    labels = set(labels_a) | set(labels_b)
    expected = sum((labels_a[label] / total) * (labels_b[label] / total) for label in labels)
    kappa = 1.0 if expected == 1.0 and observed == 1.0 else (observed - expected) / (1 - expected)
    disagreements = [(item_id, a, b) for item_id, a, b in pairs if a != b]

    print(f"Completed pairs: {total}")
    print(f"Raw agreement: {observed:.1%}")
    print(f"Cohen's kappa: {kappa:.3f}")
    print("Kappa gate (>= 0.800): " + ("PASS" if kappa >= 0.8 else "FAIL"))
    print("Incomplete IDs: " + (", ".join(incomplete) if incomplete else "none"))
    print("Disagreements:")
    if disagreements:
        for item_id, a, b in disagreements:
            print(f"- {item_id}: reviewer_a={a}; reviewer_b={b}")
    else:
        print("- none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
