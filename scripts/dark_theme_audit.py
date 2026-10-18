#!/usr/bin/env python3
"""Render actual standalone file bytes as independent SVG images without CSS.

The native-size atlas includes all 419 files in each theme at 16/24/32 px.
Three dark-surface composites and a selected before/after comparison are derived
from those raw files. These are static Inkscape renders, not browser screenshots.
"""
import base64, hashlib, json, math, subprocess, sys
from html import escape
from pathlib import Path
from PIL import Image, ImageColor
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from themes import THEMES
M=json.loads((ROOT/'manifest.json').read_text()); items=M['icons']
SIZES=(16,24,32); SURFACES=tuple(dict.fromkeys((THEMES['dark']['surface'],'#23262b','#121212')))
COLS=32; CELL=48; ROWS=math.ceil(len(items)/COLS)
TMP=ROOT/'qa/dark-render';TMP.mkdir(exist_ok=True)

def raw_image(item,theme,x,y,size):
    content=(ROOT/item['variants'][theme]['file']).read_bytes()
    encoded=base64.b64encode(content).decode()
    return f'<image x="{x}" y="{y}" width="{size}" height="{size}" href="data:image/svg+xml;base64,{encoded}"/>'

def render(svg,png):
    subprocess.run(['inkscape',str(svg),'--export-type=png','--export-filename='+str(png)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

def linear(v):
    v=v/255;return v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4

def lum(rgb):return sum(linear(v)*w for v,w in zip(rgb,(.2126,.7152,.0722)))
def contrast(a,b):
    lo,hi=sorted((lum(ImageColor.getrgb(a)),lum(ImageColor.getrgb(b))))
    return round((hi+.05)/(lo+.05),2)

atlases={};raw_hashes={}
for theme in ('light','dark'):
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{COLS*CELL}" height="{ROWS*CELL*len(SIZES)}">']
    for band,size in enumerate(SIZES):
        for n,item in enumerate(items):
            x=(n%COLS)*CELL+(CELL-size)//2;y=(band*ROWS+n//COLS)*CELL+(CELL-size)//2
            parts.append(raw_image(item,theme,x,y,size))
    parts.append('</svg>');svg=TMP/f'{theme}-native.svg';png=TMP/f'{theme}-native.png'
    svg.write_text(''.join(parts));render(svg,png);atlases[theme]=Image.open(png).convert('RGBA')
    raw_hashes[theme]={i['id']:hashlib.sha256((ROOT/i['variants'][theme]['file']).read_bytes()).hexdigest() for i in items}
    print(f'Rendered {len(items)} standalone {theme} files at {SIZES}',flush=True)
blank=[];alpha_mismatch=[];low_contrast=[]
for band,size in enumerate(SIZES):
    for n,item in enumerate(items):
        x=n%COLS*CELL;y=(band*ROWS+n//COLS)*CELL
        crops={theme:im.crop((x,y,x+CELL,y+CELL)) for theme,im in atlases.items()}
        for theme,crop in crops.items():
            if not crop.getchannel('A').getbbox():blank.append([item['id'],theme,size])
        if crops['light'].getchannel('A').tobytes()!=crops['dark'].getchannel('A').tobytes():alpha_mismatch.append([item['id'],size])
        # At least eight native pixels of meaningful contrast, rather than
        # counting the solid background or nearly invisible antialias fringes.
        for surface in SURFACES:
            bg=Image.new('RGBA',crops['dark'].size,surface);rgb=Image.alpha_composite(bg,crops['dark']).convert('RGB')
            bg_lum=lum(ImageColor.getrgb(surface));visible=0
            for pixel in getattr(rgb,'get_flattened_data',rgb.getdata)():
                lo,hi=sorted((lum(pixel),bg_lum))
                if (hi+.05)/(lo+.05)>=3:visible+=1
            if visible<8:low_contrast.append([item['id'],size,surface,visible])
for surface in SURFACES:
    out=Image.alpha_composite(Image.new('RGBA',atlases['dark'].size,surface),atlases['dark'])
    out.save(TMP/f'dark-on-{surface[1:]}.png')

# A readable all-symbol sheet per category, built from the raw dark SVGs.
for category in M['categories']:
    subset=[i for i in items if i['category']==category];cols=6;w=220;h=150;rows=math.ceil(len(subset)/cols)
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{cols*w}" height="{rows*h+65}"><rect width="100%" height="100%" fill="#f4f7f5"/><g font-family="sans-serif"><text x="18" y="28" font-size="20" fill="#253b53">{category} · {len(subset)} standalone dark SVGs</text><text x="18" y="49" font-size="12" fill="#45665f">Native 16 / 24 / 32 px · each row: #192c3c, #23262b, #121212 · no CSS recoloring</text>']
    for n,item in enumerate(subset):
        x=n%cols*w;y=65+n//cols*h
        parts.append(f'<text x="{x+8}" y="{y+13}" font-size="9" fill="#253b53">{escape(item["id"])}</text>')
        for row,surface in enumerate(SURFACES):
            yy=y+21+row*40
            parts.append(f'<rect x="{x+6}" y="{yy}" width="{w-12}" height="38" rx="4" fill="{surface}"/>')
            for size,dx in zip(SIZES,(24,84,151)):parts.append(raw_image(item,'dark',x+dx,yy+(38-size)//2,size))
    parts.append('</g></svg>');svg=ROOT/f'qa/dark-{category.lower()}.svg';png=svg.with_suffix('.png');svg.write_text(''.join(parts));render(svg,png)
    print(f'Wrote {category} raw-file three-surface sheet',flush=True)

selected=['common-info','common-save-all','cad-extrude','cad-shell','cam-swarf-milling','cae-hexahedral-mesh','cmm-measure-circle','olp-swept-volume','olp-singularity-check','cae-local-wall-offset','cae-sink-tendency','cae-analysis-report']
by_id={i['id']:i for i in items};width=1470;height=140+len(selected)*88
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"><rect width="100%" height="100%" fill="#f4f7f5"/><g font-family="sans-serif"><text x="24" y="34" font-size="25" fill="#253b53">Standalone dark SVGs · 419 meanings, two file variants each</text><text x="24" y="59" font-size="13" fill="#45665f">Actual SVG file bytes, no CSS · native 16 / 24 / 32 px in each cell · original files preserved byte-for-byte</text><text x="24" y="82" font-size="12" fill="#45665f">Opaque cutouts stay #192c3c to preserve hidden edges; their fixed color is visible on other surfaces.</text>']
columns=[('Original / white','light','#ffffff'),('Original / Studio dark','light','#23262b'),('Dark / Studio dark','dark','#23262b'),('Dark / matching surface','dark','#192c3c'),('Dark / neutral dark','dark','#121212')]
for col,(label,theme,surface) in enumerate(columns):
    x=300+col*232;parts.append(f'<text x="{x+7}" y="113" font-size="12" fill="#253b53">{label}</text>')
for row,id in enumerate(selected):
    item=by_id[id];y=126+row*88;parts.append(f'<text x="24" y="{y+36}" font-size="12" fill="#253b53">{id}</text>')
    for col,(label,theme,surface) in enumerate(columns):
        x=300+col*232;parts.append(f'<rect x="{x}" y="{y}" width="222" height="76" rx="7" fill="{surface}" stroke="#acb8b4"/>')
        for size,dx in zip(SIZES,(25,90,160)):parts.append(raw_image(item,theme,x+dx,y+(76-size)//2,size))
parts.append('</g></svg>');svg=ROOT/'qa/dark-svg-comparison.svg';svg.write_text(''.join(parts));render(svg,svg.with_suffix('.png'))
p=THEMES['dark']['palette']
report={'method':'Actual standalone SVG bytes embedded as independent images and rendered by Inkscape; no host CSS, not a browser test','semanticCount':len(items),'filesPerTheme':len(items),'themes':['light','dark'],'sizes':list(SIZES),'darkSurfaces':list(SURFACES),'renders':len(items)*len(SIZES)*2,'darkSurfaceChecks':len(items)*len(SIZES)*len(SURFACES),'blank':blank,'alphaMismatch':alpha_mismatch,'fewerThanEight3to1Pixels':low_contrast,'opaqueCutoutColor':p['cutout'],'opaqueCutoutIcons':sum('fill="white"' in i['body'] for i in items),'contrast':{**{f'{role}_on_{surface}':contrast(p[role],surface) for role in ('ink','accent','warning') for surface in SURFACES},'ink_on_body':contrast(p['ink'],p['body']),'accent_on_body':contrast(p['accent'],p['body']),'warning_on_warningBody':contrast(p['warning'],p['warningBody'])},'inputHash':hashlib.sha256(json.dumps(raw_hashes,sort_keys=True).encode()).hexdigest()}
(ROOT/'qa/dark-theme-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)
if blank or alpha_mismatch or low_contrast:raise SystemExit(1)
