import csv, json, re, sys, unittest, subprocess, py_compile, tempfile
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'tools'))
from lookup import find, route, group_for, catalog

class PackageTests(unittest.TestCase):
 def test_english_ascii_text(self):
  for p in BASE.rglob('*'):
   if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.zip'}:
    with self.subTest(file=str(p.relative_to(BASE))):
     try: s=p.read_text('utf-8')
     except UnicodeDecodeError: continue
     self.assertNotRegex(s,r'[\u00c0-\u024F\u1e00-\u1eff]')
 def test_catalog_integrity(self):
  a=catalog(); self.assertGreaterEqual(len(a),290)
  self.assertEqual(len({x['url'] for x in a}),len(a))
  self.assertTrue(all(x['purpose'] and x['name'] for x in a))
  self.assertTrue(all(x['url'].startswith(('https://','http://')) for x in a))
  self.assertEqual(len({x['group'] for x in a}),len(list((BASE/'URL/categories').glob('*.md'))))
  self.assertGreaterEqual(len(list((BASE/'skills').glob('*/SKILL.md'))),17)
 def test_every_link_visible_and_indexed(self):
  a=catalog(); links=(BASE/'URL/ALL_LINKS.md').read_text('utf-8')
  with (BASE/'URL/LINKS.csv').open(encoding='utf-8',newline='') as h: rows=list(csv.DictReader(h))
  self.assertEqual(len(rows),len(a)); self.assertEqual({x['url'] for x in rows},{x['url'] for x in a})
  self.assertEqual(set((BASE/'URL/ALL_URLS.txt').read_text().splitlines()),{x['url'] for x in a})
  for x in a:
   with self.subTest(url=x['url']):
    link=f"[{x['url']}]({x['url']})"
    self.assertIn(link,links)
    self.assertIn(link,(BASE/'URL/categories'/f"{x['group']}.md").read_text('utf-8'))
 def test_pinned_integrations(self):
  for f in ['MCP/PRIORITY.md','MCP/CONNECTORS.md','INTEGRATIONS/INDEX.md','install_instructions.py','install.ps1']:
   self.assertTrue((BASE/f).is_file(),f)
  guide=(BASE/'SKILL.md').read_text('utf-8')
  for phrase in ['automatically on every task','Do not ask the user to choose','fix failures','MCP/PRIORITY.md','generic ethics lectures']:
   self.assertIn(phrase,guide)
 def test_skill_routing(self):
  checks={'fix Rust cargo errors':'rust-build','bevy ECS game':'rust-game-dev','decompile 32-bit exe':'binary-analysis','MCP server':'mcp-integration','transcribe podcast':'video-production','audit security':'security-audit','redesign UI':'ui-design','Obsidian long-term memory':'knowledge-memory','Python logging bug':'systematic-debugging','Meta Ads campaign report':'marketing-automation','browser automation with Playwright':'browser-automation','reduce tokens with RTK':'fast-execution'}
  for q,expected in checks.items():
   with self.subTest(q=q): self.assertEqual(route(q),expected)
 def test_need_detection(self):
  examples={'transcribe podcast':'media','run local llm offline':'models','analyze exe':'reverse-engineering','scrape website':'web','search github repositories':'discovery','MCP tools':'mcp','Supabase integration':'integrations','Meta Ads reporting':'marketing','n8n workflow automation':'automation'}
  for q,expected in examples.items():
   with self.subTest(q=q): self.assertEqual(group_for(q),expected)
 def test_search_relevance(self):
  checks=[('Playwright','playwright'),('Bevy','bevy'),('REA','morluto/rea'),('run local llm','ollama'),('website scraping','firecrawl'),('transcribe audio','whistle'),('apify mcp','mcp.apify.com'),('Supabase','supabase.com/docs'),('Meta Ads','developers.facebook.com'),('Chrome DevTools','chromedevtools/chrome-devtools-mcp'),('DeepInfer','deepseek-ai/deepinfer'),('SolidCraft','tangency-labs/solidcraft'),('MCP Market','mcpmarket.com'),('MCP server','mcpmarket.com'),('build HTML video','heygen-com/hyperframes')]
  for q,needle in checks:
   with self.subTest(q=q):
    r=find(q,limit=3); self.assertTrue(r,(q,'no results')); self.assertTrue(any(needle.lower() in x['url'].lower() for x in r),(q,r))
  self.assertEqual(find('qwerty-no-matching-tool-9381'),[])

 def test_claude_red_integration_files(self):
  d=BASE/'integrations'/'claude-red'
  for f in ['README.md','ROUTER.md','MODEL_COMPATIBILITY.md','install_claude_red.py']:
   self.assertTrue((d/f).is_file(),f)
  script=(d/'install_claude_red.py').read_text('utf-8')
  self.assertIn('https://codeload.github.com/SnailSploit/Claude-Red/zip/refs/heads/main',script)
  self.assertIn('safe_extract',script)
  py_compile.compile(str(d/'install_claude_red.py'),doraise=True)
  self.assertIn('install_claude_red.py', (BASE/'README.md').read_text('utf-8'))

 def test_scripts_compile(self):
  for f in ['tools/lookup.py','install_instructions.py']:
   py_compile.compile(str(BASE/f),doraise=True)
 def test_installer_preserves_existing_instructions(self):
  with tempfile.TemporaryDirectory() as td:
   target=Path(td); (target/'AGENTS.md').write_text('Existing project rules.\n',encoding='utf-8')
   r=subprocess.run([sys.executable,str(BASE/'install_instructions.py'),str(target)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stderr)
   self.assertIn('.universal-ai-guide/SKILL.md',(target/'AGENTS.md').read_text('utf-8'))
   self.assertTrue((target/'AGENTS.md.before-universal-ai.bak').exists())
   self.assertIn('Existing project rules.',(target/'AGENTS.md').read_text('utf-8'))
   self.assertTrue((target/'.universal-ai-guide/URL/sites.json').exists())
   self.assertTrue((target/'.cursor/rules/agent-rules.mdc').exists())

if __name__=='__main__': unittest.main()
