# Design, references and scope

## 4,805 original SVGs, with explicit provenance

This library contains **100 core symbols** (20 in each discipline) and **4,705 contextual variants**. It does not claim to contain 4,805 independent software commands. The variants combine an operation with a named profile, face or process trajectory. They are useful where a product needs a context-specific symbol, but should not replace a concise core toolbar indiscriminately.

| Primary category | Core | Context variants | Total |
| --- | ---: | ---: | ---: |
| CAD | 20 | 1,011 | 1,031 |
| CAM | 20 | 1,120 | 1,140 |
| CAE | 20 | 1,120 | 1,140 |
| CMM | 20 | 1,064 | 1,084 |
| Robotics / OLP | 20 | 334 | 354 |
| Shared / Common | 0 | 56 | 56 |
| **Unique files** | **100** | **4,705** | **4,805** |

The 56 centroid symbols are stored once in Common and discoverable in both CAD and CMM. Therefore category-filter counts overlap: CAD displays 1,087; CMM displays 1,140; Common displays 56. The all-icons total does not double-count them.

## Visual language

- 32 × 32 viewBox; main stroke 1.75 px; rounded caps and joins
- Navy `#253b53`, teal `#178b88`, pale teal `#d7efed`, limited amber `#c88626`
- Geometry communicates the operation; color is supplementary
- No recolored or rotated copies are counted as separate icons
- Names, Japanese names, tags, categories, family, context, source IDs and content hashes are available in `manifest.json`
- SVGs contain paths and basic shapes only: no scripts, fonts, raster images, foreign objects or external resources
- The dark preview adapts strokes for inspection; copied/downloaded SVGs preserve the library palette

## How the collection was formed

The core set was drawn as original vector geometry. Public documentation of commercial and open-source engineering applications informed the **feature taxonomy**, not the artwork. No vendor icon artwork is copied or bundled. These references do not endorse the library and do not prove that every generated context exists as an individual vendor command.

The parametric set uses 56 named profiles and 16 robot-trajectory contexts. CAD/CAM/CAE/CMM recipes integrate operations into the geometry: sections, paths, mesh/field marks, probes, dimensions and boundaries. OLP recipes combine a pictured process tool with a trajectory. Compatibility exclusions remove selected unsuitable combinations, including corner treatments of smooth curves, thin walls on already-hollow profiles, and continuous-curved contexts for point-contact sequences. This is curated schematic coverage, not an exhaustive engineering-compatibility solver.

Sources were reviewed for this project's taxonomy on 2026-10-17. The SOLIDWORKS page is an explicitly historical feature overview; this is not a current-version product feature comparison.

| Source ID | Primary documentation | Taxonomy used |
| --- | --- | --- |
| freecad | [FreeCAD features](https://www.freecad.org/features) | Parametric CAD, sketches, parts, workbenches |
| solidworks | [SOLIDWORKS Features Overview](https://help.solidworks.com/2012/english/SolidWorks/sldworks/Features_Overview.htm) | Features, cuts, fillets, chamfers, patterns |
| fusion | [Autodesk Fusion features](https://www.autodesk.com/products/fusion-360/features) | Manufacturing, milling, toolpaths |
| linuxcnc | [LinuxCNC G-code reference](https://linuxcnc.org/docs/html/gcode.html) | Motion, coordinates, interpolation, cycles |
| ansys | [Ansys Mechanical datasheet](https://www.ansys.com/content/dam/product/structures/mechanical-datasheet.pdf) | Structural, thermal, modal, contact analysis |
| openfoam | [OpenFOAM user guide](https://www.openfoam.com/documentation/user-guide) | Meshes, boundaries, flow, fields |
| gmsh | [Gmsh manual](https://www.gmsh.info/doc/texinfo/gmsh.html) | Geometry and mesh elements |
| pcdmis | [Hexagon PC-DMIS](https://hexagon.com/products/pc-dmis) | Dimensional inspection and probing |
| calypso | [ZEISS CALYPSO](https://www.zeiss.com/metrology/en/software/zeiss-calypso.html) | Metrology and measurement planning |
| robodk | [RoboDK robot programs](https://robodk.com/doc/en/Robot-Programs.html) | Robot targets, programs and motion |
| moveit | [MoveIt concepts](https://moveit.ai/documentation/concepts/) | Planning, kinematics, collision checking |

## Intended use and limits

These are interface illustrations, not executable CAM/robot programs, finite-element results, manufacturing drawings or certified GD&T symbols. Profile offsets, field patterns, mesh lines, probes and centroids are illustrative, not exact engineering computations. Some small contextual symbols are visually similar; 24–32 px or larger is recommended, and 16 px should be checked in the intended UI. Raster uniqueness is a byte-level test, not a perceptual-distinctness guarantee. No individual semantic expert review of every variant is claimed.

All artwork and code are offered under the repository's [MIT license](../LICENSE). Product names belong to their owners and appear only to identify research sources.

## 日本語での概要

4,805個の内訳は基本シンボル100個と、形状・加工・測定・軌跡の文脈を組み合わせた派生4,705個です。4,805種類の独立したソフトウェアコマンドを意味しません。色替え・回転だけの水増しはせず、CAD/CMMで同じ意味になる図心は共通化しました。商用・OSSの一次資料は機能分類の参考とし、既存製品のアイコンは複製していません。

図形はUI向け模式図です。正確な工具経路・計算結果・安全なロボットプログラム・規格適合記号として利用しないでください。実ブラウザでのレイアウト、クリップボード、ダウンロードの統合検証は未実施です。実施済みの検査と残る制約は [QA](QA.md) に記載しています。
