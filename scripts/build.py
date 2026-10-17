#!/usr/bin/env python3
"""Deterministic, dependency-free SVG and static catalog build."""
import sys,json,hashlib
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from core import CORE,INK
from sources import SOURCE_IDS, REFERENCES

def svg(item):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="{INK}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" role="img" aria-labelledby="title"><title id="title">{escape(item["name"])}</title>{item["body"]}</svg>\n'
def build():
 data=[]
 (ROOT/'icons').mkdir(exist_ok=True)
 previous=json.loads((ROOT/'manifest.json').read_text())['icons'] if (ROOT/'manifest.json').exists() else []
 for domain,items in CORE.items():
  for base in items:
   item=dict(base,category=domain,categories=[domain],kind='core',family=base['id'],sources=SOURCE_IDS[domain],description='Original core symbol for '+base['name'].lower()+'. References describe the feature taxonomy, not the artwork.')
   item['id']=domain.lower()+'-'+base['id']; item['file']='icons/'+item['id']+'.svg'
   content=svg(item); (ROOT/item['file']).write_text(content)
   item['sha256']=hashlib.sha256(content.encode()).hexdigest(); data.append(item)
 if '--core-only' not in sys.argv:
  try:
   from extended import extend
   for item in extend():
    content=svg(item); (ROOT/item['file']).write_text(content)
    item['sha256']=hashlib.sha256(content.encode()).hexdigest(); data.append(item)
  except ImportError as e:
   if e.name!='extended':raise
 keep={i['file'] for i in data}
 for old in previous:
  if old['file'] not in keep and old['file'].startswith('icons/'):(ROOT/old['file']).unlink(missing_ok=True)
 from collections import Counter
 manifest={'counts':dict(Counter(i['kind'] for i in data)),'categories':dict(Counter(i['category'] for i in data)),'sourceReferences':REFERENCES,'version':'1.0.0','viewBox':'0 0 32 32','license':'MIT','count':len(data),'icons':data}
 (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+'\n')
 (ROOT/'catalog.js').write_text('window.CAX_CATALOG='+json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+';\n')
 print(f'Built {len(data)} icons')
if __name__=='__main__':build()
