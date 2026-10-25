#!/usr/bin/env python3
"""Refresh count/reference blocks without treating the counts as scope targets."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'manifest.json').read_text())
coverage='\n| Primary category | Symbols |\n| --- | ---: |\n'+''.join(f'| {c} | {n} |\n' for c,n in m['categories'].items())+f'| **Total** | **{m["count"]}** |\n\n'
coverage+=f'Primary roles: {m["counts"]["command"]} commands, {m["counts"]["tool"]} selectable tools, {m["counts"]["object"]} objects and {m["counts"]["status"]} status symbols. Every semantic icon is counted once; light/dark files are color variants of the same ID.\n\n'
coverage+=f'{m["usageCounts"]["model-tree"]} entries support model-tree use, including reused command/tool symbols; these are not additional semantic icons.\n'
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

Date: 2026-10-17. Baseline: `50ef1ff` (270 entries). This historical v2.2 review added **{len(records)} independently selected commands**, giving **{270+len(records)} unique SVGs** at that checkpoint. The count follows the selected functions; it is not a target. Later robotics work is documented separately in [ROBOTICS_EXPANSION.md](ROBOTICS_EXPANSION.md).

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

{sum('modelTree' in i for i in records)} of the new commands also have reviewed persistent-node uses. At the v2.2 checkpoint, **141** symbols supported model trees. Node names are nouns such as Formed feature, Composite layup and Harmonic-response study. Editing commands do not automatically become persistent nodes.

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

robotics=json.loads((ROOT/'src/robotics_commands.json').read_text())
robotics_reuse=json.loads((ROOT/'src/robotics_reuse.json').read_text())
roles=Counter(i.get('role','command') for i in robotics)
new_tree=sum('modelTree' in i for i in robotics)
parts=[f'''# Robotics command and model-tree review

Date: 2026-10-17. Baseline: `cd269ffe836d8a905f2730c29a5ab0538e850474` (357 symbols).

This historical v2.3 pass added **{len(robotics)} independent meanings**: {roles['command']} commands, {roles['tool']} selectable tools and {roles['object']} object. Its checkpoint contained **403 unique SVGs**, with **183** model-tree-compatible entries. Counts are the result of selecting useful functions, never a target. The existing 357 SVGs were unchanged at that checkpoint. Later geometry corrections and CAX source coverage are documented in [CAX_STUDIO_REVIEW.md](CAX_STUDIO_REVIEW.md).

![Robotics additions at 48, 24 and 16 px](../qa/robotics-additions.png)

## Coverage and primary evidence

- Program structure: conditional branches, loops, variables, timed waits, concurrent tasks, events, scripts, operator messages, stepping, breakpoints and synchronization
- Teaching and processes: jog, hand guidance, reference-frame calibration, palletizing, conveyor tracking, force control, stationary-tool motion, point-follow processes, contact search and welding weave
- Planning and simulation: planning groups, collision-pair configuration, task path constraints, grasp candidates, trajectory timing, frame-tree inspection, occupancy maps, carried-object attachment, I/O mapping, signal traces and motion envelopes
- Physical model: one end-effector symbol, one controller object, camera/IMU/force-torque sensors, and six distinct kinematic relations shared with CAD

Public official references come from RoboDK, Universal Robots, ABB, KUKA, FANUC, MoveIt, ROS, SDFormat and Gazebo. The primary documents establish function and object semantics; every drawing is original. Versioned documentation is a taxonomy reference, not a statement of the newest product release or feature availability.

## Reuse and excluded duplication

- The gripper and end-effector candidates are one `olp-end-effector` tool. Parallel, vacuum and other hand forms are aliases, not separate drawings or open/closed states.
- Robot links reuse `cad-part`; mechanisms reuse `cad-assembly`. Visual and collision geometry reuse solid/mesh object symbols. A model-tree label supplies the role of each geometry leaf.
- Existing fixed, revolute and prismatic joints are shared with OLP. Continuous rotation reuses the revolute symbol. The new ball, planar, floating, screw and universal joints express different degrees of freedom, while coupling defines a dependency between joints; none is a section-shape variant.
- Named robot poses, coordinate frames, joint bounds, laser ranging and point clouds reuse existing symbols. Joint friction/damping is deferred as properties-level depth rather than adding more property glyphs.
- Program generation also supports a Robot program node. Speed, blend and payload instructions gain persistent-node metadata. Import/export/run/pause/stop reuse Common actions.
- Trajectory retiming computes times and derivatives, while speed sets an instruction and cycle time estimates duration. Collision pairs configure test participation, while collision checking performs a test. Force control commands a process, while a force-torque sensor measures an interface wrench.
- A traced TCP path, recorded swept volume, reachability check and modeled workspace boundary have different outputs. The boundary icon does not certify safety or change a robot's safety configuration.
- Program single-step means one program node, not a physics timestep. No robot-specific copies of generic play/pause/stop, no brand/morphology/state products and no generic ROS transport icons are added.
- {len(robotics_reuse)} existing entries receive reviewed vocabulary, source, category or node-use improvements. No synonym SVGs are generated for them.

## Native-size integration

{new_tree} new entries also support persistent model/program nodes. Five additional existing symbols gain model-tree support; existing tree symbols keep their artwork. Commands that merely inspect or modify transient state do not automatically become tree nodes.

![Robotics model trees at native 16 px](../qa/robotics-model-tree.png)

This 70-row specimen combines cell/program instructions, robot-model/planning data and process/station logic. The joint library shows alternatives rather than claiming every joint belongs to one robot. It is an illustrative consuming interface, not a vendor screenshot or an executable program.

## Per-function additions

| ID | English / Japanese | Role and tree use | Purpose | Primary references |
| --- | --- | --- | --- | --- |
''']
for i in robotics:
 refs='; '.join(f'[{s["title"]}]({s["url"]})' for s in i['references'])
 role=i.get('role','command')+(' / model-tree' if i.get('modelTree') else '')
 parts.append(f'| `{i["id"]}` | {i["name"]} / {i["nameJa"]} | {role} | {i["description"]} | {refs} |\n')
parts.append('\n## Reused entries\n\n| Existing ID | Vocabulary or node context | Primary references |\n| --- | --- | --- |\n')
for i in robotics_reuse:
 labels=i.get('aliases',[])+i.get('nodeAliases',[])
 if i.get('modelTree'):labels=[i['modelTree']['name']]+labels
 refs='; '.join(f'[{s["title"]}]({s["url"]})' for s in i['references'])
 parts.append(f'| `{i["id"]}` | {", ".join(dict.fromkeys(labels))} | {refs} |\n')
parts.append('''
## Verification and limits

Independent commercial-robotics and open-source-model reviews found no blocking semantic or visual issues after terminology and source corrections. All 403 SVGs pass XML/security/hash checks, normalized-geometry uniqueness and a color-normalized raster audit (zero blank, overflow or identical raster groups). Script-level JavaScript tests cover robotics aliases, shared categories, tool/command roles and bilingual persistent-node labels. See [the complete QA report](QA.md).

These results describe the historical v2.3 checkpoint; [QA.md](QA.md) records the current catalog. The work creates UI artwork and metadata only. It does not connect to, configure or control physical robots. These illustrations are not executable robot programs, certified safety symbols or validated system controls. Real-browser layout, focus, clipboard and download behavior remain unverified. No CI or deployment configuration is changed.
''')
(ROOT/'docs/ROBOTICS_EXPANSION.md').write_text(''.join(parts))
print('Refreshed robotics evidence and reuse review')

studio=json.loads((ROOT/'src/studio_commands.json').read_text())
studio_reuse=json.loads((ROOT/'src/studio_reuse.json').read_text())
quality=json.loads((ROOT/'src/quality_review.json').read_text())
theme=json.loads((ROOT/'qa/theme-audit.json').read_text())
parts=[f'''# CAX Studio coverage and geometry review

Date: 2026-10-18. Historical version: 2.4.0. Baseline: the preserved 403-symbol v2.3 tree `0419c0d994e944530fc495a032b11be6750cbeec`; public base commit `cd269ffe836d8a905f2730c29a5ab0538e850474` contains 357 symbols.

This historical pass added **{len(studio)} independently useful commands**, revised **{len(quality)} existing drawings**, and enriched **{len(studio_reuse)} reused symbols** without creating synonyms. Its checkpoint contains **410 SVGs**, including **186** symbols with model-tree use. Every existing ID was retained. The later pdxadv additions are documented in [PDXADV_REVIEW.md](PDXADV_REVIEW.md).

![Source-verified CAX commands](../qa/studio-additions.png)

## Source scope

The audit read current implementation and command availability in CAX Studio `afe7a7a4abf7896b525be66b695367a819516fdc`, Core `4b96fdeeac2f8aa9fb57a618da1c78aad7627459`, Viewer `ecec36c54e24e1dc91cbe65dd1e83b2384cb0d29` and feature recognition `62319d8a27c6950d9271a52ddab278dd18574bb7`. It also checked related SDK README contracts: caxio `13eb085`, mesh2brep `8dfe1d5`, constraint `fb19a78`, renderer `0a62e3a`, mesher `c616fc4`, collision detection `e8a4a62`, cable simulation `8bf8ad3`, CNC simulation `cc90aa3` and pdxadv `cfe0a2f`.

The per-command sources below pin exact commits. Presence in a command registry was cross-checked against enabled operations and persistent-node mappings where applicable. This is a source-coverage review, not a claim that every application or SDK was compiled or runtime-tested.

## Added meanings

| ID | English / Japanese | Use | Distinction and primary evidence |
| --- | --- | --- | --- |
''']
for i in studio:
 refs='; '.join(f'[{r["title"]}]({r["url"]})' for r in i['references'])
 uses='command / model-tree' if i.get('modelTree') else 'command'
 parts.append(f'| `{i["id"]}` | {i["name"]} / {i["nameJa"]} | {uses} | {i["reviewNote"]} {refs} |\n')
parts.append('''
## Reuse and exclusions

- Recognize is an analysis action. Recognized thread results reuse `cad-thread`; no recognized/unrecognized pairs are generated. Thread recognition is **B-rep-only** at the reviewed implementation, even though the overall recognition library supports both B-rep and mesh inputs.
- A helix is a 3D curve, not a thread feature. Face offset changes an existing solid, whereas offset surface creates independent surface geometry. Defeature removes and heals local features; Delete removes selected entities. Suppression retains the definition but skips evaluation; Hide changes display visibility.
- Face offset, helix and defeature have persistent node uses. Recognition, suppression, screenshot and photoreal rendering do not create new model entity classes in this catalog.
- Generic import/export, object visibility, folder, rename, assembly placement, BOM and geometry conversion reuse existing entries. File formats, conversion methods, robot shapes, object states and tessellation settings do not create extra SVGs.
- Face move, face rotate and range stretch remain possible future candidates. They were not misleadingly aliased to whole-body move/rotate/scale. Core curve sampling is internal display processing with no independently verified UI action, so no command icon is added.

| Reused ID | Added vocabulary | Review decision |
| --- | --- | --- |
''')
for i in studio_reuse:parts.append(f'| `{i["id"]}` | {", ".join(i["aliases"])} | {i["reviewNote"]} |\n')
parts.append('''
## Geometry corrections

All 403 baseline entries were inspected at native 16 / 24 / 32 px and diagnostic enlargements. Intentional mesh/wireframe intersections, coordinate origins, dashed workspace envelopes and measurement overlays were separated from accidental occlusion or projection errors. Nine corrections address geometry or measurement conventions; two are small optical cleanups. The seven added commands were reviewed separately. The independent post-fix pass also rendered and inspected all 410 symbols in the current dark palette at native 32 / 24 / 16 px; no remaining visual blocker was found.

![Before and after](../qa/quality-before-after.png)

| ID | Correction |
| --- | --- |
''')
for i in quality:parts.append(f'| `{i["id"]}` | {i["reason"]} |\n')
parts.append(f'''
## Preview theme correction

The former dark preview replaced ink with light blue while leaving body surfaces pale, erasing clock hands, mesh edges, sensor centers and other internal details. At that checkpoint, a preview-only CSS adapter mapped each color role independently. Pale body fill becomes `{theme['darkPalette']['body']}`, ink `{theme['darkPalette']['ink']}`, and teal accent `{theme['darkPalette']['accent']}` on `{theme['darkPalette']['background']}`. Opaque white node masks remain opaque using the dark background color; `fill="none"` and `stroke="none"` remain untouched. The soft glow was removed to avoid 16 px blur. Light/checker previews and copied/downloaded source SVG palettes were unchanged at that checkpoint. Current standalone light/dark exports are documented in [DARK_THEME.md](DARK_THEME.md).

The palette's calculated contrasts are **{theme['contrast']['ink_on_body']}:1** for ink on body and **{theme['contrast']['accent_on_body']}:1** for accent on body. These are color-role calculations, not a browser-computed-style audit or accessibility certification.

![Light, dark and checker previews](../qa/theme-preview.png)

The 22-example sheet includes every new and revised drawing plus representative dark-palette failures. The palette is now centralized in `src/themes.py`; the regenerated sheet preserves the reviewed colors and is a static SVG render, not a browser screenshot.

## Verification and limits

- Python: 9 groups covering XML safety, hashes, roles, bilingual metadata, source records, reuse, reviewed geometry and normalized uniqueness
- JavaScript: 15 script-level groups, including CAX command search, persistent-node labels, recognized-result reuse, all three preview selections, palette scoping and unchanged standalone copy/download data
- Raster: all 410 SVGs at the v2.4 checkpoint, zero empty output, zero viewBox overflow and zero identical color-normalized renders
- Reproducible category, additions, native model-tree, correction and theme sheets
- Actual browser integration remains **unverified**. The supported cloud browser rejected the local `file:` URL; no alternate browser-control route was used to bypass that policy. CSS computed styles, native dialog focus/Escape, real clipboard and saved downloads therefore remain on the manual checklist.

See [QA.md](QA.md) for the current verification report. These are UI symbols, not certified manufacturing, GD&T or robot-safety controls.
''')
(ROOT/'docs/CAX_STUDIO_REVIEW.md').write_text(''.join(parts))
print('Refreshed CAX source coverage and geometry review')

pdxadv=json.loads((ROOT/'src/pdxadv_commands.json').read_text())
pdxadv_reuse=json.loads((ROOT/'src/pdxadv_reuse.json').read_text())
parts=[f'''# pdxadv analysis and design workflow

Date: 2026-10-18. Historical version: 2.5.0. Baseline: `490d20684866e39c7075485bf2dc95abb95dd341` (410 symbols).

This pass adds **{len(pdxadv)} independent meanings** selected from implemented pdxadv workflows: six analysis/design meanings and three supporting result actions. This historical checkpoint contained **419 unique SVGs**, including **186** model-tree-compatible entries. All **410 existing SVG files remain byte-for-byte unchanged**. The count follows useful functions; no numerical target or state/format product is used.

![pdxadv additions](../qa/pdxadv-additions.png)

## Source scope

Implementation evidence is pinned to [`cslroot/cax-pdxadv` commit `40cc394fd59e18b76f48efa1161a25d460bafc6d`](https://github.com/cslroot/cax-pdxadv/tree/40cc394fd59e18b76f48efa1161a25d460bafc6d). The audit inspected result-field definitions, coordinate-search optimization, local mesh deformation, baseline/comparison controls and report assembly. This establishes vocabulary and scope; pdxadv itself was not compiled or runtime-tested for this icon task.

All nine entries are display/design/report commands. The local wall patch has a region list in pdxadv, but hierarchical model-tree display was not established, so this pass does not add model-tree claims.

## Nine additions and evidence

| ID | English / Japanese | Meaning and limits | Pinned primary sources |
| --- | --- | --- | --- |
''']
for i in pdxadv:
 refs='; '.join(f'[{r["title"]}]({r["url"]})' for r in i['references'])
 parts.append(f'| `{i["id"]}` | {i["name"]} / {i["nameJa"]} | {i["description"]} {i["reviewNote"]} | {refs} |\n')
parts.append('''
## Reuse and semantic boundaries

- **Sensitivity:** raw, normalized, density and contribution vocabulary all resolve to one sensitivity icon. The derivative is with respect to element isotropic linear shrinkage, not wall thickness. The tangent drawing represents a local response derivative.
- **Thickness design:** bounded coordinate search regenerates, remeshes and reanalyzes candidates under thickness, volume and lock constraints. It is not topology optimization and does not promise a global optimum.
- **Local wall offset:** the smooth mesh displacement has a finite influence radius and an explicit fixed back plane. The icon shows a localized raised section above an unchanged hatched back plane. It is not a B-rep face edit, generic smoothing or wall boundary condition.
- **Result fields:** local thickness, effective linear shrinkage and sink tendency are independent computed quantities. Linear shrinkage is not volumetric shrinkage. Sink tendency is the uncalibrated reference index `100 × linear shrinkage × (local thickness / median thickness)^2`, not a measured or predicted defect depth. Its icon uses a surface hotspot with no depth dimension or pass/fail mark.
- **Comparison:** two analysis results use synchronized cameras and a shared display range. Normalized sensitivity is still normalized independently within each result and displayed on a common −1 to 1 range. This is not measured/CAD deviation.
- **Baseline:** copies the current result in memory; does not save a file or guarantee persistence. A pin and result sheet distinguish it from Save and location bookmarks.
- **Report:** analysis conditions, results, diagnostics, figures, selected 3D models and optional comparisons share one report operation. HTML and PPTX do not become duplicate SVGs; dimensional inspection keeps its existing separate meaning.
- **Deformation reuse:** `cae-deformation-result` gains warpage, residual displacement and total-displacement aliases without changing its SVG. Total displacement includes uniform shrinkage after rigid-motion removal; residual warpage also removes uniform shrinkage. They share the visualization symbol while remaining distinct data fields.

## Visual design and verification

![Light, dark and checker previews](../qa/pdxadv-themes.png)

All geometry is original and uses the established 32 px grid, rounded joins and caps, pale body fill and teal accent. The additions sheet and three-background sheet show actual 48 / 24 / 16 px renders. The theme sheet uses the shared color-role palette and is a **static SVG render, not a browser screenshot**. Current standalone light/dark files are documented in [DARK_THEME.md](DARK_THEME.md).

The regression suite verifies all nine source records, pinned reference commits, bilingual search, single-family alias reuse, command-only usage, the in-memory baseline wording, and the SHA-256 hashes of every baseline SVG. XML/security/metadata/geometry tests and the full-catalog raster audit cover all 419 symbols. No blank, overflow or identical normalized raster group was found. The rebuild is deterministic.

Independent semantic and visual review status is recorded in [QA.md](QA.md). Real-browser layout, computed CSS, native dialog behavior, system clipboard and actual downloads remain unverified; this pass does not claim to resolve the earlier browser-access limitation. No CI, deployment or pdxadv runtime behavior is changed.
''')
(ROOT/'docs/PDXADV_REVIEW.md').write_text(''.join(parts))
print('Refreshed pdxadv meaning and reuse review')

# Reviewed GUI additions use the catalog as their single metadata source.
import sys
sys.path.insert(0,str(ROOT/'src'))
from gui_features import ITEMS as first_features
from gui_sketch import ITEMS as first_sketch
from gui_surface import ITEMS as first_surface
first_ids={'cad-'+i['id'] for i in first_features+first_sketch+first_surface}
new=[i for i in m['icons'] if i['id'] in first_ids]
lines=['# CAD GUI expansion', '', 'Reviewed on 2026-10-24 against main 04057de766e4b2694593f47a82690f32bdedfc27.', '',
       'Historical first GUI pass: 30 new meanings, 449 total at that checkpoint. Light/dark are variants, not additional meanings. All 419 original SVGs in both themes are byte-preserved. Artwork is original; vendor documentation provides command taxonomy only.', '',
       'This is a focused gap-filling pass, not complete coverage of either product. A documented SolidCraft command is not a promise that every upstream operation is implemented or robust. Planned surface fillet was not included.', '',
       '## New command mapping', '', '| CAX ID | English / 日本語 | Source command aliases | Purpose |', '| --- | --- | --- | --- |']
for i in new:
 aliases=', '.join(a for a in i.get('aliases',[]) if '.' in a)
 lines.append(f"| {i['id']} | {i['name']} / {i['nameJa']} | {aliases} | {i['description']} |")
lines += ['', '## Reuse instead of duplicate icons', '',
          '- Polygon input methods share one icon. Straight slot construction methods share one icon; arc-slot geometry is not falsely labeled straight.',
          '- Centerline / construction geometry share one construction-line symbol.',
          '- Surface match reuses cad-surface-match; it is not a new surface-stitch meaning.',
          '- Gear coupling reuses cad-joint-coupling; center of mass reuses cad-mass-properties.',
          '- Face push/pull reuses cad-face-offset; parameter editing reuses cad-parameters; recompute reuses cad-recompute.',
          '- Datum creation methods reuse existing plane/axis symbols. Material assignment reuses the existing shared cae-material-assignment.',
          '- Face splitting is distinct from cad-split-body; B-rep normal reversal differs from mesh face orientation.',
          '- History rollback changes the active history position, unlike common-history review. Body comparison is geometry, not cae-compare-results analysis fields.', '',
          '## Evidence', '']
for key in ['solidcraft-commands','solidworks-sketch','solidworks-surfaces']:
 ref=m['sourceReferences'][key];lines.append(f"- [{ref['title']}]({ref['url']}): {ref['scope']}.")
lines += ['', '## Verification and limits', '',
          '- XML, bilingual metadata, source registration, safe SVG, normalized geometry uniqueness and exact new-set membership checks.',
          '- The old 419-entry theme hash file is unchanged. Its hashes are checked as a preserved subset; new entries are checked separately. All theme geometry/mask checks still apply to every entry.',
          '- Raster audit: all entries nonblank, within viewBox, no identical color-normalized renders.',
          '- Native PNG exports at 16/24/32/48/64/128/256 px, both themes; alpha, dimensions, file integrity and cutout checks.',
          '- App and ZIP Node harness tests, including no IntersectionObserver fallback. Harness tests are not live-browser tests.',
          '- New icons visually reviewed at native 16/24/32 px in light and dark. [Preview](../qa/gui-additions.png).',
          '- No new browser/CUA, mobile, screen-reader or production integration validation; no source application functionality was changed.', '',
          'Regenerate this document with scripts/update_docs.py. Regenerate the native preview with scripts/gui_sheet.py.', '']
(ROOT/'docs/GUI_EXPANSION.md').write_text('\n'.join(lines))
print('Refreshed GUI meaning and reuse review')
