---
name: browser-automation
description: Use for UI tests, browser actions, screenshots, and web debugging.
---

# Browser Automation

1. Prefer Playwright CLI for concise, repeatable browser actions.
2. Use Chrome DevTools MCP for console errors, requests, performance traces, and live Chrome inspection.
3. Read only relevant page state; do not dump full accessibility trees or entire DOMs without need.
4. Reuse a browser session where practical.
5. Verify the final page state and capture screenshots or traces when useful.
