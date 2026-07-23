# Review rubric

## Atomic-fact schema

Extract one record per claim for: event time; line/equipment; product or lot; measured characteristic; specification; sample size; nonconforming count; affected quantity; containment; action; result; unresolved cause; owner; due point; stop/escalation trigger. Mark source text and status.

## Metrics

Use an agreed reference set of required atomic facts.

- Fact coverage = matched required facts / required facts × 100.
- Unsupported-claim count = claims in the normalized handover not supported by the source.
- Critical ambiguity count = unresolved ambiguity in equipment, lot/scope, limit, disposition, owner, or trigger.
- Traceability = claims with a source excerpt / all normalized claims × 100.
- Actionability = unresolved items with both owner and trigger or due point / all unresolved items × 100.
- Weighted review score = 0.35 × coverage + 0.25 × traceability + 0.25 × actionability + 0.15 × (100 − 10 × critical ambiguity count), bounded to 0–100.

Do not calculate an accuracy rate without a human-labeled reference set. Call the first AI score a `baseline estimate`.

## Acceptance gates

- Use the `DOC-READY v1` gate decision in [recursive-research-protocol.md](recursive-research-protocol.md) as the authority; the weighted score cannot override it.
- Coverage ≥ 98% for critical facts.
- Unsupported critical claims = 0.
- Critical ambiguity count = 0 for `ready`; otherwise retain each ambiguity in the fact-confirmation queue.
- Ask a source owner only to confirm disputed source facts, site terms, or proposed actions. Use two independent reviewers and Cohen's kappa only when the user explicitly requests an agreement study.

## Recursive learning ledger

After human review, record one row per approved change:

| type | source phrase | approved meaning or rule | scope | evidence link | reviewer/date | status |
| --- | --- | --- | --- | --- | --- | --- |
| terminology | | | line/site | | | proposed/approved/retired |
| review rule | | | document type | | | proposed/approved/retired |

Promote a rule only after two independent approved examples, or after an explicitly documented domain-owner approval. Retire a rule when it creates an unsupported claim. Keep the original source phrase so later reviewers can audit the learning.
