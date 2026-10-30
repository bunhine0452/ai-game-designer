#!/bin/bash
# Run six real design sessions in parallel, each in its own fresh project folder.
ROOT="$(cd "$(dirname "$0")" && pwd)"
REPO="$ROOT/../ai-game-designer"
export PATH="$ROOT/.venv/bin:$PATH"   # python3 with matplotlib for the skill scripts

meta() { printf '%s\n' "$@" >> session-meta.txt; }

run_claude() {
  cd "$ROOT/$1" || return
  meta "agent: claude-code" "start: $(date -u +%FT%TZ)"
  MPLCONFIGDIR="$PWD/.mpl" claude -p "$(cat PROMPT.md)" \
    --plugin-dir "$REPO" --add-dir "$REPO" --permission-mode acceptEdits \
    --allowedTools "Bash(python3:*)" "Bash(python:*)" "Bash(ls:*)" "Bash(mkdir:*)" "Bash(head:*)" \
                   "Bash(cat:*)" Write Edit Read Glob Grep Skill \
    --max-budget-usd 5 --output-format json < /dev/null > session.json 2> session.err
  meta "exit: $?" "end: $(date -u +%FT%TZ)"
}

run_codex() {
  cd "$ROOT/$1" || return
  meta "agent: codex-cli" "start: $(date -u +%FT%TZ)"
  MPLCONFIGDIR="$PWD/.mpl" codex exec --skip-git-repo-check --approve-for-me \
    -C "$PWD" -o last-message.md "$(cat PROMPT.md)" < /dev/null > session.log 2>&1
  meta "exit: $?" "end: $(date -u +%FT%TZ)"
}

run_agy() {
  cd "$ROOT/$1" || return
  meta "agent: antigravity-cli" "start: $(date -u +%FT%TZ)"
  # Session-only allow list (never saved): the skill scripts plus read-only helpers.
  local allow='{"permissions":{"allow":["command(python3)","command(python)","command(ls)","command(mkdir)","command(cat)","command(head)","command(tail)","command(cd)","command(cp)","command(mv)","command(echo)","command(grep)","command(find)","command(wc)","command(sort)","command(touch)"]}}'
  MPLCONFIGDIR="$PWD/.mpl" agy -p "$(cat PROMPT.md)" --sandbox --mode accept-edits --settings "$allow" \
    --output-format stream-json --print-timeout 30m < /dev/null > session.log 2>&1
  meta "exit: $?" "end: $(date -u +%FT%TZ)"
}

run_claude 01-claude-ko-monster-farm &
run_claude 02-claude-en-deckbuilder &
run_claude 03-claude-ja-gacha-review &
run_codex  04-codex-en-horror-lighthouse &
run_agy    05-agy-es-garden-td &
run_codex  06-codex-zh-idle-mining &
wait
for d in "$ROOT"/0*/; do echo "== $(basename "$d")"; cat "$d/session-meta.txt"; done
