#!/usr/bin/env python3
"""Paged native 16/24/32px light/dark previews of the coverage additions."""
import json,subprocess,tempfile,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'manifest.json').read_text())
baseline=json.loads((ROOT/'src/published693_baseline.json').read_text())['icons']
items=[i for i in m['icons'] if i['id'] not in baseline]
out=ROOT/'qa/binding-preview';out.mkdir(exist_ok=True)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
W=1200;row=100;cols=3;per_page=24
with tempfile.TemporaryDirectory() as tmp:
 actions=[]
 for n,item in enumerate(items):
  for theme in ['light','dark']:
   for size in [16,24,32]:
    path=Path(tmp)/f'{n}-{theme}-{size}.png'
    actions.append(f'file-open:{ROOT/item["variants"][theme]["file"]};export-filename:{path};export-width:{size};export-height:{size};export-do;file-close')
 subprocess.run(['inkscape','--shell'],input='\n'.join(actions)+'\n',text=True,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 pages=[]
 for page in range(math.ceil(len(items)/per_page)):
  chunk=items[page*per_page:(page+1)*per_page];H=60+math.ceil(len(chunk)/cols)*row
  im=Image.new('RGB',(W,H),'#eef3f5');draw=ImageDraw.Draw(im)
  draw.text((20,12),f'CAX binding additions {page+1} | native 16 / 24 / 32 px | light and dark',font=font,fill='#253b53')
  for n,item in enumerate(chunk):
   number=page*per_page+n;x=(n%cols)*400;y=50+(n//cols)*row
   draw.text((x+12,y),item['name'],font=font,fill='#253b53')
   for j,theme in enumerate(['light','dark']):
    bx=x+12+j*184;by=y+22;draw.rectangle((bx,by,bx+174,by+60),fill='white' if theme=='light' else '#192c3c')
    for k,size in enumerate([16,24,32]):
     icon=Image.open(Path(tmp)/f'{number}-{theme}-{size}.png').convert('RGBA');im.paste(icon,(bx+12+k*52,by+12+(32-size)//2),icon)
  file=out/f'page-{page+1:02}.png';im.save(file);pages.append(str(file.relative_to(ROOT)))
 (out/'pages.json').write_text(json.dumps(pages,indent=2)+'\n')
print(f'{len(items)} new meanings across {len(pages)} preview pages')
