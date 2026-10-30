# 星尘矿场：手机放置采矿设计包

本文件夹保存了可运行的进度曲线（Progression Curve）、章节转生（Prestige）模型与概念设计评审（Design Review）。所有数值是原型假设，没有玩家实测背书。

## 主要结论

- 矿机从1级开始，升级成本 `200 × 1.18^(L−1)`，产出 `10 × 1.12^(L−1) × 永久倍率`/秒，首次升级20秒。
- 五章目标等级40/55/70/85/100，倍率1/2/4/8/16倍。本章生产时间约41/49/55/62/68分钟，总计275.12分钟（4.59小时），章末单次升级等待2.42–3.47分钟。
- 每8小时登录5分钟的样例中，第40小时看到结局。生产时间、在线时间、日历时间必须分开；离线也自动升级，转生由玩家确认。
- 同样到100级，无转生需要1084.41分钟，末次等待55.46分钟。提高成本增长率到1.20会使五章总生产时间增至754.57分钟，应避免随意微调指数参数。
- 最大设计风险是“自动看进度条”。先测试可见建设、调查选择和迁移理解，再做更多矿机与内容。五章只是短篇验证范围。
- 暗黑模式（Dark Pattern）评审未发现有依据的当前P0问题；重复复建、损失压力、限时内容和通知存在设计风险。建议无强制广告、无付费随机奖励、无断签惩罚，提供明确结局与永久可达内容。

## 文件清单

|文件|用途|
|---|---|
|[docs/economy-design.md](docs/economy-design.md)|目标、公式、阶段体感、转生规则、离线和日历假设、调整对照与验证计划|
|[docs/design-review.md](docs/design-review.md)|3个优势、7项分级问题、完整暗黑模式检查、问题清单、原型实验与研究来源|
|[scripts/progression_curve.py](scripts/progression_curve.py)|从 balance-economy 技能复制的通用进度曲线脚本；保留原始英文输出|
|[scripts/model.py](scripts/model.py)|项目模型：五章转生、升级明细、日历样例、参数敏感性与一致性检查|
|[results/mining.csv](results/mining.csv)|通用脚本的1→101级无转生对照；经验值栏在本项目解释为信用点成本|
|[results/mining_report.md](results/mining_report.md)|通用脚本原始报告，含指数等待警告；不是最终转生方案|
|[results/upgrade_details.csv](results/upgrade_details.csv)|精确到秒的1→101级成本、产出、等待与累计时间；前99行对应到100级|
|[results/prestige.csv](results/prestige.csv)|五章奖励、倍率、生产时间、末级等待及登录确认时点|
|[results/sensitivity.csv](results/sensitivity.csv)|成本增长1.18/1.20与产出80%/100%/120%的六组重算|
|[results/progression.svg](results/progression.svg)|五章等级随生产时间变化图；下降表示主动迁移重置|
|[results/model_run.txt](results/model_run.txt)|模型运行记录，含一致性检查与六组敏感性结果|
|README.md|本索引与主要结论|

`PROMPT.md`、`session-meta.txt`、`session.log` 和隐藏配置目录为已有输入或运行记录，不属于设计成果，也未改写。

## 复现

仅需 Python 3 标准库，无需联网或安装依赖。在本文件夹运行：

```bash
python3 scripts/progression_curve.py --curve exp --levels 101 --first 200 --growth 1.18 --xp-per-hour 36000 --income-growth 1.12 --name mining --out results --no-plot
python3 scripts/model.py
```

第二条输出 `Checks passed.`，并重建项目数据与独立矢量图（SVG）。修改参数后应同时更新中文说明和README，避免文档与结果不一致。通用报告按分钟取整，开局的“0 min”实际是20秒。

![五章进度图](results/progression.svg)
