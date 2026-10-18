# QA report

Date: 2026-10-18. Scope: v2.6 standalone light/dark SVGs for all 419 semantic IDs. The [pdxadv review](PDXADV_REVIEW.md) and [historical geometry/theme review](CAX_STUDIO_REVIEW.md) retain the earlier source coverage. Profile/trajectory/state variants remain excluded; light/dark palettes do not inflate meaning counts.

<!-- results:start -->
- Semantic catalog: **419 icons** (Common 73, CAD 135, CAM 44, CAE 61, CMM 34, OLP 72)
- Theme files: **419 original light + 419 standalone dark**, with the same IDs and geometry
- Model-tree-compatible entries: **186**, unchanged
- Original SVGs preserved byte-for-byte: **419 / 419**, against commit `08d22603e7b21b47da35f67025ba36a6572c3c95`
- XML/security/metadata/hash/geometry/reuse/theme checks: **11 test groups passed**
- Opaque cutouts: **184 fills in 64 icons**, retained as #192c3c in dark files
- Existing 419-icon normalized raster audit: **0 blank, 0 overflow, 0 identical groups**
- Raw standalone files rendered without CSS at native 16 / 24 / 32 px: **2,514 renders**, zero blanks and zero light/dark alpha mismatches
- Dark icons tested on #192c3c, #23262b and #121212: **3,771 surface checks**, each has at least eight native pixels of 3:1 contrast
- Dark ink/body contrast: **7.10:1**; accent/body: **4.91:1**; accent against tested backgrounds: **7.61:1 or higher**
- JavaScript syntax: **passed** for app.js and catalog.js
- Script-level app interactions: **18 groups passed**, including exact copy/download bytes for all **838** files, independent background/theme choices and close-after-theme-change focus restoration
- Rebuild: **840 generated SVG/catalog outputs identical** in an independent isolated rebuild
- Independent visual review: **419 dark files at 16 / 24 / 32 px**, checked on #192c3c, #23262b and neutral #202020; no new geometry or occlusion blockers found
- Six complete raw-file dark sheets and a selected before/after comparison on three dark surfaces
- Actual browser integration: **not run**; the earlier supported cloud-browser local-file rejection remains unresolved
<!-- results:end -->

## Executed methods

- Rebuild generated SVGs and metadata from hand-authored records
- Parse every SVG as XML; validate allowed elements, local references, hashes, bilingual metadata and semantic IDs
- Detect exact normalized-geometry duplicates, ignoring labels and colors
- Render every icon at 2× using Inkscape and measure visible alpha bounds without a per-icon viewport clip
- Compare color-normalized raster pixels for identical drawings
- Run real `app.js` and `catalog.js` in a dependency-free Node DOM harness
- Export and inspect Common, CAD, CAM, CAE, CMM and OLP contact sheets, plus all five source-reviewed additions sheets, at 48 / 24 / 16 px
- Render the actual SVG geometry at native 16 px inside the original 58 rows, 60 fabrication/mesh/analysis rows and 70 robotics rows
- Independently review all baseline drawings and additions for accidental occlusion, projected topology, arrow directions, semantic distinction, individual primary references, and appropriate glyph reuse
- Reproduce reviewed before/after geometry and source color roles in static SVG sheets
- Render actual standalone bytes as independent embedded SVG images, without CSS, using `scripts/dark_theme_audit.py`; compare alpha channels and verify native contrast pixels
- Verify every original and dark copied/downloaded SVG matches its selected file byte-for-byte in the Node harness

The standalone theme summary is [`qa/dark-theme-audit.json`](../qa/dark-theme-audit.json). The legacy normalized-geometry raster summary is [`qa/raster-audit.json`](../qa/raster-audit.json). Full raster intermediates are gitignored. Hash/XML/raster uniqueness cannot establish semantic uniqueness by themselves: the semantic review separately checks that every item describes a distinct command, tool or interface symbol.

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
15. Explicit SVG-theme selection, repeated independent background changes, synchronized global/detail selectors and selected repository paths
16. pdxadv sensitivity-family aliases, wall-design commands, result quantities, in-memory baseline wording, report format reuse and deformation aliases

17. Exact byte equality for all 838 light/dark copies and downloads, theme-specific filenames and stable semantic count
18. Focus restoration to the replacement opener card after repeated detail-theme changes

## Not executed / limits

- **No real browser UI run.** These app checks execute in a script-level DOM harness, not a browser layout engine. The supported cloud browser rejected local `file:` access. An external Playwright route was not used to bypass browser policy.
- Static theme sheets and raw-file Inkscape renders do not verify browser layout or computed styles. Color and native-pixel contrast checks are not accessibility certification.
- Dark cutouts are fixed #192c3c; they preserve hidden edges but can appear as inset patches on different backgrounds. They do not adapt automatically. See [integration constraints](DARK_THEME.md).
- Desktop/mobile layout, computed CSS, native dialog Escape/focus trapping, browser history, real system clipboard and saved downloads are not verified.
- Alpha bounds use a threshold of 10/255 at 2×; this detects visible overflow rather than every theoretical subpixel extent.
- Small previews help review legibility but do not guarantee every symbol is suitable for every 16 px toolbar. Check against the intended background and task.
- The semantic catalog is intentionally selective; it does not cover every command in every engineering product.
- No package install or runtime external artwork/font is required.

## Manual browser checklist

Serve the repository locally as described in the README, then inspect desktop and narrow-mobile widths:

- Search `open`, `保存`, `名前を付けて保存`, `extrude`, `押し出し` and a nonsense term
- Search `raster finishing`, `ICP`, `shut-off patch`, `merge coincident nodes`, `メッシュ`, `点群` and `溶接`
- Search `normalized sensitivity`, `肉厚対策`, `局所肉厚変更`, `有効線収縮率`, `ヒケ傾向指標`, `pin baseline` and `PPTX analysis report`
- Search `face offset`, `helix`, `defeature`, `unsuppress feature`, `recognized thread`, `screenshot` and `photo render`
- Search `gripper`, `IMU`, `cad-part robot link`, `planning group`, `条件分岐` and `workspace boundary`; inspect command/tool/model-tree roles
- Use Common and all five engineering categories; navigate the last page and back
- Combine Model-tree nodes with CAD, search `材料`, and reset; verify one shared material entry
- Switch command/tool/status usage filters and inspect the 16 px hierarchy specimen
- Switch languages, all sizes, both SVG themes and all backgrounds; inspect contrast and overflow
- Keep the original SVG selected on a dark surface, then explicitly choose Dark and verify preview/export colors agree
- Change the theme inside details, close and confirm keyboard focus returns to the same icon card
- Open several details; close with ×, backdrop and Escape; check focus
- Copy SVG on localhost and paste into a text editor
- Download and open both variants; check `.svg` / `.dark.svg` filenames, exact content, appearance and fixed-cutout behavior
- Confirm no console errors or external network requests

## Visual sheets

[Common](../qa/common.png) · [CAD](../qa/cad.png) · [CAM](../qa/cam.png) · [CAE](../qa/cae.png) · [CMM](../qa/cmm.png) · [OLP](../qa/olp.png) · [Earlier 38 additions](../qa/additions.png) · [87 application-family additions](../qa/application-additions.png) · [Original native 16 px hierarchy](../qa/model-tree.png) · [Additional native 16 px hierarchies](../qa/application-model-tree.png)

[46 robotics additions](../qa/robotics-additions.png) · [Native 16 px robotics hierarchies](../qa/robotics-model-tree.png)

[7 CAX additions](../qa/studio-additions.png) · [11 geometry corrections](../qa/quality-before-after.png) · [Light / dark / checker comparison](../qa/theme-preview.png) · [CAX source review](CAX_STUDIO_REVIEW.md)

[9 pdxadv additions](../qa/pdxadv-additions.png) · [pdxadv light / dark / checker](../qa/pdxadv-themes.png) · [pdxadv source review](PDXADV_REVIEW.md)

[Raw standalone comparison](../qa/dark-svg-comparison.png) · [Dark Common](../qa/dark-common.png) · [Dark CAD](../qa/dark-cad.png) · [Dark CAM](../qa/dark-cam.png) · [Dark CAE](../qa/dark-cae.png) · [Dark CMM](../qa/dark-cmm.png) · [Dark OLP](../qa/dark-olp.png) · [Theme integration](DARK_THEME.md)
