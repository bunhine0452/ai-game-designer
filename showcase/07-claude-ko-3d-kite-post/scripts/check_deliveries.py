#!/usr/bin/env python3
"""배달 테이블 난이도·보상 곡선 검사기.

사용: python3 check_deliveries.py data/deliveries_v1.csv [--report out/report.md]
CSV 열: id,name,distance_m,updrafts,target_time_s,reward

플레이어 수치는 02_art_direction.md §3 과 동일하게 유지한다.
"""
from __future__ import annotations

import argparse
import csv
import math
import os
import sys

# --- 플레이어 수치 (02_art_direction.md §3) ---
CRUISE = 14.0          # m/s
GLIDE_RATIO = 6.0      # 순항 활공비
START_ALT = 40.0       # m, 섬 발사대 출발 고도 (v1 설계의 60 m는 세션이 15분을 넘겨 낮춤)
UPDRAFT_GAIN = 40.0    # m, 기류 1회 최대 상승
CLIMB_TIME = 11.0      # s, 중간 세기 기류 1회 상승

FREE_GLIDE = START_ALT * GLIDE_RATIO        # 240 m
PER_UPDRAFT = UPDRAFT_GAIN * GLIDE_RATIO    # 240 m

# --- 검사 기준 ---
MIN_SLACK = 1.15           # 목표 시간 / 최적 시간 (일반 플레이어 여유)
TUTORIAL_SLACK = 1.40      # 첫 2개 배달
TUTORIAL_COUNT = 2
MAX_STEP = 1.60            # 난이도·보상 한 단계 최대 배율 (스파이크)
MAX_REWARD_EFF_DROP = 0.15 # 난이도당 보상이 한 단계에 이만큼 넘게 떨어지면 경고
SESSION_MIN_S = 10 * 60
SESSION_BUDGET_S = 15 * 60
# 비행 외 시간: 오프닝 60 + 배달 반응 8×15 + 추락 재시작 ~10×3 + 엔딩 30
OVERHEAD_S = 240


def analyse(row: dict) -> dict:
    d = float(row["distance_m"])
    avail = int(row["updrafts"])
    target = float(row["target_time_s"])
    required = max(0, math.ceil((d - FREE_GLIDE) / PER_UPDRAFT))
    min_time = d / CRUISE + required * CLIMB_TIME
    tightness = min_time / target
    pressure = required / avail if avail else (1.0 if required else 0.0)
    # 난이도 = 실력 검사 횟수(착지 1 + 필수 기류) × 시간 압박 × 기류 여유 부족
    difficulty = (1 + required) * tightness * (1 + 0.5 * pressure)
    return {**row, "required": required, "spare": avail - required,
            "min_time": min_time, "slack": target / min_time,
            "difficulty": difficulty, "reward": float(row["reward"])}


def check(rows: list[dict]) -> list[tuple[str, str]]:
    issues = []
    for i, r in enumerate(rows):
        tag = f"#{r['id']} {r['name']}"
        if r["spare"] < 0:
            issues.append(("HIGH", f"{tag}: 기류 {r['updrafts']}개 < 필수 {r['required']}개 → 클리어 불가"))
        need = TUTORIAL_SLACK if i < TUTORIAL_COUNT else MIN_SLACK
        if r["slack"] < need:
            issues.append(("HIGH", f"{tag}: 시간 여유 {r['slack']:.2f} < {need:.2f} (최적 {r['min_time']:.0f}s, 목표 {r['target_time_s']}s)"))
        if i == 0:
            continue
        p = rows[i - 1]
        if r["difficulty"] < p["difficulty"]:
            issues.append(("MED", f"{tag}: 난이도 하락 {p['difficulty']:.2f} → {r['difficulty']:.2f}"))
        elif r["difficulty"] / p["difficulty"] > MAX_STEP:
            issues.append(("MED", f"{tag}: 난이도 스파이크 ×{r['difficulty'] / p['difficulty']:.2f}"))
        if r["reward"] <= p["reward"]:
            issues.append(("MED", f"{tag}: 보상이 오르지 않음 {p['reward']:.0f} → {r['reward']:.0f}"))
        elif r["reward"] / p["reward"] > MAX_STEP:
            issues.append(("LOW", f"{tag}: 보상 점프 ×{r['reward'] / p['reward']:.2f}"))
        eff_p = p["reward"] / p["difficulty"]
        eff_r = r["reward"] / r["difficulty"]
        if eff_r < eff_p * (1 - MAX_REWARD_EFF_DROP):
            issues.append(("MED", f"{tag}: 난이도당 보상 하락 {eff_p:.1f} → {eff_r:.1f} (어려운데 덜 줌)"))
    total = sum(float(r["target_time_s"]) for r in rows)
    if total + OVERHEAD_S > SESSION_BUDGET_S:
        issues.append(("MED", f"목표 시간 합 {total:.0f}s + 비행 외 {OVERHEAD_S}s = {total + OVERHEAD_S:.0f}s > 15분"))
    elif total + OVERHEAD_S < SESSION_MIN_S:
        issues.append(("MED", f"목표 시간 합 {total:.0f}s + 비행 외 {OVERHEAD_S}s = {total + OVERHEAD_S:.0f}s < 10분"))
    return issues


def report(rows: list[dict], issues: list[tuple[str, str]], src: str) -> str:
    out = [f"# 배달 테이블 검사: `{src}`", "",
           f"모델: 순항 {CRUISE} m/s, 활공비 {GLIDE_RATIO}:1, 출발 고도 {START_ALT} m → 무기류 {FREE_GLIDE:.0f} m, "
           f"기류 1회 +{PER_UPDRAFT:.0f} m / {CLIMB_TIME:.0f} s", "",
           "| # | 이름 | 거리 | 기류(필수/여분) | 최적s | 목표s | 여유 | 난이도 | 보상 | 보상/난이도 |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['id']} | {r['name']} | {r['distance_m']} | {r['updrafts']} ({r['required']}/{r['spare']}) | "
                   f"{r['min_time']:.0f} | {r['target_time_s']} | {r['slack']:.2f} | {r['difficulty']:.2f} | "
                   f"{r['reward']:.0f} | {r['reward'] / r['difficulty']:.1f} |")
    total = sum(float(r["target_time_s"]) for r in rows)
    out += ["", f"목표 시간 합: {total:.0f}s + 비행 외 {OVERHEAD_S}s = 세션 {(total + OVERHEAD_S) / 60:.1f}분", "",
            "## 난이도 막대", "```"]
    top = max(r["difficulty"] for r in rows)
    for r in rows:
        out.append(f"{r['id']} {'█' * round(30 * r['difficulty'] / top):<30} {r['difficulty']:.2f}")
    out += ["```", "", f"## 문제 ({len(issues)}건)"]
    out += [f"- **{s}** {m}" for s, m in issues] or ["- 없음 ✅"]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--report")
    a = ap.parse_args()
    with open(a.csv, encoding="utf-8") as f:
        rows = [analyse(r) for r in csv.DictReader(f)]
    issues = check(rows)
    text = report(rows, issues, a.csv)
    if a.report:
        os.makedirs(os.path.dirname(a.report) or ".", exist_ok=True)
        with open(a.report, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)
    return 1 if any(s in ("HIGH", "MED") for s, _ in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
