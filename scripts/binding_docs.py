#!/usr/bin/env python3
"""Document conditional command bindings without claiming consumer deployment."""
import json,collections,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=json.loads((R/'command-bindings.json').read_text());m=json.loads((R/'manifest.json').read_text());b=json.loads((R/'src/published693_baseline.json').read_text())['icons'];trace=json.loads((R/'src/binding_art_trace.json').read_text());new=[i for i in m['icons'] if i['id'] in trace]
counts=collections.Counter(r['outcome'] for r in p['bindings']);unknown=[r for r in p['bindings'] if r['outcome']=='unresolved']
lines=['# Conditional GUI binding review','',f'This review covers exactly the 180 uncertain rows in the frozen 1,089-row source audit. It adds {len(new)} independently reviewed original glyphs to the published 693-icon baseline; the catalog now has {m["count"]} semantic entries. All 693 previous records and both SVG variants are unchanged.','',
'## What these results mean','',
'- `direct`: an existing glyph directly describes the command meaning.','- `conditional-reuse`: artwork is usable only under the explicit context, label, state and routing requirements. This is not standalone icon-only equivalence.','- `new-art`: new original artwork supplies a missing meaning; command-specific conditions still apply.','- `unresolved`: at least one source-level branch remains unverified, even where some branches now have artwork.','- No row verifies an implemented consumer GUI. The JSON is a declarative integration contract, not executable dispatch logic. Do not infer success, permissions, network upload, a solver run or transaction completion from a glyph.','',
'## Row outcomes','']
lines += [f'- {k}: {v}' for k,v in sorted(counts.items())]
lines += ['','The original audit statuses are preserved. See [machine-readable policy](../command-bindings.json) and [sortable resolution table](GUI_BINDING_RESOLUTIONS.csv).','',
'## Source and interpretation corrections','',
'- SOLIDWORKS Mate uses its documented standard/advanced/mechanical relation taxonomy, not SolidCraft’s joint-type menu.','- Selection filters restrict pick eligibility; they do not hide matching display objects. Labels and selected states are mandatory.','- Cosmetic threads do not create modeled threads. Lightweight weld graphics are not modeled weld solids.','- Motion Trace samples positions without modifying the design; Keep Motion Trace creates persistent geometry.','- Universal Joint reuses crossed-yoke artwork only with the documented coupled input/output shaft motion.','- Mates in path to ground is a discrete graph status, not a creation command and not removed from the audit denominator.','- Current and older official documentation versions remain identified in each row’s source URLs. No broader product/add-in/menu coverage is claimed.','',
'## Genuine remaining source limits','']
for r in unknown:
 lines += [f'### {r["product"]}: {r["command"]}','',r['reason'],'']+[f'- {x}' for x in r['remaining_unknown']]+['']
lines+=['## New original glyphs','','| ID | English / 日本語 | Meaning |','| --- | --- | --- |']
for i in new:lines.append(f'| {i["id"]} | {i["name"]} / {i["nameJa"]} | {i["description"]} |')
lines += ['','## Validation and delivery','',
'Full catalog and binding tests pin all published 693 records/SVG hashes, require all 180 rows exactly once, validate IDs and sources, and trace every new glyph to a binding. XML, geometry duplication, native light/dark rendering, clipping, contrast, PNG export and application/ZIP regressions are rerun after integration. Native preview sheets and raw validation outputs are in the complete delivery package; they are not proof of browser or assistive-technology integration.','',
'This follow-on unit preserves the previously published 693-icon commit as its baseline. Consult repository history for the publication state of this revision.','']
(R/'docs/GUI_BINDINGS.md').write_text('\n'.join(lines))
readme=R/'README.md';s=readme.read_text();block=f'''<!-- binding-review:start -->
## Conditional GUI binding review (2026-10-25)

{len(new)} additional original glyphs support the reviewed command bindings. Current catalog: **{m['count']} semantic icons / {2*m['count']} theme SVGs**. The published 693-icon baseline is unchanged.

See [conditions, evidence and unresolved branches](docs/GUI_BINDINGS.md), [binding JSON](command-bindings.json) and [180-row resolution CSV](docs/GUI_BINDING_RESOLUTIONS.csv). Conditional reuse does not mean a consumer GUI has implemented the required labels, states or routing.
<!-- binding-review:end -->'''
if '<!-- binding-review:start -->' in s:s=re.sub(r'<!-- binding-review:start -->.*?<!-- binding-review:end -->',block,s,flags=re.S)
else:s=s.replace('# CAX Iconset','# CAX Iconset\n\n'+block,1)
readme.write_text(s)
print(dict(counts),len(new),'new glyphs')
