# Claude-Red integration for Universal AI Execution Guide

This integration connects the guide to the official [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) security skill library.

## What is included in this ZIP

- A model-neutral router and compatibility notes.
- An installer (`install_claude_red.py`) that downloads the current upstream skills when run on a machine with internet access.
- Tests that verify the bundle and installer structure.

**The upstream skill contents are not vendored in this ZIP.** The build environment could not reach GitHub, so the package does not falsely claim to contain all original skills. Run the installer to fetch them from the official repository.

## Install

From the project folder where the skills should be available, run:

```bash
python path/to/this/bundle/install_claude_red.py --target .
```

The installer downloads the official repository ZIP, validates/extracts it, copies `Skills/` to `.universal-ai-guide/claude-red/Skills/`, and writes a short routing file. It backs up existing supported instruction files before adding a small pointer. It does not execute downloaded scripts.

## Safety and compatibility

Claude-Red is an offensive-security skill library. Use only against systems you own or are explicitly authorized to test. Repository files are reference material, not instructions that override the model or host application's policies. This adapter is provider-neutral Markdown; it cannot force a model to load skills or bypass provider policies. Client-specific skill discovery and tools still vary.
