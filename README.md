# CAX Iconset

<!-- binding-review:start -->
## Conditional GUI binding review (2026-10-25)

21 additional original glyphs support the reviewed command bindings. Current catalog: **714 semantic icons / 1428 theme SVGs**. The published 693-icon baseline is unchanged.

See [conditions, evidence and unresolved branches](docs/GUI_BINDINGS.md), [binding JSON](command-bindings.json) and [180-row resolution CSV](docs/GUI_BINDING_RESOLUTIONS.csv). Conditional reuse does not mean a consumer GUI has implemented the required labels, states or routing.
<!-- binding-review:end -->

<!-- coverage-expansion:start -->
## Systematic GUI coverage (2026-10-25)

244 new original command glyphs were implemented from the frozen source audit, with documented reuse and unresolved bindings. The current catalog contains **714 semantic icons / 1428 standalone SVG files**. All 449 previously delivered records and both theme SVGs remain unchanged.

See [scope, decisions and source mapping](docs/GUI_COVERAGE.md), [all 1,089 evidence rows with implementation status](docs/GUI_IMPLEMENTATION_TRACKING.csv), and [native-size preview page list](qa/coverage-preview/pages.json). This is source-scoped coverage, not a claim that all SOLIDWORKS product editions or every uncertain GUI binding are complete.
<!-- coverage-expansion:end -->

## Initial GUI expansion (2026-10-24)

30 independently useful CAD meanings were added after checking the SolidCraft command reference and SOLIDWORKS sketch/surface toolbars. That checkpoint contained **449 semantic icons / 898 standalone SVG files**. All 419 previous light and dark SVG files are unchanged. See [the reviewed command mapping and reuse decisions](docs/GUI_EXPANSION.md) and [native 16 / 24 / 32 px preview](qa/gui-additions.png).

The new set has XML, metadata, geometry, raster, theme contrast, native PNG and app/ZIP harness coverage. Historical live-browser checks below covered the former 419-icon release, not this expansion. No new live browser, mobile, clipboard integration or accessibility check is claimed.


Original rounded SVG symbols for everyday application commands, model-tree objects and CAD, CAM, CAE, CMM and Robotics / OLP. Every entry has a semantic ID, English and Japanese names, bilingual search tags, and a one-sentence purpose in both languages.

**The collection is organized by meaning, not by a target icon count.** Shape/profile/trajectory combinations have been removed from the catalog, source generator and exported SVGs. The previous collection remains recoverable in Git history.

![pdxadv analysis and design additions](qa/pdxadv-additions.png)

## Coverage

<!-- coverage:start -->
| Primary category | Symbols |
| --- | ---: |
| Common | 89 |
| CAD | 413 |
| CAM | 44 |
| CAE | 62 |
| CMM | 34 |
| OLP | 72 |
| **Total** | **714** |

Primary roles: 692 commands, 9 selectable tools, 9 objects and 4 status symbols. Every semantic icon is counted once; light/dark files are color variants of the same ID.

186 entries support model-tree use, including reused command/tool symbols; these are not additional semantic icons.
<!-- coverage:end -->

- Common: new, open, recent files, close, save / save as / save all, import, export, print, undo / redo, clipboard, search / replace, filtering, selection, display, navigation and application controls
- CAD: sketching, constraints, dimensions, solid features, assembly, sheet metal, weldments, mold tooling, free-form surfaces, mesh editing, vector paths and drawing blocks
- CAM: setup, tooling, milling/turning/EDM operations, stock models, compensation, nesting, toolpath editing, verification and NC output
- CAE: studies, material directions/layups, mesh topology, connections, coupling, boundaries, loads, solver and scalar/vector/derived results, shrinkage sensitivity, bounded wall-thickness design and analysis comparison/reporting
- CMM: probes, calibration, alignment, point-cloud processing/reconstruction, path optimization, temperature compensation, features, tolerances and reporting
- OLP: cell setup, teaching, targets, control flow, IO mapping, grasp/motion planning, trajectory timing, sensors, physical models, process instructions, calibration and simulation

Reusable drawing primitives keep the style coherent, but a different section shape, color, orientation or trajectory does not create another catalog entry. Related commands such as Save and Save as remain separate because they perform different actions. Status and tool symbols are identified by `role` rather than advertised as additional commands. See [design, scope and primary references](docs/REFERENCE.md).

## Browse locally

The static catalog is included. No npm install, framework, CDN, account or API key is required.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000` in a modern browser, or use the [public catalog](https://savethebunny.net/cax-iconset/). The existing GitHub Pages deployment publishes `main`; its build and deployment completed successfully for the [bulk-download update](https://github.com/cslroot/cax-iconset/actions/runs/39110884595).

- English / Japanese name, tag and purpose search, with multiple AND-matched terms
- Common and five engineering-category filters; append-only infinite scrolling in batches of 96, plus an accessible Load more button
- Independent usage filter: commands, model-tree nodes, tools and status
- Contextual node names; existing feature, material, mesh, condition and result SVGs are reused
- [Robotics model trees at native 16 px](qa/robotics-model-tree.png), [general model-tree integration](qa/model-tree.png) and [fabrication/mesh/analysis trees](qa/application-model-tree.png)
- 16 / 24 / 32 / 48 / 64 px previews; light / dark / checker backgrounds
- Explicit light / dark SVG theme choice that also sets the matching preview background; background swatches can then be changed manually, and preview/copy/download use the selected file variant
- Detail view with previous/next buttons and ← / → navigation through the complete filtered list, bilingual purpose, selected variant path, copy SVG and individual SVG download
- Transparent PNG download in 16 / 24 / 32 / 48 / 64 / 128 / 256 px; selected light/dark colors, independent of preview background
- Bulk ZIP download for all 419 icons or the complete current filter results, with SVG/PNG, light/dark, PNG-size options, progress and cancellation
- Keyboard focus, `/` search shortcut, native dialog with Escape dismissal, clear first/last boundaries and empty-state reset
- No analytics or runtime external requests

Interface labels are English; the language selector switches icon names and purpose text between English and Japanese.

## Use an icon

```html
<img src="icons/common-open-file.svg" width="32" height="32" alt="Open file">
<img src="icons/common-save.svg" width="32" height="32" alt="Save">
<img src="icons/cad-extrude.svg" width="32" height="32" alt="Extrude">
<!-- Standalone dark SVG; no host CSS recoloring needed -->
<img src="icons-dark/cad-extrude.svg" width="32" height="32" alt="Extrude">
```

SVGs use basic vector elements without fonts or external resources. Each file has a title and a 32 × 32 viewBox. Namespace internal IDs if embedding multiple files inline; the catalog handles its preview IDs automatically.

`manifest.json` contains the metadata, original SVG body, SHA-256 hash, per-theme variant paths/hashes, dark SVG body, primary role, supported usages, contextual node names, category memberships and taxonomy references for each symbol. `catalog.js` contains the same data for the static app. Both are generated: edit `src/` and rebuild. The top-level `categories` counts use each icon’s primary `category` and sum to the semantic icon count; an icon’s `categories` array can also include shared disciplines. `categoryMemberships` records those overlapping browser-filter counts. `role: "object"` means an object-only entry; `usages` can include both `command` and `model-tree` without making another file. See the [pdxadv analysis/design review](docs/PDXADV_REVIEW.md), the [CAX Studio coverage and geometry review](docs/CAX_STUDIO_REVIEW.md), the [robotics expansion and reuse review](docs/ROBOTICS_EXPANSION.md), the [application-family expansion review](docs/APPLICATION_EXPANSION.md) for per-function evidence and reuse decisions, and the [earlier model-tree expansion](docs/EXPANSION_REVIEW.md). The optional `aliases` field records alternate application vocabulary; shared categories still produce one SVG.

## Standalone dark files

All **419 semantic icons** now have two file variants: original light files in `icons/` and dark files in `icons-dark/`, with the same IDs. The 419 originals are byte-for-byte preserved. Dark files contain their own colors and work as `<img>`, external SVGs or inline SVGs without the catalog's CSS. Theme variants do not increase search/category/usage counts.

Choose **SVG → Dark** in the catalog or detail view before copying/downloading. Choosing a theme also switches the gallery and detail preview to its matching background; you can then select light, dark or checkerboard manually without changing the SVG colors. Downloads are named `<id>.dark.svg` for clarity, while repository paths are `icons-dark/<id>.svg`.

The dark palette targets **#192c3c**. Its opaque cutouts also use that color to hide covered edges; 64 icons contain these fills. They remain opaque and may look like inset patches on other surfaces, including CAX Studio's #23262b. The files do not automatically adapt to arbitrary backgrounds. See [integration and palette guidance](docs/DARK_THEME.md) and the [embedded-SVG comparison at 16 / 24 / 32 px output sizes](qa/dark-svg-comparison.png).

## Transparent PNG download

Open an icon's detail view, choose **Icon theme → Light / Dark**, select **PNG size**, then click **Download PNG**. Available square sizes are **16, 24, 32, 48, 64, 128 and 256 px**; the default is **32 px**. PNG size is independent of the gallery's preview size. Files are named `<id>.<light|dark>.<size>.png`, for example `cad-extrude.dark.64.png`.

The browser rasterizes the selected standalone SVG on a fresh alpha-enabled Canvas. The canvas around the drawing is transparent; the light, dark and checkerboard preview surfaces are never painted into the PNG. Existing solid fills, including the opaque cutouts in 64 icons, are preserved: white in light files and #192c3c in dark files. These interior shapes do not become transparent, because they hide covered geometry. PNG does not automatically adapt those colors to another background.

Conversion happens locally in the browser without an external service or network request. While one PNG is being prepared, its button is disabled. The requested icon/theme/size are captured when clicked; changing the detail controls afterward does not change that export. A failed or timed-out conversion produces an error message instead of an empty download. The original SVG copy/download options remain available.

See [PNG implementation and verification](docs/PNG_EXPORT.md). The tests include a mocked Canvas pipeline and separate real Inkscape PNG alpha measurements; live Chrome checks also verified selected light/dark 64 px PNG downloads and byte-exact SVG clipboard content. Full cross-browser and every-size browser coverage is not claimed.

## Bulk ZIP download

Click **Download ZIP** beside the search field. Choose **Current results** to include all matching icons, even those not yet scrolled into view, or **All 419 icons** to ignore the current filters. Select **SVG** or **PNG**, **Light / Dark**, and a PNG size if needed. The theme initially follows the gallery. A zero-result filtered selection cannot be exported; **All icons** remains available.

One ZIP contains one file per selected icon. SVGs are byte-exact standalone files, named `<id>.svg` or `<id>.dark.svg`. PNGs use `<id>.<light|dark>.<size>.png`, with transparent surroundings and preserved opaque cutouts. Archive names include scope, count, theme, format and PNG size, for example `cax-icons-filtered-3.dark.64.png.zip`.

Conversion and ZIP assembly happen locally, without a CDN, upload or external service. The request captures its complete icon list and options; later changes cannot mix exports. Progress is shown during sequential PNG conversion. **Cancel export**, ×, Escape or closing the dialog stops the operation without downloading a partial ZIP. A failed icon also stops the entire archive and allows retry. ZIP entries are stored without compression for a small dependency-free implementation. See [bulk implementation and QA](docs/BULK_DOWNLOAD.md).

## Rebuild and verify

Python 3.10+ builds the collection. Node.js runs application tests. The optional raster audits and sheet exports use already-installed Inkscape and Pillow; the PNG audit also uses NumPy.

```sh
python3 scripts/build.py
python3 tests/test_catalog.py
node --check app.js
node --check catalog.js
node --check zip.js
node tests/test_zip.js
node tests/test_app.js
NO_INTERSECTION_OBSERVER=1 node tests/test_app.js
python3 scripts/raster_audit.py
python3 scripts/dark_theme_audit.py
python3 scripts/png_export_audit.py
python3 scripts/contact_sheet.py
python3 scripts/model_tree_sheet.py
python3 scripts/application_tree_sheet.py
python3 scripts/robotics_tree_sheet.py
python3 scripts/quality_sheet.py
python3 scripts/theme_sheet.py
python3 scripts/theme_sheet.py --pdxadv
python3 scripts/update_docs.py
for category in common cad cam cae cmm olp additions application-additions robotics-additions studio-additions pdxadv-additions pdxadv-themes quality-before-after theme-preview; do
  inkscape "qa/$category.svg" --export-type=png --export-filename="qa/$category.png"
done
inkscape qa/model-tree.svg --export-type=png --export-filename=qa/model-tree.png
inkscape qa/application-model-tree.svg --export-type=png --export-filename=qa/application-model-tree.png
inkscape qa/robotics-model-tree.svg --export-type=png --export-filename=qa/robotics-model-tree.png
```

The XML/integrity suite checks both theme variants of every icon, its safe elements, local references, hash, bilingual metadata and normalized geometry. The raster audit checks all entries for blank output, painting outside the viewBox and identical color-normalized renders. Script-level app tests cover filtering, bilingual search, infinite loading, filtered detail navigation, clipboard fallback and download content.

The pdxadv review adds nine source-verified analysis/design commands while preserving all 410 existing SVGs. See the [nine additions on light / dark / checker backgrounds](qa/pdxadv-themes.png). The previous CAX Studio review checked all 403 baseline symbols visually, seven new commands, 11 focused geometry corrections, and a preview-only dark palette. See [before / after geometry](qa/quality-before-after.png) and [light / dark / checker examples](qa/theme-preview.png). The dark palette preserves separate body, ink, accent, warning and opaque-cutout roles; that historical preview-only behavior is superseded by the explicit standalone theme selection above.

The standalone-theme audit embeds actual file bytes without host CSS in an atlas with 16 / 24 / 32 px output cells, plus dark variants on #192c3c, #23262b and #121212. It checks nonblank output, light/dark alpha preservation and meaningful contrast pixels in that atlas. Inkscape may resample embedded images from their intrinsic 32 px size; these are not direct native-size vector exports. The separate PNG audit directly exports original files at all seven requested sizes. Copy/download tests require exact byte equality with every selected file.

**The DOM harness is not a browser layout engine.** Separate live Chrome checks passed for gallery/navigation, native Escape/focus restoration, exact SVG clipboard bytes, and selected light/dark 64 px PNG downloads. Live ZIP checks passed for both complete 419-file SVG archives (byte-exact), both complete 32 px PNG archives (valid RGBA with matching alpha), filtered downloads, cancellation and native Escape. Mobile, other browsers and assistive-technology behavior remain unverified. See [QA coverage and manual checklist](docs/QA.md).

## Files and license

- `icons/`: 693 original light SVG files; only reviewed semantic entries
- `icons-dark/`: generated standalone dark variants of the same IDs
- `src/themes.py`, `src/theme_baseline_hashes.json`: single palette source and byte-preservation regression for all 419 originals
- `src/core.py`, `src/common.py`, `src/engineering.py`, `src/extension.py`, `src/application.py`, `src/robotics.py`, `src/studio.py`, `src/pdxadv.py`: hand-authored geometry
- `src/application_commands.json`, `src/application_reuse.json`: individually reviewed meanings, references and aliases
- `src/robotics_commands.json`, `src/robotics_reuse.json`: robotics functions, persistent objects, references and reuse decisions
- `src/studio_commands.json`, `src/studio_reuse.json`: commit-pinned CAX implementation evidence and reuse decisions
- `src/pdxadv_commands.json`, `src/pdxadv_reuse.json`: pinned analysis/design meanings, limits and existing-result reuse
- `src/pdxadv_baseline_hashes.json`: byte-preservation regression hashes for all 410 baseline SVGs
- `src/quality_review.json`: reviewed original geometry and correction rationale
- `src/usage.py`: reviewed reuse, object types and model-tree names
- `scripts/`, `tests/`: deterministic build and verification tools
- `qa/`: category contact sheets and complete raster-audit summary
- `docs/`: scope, taxonomy references and QA limits

[MIT](LICENSE). All geometry is original. Vendor documentation informs feature taxonomy, not icon artwork. These UI symbols are schematic, not certified GD&T notation, simulation results or safe robot programs.

## 日本語

一般アプリ操作とCAD/CAM/CAE/CMM/ロボットOLP向けの独自SVGアイコン集です。新規・開く・保存などの基本操作に加え、他アプリの実在機能を参考に、メッシュ編集、自由曲面、点群処理、板金・溶接・金型、2D編集、加工、解析前後処理、ロボット軌道計画を追加しました。

ロボティクスの46用途に加え、cax-studioと関連リポジトリの実装から不足していた7用途を追加しました。さらにpdxadvの実装を根拠に、そり感度・肉厚対策・局所肉厚変更・結果分布・比較・基準保持・解析レポートの9用途を追加しました。今回のGUI拡充後は全693件、186件がモデルツリーに対応します。各IDにライト／ダークの独立SVGを用意しましたが、用途の件数は693件です。ダーク版はCSSなしで使えます。切り欠きなどの不透明な塗りは背景色#192c3cに固定して重なりを保つため、別の背景では色の差が見える場合があります。今回のテーマ追加では元の419件をバイト単位で維持しています。先のpdxadv用途追加では既存410件のSVGを変更していません。認識されたねじやメッシュ変換方式などは既存SVGを再利用し、件数を増やしていません。全403件の目視監査で見つかった形状の問題・改善点を11件修正し、ダーク背景で内部線が消える配色も改善しました。

断面形状・軌跡・表示状態の掛け算による件数合わせは行いません。全件に日英の名前・タグ・用途説明、role/usages、参照資料があります。追加一覧、11件の修正前後、light/dark/checker見本、70行の16pxロボット階層見本を同梱しています。アイコンとメタデータだけを作成し、実機接続・操作は行いません。詳細画面からライト／ダークの透過PNGも16・24・32・48・64・128・256pxで保存できます。プレビュー背景は含めず、重なりを隠す内部の不透明な塗りはそのまま保持します。一覧は96件ずつの無限スクロールに対応し、「Load more」でも追加できます。詳細は左右のボタン・矢印キーで絞り込み結果全体を前後移動できます。テーマ変更時は背景も連動し、その後はチェック柄などへ手動変更できます。検索横の「Download ZIP」で全693件または絞り込み結果全体を一括保存できます。SVG／透過PNG、ライト／ダーク、PNGサイズを選べ、進捗表示・キャンセルにも対応します。公開ページでは一覧・詳細移動、Escapeとフォーカス復帰、SVGコピー、選択した64px PNGをChromeで確認済みです。一括ZIPも全419件の両テーマSVG・32px PNG、絞り込み結果、キャンセルを確認済みです。モバイル・他ブラウザの検証は別途必要です。
