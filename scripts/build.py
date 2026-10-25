#!/usr/bin/env python3
"""Deterministic, dependency-free SVG and static catalog build."""
import sys,json,hashlib
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from core import CORE
from themes import THEMES, themed_body
from common import COMMON
from engineering import ENGINEERING
from extension import EXTENSION
from application import APPLICATION, apply_reuse
from robotics import ROBOTICS, apply_robotics_reuse
from studio import STUDIO, apply_studio_reuse
from pdxadv import PDXADV, apply_pdxadv_reuse
from gui_features import ITEMS as GUI_FEATURES
from gui_sketch import ITEMS as GUI_SKETCH
from gui_surface import ITEMS as GUI_SURFACE
from coverage import COVERAGE
from binding_additions import BINDING_ADDITIONS
from toolbar_additions import TOOLBAR_ADDITIONS
from oct25_additions import ADDITIONS as OCT25_ADDITIONS
from usage import apply_usage
from sources import SOURCE_IDS, REFERENCES

def svg(item, theme="light"):
 ink=THEMES[theme]["palette"]["ink"]
 body=item["body"] if theme=="light" else themed_body(item["body"],theme)
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{ink}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" role="img" aria-labelledby="title"><title id="title">{escape(item["name"])}</title>{body}</svg>\n'
def build():
 data=[]
 (ROOT/'icons').mkdir(exist_ok=True)
 (ROOT/'icons-dark').mkdir(exist_ok=True)
 previous=json.loads((ROOT/'manifest.json').read_text())['icons'] if (ROOT/'manifest.json').exists() else []
 collection={'Common':COMMON+EXTENSION.get('Common',[])+APPLICATION.get('Common',[])+STUDIO.get('Common',[])}
 for domain,items in CORE.items():
  collection[domain]=items+ENGINEERING.get(domain,[])+EXTENSION.get(domain,[])+APPLICATION.get(domain,[])+ROBOTICS.get(domain,[])+STUDIO.get(domain,[])+PDXADV.get(domain,[])
 collection['CAD'] += GUI_FEATURES + GUI_SKETCH + GUI_SURFACE
 for domain,items in BINDING_ADDITIONS.items():
  collection.setdefault(domain, []).extend(items)
 for domain,items in TOOLBAR_ADDITIONS.items():
  collection.setdefault(domain, []).extend(items)
 for domain,items in OCT25_ADDITIONS.items():
  collection.setdefault(domain, []).extend(items)
 for domain,items in COVERAGE.items():
  collection.setdefault(domain,[]).extend(items)
 ids=[domain.lower()+'-'+base['id'] for domain,items in collection.items() for base in items]
 if len(ids)!=len(set(ids)):raise ValueError('Duplicate semantic ID in source records')
 for domain,items in collection.items():
  for base in items:
   item=dict(base,category=domain,categories=[domain],sources=base.get('sources',SOURCE_IDS[domain]))
   item.setdefault('family',base['id'])
   item.setdefault('role','tool' if (domain,base['id']) in {('CAM','end-mill'),('CAM','ball-end-mill'),('CMM','tactile-probe'),('CMM','laser-scanner'),('OLP','robot-arm')} else 'command')
   for required in ['description','descriptionJa','tags']:
    if not item.get(required):raise ValueError(f'{domain}/{base["id"]} missing {required}')
   item['id']=domain.lower()+'-'+base['id']; item['file']='icons/'+item['id']+'.svg'
   apply_reuse(item)
   apply_robotics_reuse(item)
   apply_studio_reuse(item)
   apply_pdxadv_reuse(item)
   apply_usage(item)
   content=svg(item); (ROOT/item['file']).write_text(content)
   item['sha256']=hashlib.sha256(content.encode()).hexdigest()
   dark_content=svg(item,'dark'); dark_file='icons-dark/'+item['id']+'.svg'
   (ROOT/dark_file).write_text(dark_content)
   item['variants']={
    'light':{'file':item['file'],'sha256':item['sha256']},
    'dark':{'file':dark_file,'sha256':hashlib.sha256(dark_content.encode()).hexdigest(),'body':themed_body(item['body'],'dark')}
   }
   data.append(item)
 keep={i['file'] for i in data}
 for old in previous:
  if old['file'] not in keep and old['file'].startswith('icons/'):(ROOT/old['file']).unlink(missing_ok=True)
 for stale in (ROOT/'icons-dark').glob('*.svg'):
  if stale.stem not in set(ids):stale.unlink()
 from collections import Counter
 manifest={'counts':dict(Counter(i['role'] for i in data)),'categories':dict(Counter(i['category'] for i in data)),'sourceReferences':REFERENCES,'categoryMemberships':dict(Counter(c for i in data for c in i['categories'])),'usageCounts':dict(Counter(u for i in data for u in i['usages'])),'version':'2.11.0','themes':THEMES,'defaultTheme':'light','viewBox':'0 0 32 32','license':'MIT','count':len(data),'scope':'One semantic entry per independent command, tool, object or status; reuse geometry across command and model-tree contexts; no profile or trajectory variants.','icons':data}
 (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+'\n')
 (ROOT/'catalog.js').write_text('window.CAX_CATALOG='+json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+';\n')
 print(f'Built {len(data)} semantic icons, each with light and dark SVG variants')
if __name__=='__main__':build()
