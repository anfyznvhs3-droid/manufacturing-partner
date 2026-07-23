# GOAL 8: synthetic evidence audit

## Evidence boundary

All inputs in this bundle are deliberately synthetic training evidence. They verify the review workflow only; they are not a product test, certificate, supplier record, or authorization to operate or ship equipment.

## Normalized configuration

The authoritative training configuration is `TRAIN-GW-01`, BOM revision `A`, firmware `FW-GW-0.8.0`, enclosure `ENC-TRAIN-01`, sensor interface `SENS-IF-TRAIN-A`, and cable set `CBL-TRAIN-01`.

## Fact audit

| Evidence | Status | Finding |
| --- | --- | --- |
| Configuration and firmware manifest | stated | Both declare `FW-GW-0.8.0`. |
| T01 | stated/pass | Configuration-control training record matches the authoritative configuration. |
| T02 and T03 | conflicting | Both claim `FW-GW-0.8.1`, which differs from the authoritative and manifest firmware ID. Their pass result cannot be reused. |
| T04 and T06 | stated/pass | Identifiers match, but results remain synthetic only. |
| T05 | stated/fail | Default credential is unapproved. |
| T07 | stated/fail | Market-entry route is incomplete. |

## Metrics and decision

- Required T01-T07 evidence rows: 7 of 7 present.
- Configuration conflicts: 2 of 7 rows (T02, T03).
- Non-passing rows: 2 of 7 (T05, T07).
- Reusable pass evidence for the authoritative configuration: 3 of 7, synthetic only.
- DOC-READY v1 decision: `blocked-by-conflict`.

The configuration conflict overrides the nominal `pass` values. The system must not resolve the conflict by selecting a preferred firmware ID without controlled change evidence.

## Required remediation before a new gate decision

1. Establish whether `FW-GW-0.8.0` or `FW-GW-0.8.1` is the intended released firmware; revise the controlled configuration and manifest once, with owner/date/change rationale.
2. Rerun T02 and T03 on the resulting exact configuration; preserve full laboratory evidence in a real project.
3. Remove the default credential, define the credential lifecycle, and rerun T05 against the selected IEC 62443 scope.
4. Complete the Korea/EU market-route decision and rerun T07 against the final product configuration.

## Learning update

The traceability guard is validated: a `pass` result with a mismatched configuration is unusable evidence. Add no product-specific knowledge from this synthetic bundle.
