# Interest curve report: 종이연 우편부 v2

| Metric | Value |
|---|---|
| Duration | 14.5 min |
| Beats | 29 |
| Mean intensity | 5.36 / 10 |
| Peaks (≥ threshold) | 7 |
| Climax | 10 at 13.25 min (91% through) |
| Hook strength | 7 / 10 |
| Time at high intensity | 9% |
| Time at low intensity | 7% |
| Pacing health (heuristic) | 100 / 100 |

![Interest curve](beats_v2_curve.png)

## Findings

No pacing problems detected by the heuristics. Validate with playtests.


## Curve (text view)

```
 10 |                                                          o     
  9 |                                              o      o   ··     
  8 |                             o        o      ··    ·· ·         
  7 | o                    o     ·        ·     ··     o     ·       
  6 |       o       o     · ·   ·  ·     ·  ·  o    · ·     ·   ·    
  5 |  ·   ··   o  · ·   o     o        o     ·             o        
  4 |o    o  · · ·    · ·    ·          ·    o       o           o   
  3 |   o·    o   o    o      o     o· ·                          ·· 
  2 |                                 o                             o
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         14.5
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 4 | hook | 바람에 날린 편지 |
| 0.25 | 7 | hook | 탑에서 다이브·군도 공개 |
| 0.75 | 3 | tutorial | 편지 잡고 발사대 착지 - 우체국장 한 줄 임명 |
| 1.08333 | 4 | tutorial | #1 이륙 - 조작은 화면 힌트로만 |
| 1.5 | 6 | tutorial | #1 첫 상승기류 선회 - 등대가 시야에 솟음 |
| 2 | 3 | reward | #1 등대지기 배달 - 첫 우표 |
| 2.5 | 5 | flight | #2 빵집 섬 - 기류 2개 중 하나 고르기 |
| 3 | 3 | reward | #2 배달 - 갓 구운 빵 냄새 연출 |
| 3.41667 | 6 | challenge | #3 종탑 - 종이 울리기 전 도착(첫 타임어택) |
| 4.08333 | 3 | reward | #3 배달 - 종소리로 금우표 판정 |
| 4.5 | 5 | flight | #4 풍차 군도 - 섬 3개 경유 |
| 5.16667 | 7 | challenge | #4 풍차가 끊는 기류 |
| 5.66667 | 3 | reward | #4 배달 - 초대장 받은 할머니 |
| 6.08333 | 5 | flight | #5 폭포섬 - 여분 기류 0개 |
| 6.75 | 8 | challenge | #5 폭포 다이브 |
| 7.16667 | 3 | reward | #5 연애편지 배달 - 짧은 사연 |
| 7.58333 | 2 | rest | 우체국 귀환 - 연 꼬리 해금 / 노을 전 한낮 정적 |
| 8.16667 | 5 | flight | #6 구름 다리 - 강한(좁은) 기류 등장 |
| 8.83333 | 8 | challenge | #6 좁은 금색 기류 |
| 9.25 | 4 | reward | #6 배달 - 하늘이 남보라로 변함 |
| 9.75 | 6 | flight | #7 폭풍 전선 진입 - 역풍 |
| 10.5 | 9 | challenge | #7 번개 사이 기류 |
| 11 | 4 | rest | #7 배달 - 폭풍 속 피난처 섬에서 숨 고르기 |
| 11.5 | 7 | flight | #8 마지막 편지 - 바람길(뒷바람) 첫 등장 |
| 12.25 | 9 | challenge | #8 폭풍 벽 |
| 12.75 | 5 | reveal | 폭풍의 눈 - 고요 속 하늘 우체국 첫 모습 |
| 13.25 | 10 | climax | 최종 다이브·편지 투하 |
| 13.75 | 4 | story | 받는 사람 공개 - 편지는 우편부 자신에게 |
| 14.5 | 2 | story | 크레딧 - 자유 비행 |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
