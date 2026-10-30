# Game Design Charts

An optional companion to the **game-designer** plugin: a small MCP server with two tools that
return exact numbers as text and, in hosts that support **MCP Apps** (such as the Claude desktop
app), an interactive chart in the conversation.

| Tool | What it does | Chart |
|---|---|---|
| `interest_curve` | Diagnoses a session's pacing from beats (time, intensity 0–10, label): late hook, early peak, long lulls, flat stretches, missing rhythm or resolution | Drag points to try changes, see the diagnosis update, and send the edited curve back to the chat |
| `gacha_odds` | The exact distribution of pulls needed for a featured unit, given the rate, the featured share (50/50), a guarantee after a lost 50/50, hard pity and spark, plus the chance within a pull budget | Sliders for every rule, a cumulative chance curve, mean, median, 90th and 99th percentiles, and the worst case |

Try: "Use gacha_odds: 3% top rate, 50/50 with guarantee, spark at 120, budget 60 pulls."

## Install

- **Claude Code:** `/plugin marketplace add bunhine0452/ai-game-designer`, then
  `/plugin install game-design-charts@ai-game-designer`. Claude Code shows the text results.
  It doesn't render MCP Apps.
- **Claude desktop app** (renders the charts): add the server to `claude_desktop_config.json`
  (Settings → Developer → Edit Config) with the absolute path to your clone:

```json
{ "mcpServers": { "game-design-charts": { "command": "python3", "args": ["/path/to/ai-game-designer/plugins/game-design-charts/server/server.py"] } } }
```

## What it runs, sends, and fetches

`server/server.py` is a Python 3 standard-library program that speaks MCP over stdio. It
computes results in memory, reads only its own `server/views/*.html` files, writes no files,
and makes **no network requests**. The chart views are self-contained HTML with inline scripts
and no external resources. No telemetry, no data collection.

License: MIT · Support: https://github.com/bunhine0452/ai-game-designer/issues
