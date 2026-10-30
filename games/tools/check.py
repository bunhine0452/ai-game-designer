#!/usr/bin/env python3
"""Run every game's self-test and capture screenshots with headless Chrome.

  python3 games/tools/check.py              # all games: self-test + screenshot
  python3 games/tools/check.py stardust-mine --no-shot

Each game supports ?test=1 (runs its logic tests and writes JSON into <pre id="selftest">)
and ?shot=1 (sets up a representative, deterministic state for the screenshot).
Chrome runs with a throwaway profile so it never touches your own browser data.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

GAMES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(GAMES, "screenshots")
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def chrome(args, budget_ms):
    with tempfile.TemporaryDirectory() as profile:
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
               "--no-default-browser-check", f"--user-data-dir={profile}", "--window-size=1280,860",
               f"--virtual-time-budget={budget_ms}", "--allow-file-access-from-files"] + args
        return subprocess.run(cmd, capture_output=True, text=True, timeout=120)


def main():
    names = [a for a in sys.argv[1:] if not a.startswith("--")]
    shoot = "--no-shot" not in sys.argv
    games = names or sorted(d for d in os.listdir(GAMES)
                            if os.path.isfile(os.path.join(GAMES, d, "index.html")) and d != "tools")
    os.makedirs(SHOTS, exist_ok=True)
    failed = False
    for name in games:
        url = "file://" + os.path.join(GAMES, name, "index.html")
        res = chrome(["--dump-dom", url + "?test=1"], 6000)
        m = re.search(r'<pre id="selftest"[^>]*>(.*?)</pre>', res.stdout, re.S)
        if not m or not m.group(1).strip():
            print(f"[FAIL] {name}: no self-test output\n{res.stderr[-800:]}")
            failed = True
            continue
        data = json.loads(m.group(1).replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&"))
        bad = [r for r in data["results"] if not r["pass"]]
        print(f"[{'PASS' if data['pass'] else 'FAIL'}] {name}: {len(data['results']) - len(bad)}/{len(data['results'])} checks")
        for r in bad:
            print(f"    ✗ {r['name']} {r.get('info', '')}")
        failed |= not data["pass"]
        if shoot:
            path = os.path.join(SHOTS, f"{name}.png")
            chrome([f"--screenshot={path}", url + "?shot=1"], 5000)
            print(f"       screenshot: {os.path.relpath(path, GAMES)} ({os.path.getsize(path) // 1024} KB)"
                  if os.path.exists(path) else "       screenshot FAILED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
