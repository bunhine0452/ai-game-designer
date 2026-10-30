#!/bin/bash
# Relaunch only the two Codex sessions (first launch failed on a flag conflict).
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PATH="$ROOT/.venv/bin:$PATH"
eval "$(sed -n '/^meta()/,/^}/p; /^run_codex()/,/^}/p' "$ROOT/run_all.sh")"
run_codex 04-codex-en-horror-lighthouse &
run_codex 06-codex-zh-idle-mining &
wait
