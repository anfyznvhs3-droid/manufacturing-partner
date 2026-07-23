# International-standards baseline

## Status and boundary

Use public international standards as the default verification vocabulary because company-confidential requirements are unavailable in the skillathon. This is a document-review baseline only. It does not assert product conformity, certify a management system, replace a licensed standard, or replace country-specific legal requirements and accredited testing.

Record the exact edition and applicable clauses from a licensed or authorized copy before claiming conformance. In July 2026, ISO 9001:2015 remains published but is expected to be replaced by ISO 9001:2026; recheck edition status at each formal use.

## Default document-review references

| Purpose | Baseline | Use in this skill |
| --- | --- | --- |
| Quality-management and continual-improvement framing | ISO 9001:2015 and Amd 1:2024 | Require controlled documented information, evidence, evaluation, and improvement records. |
| Documented-information guidance | ISO 10013:2021 | Check identity, revision, approval, availability, retention, and traceability of the document/record. |
| Audit method | ISO 19011:2026 | Separate evidence collection, audit criteria, findings, and conclusion; keep the audit trail. |

## Conditional technical reference families

Select only when the product/use case makes the scope applicable. Do not invent a compliance claim.

| Condition | Candidate family | Required confirmation |
| --- | --- | --- |
| Industrial control system has connected assets or remote management | IEC 62443 series | Asset role, security level, architecture, and the exact part/edition. |
| The product implements a safety function | IEC 61508 series | Hazard analysis, claimed safety integrity, lifecycle role, and applicable part. |
| Environmental robustness is a requirement | IEC 60068 series | Exact test method, severity, acceptance criterion, and product configuration. |
| Electrostatic-discharge handling/control is relevant | IEC 61340 series | ESD control-program scope and applicable part. |
| PLC system/integration is in scope | IEC 61131 series | Product type, programming/integration scope, and applicable part. |

## Codex checks derived from the baseline

For every reviewed document, add a `standards basis` field with: `selected standard`, `edition`, `scope match`, `evidence source`, and `not applicable rationale`. If no standard is selected, return `needs-fact-confirmation`, not a conformance claim.

For every test statement, require a test object/configuration, condition, method, acceptance criterion, result, instrument or source reference, performer/date, and record identifier. Missing fields make the test statement non-verifiable.

## Official reference pages

- ISO 9001:2015: https://www.iso.org/standard/62085.html
- ISO 10013:2021 release: https://committee.iso.org/sites/tc176/home/news/content-left-area/news-and-updates/release-of-iso-100132021-quality.html
- ISO 19011:2026: https://www.iso.org/standard/19011
- IEC 62443 overview entry: https://webstore.iec.ch/en/publication/7031
