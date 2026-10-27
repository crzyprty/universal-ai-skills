<div align="center">

# Universal AI Skills & Execution Guide

[![GitHub Actions CI](https://img.shields.io/badge/CI-Automated%20Cloud-success?logo=githubactions)](.github/workflows/autonomous-maintenance.yml)
[![Supported Models](https://img.shields.io/badge/Models-Claude%20%7C%20Gemini%20%7C%20Codex%20%7C%20Cursor%20%7C%20Windsurf%20%7C%20Cline%20%7C%20Kimi-blueviolet)](#supported-models)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Autonomous Cloud](https://img.shields.io/badge/Autonomous%2024%2F7-Cloud%20Active-orange)](.github/workflows/ai-issue-agent.yml)

**Universal skill catalog, execution rules, and autonomous cloud workflows for all major AI models and coding agents.**

</div>

---

**Primary guide:** [`SKILL.md`](SKILL.md). It acts as the agent operating manual: infer defaults, choose tools automatically, fetch only needed docs, execute, repair errors, and verify.

---

## 24/7 Cloud Autonomy (Runs Even When PC Is Off)

This repository includes autonomous GitHub Actions workflows running around the clock on GitHub cloud servers:
- **Autonomous AI Issue & PR Assistant** (`.github/workflows/ai-issue-agent.yml`): Automatically routes incoming issues and pull requests to the right skill and documentation, provides immediate assistance, and labels items.
- **Weekly Autonomous Healthcheck** (`.github/workflows/autonomous-maintenance.yml`): Runs comprehensive integrity tests, updates catalog validation, and packages the bundle for download.

---

## Supported Models

| Model / Agent | Entry File | Description |
| :--- | :--- | :--- |
| **Anthropic Claude** | [`CLAUDE.md`](CLAUDE.md) | Claude 3.5 Sonnet / Claude Code adapter |
| **Google Gemini** | [`GEMINI.md`](GEMINI.md) | Gemini 1.5/2.0 Flash & Pro / Antigravity |
| **OpenAI Codex / ChatGPT** | [`OPENAI_CODEX.md`](OPENAI_CODEX.md) | GPT-4o, o1, o3, Codex CLI instructions |
| **Cursor IDE** | [`.cursor/rules/agent-rules.mdc`](.cursor/rules/agent-rules.mdc) | Cursor Rules integration |
| **Windsurf (Codeium)** | [`.windsurfrules`](.windsurfrules) | Windsurf Cascade rules |
| **Cline (VS Code)** | [`.clinerules`](.clinerules) | Cline autonomous agent rules |
| **Moonshot Kimi** | [`KIMI.md`](KIMI.md) | Kimi K1 / K1.5 integration |
| **Generic Agents** | [`AGENTS.md`](AGENTS.md) | Universal ReAct / Tool-calling agents |

---

## Install once into a project

From the target project directory, run:

```powershell
python path\to\this\bundle\install_instructions.py .
```

Or from PowerShell:

```powershell
& path\to\this\bundle\install.ps1 .
```

The installer copies the guide, catalog, router, and skills to `.universal-ai-guide/`, then adds small entry pointers for common coding agents. Existing instruction files are backed up as `*.before-universal-ai.bak` before the guide pointer is added. Restart or reload the coding agent after installation.

A ZIP cannot activate itself inside an AI client. Automatic use starts after the guide is loaded as a skill or installed into the project instructions. Actual MCP connections may still require OAuth, client support, or account permissions.

---

## Fast routing

```bash
python tools/lookup.py "fix this test failure"
python tools/lookup.py route "build a marketing automation"
```

- [`FAST.md`](FAST.md) - compact operating rules.
- [`CORE_FEATURES.md`](CORE_FEATURES.md) - short summary of the requested repositories and their useful behaviors.
- [`URL/BY_NEED.md`](URL/BY_NEED.md) - common task to link mapping.
- [`URL/INDEX.md`](URL/INDEX.md) - categories.
- [`URL/ALL_LINKS.md`](URL/ALL_LINKS.md) - every catalog link with purpose.
- [`MCP/PRIORITY.md`](MCP/PRIORITY.md) - pinned high-value MCP and agent resources.
- [`MCP/CONNECTORS.md`](MCP/CONNECTORS.md) - official docs and endpoints.
- [`INTEGRATIONS/INDEX.md`](INTEGRATIONS/INDEX.md) - Kimi, Supabase, Meta Ads, Miro, n8n, Canva, Context7, Analytics, Stripe, Playwright CLI, HubSpot, Notion, Zapier, GitHub, Shopify, Figma, Vercel, Chrome DevTools.

The bundle is a guide and reference catalog. It does not install third-party applications or authenticate accounts automatically.

---

## Claude-Red integration

The package includes a cross-model router and an installer for the official Claude-Red skill library. The upstream skill contents are fetched at install time (internet required):

```bash
python integrations/claude-red/install_claude_red.py --target .
```

This downloads `SKILL.md` files from the official repository into `.universal-ai-guide/claude-red/Skills/`; it does not execute upstream scripts or automatically activate skills in every AI client. See `integrations/claude-red/README.md`.

---

## License

This project is licensed under the [MIT License](LICENSE).
