"""Deterministic mining model; Python 3 standard library only. Run from any cwd."""
from pathlib import Path
import csv, math
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)

def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

def run(growth=1.18, income_factor=1.0):
    rows=[]; bank=0; total=0; calendar=0
    for chapter, target in enumerate([40,55,70,85,100],1):
        multiplier=1+bank; seconds=0
        for level in range(1,target):
            cost=200*growth**(level-1)
            income=10*1.12**(level-1)*multiplier*income_factor
            seconds+=cost/income
        # 5-minute sessions starting every 8 hours; automatic upgrades work offline.
        ready=calendar+seconds
        slot=math.floor(ready/(8*3600))
        claim=ready if ready-slot*8*3600<=300 else (slot+1)*8*3600
        reward=2**(chapter-1) if chapter<5 else 0
        total+=seconds
        rows.append(dict(chapter=chapter,target_level=target,multiplier=multiplier,
                         reward=reward,run_minutes=round(seconds/60,3),
                         cumulative_minutes=round(total/60,3),
                         last_upgrade_minutes=round(20*(growth/1.12)**(target-2)/multiplier/income_factor/60,3),
                         ready_calendar_hours=round(ready/3600,3),
                         claim_calendar_hours=round(claim/3600,3)))
        bank+=reward; calendar=claim
    return rows

rows=run(); write('prestige.csv',rows)
levels=[]; elapsed=0
for level in range(1,101):
    cost=200*1.18**(level-1); income=10*1.12**(level-1); wait=cost/income; elapsed+=wait
    levels.append(dict(from_level=level,to_level=level+1,cost=round(cost,6),
                       income_per_second=round(income,6),wait_seconds=round(wait,6),
                       cumulative_minutes=round(elapsed/60,6)))
write('upgrade_details.csv',levels)
sensitivity=[]
for growth in [1.18,1.20]:
    for speed in [.8,1,1.2]:
        r=run(growth,speed)
        sensitivity.append(dict(cost_growth=growth,income_factor=speed,
                               first_run_minutes=r[0]['run_minutes'],
                               total_minutes=r[-1]['cumulative_minutes'],
                               final_claim_hours=r[-1]['claim_calendar_hours']))
write('sensitivity.csv',sensitivity)
# Meaningful invariants: indexing, resets, one-time rewards, time/cost integration.
assert levels[0]['cost']==200 and levels[0]['wait_seconds']==20
assert [r['multiplier'] for r in rows]==[1,2,4,8,16]
assert [r['reward'] for r in rows]==[1,2,4,8,0]
assert all(r['claim_calendar_hours']>=r['ready_calendar_hours'] for r in rows)
assert math.isclose(sum(20*(1.18/1.12)**i for i in range(39))/60,rows[0]['run_minutes'],abs_tol=.001)
# Standalone SVG; no plotting dependencies.
points=[]; t=0
for r in rows:
    m=r['multiplier']
    for l in range(1,r['target_level']):
        points.append((t,l)); t+=20*(1.18/1.12)**(l-1)/m/60
    points.append((t,r['target_level']))
xmax=t
coords=' '.join(f'{60+x/xmax*800:.2f},{350-y/100*290:.2f}' for x,y in points)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="940" height="430" viewBox="0 0 940 430"><rect width="940" height="430" fill="#101827"/><g fill="#e5edf7" font-family="sans-serif"><text x="60" y="30" font-size="20">Stardust Mine: five chapters, ideal auto-upgrade time</text><text x="60" y="385">0 min</text><text x="780" y="385">{xmax:.1f} min</text><text x="15" y="60">100</text><text x="25" y="350">1</text><text x="60" y="412">X: productive minutes | Y: miner level | drops: voluntary prestige</text></g><path d="M60 50V355H880" stroke="#8b9cb1" fill="none"/><polyline points="{coords}" stroke="#53dfbc" fill="none" stroke-width="2.5"/></svg>'''
(OUT/'progression.svg').write_text(svg)
print('Checks passed.'); print(*rows,sep='\n'); print('Sensitivity:',sensitivity)
