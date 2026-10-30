#!/bin/bash
# Showcase sessions 07 (3D) and 08 (pixel): real Claude Code runs with the plugin loaded.
ROOT="$(cd "$(dirname "$0")" && pwd)"
REPO="$ROOT/../ai-game-designer"
export PATH="$ROOT/.venv/bin:$PATH"
meta() { printf '%s\n' "$@" >> session-meta.txt; }
run_claude() {
  cd "$ROOT/$1" || return
  meta "agent: claude-code" "start: $(date -u +%FT%TZ)"
  MPLCONFIGDIR="$PWD/.mpl" claude -p "$(cat PROMPT.md)" \
    --plugin-dir "$REPO/plugins/game-designer" --add-dir "$REPO" --permission-mode acceptEdits \
    --allowedTools "Bash(python3:*)" "Bash(python:*)" "Bash(ls:*)" "Bash(mkdir:*)" "Bash(head:*)" \
                   "Bash(cat:*)" Write Edit Read Glob Grep Skill \
    --model opus --max-budget-usd 6 --output-format json < /dev/null > session.json 2> session.err
  meta "exit: $?" "end: $(date -u +%FT%TZ)"
}
run_claude 07-claude-ko-3d-kite-post &
run_claude 08-claude-ja-pixel-garden &
wait
