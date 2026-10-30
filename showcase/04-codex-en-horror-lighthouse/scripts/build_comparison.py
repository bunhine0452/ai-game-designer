"""Build dependency-free SVG and summary from the actual analyzer outputs."""
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
before=json.loads((ROOT/'analysis/beats_before_report.json').read_text())
after=json.loads((ROOT/'analysis/beats_after_report.json').read_text())
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="500" viewBox="0 0 1100 500" role="img" aria-labelledby="title desc">','<title id="title">Low Tide: before and after pacing</title>','<desc id="desc">Original peaks at minute 12 then plateaus. Revision alternates rising threats with relief and peaks at minute 38. Predicted intensity, not playtest measurements.</desc>','<rect width="1100" height="500" fill="white"/>','<g font-family="sans-serif" fill="#182332">','<text x="75" y="30" font-size="23">Low Tide — predicted chapter tension</text>']
for v in range(11):
 y=400-v*32
 parts.extend([f'<path d="M75 {y} H1035" stroke="#dce1e6"/>',f'<text x="48" y="{y+5}" font-size="14">{v}</text>'])
for t in range(0,41,5):
 x=75+t*24
 parts.extend([f'<text x="{x-8}" y="425" font-size="14">{t}</text>'])
for data,color,dash in [(before,'#9a4d00','8 5'),(after,'#005b9a','')]:
 pts=' '.join(f"{75+b['time']*24},{400-b['intensity']*32}" for b in data['beats'])
 parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-dasharray="{dash}"/>')
 for b in data['beats']:
  parts.append(f'<circle cx="{75+b["time"]*24}" cy="{400-b["intensity"]*32}" r="3" fill="{color}"/>')
parts.extend(['<text x="75" y="61" font-size="14">Intensity (0–10)</text>','<text x="485" y="452" font-size="15">Chapter time (minutes)</text>','<text x="75" y="480" fill="#9a4d00" font-size="15">Dashed: original draft</text>','<text x="330" y="480" fill="#005b9a" font-size="15">Solid: revised draft</text>','</g></svg>'])
(ROOT/'analysis/comparison.svg').write_text('\n'.join(parts))
metrics=[('Duration (min)','duration'),('Beat samples','beats'),('Mean predicted intensity / 10','mean_intensity'),('Climax time (min)','climax_time'),('Climax position (fraction)','climax_position'),('Time at intensity ≥8 (fraction)','share_high'),('Time at intensity ≤3 (fraction)','share_low'),('Pacing health / 100 (heuristic)','pacing_score')]
lines=['# Before and after metrics','','| Metric | Original | Revised |','|---|---:|---:|']
for label,key in metrics: lines.append(f"| {label} | {before['metrics'][key]} | {after['metrics'][key]} |")
lines.extend([f"| Findings | {len(before['findings'])} | {len(after['findings'])} |",'', '![Before and after curves](comparison.svg)','','Scores summarize rule violations; they do not measure fear, quality, accessibility, or enjoyment. Shares are computed from evenly resampled, linearly interpolated predictions. See the reports for beat tables and text charts.'])
(ROOT/'analysis/comparison.md').write_text('\n'.join(lines)+'\n')
