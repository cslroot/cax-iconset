#!/usr/bin/env python3
"""Actual-render bounds and raster-duplicate audit using installed Inkscape.

The atlas intentionally does NOT clip each icon to its 32 px viewBox, allowing
paint outside the nominal viewport to be detected. It is rendered at 2x.
"""
import json,subprocess,hashlib,collections,re
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'manifest.json').read_text())['icons']
COLS=64;CELL=48;SCALE=2
rows=(len(items)+COLS-1)//COLS
head=f'<svg xmlns="http://www.w3.org/2000/svg" width="{COLS*CELL*SCALE}" height="{rows*CELL*SCALE}" viewBox="0 0 {COLS*CELL} {rows*CELL}">'
parts=[head]
for n,i in enumerate(items):
 x=(n%COLS)*CELL+8;y=(n//COLS)*CELL+8
 body=i['body']
 # Color-independent render: keep white cutouts, normalize all accent colors.
 body=re.sub(r'#[0-9a-fA-F]{3,8}',lambda m:'#ddd' if m.group(0).lower() in ['#d7efed','#fff3da'] else '#222',body)
 parts.append(f'<g transform="translate({x} {y})" fill="none" stroke="#222" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{body}</g>')
parts.append('</svg>');svg=ROOT/'qa/raster-atlas.svg';png=ROOT/'qa/raster-atlas.png';svg.write_text(''.join(parts))
subprocess.run(['inkscape',str(svg),'--export-type=png','--export-filename='+str(png)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
im=Image.open(png).convert('RGBA');over=[];empty=[];hashes=collections.defaultdict(list)
for n,i in enumerate(items):
 x=(n%COLS)*CELL*SCALE;y=(n//COLS)*CELL*SCALE
 crop=im.crop((x,y,x+CELL*SCALE,y+CELL*SCALE));a=crop.getchannel('A');box=a.point(lambda x:255 if x>10 else 0).getbbox()
 if not box:empty.append(i['id']);continue
 if box[0]<8*SCALE or box[1]<8*SCALE or box[2]>40*SCALE or box[3]>40*SCALE:over.append({'id':i['id'],'bounds':box})
 hashes[hashlib.sha256(crop.tobytes()).hexdigest()].append(i['id'])
result={'rendered':len(items),'render_scale':SCALE,'empty':empty,'paint_outside_viewbox':over,'identical_raster_groups':[v for v in hashes.values() if len(v)>1]}
(ROOT/'qa/raster-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if result['empty'] or result['paint_outside_viewbox'] or result['identical_raster_groups']:
 raise SystemExit(1)
