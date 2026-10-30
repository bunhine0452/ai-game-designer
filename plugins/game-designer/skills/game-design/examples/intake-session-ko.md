# Example: Korean-language intake and routing

This shows the language rules at work: the answer is in Korean, each technical term is
localized and followed by the English term in parentheses on first use, and the intake
asks only for what is missing.

---

**User:** 몬스터랑 같이 농사짓는 힐링 게임 만들고 싶어. 어디서부터 시작하지?

**Assistant:**

좋은 출발점이에요. 바로 설계에 들어가기 전에 빠진 정보만 짧게 확인할게요.
답하기 귀찮으면 "기본값으로" 라고만 해 주세요.

| 항목 | 질문 | 기본값 |
|---|---|---|
| 플랫폼 | PC, 스위치, 모바일 중 어디인가요? | PC + 게임패드 |
| 세션 길이 (Session Length) | 한 번에 보통 몇 분 플레이하나요? | 20~40분 (게임 속 하루 2~3번) |
| 대상 플레이어 | 누구를 위한 게임인가요? | 스타듀 밸리류를 좋아하는 힐링 게임 플레이어 |
| 개발 단계 | 아이디어 단계인가요, 프로토타입이 있나요? | 아이디어 단계 |

그동안 방향을 잡을 수 있게 첫 설계 초안을 드릴게요.

- **목표 미학 (Target Aesthetics):** 1순위 소일거리 (Submission), 2순위
  발견 (Discovery), 3순위 표현 (Expression). 긴장감보다는 "틀어 두고 편하게 하는 재미"가
  중심이에요.
- **디자인 기둥 (Design Pillars)**
  1. *몬스터 하나하나가 농장을 바꾼다*: 이 몬스터가 지형, 작물, 동선 중 하나라도 바꾸나요?
  2. *실패는 없고, 우회만 있다*: 실수 하나로 진행이 막힐 수 있다면 다시 설계합니다.
  3. *관찰로 발견한다*: 툴팁 없이 세상을 보고 배울 수 있나요?
- **코어 루프 (Core Loop)**
  - 순간순간의 플레이: 쓰다듬기·먹이 주기·몬스터 이끌기 → 지형이 바뀌는 피드백 → 작은 수확
  - 세션 루프: 오늘의 밭 목표 고르기 → 몬스터 능력 조합 → 수확 → 씨앗·몬스터 해금 → 다음 목표
  - 메타 루프 (Meta Loop): 계곡 복원 지도, 몬스터 도감, 계절 축제

다음 단계로 이런 걸 해 드릴 수 있어요.

1. 하루 한 사이클의 **관심 곡선 (Interest Curve)** 을 그려서 지루한 구간 찾기 → `fun-curve`
2. 농장 시뮬레이션·힐링 장르의 **장르 플레이북 (Genre Playbook)** 정리 → `genre-design`
3. 작물 판매 가격과 몬스터 먹이 비용의 **재화 유입처 (Faucet)와 소모처 (Sink)** 모델링 →
   `balance-economy`

어떤 것부터 할까요?

---

## What this example shows

- The whole answer is Korean. Skill names (`fun-curve`) stay in English because they are
  identifiers.
- The first use of each term adds the English term: `관심 곡선 (Interest Curve)`. A repeat
  use (e.g. `코어 루프` in a later message) would drop the parentheses.
- Glossary entries were used: 디자인 기둥, 코어 루프, 메타 루프, 재화 유입처/소모처.
- The intake asked only for four missing facts and offered defaults. Genre was inferred
  from the pitch.
