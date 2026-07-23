# 단일 운영자·다중 출처 접수 계약

## 적용 범위

스킬 사용자는 한 명이다. 이 운영자는 최대 20명의 엔지니어에게서 들어온 문서, 구두 인수인계, 시험 기록, 벤더 선언, 이메일, 외부 웹 출처를 한 배치로 접수한다. 출처가 20개를 넘으면 임의로 합치지 말고 범위·구성 기준으로 배치를 분할한다.

`operator-intake/v1`은 접수 단계의 계약이다. 최종 결론은 언제나 [unified-output-contract.md](unified-output-contract.md)의 `manufacturing-gate/v1`으로만 반환한다.

## 필수 구조

```json
{
  "contract": "operator-intake/v1",
  "intake_batch_id": "INT-YYYY-NNN",
  "operator": {"operator_id": "OP-..."},
  "sources": [
    {
      "source_id": "SRC-...",
      "source_owner_id": "ENG-...",
      "artifact_type": "document | verbal-handover | test-record | vendor-declaration | email | external-web-source",
      "received_at": "ISO-8601 timestamp",
      "authored_or_revision": "record date or revision",
      "scope": "product/process/lot or stated unknown",
      "configuration_id": "configuration ID or stated unknown",
      "evidence_level": "approved provenance type",
      "original_record_locator": "immutable original location or record ID"
    }
  ],
  "claims": [{"claim_id": "CLM-...", "statement": "", "source_ids": ["SRC-..."]}],
  "confirmation_queue": [{"queue_id": "CQ-...", "source_id": "SRC-...", "request": ""}]
}
```

## 처리 규칙

1. 운영자 ID는 하나만 기록한다. 운영자는 접수·정규화 담당자이며, 자료의 사실 소유자나 승인 권한자가 아니다.
2. 각 자료는 출처·원본 위치·수령시각·작성일/개정·범위·구성·증거 수준을 보존한다. 알 수 없는 값은 빈칸으로 두지 말고 `stated unknown`으로 기록하고 확인 큐에 넣는다.
3. 원자 주장은 하나 이상의 `source_id`만 참조한다. 서로 다른 구성·개정의 주장을 하나의 사실로 병합하지 않는다.
4. 구두 인수인계는 `verbal-handover`로 등록한다. 확인 전에는 증거가 아닌 미확인 주장이다.
5. 확인 요청은 해당 `source_id`의 `source_owner_id`에게만 보낸다. 다른 엔지니어의 추측으로 닫지 않는다.
6. 출처 충돌, 핵심 구성 미확인, 근거 부족은 `manufacturing-gate/v1`의 `conflicts` 또는 `confirmation_queue`로 넘긴다. 운영자는 이를 해소했다고 선언할 수 없다.

## 자동 검증

```powershell
python scripts/validate_multisource_intake.py --input <intake.json> --report <report.json>
```

검증기는 출처 수 1~20, 필수 출처 추적 필드, 주장/확인 큐의 출처 참조를 검사한다. 통과는 접수 추적성만 뜻하며 문서 준비도나 운영 권한을 뜻하지 않는다.
