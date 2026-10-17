#!/usr/bin/env python3
"""Illustrative CAD/CAM/CAE hierarchy with real 16px icons, not enlarged glyphs.

This is a static integration specimen, not a screenshot of an application or an
assertion that different products expose identical hierarchies. Instance, feature
and condition reuse is visible; status is an independent adjacent symbol.
"""
import json,re
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'manifest.json').read_text())
ICONS={i['id']:i for i in M['icons']}
TREES=[('CAD / design & topology',[
 (0,'cad-assembly','Drive assembly'),
 (1,'cad-part','Housing:1  [component instance]'),
 (2,'cad-solid-body','Solid body'),
 (3,'cad-sketch','Sketch.1'),
 (3,'cad-extrude','Extrude.1'),
 (3,'cad-hole','Hole.1'),
 (3,'cad-thread','Thread.1'),
 (3,'cad-face','Face[12]  [topology selection]'),
 (2,'cae-material-assignment','Aluminum 6061'),
 (1,'cad-part','Bracket:1  [same part symbol]'),
 (2,'cad-solid-body','Solid body'),
 (3,'cad-rib','Rib.1'),
 (3,'cad-fillet','Fillet.1'),
 (1,'cad-part','Bracket:2  [placed occurrence]'),
 (1,'common-folder','Reference geometry'),
 (2,'olp-reference-frame','Origin'),
 (2,'cad-datum-plane','Datum plane'),
 (2,'cad-surface-patch','Surface body'),
 (2,'cad-mesh-body','Imported mesh body'),
 (2,'cmm-point-cloud','Scan points'),
]),('CAM / machining sequence',[
 (0,'cam-setup','Setup 1  [machining job]'),
 (1,'cam-stock-setup','Stock'),
 (1,'cam-work-coordinate-system','WCS / G54'),
 (1,'cam-fixture-clamp','Fixture'),
 (1,'common-folder','Tools'),
 (2,'cam-end-mill','T1 / flat end mill'),
 (2,'cam-ball-end-mill','T2 / ball end mill'),
 (1,'common-folder','Operations'),
 (2,'cam-face-milling','Face.1'),
 (2,'cam-adaptive-clearing','Adaptive.1'),
 (2,'cam-contour-milling','Contour.1'),
 (3,'cam-holding-tabs','Holding tabs'),
 (2,'cam-drilling','Drill.1'),
 (2,'cam-tapping','Tap.1'),
 (2,'cam-thread-milling','Thread mill.1'),
 (2,'cam-engrave','Engrave.1'),
 (2,'cam-deburr','Deburr.1'),
 (1,'cam-post-process','NC program 1001'),
]),('CAE / analysis objects',[
 (0,'cae-new-study','Study 1'),
 (1,'cae-solver-settings','Analysis settings'),
 (1,'cad-solid-body','Body'),
 (2,'cae-material-assignment','Steel'),
 (1,'cae-named-selection','Named selection / inlet faces'),
 (1,'cae-tetrahedral-mesh','Tetrahedral mesh'),
 (2,'cae-mesh-refinement','Local refinement'),
 (2,'cae-boundary-layer-mesh','Boundary-layer control'),
 (1,'cae-contact-pair','Contact pair'),
 (1,'common-folder','Conditions'),
 (2,'cae-fixed-support','Fixed support'),
 (2,'cae-gravity-load','Gravity'),
 (2,'cae-moment-load','Moment'),
 (2,'cae-symmetry-boundary','Symmetry'),
 (2,'cae-fluid-inlet','Fluid inlet'),
 (2,'cae-fluid-outlet','Fluid outlet'),
 (2,'cae-wall-boundary','Wall'),
 (1,'common-folder','Results'),
 (2,'cae-stress-contour','Stress contour'),
 (2,'cae-streamline-result','Streamlines'),
])]
WIDTH=1200;HEIGHT=676
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}"><rect width="1200" height="676" fill="#f4f7f5"/><text x="24" y="34" font-family="sans-serif" font-size="21" fill="#253b53">CAX / model-tree integration specimen</text><text x="24" y="59" font-family="sans-serif" font-size="12" fill="#526f68">Native 16 px icons · 24 px rows · repeated instances reuse one SVG · illustrative cross-product hierarchy</text>']
for col,(title,rows) in enumerate(TREES):
 x=18+col*395
 parts.append(f'<rect x="{x}" y="80" width="382" height="538" rx="9" fill="white" stroke="#d8e2dc"/><text x="{x+14}" y="108" font-family="sans-serif" font-size="15" fill="#253b53">{escape(title)}</text>')
 for n,(depth,id,label) in enumerate(rows):
  i=ICONS[id];y=127+n*24;ix=x+15+depth*17
  assert 'model-tree' in i['usages'],id
  if n%2==1: parts.append(f'<rect x="{x+1}" y="{y-3}" width="380" height="24" fill="#f7f9f7"/>')
  if depth:parts.append(f'<path d="M{ix-10} {y-4} V{y+8} H{ix-4}" stroke="#c4d1cb" fill="none"/>')
  prefix=f'tree-{col}-{n}-';body=re.sub(r'id="([^"]+)"',lambda m:f'id="{prefix}{m[1]}"',i['body']);body=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{prefix}{m[1]})',body)
  parts.append(f'<svg x="{ix}" y="{y}" width="16" height="16" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{body}</svg><text x="{ix+23}" y="{y+12}" font-family="sans-serif" font-size="12" fill="#253b53">{escape(label)}</text>')
parts.append('<text x="24" y="644" font-family="sans-serif" font-size="12" fill="#526f68">Feature/operation/condition nodes reuse the command artwork. Part definitions and occurrences share a symbol.</text><text x="24" y="663" font-family="sans-serif" font-size="11" fill="#526f68">Face is a topology-selection example. No selected/hidden/error × object variants are generated. Check final app contrast and accessibility.</text></svg>')
(ROOT/'qa/model-tree.svg').write_text(''.join(parts))
print('Built CAD/CAM/CAE model-tree specimen with '+str(sum(len(rows) for _,rows in TREES))+' native 16px rows')
