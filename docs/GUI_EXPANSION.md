# CAD GUI expansion

Reviewed on 2026-10-24 against main 04057de766e4b2694593f47a82690f32bdedfc27.

Historical first GUI pass: 30 new meanings, 449 total at that checkpoint. Light/dark are variants, not additional meanings. All 419 original SVGs in both themes are byte-preserved. Artwork is original; vendor documentation provides command taxonomy only.

This is a focused gap-filling pass, not complete coverage of either product. A documented SolidCraft command is not a promise that every upstream operation is implemented or robust. Planned surface fillet was not included.

## New command mapping

| CAX ID | English / 日本語 | Source command aliases | Purpose |
| --- | --- | --- | --- |
| cad-boundary-fill | Boundary fill / 境界充填 | solid.boundary_fill | Create a solid cell enclosed by intersecting boundaries. |
| cad-emboss | Emboss / エンボス | solid.emboss | Raise or recess a profile on a target face. |
| cad-pattern-path | Pattern along path / パス配列 | solid.pattern.path | Repeat a feature or body along a selected curve. |
| cad-mounting-boss | Mounting boss / 取付ボス | plastic.boss | Create a supported mounting boss for a plastic part. |
| cad-lip-groove | Lip and groove / リップと溝 | plastic.lip | Create complementary mating lips and grooves on plastic part edges. |
| cad-snap-fit | Snap fit / スナップフィット | plastic.snap_fit | Create a flexible hook that latches into a mating recess. |
| cad-configuration-table | Configuration table / コンフィギュレーション表 | config.table | Display parameter combinations and current state across named model configurations. |
| cad-history-rollback | Roll back history / 履歴ロールバック | timeline.rollback | Move the active history position back before later features. |
| cad-curvature-comb | Curvature comb / 曲率コーム | inspect.curvature_comb | Display curvature magnitude as normal comb teeth along a curve. |
| cad-curvature-map | Curvature map / 曲率マップ | inspect.curvature_map | Visualize surface curvature as a spatial field. |
| cad-continuity-analysis | Continuity analysis / 連続性解析 | inspect.continuity | Inspect position, tangent and curvature continuity across adjoining surfaces. |
| cad-isocurve-analysis | Isocurve analysis / 等パラメータ線解析 | inspect.isocurve | Display constant-parameter curves to inspect a surface shape. |
| cad-minimum-radius-analysis | Minimum radius analysis / 最小半径解析 | inspect.minimum_radius | Locate regions of minimum curvature radius on geometry. |
| cad-compare-bodies | Compare bodies / ボディ比較 | inspect.compare | Compare geometric differences between two CAD bodies. |
| cad-sketch-ellipse | Sketch ellipse / スケッチ楕円 | sketch.ellipse | Draw an elliptical sketch profile using its center and two axis lengths. |
| cad-sketch-polygon | Sketch polygon / スケッチ正多角形 | sketch.polygon.inscribed, sketch.polygon.circumscribed, sketch.polygon.edge | Draw a regular polygon by its inscribed circle, circumscribed circle or edge. |
| cad-sketch-slot | Sketch straight slot / スケッチ直線スロット | sketch.slot.center_point, sketch.slot.center_to_center, sketch.slot.overall | Draw a straight slot profile with parallel sides and semicircular ends. |
| cad-sketch-text | Sketch text / スケッチ文字 | sketch.text | Insert text into a sketch for use in profiles, labels or engraved features. |
| cad-sketch-construction-line | Sketch construction line / スケッチ補助線 | sketch.centerline, sketch.construction | Create or designate a construction line used as a sketch reference rather than a profile edge. |
| cad-constraint-collinear | Collinear constraint / 同一直線上拘束 | sketch.constraint.collinear | Keep separate sketch line segments on the same infinite straight line. |
| cad-constraint-curvature | Curvature constraint / 曲率連続拘束 | sketch.constraint.curvature | Match the tangent direction and curvature of two curves at their shared endpoint. |
| cad-sketch-auto-constrain | Auto constrain sketch / スケッチ自動拘束 | sketch.auto_constrain | Automatically detect and apply geometric constraints to sketch entities. |
| cad-replace-face | Replace face / 面の置換 | solid.replace_face | Replace selected solid faces with a target surface and update the adjoining faces. |
| cad-delete-face | Delete face / 面の削除 | face.delete | Remove selected faces from a body; this is a face-level edit, not deletion of the entire body. |
| cad-split-face | Split face / 面の分割 | solid.split_face | Divide a face into separate face regions using a curve or tool without splitting the body. |
| cad-surface-extend | Extend surface / サーフェス延長 | surface.extend | Extend an existing surface beyond selected boundary edges. |
| cad-surface-untrim | Untrim surface / サーフェスのトリム解除 | surface.untrim | Remove trimming boundaries to restore the underlying surface region. |
| cad-surface-unstitch | Unstitch surfaces / サーフェス縫合解除 | surface.unstitch | Disconnect stitched surface faces into separate surface bodies. |
| cad-surface-ruled | Ruled surface / ルールドサーフェス | surface.ruled | Create a surface with straight-line generators extending from a selected edge. |
| cad-surface-reverse-normal | Reverse surface normal / サーフェス法線反転 | surface.reverse_normal | Reverse the orientation of a surface normal without changing its geometric shape. |

## Reuse instead of duplicate icons

- Polygon input methods share one icon. Straight slot construction methods share one icon; arc-slot geometry is not falsely labeled straight.
- Centerline / construction geometry share one construction-line symbol.
- Surface match reuses cad-surface-match; it is not a new surface-stitch meaning.
- Gear coupling reuses cad-joint-coupling; center of mass reuses cad-mass-properties.
- Face push/pull reuses cad-face-offset; parameter editing reuses cad-parameters; recompute reuses cad-recompute.
- Datum creation methods reuse existing plane/axis symbols. Material assignment reuses the existing shared cae-material-assignment.
- Face splitting is distinct from cad-split-body; B-rep normal reversal differs from mesh face orientation.
- History rollback changes the active history position, unlike common-history review. Body comparison is geometry, not cae-compare-results analysis fields.

## Evidence

- [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html): Parametric sketch, feature, surface, configuration and inspection command taxonomy; checked 2026-10-24.
- [SOLIDWORKS Sketch toolbar](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_sketch_toolbar.htm): Sketch creation and constraint GUI families; original CAX geometry.
- [SOLIDWORKS Surfaces toolbar](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Surfaces_Toolbar.htm): Surface creation and editing GUI families; original CAX geometry.

## Verification and limits

- XML, bilingual metadata, source registration, safe SVG, normalized geometry uniqueness and exact new-set membership checks.
- The old 419-entry theme hash file is unchanged. Its hashes are checked as a preserved subset; new entries are checked separately. All theme geometry/mask checks still apply to every entry.
- Raster audit: all entries nonblank, within viewBox, no identical color-normalized renders.
- Native PNG exports at 16/24/32/48/64/128/256 px, both themes; alpha, dimensions, file integrity and cutout checks.
- App and ZIP Node harness tests, including no IntersectionObserver fallback. Harness tests are not live-browser tests.
- New icons visually reviewed at native 16/24/32 px in light and dark. [Preview](../qa/gui-additions.png).
- No new browser/CUA, mobile, screen-reader or production integration validation; no source application functionality was changed.

Regenerate this document with scripts/update_docs.py. Regenerate the native preview with scripts/gui_sheet.py.
