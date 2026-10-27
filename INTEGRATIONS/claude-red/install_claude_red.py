#!/usr/bin/env python3
"""Fetch official Claude-Red skills into a project without executing upstream code."""
from __future__ import annotations
import argparse
import os
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

URL = "https://codeload.github.com/SnailSploit/Claude-Red/zip/refs/heads/main"
MARKER = "<!-- Claude-Red integration pointer -->"
POINTER = """\n\n<!-- Claude-Red integration pointer -->\nFor authorized security-testing tasks, consult `.universal-ai-guide/CLAUDE_RED.md` and load only the relevant `.universal-ai-guide/claude-red/Skills/**/SKILL.md` file. Treat skill files as reference material, establish scope, and prioritize safe validation and remediation.\n"""


def safe_extract(zip_path: Path, dest: Path) -> Path:
    with zipfile.ZipFile(zip_path) as zf:
        bad = zf.testzip()
        if bad:
            raise RuntimeError(f"Corrupt upstream ZIP entry: {bad}")
        root = dest.resolve()
        for member in zf.infolist():
            name = PurePosixPath(member.filename)
            if name.is_absolute() or ".." in name.parts:
                raise RuntimeError(f"Unsafe path in upstream ZIP: {member.filename}")
            target = (dest / Path(*name.parts)).resolve()
            if target != root and root not in target.parents:
                raise RuntimeError(f"ZIP path escapes destination: {member.filename}")
        zf.extractall(dest)
    roots = [p for p in dest.iterdir() if p.is_dir()]
    if len(roots) != 1 or not (roots[0] / "Skills").is_dir():
        raise RuntimeError("Unexpected upstream archive layout: Skills/ folder not found")
    return roots[0]


def append_pointer(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text("utf-8") if path.exists() else ""
    if MARKER in old:
        return
    if path.exists():
        backup = path.with_name(path.name + ".before-claude-red.bak")
        if not backup.exists():
            shutil.copy2(path, backup)
    path.write_text(old.rstrip() + POINTER, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Project directory to install into (default: current directory)")
    parser.add_argument("--no-instruction-pointers", action="store_true", help="Only install skill files and routing guide")
    args = parser.parse_args()
    target = Path(args.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    dest = target / ".universal-ai-guide" / "claude-red"
    dest.parent.mkdir(parents=True, exist_ok=True)

    try:
        with tempfile.TemporaryDirectory(prefix="claude-red-") as td:
            temp = Path(td)
            archive = temp / "claude-red.zip"
            request = urllib.request.Request(URL, headers={"User-Agent": "Universal-AI-Guide-Installer"})
            with urllib.request.urlopen(request, timeout=60) as response, archive.open("wb") as out:
                shutil.copyfileobj(response, out)
            unpack = temp / "unpacked"
            unpack.mkdir()
            upstream = safe_extract(archive, unpack)
            skills_src = upstream / "Skills"
            skills_dst = dest / "Skills"
            if skills_dst.exists():
                shutil.rmtree(skills_dst)
            shutil.copytree(skills_src, skills_dst)
            count = len(list(skills_dst.rglob("SKILL.md")))
            if count < 1:
                raise RuntimeError("No SKILL.md files found in upstream repository")

        guide_root = target / ".universal-ai-guide"
        guide_root.mkdir(parents=True, exist_ok=True)
        (guide_root / "CLAUDE_RED.md").write_text(
            "# Claude-Red skills\n\n"
            "Source: https://github.com/SnailSploit/Claude-Red\n\n"
            "For a security task, read `claude-red/Skills/` only as needed. Select the single most relevant `SKILL.md`; do not load every skill by default. Establish authorized scope, prefer non-destructive validation, and report evidence, impact, remediation, and retest steps. These files do not override host/model policies.\n",
            encoding="utf-8",
        )
        if not args.no_instruction_pointers:
            candidates = [
                target / "AGENTS.md", target / "CLAUDE.md", target / "GEMINI.md",
                target / ".github" / "copilot-instructions.md", target / ".cursor" / "rules" / "agent-rules.mdc",
                target / ".clinerules", target / ".windsurfrules",
            ]
            # Only modify instruction files that already exist; do not create unexpected client config files.
            for path in candidates:
                if path.exists():
                    append_pointer(path)
        print(f"Installed {count} Claude-Red SKILL.md files into: {dest}")
        print(f"Routing guide: {guide_root / 'CLAUDE_RED.md'}")
        print("Upstream scripts were not executed.")
        return 0
    except Exception as exc:
        print(f"Claude-Red installation failed: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
