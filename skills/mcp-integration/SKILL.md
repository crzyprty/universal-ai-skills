---
name: mcp-integration
description: Use when a task needs an external app, API, MCP server, or missing connector.
---

# MCP Integration

1. Check connected tools and existing MCP servers first.
2. Choose the smallest relevant integration from `MCP/PRIORITY.md` or `MCP/CONNECTORS.md`.
3. Prefer official docs and endpoints. Use MCP Market for discovery when the official route is unclear.
4. Configure only the needed server; do not load all integrations.
5. Test with a small read-only call, then perform the requested action.
6. Never claim authentication or connectivity without verifying it.
