# QA report

Date: 2026-10-18. Scope: infinite gallery loading, filtered dialog navigation, synchronized preview backgrounds, standalone light/dark SVGs and transparent PNG export for all 419 semantic IDs. The [pdxadv review](PDXADV_REVIEW.md) and [historical geometry/theme review](CAX_STUDIO_REVIEW.md) retain the earlier source coverage. Profile/trajectory/state variants remain excluded; light/dark palettes do not inflate meaning counts.

<!-- results:start -->
- Semantic catalog: **419 icons** (Common 73, CAD 135, CAM 44, CAE 61, CMM 34, OLP 72)
- Theme files: **419 original light + 419 standalone dark**, with the same IDs and geometry
- Model-tree-compatible entries: **186**, unchanged
- Original SVGs preserved byte-for-byte: **419 / 419**, against commit `08d22603e7b21b47da35f67025ba36a6572c3c95`
- XML/security/metadata/hash/geometry/reuse/theme checks: **11 test groups passed**
- Opaque cutouts: **184 fills in 64 icons**, retained as #192c3c in dark files
- Existing 419-icon normalized raster audit: **0 blank, 0 overflow, 0 identical groups**
- Embedded standalone-SVG atlas without CSS at 16 / 24 / 32 px output sizes: **2,514 renders**, zero blanks and zero light/dark alpha mismatches
- Dark icons tested on #192c3c, #23262b and #121212: **3,771 surface checks**, each has at least eight output pixels of 3:1 contrast
- Dark ink/body contrast: **7.10:1**; accent/body: **4.91:1**; accent against tested backgrounds: **7.61:1 or higher**
- JavaScript syntax: **passed** for app.js and catalog.js
- Script-level app interactions: **29 groups passed**, including exact copy/download bytes for all **838** SVG files, **5,866** selected theme/size PNG source pipelines, automatic theme/background synchronization, manual surface overrides, infinite-scroll observer/fallback behavior, full-filtered-list detail navigation, asynchronous retries and cleanup
- PNG sizes: **16 / 24 / 32 / 48 / 64 / 128 / 256 px**, default 32; preview backgrounds excluded and opaque cutouts preserved
- Direct Inkscape PNG raster evidence: **5,866 RGBA exports**, zero dimension/blank/transparency/alpha mismatches; **28** independent single-file CLI matches
- Cutout raster evidence: **896** probe cases with matching alpha and **97,910** exact opaque-color pixels; four fully overpainted source variants are explicitly verified by geometry/order and opaque center samples
- PNG implementation preserves all **840** SVG/catalog outputs byte-for-byte against `55762ab8dcac8b537e884b96e42c8ab941ce4dcc`, including after rebuild
- Rebuild: **840 generated SVG/catalog outputs identical** in an independent isolated rebuild
- Independent visual review: **419 dark files in 16 / 24 / 32 px atlas cells**, checked on #192c3c, #23262b and neutral #202020; no new geometry or occlusion blockers found
- Six complete raw-file dark sheets and a selected before/after comparison on three dark surfaces
- Navigation update: **all 838 SVG files and both catalog outputs unchanged** against `b9411874bbb7e69366b968d83ab7fa7f5dc0ea13`; both observer-enabled and observer-unavailable harness runs pass
- Actual browser integration: **not run**; the earlier supported cloud-browser local-file rejection remains unresolved
<!-- results:end -->

The gallery/navigation update reruns the XML/integrity suite, JavaScript syntax checks and both modes of the DOM harness. Raster and static visual figures above are retained evidence from the preceding unchanged SVG/PNG work; they are not fresh browser verification.

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
- Render actual standalone bytes as independent embedded SVG images, without CSS, using `scripts/dark_theme_audit.py`; compare alpha channels and verify output contrast pixels
- Verify every original and dark copied/downloaded SVG matches its selected file byte-for-byte in the Node harness
- Execute PNG export with mocked Image/Canvas objects for all 838 variants at seven sizes; verify selected source bytes, dimensions, failures, timeouts, late completion, snapshot behavior and object-URL cleanup
- Measure actual independently rasterized PNG alpha and filled cutouts using `scripts/png_export_audit.py`; this is separate from browser Canvas testing

The transparent PNG audit is [`qa/png-export-audit.json`](../qa/png-export-audit.json); see [PNG behavior and limits](PNG_EXPORT.md). The standalone theme summary is [`qa/dark-theme-audit.json`](../qa/dark-theme-audit.json). The legacy normalized-geometry raster summary is [`qa/raster-audit.json`](../qa/raster-audit.json). Full raster intermediates are gitignored. Hash/XML/raster uniqueness cannot establish semantic uniqueness by themselves: the semantic review separately checks that every item describes a distinct command, tool or interface symbol.

## Application test coverage

1. Dynamic total, bounded first batch, six categories and removal of the old context filter
2. English / Japanese / AND / Unicode-normalized searches, common file actions, empty state and clear
3. Common/engineering category intersections and reset
4. Append-only 96-item batches, full ordered catalog without duplicates, complete/empty status, manual-load focus and query/category/usage resets
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
15. SVG-theme selection synchronizes global/detail selectors and preview backgrounds; subsequent swatch choices remain independent; selected repository paths stay correct
16. pdxadv sensitivity-family aliases, wall-design commands, result quantities, in-memory baseline wording, report format reuse and deformation aliases

17. Exact byte equality for all 838 light/dark copies and downloads, theme-specific filenames and stable semantic count
18. Theme/language changes preserve every loaded card and restore focus to the original opener
19. Seven explicit PNG sizes, default 32, independent gallery preview size, cutout note and in-dialog live status
20. All 5,866 light/dark PNG source pipelines: exact selected SVG bytes with sized root, requested dimensions, nonempty PNG MIME, timer/URL/callback/canvas cleanup
21. PNG source unaffected by light/dark/checker preview backgrounds
22. Async PNG snapshots during repeated clicks, theme/size changes, close/reopen and a later fresh export
23. No download on Canvas/decode/draw/encode/Blob/URL/anchor errors or timeouts; busy-state restoration and working retry
24. Late decode/encode completion after a timeout cannot download or disturb a new request
25. Invalid PNG sizes rejected before creating an image or downloading
26. Mocked IntersectionObserver appends at the sentinel, disconnects on completion, ignores queued stale callbacks after filters and pauses behind an open dialog; the entire suite also passes with the API unavailable
27. Previous/next buttons traverse the complete ordered filtered list beyond rendered cards, disable at either boundary, update bilingual labels and restore the original opener
28. Arrow keys preserve active controls and ignore input/textarea/select/contentEditable targets, modifiers, composition and previously handled events; Escape remains owned by the native dialog
29. Copy/download use the newly selected icon, and navigating while a PNG is pending preserves its captured icon/theme/size

## Not executed / limits

- **No real browser UI run.** These app checks execute in a script-level DOM harness, not a browser layout engine. The supported cloud browser rejected local `file:` access. An external Playwright route was not used to bypass browser policy.
- The older dark-theme audit embeds SVG images with intrinsic 32 px dimensions into 16 / 24 / 32 px atlas cells. Inkscape may resample them rather than render vectors directly at each output size. Its alpha/nonblank/contrast figures describe those atlas pixels, not direct native-size vector exports. The new PNG audit uses direct exports instead.
- Static theme sheets and direct-file Inkscape renders do not verify browser layout or computed styles. Color and output-pixel contrast checks are not accessibility certification.
- Dark cutouts are fixed #192c3c; they preserve hidden edges but can appear as inset patches on different backgrounds. They do not adapt automatically. See [integration constraints](DARK_THEME.md).
- Desktop/mobile layout, computed CSS, native dialog Escape/focus trapping, live-region announcements, browser history, real system clipboard, browser SVG-to-Canvas PNG encoding and saved downloads are not verified. Mock PNG blobs are not raster evidence; the independent Inkscape/Pillow pixel audit does not replace these browser checks.
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
- Use Common and all five engineering categories; scroll through all batches, check for duplicate/missing cards and confirm the end state; repeat with the Load more button and IntersectionObserver unavailable
- Combine Model-tree nodes with CAD, search `材料`, and reset; verify one shared material entry
- Switch command/tool/status usage filters and inspect the 16 px hierarchy specimen
- Switch languages, all sizes, both SVG themes and all backgrounds; inspect contrast and overflow
- Choose Dark in both selectors and confirm gallery/detail backgrounds switch together; choose Light and then manually select checkerboard, verifying the SVG colors stay selected
- Load several batches, change theme/language, and confirm the existing cards stay loaded; change the theme inside details, close and confirm keyboard focus returns to the same icon card
- Open the 96th icon and use Next to reach the 97th without loading another gallery batch; navigate filtered results to both boundaries; repeat with ← / → and check controls/modified keys are unaffected
- Open several details; close with ×, backdrop and Escape; check focus
- Copy SVG on localhost and paste into a text editor
- Download and open both variants; check `.svg` / `.dark.svg` filenames, exact content, appearance and fixed-cutout behavior
- Export both PNG themes at every listed size, reopen the saved files and inspect dimensions and transparent alpha
- Verify PNG ignores all preview backgrounds while retaining white/#192c3c opaque cutouts
- Move to another icon, change theme/size or close/reopen during PNG preparation; confirm captured request, repeated-click lock, status announcements and retry
- Confirm no console errors or external network requests

## Visual sheets

[Common](../qa/common.png) · [CAD](../qa/cad.png) · [CAM](../qa/cam.png) · [CAE](../qa/cae.png) · [CMM](../qa/cmm.png) · [OLP](../qa/olp.png) · [Earlier 38 additions](../qa/additions.png) · [87 application-family additions](../qa/application-additions.png) · [Original native 16 px hierarchy](../qa/model-tree.png) · [Additional native 16 px hierarchies](../qa/application-model-tree.png)

[46 robotics additions](../qa/robotics-additions.png) · [Native 16 px robotics hierarchies](../qa/robotics-model-tree.png)

[7 CAX additions](../qa/studio-additions.png) · [11 geometry corrections](../qa/quality-before-after.png) · [Light / dark / checker comparison](../qa/theme-preview.png) · [CAX source review](CAX_STUDIO_REVIEW.md)

[9 pdxadv additions](../qa/pdxadv-additions.png) · [pdxadv light / dark / checker](../qa/pdxadv-themes.png) · [pdxadv source review](PDXADV_REVIEW.md)

[Raw standalone comparison](../qa/dark-svg-comparison.png) · [Dark Common](../qa/dark-common.png) · [Dark CAD](../qa/dark-cad.png) · [Dark CAM](../qa/dark-cam.png) · [Dark CAE](../qa/dark-cae.png) · [Dark CMM](../qa/dark-cmm.png) · [Dark OLP](../qa/dark-olp.png) · [Theme integration](DARK_THEME.md)

[Transparent PNG diagnostic examples](../qa/png-export-preview.png) · [PNG export implementation and validation limits](PNG_EXPORT.md)
