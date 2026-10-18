#!/usr/bin/env python3
"""Static SVG theme QA using the production CSS palette, not a browser test."""
import json, re, argparse
from pathlib import Path
from html import escape
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--pdxadv',action='store_true',help='Render the nine pdxadv workflow additions')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]
css=(ROOT/'styles.css').read_text()
adapter=css.split('/* Preview-only dark palette.',1)[1]
palette={(kind,old):new for kind,old,new in re.findall(r'svg \[(fill|stroke)="([^"]+)"\] \{(?:fill|stroke):([^}]+)\}',adapter)}
ink=re.search(r'\.detail-preview\.dark-bg>svg \{stroke:([^}]+)\}',adapter)[1]
bg=re.search(r'\.detail-preview\.dark-bg\{background:([^}]+)\}',css)[1]
items={i['id']:i for i in json.loads((ROOT/'manifest.json').read_text())['icons']}
reviewed=json.loads((ROOT/'src/quality_review.json').read_text())
new=json.loads((ROOT/'src/studio_commands.json').read_text())
ids=list(dict.fromkeys(['common-info','common-save-all','olp-swept-volume','olp-singularity-check']+[i['id'] for i in reviewed+new]))
if args.pdxadv:
    ids=[i['id'] for i in json.loads((ROOT/'src/pdxadv_commands.json').read_text())]
name='pdxadv-themes' if args.pdxadv else 'theme-preview'
title='CAX / pdxadv workflow: light, dark and checker' if args.pdxadv else 'CAX / light, dark and checker palette'
width=1200; height=100+len(ids)*102
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><defs><pattern id="checker" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="white"/><path d="M0 0H7V7H0Z M7 7H14V14H7Z" fill="#eff3ef"/></pattern></defs><rect width="100%" height="100%" fill="#f5f8f5"/><g font-family="sans-serif"><text x="22" y="34" font-size="23" fill="#253b53">{title}</text><text x="22" y="60" font-size="13" fill="#45665f">48 / 24 / 16 px · production CSS color mapping · static SVG rendering, not browser verification</text>']
for n,id in enumerate(ids):
    item=items[id];y=80+n*102
    parts.append(f'<text x="22" y="{y+20}" font-size="12" fill="#253b53">{escape(id)}</text>')
    for theme,x,color in [('Light',380,'white'),('Dark',645,bg),('Checker',910,'url(#checker)')]:
        parts.append(f'<rect x="{x}" y="{y}" width="250" height="90" rx="8" fill="{color}" stroke="#7e8b95"/><text x="{x+10}" y="{y+15}" font-size="10" fill="{ink if theme=="Dark" else "#45665f"}">{theme}</text>')
        body=item['body']
        if theme=='Dark':
            body=re.sub(r'(fill|stroke)="([^"]+)"',lambda m:f'{m[1]}="{palette.get((m[1],m[2]),m[2])}"',body)
        for size,dx in [(48,20),(24,105),(16,180)]:
            prefix=f'theme-{n}-{theme}-{size}-'
            unique=re.sub(r'id="([^"]+)"',lambda m:f'id="{prefix}{m[1]}"',body)
            unique=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{prefix}{m[1]})',unique)
            parts.append(f'<svg x="{x+dx}" y="{y+26+(48-size)/2}" width="{size}" height="{size}" viewBox="0 0 32 32" fill="none" stroke="{ink if theme=="Dark" else "#253b53"}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{unique}</svg>')
parts.append('</g></svg>');(ROOT/f'qa/{name}.svg').write_text(''.join(parts))
def luminance(color):
    rgb=[int(color[i:i+2],16)/255 for i in [1,3,5]]
    rgb=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in rgb]
    return sum(v*w for v,w in zip(rgb,[.2126,.7152,.0722]))
def contrast(a,b):
    a,b=sorted([luminance(a),luminance(b)])
    return round((b+.05)/(a+.05),2)
body=palette[('fill','#d7efed')]; accent=palette[('stroke','#178b88')]
report={'method':'Static color-role contrast from production CSS; not browser computed-style or accessibility certification','examples':len(ids),'sizes':[48,24,16],'darkPalette':{'background':bg,'ink':ink,'body':body,'accent':accent},'contrast':{'ink_on_body':contrast(ink,body),'accent_on_body':contrast(accent,body),'ink_on_background':contrast(ink,bg),'accent_on_background':contrast(accent,bg)},'opaqueCutoutPreserved':palette.get(('fill','white'))==bg}
assert min(report['contrast'].values())>=3
(ROOT/f'qa/{"pdxadv-theme-audit" if args.pdxadv else "theme-audit"}.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
