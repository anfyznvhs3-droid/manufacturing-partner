#!/usr/bin/env python3
"""Validate one operator's traceable intake batch of up to 20 sources."""

import argparse
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "contract",
    "intake_batch_id",
    "operator",
    "sources",
    "claims",
    "confirmation_queue",
}
REQUIRED_SOURCE_FIELDS = {
    "source_id",
    "source_owner_id",
    "artifact_type",
    "received_at",
    "authored_or_revision",
    "scope",
    "configuration_id",
    "evidence_level",
    "original_record_locator",
}
ALLOWED_ARTIFACT_TYPES = {
    "document",
    "verbal-handover",
    "test-record",
    "vendor-declaration",
    "email",
    "external-web-source",
}
ALLOWED_EVIDENCE_LEVELS = {
    "synthetic-training",
    "public-vendor",
    "controlled-internal",
    "qualified-laboratory",
    "independent-security-assessment",
    "regulatory-authority",
    "approved-authority",
}


def validate_payload(payload: dict) -> dict:
    """Return deterministic intake-contract errors without changing the input."""
    errors = []
    missing_top_level = REQUIRED_TOP_LEVEL - set(payload)
    errors.extend(f"missing-top-level:{key}" for key in sorted(missing_top_level))

    if payload.get("contract") != "operator-intake/v1":
        errors.append("invalid-contract")
    if not isinstance(payload.get("intake_batch_id"), str) or not payload.get("intake_batch_id").strip():
        errors.append("invalid-intake-batch-id")

    operator = payload.get("operator")
    if not isinstance(operator, dict) or not isinstance(operator.get("operator_id"), str) or not operator["operator_id"].strip():
        errors.append("invalid-single-operator")

    sources = payload.get("sources")
    if not isinstance(sources, list):
        errors.append("sources-not-a-list")
        sources = []
    if not 1 <= len(sources) <= 20:
        errors.append("source-count-out-of-range")

    source_ids = set()
    for source in sources:
        if not isinstance(source, dict):
            errors.append("invalid-source-record")
            continue
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or not source_id.strip():
            errors.append("invalid-source-id")
            continue
        if source_id in source_ids:
            errors.append(f"duplicate-source-id:{source_id}")
        source_ids.add(source_id)
        for field in sorted(REQUIRED_SOURCE_FIELDS - set(source)):
            errors.append(f"source-missing-field:{source_id}:{field}")
        for field in REQUIRED_SOURCE_FIELDS & set(source):
            if not isinstance(source[field], str) or not source[field].strip():
                errors.append(f"source-invalid-field:{source_id}:{field}")
        if source.get("artifact_type") not in ALLOWED_ARTIFACT_TYPES:
            errors.append(f"source-invalid-artifact-type:{source_id}")
        if source.get("evidence_level") not in ALLOWED_EVIDENCE_LEVELS:
            errors.append(f"source-invalid-evidence-level:{source_id}")

    claims = payload.get("claims")
    if not isinstance(claims, list):
        errors.append("claims-not-a-list")
        claims = []
    for claim in claims:
        if not isinstance(claim, dict) or not isinstance(claim.get("claim_id"), str):
            errors.append("invalid-claim")
            continue
        claim_id = claim["claim_id"]
        claim_sources = claim.get("source_ids")
        if not isinstance(claim_sources, list) or not claim_sources:
            errors.append(f"claim-missing-source-reference:{claim_id}")
            continue
        for source_id in claim_sources:
            if source_id not in source_ids:
                errors.append(f"claim-references-unknown-source:{claim_id}:{source_id}")

    queue = payload.get("confirmation_queue")
    if not isinstance(queue, list):
        errors.append("confirmation-queue-not-a-list")
        queue = []
    for item in queue:
        if not isinstance(item, dict) or not isinstance(item.get("queue_id"), str):
            errors.append("invalid-confirmation-item")
            continue
        queue_id = item["queue_id"]
        source_id = item.get("source_id")
        if source_id not in source_ids:
            errors.append(f"confirmation-references-unknown-source:{queue_id}:{source_id}")

    return {
        "valid": not errors,
        "source_count": len(sources),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    result = validate_payload(json.loads(args.input.read_text(encoding="utf-8")))
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
