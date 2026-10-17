# Design, references and scope

## Semantic entries, not shape multiplication

Each catalog entry represents a distinct application command, engineering tool, or interface status. All entries have a semantic ID, English and Japanese names/tags, and one-sentence usage descriptions in both languages. A shared operation is listed once; a differently shaped part or a different trajectory does not create another icon.

The earlier operation × profile/trajectory generator has been removed, along with its exported variants and contact sheets. It can be recovered from the preceding commit in Git history, but is not part of the current library or build path. No numerical target is used to expand the collection.

<!-- coverage:start -->
| Category | Symbols |
| --- | ---: |
| Common | 69 |
| CAD | 58 |
| CAM | 26 |
| CAE | 27 |
| CMM | 25 |
| OLP | 27 |
| **Total** | **232** |

Roles: 224 commands, 5 selectable tools and 3 status symbols. Every symbol is counted once.
<!-- coverage:end -->

The manifest `role` field distinguishes commands from selectable tools and status symbols. In particular, information, warning and error symbols are not additional software commands. Categories do not overlap, so the sum of their counts equals the number of SVG files.

## Inclusion rules

- Include genuinely different actions: Save, Save as and Save all have different effects on files
- Keep common actions in Common instead of repeating them under every engineering discipline
- Include domain-specific actions only when their purpose differs, such as solving an analysis versus simulating robot motion
- Preserve meaningful engineering distinctions such as machining with a flat-end versus a ball-end cutter, rather than generating either operation for many decorative profiles
- Exclude mere recolorings, rotated copies, section-shape swaps, trajectory swaps and state-badge grids
- Draw each added command deliberately; reusable drawing primitives are stylistic building blocks, never a Cartesian-product catalog generator
- Use descriptions and source taxonomy to review meaning; XML and raster uniqueness alone are insufficient

## Visual language

- 32 × 32 viewBox, 1.75 px main stroke, rounded caps and joins
- Navy `#253b53`, teal `#178b88`, pale teal `#d7efed`, limited amber `#c88626`
- Geometry carries meaning; color is supplementary
- SVG paths and basic shapes only: no scripts, fonts, raster images, foreign objects or external resources
- Dark preview adapts strokes for inspection; downloaded SVGs retain the library palette
- Contact sheets show every entry at 48, 24 and 16 px

## Primary taxonomy references

Vendor and OSS documentation informs the functional taxonomy, not the artwork. No vendor icon geometry is copied or bundled. Product names identify sources and do not imply endorsement. The collection does not claim that every item is a separately named command in every cited application. Some sources intentionally describe historical versions.

<!-- references:start -->
| Source | Primary documentation | Taxonomy |
| --- | --- | --- |
| fusion-drawing | [Fusion Drawing toolbar](https://help.autodesk.com/cloudhelp/ENU/Fusion-Drawing/files/DWG-REF-DRAWING-TAB.htm) | Drawing creation, projected/detail views, dimensions and annotations |
| solidworks-standard | [SOLIDWORKS standard toolbar](https://help.solidworks.com/2017/english/SolidWorks/sldworks/r_Standard.htm?id=2.11.3.1.31) | File and edit commands; historical taxonomy reference |
| inventor-files | [Inventor save and export files](https://help.autodesk.com/cloudhelp/2025/ENU/Inventor-Help/files/GUID-08D6DD13-3066-4210-9F19-5F7E8DB8AD5D.htm) | Save, save as, and export operations |
| fusion-selection | [Fusion selection tools](https://help.autodesk.com/view/fusion360/ENU/?guid=SLD-SELECTION) | Window, crossing and freeform selection semantics |
| inventor-assembly | [Inventor assembly workflow](https://help.autodesk.com/cloudhelp/2024/ENU/Inventor-Help/files/GUID-AB69CA08-CD95-410C-9E72-49CCBB858915.htm) | Assembly placement, constraints, and analysis |
| fusion-milling | [Fusion milling workflow](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/MFG-OVERVIEW-MILLING-WORKFLOW.htm) | Setup, tooling, toolpath generation, simulation and NC output |
| fusion-simulation | [Fusion simulation setup](https://help.autodesk.com/cloudhelp/ENU/Fusion-Simulate/files/SIM-SETUP-TAB.htm) | Study, materials, constraints, loads, contacts, mesh, precheck and solve |
| pcdmis-quickstart | [PC-DMIS Quick Start interface](https://docs.hexagonmi.com/pcdmis/2023.1/en/helpcenter/mergedprojects/core/10_view_topics/Quick_Start_Interface.htm) | Probe setup, calibration, alignment, features and dimensions |
| freecad | [FreeCAD features](https://www.freecad.org/features) | Parametric modeling, sketches, parts and workbenches |
| solidworks | [SOLIDWORKS Features Overview](https://help.solidworks.com/2012/english/SolidWorks/sldworks/Features_Overview.htm) | Feature-based solids, cuts, fillets, chamfers and patterns; historical taxonomy reference |
| fusion | [Autodesk Fusion features](https://www.autodesk.com/products/fusion-360/features) | CAD/CAM, manufacturing, milling and toolpath workflows |
| linuxcnc | [LinuxCNC G-code reference](https://linuxcnc.org/docs/html/gcode.html) | Motion, coordinates, interpolation and machining cycles |
| ansys | [Ansys Mechanical datasheet](https://www.ansys.com/content/dam/product/structures/mechanical-datasheet.pdf) | Structural, thermal, modal and contact analysis |
| openfoam | [OpenFOAM user guide](https://www.openfoam.com/documentation/user-guide) | Mesh, boundary conditions, flow and field concepts |
| gmsh | [Gmsh reference manual](https://www.gmsh.info/doc/texinfo/gmsh.html) | Geometry, meshing and mesh elements |
| pcdmis | [Hexagon PC-DMIS](https://hexagon.com/products/pc-dmis) | Dimensional inspection, probing and metrology |
| calypso | [ZEISS CALYPSO](https://www.zeiss.com/metrology/en/software/zeiss-calypso.html) | Dimensional metrology and measurement planning |
| robodk | [RoboDK robot programs](https://robodk.com/doc/en/Robot-Programs.html) | Robot programming, targets and motion instructions |
| moveit | [MoveIt concepts](https://moveit.ai/documentation/concepts/) | Motion planning, kinematics and collision checking |
<!-- references:end -->

## Intended use and limits

These are schematic UI illustrations, not executable machining/robot programs, finite-element results, exact geometry calculations, manufacturing drawings or certified GD&T symbols. Review them at the intended display size, contrast and usage context. The set is selective rather than exhaustive.

All artwork and code use the repository's [MIT license](../LICENSE). See [QA](QA.md) for precisely what was tested and the remaining browser-verification limits.

## 日本語

断面形状・軌跡を掛け合わせた派生を削除し、一般操作と実際の専門機能ごとに整理したアイコン集です。件数を増やすための色替え・回転・形状差し替えは採用しません。保存／名前を付けて保存／すべて保存のように実際の動作が異なるものは別項目とし、警告などの状態シンボルはコマンドと区別しています。

一次資料は機能分類の参考であり、他製品のアイコンは複製していません。各図柄はUI向け模式図です。正確な計算結果、安全なロボットプログラム、規格適合記号の代用にはできません。
