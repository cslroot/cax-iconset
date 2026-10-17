# QA report

Date: 2026-10-17. Scope: the semantic v2.1 catalog and model-tree integration, with all profile/trajectory variants excluded.

<!-- results:start -->
- Final collection: **270 SVGs** (primary categories: Common 70, CAD 82, CAM 31, CAE 35, CMM 25, OLP 27)
- Added independent symbols: **38** (30 commands and 8 persistent objects)
- Model-tree-compatible entries: **118**, reusing the same SVGs rather than emitting variants
- XML, safety, metadata, hash, geometry, reuse and removed-generator checks: **5 test groups passed**
- Normalized-geometry duplicates: **0**
- All 270 SVGs rendered at 2×: **0 blank, 0 overflow, 0 identical normalized raster groups**
- JavaScript syntax: **passed** for app.js and catalog.js
- Script-level application interactions: **11 groups passed**
- All six category sheets and the 38-addition sheet inspected at 48 / 24 / 16 px
- Model-tree integration specimen: **58 rows at native 16 px**, inspected as three indented hierarchies
- Independent CAD and CAM/CAE semantic and visual reviews: **no blocking issues**
- Deterministic rebuild: **passed**, generated SVGs, metadata, sheets and coverage blocks unchanged
- Actual browser integration: **not run**
<!-- results:end -->

## Executed methods

- Rebuild generated SVGs and metadata from hand-authored records
- Parse every SVG as XML; validate allowed elements, local references, hashes, bilingual metadata and semantic IDs
- Detect exact normalized-geometry duplicates, ignoring labels and colors
- Render every icon at 2× using Inkscape and measure visible alpha bounds without a per-icon viewport clip
- Compare color-normalized raster pixels for identical drawings
- Run real `app.js` and `catalog.js` in a dependency-free Node DOM harness
- Export and inspect Common, CAD, CAM, CAE, CMM and OLP contact sheets, plus the source-reviewed additions, at 48 / 24 / 16 px
- Render the actual SVG geometry at native 16 px inside 58 indented CAD/CAM/CAE tree rows
- Independently review additions for semantic distinction, individual primary references, and appropriate glyph reuse

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

## Not executed / limits

- **No real browser UI run.** These app checks execute in a script-level DOM harness, not a browser layout engine.
- Desktop/mobile layout, computed CSS, native dialog Escape/focus trapping, browser history, real system clipboard and saved downloads are not verified.
- Alpha bounds use a threshold of 10/255 at 2×; this detects visible overflow rather than every theoretical subpixel extent.
- Small previews help review legibility but do not guarantee every symbol is suitable for every 16 px toolbar. Check against the intended background and task.
- The semantic catalog is intentionally selective; it does not cover every command in every engineering product.
- No package install or runtime external artwork/font is required.

## Manual browser checklist

Serve the repository locally as described in the README, then inspect desktop and narrow-mobile widths:

- Search `open`, `保存`, `名前を付けて保存`, `extrude`, `押し出し` and a nonsense term
- Use Common and all five engineering categories; navigate the last page and back
- Combine Model-tree nodes with CAD, search `材料`, and reset; verify one shared material entry
- Switch command/tool/status usage filters and inspect the 16 px hierarchy specimen
- Switch languages, all sizes and backgrounds; inspect contrast and overflow
- Open several details; close with ×, backdrop and Escape; check focus
- Copy SVG on localhost and paste into a text editor
- Download and open an SVG; check its filename and appearance
- Confirm no console errors or external network requests

## Visual sheets

[Common](../qa/common.png) · [CAD](../qa/cad.png) · [CAM](../qa/cam.png) · [CAE](../qa/cae.png) · [CMM](../qa/cmm.png) · [OLP](../qa/olp.png) · [38 additions](../qa/additions.png) · [Native 16 px model-tree hierarchy](../qa/model-tree.png)
