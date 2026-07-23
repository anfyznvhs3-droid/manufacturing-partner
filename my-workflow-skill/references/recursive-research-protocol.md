# Recursive research protocol for manufacturing documents

## Purpose

Improve document review quality without repeatedly rereading full documents or silently turning uncertain manufacturing knowledge into fact. This protocol adapts the operational ideas in the archived CDC prompt: precise success conditions, independent early exploration, an approach registry, adversarial audit, concrete artifacts, and explicit stall rules. It does not rely on or assert the mathematical claims surrounding that source.

## GOAL contract

Every GOAL must state: input corpus; document class; required schema; non-negotiable safety boundaries; measurable acceptance gates; and a bounded deliverable. Reject a result that is only a summary, an elegant restatement, or an unverified reduction.

## Task list and GOAL categories

| Task | GOAL category | Output |
| --- | --- | --- |
| Archive external inputs and set a source baseline | GOAL 1: establish evidence | manifest with URL, timestamp, and SHA-256 |
| Define required fact schema and decision gates | GOAL 2: define contract | schema and `DOC-READY` rules |
| Generate diverse independent examples or analyses | GOAL 3: diversify | approach registry and source documents |
| Extract evidence-led facts without full-document repetition | GOAL 4: compress safely | fact table with excerpts and uncertainty labels |
| Attack missing facts, unsafe inferences, and terminology | GOAL 5: adversarial audit | counterexample/ambiguity log |
| Decide readiness and request only necessary confirmations | GOAL 6: gate decision | decision plus confirmation queue |
| Promote approved terms and rules; retire harmful rules | GOAL 7: learn | append-only ledger update |

After each GOAL, issue the next uncompleted GOAL command. Do not advance a route merely because it sounds plausible.

## DOC-READY v1: Codex decision standard

### Required fields

For a manufacturing handover: event/time, product or lot, line/equipment/configuration, specification or acceptance criterion, evidence/measurement, affected scope, containment/disposition, action/result, open issue, owner, and due point or measurable escalation trigger.

For a semiconductor product description: product/configuration, intended function, I/O or interface boundary, operating limits, fault response, verification conditions, unknown specification fields, and standards basis. Select that basis with [international-standards-baseline.md](international-standards-baseline.md); do not claim conformance from a document review.

### Evidence labels

Mark every extracted claim `stated`, `inferred`, `missing`, `conflicting`, or `site-term-unknown`. Store a source excerpt for every `stated` claim. An inference may explain a question but cannot satisfy a required field.

### Gate decision

- `ready`: Every required field is stated with evidence; critical evidence coverage is at least 98%; unsupported critical claims are zero; no safety-critical ambiguity remains; each open issue has an owner and a due point or measurable trigger.
- `needs-fact-confirmation`: No contradiction exists, but a required field, site term, owner, due point, or non-safety-critical action needs source-owner confirmation.
- `blocked-by-conflict`: Sources conflict, a safety state/disposition is undefined, or the requested output would authorize release, scrap, rework, or process change without an approved authority. Preserve both source claims and stop the action recommendation.
- `insufficient-source`: The input cannot establish product/configuration, required scope, or critical evidence. Request the minimal missing source instead of guessing.

The gate decision overrides the weighted quality score.

## Portfolio and registry

Keep early investigations independent. Register each approach by information type, not writing style: functional specification, FMEA, reliability, commissioning, metrology, thermal/power integrity, compliance/security, field service, supplier quality, or user/operator behavior. Do not reveal a favored hypothesis to new agents. If two routes belong to the same family, redirect the next route to an unrepresented family.

Require every agent to return a concrete artifact: source document, atomic-fact table, test condition, counterexample, terminology candidate, or explicit gap. Reject progress-only reports.

## Adversarial audit

Audit a producer's document with a different route. Search for unsupported thresholds, an unapproved safety state, configuration mismatch, missing unit/condition, vague actor (`operator`, `team`, `usual way`), site-specific term, and action without owner/trigger. A producer must not certify its own output.

## Iteration and stopping

For each round, record: gate decision; weighted quality score; critical ambiguity count; unsupported claim count; and token count used for source extraction. Promote a rule only after a source owner approves it or it recurs in two approved examples. Retire a rule after it produces an unsupported claim.

Pivot a route when two rounds yield no reduction in critical ambiguity or unsupported claims, or it requires a missing statement as strong as the original problem. Stop a document at `ready`; otherwise issue only the next GOAL that removes the highest-risk failed gate.
