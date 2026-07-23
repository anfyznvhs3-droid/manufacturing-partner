---
name: manufacturing-document-review
description: 제조·반도체 자료를 쉽게 읽고, 여러 엔지니어의 내용을 출처별로 확인해 하나의 안전한 결과로 정리해야 할 때 사용한다.
---

# 제조 자료 검토 스킬

## 이 스킬을 한 문장으로 말하면

여러 사람이 보낸 자료를 한 명의 운영자가 모아, **확인된 사실·아직 모르는 것·서로 다른 내용**을 구분해 하나의 결과로 정리하는 도구다.

AI가 그럴듯하게 말하더라도 근거가 없으면 사실로 확정하지 않는다.

## 제조도메인 암묵지를 다루는 이야기

제조 현장의 중요한 지식은 데이터시트에 모두 적혀 있지 않다. 같은 “정상 동작”이라는 말도 제품 세대, 공정 단계, 검사 장비, 고객 요구에 따라 다른 의미가 될 수 있다. 작업자는 이런 차이를 경험으로 알고 있지만, AI는 문서에 표현된 범위만 볼 수 있다.

그래서 이 스킬은 암묵지를 자동으로 채우지 않는다. 문서에 있는 말과 현장에서 통용되는 말을 분리하고, 약어·임계값·공정 조건·예외 상황을 질문으로 바꾼 뒤, 해당 제품이나 공정을 만든 엔지니어에게 확인을 요청한다. 확인 전에는 `inferred`, `missing`, `conflicting` 상태를 유지하고, 확인된 답변만 출처와 함께 통합 결과에 반영한다.

이 구조는 AI가 제조 전문성을 대신한다고 주장하지 않는다. 사람의 암묵지를 짧은 질문과 추적 가능한 근거로 바꾸어 다음 문서에서도 재사용할 수 있게 한다. 공개 설명은 [스토리 페이지](assets/public-explainer/index.html), 입력·알고리즘·출력 연결은 [워크플로 알고리즘](assets/workflow-algorithm/index.html)에서 확인한다.

## 누가 어떻게 사용하는가

- 스킬을 사용하는 사람: 1명
- 자료를 보내는 사람: 최대 20명의 엔지니어
- 최종 기준을 관리하는 팀: 우리 2명
- 확인 요청을 받는 사람: 해당 자료를 실제로 만든 엔지니어

20명의 엔지니어가 스킬을 각각 쓰는 구조가 아니다. 한 명의 운영자가 자료를 받아 이 스킬로 정리한다.

## 언제 사용하는가

다음 자료가 들어오면 사용한다.

- 긴 데이터시트나 기능 설명서
- 구두 인수인계나 메신저 내용
- 시험 계획서와 시험 결과
- 벤더 선언서
- 품질 이슈, 정비 기록, 생산 기록
- 서로 내용이 다른 문서 묶음

## 처음 사용하는 동료를 위한 입력 계약

입력은 `operator-intake/v1` JSON 한 개로 시작한다. 아래 항목이 없으면 처리하지 말고 `insufficient-source`로 돌린다.

| 항목 | 반드시 넣을 내용 |
| --- | --- |
| `intake_batch_id` | 이번 검토 배치의 고유 ID |
| `operator.operator_id` | 스킬을 실행한 한 명의 운영자 ID(실명 대신 사내 별칭) |
| `sources[]` | 1~20개 출처의 ID, 소유자 ID, 유형, 수신 시각, 개정, 범위, 구성 ID, 증거 수준, 원본 위치 |
| `claims[]` | 원문에서 분해한 주장과 연결된 `source_ids` |
| `confirmation_queue[]` | 확인할 질문, 대상 `source_id`, 확인 담당자 |

최소 입력 예시는 [operator-intake-sample.json](mock-data/goal12-operator-intake/operator-intake-sample.json)이다. 먼저 아래 명령으로 입력 계약을 검사한다.

```powershell
python scripts/validate_multisource_intake.py `
  --input mock-data/goal12-operator-intake/operator-intake-sample.json `
  --report mock-data/goal12-operator-intake/operator-intake-validation-report.json
```

## 개인정보·고객정보·기밀정보 보호

해커톤과 공개 저장소에는 실제 회사 자료를 넣지 않는다. 입력 전 운영자는 다음을 수행한다.

1. 이름·이메일·전화번호·사번·계정·토큰·주소를 운영자/소유자 별칭으로 치환한다.
2. 고객명·제품 일련번호·주문번호·내부 URL·접근 키·회사 기밀 수치와 도면을 삭제하거나 합성값으로 바꾼다.
3. 원본은 회사 승인 저장소에만 두고, `original_record_locator`에는 `controlled://` 같은 비밀을 노출하지 않는 위치만 적는다.
4. 공개 예시에는 `synthetic-training`, `public-vendor` 수준의 자료만 사용한다.
5. 실수로 기밀이 들어오면 즉시 처리를 중단하고 해당 원본 소유자와 보안 담당자에게 알린다.

이 저장소의 `assets/public-sources/`와 `mock-data/`는 공개·합성 예시이며 실제 회사·고객 데이터를 대표하지 않는다.

## 반복 학습과 99% 중단 규칙

이 스킬은 한 번의 답변으로 끝내지 않는다. 매 회차의 오류·누락·충돌을 다음 회차의 질문과 규칙에 반영해 조금씩 더 정확하게 만든다.

1. 입력을 출처별로 등록하고 원자 사실로 분해한다.
2. AI 결과를 독립적인 관점으로 재검토한다.
3. 사람이 `ratified`, `corrected`, `rejected`, `not-reviewable` 중 하나로 확정한다.
4. precision, recall, 충돌 탐지율, 출처 일치율을 계산한다.
5. 오류 유형을 `Learning update`에 추가하고 다음 회차의 질문·루브릭·예시에 반영한다.
6. 동일한 검증을 다시 실행해 개선 폭을 기록한다.

정확도는 AI의 자기평가가 아니라 사람이 확정한 라벨을 기준으로 계산한다. 사람 확정 사실의 정량 정확도가 **99.0% 이상**이고, 필수 증거 누락·충돌·권한 위반이 0건이면 반복을 멈춘다. 멈출 때는 최종 출력에 다음을 포함해 담당자에게 알림 상태를 남긴다.

```json
{
  "recursive_status": "stopped_at_threshold",
  "accuracy_percent": 99.0,
  "threshold_percent": 99.0,
  "owner_notification": {
    "required": true,
    "message": "사람 확정 정확도 99% 이상에 도달했습니다. 다음 회차를 중단하고 담당자 확인을 요청합니다.",
    "channel": "manufacturing-gate/v1"
  }
}
```

99%에 도달하지 못했거나 충돌·필수 누락·권한 위반이 하나라도 있으면 `recursive_status`를 `continue`로 두고 다음 회차를 제시한다. 이 스킬은 외부 메신저로 자동 발송하지 않으며, 위 알림 객체를 통해 담당자가 확인할 수 있는 감사 기록을 만든다.

## 처리 방법

### 1. 자료를 먼저 등록한다 [근거 1]

한 번에 1~20개 출처만 등록한다. 20개를 넘으면 출처를 섞지 말고 배치를 나눈다.

각 자료에 다음 정보를 붙인다.

`source_id`, 원본 위치, 받은 시각, 작성일/개정, 대상 범위, 구성 ID, 증거 수준

등록 검사는 다음 명령으로 한다.

```powershell
python scripts/validate_multisource_intake.py --input <intake.json> --report <report.json>
```

### 2. 문장을 작은 사실로 나눈다 [근거 2]

각 사실을 아래 네 가지 중 하나로 표시한다.

| 상태 | 쉬운 뜻 |
| --- | --- |
| `stated` | 원문에 그대로 적혀 있음 |
| `inferred` | 원문을 보고 추측한 내용 |
| `missing` | 필요한데 자료에 없음 |
| `conflicting` | 자료끼리 서로 다름 |

추측한 내용은 `stated`로 바꾸지 않는다.

### 3. 애매한 말을 표시한다 [근거 2·3]

다음 표현은 그대로 믿지 말고 질문으로 바꾼다.

- “평소처럼”, “정상”, “빠르게”, “적당히”
- 설명되지 않은 약어와 현장 용어
- 위치가 불분명한 표현
- 숫자 없는 임계값
- 개인의 기억에만 의존한 작업 지시

### 4. 문서 상태를 결정한다 [근거 3]

`DOC-READY v1` 기준으로 아래 네 상태 중 하나만 사용한다.

- `ready`: 필요한 사실과 근거가 연결됨
- `needs-fact-confirmation`: 사실 확인이 더 필요함
- `blocked-by-conflict`: 자료가 서로 충돌함
- `insufficient-source`: 자료 자체가 부족함

점수가 높아도 필수 증거가 없으면 `ready`로 올리지 않는다.

### 5. 운영 권한을 따로 결정한다 [근거 4]

문서가 읽기 좋다는 것과 실제 제품을 운전해도 된다는 것은 다르다.

- `denied`: 충돌, 핵심 증거 부족, 합성 핵심 증거가 있음
- `pending-authority`: 확인할 내용이나 승인 권한자가 남아 있음
- `authorized`: 모든 실제 증거와 승인 권한이 갖춰진 경우에만 가능

이 스킬은 `authorized`를 대신 결정하지 않는다. 실제 운전·출하·폐기·재작업·공정변경을 AI가 단독으로 승인하지 않는다.

## 반드시 지키는 규칙 [근거 4·5]

1. 벤더 부품 자료를 최종 제품의 안전·규제 적합성으로 확대하지 않는다.
2. 구두 주장과 시험 계획을 시험 결과로 바꾸지 않는다.
3. 충돌한 두 자료 중 하나를 임의로 선택하지 않는다.
4. 확인 질문은 해당 `source_id`의 원본 소유자에게만 보낸다.
5. 국제표준은 적용 범위를 정하는 참고 기준이다. 인증서나 법적 판단이 아니다.
6. 합성 예시는 학습용일 뿐 실제 제품 증거가 아니다.

## 최종 답변 형식

항상 아래 순서로 답한다.

1. `Normalized handover`: 누구나 읽을 수 있는 짧은 인수인계
2. `Fact audit`: 사실, 출처, 상태, 문제
3. `Fact confirmation queue`: 누구에게 무엇을 물을지
4. `Metrics and decision`: 숫자, 문서 상태, 운영 권한, 이유
5. `Learning update`: 다음 검토에 적용할 규칙

마지막 결과는 반드시 `manufacturing-gate/v1` 형식으로 만든다. 이 형식은 모든 입력을 같은 모양으로 보여주기 위한 계약이다.

최종 JSON에는 최소한 `contract`, `review_decision`, `operational_authorization`, `claims`, `confirmation_queue`, `metrics`, `learning_update`, `recursive_status`, `owner_notification`을 포함한다. `review_decision`은 `ready`, `needs-fact-confirmation`, `blocked-by-conflict`, `insufficient-source` 중 하나이고, `operational_authorization`은 `denied`, `pending-authority`, `authorized` 중 하나다.

## 사람이 반드시 확인할 부분

AI가 제안한 결과를 그대로 제출하지 않는다. 담당자는 다음을 직접 확인하고 이름/ID와 시각을 기록한다.

- 각 `claim`이 실제 원본의 해당 페이지·표·시험 기록과 일치하는가
- `inferred`, `missing`, `conflicting` 상태가 누락되지 않았는가
- 구성 ID·개정·시험 조건이 같은 제품 범위를 가리키는가
- 벤더 선언이나 구두 인수인계를 시험 결과·안전 적합성으로 확대하지 않았는가
- 충돌이 있으면 `blocked-by-conflict`로 멈췄는가
- `authorized`가 필요한 경우 실제 권한자와 승인 증거가 존재하는가
- 99% 중단 조건의 정확도 산정에 사람 확정 라벨만 사용했는가

## 자주 쓰는 도구 [근거 1·2·4]

- `scripts/validate_multisource_intake.py`: 한 운영자와 출처 1~20개를 검사한다.
- `scripts/build_unified_output.py`: `manufacturing-gate/v1` 결과를 만든다.
- `scripts/verify_unified_outputs.py`: 충돌·모호성·벤더 자료 사례를 다시 검사한다.
- `scripts/score_atomic_fact_extraction.py`: 사람이 확정한 라벨만으로 사실 precision/recall을 계산한다.
- `scripts/extract_pdf_text_metrics.py`: 긴 PDF를 한 번 추출하고 핵심 사실만 다음 검토에 전달한다.

## mock-data 재실행 순서

처음 보는 동료는 실제 자료 대신 아래 합성 자료로 전체 흐름을 재현할 수 있다.

```powershell
# 1) 입력 계약
python scripts/validate_multisource_intake.py `
  --input mock-data/goal12-operator-intake/operator-intake-sample.json `
  --report mock-data/goal12-operator-intake/operator-intake-validation-report.json

# 2) 상충·모호·벤더 선언 가드레일
python scripts/verify_unified_outputs.py `
  --directory mock-data/goal11-adversarial `
  --expectations mock-data/goal11-adversarial/expectations.json `
  --report mock-data/goal11-adversarial/verification-report.json

# 3) 공개 스토리 HTML 계약
python scripts/validate_public_story_html.py `
  --input assets/public-explainer/index.html `
  --contract mock-data/public-story-html/expected-contract.json `
  --report mock-data/public-story-html/validation-report.json

# 4) 사람 라벨 기반 사실 추출 지표
python scripts/score_atomic_fact_extraction.py --help
```

각 명령의 `valid`, `keys_ok`, `review_ok`, `authorization_ok`를 확인한다. 마지막 명령은 실제 라벨 파일을 연결해야 하므로, 사람 확정 라벨 없이 정확도를 주장하지 않는다.

## 파일 구조 점검

배포 전 `references/`, `scripts/`, `assets/`, `mock-data/` 각각에 실제 파일이 하나 이상 있는지 확인한다. 이 네 폴더가 비어 있으면 스킬을 배포하지 않는다.

자세한 기준은 다음 자료를 필요할 때만 읽는다.

- [검토 루브릭](references/review-rubric.md)
- [반복 연구 절차](references/recursive-research-protocol.md)
- [단일 운영자·다중 출처 계약](references/single-operator-multisource-intake.md)
- [통합 출력 계약](references/unified-output-contract.md)
- [국제표준 기준선](references/international-standards-baseline.md)

## 근거 각주

아래 각주는 이 스킬의 규칙이 임의의 조언이 아니라, 지금까지 만든 계약·루브릭·검증 결과에 연결되어 있음을 보여준다.

## 근거 1 — 여러 출처를 한 운영자가 받는 구조

[단일 운영자·다중 출처 계약](references/single-operator-multisource-intake.md)은 한 배치에 출처 1~20개를 등록하고, 각 출처의 소유자와 원본 위치를 보존하도록 정한다. `validate_multisource_intake.py`의 계약 테스트도 이 규칙을 확인한다.

## 근거 2 — 사실과 추측을 나누는 방법

[검토 루브릭](references/review-rubric.md)은 원자 사실을 `stated`, `inferred`, `missing`, `conflicting`으로 나눈다. 이 구분이 있어야 AI가 자연스럽게 쓴 문장을 사실로 잘못 확정하지 않는다.

## 근거 3 — 문서 준비 상태를 결정하는 방법

[반복 연구 절차](references/recursive-research-protocol.md)는 `DOC-READY v1`의 네 상태와 확인 큐를 정의한다. 점수는 우선순위에 쓰지만 필수 증거가 없는 문서를 `ready`로 바꾸지 않는다.

## 근거 4 — 문서 판정과 운영 권한을 분리하는 방법

[통합 출력 계약](references/unified-output-contract.md)은 `review_decision`과 `operational_authorization`을 분리한다. GOAL 10~13의 구성 사례에서도 문서가 `ready`여도 합성 증거·충돌·권한 부족이면 운영 권한은 `denied` 또는 `pending-authority`로 남았다.

## 근거 5 — 국제표준을 사용하는 범위

[국제표준 기준선](references/international-standards-baseline.md)은 ISO/IEC 표준을 인증서처럼 사용하지 않고, 적용 범위·판본·근거를 선택하는 참고 기준으로만 사용하게 한다.

## 근거 6 — 시간 제한 상황의 임시 정확도

[GOAL 13 AI 블라인드 합의 결과](mock-data/goal13-blind-consensus.json)는 독립 에이전트 3개의 30개 후보 대조 결과를 기록한다. `96.7%`는 임시 합의 지표이며 사람 확정 사실 정확도나 운영 승인이 아니다.

## 워크플로 알고리즘 HTML

입력부터 최종 출력까지의 흐름은 [워크플로 알고리즘 HTML](assets/workflow-algorithm/index.html)에서 한 화면으로 확인할 수 있다. 이 페이지의 알고리즘도 입력을 바로 승인으로 바꾸지 않고, 사실 분해·충돌 검사·확인 큐를 거친다.
