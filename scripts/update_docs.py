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

Date: 2026-10-18. Version: {m['version']}. Baseline: the preserved 403-symbol v2.3 tree `0419c0d994e944530fc495a032b11be6750cbeec`; public base commit `cd269ffe836d8a905f2730c29a5ab0538e850474` contains 357 symbols.

This pass adds **{len(studio)} independently useful commands**, revises **{len(quality)} existing drawings**, and enriches **{len(studio_reuse)} reused symbols** without creating synonyms. The resulting collection contains **{m['count']} SVGs**, including **{m['usageCounts']['model-tree']}** symbols with model-tree use. Every existing ID is retained.

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

The former dark preview replaced ink with light blue while leaving body surfaces pale, erasing clock hands, mesh edges, sensor centers and other internal details. A preview-only CSS adapter now maps each color role independently. Pale body fill becomes `{theme['darkPalette']['body']}`, ink `{theme['darkPalette']['ink']}`, and teal accent `{theme['darkPalette']['accent']}` on `{theme['darkPalette']['background']}`. Opaque white node masks remain opaque using the dark background color; `fill="none"` and `stroke="none"` remain untouched. The soft glow was removed to avoid 16 px blur. Light/checker previews and copied/downloaded source SVG palettes remain unchanged.

The palette's calculated contrasts are **{theme['contrast']['ink_on_body']}:1** for ink on body and **{theme['contrast']['accent_on_body']}:1** for accent on body. These are color-role calculations, not a browser-computed-style audit or accessibility certification.

![Light, dark and checker previews](../qa/theme-preview.png)

The 22-example sheet includes every new and revised drawing plus representative dark-palette failures. Its colors are extracted from the production CSS and rendered as SVG, so it is reproducible without representing it as a browser screenshot.

## Verification and limits

- Python: 9 groups covering XML safety, hashes, roles, bilingual metadata, source records, reuse, reviewed geometry and normalized uniqueness
- JavaScript: 15 script-level groups, including CAX command search, persistent-node labels, recognized-result reuse, all three preview selections, palette scoping and unchanged standalone copy/download data
- Raster: all {m['count']} SVGs, zero empty output, zero viewBox overflow and zero identical color-normalized renders
- Reproducible category, additions, native model-tree, correction and theme sheets
- Actual browser integration remains **unverified**. The supported cloud browser rejected the local `file:` URL; no alternate browser-control route was used to bypass that policy. CSS computed styles, native dialog focus/Escape, real clipboard and saved downloads therefore remain on the manual checklist.

See [QA.md](QA.md) for the current verification report. These are UI symbols, not certified manufacturing, GD&T or robot-safety controls.
''')
(ROOT/'docs/CAX_STUDIO_REVIEW.md').write_text(''.join(parts))
print('Refreshed CAX source coverage and geometry review')
