#!/usr/bin/env python3
"""Run browser prototypes' self-tests and capture screenshots with headless Chrome.

  python3 check.py games/                     # every <game>/index.html under games/
  python3 check.py my-game/index.html --no-shot
  python3 check.py games/ --shots out/shots   # choose the screenshot folder

Contract (see ../references/testing-and-bots.md):
  ?test=1  the page writes {"game","pass","results":[...]} JSON into <pre id="selftest">
  ?shot=1  the page builds a deterministic, representative state for the screenshot

Chrome/Chromium/Edge is found automatically, or set CHROME=/path/to/browser. Each run uses a
throwaway profile, so it never touches your own browser data. Standard library only.
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "msedge", "chrome"):
        if shutil.which(name):
            return shutil.which(name)
    return next((p for p in CANDIDATES if os.path.exists(p)), None)


def run(browser, args, budget_ms, size="1280,720"):
    with tempfile.TemporaryDirectory() as profile:
        # SwiftShader flags let WebGL (3D prototypes) render in headless mode without a GPU.
        cmd = [browser, "--headless=new", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--hide-scrollbars", "--no-first-run",
               "--no-default-browser-check", f"--user-data-dir={profile}", f"--window-size={size}",
               f"--virtual-time-budget={budget_ms}", "--allow-file-access-from-files"] + args
        return subprocess.run(cmd, capture_output=True, text=True, timeout=180)


def collect(paths):
    """Return (name, html_path, default_shot_dir) for each prototype found."""
    found = []
    for p in paths:
        p = os.path.abspath(p)
        if os.path.isfile(p):
            folder = os.path.dirname(p)
            found.append((os.path.basename(folder) if os.path.basename(p) == "index.html" else os.path.splitext(os.path.basename(p))[0],
                          p, os.path.join(os.path.dirname(folder), "screenshots")))
        elif os.path.isfile(os.path.join(p, "index.html")) and not any(
                os.path.isfile(os.path.join(p, d, "index.html")) for d in os.listdir(p)):
            found.append((os.path.basename(p), os.path.join(p, "index.html"), os.path.join(os.path.dirname(p), "screenshots")))
        else:
            for d in sorted(os.listdir(p)):
                f = os.path.join(p, d, "index.html")
                if os.path.isfile(f):
                    found.append((d, f, os.path.join(p, "screenshots")))
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="prototype folders or HTML files")
    ap.add_argument("--shots", help="screenshot folder (default: <parent>/screenshots)")
    ap.add_argument("--no-shot", action="store_true", help="only run self-tests")
    ap.add_argument("--budget", type=int, default=8000, help="virtual time budget for tests (ms)")
    ap.add_argument("--size", default="1280,720", help="screenshot window size, WIDTH,HEIGHT (default 1280,720: a 16:9 stage)")
    a = ap.parse_args()
    browser = find_browser()
    if not browser:
        print("error: no Chrome/Chromium/Edge found; set CHROME=/path/to/browser", file=sys.stderr)
        return 2
    games = collect(a.paths)
    if not games:
        print("error: no index.html prototypes found", file=sys.stderr)
        return 2
    failed = False
    for name, page, shot_dir in games:
        url = "file://" + page
        res = run(browser, ["--dump-dom", url + "?test=1"], a.budget)
        m = re.search(r'<pre id="selftest"[^>]*>(.*?)</pre>', res.stdout, re.S)
        if not m or not m.group(1).strip():
            print(f"[FAIL] {name}: no self-test output (does the page implement ?test=1?)\n{res.stderr[-600:]}")
            failed = True
            continue
        data = json.loads(html.unescape(m.group(1)))
        bad = [r for r in data["results"] if not r["pass"]]
        print(f"[{'PASS' if data['pass'] else 'FAIL'}] {name}: {len(data['results']) - len(bad)}/{len(data['results'])} checks")
        for r in data["results"]:
            if not r["pass"] or r.get("info"):
                print(f"    {'✗' if not r['pass'] else '·'} {r['name']}{': ' + str(r['info']) if r.get('info') else ''}")
        failed |= not data["pass"]
        if not a.no_shot:
            out = os.path.abspath(a.shots) if a.shots else shot_dir
            os.makedirs(out, exist_ok=True)
            path = os.path.join(out, f"{name}.png")
            run(browser, [f"--screenshot={path}", url + "?shot=1"], 5000, a.size)
            print(f"    screenshot: {path} ({os.path.getsize(path) // 1024} KB)" if os.path.exists(path) else "    screenshot FAILED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
