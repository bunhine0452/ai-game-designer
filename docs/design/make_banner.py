#!/usr/bin/env python3
"""Render the ai-game-designer banner ("Measured Wonder, plate 2: From Curve to Play").

  python3 docs/design/make_banner.py

Renders docs/design/banner.html (2560x1280) in headless Chrome, Chromium or Edge, then writes
docs/images/banner.png (2000x1000, README) and docs/images/social-preview.png (1280x640, GitHub
social preview, kept under 1 MB). The page loads Instrument Serif, Instrument Sans and Geist Mono
(SIL Open Font License) from Google Fonts and the eight game screenshots from games/screenshots/.
Needs Pillow for the resize. See banner-philosophy.md for the design rules.

Hidden in plain sight: the gold line is an interest curve (hook, rising peaks, climax, a short
resolution) that runs out of the type and across the games the skills produced; the faint traces
around it are its spread across players.
"""
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "plugins", "game-designer", "skills", "playable-prototype", "scripts"))
from check import find_browser  # noqa: E402  (same browser lookup as the prototype checker)


def main() -> int:
    try:
        from PIL import Image
    except ImportError:
        sys.exit("error: needs Pillow (pip install pillow)")
    browser = find_browser()
    if not browser:
        sys.exit("error: no Chrome, Chromium or Edge found")
    page = "file://" + os.path.join(ROOT, "docs", "design", "banner.html")
    tmp = tempfile.mkdtemp()
    raw = os.path.join(tmp, "banner-raw.png")
    try:
        subprocess.run([browser, "--headless=new", "--hide-scrollbars", "--no-first-run", f"--user-data-dir={tmp}",
                        "--window-size=2560,1280", "--force-device-scale-factor=1", "--virtual-time-budget=8000",
                        "--allow-file-access-from-files", f"--screenshot={raw}", page],
                       capture_output=True, timeout=180, check=False)
        if not os.path.exists(raw):
            sys.exit("error: the browser did not write a screenshot")
        im = Image.open(raw).convert("RGB")
        out = os.path.join(ROOT, "docs", "images")
        im.resize((2000, 1000), Image.LANCZOS).save(os.path.join(out, "banner.png"), optimize=True)
        social = os.path.join(out, "social-preview.png")
        im.resize((1280, 640), Image.LANCZOS).save(social, optimize=True)
        if os.path.getsize(social) > 1_000_000:   # GitHub's social preview limit is 1 MB
            im.resize((1280, 640), Image.LANCZOS).quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(social, optimize=True)
        for name in ("banner.png", "social-preview.png"):
            p = os.path.join(out, name)
            print(f"wrote {os.path.relpath(p, ROOT)} ({os.path.getsize(p) // 1024} KB)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
