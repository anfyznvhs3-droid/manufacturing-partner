# 공개 제조 검증 스토리 페이지 Implementation Plan

> **For agentic workers:** 이 계획은 승인된 공개 설명용 HTML을 단계별로 구현하고 검증한다.

**Goal:** 제조도메인 스킬을 일반인이 이해하도록 소개하는 단일 HTML 랜딩 페이지와 3상태 인터랙티브 데모를 만든다.

**Architecture:** CSS와 JavaScript를 HTML에 내장한 정적 단일 파일이다. 데이터는 공개용 문구와 이미 확정된 임시 합의 지표만 사용하고, 데모 상태는 `vendor`, `handover`, `conflict` 세 값으로 제한한다. 어떤 경로도 운영 승인 `authorized`를 표시하지 않는다.

**Tech Stack:** HTML5, CSS3, 바닐라 JavaScript, Python 표준 라이브러리 정적 검증기.

## Global Constraints

- 공개 설명용이며 투자심사·운영승인 UI가 아니다.
- 한 명의 운영자와 최대 20개 엔지니어 출처 모델을 시각화한다.
- `96.7%`는 AI 블라인드 합의 임시 지표이며 실제 사실 정확도가 아니다.
- 외부 CDN, 빌드 단계, 프레임워크를 사용하지 않는다.
- 한국어 본문을 사용하고 `manufacturing-gate/v1`, `DOC-READY`, `pending-authority`, `denied` 같은 기술 식별자는 유지한다.
- 모바일 390px와 데스크톱 1440px에서 가로 스크롤이 없어야 한다.

---

### Task 1: HTML 수용 기준 검증기 작성

**Files:**
- Create: `my-workflow-skill/scripts/validate_public_story_html.py`
- Test: `my-workflow-skill/mock-data/public-story-html/expected-contract.json`

- [ ] **Step 1: 검증 대상 계약을 JSON으로 정의한다**

`expected-contract.json`에 필수 섹션 ID, 금지 문자열 `authorized`, 필수 상태 버튼 3개, 접근성 속성 목록을 기록한다.

- [ ] **Step 2: 실패하는 검증기를 먼저 실행한다**

아직 HTML이 없으므로 `python scripts/validate_public_story_html.py --input ...`은 파일 없음 오류를 반환해야 한다.

- [ ] **Step 3: HTML 검증기를 구현한다**

표준 라이브러리 `html.parser`로 ID·문구·버튼·`aria-live`·`prefers-reduced-motion` 존재 여부를 검사하고, `authorized`가 있으면 실패한다.

- [ ] **Step 4: 검증기 단위 실행**

실행: `python my-workflow-skill/scripts/validate_public_story_html.py --input my-workflow-skill/assets/public-explainer/index.html --contract my-workflow-skill/mock-data/public-story-html/expected-contract.json`

예상: HTML이 아직 없으면 실패, HTML 구현 후 통과.

### Task 2: 공개 스토리 HTML 골격과 시각 시스템 구현

**Files:**
- Create: `my-workflow-skill/assets/public-explainer/index.html`

- [ ] **Step 1: Hero·문제 카드·운영 모델·타임라인 섹션을 작성한다**

한국어 카피와 `96.7%` 임시 지표, `20명 → 1명 → 1개 출력` 구조를 포함한다.

- [ ] **Step 2: 정확도·신뢰·CTA 섹션을 작성한다**

96.7%의 한계 문구를 반복하고, 벤더 PDF·국제표준·운영 권한을 과장하지 않는 설명을 넣는다.

- [ ] **Step 3: 반응형 CSS를 작성한다**

네이비·아이보리·청록·주황·빨강 토큰과 390px/1440px 레이아웃을 만들고, `prefers-reduced-motion`을 지원한다.

### Task 3: 3상태 데모 상호작용 구현

**Files:**
- Modify: `my-workflow-skill/assets/public-explainer/index.html`

- [ ] **Step 1: 탭 버튼에 상태 계약을 연결한다**

`data-demo="vendor|handover|conflict"`, `aria-pressed`, `aria-live`를 사용한다.

- [ ] **Step 2: 상태별 결과 카드를 렌더링한다**

벤더는 `확인 필요`, 구두 인수인계는 `정의 필요`, 상충 시험성적서는 `충돌로 중지`를 보여준다. 어느 상태도 `authorized`를 출력하지 않는다.

- [ ] **Step 3: 키보드·모션 접근성을 검증한다**

버튼이 Tab으로 이동하고, 선택 상태가 텍스트와 `aria-pressed`에 동시에 반영되며, 축소 모션 환경에서 전환 애니메이션을 제거한다.

### Task 4: 최종 정적 QA

**Files:**
- Modify: `my-workflow-skill/scripts/validate_public_story_html.py` if a discovered deterministic check needs correction.

- [ ] **Step 1: HTML 계약 검증을 실행한다**

예상: 필수 섹션·문구·접근성 검사 PASS, 금지 승인 상태 0건.

- [ ] **Step 2: 파일 구조와 상대 경로를 확인한다**

`my-workflow-skill/assets/public-explainer/index.html`을 직접 열 수 있고 외부 리소스 요청이 없어야 한다.

- [ ] **Step 3: 결과를 운영 대시보드와 연결한다**

완성 HTML의 경로와 정적 QA 결과를 `recursive-accuracy-dashboard.md`에 추가한다.
