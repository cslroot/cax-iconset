# Design, references and scope

## Semantic entries, not shape multiplication

Each catalog entry represents a distinct application command, engineering tool, persistent model object, or interface status. All entries have a semantic ID, English and Japanese names/tags, and one-sentence usage descriptions in both languages. A shared operation is listed once; a differently shaped part or a different trajectory does not create another icon.

The earlier operation × profile/trajectory generator has been removed, along with its exported variants and contact sheets. It can be recovered from the preceding commit in Git history, but is not part of the current library or build path. No numerical target is used to expand the collection.

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

The manifest `role` field identifies the primary role: command, tool, object or status. `usages` describes supported contexts and can contain both `command` and `model-tree`; reused entries are still counted once. `nodeName`, `nodeNameJa` and `objectType` provide contextual noun labels. Part definitions and their placed instances deliberately use the same part icon.

Primary categories are exclusive and sum to the SVG count. Additional category memberships reuse material, point-cloud and coordinate-system symbols across disciplines; `categoryMemberships` therefore overlaps and is used for browser filters. Information, warning and error remain status symbols. No object × state glyph matrix is produced.

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
- A separate 16 px integration specimen places reused objects in actual indented row layouts
- Model-tree object and command uses share artwork where the same concept is intended; only genuinely absent objects get new drawings
- Small pictograms require accessible names and visible labels; technical annotation symbols are schematic and not certified production marks

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
| solidworks-features-2026 | [SOLIDWORKS 2026 Features toolbar](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Features_Toolbar.htm?id=2.12.4.1.11) | Hole, thread, draft and rib feature commands |
| onshape-split | [Onshape Split](https://cad.onshape.com/help/Content/PartStudio/split.htm) | Split parts using surfaces or planes |
| onshape-thicken | [Onshape Thicken](https://cad.onshape.com/help/Content/PartStudio/thicken.htm) | Add thickness to surfaces to create solids |
| onshape-offset-surface | [Onshape Offset surface](https://cad.onshape.com/help/Content/PartStudio/offset_surface.htm) | Create a normal offset surface |
| onshape-project | [Onshape Use projected geometry](https://cad.onshape.com/help/Content/Sketch/use.htm) | Reference projected external geometry in a sketch |
| fusion-sketch-constraints | [Fusion sketch constraints](https://help.autodesk.com/cloudhelp/ENU/Fusion-Sketch/files/SKT-CONSTRAINTS.htm) | Horizontal/vertical, concentric and midpoint constraints |
| onshape-mass-properties | [Onshape Mass properties](https://cad.onshape.com/help/Content/View/mass_properties_tool.htm) | Mass, center of mass and inertia |
| fusion-mesh-convert | [Fusion Convert Mesh](https://help.autodesk.com/cloudhelp/ENU/Fusion-Mesh/files/MESH-CONVERT-TO-SOLID.htm) | Mesh bodies and conversion to B-rep |
| onshape-feature-parts | [Onshape feature and parts lists](https://cad.onshape.com/help/Content/PartStudio/features_and_parts_lists.htm) | Part, sketch and feature list objects; feature nodes reuse their creating tool icons |
| onshape-instances | [Onshape assembly instances list](https://cad.onshape.com/help/Content/Assembly/instances_list.htm) | Assemblies, component instances and their containment |
| solidworks-multibody | [SOLIDWORKS multibody overview](https://help.solidworks.com/2026/English/SolidWorks/Sldworks/c_Multibody_Overview.htm) | One part can contain multiple solid and surface bodies |
| fusion-components | [Fusion components, occurrences and proxies](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ComponentsProxies_UM.htm) | Component definitions versus placed occurrences |
| fusion-manufacture-browser | [Fusion Manufacture browser](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/GUIDB87E0180-7CDD-41B0-866C-EEDACB946E09.htm) | Setups, operation groups, folders and NC program tree organization |
| fusion-nc-program | [Fusion NC programs](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/MFG-NC-PROGRAM-OVERVIEW.htm) | NC program nodes and post-processing output |
| fusion-thread-milling | [Fusion 2D Thread](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/2D-THREAD-STEPS.htm) | Helical thread milling operation |
| fusion-holding-tabs | [Fusion 2D Contour reference](https://help.autodesk.com/view/fusion360/ENU/?contextId=MFG-REF-2D-CONTOUR-CMD) | Holding tabs left in contour cutting |
| fusion-engrave | [Fusion Engrave reference](https://help.autodesk.com/view/fusion360/ENU/?contextId=MFG-REF-2D-ENGRAVE-CMD) | V-tool engraving with sharp corners |
| fusion-cam-chamfer | [Fusion 2D Chamfer](https://help.autodesk.com/view/fusion360/ENU/?contextId=2D-CHAMFER-STEPS) | Machining edge chamfers with a cutter |
| ansys-gravity | [Ansys Mechanical Standard Earth Gravity](https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/wb_sim/ds_Gravity.html) | Gravity as an acceleration/body load |
| ansys-moment | [Ansys Mechanical Moment](https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/wb_sim/ds_Moment.html) | Moment loading of scoped model regions |
| ansys-symmetry | [Ansys Mechanical Symmetry Region](https://ansyshelp.ansys.com/public/Views/Secured/corp/v251/en/mech_obj/ds_Symmetry_Region_o_r.html) | Symmetry boundary object and constraints |
| gmsh-physical-groups | [Gmsh elementary entities and physical groups](https://gmsh.info/doc/texinfo/gmsh.html#Elementary-entities-vs-physical-groups) | Reusable semantic groups of geometry/mesh entities |
| ansys-inflation | [Ansys Meshing Inflation](https://ansyshelp.ansys.com/public/views/secured/corp/v252/en/wb_msh/ds_Inflation.html) | Graded wall-normal boundary-layer elements |
| openfoam-boundaries | [OpenFOAM boundary conditions](https://doc.openfoam.com/2306/tools/processing/boundary-conditions/) | Distinct inlet, outlet and wall condition families; version 2306 reference |
| openfoam-streamline | [OpenFOAM streamLine](https://doc.openfoam.com/2306/tools/post-processing/function-objects/field/streamLine/) | Vector-field streamline tracing; version 2306 reference |
| fusion-brep-face | [Fusion BRepFace API object](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepFace.htm) | One bounded face and its parent body/shell; topology-object use, not a claim about a default browser node |
| freecad-partdesign-commands | [FreeCAD PartDesign command registration](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/PartDesign/Gui/Workbench.cpp) | Official source registration of Hole, Draft and other PartDesign commands |
| freecad-holding-tags | [FreeCAD CAM holding tags](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/CAM_DressupTag.md) | Holding-tag dressup object beneath an operation; archived official documentation, not a current-version UI claim |
| mastercam-deburr | [Mastercam 2025 feature overview](https://www.mastercam.com/community/blog/10-mastercam-2025-features-you-need-to-know/) | Independent Deburr machining command, separate from modeled CAD chamfers |
| ansys-analysis-tree | [Ansys Mechanical analysis environment object](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/mech_obj/ds_Environment_o_r.html) | Analysis tree children including Analysis Settings |
<!-- references:end -->

## Source-backed expansion

The [v2.1 expansion review](EXPANSION_REVIEW.md) records 38 independent additions, explicit reuse decisions and the difference from the 232-entry baseline. It includes model objects and targeted CAD/CAM/CAE functionality; there is no count target. New entries carry narrower per-feature references rather than merely inheriting a whole-product source list.

## Intended use and limits

These are schematic UI illustrations, not executable machining/robot programs, finite-element results, exact geometry calculations, manufacturing drawings or certified GD&T symbols. Review them at the intended display size, contrast and usage context. The set is selective rather than exhaustive.

All artwork and code use the repository's [MIT license](../LICENSE). See [QA](QA.md) for precisely what was tested and the remaining browser-verification limits.

## 日本語

断面形状・軌跡を掛け合わせた派生を削除し、一般操作と実際の専門機能ごとに整理したアイコン集です。件数を増やすための色替え・回転・形状差し替えは採用しません。保存／名前を付けて保存／すべて保存のように実際の動作が異なるものは別項目とし、警告などの状態シンボルはコマンドと区別しています。

一次資料は機能分類の参考であり、他製品のアイコンは複製していません。各図柄はUI向け模式図です。正確な計算結果、安全なロボットプログラム、規格適合記号の代用にはできません。
