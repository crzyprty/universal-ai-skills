#!/usr/bin/env python3
"""Install the Universal AI Execution Guide into a project without discarding existing instructions."""
from pathlib import Path
import argparse, shutil
HERE = Path(__file__).resolve().parent
MARKER = "<!-- UNIVERSAL_AI_EXECUTION_GUIDE -->"
ENTRY = (MARKER + "\n" + "Follow `.universal-ai-guide/SKILL.md` automatically for every task. Use available tools and relevant MCPs directly, choose sensible defaults without asking the user to select tools, read only relevant files, execute the work, and verify the result.\n\n")
ROOT_FILES = ["AGENTS.md", "CLAUDE.md", "GEMINI.md", "OPENAI_CODEX.md", "KIMI.md", ".windsurfrules", ".clinerules"]
BUNDLE_DIRS = ["URL", "MCP", "INTEGRATIONS", "skills", "tools"]
BUNDLE_FILES = ["SKILL.md", "FAST.md", "CORE_FEATURES.md"]
def merge_entry(target: Path, name: str):
    p = target / name
    if p.exists():
        old = p.read_text(encoding="utf-8", errors="replace")
        if MARKER in old: return "unchanged"
        backup = p.with_name(p.name + ".before-universal-ai.bak")
        if not backup.exists(): shutil.copy2(p, backup)
        p.write_text(ENTRY + old, encoding="utf-8")
        return "merged"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(ENTRY, encoding="utf-8")
    return "created"
def main():
    parser = argparse.ArgumentParser(description="Install the guide into a project.")
    parser.add_argument("target", nargs="?", default=".", help="Project directory (default: current directory)")
    target = Path(parser.parse_args().target).expanduser().resolve()
    if not target.exists() or not target.is_dir(): raise SystemExit(f"Target directory does not exist: {target}")
    dest = target / ".universal-ai-guide"; dest.mkdir(exist_ok=True)
    for name in BUNDLE_FILES: shutil.copy2(HERE / name, dest / name)
    for name in BUNDLE_DIRS:
        src = HERE / name
        if src.exists(): shutil.copytree(src, dest / name, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    results = [(name, merge_entry(target, name)) for name in ROOT_FILES]
    cursor = target / ".cursor" / "rules" / "agent-rules.mdc"; cursor.parent.mkdir(parents=True, exist_ok=True)
    cursor_head = "---\ndescription: Always follow the Universal AI Execution Guide.\nalwaysApply: true\n---\n"
    if cursor.exists():
        old = cursor.read_text(encoding="utf-8", errors="replace")
        if MARKER not in old:
            backup = cursor.with_name(cursor.name + ".before-universal-ai.bak")
            if not backup.exists(): shutil.copy2(cursor, backup)
            # Preserve existing frontmatter instead of nesting a second one.
            if old.startswith("---\n") and "\n---\n" in old[4:]:
                cut = old.find("\n---\n", 4) + len("\n---\n")
                cursor.write_text(old[:cut] + MARKER + "\nFollow `.universal-ai-guide/SKILL.md` automatically.\n\n" + old[cut:], encoding="utf-8")
            else: cursor.write_text(cursor_head + ENTRY + old, encoding="utf-8")
            results.append((str(cursor.relative_to(target)), "merged"))
        else: results.append((str(cursor.relative_to(target)), "unchanged"))
    else:
        cursor.write_text(cursor_head + ENTRY, encoding="utf-8"); results.append((str(cursor.relative_to(target)), "created"))
    copilot = target / ".github" / "copilot-instructions.md"
    results.append((str(copilot.relative_to(target)), merge_entry(target, str(copilot.relative_to(target)))))
    print(f"Installed guide files to: {dest}")
    for name, status in results: print(f"{status:9} {name}")
    print("Reload the coding agent so it reads the project instructions.")
if __name__ == "__main__": main()
