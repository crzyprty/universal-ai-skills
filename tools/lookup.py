#!/usr/bin/env python3
"""Fast offline task-to-link and task-to-skill router. Python 3 standard library only."""
from pathlib import Path
from collections import Counter
import argparse
import json
import re
import sys

BASE = Path(__file__).resolve().parents[1]
CATALOG = BASE / "URL" / "sites.json"
DATA = None

SKILLS = [
 ("binary-analysis", ("reverse engineer", "decompile", "binary", "exe", "dll", "elf", "pe32", "mach-o", "32-bit", "64-bit", "ghidra", "rea")),
 ("rust-game-dev", ("bevy", "rust game", "ecs game")),
 ("mcp-integration", ("mcp", "model context protocol", "tool server", "connector setup", "connect mcp")),
 ("browser-automation", ("browser automation", "playwright", "chrome devtools", "browser test", "test website")),
 ("video-production", ("video", "transcribe", "transcription", "speech", "audio", "subtitle", "podcast", "voice")),
 ("ui-design", ("frontend", "user interface", "ui", "ux", "layout", "design", "desktop app", "figma", "canva", "miro")),
 ("marketing-automation", ("meta ads", "google analytics", "marketing automation", "campaign reporting", "hubspot", "shopify", "n8n", "zapier", "stripe")),
 ("security-audit", ("security audit", "audit security", "vulnerability audit", "pentest", "threat model", "prompt injection")),
 ("systematic-debugging", ("debug", "bug", "bug fix", "test failure", "stack trace", "build error", "runtime error", "failing test")),
 ("tdd", ("test driven development", "tdd", "write tests first", "feature test")),
 ("fast-execution", ("reduce tokens", "token usage", "context overhead", "faster workflow", "speed up agent", "compress output")),
 ("knowledge-memory", ("knowledge graph", "obsidian", "long-term memory", "second brain")),
 ("project-memory", ("project memory", "context notes", "resume project")),
 ("agent-orchestration", ("agents", "agent", "orchestration", "workflow", "opencode", "openclaw", "claudeman", "hermes agent")),
 ("skill-quality", ("skill.md", "agent skills", "skill validation", "skill quality")),
 ("rust-build", ("rust", "cargo", "clippy", "rustfmt", "rustc")),
]

TOPICS = [
 ("marketing", ("meta ads", "marketing api", "google analytics", "campaign reporting", "ad campaign", "marketing")),
 ("automation", ("n8n", "zapier", "workflow automation", "automate apps", "saas automation")),
 ("integrations", ("supabase", "notion", "stripe", "shopify", "hubspot", "figma mcp", "miro mcp", "vercel mcp", "integration")),
 ("web", ("scrape", "scraping", "crawl", "website", "browser", "playwright", "automate web", "web automation", "chrome devtools")),
 ("models", ("local llm", "offline llm", "local model", "llama", "ollama", "inference", "run models", "run ai locally", "deepinfer", "kimi code")),
 ("media", ("transcribe", "transcription", "subtitle", "speech", "voice", "podcast", "video", "audio", "hyperframes", "openmontage")),
 ("reverse-engineering", ("reverse engineer", "decompile", "binary", "exe", "dll", "disassembly", "ghidra", "ida pro", "32-bit", "64-bit", "rea")),
 ("security", ("security", "audit security", "security audit", "vulnerability", "pentest", "red team", "prompt injection", "jailbreak benchmark", "malware", "mpc platform")),
 ("mcp", ("mcp", "model context protocol", "mcp server", "mcp market", "apis.io mcp")),
 ("memory", ("long-term memory", "knowledge base", "knowledge graph", "obsidian", "memory")),
 ("games", ("game", "bevy", "unreal engine", "modding", "mod")),
 ("design", ("ui", "ux", "design", "frontend", "desktop app", "react", "cad", "solidcraft", "scroll craft")),
 ("agents", ("agent", "orchestration", "coding assistant", "assistant", "workflow", "caveman", "rtk")),
 ("coding", ("coding", "code", "programming", "debug", "developer", "documentation", "rust")),
 ("discovery", ("find tools", "tool list", "discover", "search github", "public api", "repository", "apis.io", "skills.sh", "awesome list")),
]

# Phrases and keywords map common user requests to concrete catalog words.
EXPAND = {
 "transcribe": ("transcribe", "transcription", "speech", "audio", "whistle"),
 "subtitle": ("subtitle", "transcript", "video", "speech"),
 "speech": ("speech", "audio", "transcription", "whistle"),
 "podcast": ("audio", "speech", "whistle"),
 "scrape": ("scraping", "extract", "firecrawl"),
 "browser": ("browser", "playwright"),
 "automate": ("automation", "automate", "playwright"),
 "offline": ("local", "ollama", "llama"),
 "llm": ("llm", "model", "ollama", "llama"),
 "local": ("local", "ollama", "llama"),
 "model": ("model", "llm", "ollama"),
 "exe": ("exe", "binary", "ghidra", "rea"),
 "decompile": ("decompilation", "decompile", "ghidra"),
 "design": ("design", "ui", "ux"),
 "frontend": ("frontend", "ui", "react"),
 "memory": ("memory", "knowledge", "hindsight"),
 "mcp": ("mcp", "protocol", "server"),
 "security": ("security", "audit", "vulnerability"),
 "rust": ("rust", "cargo"),
 "game": ("game", "bevy"),
 "agents": ("agent", "orchestration"),
 "agent": ("agent", "orchestration"),
 "documentation": ("documentation", "docs", "context7"),
 "docs": ("docs", "documentation", "context7"),
 "test": ("test", "testing", "promptfoo"),
 "api": ("api", "public", "apis.io"),
 "supabase": ("supabase", "database", "mcp"),
 "stripe": ("stripe", "payments", "mcp"),
 "notion": ("notion", "workspace", "mcp"),
 "shopify": ("shopify", "ecommerce", "mcp"),
 "hubspot": ("hubspot", "crm", "marketing"),
 "meta": ("meta ads", "marketing api", "campaign"),
 "analytics": ("google analytics", "reporting", "mcp"),
 "n8n": ("n8n", "workflow automation"),
 "zapier": ("zapier", "workflow automation"),
 "figma": ("figma", "design", "mcp"),
 "miro": ("miro", "board", "mcp"),
 "canva": ("canva", "design"),
 "vercel": ("vercel", "deployment", "mcp"),
 "context7": ("context7", "documentation", "mcp"),
 "apify": ("apify", "scraping", "mcp"),
 "deepinfer": ("deepinfer", "inference", "deepseek"),
 "solidcraft": ("solidcraft", "cad", "mcp"),
 "hyperframes": ("hyperframes", "video", "html"),
 "superpowers": ("superpowers", "tdd", "debugging"),
 "claudeman": ("claudeman", "container", "claude code"),
 "caveman": ("caveman", "token", "compress"),
 "rtk": ("rtk", "token", "compress"),
 "kimi": ("kimi code", "coding agent"),
}
STOP = {"i", "a", "an", "and", "or", "for", "to", "from", "the", "need", "want", "find", "best", "good", "use", "using", "with", "that", "this", "is", "my", "me", "please", "how", "can", "do", "it", "help", "which", "of", "in", "on", "by", "make", "get", "about", "some", "tools", "tool", "ai", "free", "new", "no", "not", "matching"}

# High-confidence task matches: output only useful links, not filler suggestions.
QUICK = [
 (("apify mcp", "apify endpoint", "apify"), ("Apify MCP Endpoint", "Apify MCP Server")),
 (("mcp market", "mcp marketplace", "discover mcp"), ("MCP Market", "APIs.io MCP")),
 (("apis.io", "api discovery", "discover apis"), ("APIs.io", "APIs.io MCP")),
 (("supabase",), ("Supabase MCP Docs", "Supabase MCP Endpoint")),
 (("meta ads", "marketing api"), ("Meta Marketing API", "Google Analytics MCP")),
 (("google analytics",), ("Google Analytics MCP",)),
 (("n8n",), ("n8n Docs", "Zapier MCP Docs")),
 (("zapier",), ("Zapier MCP Docs", "Zapier MCP Endpoint")),
 (("stripe",), ("Stripe MCP Docs", "Stripe MCP Endpoint")),
 (("notion",), ("Notion MCP Docs", "Notion MCP Endpoint")),
 (("hubspot",), ("HubSpot Developer Docs",)),
 (("shopify",), ("Shopify Dev MCP",)),
 (("canva",), ("Canva MCP",)),
 (("miro",), ("Miro MCP Docs", "Miro MCP Endpoint")),
 (("figma",), ("Figma MCP Docs", "Figma MCP Endpoint")),
 (("vercel",), ("Vercel MCP Docs", "Vercel MCP Endpoint")),
 (("chrome devtools",), ("Chrome DevTools MCP",)),
 (("playwright cli",), ("Playwright CLI",)),
 (("context7",), ("Context7", "Context7 MCP Endpoint")),
 (("kimi code",), ("Kimi Code",)),
 (("deepinfer",), ("DeepInfer",)),
 (("solidcraft",), ("SolidCraft",)),
 (("mpc platform",), ("MPC Platform",)),
 (("claudeman",), ("Claudeman",)),
 (("caveman",), ("Caveman", "RTK CLI")),
 (("superpowers marketplace",), ("Superpowers Marketplace", "Superpowers")),
 (("scroll craft", "scroll-craft"), ("Scroll Craft",)),
 (("build html video", "html video", "html to video", "video from html"), ("Hyperframes", "OpenMontage")),
 (("openmontage",), ("OpenMontage",)),
 (("hermes agent",), ("Hermes Agent",)),
 (("hyperframes",), ("Hyperframes",)),
 (("transcribe", "transcription", "speech recognition", "speech to text", "podcast"), ("Whistle Speech Model", "Whistle")),
 (("extract data from websites", "scrape", "scraping", "web crawl", "crawl website"), ("Firecrawl",)),
 (("browser automation", "automate browser", "browser test", "playwright"), ("Playwright", "Playwright CLI")),
 (("local llm", "offline llm", "local model", "run llm locally", "ollama"), ("ollama", "LM Studio", "llama.cpp")),
 (("32-bit exe", "64-bit exe", "analyze exe", "inspect exe", "decompile", "binary analysis", "reverse engineer"), ("Ghidra", "REA official")),
 (("rea",), ("REA official", "REA Guides")),
 (("rust mcp", "mcp rust", "mcp with rust", "mcp server in rust"), ("RMCP Rust SDK", "MCP Specification")),
 (("mcp", "model context protocol", "mcp server"), ("MCP Market", "MCP Reference Servers", "Model Context Protocol")),
 (("long-term memory", "agent memory", "knowledge graph"), ("Hindsight", "Context Mode")),
 (("obsidian",), ("Obsidian",)),
 (("security audit", "web security audit", "audit a web"), ("Cloudflare Security Audit Skill", "NVIDIA Garak")),
 (("model robustness", "test llm security", "jailbreak benchmark"), ("NVIDIA Garak", "Promptfoo")),
 (("agent skill", "skill.md", "skill creator"), ("Anthropic Skill Creator", "Anthropic Skills")),
 (("frontend ui", "web frontend", "frontend design"), ("Anthropic frontend-design Skill", "UI UX Pro Max")),
 (("ui design", "ux design", "design ui", "web ui"), ("UI UX Pro Max", "Impeccable")),
 (("react interface", "react app"), ("react/react",)),
 (("rust desktop", "tauri"), ("tauri", "egui")),
 (("bevy", "rust game"), ("Bevy Engine", "Bevy Examples")),
 (("documentation", "latest docs", "current docs"), ("Context7",)),
 (("search github repositories", "search github", "find repositories", "github projects"), ("GitHub Explore", "GitHub Trending")),
 (("public api", "free api"), ("Public APIs", "Free API")),
 (("video generation", "generate video", "video with code"), ("Remotion Skills", "Hyperframes")),
 (("ai agent", "coding agent", "terminal agent"), ("OpenCode", "Pi")),
]

def words(text):
 return re.findall(r"[a-z0-9]+", text.lower())

def has_phrase(text, pattern):
 tokens=words(text); target=words(pattern)
 return bool(target) and any(tokens[i:i+len(target)]==target for i in range(len(tokens)-len(target)+1))

def route(task):
 scores=[]
 for idx,(name,terms) in enumerate(SKILLS):
  score=sum(5 + 2*(len(words(term))>1) for term in terms if has_phrase(task,term))
  if score: scores.append((score,-idx,name))
 return max(scores)[2] if scores else 'root'

def group_for(task):
 options=[]
 for idx,(group,phrases) in enumerate(TOPICS):
  score=sum(4 if len(words(p))>1 else 2 for p in phrases if has_phrase(task,p))
  if score:options.append((score,-idx,group))
 return max(options)[2] if options else None

def catalog():
 global DATA
 if DATA is None: DATA=json.loads(CATALOG.read_text(encoding='utf-8'))
 return DATA

def find(query, group=None, limit=5):
 tokens=[x for x in words(query) if x not in STOP]
 target_group=group or group_for(query)
 if not tokens and target_group is None: return []
 for phrases,names in QUICK:
  if any(has_phrase(query,p) for p in phrases):
   selected=[next((x for x in catalog() if x['name']==name and (not group or x['group']==group)),None) for name in names]
   selected=[x for x in selected if x is not None]
   if selected: return selected[:limit]
 expanded=set(tokens)
 for w in tokens:expanded.update(EXPAND.get(w,()))
 # Domain-aware, weighted: return concise, task-relevant matches, never all links.
 results=[]
 for item in catalog():
  if group and item['group']!=group:continue
  if target_group and item['group'] != target_group and not has_phrase(query,item['name']):continue
  name=set(words(item['name']))
  purpose=set(words(item['purpose']))
  score=sum(9 for t in tokens if t in name) + sum(3 for t in tokens if t in purpose)
  score+=sum(3 for t in expanded-set(tokens) if t in name)
  score+=sum(1 for t in expanded-set(tokens) if t in purpose)
  if target_group == item['group']:score+=6
  if has_phrase(item['name'],query):score+=22
  if item['kind']=='tool':score+=2
  if item['kind']=='review-only':score-=12
  if 'unverified' in item['purpose'].lower() or 'unrelated' in item['purpose'].lower():score-=6
  if score>5 and (target_group==item['group'] or any(t in name or t in purpose for t in expanded)):
   results.append((score,item))
 results.sort(key=lambda v:(-v[0],v[1]['name'].lower(),v[1]['url']))
 return [x for _,x in results[:limit]]

def show(items, task=None):
 if task is not None:
  group=group_for(task)
  skill=route(task)
  print('Skill: '+('SKILL.md' if skill=='root' else f'skills/{skill}/SKILL.md'))
  if group:print('Category: URL/categories/'+group+'.md')
 if not items:
  print('No external link is needed from this catalog; use the selected skill and available project tools.')
  return
 for i,x in enumerate(items,1):
  print(f"{i}. {x['name']} [{x['kind']}]\n   {x['purpose']}\n   {x['url']}")

def main(argv=None):
 argv=list(sys.argv[1:] if argv is None else argv)
 if argv and argv[0] not in {'find','route','groups','pick'} and not argv[0].startswith('-'):
  show(find(' '.join(argv),limit=3),task=' '.join(argv));return
 parser=argparse.ArgumentParser(description='Fast offline URL and skill router')
 sub=parser.add_subparsers(dest='command',required=True)
 p=sub.add_parser('pick');p.add_argument('task')
 p=sub.add_parser('find');p.add_argument('query');p.add_argument('--group');p.add_argument('--limit',type=int,default=5);p.add_argument('--json',action='store_true')
 p=sub.add_parser('route');p.add_argument('task')
 sub.add_parser('groups')
 a=parser.parse_args(argv)
 if a.command=='route':
  s=route(a.task);print('SKILL.md' if s=='root' else f'skills/{s}/SKILL.md')
 elif a.command=='groups':
  for group in sorted({i['group'] for i in catalog()}):print(group)
 elif a.command=='pick':show(find(a.task,limit=3),task=a.task)
 else:
  if not 1<=a.limit<=20:parser.error('--limit must be between 1 and 20')
  if a.group and a.group not in {i['group'] for i in catalog()}:parser.error('Unknown category')
  result=find(a.query,a.group,a.limit)
  if a.json:print(json.dumps(result,indent=2))
  else:show(result)

if __name__=='__main__':main()
