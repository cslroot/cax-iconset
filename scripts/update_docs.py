#!/usr/bin/env python3
"""Refresh count/reference blocks without treating the counts as scope targets."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'manifest.json').read_text())
coverage='\n| Primary category | Symbols |\n| --- | ---: |\n'+''.join(f'| {c} | {n} |\n' for c,n in m['categories'].items())+f'| **Total** | **{m["count"]}** |\n\n'
coverage+=f'Primary roles: {m["counts"]["command"]} commands, {m["counts"]["tool"]} selectable tools, {m["counts"]["object"]} objects and {m["counts"]["status"]} status symbols. Every SVG is counted once.\n\n'
coverage+=f'{m["usageCounts"]["model-tree"]} entries support model-tree use, including reused command/tool symbols; these are not additional SVGs.\n'
for file in ['README.md','docs/REFERENCE.md']:
 p=ROOT/file;s=p.read_text();s=re.sub(r'(?<=<!-- coverage:start -->).*?(?=<!-- coverage:end -->)',coverage,s,flags=re.S)
 if file=='docs/REFERENCE.md':
  refs='\n| Source | Primary documentation | Taxonomy |\n| --- | --- | --- |\n'+''.join(f'| {id} | [{v["title"]}]({v["url"]}) | {v["scope"]} |\n' for id,v in m['sourceReferences'].items())
  s=re.sub(r'(?<=<!-- references:start -->).*?(?=<!-- references:end -->)',refs,s,flags=re.S)
 p.write_text(s)
print('Refreshed coverage and primary-source documentation')

# Per-command evidence is generated from the same curated records as the SVGs.
records=json.loads((ROOT/'src/application_commands.json').read_text())
reused=json.loads((ROOT/'src/application_reuse.json').read_text())
by_id={i['id']:i for i in m['icons']}
from collections import Counter
counts=Counter(i['domain'] for i in records)
parts=[f'''# Additional application command families

Date: 2026-10-17. Baseline: `50ef1ff` (270 entries). This review adds **{len(records)} independently selected commands**, giving **{m['count']} unique SVGs**. The count follows the selected functions; it is not a target.

![Additional application commands](../qa/application-additions.png)

## Scope and selection

The added primary-category counts are {', '.join(f'{k} {v}' for k,v in counts.items())}. References cover Blender mesh editing, Rhino free-form surfaces, CloudCompare point-cloud processing, SOLIDWORKS sheet metal/weldments/mold tools/routing, Inkscape and QCAD drawing tools, Mastercam/PowerMill/LinuxCNC/SolidCAM manufacturing, SALOME/HyperMesh/Ansys/ParaView analysis, PC-DMIS inspection and RoboDK robotics.

All artwork is independently drawn on the existing 32 px grid. Documentation establishes command semantics; vendor icons are neither traced nor bundled. Historical and versioned references are labeled in the source metadata, without claiming those are current product versions. API, pricing and feature availability are outside this review.

## Reuse and rejected duplication

- Mesh vertex/node merging and smoothing each have one new SVG shared by CAD and CAE, with both application vocabularies and primary sources. There are no duplicate `cae-merge-nodes` or `cae-smooth-mesh` entries.
- Point-cloud outlier filtering, subsampling and surface reconstruction were found in both research streams and merged into one entry each. The same scan-processing entries can be filtered under CAD or CMM.
- Mesh bridge adds faces across a gap; mesh sewing matches existing borders and can insert corresponding nodes; merge by distance collapses coincident nodes. These have different topology effects. B-rep surface sewing remains its own existing command.
- Stock-model calculation produces remaining-stock data. Rest machining cuts residual stock. Constant-Z and pencil finishing are distinct documented machining strategies, not profile or path-shape variants invented to increase the count.
- The generic surface-patch drawing is reused for the geometric patch in a mold shut-off workflow. The host application must still supply core/cavity assignment and mold-specific controls; the patch icon does not claim to implement those controls. No separate shut-off SVG was added.
- Existing parallel finishing, swarf milling, mesh quality, streamlines and best-fit alignment gain application-specific aliases and references instead of synonym icons. ICP is covered by best-fit alignment; its description includes both nominal and reference geometry.
- A weld-bead node represents the documented weld definition/display; it does not claim to create solid weld geometry. Weldment gussets and integral ribs retain separate manufacturing meanings.
- Model-tree support reuses existing command geometry. No hidden/selected/suppressed/error × object variants, section-shape products or trajectory products are generated.

## Persistent model-tree use

{sum('modelTree' in i for i in records)} of the new commands also have reviewed persistent-node uses. Together with existing entries, **{m['usageCounts']['model-tree']}** symbols support model trees. Node names are nouns such as Formed feature, Composite layup and Harmonic-response study. Editing commands do not automatically become persistent nodes.

![Additional native-size model trees](../qa/application-model-tree.png)

This 60-row specimen uses native 16 px SVGs and 24 px rows. It is a cross-application integration illustration, not a vendor UI screenshot. Repeated part instances, processed meshes and drawing blocks reuse the same symbol.

## Per-function additions and evidence

The descriptions below state each actual operation. The source JSON also preserves the reviewed difference from existing functions.
''']
for category in counts:
 parts.append(f'\n### {category}\n\n| Semantic ID | English / Japanese | Purpose | Primary reference |\n| --- | --- | --- | --- |\n')
 for i in records:
  if i['domain']!=category:continue
  live=by_id[i['id']]
  refs='; '.join(f'[{m["sourceReferences"][s]["title"]}]({m["sourceReferences"][s]["url"]})' for s in live['sources'])
  parts.append(f'| `{i["id"]}` | {i["name"]} / {i["nameJa"]} | {i["description"]} | {refs} |\n')
parts.append('\n## Existing symbols with expanded vocabulary\n\n| Existing ID | Added search aliases | Primary reference |\n| --- | --- | --- |\n')
for i in reused:
 parts.append(f'| `{i["id"]}` | {", ".join(i["aliases"])} | [{i["sourceTitle"]}]({i["sourceUrl"]}) |\n')
parts.append('''
## Verification and limits

Independent application-family and manufacturing/analysis reviews found no blocking semantic or visual issues in the 48 / 24 / 16 px additions sheet. All SVGs pass XML safety, local-reference/hash integrity, normalized-geometry uniqueness and a color-normalized raster audit. The additional application aliases and shared-category/model-tree behavior have dedicated regression tests. See [the current QA report](QA.md).

These checks do not establish real-browser layout, native dialog focus/Escape, system clipboard or saved-download behavior. No deployment or CI configuration is added.
''')
(ROOT/'docs/APPLICATION_EXPANSION.md').write_text(''.join(parts))
print('Refreshed per-command application expansion review')
