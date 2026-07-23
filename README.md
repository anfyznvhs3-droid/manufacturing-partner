# 제조업파트너 · Manufacturing Partner

제조·반도체 문서를 한 명의 운영자가 최대 20명의 엔지니어 자료로부터 받아, 출처와 사람 검증을 보존한 하나의 `manufacturing-gate/v1` 결과로 정리하는 Codex 스킬입니다.

## 바로 보기

- [제조업파트너 공개 스토리](index.html)
- [동료용 스킬 설명 슬라이드](skill-slides.html)
- [역할별 업무 흐름도](my-workflow-skill/assets/workflow-algorithm/index.html)

## 문제와 해결 방식

- 긴 문서를 그대로 읽어 토큰을 낭비하지 않고 원자 사실로 분해합니다.
- AI가 만든 문장을 사실로 확정하지 않고, 사람이 출처와 맥락을 확인합니다.
- 제조 현장의 암묵지를 추측으로 채우지 않고 확인 질문과 재사용 가능한 기록으로 바꿉니다.
- 벤더 선언, 구두 인수인계, 상충 시험성적서도 동일한 출력 계약으로 통합합니다.

## 운영 모델

제작·운영팀은 2명이며, 실제 스킬 사용자는 1명입니다. 최대 20명의 엔지니어가 자료를 제공하고, 원본 소유자에게만 사실 확인을 요청합니다. `ready`는 문서 상태일 뿐 운전·출하·공정변경 권한을 의미하지 않습니다.

## 반복 학습과 점진 개선

각 회차는 `등록 → 사실 분해 → 출처 대조 → 사람 확정 → 지표 계산 → Learning update`로 반복됩니다. 사람 확정 정확도가 99.0% 이상이고 필수 증거 누락·충돌·권한 위반이 없으면 루프를 멈추고 `owner_notification`을 통합 출력에 기록합니다. 99% 미만이면 다음 회차의 질문과 규칙을 생성합니다.

## 파일 안내

- [`my-workflow-skill/SKILL.md`](my-workflow-skill/SKILL.md): 스킬 사용 규칙과 반복 학습 방법
- [`assets/public-explainer/index.html`](my-workflow-skill/assets/public-explainer/index.html): 대중용 제조 스토리
- [`assets/workflow-algorithm/index.html`](my-workflow-skill/assets/workflow-algorithm/index.html): INPUT → ALGORITHM → OUTPUT 흐름
- [`references/review-rubric.md`](my-workflow-skill/references/review-rubric.md): 사실·맥락·출처 검수 기준
- [`references/international-standards-baseline.md`](my-workflow-skill/references/international-standards-baseline.md): 국제표준 적용 가드레일
- [`mock-data/`](my-workflow-skill/mock-data/): 익명 예시와 기대 결과
- [`scripts/`](my-workflow-skill/scripts/): 입력 검증·지표 계산·통합 출력 도구

## 품질 원칙

국제표준은 적용 범위를 정하는 참고 기준으로만 사용하며 인증이나 법적 적합성을 주장하지 않습니다. 실제 제품의 운영 권한은 사람이 확인하고 결정합니다.

## 검증

```powershell
python -X utf8 "$PWD/my-workflow-skill/scripts/validate_public_story_html.py" `
  --input "$PWD/my-workflow-skill/assets/public-explainer/index.html" `
  --contract "$PWD/my-workflow-skill/mock-data/public-story-html/expected-contract.json"
```

GitHub 저장소: <https://github.com/anfyznvhs3-droid/manufacturing-partner>
