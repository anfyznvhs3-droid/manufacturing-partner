# GOAL 4 pilot: manufacturing handover review

## Input

Review the source in `../references/example-tacit-knowledge.md`.

## Normalized handover (AI draft; not approved)

- Event: 7/23 10:15, assembly line 2, press 03, hole-diameter nonconformance.
- Evidence: limit 10.00 +/- 0.05 mm; 3 of 12 samples exceeded the upper limit.
- Scope and containment: 186 units are isolated; exact isolation location is not stated.
- Action/result: die clamping torque was retightened; five trial parts measured 9.98 to 10.03 mm.
- Unresolved: punch wear and material thickness have not been checked.
- Escalation: the document asks operators to stop when the same condition is observed, but it gives no measurable recurrence trigger.

## Atomic-fact audit

| ID | atomic fact | AI label | evidence | reviewer A | reviewer B | resolved label |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | Event time is 7/23 10:15. | stated | `7/23 10:15` |  |  |  |
| F02 | Equipment is assembly line 2, press 03. | stated | `조립2라인 프레스03` |  |  |  |
| F03 | Limit is 10.00 +/- 0.05 mm. | stated | `기준은 10.00±0.05mm` |  |  |  |
| F04 | 3 of 12 samples exceeded the upper limit. | stated | `12개 중 3개가 상한을 넘었습니다` |  |  |  |
| F05 | 186 units are isolated. | stated | `186개는 격리` |  |  |  |
| F06 | Die clamping torque was retightened. | stated | `체결 토크는 재체결` |  |  |  |
| F07 | Five trials measured 9.98 to 10.03 mm. | stated | `시제품 5개는 9.98~10.03mm` |  |  |  |
| F08 | Punch wear is unconfirmed. | stated | `펀치 마모 ... 확인 전` |  |  |  |
| F09 | Material thickness is unconfirmed. | stated | `소재 두께는 아직 확인 전` |  |  |  |
| F10 | Recurrence requires a production stop and report. | ambiguous | `같은 느낌 ... 바로 멈추고` |  |  |  |

Allowed labels: `stated`, `inferred`, `missing`, `conflicting`, `ambiguous`.

## Human review queue

1. Define the exact isolation location and traceability identifier for the 186 units.
2. Replace `평소보다 신경 써서`, `같은 느낌`, and `제가 보던 방식` with a sampling method, a numeric stop trigger, and an authorized decision owner.
3. Name the owner and due point for punch-wear and material-thickness checks.
4. Confirm whether final restart approval belongs to Quality, Production Engineering, or another named role.

## Metrics before human review

- Required-fact coverage: 9 / 10 = 90%; F10 is not measurable enough to accept.
- Unsupported-claim count in AI draft: 0.
- Critical ambiguity count: 2 (isolation traceability; recurrence trigger/decision rule).
- Traceability: 10 / 10 = 100% for extracted claims.
- Actionability: 0 / 2 = 0%; neither unresolved item has an owner and due point.
- Baseline weighted score: 68.5 / 100. This is a screening estimate, not an approval.

## Learning update: proposed only

| type | source phrase | proposed rule | status |
| --- | --- | --- | --- |
| review rule | `다들 아는 쪽` | Require a physical location and lot/containment identifier. | proposed |
| review rule | `평소보다 신경 써서` | Require a sampling frequency and acceptance criterion. | proposed |
| review rule | `같은 느낌` | Require a measurable stop/escalation trigger. | proposed |
| review rule | `제가 보던 방식` | Require a documented method and authorized decision owner. | proposed |

Promote a row only after both reviewers approve it, or a documented domain owner approves it.
