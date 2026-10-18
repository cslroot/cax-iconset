# CAX Iconset

Original rounded SVG symbols for everyday application commands, model-tree objects and CAD, CAM, CAE, CMM and Robotics / OLP. Every entry has a semantic ID, English and Japanese names, bilingual search tags, and a one-sentence purpose in both languages.

**The collection is organized by meaning, not by a target icon count.** Shape/profile/trajectory combinations have been removed from the catalog, source generator and exported SVGs. The previous collection remains recoverable in Git history.

![pdxadv analysis and design additions](qa/pdxadv-additions.png)

## Coverage

<!-- coverage:start -->
| Primary category | Symbols |
| --- | ---: |
| Common | 73 |
| CAD | 135 |
| CAM | 44 |
| CAE | 61 |
| CMM | 34 |
| OLP | 72 |
| **Total** | **419** |

Primary roles: 398 commands, 9 selectable tools, 9 objects and 3 status symbols. Every SVG is counted once.

186 entries support model-tree use, including reused command/tool symbols; these are not additional SVGs.
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

Open `http://127.0.0.1:8000` in a modern browser. No public deployment is configured or claimed.

- English / Japanese name, tag and purpose search, with multiple AND-matched terms
- Common and five engineering-category filters; 96-item pagination
- Independent usage filter: commands, model-tree nodes, tools and status
- Contextual node names; existing feature, material, mesh, condition and result SVGs are reused
- [Robotics model trees at native 16 px](qa/robotics-model-tree.png), [general model-tree integration](qa/model-tree.png) and [fabrication/mesh/analysis trees](qa/application-model-tree.png)
- 16 / 24 / 32 / 48 / 64 px previews; light / dark / checker backgrounds
- Detail view with bilingual purpose, copy SVG and individual SVG download
- Keyboard focus, `/` search shortcut, native dialog and empty-state reset
- No analytics or runtime external requests

Interface labels are English; the language selector switches icon names and purpose text between English and Japanese.

## Use an icon

```html
<img src="icons/common-open-file.svg" width="32" height="32" alt="Open file">
<img src="icons/common-save.svg" width="32" height="32" alt="Save">
<img src="icons/cad-extrude.svg" width="32" height="32" alt="Extrude">
```

SVGs use basic vector elements without fonts or external resources. Each file has a title and a 32 × 32 viewBox. Namespace internal IDs if embedding multiple files inline; the catalog handles its preview IDs automatically.

`manifest.json` contains the metadata, original SVG body, SHA-256 hash, primary role, supported usages, contextual node names, category memberships and taxonomy references for each symbol. `catalog.js` contains the same data for the static app. Both are generated: edit `src/` and rebuild. The top-level `categories` counts use each icon’s primary `category` and sum to the unique SVG count; an icon’s `categories` array can also include shared disciplines. `categoryMemberships` records those overlapping browser-filter counts. `role: "object"` means an object-only entry; `usages` can include both `command` and `model-tree` without making another file. See the [pdxadv analysis/design review](docs/PDXADV_REVIEW.md), the [CAX Studio coverage and geometry review](docs/CAX_STUDIO_REVIEW.md), the [robotics expansion and reuse review](docs/ROBOTICS_EXPANSION.md), the [application-family expansion review](docs/APPLICATION_EXPANSION.md) for per-function evidence and reuse decisions, and the [earlier model-tree expansion](docs/EXPANSION_REVIEW.md). The optional `aliases` field records alternate application vocabulary; shared categories still produce one SVG.

## Rebuild and verify

Python 3.10+ builds the collection. Node.js runs application tests. The optional raster audit and sheet export use an already-installed Inkscape and Pillow.

```sh
python3 scripts/build.py
python3 tests/test_catalog.py
node --check app.js
node --check catalog.js
node tests/test_app.js
python3 scripts/raster_audit.py
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

The XML/integrity suite checks every SVG, its safe elements, local references, hash, bilingual metadata and normalized geometry. The raster audit checks all entries for blank output, painting outside the viewBox and identical color-normalized renders. Script-level app tests cover filtering, bilingual search, pagination, detail interactions, clipboard fallback and download content.

The pdxadv review adds nine source-verified analysis/design commands while preserving all 410 existing SVGs. See the [nine additions on light / dark / checker backgrounds](qa/pdxadv-themes.png). The previous CAX Studio review checked all 403 baseline symbols visually, seven new commands, 11 focused geometry corrections, and a preview-only dark palette. See [before / after geometry](qa/quality-before-after.png) and [light / dark / checker examples](qa/theme-preview.png). The dark palette preserves separate body, ink, accent, warning and opaque-cutout roles; copied/downloaded SVGs keep their original colors.

**These checks are not a real-browser integration test.** Browser layout, native dialog focus/Escape, actual system clipboard and saved downloads remain unverified. See [QA coverage and manual checklist](docs/QA.md).

## Files and license

- `icons/`: individual SVG files; only reviewed semantic entries
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

ロボティクスの46用途に加え、cax-studioと関連リポジトリの実装から不足していた7用途を追加しました。さらにpdxadvの実装を根拠に、そり感度・肉厚対策・局所肉厚変更・結果分布・比較・基準保持・解析レポートの9用途を追加しました。全419件、186件がモデルツリーに対応します。今回の追加では既存410件のSVGを変更していません。認識されたねじやメッシュ変換方式などは既存SVGを再利用し、件数を増やしていません。全403件の目視監査で見つかった形状の問題・改善点を11件修正し、ダーク背景で内部線が消える配色も改善しました。

断面形状・軌跡・表示状態の掛け算による件数合わせは行いません。全件に日英の名前・タグ・用途説明、role/usages、参照資料があります。追加一覧、11件の修正前後、light/dark/checker見本、70行の16pxロボット階層見本を同梱しています。アイコンとメタデータだけを作成し、実機接続・操作は行いません。実ブラウザ統合検証は未実施です。
