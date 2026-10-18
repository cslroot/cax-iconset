#!/usr/bin/env python3
"""Contact sheets of every distinct semantic entry, with 48/24/16px previews."""
import json, math
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'manifest.json').read_text())

def sheet(items, name, title):
 cols=8; width=1440; height=88+math.ceil(len(items)/cols)*126
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="{width}" height="{height}" fill="#f5f8f5"/><text x="24" y="35" font-family="sans-serif" font-size="23" fill="#253b53">{escape(title)}</text><text x="24" y="60" font-family="sans-serif" font-size="13" fill="#45665f">{len(items)} semantic entries · original 32px grid · previews at 48 / 24 / 16 px</text>']
 for n,i in enumerate(items):
  x=20+(n%cols)*177;y=80+(n//cols)*126
  parts.append(f'<rect x="{x}" y="{y}" width="169" height="118" rx="9" fill="white" stroke="#dce6df"/>')
  for size,dx in [(48,16),(24,87),(16,132)]:
   body=i['body']
   prefix=f'sheet-{n}-{size}-'
   import re
   body=re.sub(r'id="([^"]+)"',lambda m:f'id="{prefix}{m[1]}"',body)
   body=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{prefix}{m[1]})',body)
   parts.append(f'<svg x="{x+dx}" y="{y+15+(48-size)/2}" width="{size}" height="{size}" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')
  parts.append(f'<text x="{x+8}" y="{y+84}" font-family="sans-serif" font-size="10" fill="#253b53">{escape(i["name"])}</text><text x="{x+8}" y="{y+102}" font-family="sans-serif" font-size="7.5" fill="#45665f">{escape(i["id"])}</text>')
 parts.append('</svg>');(ROOT/f'qa/{name}.svg').write_text(''.join(parts))
for category in manifest['categories']:
 sheet([i for i in manifest['icons'] if i['category']==category],category.lower(),'CAX / '+category)
# Keep the reviewed-additions sheet reproducible independently of Git HEAD.
import sys
sys.path.insert(0,str(ROOT/'src'))
from extension import EXTENSION
added={domain.lower()+'-'+i['id'] for domain,items in EXTENSION.items() for i in items}
sheet([i for i in manifest['icons'] if i['id'] in added],'additions','CAX / source-reviewed additions')
from application import APPLICATION
current={domain.lower()+'-'+i['id'] for domain,items in APPLICATION.items() for i in items}
sheet([i for i in manifest['icons'] if i['id'] in current],'application-additions','CAX / application command families')
from robotics import GLYPHS as ROBOTICS_GLYPHS
sheet([i for i in manifest['icons'] if i['id'] in ROBOTICS_GLYPHS],'robotics-additions','CAX / robotics, programming and simulation')
from studio import GLYPHS as STUDIO_GLYPHS
sheet([i for i in manifest['icons'] if i['id'] in STUDIO_GLYPHS],'studio-additions','CAX / source-verified Studio commands')
from pdxadv import GLYPHS as PDXADV_GLYPHS
sheet([i for i in manifest['icons'] if i['id'] in PDXADV_GLYPHS],'pdxadv-additions','CAX / pdxadv analysis and design workflow')
print('Built six category sheets and five reviewed-additions sheets')
