#!/usr/bin/env python3
"""Deterministic, dependency-free SVG and static catalog build."""
import sys,json,hashlib
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from core import CORE,INK
from common import COMMON
from engineering import ENGINEERING
from extension import EXTENSION
from usage import apply_usage
from sources import SOURCE_IDS, REFERENCES

def svg(item):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{INK}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" role="img" aria-labelledby="title"><title id="title">{escape(item["name"])}</title>{item["body"]}</svg>\n'
def build():
 data=[]
 (ROOT/'icons').mkdir(exist_ok=True)
 previous=json.loads((ROOT/'manifest.json').read_text())['icons'] if (ROOT/'manifest.json').exists() else []
 collection={'Common':COMMON+EXTENSION.get('Common',[])}
 for domain,items in CORE.items():
  collection[domain]=items+ENGINEERING.get(domain,[])+EXTENSION.get(domain,[])
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
   apply_usage(item)
   content=svg(item); (ROOT/item['file']).write_text(content)
   item['sha256']=hashlib.sha256(content.encode()).hexdigest(); data.append(item)
 keep={i['file'] for i in data}
 for old in previous:
  if old['file'] not in keep and old['file'].startswith('icons/'):(ROOT/old['file']).unlink(missing_ok=True)
 from collections import Counter
 manifest={'counts':dict(Counter(i['role'] for i in data)),'categories':dict(Counter(i['category'] for i in data)),'sourceReferences':REFERENCES,'categoryMemberships':dict(Counter(c for i in data for c in i['categories'])),'usageCounts':dict(Counter(u for i in data for u in i['usages'])),'version':'2.1.0','viewBox':'0 0 32 32','license':'MIT','count':len(data),'scope':'One semantic entry per independent command, tool, object or status; reuse geometry across command and model-tree contexts; no profile or trajectory variants.','icons':data}
 (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+'\n')
 (ROOT/'catalog.js').write_text('window.CAX_CATALOG='+json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+';\n')
 print(f'Built {len(data)} icons')
if __name__=='__main__':build()
