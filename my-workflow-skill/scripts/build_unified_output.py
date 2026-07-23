#!/usr/bin/env python3
"""Build one guardrailed manufacturing-gate output from an evidence register."""

import argparse
import json
from collections import Counter
from pathlib import Path


DECISIONS = {"ready", "needs-fact-confirmation", "blocked-by-conflict", "insufficient-source"}
PROVENANCE = {
    "synthetic-training", "public-vendor", "controlled-internal", "qualified-laboratory",
    "independent-security-assessment", "regulatory-authority", "approved-authority",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    register = json.loads(args.input.read_text(encoding="utf-8"))

    required = {"scope", "review_decision", "critical_evidence", "required_critical_provenance", "conflicts", "confirmation_queue"}
    missing = sorted(required - set(register))
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    if register["review_decision"] not in DECISIONS:
        raise ValueError("Invalid review_decision")

    evidence = register["critical_evidence"]
    provenance = [item.get("provenance") for item in evidence]
    invalid = sorted(set(provenance) - PROVENANCE)
    if invalid:
        raise ValueError(f"Invalid provenance: {', '.join(invalid)}")
    required_provenance = set(register["required_critical_provenance"])
    if not required_provenance.issubset(PROVENANCE):
        raise ValueError("Invalid required_critical_provenance")

    actual = set(provenance)
    missing_provenance = sorted(required_provenance - actual)
    reasons = []
    if register["review_decision"] in {"blocked-by-conflict", "insufficient-source"} or register["conflicts"]:
        authorization = "denied"
        reasons.append("review conflict or insufficient source")
    elif "synthetic-training" in actual:
        authorization = "denied"
        reasons.append("critical synthetic training evidence is present")
    elif register["review_decision"] != "ready" or register["confirmation_queue"] or missing_provenance or "approved-authority" not in actual:
        authorization = "pending-authority"
        if register["review_decision"] != "ready":
            reasons.append("review decision is not ready")
        if register["confirmation_queue"]:
            reasons.append("fact confirmations remain")
        if missing_provenance:
            reasons.append("required evidence provenance is missing")
        if "approved-authority" not in actual:
            reasons.append("approved authority evidence is missing")
    else:
        authorization = "authorized"
        reasons.append("all declared gates passed")

    output = {
        "contract": "manufacturing-gate/v1",
        "scope": register["scope"],
        "review_decision": register["review_decision"],
        "operational_authorization": authorization,
        "evidence_summary": {
            "critical_total": len(evidence),
            "by_provenance": dict(sorted(Counter(provenance).items())),
            "missing_required_provenance": missing_provenance,
        },
        "claims": register.get("claims", []),
        "conflicts": register["conflicts"],
        "confirmation_queue": register["confirmation_queue"],
        "metrics": register.get("metrics", {}),
        "learning_update": register.get("learning_update", []),
        "recursive_status": register.get("recursive_status", "continue"),
        "owner_notification": register.get("owner_notification", {
            "required": False,
            "message": "정확도 임계값 미도달 또는 사람 확인이 남아 있습니다.",
            "channel": "manufacturing-gate/v1",
        }),
        "rules_applied": ["DOC-READY v1", "Manufacturing Gate Output Contract v1"],
        "authorization_reasons": reasons,
        "next_goal": register.get("next_goal", "Provide the highest-risk missing evidence."),
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
