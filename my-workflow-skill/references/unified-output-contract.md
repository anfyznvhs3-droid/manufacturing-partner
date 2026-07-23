# Manufacturing Gate Output Contract v1

## Non-negotiable rule

Normalize every input type - vendor PDF, operator handover, test result, agent draft, email, or external web source - into this contract before returning a conclusion. Do not allow a source's tone, authority, length, or optimistic wording to change the output shape or bypass a gate.

When a single operator receives material from multiple engineers, register the input first as `operator-intake/v1` using [single-operator-multisource-intake.md](single-operator-multisource-intake.md). Preserve the source IDs in each claim and confirmation item before emitting this final contract.

## Required output fields

```json
{
  "contract": "manufacturing-gate/v1",
  "scope": {"system_id": "", "configuration_id": "", "intended_use": ""},
  "review_decision": "ready | needs-fact-confirmation | blocked-by-conflict | insufficient-source",
  "operational_authorization": "authorized | pending-authority | denied",
  "evidence_summary": {"critical_total": 0, "by_provenance": {}},
  "claims": [{"id": "", "status": "stated | inferred | missing | conflicting | site-term-unknown", "evidence_ids": []}],
  "conflicts": [],
  "confirmation_queue": [],
  "rules_applied": [],
  "next_goal": ""
}
```

`review_decision` evaluates document completeness and consistency. `operational_authorization` is a separate and stricter gate. Never imply authorization from `ready` alone.

## Evidence provenance

Classify every critical evidence item as exactly one of: `synthetic-training`, `public-vendor`, `controlled-internal`, `qualified-laboratory`, `independent-security-assessment`, `regulatory-authority`, or `approved-authority`.

Synthetic training evidence may test the workflow but always denies operational authorization. A vendor source may support component facts but cannot alone prove the final configured product. The input must declare the provenance types required for the stated scope.

## Authorization decision

- Return `denied` when a critical conflict exists, review is `blocked-by-conflict` or `insufficient-source`, or any critical evidence is synthetic training evidence.
- Return `pending-authority` when review is not `ready`, confirmation items remain, required evidence provenance is missing, or an approved authority record is absent.
- Return `authorized` only when review is `ready`, all required provenance is present, no conflict or confirmation item remains, no critical evidence is synthetic, and approved-authority evidence is present.

The contract controls the format, not engineering responsibility. `authorized` is possible only for a properly scoped real evidence register and does not replace law, certification, or qualified engineering review.
