# Conditional GUI binding review

This review covers exactly the 180 uncertain rows in the frozen 1,089-row source audit. It adds 21 independently reviewed original glyphs to the published 693-icon baseline; the catalog now has 714 semantic entries. All 693 previous records and both SVG variants are unchanged.

## What these results mean

- `direct`: an existing glyph directly describes the command meaning.
- `conditional-reuse`: artwork is usable only under the explicit context, label, state and routing requirements. This is not standalone icon-only equivalence.
- `new-art`: new original artwork supplies a missing meaning; command-specific conditions still apply.
- `unresolved`: at least one source-level branch remains unverified, even where some branches now have artwork.
- No row verifies an implemented consumer GUI. The JSON is a declarative integration contract, not executable dispatch logic. Do not infer success, permissions, network upload, a solver run or transaction completion from a glyph.

## Row outcomes

- conditional-reuse: 145
- direct: 2
- new-art: 31
- unresolved: 2

The original audit statuses are preserved. See [machine-readable policy](../command-bindings.json) and [sortable resolution table](GUI_BINDING_RESOLUTIONS.csv).

## Source and interpretation corrections

- SOLIDWORKS Mate uses its documented standard/advanced/mechanical relation taxonomy, not SolidCraft’s joint-type menu.
- Selection filters restrict pick eligibility; they do not hide matching display objects. Labels and selected states are mandatory.
- Cosmetic threads do not create modeled threads. Lightweight weld graphics are not modeled weld solids.
- Motion Trace samples positions without modifying the design; Keep Motion Trace creates persistent geometry.
- Universal Joint reuses crossed-yoke artwork only with the documented coupled input/output shaft motion.
- Mates in path to ground is a discrete graph status, not a creation command and not removed from the audit denominator.
- Current and older official documentation versions remain identified in each row’s source URLs. No broader product/add-in/menu coverage is claimed.

## Genuine remaining source limits

### SolidCraft: solid.press_pull

Existing glyph families cover resolved branches only. Official material still does not establish the face extrusion-versus-offset dispatch algorithm; this is an evidence gap rather than a request for arbitrary extra art.

- The exact algorithm selecting face extrusion versus normal offset remains undocumented in reviewed official material. New art would not establish that algorithm.

### SolidCraft: joint.as_built

The seven kinematic type routes now include a dedicated cylindrical glyph, always with explicit as-built placement preservation. Acceptance of the six geometric relation names remains unestablished and this dispatcher is therefore still unresolved.

- Acceptance of parallel, perpendicular, angle, point_on_plane, point_on_line and line_on_plane by joint.as_built is not independently established.

## New original glyphs

| ID | English / 日本語 | Meaning |
| --- | --- | --- |
| common-measure-geometry | Measure geometry / 形状を測定 | Inspect geometric measurements such as distance, angle, radius, coordinates or area without creating a persistent model or drawing dimension. |
| common-launch-external-service | Open external application or service / 外部アプリ・サービスを開く | Open the explicitly named external application or service; launching alone does not mean transferring a model, solving, requesting a quote or placing an order. |
| cad-replace-selected-object | Replace selected object / 選択オブジェクトを置換 | Substitute one selected geometric object or component for another; the command context specifies reference-transfer policy. |
| cad-transform-selected-face | Transform selected face / 選択面を変換 | Translate or rotate a selected face while retaining the surrounding body context; normal offset is one mode, not the entire operation. |
| cad-deform-shape | Deform shape / 形状を変形 | Change surface or solid shape without implying an enclosing control cage; the labeled command selects its actual deformation method. |
| cad-align-body | Align body to reference / ボディを参照に整列 | Move and orient a body by matching a selected source reference to a target point, face, or plane; this does not create a persistent mate. |
| cad-surface-planar | Create planar surface / 平面サーフェスを作成 | Create a bounded flat surface body without thickness; not a curved fill or construction datum plane. |
| cad-wrap-profile | Wrap profile onto face / 輪郭を面へラップ | Map sketch contours onto a face, including no-depth Scribe imprints; material addition or removal is a separately labeled mode. |
| cad-groove-bead | Create solid gap weld / ソリッドの隙間溶接を作成 | Create weld material as a solid body in the gap between selected surfaces; not a cosmetic bead annotation. |
| cad-design-study | Evaluate design scenarios / 設計シナリオを評価 | Evaluate or optimize candidate designs from variables, constraints and goals; the visible mode distinguishes evaluation from optimization and does not imply a physics solve. |
| cad-manufacturability-check | Check manufacturability / 製造性を検証 | Check a part against configured design-for-manufacture rules without implying geometric validity checks, automatic repair or fabrication execution. |
| cad-author-asset-references | Define asset placement references / アセット配置参照を定義 | Prepare a local layout asset by defining its ground attachment and outward connection points or directions, not by mating existing assets or uploading them. |
| cad-publish-model-cloud | Publish model to remote service / モデルを外部サービスに公開 | Transfer a model for publication to an explicitly named remote service; the workflow defines the audience and does not imply local export or continuous synchronization. |
| cad-annotation-note | Place annotation note / 注記を配置 | Place plain or property-linked annotation text without requiring a geometry leader or creating sketch profiles. |
| cad-cylindrical-joint | Cylindrical joint / 円筒ジョイント | Allow independent rotation about and translation along one common axis, without a screw-pitch relationship. |
| cad-line-on-plane | Constrain line to plane / 直線を平面上に拘束 | Keep an entire line on a reference plane, with any permitted offset explicitly specified by the command. |
| cad-linear-travel-limits | Set linear travel limits / 直線移動の範囲を制限 | Set minimum and maximum translation along a joint or mate axis; not a fixed separation or an angular bound. |
| cad-define-forming-tool | Define forming tool / フォームツールを定義 | Define reusable sheet-forming tool geometry through stopping/removal faces and an insertion reference; does not apply or stamp the tool. |
| cad-solid-corner-weld | Create modeled corner weld / ソリッドの隅肉溶接を作成 | Create modeled weld material at meeting faces or a folded sheet corner; sheet-specific options and flattening behavior belong to the command binding. |
| cad-mate-path-to-ground | Mate path to ground / 固定部までの合致経路 | Status marker identifying a mate relation on the graph path to a grounded component; not a command to fix or lock components. |
| cae-simulation-overlay | Display simulation in model context / モデル上に解析結果を表示 | Overlay a stored simulation result on its CAD model or assembly context, without selecting a particular result type or starting a solver. |

## Validation and delivery

Full catalog and binding tests pin all published 693 records/SVG hashes, require all 180 rows exactly once, validate IDs and sources, and trace every new glyph to a binding. XML, geometry duplication, native light/dark rendering, clipping, contrast, PNG export and application/ZIP regressions are rerun after integration. Native preview sheets and raw validation outputs are in the complete delivery package; they are not proof of browser or assistive-technology integration.

This follow-on unit preserves the previously published 693-icon commit as its baseline. Consult repository history for the publication state of this revision.
