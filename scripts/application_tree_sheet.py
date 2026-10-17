#!/usr/bin/env python3
"""Native-size integration specimen for the additional command families.

This is an illustrative consuming UI, not a vendor UI screenshot. Operations
that do not define a persistent node are deliberately absent from these trees.
"""
import json, re
from html import escape
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ICONS={i['id']:i for i in json.loads((ROOT/'manifest.json').read_text())['icons']}
TREES=[('CAD / fabricated components',[
 (0,'cad-assembly','Frame assembly'),
 (1,'cad-part','Folded bracket'),
 (2,'cad-convert-sheet-metal','Sheet-metal conversion'),
 (2,'cad-sheet-metal-hem','Hem.1'),
 (2,'cad-sheet-metal-jog','Jog.1'),
 (2,'cad-sheet-metal-form-tool','Formed feature.1'),
 (2,'cad-sheet-metal-corner-relief','Corner relief.1'),
 (2,'cad-sheet-metal-tab-slot','Tab and slot.1'),
 (1,'cad-part','Welded frame'),
 (2,'cad-weldment-member','Structural member.1'),
 (2,'cad-weldment-member','Structural member.2'),
 (2,'cad-weldment-trim-extend','Member end treatment.1'),
 (2,'cad-weldment-end-cap','End cap.1'),
 (2,'cad-weldment-gusset','Gusset.1'),
 (2,'cad-weld-bead','Weld bead definition.1'),
 (1,'cad-part','Mold tooling'),
 (2,'cad-mold-parting-line','Parting line.1'),
 (2,'cad-mold-tooling-split','Tooling split.1'),
 (2,'cad-solid-body','Core body'),
 (2,'cad-solid-body','Cavity body'),
]),('CAD / representations & drawing',[
 (0,'common-folder','Scan-derived model'),
 (1,'cmm-point-cloud','Measured point cloud'),
 (1,'cad-mesh-body','Reconstructed surface mesh'),
 (2,'cad-mesh-remesh','Remesh modifier'),
 (2,'cad-mesh-shrinkwrap','Shrinkwrap modifier'),
 (1,'cad-solid-body','Converted solid body'),
 (0,'common-folder','Routing assembly'),
 (1,'cad-part','Connector A'),
 (1,'cad-part','Connector B'),
 (1,'cad-auto-route','Routed connection'),
 (0,'common-folder','Drawing definitions'),
 (1,'cad-create-block','Block: mounting detail'),
 (2,'common-layers','Layer: outlines'),
 (2,'cad-drawing-hatch','Hatch.1'),
 (1,'cad-create-block','Block: fabrication section'),
 (2,'cad-drawing-hatch','Hatch.2'),
 (0,'common-folder','Shared object symbols'),
 (1,'cad-part','Bracket:1 [placed instance]'),
 (1,'cad-part','Bracket:2 [same SVG]'),
 (1,'cad-mesh-body','Processed mesh [same SVG]'),
]),('CAE / persistent analysis objects',[
 (0,'cae-harmonic-response','Harmonic-response study'),
 (1,'cae-solver-settings','Analysis settings'),
 (1,'cad-solid-body','Structure'),
 (2,'cae-material-assignment','Orthotropic material'),
 (2,'cae-composite-layup','Composite layup'),
 (1,'cae-tetrahedral-mesh','Finite-element mesh'),
 (2,'cae-mesh-refinement','Local refinement'),
 (1,'common-folder','Connections'),
 (2,'cae-rigid-connection','Rigid connection.1'),
 (2,'cae-spring-connection','Spring connection.1'),
 (2,'cae-contact-pair','Contact pair.1'),
 (1,'cae-coupling-interface','Coupling interface'),
 (1,'cae-named-selection','Named selection / interface'),
 (1,'common-folder','Conditions'),
 (2,'cae-fixed-support','Fixed support'),
 (2,'cae-force-load','Excitation force'),
 (2,'cae-gravity-load','Gravity'),
 (1,'common-folder','Results'),
 (2,'cae-result-plot','Frequency-response plot'),
 (2,'cae-deformation-result','Deformation'),
])]
width=1200;height=676
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="1200" height="676" fill="#f4f7f5"/><text x="24" y="34" font-family="sans-serif" font-size="21" fill="#253b53">CAX / additional application families in model trees</text><text x="24" y="59" font-family="sans-serif" font-size="12" fill="#526f68">Native 16 px · 24 px rows · commands and persistent nodes reuse the same SVG · illustrative hierarchy</text>']
for col,(title,rows) in enumerate(TREES):
 x=18+col*395
 parts.append(f'<rect x="{x}" y="80" width="382" height="538" rx="9" fill="white" stroke="#d8e2dc"/><text x="{x+14}" y="108" font-family="sans-serif" font-size="15" fill="#253b53">{escape(title)}</text>')
 for n,(depth,id,label) in enumerate(rows):
  i=ICONS[id];y=127+n*24;ix=x+15+depth*17
  assert 'model-tree' in i['usages'],id
  if n%2:parts.append(f'<rect x="{x+1}" y="{y-3}" width="380" height="24" fill="#f7f9f7"/>')
  if depth:parts.append(f'<path d="M{ix-10} {y-4} V{y+8} H{ix-4}" stroke="#c4d1cb" fill="none"/>')
  prefix=f'advanced-{col}-{n}-'
  body=re.sub(r'id="([^"]+)"',lambda m:f'id="{prefix}{m[1]}"',i['body'])
  body=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{prefix}{m[1]})',body)
  parts.append(f'<svg x="{ix}" y="{y}" width="16" height="16" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{body}</svg><text x="{ix+23}" y="{y+12}" font-family="sans-serif" font-size="12" fill="#253b53">{escape(label)}</text>')
parts.append('<text x="24" y="644" font-family="sans-serif" font-size="12" fill="#526f68">The same part/mesh/hatch symbols are reused for repeated objects. Editing commands need not become persistent nodes.</text><text x="24" y="663" font-family="sans-serif" font-size="11" fill="#526f68">Node names describe stored objects, not actions. No selected/hidden/error state variants are generated.</text></svg>')
(ROOT/'qa/application-model-tree.svg').write_text(''.join(parts))
print(f'Built additional model-tree specimen with {sum(len(rows) for _,rows in TREES)} native 16px rows')
