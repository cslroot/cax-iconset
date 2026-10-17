# Design, references and scope

## Semantic entries, not shape multiplication

Each catalog entry represents a distinct application command, engineering tool, persistent model object, or interface status. All entries have a semantic ID, English and Japanese names/tags, and one-sentence usage descriptions in both languages. A shared operation is listed once; a differently shaped part or a different trajectory does not create another icon.

The earlier operation × profile/trajectory generator has been removed, along with its exported variants and contact sheets. It can be recovered from the preceding commit in Git history, but is not part of the current library or build path. No numerical target is used to expand the collection.

<!-- coverage:start -->
| Primary category | Symbols |
| --- | ---: |
| Common | 72 |
| CAD | 123 |
| CAM | 44 |
| CAE | 52 |
| CMM | 34 |
| OLP | 32 |
| **Total** | **357** |

Primary roles: 341 commands, 5 selectable tools, 8 objects and 3 status symbols. Every SVG is counted once.

141 entries support model-tree use, including reused command/tool symbols; these are not additional SVGs.
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
| blender-bridge | [Blender Bridge Edge Loops](https://docs.blender.org/manual/en/5.2/modeling/meshes/editing/edge/bridge_edge_loops.html) | Official manual indexed as 5.2; use for operation semantics only. |
| blender-mesh-toolbar | [Blender mesh edit toolbar](https://docs.blender.org/manual/en/latest/modeling/meshes/tools/toolbar.html) | Official Blender manual; command semantics only, not a current-version assertion. |
| blender-mesh-cleanup | [Blender mesh cleanup](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/cleanup.html) | Official Blender manual; polygon cleanup and repair commands. |
| salome-merge-nodes | [SALOME merging nodes](https://docs.salome-platform.org/latest/gui/SMESH/merging_nodes.html) | Merge coincident nodes by tolerance |
| blender-dissolve | [Blender Deleting and Dissolving](https://docs.blender.org/manual/en/5.0/modeling/meshes/editing/mesh/delete.html) | Blender 5.0 manual; dissolve operation reference. |
| blender-remesh | [Blender Remesh modifier](https://docs.blender.org/manual/id/4.5/modeling/modifiers/generate/remesh.html) | Blender 4.5 manual; remeshing modes are treated as one operation. |
| blender-smooth-vertices | [Blender Smooth Vertices](https://docs.blender.org/manual/en/4.5/modeling/meshes/editing/vertex/smooth_vertices.html) | Blender 4.5 LTS manual; vertex-position smoothing. |
| salome-smoothing | [SALOME smoothing](https://docs.salome-platform.org/latest/gui/SMESH/smoothing.html) | Improve mesh shape by repositioning nodes |
| blender-shrinkwrap | [Blender Shrinkwrap modifier](https://docs.blender.org/manual/en/2.81/modeling/modifiers/deform/shrinkwrap.html) | Blender 2.81 historical manual; stable operation semantics, also corroborated by official ShrinkwrapModifier API. |
| blender-uv-unwrap | [Blender UV operators](https://docs.blender.org/manual/en/5.4/modeling/meshes/editing/uv.html) | Official manual indexed as 5.4; reference for UV operation semantics, not a current-version assertion. |
| rhino-blendsrf | [Rhino blendsrf](https://docs.mcneel.com/rhino/8/help/en-us/commands/blendsrf.htm) | Rhino 8 official command help; operation semantics. |
| rhino-matchsrf | [Rhino matchsrf](https://docs.mcneel.com/rhino/8mac/help/en-us/commands/matchsrf.htm) | Rhino 8 official command help; operation semantics. |
| rhino-networksrf | [Rhino networksrf](https://docs.mcneel.com/rhino/8mac/help/en-us/commands/networksrf.htm) | Rhino 8 official command help; operation semantics. |
| rhino-rebuild | [Rhino rebuild](https://docs.mcneel.com/rhino/8/help/en-us/commands/rebuild.htm) | Rhino 8 official command help; operation semantics. |
| rhino-extractisocurve | [Rhino extractisocurve](https://docs.mcneel.com/rhino/8mac/help/en-us/commands/extractisocurve.htm) | Rhino 8 official command help; operation semantics. |
| rhino-cageedit | [Rhino cageedit](https://docs.mcneel.com/rhino/8mac/help/en-us/commands/cageedit.htm) | Rhino 8 official command help; operation semantics. |
| rhino-flowalongsrf | [Rhino flowalongsrf](https://docs.mcneel.com/rhino/8/help/en-us/commands/flowalongsrf.htm) | Rhino 8 official command help; operation semantics. |
| rhino-zebra | [Rhino zebra](https://docs.mcneel.com/rhino/8/help/en-us/commands/zebra.htm) | Rhino 8 official command help; operation semantics. |
| rhino-draftangleanalysis | [Rhino draftangleanalysis](https://docs.mcneel.com/rhino/8/help/en-us/commands/draftangleanalysis.htm) | Rhino 8 official command help; operation semantics. |
| cloudcompare-subsample | [CloudCompare Subsample point cloud](https://cloudcompare.org/doc/wiki/index.php/Edit%5CSubsample) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| cloudcompare-outlier-removal | [CloudCompare Remove point-cloud outliers](https://cloudcompare.org/doc/wiki/index.php/SOR_filter) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| cloudcompare-normals | [CloudCompare Compute point-cloud normals](https://cloudcompare.org/doc/wiki/index.php/Normals%5CCompute) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| cloudcompare-components | [CloudCompare Extract connected components](https://cloudcompare.org/doc/wiki/index.php/Label_Connected_Components) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| cloudcompare-primitive-detection | [CloudCompare Detect point-cloud primitives](https://cloudcompare.org/doc/wiki/index.php/PluginRansacSD) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| cloudcompare-reconstruct | [CloudCompare Reconstruct surface from points](https://cloudcompare.org/doc/wiki/index.php/Poisson_Surface_Reconstruction_%28plugin%29) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| cloudcompare-rasterize | [CloudCompare Rasterize point cloud](https://cloudcompare.org/doc/wiki/index.php/Rasterize) | Official CloudCompare wiki; standalone or named plugin command semantics. Historical screenshots/version notes are not current-version claims. |
| solidworks-hem | [SOLIDWORKS Hems](https://help.solidworks.com/2024/english/SolidWorks/sldworks/c_Hems.htm?id=474d0dc2a50946878872d45b767b9d21) | SOLIDWORKS 2024 official help; dedicated Hem command. |
| solidworks-jog | [SOLIDWORKS Jogs](https://help.solidworks.com/2024/English/SolidWorks/sldworks/c_Jogs.htm?id=fa64ae6f294049598ffaec44d7f221e4) | SOLIDWORKS 2024 official help; dedicated Jog command. |
| solidworks-forming-tools | [SOLIDWORKS Using Forming Tools with Sheet Metal](https://help.solidworks.com/2024/English/solidworks/sldworks/c_Forming_Tools.htm) | SOLIDWORKS 2024 official help; applying library forming tools to a sheet-metal target. |
| solidworks-corner-relief | [SOLIDWORKS Corner Relief PropertyManager](https://help.solidworks.com/2023/English/SolidWorks/sldworks/HIDD_SHEET_METAL_CORNER_RELIEF.htm) | SOLIDWORKS 2023 official help; reliefs at two- or three-bend corners, one semantic entry. |
| solidworks-tab-slot | [SOLIDWORKS Creating a Tab and Slot](https://help.solidworks.com/2026/english/SolidWorks/sldworks/t_creating_a_tab_and_slot.htm?id=25.1.7.0) | SOLIDWORKS 2026 official help; tab/slot pairs on sheet-metal or eligible nonsheet parts. |
| solidworks-convert-sheetmetal | [SOLIDWORKS Converting an Imported Part to a Sheet Metal Part](https://help.solidworks.com/2026/english/solidworks/sldworks/t_converting_imported_part_sheet_metal.htm) | SOLIDWORKS 2026 official help; constant-thickness imported sheet-metal-type parts. |
| solidworks-weldments | [SOLIDWORKS Weldments](https://help.solidworks.com/2026/English/SolidWorks/Sldworks/c_Weldments_Overview.htm) | SOLIDWORKS 2026 official help; grouped sketch segments and library structural profiles. |
| solidworks-weldment-trim | [SOLIDWORKS Weldments Trim and Extend](https://help.solidworks.com/2020/english/SolidWorks/Sldworks/c_Weldments_Trim_and_Extend.htm) | SOLIDWORKS 2020 official help; member end treatments and cut-length accuracy. |
| solidworks-end-cap | [SOLIDWORKS Adding End Caps](https://help.solidworks.com/2026/english/SolidWorks/sldworks/t_adding_an_end_cap.htm?id=35.0.14.0) | SOLIDWORKS 2026 official help; End Cap command and thickness/offset controls. |
| solidworks-gusset | [SOLIDWORKS Weldments Gussets](https://help.solidworks.com/2026/English/SolidWorks/sldworks/c_Weldments_Gussets.htm?id=58a3c7988bad44a4843f5bbe55cec5a4) | SOLIDWORKS 2026 official help; dedicated weldment Gusset command. |
| solidworks-weld-bead | [SOLIDWORKS Weld Beads](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_Weld_Beads.htm?id=35.0.15) | SOLIDWORKS 2026 official help; lightweight graphical weld-bead feature, not newly created solid geometry. |
| solidworks-parting-line | [SOLIDWORKS Parting Lines](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_parting_lines.htm?id=d1404aa33b544f98b65f89fcd8c80846) | SOLIDWORKS 2026 official help; core/cavity boundary and surface classification. |
| solidworks-tooling-split | [SOLIDWORKS Tooling Split PropertyManager](https://help.solidworks.com/2025/english/SolidWorks/sldworks/HIDD_MOLD_CAVITY_CORE_SOLIDS.htm) | SOLIDWORKS 2025 official help; creation of core/cavity blocks from three surface-body roles. |
| solidworks-auto-route | [SOLIDWORKS Creating Flexible Ribbon Cable Routes](https://help.solidworks.com/2026/english/SolidWorks/sldpiping/t_creating_flexible_ribbon_cable_routes.htm) | SOLIDWORKS 2026 official help; connector-to-connector Auto Route example for flexible ribbon cable. |
| inkscape-node-editing | [Inkscape Advanced tutorial: editing paths](https://inkscape.org/es/doc/tutorials/advanced/tutorial-advanced.html?switchlang=es) | Official localized Inkscape tutorial with path-editing description; function reference, no current-version assertion. |
| inkscape-stroke-to-path | [Inkscape 1.0 release notes: Stroke to Path](https://wiki.inkscape.org/wiki/Release_notes/1.0) | Official Inkscape 1.0 release notes; historical reference for stroke-outline conversion. |
| inkscape-trace-bitmap | [Inkscape Tracing bitmaps tutorial](https://inkscape.org/en/doc/tutorials/tracing/tutorial-tracing.ru.html/) | Official Inkscape localized tutorial; bitmap-to-vector tracing command, not claims about fidelity. |
| qcad-hatch | [QCAD Hatch from Selection](https://qcad.org/doc/qcad/latest/reference/en/scripts/Draw/Hatch/HatchFromSelection/doc/HatchFromSelection_en.html) | Official QCAD user reference; hatch creation from closed boundaries. |
| qcad-create-block | [QCAD Create Block from Selection](https://qcad.org/en/manual/scripts/block/createblock/doc/createblock/) | Official QCAD user manual; block definitions and reusable references. |
| qcad-explode | [QCAD Explode](https://www.qcad.org/doc/qcad/latest/reference/en/scripts/Modify/Explode/doc/Explode_en.html) | Official QCAD user reference; block references and compound drawing entities. |
| inkscape-actions | [Inkscape action reference](https://wiki.inkscape.org/wiki/Action) | Official action table explicitly covering Inkscape 1.2; align and distribute command semantics. |
| mastercam-wire | [Mastercam Wire](https://www.mastercam.com/solutions/products/wire/) | Wire EDM toolpath programming |
| linuxcnc-tool-compensation | [LinuxCNC Tool Compensation](https://linuxcnc.org/docs/html/gcode/tool-compensation.html) | Tool radius compensation and tool-length touch-off |
| powermill-stock-model | [PowerMill stock model](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-create-a-stock-model-in-PowerMILL.html) | Update in-process material using machining operations |
| solidcam-hole-recognition | [SolidCAM automatic feature recognition](https://solidcam.com/de/cam-loesungen/automatische-feature-erkennung/) | Recognize holes and derive machining operations |
| mastercam-lathe | [Mastercam Lathe](https://www.mastercam.com/solutions/products/lathe-programming-software/) | Grooving and single-point thread turning |
| powermill-finishing | [PowerMill finishing strategies](https://help.autodesk.com/cloudhelp/2022/ENU/PWRM-ReferenceHelp/files/GUID-B5C85060-9C1C-4EAE-960F-41F89B1E7C1D.htm) | Constant-Z and corner-pencil finishing |
| mastercam-nesting | [Mastercam CNC Router nesting](https://www.mastercam.com/solutions/products/cnc-router-software/) | Geometry and toolpath nesting on sheet stock |
| mastercam-port | [Mastercam Port Expert](https://www.mastercam.com/solutions/add-ons/port-export/) | Multiaxis internal port machining |
| fusion-trim-toolpath | [Fusion trim a toolpath](https://help.autodesk.com/view/fusion360/ENU/?contextId=MFG-TRIM-TOOLPATH) | Limit an existing toolpath by polygon, plane or boundary |
| powermill-reorder | [PowerMill reorder toolpath segments](https://help.autodesk.com/cloudhelp/2022/ENU/PWRM-ReferenceHelp/files/GUID-12327ECE-5C71-4175-B13C-F4E46261C4CB.htm) | Change segment sequence and directions with rebuilt links |
| salome-sew | [SALOME sewing meshes](https://docs.salome-platform.org/latest/gui/SMESH/sewing_meshes.html) | Connect mesh borders or mesh sides |
| salome-orient-faces | [SALOME orient faces](https://docs.salome-platform.org/latest/gui/SMESH/reorient_faces.html) | Make mesh face orientations consistent |
| salome-quadratic | [SALOME convert to/from quadratic mesh](https://docs.salome-platform.org/latest/gui/SMESH/convert_to_from_quadratic_mesh.html) | Convert finite-element interpolation order |
| salome-boundary-elements | [SALOME generate boundary elements](https://docs.salome-platform.org/latest/gui/SMESH/make_2dmesh_from_3d.html) | Create lower-dimensional boundary elements from higher-dimensional mesh |
| altair-material-orientation | [HyperMesh Material Orientation](https://help.altair.com/2024/hwdesktop/hwx/topics/pre_processing/aerospace/model_orientation_r.htm) | Assign anisotropic material directions |
| altair-composite-model | [HyperMesh Composite Analysis](https://help.altair.com/hwdesktop/hwx/topics/tutorials/hwx/composite_analysis_t.htm) | Define laminate plies, stacking and composite properties |
| altair-rigid-link | [HyperMesh bracket and cradle preprocessing](https://2022.help.altair.com/2022/hwdesktop/hm/topics/tutorials/hm/hm_4340_pre_processing_for_bracket_and_cradle_analysis_c.htm) | Create rigid spider links and kinematic couplings |
| altair-spring-element | [HyperMesh Springs Panel](https://2022.help.altair.com/2022/hwdesktop/hm/topics/panels/help057.htm) | Create spring elements between nodes |
| ansys-bolt-pretension | [Ansys Mechanical Bolt Pretension](https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/wb_sim/ds_Pretension.html) | Define bolt preload boundary conditions |
| ansys-load-mapping | [Ansys Mechanical Importing Loads](https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/wb_sim/ds_ext_file_import_loads.html) | Map external load fields onto the analysis model |
| ansys-harmonic-response | [Ansys Harmonic Response](https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/wb2_help/wb2h_harmrespAN.html) | Create steady-state frequency-response analysis |
| ansys-system-coupling | [Ansys System Coupling Region](https://ansyshelp.ansys.com/public/Views/Secured/corp/v242/en/wb_sim/ds_system_coupling_region.html) | Define the interface used to exchange multiphysics data |
| paraview-data-filters | [ParaView Filtering Data](https://docs.paraview.org/en/latest/UsersGuide/filteringData.html) | Extract isosurfaces, generate vector glyphs and compute derived data |
| paraview-integrate | [ParaView IntegrateVariables](https://www.paraview.org/paraview-docs/v5.13.2/python/paraview.simple.IntegrateVariables.html) | Spatial integration of point and cell fields |
| paraview-temporal-statistics | [ParaView TemporalStatistics](https://www.paraview.org/paraview-docs/v5.13.2/python/paraview.simple.TemporalStatistics.html) | Compute timestep statistics of result fields |
| pcdmis-temperature | [PC-DMIS Temperature Compensation](https://docs.hexagonmi.com/pcdmis/2019.1/en/helpcenter/mergedProjects/core/06_pref_topics/Temperature_Compensation.htm) | Compensate measured part dimensions using temperature |
| pcdmis-optimize-path | [PC-DMIS Optimizing the Path](https://docs.hexagonmi.com/pcdmis/2019.1/en/helpcenter/mergedProjects/core/inspection_plans/Optimizing_the_Path.htm) | Optimize tactile inspection sequence and probe-tip angles |
| robodk-curve-follow | [RoboDK Curve Follow Project](https://robodk.com/doc/en/Robot-Machining-Curve-Follow-Project.html) | Generate robot paths from geometric curves and surface normals |
| robodk-collision-planner | [RoboDK Collision-Free Motion Planner](https://robodk.com/doc/en/Collision-Avoidance-Collision-Free-Motion-Planner.html) | Generate collision-free paths through robot configuration space |
| robodk-synchronize-axes | [RoboDK Synchronize Additional Axes](https://robodk.com/doc/en/General-Synchronize-Additional-Axes.html) | Synchronize external mechanisms with robot motion |
| robodk-robot-calibration | [RoboDK Robot Calibration](https://robodk.com/doc/en/Robot-Calibration-LaserTracker.html) | Estimate robot kinematic error parameters from measurements |
| robodk-configurations | [RoboDK Robot Configurations](https://robodk.com/doc/en/Interface-Robot-Configurations.html) | Choose a robot kinematic solution for a target pose |
| powermill-raster-finishing | [PowerMill Raster Finishing](https://help.autodesk.com/cloudhelp/2022/ENU/PWRM-ReferenceHelp/files/GUID-72851E2B-E8E1-46D9-98F7-B9EB47CE2E4B.htm) | Parallel surface-finishing passes; historical PowerMill 2022 terminology |
| powermill-swarf-finishing | [PowerMill Swarf Finishing](https://help.autodesk.com/cloudhelp/2022/ENU/PWRM-ReferenceHelp/files/GUID-B5C85060-9C1C-4EAE-960F-41F89B1E7C1D.htm) | Cutter-flank surface finishing; historical PowerMill 2022 terminology |
| paraview-stream-tracer | [ParaView filtering data](https://docs.paraview.org/en/latest/UsersGuide/filteringData.html) | Stream Tracer integrates a vector field into streamlines |
| salome-quality-controls | [SALOME mesh quality controls](https://docs.salome-platform.org/latest/gui/SMESH/index.html) | Mesh quality checks; different quality metrics reuse the quality-check symbol |
| cloudcompare-icp | [CloudCompare ICP fine registration](https://cloudcompare.org/doc/wiki/index.php/ICP) | Iterative closest-point fine registration of measured geometry |
| solidworks-shutoff | [SOLIDWORKS Shut-off Surfaces](https://help.solidworks.com/2025/english/solidworks/sldworks/c_shut_off_surfaces.htm) | SOLIDWORKS 2025 official help; through-hole shutoffs populate core and cavity surface bodies. |
<!-- references:end -->

## Source-backed expansion

The [v2.1 expansion review](EXPANSION_REVIEW.md) records 38 independent additions, explicit reuse decisions and the difference from the 232-entry baseline. It includes model objects and targeted CAD/CAM/CAE functionality; there is no count target. New entries carry narrower per-feature references rather than merely inheriting a whole-product source list.

## Intended use and limits

These are schematic UI illustrations, not executable machining/robot programs, finite-element results, exact geometry calculations, manufacturing drawings or certified GD&T symbols. Review them at the intended display size, contrast and usage context. The set is selective rather than exhaustive.

All artwork and code use the repository's [MIT license](../LICENSE). See [QA](QA.md) for precisely what was tested and the remaining browser-verification limits.

## 日本語

断面形状・軌跡を掛け合わせた派生を削除し、一般操作と実際の専門機能ごとに整理したアイコン集です。件数を増やすための色替え・回転・形状差し替えは採用しません。保存／名前を付けて保存／すべて保存のように実際の動作が異なるものは別項目とし、警告などの状態シンボルはコマンドと区別しています。

一次資料は機能分類の参考であり、他製品のアイコンは複製していません。各図柄はUI向け模式図です。正確な計算結果、安全なロボットプログラム、規格適合記号の代用にはできません。

## Additional application families

The [v2.2 application-family review](APPLICATION_EXPANSION.md) lists every new command, its purpose and primary evidence. It also records rejected duplicate candidates, alternate application vocabulary, shared CAD/CAE and CAD/CMM uses, and the distinction between command and persistent-node contexts.
