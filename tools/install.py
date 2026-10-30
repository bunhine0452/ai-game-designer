#!/usr/bin/env python3
"""Install the game design skills into any agent that reads Agent Skills (SKILL.md folders).

Examples:
  python3 tools/install.py                          # universal: ./.agents/skills (Codex, Gemini CLI, ...)
  python3 tools/install.py --agent claude --scope user
  python3 tools/install.py --agent all --scope project --project-dir ~/my-game
  python3 tools/install.py --dest ~/somewhere/skills --link
  python3 tools/install.py --agent cursor --uninstall

Each copied skill gets the shared glossary at references/glossary.md, so skills work even
when installed one at a time. --link symlinks instead (handy while editing this repo).
Paths marked "reported" come from community documentation; use --dest if your agent differs.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
GLOSSARY = os.path.join(SKILLS, "game-design", "references", "glossary.md")

# agent: (project dir, user dir, note)
AGENTS = {
    "universal": (".agents/skills", "~/.agents/skills", "shared path read by Codex, Gemini CLI and others"),
    "claude": (".claude/skills", "~/.claude/skills", "Claude Code"),
    "codex": (".agents/skills", "~/.codex/skills", "OpenAI Codex CLI"),
    "gemini": (".gemini/skills", "~/.gemini/skills", "Gemini CLI"),
    "cursor": (".cursor/skills", "~/.cursor/skills", "Cursor (reported)"),
    "copilot": (".github/skills", "~/.copilot/skills", "GitHub Copilot (reported)"),
    "opencode": (".opencode/skills", "~/.config/opencode/skills", "OpenCode (reported)"),
}
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def skill_names() -> list[str]:
    return sorted(d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md")))


def targets(args) -> list[tuple[str, str]]:
    if args.dest:
        return [("custom", os.path.expanduser(args.dest))]
    names = list(AGENTS) if args.agent == "all" else [args.agent]
    out, seen = [], set()
    for name in names:
        project, user, _ = AGENTS[name]
        path = os.path.expanduser(user) if args.scope == "user" else os.path.join(args.project_dir, project)
        path = os.path.abspath(path)
        if path not in seen:
            seen.add(path)
            out.append((name, path))
    return out


def install_one(skill: str, dest_root: str, link: bool, dry: bool) -> str:
    src, dst = os.path.join(SKILLS, skill), os.path.join(dest_root, skill)
    if dry:
        return f"would {'link' if link else 'copy'} {skill} -> {dst}"
    os.makedirs(dest_root, exist_ok=True)
    if os.path.islink(dst) or os.path.isfile(dst):
        os.remove(dst)
    elif os.path.isdir(dst):
        shutil.rmtree(dst)
    if link:
        os.symlink(src, dst)
    else:
        shutil.copytree(src, dst, ignore=IGNORE)
        if skill != "game-design":
            shutil.copy2(GLOSSARY, os.path.join(dst, "references", "glossary.md"))
    return f"{'linked' if link else 'installed'} {skill} -> {dst}"


def uninstall_one(skill: str, dest_root: str, dry: bool) -> str | None:
    dst = os.path.join(dest_root, skill)
    if not (os.path.lexists(dst)):
        return None
    if not dry:
        if os.path.islink(dst) or os.path.isfile(dst):
            os.remove(dst)
        else:
            shutil.rmtree(dst)
    return f"{'would remove' if dry else 'removed'} {dst}"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agent", default="universal", choices=list(AGENTS) + ["all"])
    ap.add_argument("--scope", default="project", choices=["project", "user"])
    ap.add_argument("--project-dir", default=os.getcwd(), help="project root for --scope project")
    ap.add_argument("--dest", help="install into this skills directory instead")
    ap.add_argument("--skills", help="comma-separated subset (default: all six)")
    ap.add_argument("--link", action="store_true", help="symlink instead of copying")
    ap.add_argument("--uninstall", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list-agents", action="store_true")
    args = ap.parse_args(argv)

    if args.list_agents:
        for name, (project, user, note) in AGENTS.items():
            print(f"{name:10} project: {project:20} user: {user:28} {note}")
        return 0
    available = skill_names()
    chosen = available if not args.skills else [s.strip() for s in args.skills.split(",")]
    unknown = sorted(set(chosen) - set(available))
    if unknown:
        print(f"error: unknown skill(s): {', '.join(unknown)}; available: {', '.join(available)}", file=sys.stderr)
        return 2
    for agent, dest in targets(args):
        print(f"[{agent}] {dest}")
        for skill in chosen:
            msg = uninstall_one(skill, dest, args.dry_run) if args.uninstall else \
                install_one(skill, dest, args.link, args.dry_run)
            if msg:
                print(f"  {msg}")
    if not args.uninstall and not args.dry_run:
        print("Done. Start a new agent session so it discovers the skills. The scripts need Python 3 "
              "(matplotlib optional, for charts).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
