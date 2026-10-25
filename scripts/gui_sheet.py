#!/usr/bin/env python3
"""Native-size exports of the new GUI symbols, not resized 32px pictures."""
import json,subprocess,tempfile
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'manifest.json').read_text())
import sys
sys.path.insert(0,str(ROOT/'src'))
from gui_features import ITEMS as first_features
from gui_sketch import ITEMS as first_sketch
from gui_surface import ITEMS as first_surface
first_ids={'cad-'+i['id'] for i in first_features+first_sketch+first_surface}
items=[i for i in m['icons'] if i['id'] in first_ids]
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
W=1200; row=100; cols=3; H=60+((len(items)+cols-1)//cols)*row
im=Image.new('RGB',(W,H),'#eef3f5');draw=ImageDraw.Draw(im)
draw.text((20,12),'CAX GUI additions | native 16 / 24 / 32 px | light and dark',font=font,fill='#253b53')
with tempfile.TemporaryDirectory() as tmp:
 actions=[]
 for n,item in enumerate(items):
  for theme in ['light','dark']:
   for size in [16,24,32]:
    path=Path(tmp)/f'{n}-{theme}-{size}.png'
    actions.append(f'file-open:{ROOT/item["variants"][theme]["file"]};export-filename:{path};export-width:{size};export-height:{size};export-do;file-close')
 subprocess.run(['inkscape','--shell'],input='\n'.join(actions)+'\n',text=True,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 for n,item in enumerate(items):
  x=(n%cols)*400;y=50+(n//cols)*row
  draw.text((x+12,y),item['name'],font=font,fill='#253b53')
  for j,theme in enumerate(['light','dark']):
   bx=x+12+j*184;by=y+22
   draw.rectangle((bx,by,bx+174,by+60),fill='white' if theme=='light' else '#192c3c')
   for k,size in enumerate([16,24,32]):
    icon=Image.open(Path(tmp)/f'{n}-{theme}-{size}.png').convert('RGBA')
    im.paste(icon,(bx+12+k*52,by+12+(32-size)//2),icon)
 out=ROOT/'qa/gui-additions.png';im.save(out)
print(out)
