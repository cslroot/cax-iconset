#!/usr/bin/env python3
"""Refresh count/reference blocks without treating the counts as scope targets."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'manifest.json').read_text())
coverage='\n| Primary category | Symbols |\n| --- | ---: |\n'+''.join(f'| {c} | {n} |\n' for c,n in m['categories'].items())+f'| **Total** | **{m["count"]}** |\n\n'
coverage+=f'Primary roles: {m["counts"]["command"]} commands, {m["counts"]["tool"]} selectable tools, {m["counts"]["object"]} objects and {m["counts"]["status"]} status symbols. Every SVG is counted once.\n\n'
coverage+=f'{m["usageCounts"]["model-tree"]} entries support model-tree use, including reused command/tool symbols; these are not additional SVGs.\n'
for file in ['README.md','docs/REFERENCE.md']:
 p=ROOT/file;s=p.read_text();s=re.sub(r'(?<=<!-- coverage:start -->).*?(?=<!-- coverage:end -->)',coverage,s,flags=re.S)
 if file=='docs/REFERENCE.md':
  refs='\n| Source | Primary documentation | Taxonomy |\n| --- | --- | --- |\n'+''.join(f'| {id} | [{v["title"]}]({v["url"]}) | {v["scope"]} |\n' for id,v in m['sourceReferences'].items())
  s=re.sub(r'(?<=<!-- references:start -->).*?(?=<!-- references:end -->)',refs,s,flags=re.S)
 p.write_text(s)
print('Refreshed coverage and primary-source documentation')
