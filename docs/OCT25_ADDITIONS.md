# October 25 additional icons (A/B)

42 original icons: A 25 current substitutions and B 17 future-function requests. Catalog 800 meanings / 1,600 light and dark SVGs. All 758 prior records and SVG pairs are unchanged. IDs match the user proposal exactly.

This is an icon library delivery, not Studio, Viewer or PDxAdv integration. No runtime feature availability is claimed. SDF here means signed distance field, not SDFormat. The expanded-tree glyph is a status/disclosure mark; consumers must supply accessible state labels.

| Section | ID | Japanese | Meaning |
| --- | --- | --- | --- |
| A | `cad-rotate-selected-face` | 選択面を回転 | Rotate a selected face about an axis; distinct from translating that face. |
| A | `cad-silhouette-edges` | シルエットエッジ表示 | Show view-dependent silhouette contours, not all topological model edges. |
| A | `cad-ground-shadow` | 床面の影 | Show a shadow cast onto a floor plane rather than shadows between scene objects. |
| A | `cad-shadow-maps` | シャドウマップ | Enable object-to-object shadow casting; distinct from an isolated floor shadow. |
| A | `cad-selection-filter-component` | 部品選択フィルタ | Restrict picking to whole assembly components, not individual faces. |
| A | `cad-selection-filter-face` | 面選択フィルタ | Restrict picking to topological faces. |
| A | `cad-selection-filter-face-edge` | 面と稜線の選択フィルタ | Allow picking faces and edges together; not generic object selection. |
| A | `cad-face-reblend` | 面のフィレット付け直し | Reconstruct a blend after editing neighboring faces rather than create a first fillet. |
| A | `cad-copy-face-feature` | 面形状フィーチャーのコピー | Copy a face-defined feature to another location, not a linear pattern. |
| A | `cad-sketch-fillet` | スケッチの角丸め | Replace a planar sketch corner by a tangent arc, not a solid-edge fillet. |
| A | `cad-sketch-chamfer` | スケッチの面取り | Replace a planar sketch corner by a straight bevel segment. |
| A | `cad-sketch-radius-dimension` | スケッチ半径寸法 | Dimension the radius from a circle or arc center to its curve. |
| A | `cad-sketch-clear` | スケッチを全消去 | Remove all geometry in the active sketch, not delete the sketch object. |
| A | `cad-edit-feature` | フィーチャーを編集 | Open a feature definition for editing; simplified silhouette for 16px tree-row buttons. |
| A | `cad-attach-reference` | 側面参照を追加 | Attach a side reference to a feature or part, not a generic hyperlink. |
| A | `cad-component-list` | 部品一覧 | Show a list of assembly components rather than create a single part. |
| A | `cad-open-sheet-metal-sample` | 板金サンプルを開く | Open a sheet-metal example, distinct from the general sample chooser. |
| A | `common-reset` | 既定値に戻す | Restore default settings rather than refresh or reload current data. |
| A | `common-background-color` | 背景色 | Choose the viewport background color, not the object material color. |
| A | `cad-surface-lit` | 通常ライティング | Shade surfaces using scene lighting, distinct from matcap and zebra analysis. |
| A | `cad-markup-freehand` | フリーハンドマークアップ | Draw a freehand review annotation, not an editable sketch spline. |
| A | `cad-markup-circle` | 円マークアップ | Draw a circular review annotation without creating sketch geometry. |
| A | `cad-markup-rectangle` | 矩形マークアップ | Draw a rectangular review annotation without creating sketch geometry. |
| A | `cae-export-pptx-report` | PowerPointレポート出力 | Export an analysis report as a PowerPoint presentation, not an HTML report. |
| A | `common-tree-node-expanded` | ツリー展開マーク | Indicate an expanded tree node; a downward disclosure chevron. |
| B | `cad-implicit-body` | 陰関数ボディ | Represent an implicit isosurface rather than an exact boundary representation. |
| B | `cad-sdf-convert` | SDFへ変換 | Convert geometry to a signed distance field; not SDFormat robot export. |
| B | `cad-csg-tree` | CSG演算ツリー | Inspect constructive-solid-geometry operands and Boolean operations. |
| B | `cad-lattice-gyroid` | ジャイロイド格子 | Create a smooth triply periodic gyroid-style lattice rather than rod struts. |
| B | `cad-lattice-rod` | ロッド格子 | Create connected straight lattice struts, distinct from a gyroid sheet lattice. |
| B | `cae-mesh-settings` | メッシュ設定 | Configure mesh generation parameters rather than solver settings. |
| B | `cae-mesh-refine-region` | 領域メッシュ細分化 | Apply local mesh refinement inside a selected region. |
| B | `cae-boundary-layer` | 境界層設定 | Configure layered cells next to a wall, not a generic tetrahedral mesh. |
| B | `common-timeline` | タイムライン | Open the time axis and keyframe track for animation. |
| B | `common-record` | アニメーション記録 | Start recording animation or keyframe capture; not playback. |
| B | `common-loop` | ループ再生 | Repeat animation playback rather than reset its parameters. |
| B | `common-playback-speed` | 再生速度 | Adjust the animation time multiplier without changing recorded motion. |
| B | `common-step-forward` | 1ステップ進む | Advance animation by one frame or discrete step. |
| B | `common-step-back` | 1ステップ戻る | Move animation back by one frame or discrete step. |
| B | `cad-pmi-edit` | PMIを編集 | Edit a product-manufacturing annotation, not geometry parameters. |
| B | `cad-pmi-associate` | PMIを形状へ関連付け | Associate a PMI annotation to an explicit geometric target. |
| B | `cad-quad-remesh` | 四角形リメッシュ | Remesh a surface into a quadrilateral layout, distinct from generic remeshing. |

## Verification

22 Python catalog/acceptance tests, app and ZIP harnesses, raster uniqueness/bounds checks, native 16/24/32 px light/dark previews. Static rendering is not live consumer UI validation. Existing generic icons remain available; no consumer files are changed.
