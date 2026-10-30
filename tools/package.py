#!/usr/bin/env python3
"""Build release artifacts into dist/.

  dist/game-designer.plugin   zip of the plugin folder plugins/game-designer/ (manifests, skills, research)
  dist/skills/<skill>.zip     one self-contained zip per skill for the Claude app; each
                              includes the shared glossary at references/glossary.md

Usage: python3 tools/package.py
"""
from __future__ import annotations

import json
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
PLUGIN = os.path.join(ROOT, "plugins", "game-designer")
GLOSSARY = os.path.join(PLUGIN, "skills", "game-design", "references", "glossary.md")
SKIP_DIRS = {"__pycache__", ".git", "dist", "results"}
SKIP_FILES = {".DS_Store"}


def walk(path: str):
    for base, dirs, files in os.walk(path):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name not in SKIP_FILES and not name.endswith(".pyc"):
                yield os.path.join(base, name)


def build_plugin() -> str:
    name = json.load(open(os.path.join(PLUGIN, ".claude-plugin", "plugin.json")))["name"]
    out = os.path.join(DIST, f"{name}.plugin")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in walk(PLUGIN):
            zf.write(f, os.path.relpath(f, PLUGIN))
    return out


def build_skill_zips() -> list[str]:
    outs = []
    os.makedirs(os.path.join(DIST, "skills"), exist_ok=True)
    skills_dir = os.path.join(PLUGIN, "skills")
    for skill in sorted(os.listdir(skills_dir)):
        src = os.path.join(skills_dir, skill)
        if not os.path.isfile(os.path.join(src, "SKILL.md")):
            continue
        out = os.path.join(DIST, "skills", f"{skill}.zip")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in walk(src):
                zf.write(f, os.path.join(skill, os.path.relpath(f, src)))
            if skill != "game-design":
                zf.write(GLOSSARY, os.path.join(skill, "references", "glossary.md"))
        outs.append(out)
    return outs


def main() -> int:
    os.makedirs(DIST, exist_ok=True)
    plugin = build_plugin()
    zips = build_skill_zips()
    for p in [plugin] + zips:
        print(f"{os.path.relpath(p, ROOT):40} {os.path.getsize(p) / 1024:8.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
