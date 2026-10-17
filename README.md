# CAX Iconset

Original rounded SVG symbols for everyday application commands, model-tree objects and CAD, CAM, CAE, CMM and Robotics / OLP. Every entry has a semantic ID, English and Japanese names, bilingual search tags, and a one-sentence purpose in both languages.

**The collection is organized by meaning, not by a target icon count.** Shape/profile/trajectory combinations have been removed from the catalog, source generator and exported SVGs. The previous collection remains recoverable in Git history.

![Common application commands](qa/common.png)

## Coverage

<!-- coverage:start -->
| Primary category | Symbols |
| --- | ---: |
| Common | 70 |
| CAD | 82 |
| CAM | 31 |
| CAE | 35 |
| CMM | 25 |
| OLP | 27 |
| **Total** | **270** |

Primary roles: 254 commands, 5 selectable tools, 8 objects and 3 status symbols. Every SVG is counted once.

118 entries support model-tree use, including reused command/tool symbols; these are not additional SVGs.
<!-- coverage:end -->

- Common: new, open, recent files, close, save / save as / save all, import, export, print, undo / redo, clipboard, search / replace, filtering, selection, display, navigation and application controls
- CAD: sketching, constraints, dimensions, solid features, assembly, sheet metal, surfaces and viewing
- CAM: setup, tooling, machining operations, toolpath calculation, verification and NC output
- CAE: studies, material, mesh, boundaries, loads, contact, solver and results
- CMM: probes, calibration, alignment, measured/constructed features, tolerances and reporting
- OLP: cell setup, targets, motion, IO, simulation, verification and robot programs

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
- [Native 16 px model-tree integration specimen](qa/model-tree.png) with CAD, CAM and CAE hierarchies
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

`manifest.json` contains the metadata, original SVG body, SHA-256 hash, primary role, supported usages, contextual node names, category memberships and taxonomy references for each symbol. `catalog.js` contains the same data for the static app. Both are generated: edit `src/` and rebuild. The top-level `categories` counts use each icon’s primary `category` and sum to the unique SVG count; an icon’s `categories` array can also include shared disciplines. `categoryMemberships` records those overlapping browser-filter counts. `role: "object"` means an object-only entry; `usages` can include both `command` and `model-tree` without making another file. See the [expansion review](docs/EXPANSION_REVIEW.md) for the per-function additions and reuse decisions.

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
python3 scripts/update_docs.py
for category in common cad cam cae cmm olp additions; do
  inkscape "qa/$category.svg" --export-type=png --export-filename="qa/$category.png"
done
inkscape qa/model-tree.svg --export-type=png --export-filename=qa/model-tree.png
```

The XML/integrity suite checks every SVG, its safe elements, local references, hash, bilingual metadata and normalized geometry. The raster audit checks all entries for blank output, painting outside the viewBox and identical color-normalized renders. Script-level app tests cover filtering, bilingual search, pagination, detail interactions, clipboard fallback and download content.

**These checks are not a real-browser integration test.** Browser layout, native dialog focus/Escape, actual system clipboard and saved downloads remain unverified. See [QA coverage and manual checklist](docs/QA.md).

## Files and license

- `icons/`: individual SVG files; only reviewed semantic entries
- `src/core.py`, `src/common.py`, `src/engineering.py`, `src/extension.py`: hand-authored drawings and meanings
- `src/usage.py`: reviewed reuse, object types and model-tree names
- `scripts/`, `tests/`: deterministic build and verification tools
- `qa/`: category contact sheets and complete raster-audit summary
- `docs/`: scope, taxonomy references and QA limits

[MIT](LICENSE). All geometry is original. Vendor documentation informs feature taxonomy, not icon artwork. These UI symbols are schematic, not certified GD&T notation, simulation results or safe robot programs.

## 日本語

一般的なアプリ操作とCAD/CAM/CAE/CMM/ロボットOLP向けのSVGアイコン集です。新規・開く・保存・名前を付けて保存・印刷・検索などの共通操作を追加し、断面形状や軌跡の組合せによる派生を削除しました。件数合わせは行わず、実際の機能または用途を持つシンボルごとに整理しています。公式CAD/CAM/CAE資料を照合して38件の不足機能・オブジェクトを追加し、既存図柄の再利用を含む118件をモデルツリーに対応させました。コマンド／ツリーノード／工具／状態の用途フィルタと、16pxの階層表示見本があります。全件に意味を表すID、日英の名前・タグ・用途説明があります。旧版はGit履歴から復元できます。実ブラウザ統合検証は未実施です。
