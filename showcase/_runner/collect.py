#!/usr/bin/env python3
"""Copy session outputs into the repo's showcase/ folder.

Skips session plumbing (installed skills, caches, raw logs), strips local absolute paths
from text files, and writes a session.md summary (agent, model, duration, cost if known).
"""
import json
import os
import re
import shutil
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(os.path.dirname(ROOT), "ai-game-designer", "showcase")
SKIP_DIRS = {".agents", ".mpl", ".git", "__pycache__", ".venv", ".claude", ".codex", "scratch"}
SKIP_FILES = {"session.json", "session.err", "session.log", "session-meta.txt", ".DS_Store"}
TEXT_EXT = {".md", ".csv", ".json", ".txt", ".py", ".yaml", ".yml", ".toml"}
SESSION = re.compile(r"(file://)?(/private)?/(Users|tmp|var/folders)/[^\s)\"'`]*?showcase-runs/\d\d-[^/\s)\"'`]+/")
LOCAL = re.compile(r"(file://)?(/private)?/(Users|tmp|var/folders)/[^\s)\"'`]*?(showcase-runs|ai-game-designer)/")


def meta(d):
    m = {}
    path = os.path.join(d, "session-meta.txt")
    if os.path.exists(path):
        for line in open(path):
            k, _, v = line.strip().partition(": ")
            m[k] = v  # last value wins (retries overwrite)
    sj = os.path.join(d, "session.json")
    if os.path.exists(sj):
        try:
            data = json.load(open(sj))
            m["cost_usd"] = round(data.get("total_cost_usd", 0), 2)
            m["turns"] = data.get("num_turns")
            models = list((data.get("modelUsage") or {}).keys())
            m["model"] = ", ".join(models) if models else data.get("model", "")
        except (json.JSONDecodeError, OSError):
            pass
    log = os.path.join(d, "session.log")
    if os.path.exists(log):
        text = open(log, errors="ignore").read()
        mm = re.search(r"^model: (.+)$", text, re.M)
        if mm:
            m["model"] = mm.group(1).strip()
        tk = re.findall(r"tokens used\s*\n\s*([\d,]+)", text)
        if tk:
            m["tokens"] = tk[-1]
    if m.get("start") and m.get("end"):
        fmt = "%Y-%m-%dT%H:%M:%SZ"
        secs = (datetime.strptime(m["end"], fmt) - datetime.strptime(m["start"], fmt)).total_seconds()
        m["duration_min"] = round(secs / 60, 1)
    return m


def main():
    os.makedirs(DEST, exist_ok=True)
    only = set(sys.argv[1:])  # optional: collect only these session folders
    for name in sorted(os.listdir(ROOT)):
        src = os.path.join(ROOT, name)
        if not (os.path.isdir(src) and name[:2].isdigit()) or (only and name not in only):
            continue
        dst = os.path.join(DEST, name)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        for base, dirs, files in os.walk(src):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            for f in files:
                if f in SKIP_FILES:
                    continue
                s = os.path.join(base, f)
                t = os.path.join(dst, os.path.relpath(s, src))
                os.makedirs(os.path.dirname(t), exist_ok=True)
                if os.path.splitext(f)[1].lower() in TEXT_EXT:
                    text = open(s, encoding="utf-8", errors="ignore").read()
                    open(t, "w", encoding="utf-8").write(LOCAL.sub("", SESSION.sub("", text)))
                else:
                    shutil.copy2(s, t)
        m = meta(src)
        with open(os.path.join(dst, "session.md"), "w", encoding="utf-8") as fh:
            fh.write(f"# Session: {name}\n\n")
            for k in ("agent", "model", "duration_min", "turns", "cost_usd", "tokens", "exit"):
                if m.get(k) not in (None, ""):
                    fh.write(f"- **{k}**: {m[k]}\n")
            fh.write("\nThe prompt is in `PROMPT.md`. Every other file was written by the agent during the session.\n")
        print(f"{name}: {m}")


if __name__ == "__main__":
    main()
