# Choose a Resource by Need

Start with one matching route. The main guide should make the choice automatically.

| Need | Start here | Purpose |
|---|---|---|
| Coding behavior and minimal changes | [Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills) | Simplicity, surgical edits, clear goals, verification |
| Complex coding workflow, TDD, debugging | [Superpowers](https://github.com/obra/superpowers) | Structured engineering skills and workflows |
| Reduce tokens and noisy CLI output | [Caveman](https://github.com/JuliusBrussee/caveman) or [RTK](https://github.com/rtk-ai/rtk) | Compress output and reduce context overhead |
| Run Claude Code in containers | [Claudeman](https://github.com/scottrigby/claudeman) | Container profiles, hooks, caches, isolated sessions |
| Discover agent skills | [skills.sh](https://skills.sh/) or [Anthropic Skills](https://github.com/anthropics/skills) | Find and reuse agent skills |
| Discover MCP servers | [MCP Market](https://mcpmarket.com/) | Search MCP servers and skills |
| Extract websites and online data | [Apify MCP](https://mcp.apify.com/) | Structured extraction from websites and platforms |
| Discover APIs and schemas | [APIs.io](https://apis.io/) | API providers, documentation, schemas, MCP/skills |
| Browser tests and interaction | [Playwright CLI](https://github.com/microsoft/playwright-cli) | Fast browser automation with compact CLI output |
| Browser console, network, performance | [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Live Chrome inspection and debugging |
| Current package/library docs | [Context7](https://github.com/upstash/context7) | Version-specific documentation and examples |
| Supabase | [Supabase MCP docs](https://supabase.com/docs/guides/ai-tools/mcp) | Database and backend access |
| Meta Ads | [Meta Marketing API](https://developers.facebook.com/docs/marketing-api/) | Campaigns, ad insights, reporting |
| Google Analytics | [Analytics MCP](https://developers.google.com/analytics/devguides/MCP) | Read-only analytics queries |
| CRM and marketing | [HubSpot developer docs](https://developers.hubspot.com/) | CRM, sales, marketing APIs |
| Cross-app automation | [Zapier MCP](https://help.zapier.com/hc/en-us/articles/48308034391821-What-is-Zapier-MCP) or [n8n](https://docs.n8n.io/) | SaaS actions and workflow automation |
| Notion | [Notion MCP docs](https://www.notion.com/help/notion-mcp) | Read and write authorized workspace content |
| Payments and billing | [Stripe MCP docs](https://docs.stripe.com/mcp) | Stripe resources and actions |
| Store development | [Shopify Dev MCP](https://shopify.dev/docs/apps/build/devmcp) | Shopify app and store workflows |
| Design assets | [Figma MCP](https://developers.figma.com/docs/figma-mcp-server/) or [Canva MCP](https://community.canva.dev/t/the-wait-list-is-over-canva-mcp-server-is-now-generally-available/8942) | Read/edit designs and generate assets |
| Boards and diagrams | [Miro MCP](https://developers.miro.com/docs/miro-mcp) | Work with Miro boards |
| Deployments | [Vercel MCP](https://vercel.com/docs/ai-tooling/vercel-mcp) | Projects, deployments, and logs |
| Video from HTML | [Hyperframes](https://github.com/heygen-com/hyperframes) | Render editable HTML/CSS/JS video projects |
| Multi-stage video production | [OpenMontage](https://github.com/calesthio/OpenMontage) | Agentic video production pipelines |
| Scroll-driven websites | [Scroll Craft](https://github.com/nateherkai/scroll-craft) | High-craft scroll-driven frontend design |
| Parametric 3D CAD | [SolidCraft](https://github.com/tangency-labs/solidcraft) | CAD modeling and MCP automation |
| DeepSeek offline inference | [DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Specialized high-performance inference; verify hardware requirements |
| Multi-party computation verification | [MPC Platform](https://github.com/CircuitMurderer/MPC-Platform) | Verify secure multi-party computation results; not an MCP server |
| Natural-sounding prose | [Humanizer](https://github.com/blader/humanizer) | Edit prose while preserving meaning |

If no match is obvious, run `python tools/lookup.py "describe the task"`. It returns up to three candidates and a specialist skill.
