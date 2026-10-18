# QA report

Date: 2026-10-18. Scope: semantic v2.4 CAX coverage, all 403 baseline drawings, seven additions, 11 geometry corrections and the preview-only dark palette. All profile/trajectory/state variants remain excluded.

<!-- results:start -->
- Final collection: **410 SVGs** (Common 73, CAD 135, CAM 44, CAE 52, CMM 34, OLP 72)
- Added in this pass: **7 independent commands**, sourced to pinned CAX implementation commits
- Model-tree-compatible entries: **186**; face offset, helix and defeature add three persistent-node uses
- Existing IDs retained: **403 / 403**; 11 drawings corrected, 392 baseline drawings unchanged
- Existing CAX vocabulary reuse: **9 entries**, with no synonym SVGs
- XML/security/metadata/hash/geometry/reuse checks: **9 test groups passed**
- Normalized-geometry duplicates: **0**
- All 410 SVGs rendered at 2×: **0 blank, 0 overflow, 0 identical normalized raster groups**
- JavaScript syntax: **passed** for app.js and catalog.js
- Script-level application interactions and palette scope: **15 groups passed**
- Six category sheets and four reviewed-additions sheets render at 48 / 24 / 16 px
- All three native 16 px model-tree specimens retained and regenerated (58 / 60 / 70 rows)
- Independent baseline visual coverage: **403 / 403**, plus independent review of all 11 revised and seven new drawings
- Palette examples: **22** at 48 / 24 / 16 px on light, dark and checker backgrounds
- Independent dark-palette regression review: **410 / 410**, all icons at native 32 / 24 / 16 px; no remaining visual blockers
- Dark ink/body contrast: **7.10:1**; accent/body contrast: **4.91:1** (static color calculations)
- Deterministic rebuild: **passed**, generated SVGs, metadata, sheets and documentation unchanged
- Actual browser integration: **not run**; supported cloud browser rejected the local file URL
<!-- results:end -->

## Executed methods

- Rebuild generated SVGs and metadata from hand-authored records
- Parse every SVG as XML; validate allowed elements, local references, hashes, bilingual metadata and semantic IDs
- Detect exact normalized-geometry duplicates, ignoring labels and colors
- Render every icon at 2× using Inkscape and measure visible alpha bounds without a per-icon viewport clip
- Compare color-normalized raster pixels for identical drawings
- Run real `app.js` and `catalog.js` in a dependency-free Node DOM harness
- Export and inspect Common, CAD, CAM, CAE, CMM and OLP contact sheets, plus all four source-reviewed additions sheets, at 48 / 24 / 16 px
- Render the actual SVG geometry at native 16 px inside the original 58 rows, 60 fabrication/mesh/analysis rows and 70 robotics rows
- Independently review all baseline drawings and additions for accidental occlusion, projected topology, arrow directions, semantic distinction, individual primary references, and appropriate glyph reuse
- Reproduce reviewed before/after geometry and the production CSS color-role mapping in static SVG sheets; test adapter selectors without claiming browser computed-style coverage

The machine-readable raster summary is [`qa/raster-audit.json`](../qa/raster-audit.json). Full raster intermediates are gitignored. Hash/XML/raster uniqueness cannot establish semantic uniqueness by themselves: the semantic review separately checks that every item describes a distinct command, tool or interface symbol.

## Application test coverage

1. Dynamic total, bounded first page, six categories and removal of the old context filter
2. English / Japanese / AND / Unicode-normalized searches, common file actions, empty state and clear
3. Common/engineering category intersections and reset
4. All pages, last-page bounds, previous navigation and query page reset
5. Japanese labels, preview size and backgrounds
6. Bilingual purpose, repeated detail open, close, backdrop targeting and focus restoration
7. Copied SVG title, geometry and absence of preview-only IDs
8. Clipboard rejection, failed/throwing fallback and temporary-element cleanup
9. Download filename, SVG type and content
10. `/` shortcut guarded while typing or viewing a dialog
11. Usage filters, model-tree noun labels, Japanese node labels, category/usage/search intersections, shared entries without duplicate cards, instance alias search and complete reset
12. Application aliases (raster finishing, ICP, shut-off patch, mesh nodes), shared CAD/CAE search and advanced model-tree names
13. Robotics aliases, shared OLP joints/robot links, command-only calibration, and bilingual conditional-branch/planning-group nodes
14. CAX additions, recognized-thread reuse, source-verified command roles and persistent node names
15. Preview-only dark palette scoping, opaque masks, three repeated background selections and light/dark detail context

## Not executed / limits

- **No real browser UI run.** These app checks execute in a script-level DOM harness, not a browser layout engine. The supported cloud browser rejected local `file:` access. An external Playwright route was not used to bypass browser policy.
- Static theme sheets extract role colors from production CSS; they do not verify selector matching or computed styles in a browser. Color contrast calculations are not accessibility certification.
- Desktop/mobile layout, computed CSS, native dialog Escape/focus trapping, browser history, real system clipboard and saved downloads are not verified.
- Alpha bounds use a threshold of 10/255 at 2×; this detects visible overflow rather than every theoretical subpixel extent.
- Small previews help review legibility but do not guarantee every symbol is suitable for every 16 px toolbar. Check against the intended background and task.
- The semantic catalog is intentionally selective; it does not cover every command in every engineering product.
- No package install or runtime external artwork/font is required.

## Manual browser checklist

Serve the repository locally as described in the README, then inspect desktop and narrow-mobile widths:

- Search `open`, `保存`, `名前を付けて保存`, `extrude`, `押し出し` and a nonsense term
- Search `raster finishing`, `ICP`, `shut-off patch`, `merge coincident nodes`, `メッシュ`, `点群` and `溶接`
- Search `face offset`, `helix`, `defeature`, `unsuppress feature`, `recognized thread`, `screenshot` and `photo render`
- Search `gripper`, `IMU`, `cad-part robot link`, `planning group`, `条件分岐` and `workspace boundary`; inspect command/tool/model-tree roles
- Use Common and all five engineering categories; navigate the last page and back
- Combine Model-tree nodes with CAD, search `材料`, and reset; verify one shared material entry
- Switch command/tool/status usage filters and inspect the 16 px hierarchy specimen
- Switch languages, all sizes and backgrounds; inspect contrast and overflow
- Open several details; close with ×, backdrop and Escape; check focus
- Copy SVG on localhost and paste into a text editor
- Download and open an SVG; check its filename and appearance
- Confirm no console errors or external network requests

## Visual sheets

[Common](../qa/common.png) · [CAD](../qa/cad.png) · [CAM](../qa/cam.png) · [CAE](../qa/cae.png) · [CMM](../qa/cmm.png) · [OLP](../qa/olp.png) · [Earlier 38 additions](../qa/additions.png) · [87 application-family additions](../qa/application-additions.png) · [Original native 16 px hierarchy](../qa/model-tree.png) · [Additional native 16 px hierarchies](../qa/application-model-tree.png)

[46 robotics additions](../qa/robotics-additions.png) · [Native 16 px robotics hierarchies](../qa/robotics-model-tree.png)

[7 CAX additions](../qa/studio-additions.png) · [11 geometry corrections](../qa/quality-before-after.png) · [Light / dark / checker comparison](../qa/theme-preview.png) · [CAX source review](CAX_STUDIO_REVIEW.md)
