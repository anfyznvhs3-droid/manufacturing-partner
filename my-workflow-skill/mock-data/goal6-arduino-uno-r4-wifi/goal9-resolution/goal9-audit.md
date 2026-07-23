# GOAL 9: synthetic change-control audit

## Resolution record

`CC-002` changes the authoritative training configuration from BOM revision A / `FW-GW-0.8.0` to BOM revision B / `FW-GW-0.8.1`. It identifies the earlier T02/T03 evidence as invalidated rather than deleting or overwriting it.

## Fact audit

| Check | Evidence | Result |
| --- | --- | --- |
| Change-control identity | `change-control-cc-002.json` | stated; prior and new configurations are explicit. |
| New configuration matches firmware manifest | `configuration-rev-b.json`, firmware manifest | stated; both identify `FW-GW-0.8.1`. |
| T01-T07 configuration traceability | `test-results-rev-b.csv` | stated; all seven rows match the new configuration. |
| Prior mismatch preservation | `invalidated_evidence` in CC-002 | stated; previous T02/T03 remain auditable and unusable. |
| T05/T07 remediation | firmware manifest and revised training rows | stated for the training scenario only; no external security, legal, or laboratory evidence exists. |

## Metrics and decision

- Required T01-T07 rows: 7 of 7 present.
- Configuration conflicts: 0.
- Non-passing rows: 0.
- Gate decision: `ready` for the synthetic evidence bundle.

`ready` means the declared training configuration, change record, manifest, and seven synthetic result rows are internally traceable. It does not mean that the Arduino-based gateway is safe, certified, market-authorized, EMC-tested, secure, or ready to ship.

## Real-product confirmation queue

1. Replace each synthetic row with configuration-linked laboratory, security-assessment, functional-test, and regulatory evidence.
2. Obtain an approved product BOM, enclosure/cable/sensor/firmware identifiers, and market-entry review.
3. Use licensed standard texts and qualified review/testing appropriate to the final market and product.

## Learning update

Preserve invalid evidence and link it to a controlled change record. Do not overwrite a failed or mismatched result merely because a later configuration passes a new test.
