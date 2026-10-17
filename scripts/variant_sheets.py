#!/usr/bin/env python3
"""Render reproducible representative sheets without external assets."""
import json
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'manifest.json').read_text())['icons']
for domain in ['CAD','CAM','CAE','CMM','OLP']:
 items=[i for i in data if i['category']==domain and i['kind']=='variant']
 families=list(dict.fromkeys(i['family'] for i in items))
 picks=[]
 for idx,fam in enumerate(families):
  family=[i for i in items if i['family']==fam]
  # Four geometrically different contexts per recipe. Keep selection stable.
  for context in ['circle','l-section','hexagon','slotted-plate'] if domain!='OLP' else ['straight','spline','zigzag','circle']:
   found=next((i for i in family if i['context']==context),None)
   if found:picks.append(found)
 rows=(len(picks)+7)//8;h=100+rows*122
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="{h}" viewBox="0 0 1400 {h}"><rect width="1400" height="{h}" fill="#f5f8f5"/><text x="30" y="38" font-family="sans-serif" font-size="23" fill="#253b53">CAX / {domain} contextual variants</text><text x="30" y="65" font-family="sans-serif" font-size="12" fill="#7e8b95">Four distinct geometry contexts per compatible recipe · 48 / 24 px previews</text>']
 for n,i in enumerate(picks):
  x=20+(n%8)*172;y=86+(n//8)*122
  parts.append(f'<rect x="{x}" y="{y}" width="164" height="112" rx="8" fill="white" stroke="#e0e7df"/>')
  for size,dx,dy in [(48,45,9),(24,103,25)]:parts.append(f'<svg x="{x+dx}" y="{y+dy}" width="{size}" height="{size}" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{i["body"]}</svg>')
  parts.append(f'<text x="{x+82}" y="{y+79}" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#253b53">{escape(i["family"])}</text><text x="{x+82}" y="{y+98}" text-anchor="middle" font-family="sans-serif" font-size="8" fill="#709387">{escape(i["context"])}</text>')
 parts.append('</svg>');(ROOT/f'qa/variants-{domain.lower()}.svg').write_text(''.join(parts))
