# Model compatibility

This package uses portable Markdown and upstream `SKILL.md` files. It does not use a universal plugin API.

- Claude / Claude Code: use the client's supported skills directory or project instructions.
- ChatGPT: attach the relevant skill as context or place the guide in a supported project/workspace; the ZIP itself does not activate skills.
- Gemini / Kimi: attach the relevant Markdown or use product-supported project instructions.
- GitHub Copilot: use repository instructions supported by the chosen IDE.
- Cursor / Windsurf: use their supported project rules or referenced Markdown.
- OpenAI Codex: use `AGENTS.md` or repository instructions.
- Other models: provide the task preamble and one relevant skill file, subject to that model's context/tool limits.

Compatibility means the material is readable and reusable across models, not that every client auto-loads or executes it. Tools, authentication, context limits, and safety rules remain product-specific.
