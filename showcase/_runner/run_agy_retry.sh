#!/bin/bash
# Relaunch the Antigravity session with a session-only command allow list.
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PATH="$ROOT/.venv/bin:$PATH"
eval "$(sed -n '/^meta()/,/^}/p; /^run_agy()/,/^}/p' "$ROOT/run_all.sh")"
run_agy 05-agy-es-garden-td
cat "$ROOT/05-agy-es-garden-td/session-meta.txt"
