# Universal AI Execution Guide (English)

**Primary guide:** [`SKILL.md`](SKILL.md). It acts as the agent's operating manual: infer defaults, choose tools automatically, fetch only needed docs, execute, repair errors, and verify.

## Install once into a project

From the target project directory, run:

```powershell
python path\to\this\bundle\install_instructions.py .
```

Or from PowerShell:

```powershell
& path\to\this\bundle\install.ps1 .
```

The installer copies the guide, catalog, router, and skills to `.universal-ai-guide/`, then adds small entry pointers for common coding agents. Existing instruction files are backed up as `*.before-universal-ai.bak` before the guide pointer is added. Restart/reload the coding agent after installation.

A ZIP cannot activate itself inside an AI client. Automatic use starts after the guide is loaded as a skill or installed into the project instructions. Actual MCP connections may still require OAuth, client support, or account permissions.

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


## Claude-Red integration

The package includes a cross-model router and an installer for the official Claude-Red skill library. The upstream skill contents are fetched at install time (internet required):

```bash
python integrations/claude-red/install_claude_red.py --target .
```

This downloads `SKILL.md` files from the official repository into `.universal-ai-guide/claude-red/Skills/`; it does not execute upstream scripts or automatically activate skills in every AI client. See `integrations/claude-red/README.md`.
