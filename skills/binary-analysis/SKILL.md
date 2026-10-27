---
name: binary-analysis
description: Authorized native binary inspection.
---

# Authorized native binary inspection

Use for PE, ELF, Mach-O, executable headers, architecture, and reverse engineering of authorized binaries. Start by identifying format, bitness, and target architecture without executing unknown files. REA, Ghidra, McSema, Remill, and rev.ng are external tools, not bundled. A general one-click 32-bit-to-64-bit EXE converter does not exist. REA is one optional analyzer, not a mandatory tool. Explain supported alternatives and verify any claims.

Follow root `SKILL.md`. Find external references only when necessary with `python tools/lookup.py find "topic"`.
