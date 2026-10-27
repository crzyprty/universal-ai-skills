# MCP and Integration Quick Reference

Use existing connected integrations first. The endpoints below are references, not proof that a connector is installed or authenticated. OAuth, permissions, and supported clients vary.

| Need | Official docs or endpoint |
|---|---|
| Discover MCP servers | [MCP Market](https://mcpmarket.com/) |
| Extract website data | [Apify MCP](https://mcp.apify.com/) and [source repo](https://github.com/apify/apify-mcp-server) |
| Discover APIs | [APIs.io](https://apis.io/) and [APIs.io MCP](https://apis.io/mcp) |
| Current library docs | [Context7 docs](https://github.com/upstash/context7) / `https://mcp.context7.com/mcp` |
| GitHub repositories and issues | [GitHub MCP source](https://github.com/github/github-mcp-server) / `https://api.githubcopilot.com/mcp/` |
| Supabase database and backend | [Setup guide](https://supabase.com/docs/guides/ai-tools/mcp) / `https://mcp.supabase.com/mcp` |
| Notion pages and databases | [Setup guide](https://www.notion.com/help/notion-mcp) / `https://mcp.notion.com/mcp` |
| Stripe | [Setup guide](https://docs.stripe.com/mcp) / `https://mcp.stripe.com` |
| Figma designs | [Setup guide](https://developers.figma.com/docs/figma-mcp-server/) / `https://mcp.figma.com/mcp` |
| Miro boards | [Setup guide](https://developers.miro.com/docs/miro-mcp) / `https://mcp.miro.com/` |
| Vercel projects and deployments | [Setup guide](https://vercel.com/docs/ai-tooling/vercel-mcp) / `https://mcp.vercel.com` |
| Zapier app actions | [Setup guide](https://help.zapier.com/hc/en-us/articles/48308034391821-What-is-Zapier-MCP) / `https://mcp.zapier.com/` |
| Canva design operations | [Canva MCP announcement](https://community.canva.dev/t/the-wait-list-is-over-canva-mcp-server-is-now-generally-available/8942) |
| Meta Ads | [Marketing API docs](https://developers.facebook.com/docs/marketing-api/) |
| Google Analytics | [Read-only Analytics MCP docs](https://developers.google.com/analytics/devguides/MCP) |
| Shopify | [Shopify Dev MCP docs](https://shopify.dev/docs/apps/build/devmcp) |
| HubSpot | [Official developer docs](https://developers.hubspot.com/) |
| Browser CLI | [Playwright CLI](https://github.com/microsoft/playwright-cli) |
| Chrome debugging | [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| n8n workflows | [n8n docs](https://docs.n8n.io/) |

## Minimal connection procedure

1. Check whether the client already has the relevant connector.
2. If yes, use it and inspect its available tools.
3. If no, open the official setup guide and configure only that server if setup tools are available.
4. If OAuth, account login, paid access, or admin approval is required, prepare the exact next step; do not pretend the connection is active.
5. Verify the connection with one small read-only call before using write actions.

Do not enable every server. Too many MCPs create tool-selection noise, latency, and context overhead.
