# Design, references and scope

## Semantic entries, not shape multiplication

Each catalog entry represents a distinct application command, engineering tool, persistent model object, or interface status. All entries have a semantic ID, English and Japanese names/tags, and one-sentence usage descriptions in both languages. A shared operation is listed once; a differently shaped part or a different trajectory does not create another icon.

The earlier operation × profile/trajectory generator has been removed, along with its exported variants and contact sheets. It can be recovered from the preceding commit in Git history, but is not part of the current library or build path. No numerical target is used to expand the collection.

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
| moveit-setup-assistant | [MoveIt Setup Assistant](https://moveit.picknik.ai/main/doc/examples/setup_assistant/setup_assistant_tutorial.html) | Planning groups, end effectors, named poses and controllers |
| moveit-urdf-srdf | [MoveIt URDF and SRDF](https://moveit.picknik.ai/main/doc/examples/urdf_srdf/urdf_srdf_tutorial.html) | Robot model, virtual/passive joints, groups, poses and self-collision pairs |
| robodk-general | [RoboDK: General Tips](https://robodk.com/doc/en/General.html) | Reference-frame calibration and mechanism/gripper modeling |
| moveit-planning-scene | [MoveIt Planning Scene](https://moveit.picknik.ai/main/doc/examples/planning_scene/planning_scene_tutorial.html) | Collision checking, allowed collision matrix and kinematic constraints |
| moveit-group-interface | [MoveIt Move Group C++ Interface](https://moveit.picknik.ai/main/doc/examples/move_group_interface/move_group_interface_tutorial.html) | Joint/pose goals, path constraints, planning and attached objects |
| moveit-task-constructor | [Pick and Place with MoveIt Task Constructor](https://moveit.picknik.ai/main/doc/tutorials/pick_and_place_with_moveit_task_constructor/pick_and_place_with_moveit_task_constructor.html) | Grasp pose generation, IK filtering and attach/detach stages |
| moveit-time-parameterization | [MoveIt Time Parameterization](https://moveit.picknik.ai/main/doc/examples/time_parameterization/time_parameterization_tutorial.html) | Trajectory timestamps, velocity/acceleration constraints and jerk-limited smoothing |
| ros2-tf-tree | [ROS 2 tf2 view_frames](https://github.com/ros2/geometry2/blob/rolling/tf2_tools/tf2_tools/view_frames.py) | Frame graph inspection with parent-child transforms and publication timing |
| ros2-robot-state | [ROS Robot State Publisher](https://github.com/ros/robot_state_publisher/blob/rolling/README.md) | URDF kinematic tree and TF transforms from joint states |
| moveit-perception | [MoveIt Perception Pipeline](https://moveit.picknik.ai/main/doc/examples/perception_pipeline/perception_pipeline_tutorial.html) | Occupancy maps updated from point clouds and depth images |
| sdf-model-kinematics | [SDFormat model kinematics](https://sdformat.org/tutorials/specification/spec_model_kinematics/) | Rigid links, model containers and joint degrees of freedom |
| moveit-planar-joint | [MoveIt planar joint model](https://github.com/moveit/moveit2/blob/main/moveit_core/robot_model/src/planar_joint_model.cpp) | Planar joint x/y/theta coordinates |
| moveit-floating-joint | [MoveIt floating joint model](https://moveit.picknik.ai/main/api/html/floating__joint__model_8cpp_source.html) | Free spatial joint with translation and quaternion orientation |
| sdf-joints | [SDFormat 1.12 joint specification](https://sdformat.org/spec/1.12/joint/) | Joint types, axis properties, dynamics, limits and mimic coupling |
| gazebo-sensor-models | [Gazebo Sensors](https://gazebosim.org/libs/sensors/) | Camera, lidar, IMU and force-torque sensor model classes |
| sdf-sensors | [SDFormat 1.12 sensor specification](https://sdformat.org/spec/1.12/sensor/) | Sensor configuration objects, camera projection and physical measurements |
| gazebo-sensors-tutorial | [Gazebo sensor tutorial](https://gazebosim.org/docs/harmonic/sensors/) | Persistent IMU, contact and lidar sensor definitions in robot models |
| ur-jog | [UR PolyScope: Move Tab](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/move_g5/move_tab_en.htm) | Jog, Freedrive, joint/TCP movement |
| abb-robotstudio | [ABB: RobotStudio Suite](https://www.abb.com/global/en/areas/robotics/products/software/robotstudio-suite?TID=828) | Virtual controller, swept volume and cable simulation |
| robodk-programs | [RoboDK: Robot Programs](https://robodk.com/doc/en/Robot-Programs.html) | Program tree; motion, frame, I/O and simulation-event instructions |
| ur-if | [UR PolyScope: If](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/AdvProgNodes/commandtab_ifcondition_en.htm) | Conditional program branch |
| ur-loop | [UR PolyScope: Loop](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/AdvProgNodes/commandtab_loop_en.htm) | Repeated program block |
| ur-assignment | [UR PolyScope: Assignment](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/AdvProgNodes/commandtab_assignment_en.htm) | Assign expressions to variables |
| ur-wait | [UR: Wait for input, time or condition](https://www.universal-robots.com/articles/ur/programming/wait-for-input-time-or-wait-command/) | Timed program delay and condition wait |
| ur-thread | [UR PolyScope: Thread](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/AdvProgNodes/commandtab_thread_en.htm) | Concurrent program branch |
| ur-event | [UR PolyScope: Event](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/AdvProgNodes/commandtab_event_en.htm) | Input-triggered handler |
| ur-script | [UR PolyScope: Script](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/AdvProgNodes/commandtab_script_en.htm) | Inline or file-based script instruction |
| ur-popup | [UR PolyScope: Popup](https://www.universal-robots.com/manuals/EN/HTML/SW5_26/Content/prod-usr-man/software/PolyScope/content/BasicProgNodes/commandtab_popup_en.htm) | Operator-facing program messages |
| ur-pallet | [UR PolyScope: Palletizing](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/Template/new_pallet_en.htm) | Layer and pattern based pallet handling |
| fanuc-roboguide | [FANUC: ROBOGUIDE](https://www.fanucamerica.com/products/software/robot/roboguide) | Cell modeling, CAD-to-path and application simulation |
| ur-conveyor | [UR PolyScope: Conveyor Tracking](https://www.universal-robots.com/manuals/EN/HTML/SW5_26/Content/prod-usr-man/software/PolyScope/content/Template/commandtab_conveyor_tracking_en.htm) | Motion relative to moving conveyor |
| ur-force | [UR PolyScope: Force](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/Template/commandtab_force_en.htm) | Force/torque-controlled motion |
| ur-remote-tcp | [UR PolyScope: Remote TCP and Toolpath](https://www.universal-robots.com/manuals/EN/HTML/SW5_26/Content/prod-usr-man/software/PolyScope/content/robot_control/urcaps_en.htm) | Stationary tool and robot-carried part |
| robodk-point-follow | [RoboDK: Point Follow Project](https://robodk.com/doc/en/Robot-Machining-Point-Follow-Project.html) | Create discrete process paths from points and normals |
| robodk-safety-zones | [RoboDK: Safety Zones](https://robodk.com/doc/en/Addin-Safety-Zones.html) | Modeled workspace boundaries; not certification |
| kuka-sim | [KUKA.Sim: Features Overview](https://www.kuka.com/en-gb/products/robotics-systems/software/simulation-planning-optimization/kuka_sim/kuka_sim_updates) | I/O editor, virtual commissioning, RoboTeam and welding weave |
| abb-station-logic | [ABB RobotStudio Operating Manual](https://search.abb.com/library/Download.aspx?Action=Launch&DocumentID=3HAC032104-001&DocumentPartId=&LanguageCode=en) | 17.1 Station Logic (pp. 375–381, Rev. BC): source and target signal connections |
| abb-io-connection | [ABB RobotStudio API: IOConnection](https://developercenter.robotstudio.com/api/robotstudio/api/ABB.Robotics.RobotStudio.Stations.IOConnection.html) | I/O source and target connection object |
| abb-signals | [ABB: RobotStudio optimization functions](https://new.abb.com/news/detail/96221/10-ways-that-abbs-robotstudior-software-can-help-you-optimize-your-robots-performance) | Record and analyze time-aligned motion/I/O signals |
| robodk-io-monitor | [RoboDK: IO Monitor](https://robodk.com/doc/en/IO-Monitor.html) | Inspect station signals |
| robodk-tips | [RoboDK: Tips and Tricks](https://robodk.com/doc/en/Tips-and-Tricks.html) | Robot trace, program validation, surface target teaching |
| abb-tutorials | [ABB: RobotStudio Tutorials](https://new.abb.com/products/robotics/software-and-digital/robotstudio/tutorials) | Swept volume, cable simulation, AutoPath and other documented workflows |
| ur-single-step | [UR PolyScope: Single Step](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/program_node_sections_g5/single_step_en.htm) | Execute one program node |
| ur-breakpoint | [UR PolyScope: Using Breakpoints](https://www.universal-robots.com/manuals/EN/HTML/SW5_23/Content/prod-usr-man/software/PolyScope/content/program_node_sections_g5/breakpoint_en.htm) | Pause at a selected program location |
| abb-sync-task | [ABB RAPID: WaitSyncTask](https://library.e.abb.com/public/b227fcd260204c4dbeb8a58f8002fe64/Rapid_instructions.pdf) | Program-task synchronization barrier |
| ur-tool-contact | [UR ROS 2 Driver: Tool Contact example](https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_client_library/doc/examples/tool_contact_example.html) | Interrupt motion on detected tool contact |
| gazebo-build-model | [Gazebo building your own robot](https://gazebosim.org/docs/harmonic/building_robot/) | Links, inertial properties, visual and collision geometry, frames and joints |
| gazebo-gui | [Gazebo GUI and entity tree](https://gazebosim.org/docs/harmonic/gui/) | Entity tree links/visuals/collisions/joints, inspector, playback and reset |
| sdf-contact-properties | [SDFormat 1.12 collision surface properties](https://sdformat.org/spec/1.12/collision/) | Friction, restitution and contact stiffness/damping |
| sdf-physics-settings | [SDFormat 1.12 physics settings](https://sdformat.org/spec/1.12/physics/) | Dynamics engine, timestep, solver iteration and accuracy controls |
| ur-node-types | [PolyScope X: NodeType API](https://docs.universal-robots.com/PolyScopeX_SDK_Documentation/build/SDK-v0.14/_static/htmlpages/typescript-api-reference/enums/contribution_api.NodeType.html) | Program tree node names including PAYLOAD and SET_TCP |
| cax-studio-commands | [CAX Studio command registry (afe7a7a)](https://github.com/cslroot/cax-studio/blob/afe7a7a4abf7896b525be66b695367a819516fdc/src/commands.ts) | Implemented feature, recognition and application commands at the reviewed commit |
| cax-studio-kernel-tree | [CAX Studio kernel model-tree mapping (afe7a7a)](https://github.com/cslroot/cax-studio/blob/afe7a7a4abf7896b525be66b695367a819516fdc/src/kernelTree.ts#L102-L105) | Persistent face-offset, defeature and helix nodes |
| cax-core-face-offset | [CAX Core face-offset feature (4b96fde)](https://github.com/cslroot/cax-core/blob/4b96fdeeac2f8aa9fb57a618da1c78aad7627459/crates/cax-modeler/src/session/face_offset_feature.rs#L1-L18) | Existing solid-face displacement; distinct from creating an independent offset surface |
| cax-studio-suppression | [CAX Studio feature suppression control (afe7a7a)](https://github.com/cslroot/cax-studio/blob/afe7a7a4abf7896b525be66b695367a819516fdc/src/ui/ModelTree.tsx#L64-L73) | Toggle suppression while retaining the feature definition |
| cax-studio-suppression-kernel | [CAX Studio suppression evaluation (afe7a7a)](https://github.com/cslroot/cax-studio/blob/afe7a7a4abf7896b525be66b695367a819516fdc/src-tauri/src/state/kernel/part_browser.rs#L495-L542) | Suppression and restoration, including dependent-node checks while retaining names and definitions |
| cax-feature-recognition | [CAX feature recognition (62319d8)](https://github.com/cslroot/cax-feature-recognition/blob/62319d8a27c6950d9271a52ddab278dd18574bb7/README.md#L3-L39) | B-rep and mesh recognition of holes, fillets, chamfers, bosses, ribs, pockets and other features |
| cax-studio-photo-render | [CAX Studio photo renderer (afe7a7a)](https://github.com/cslroot/cax-studio/blob/afe7a7a4abf7896b525be66b695367a819516fdc/src/ui/PhotoRenderDialog.tsx#L25-L29) | CPU path-traced image generation, independent of viewport screenshot capture |
| cax-recognized-thread | [CAX thread recognizer (62319d8)](https://github.com/cslroot/cax-feature-recognition/blob/62319d8a27c6950d9271a52ddab278dd18574bb7/src/recognizers/thread.rs) | B-rep-only ThreadRecognizer produces a Thread feature result; mesh thread recognition is not claimed |
| cax-mesh2brep-methods | [CAX mesh-to-B-rep methods (8dfe1d5)](https://github.com/cslroot/cax-mesh2brep/blob/8dfe1d5036c4a803d4e0e3ec550a28520d40dd54/README.md#L8-L17) | Faceted, analytic, quad, subdivision and hybrid conversion methods |
| pdxadv-result-fields | [pdxadv result-field definitions (40cc394)](https://github.com/cslroot/cax-pdxadv/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/web/viewport.js#L3-L37) | Displacement, residual warpage, shrinkage sensitivity, local thickness, effective linear shrinkage and uncalibrated sink tendency |
| pdxadv-thickness-advisor | [pdxadv bounded coordinate-search advisor (40cc394)](https://github.com/cslroot/cax-pdxadv/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/src/workflow.rs#L401-L556) | Bounded wall-thickness candidates with complete regeneration, remeshing and reanalysis, volume limits and locked parameters |
| pdxadv-local-wall-offset | [pdxadv local wall modifier (40cc394)](https://github.com/cslroot/cax-pdxadv/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/src/design.rs#L1-L85) | Radius-bounded smooth mesh deformation with a fixed back plane; source CAD is retained and no edited B-rep is produced |
| pdxadv-comparison-actions | [pdxadv baseline, comparison and report actions (40cc394)](https://github.com/cslroot/cax-pdxadv/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/web/app.js#L440-L472) | Retain a copied current result in memory, compare paired results and generate reports |
| pdxadv-comparison-display | [pdxadv synchronized result comparison (40cc394)](https://github.com/cslroot/cax-pdxadv/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/web/app.js#L240-L258) | Before/after display uses common field ranges and synchronized view settings |
| pdxadv-analysis-report | [pdxadv analysis-report generation (40cc394)](https://github.com/cslroot/cax-pdxadv/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/src/report.rs#L419-L590) | Assemble analysis reports with figures, selected 3D models and optional before/after data |
| solidcraft-commands | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html) | Parametric sketch, feature, surface, configuration and inspection command taxonomy; checked 2026-10-24 |
| solidworks-sketch | [SOLIDWORKS Sketch toolbar](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_sketch_toolbar.htm) | Sketch creation and constraint GUI families; original CAX geometry |
| solidworks-surfaces | [SOLIDWORKS Surfaces toolbar](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Surfaces_Toolbar.htm) | Surface creation and editing GUI families; original CAX geometry |
| gui-audit-f30c7dc7d5 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_view_toolbar.htm?id=d7123216e4cc48df9f6b6be904699b39) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-4396f7e3ba | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_tools_toolbar.htm?id=2.12.4.1.39) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-7830b955e2 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2021/english/SolidWorks/sldworks/r_Drawing_Toolbar.htm) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-8f5f9d7f22 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_standard.htm?id=2.12.4.1.33) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-32463001c1 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Annotations_Toolbar.htm?id=2.12.4.1.2) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-9b51c95f92 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2023/english/SolidWorks/sldworks/r_table_toolbar.htm?id=3.13.4.1.35) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-8a41850734 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Assembly_Toolbar.htm?id=2.12.4.1.3) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-aad95a4813 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sketch--inspect) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-cf394eb201 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sketch--insert) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-770ce672d7 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-canvas) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-5952aec4b6 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_sketch_toolbar.htm?id=2.12.4.1.29) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-27d4ba3bf3 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sketch--constraints) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-318833252a | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Spline_Tools_Toolbar.htm?id=a4ff97c5f9a44cdfa2f834f95f252946) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-4023a9e23d | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-sketch) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-1bed7f8e51 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_blocks_toolbar.htm?id=2.12.4.1.4) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-3762e45220 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sketch--create) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-f00a42accf | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sketch--modify) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-43d4d0f047 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-render) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-64d1c36155 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#surface--create) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-f42456e152 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Surfaces_Toolbar.htm?id=228c84f71d5c424ab88a08a5e57b3e33) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-efdc5a5641 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#surface--modify) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-117fa3c165 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/t_Changing_from_One_Display_State_to_Another.htm) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-8ff0ee5324 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/HIDD_NEW_ADD_CONFIG.htm?id=9.2.0.2) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-875626de06 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-view) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-08eeb2032b | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-appearance) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-ecd16ac847 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#solid--modify) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-a3a82707e9 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-edit) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-e02b0eaa69 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-config) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-a5fe59e311 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-diagnostics) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-950e136ff6 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-parameters) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-676d40e2c6 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-timeline) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-0b7fca4246 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-library) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-1360b317c3 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-material) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-406303650d | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-expr) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-cba07c324a | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_select_flyout_menu_assembly.htm?id=7.1.4.0) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-c14a946b6f | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-browser) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-c2a5f59b1b | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Features_Toolbar.htm?id=2.12.4.1.11) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-e00cc276d0 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-component) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-952753343a | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#solid--assemble) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-682bbc8192 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_mate_icons_featuremanager_design_tree.htm?id=7.7.4) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-5b19650212 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#solid--create) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-2bf9f54b30 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#solid--position) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-aa090f2a75 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/English/SolidWorks/sldworks/r_weldments_toolbar.htm?id=a668b8ee4e4b429aa9a10dda92a9a6f4) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-48d928339e | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#solid--construct) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-3abc9063cf | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-parts) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-c977662189 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#solid--insert) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-2f3c6a71c2 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-frame) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-319974c257 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/japanese/SolidWorks/sldworks/r_Mold_Tools_Toolbar_mold.htm) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-73a2f59c6c | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#plastic--create) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-1b7d149ee8 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#other-motion) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-710dd04d55 | [SOLIDWORKS official GUI documentation](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Sheet_Metal_Toolbar.htm?id=2.12.4.1.28) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-749742060e | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sheet-metal--create) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-audit-f87ed3acf1 | [SolidCraft command reference](https://docs.solidcraft.io/reference/commands.html#sheet-metal--modify) | Reviewed command taxonomy; original CAX artwork. The bounded coverage audit records source-year and retrieval limits. |
| gui-binding-95ed3a6ad9 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/English/SolidWorks/sldworks/c_replace_sketch_entities.htm?id=60e56696b89a4838bd298f13b38a545a) | Command meaning only; original artwork, no vendor assets |
| gui-binding-6935560205 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/SolidWorks/sldworks/HIDD_DVE_REPLACE_COMPS.htm?id=7.11.8) | Command meaning only; original artwork, no vendor assets |
| gui-binding-ccf6084f52 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/japanese/SolidWorks/sldworks/HIDD_DVE_REPLACE_COMPS.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-c706fb842d | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/SolidWorks/sldworks/hidd_dve_feat_move_face.htm?id=23.6.36.2.14) | Command meaning only; original artwork, no vendor assets |
| gui-binding-8b14449f5f | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/SolidWorks/sldworks/c_Freeforms_Folder.htm?id=ed52e5d0bb4949d881b206d79ae6e160) | Command meaning only; original artwork, no vendor assets |
| gui-binding-159490dd9a | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2022/english/SolidWorks/sldworks/HIDD_DVE_FEAT_PPGORDON.htm?id=2b6c7bfd8ce44176b235661493bbb122) | Command meaning only; original artwork, no vendor assets |
| gui-binding-b3e2d17dd0 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/solidworks/sldworks/c_Deforms_Top_Folder.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-f0c46894c1 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2012/English/SolidWorks/sldworks/HIDD_DVE_DEFORM.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-ecd16ac847 | [Official command semantics for conditional GUI bindings](https://docs.solidcraft.io/reference/commands.html#solid--modify) | Command meaning only; original artwork, no vendor assets |
| gui-binding-5c2115eb24 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/SolidWorks/sldworks/HIDD_DVE_PLANAR_SURFACE.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-4d9736f9fd | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/SolidWorks/sldworks/HIDD_DVE_SURF_WRAPPING_SKETCH.htm?id=23.6.40) | Command meaning only; original artwork, no vendor assets |
| gui-binding-e3a26b2837 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWrapSketchType_e.html) | Command meaning only; original artwork, no vendor assets |
| gui-binding-aa1eeeab9d | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/t_creating_groove_beads.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-b3db87199e | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/WhatsNew/c_wn2025_weldments_groove_beads.htm?id=9.7) | Command meaning only; original artwork, no vendor assets |
| gui-binding-f7a6b6fdd8 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2024/english/SolidWorks/sldworks/c_Weld_Beads.htm?id=35.0.15) | Command meaning only; original artwork, no vendor assets |
| gui-binding-f30c7dc7d5 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_view_toolbar.htm?id=d7123216e4cc48df9f6b6be904699b39) | Command meaning only; original artwork, no vendor assets |
| gui-binding-172ac8ab94 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/simtutorialonline/t_viewing_optimization_results.htm?id=0.2.6.8) | Command meaning only; original artwork, no vendor assets |
| gui-binding-9baa1e8232 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2022/english/SolidWorks/sldworks/t_displaying_sw_sim_results_inga.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-4396f7e3ba | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_tools_toolbar.htm?id=2.12.4.1.39) | Command meaning only; original artwork, no vendor assets |
| gui-binding-53d9c98fae | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_Design_Studies_SOLIDWORKS.htm?id=e0490acf4f374e5a800fca910b819154) | Command meaning only; original artwork, no vendor assets |
| gui-binding-8e7060fa2f | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/cworks/c_Design_Study.htm?id=26.13) | Command meaning only; original artwork, no vendor assets |
| gui-binding-62e45fcfa1 | [Official command semantics for conditional GUI bindings](https://docs.solidcraft.io/reference/commands.html#solid--inspect) | Command meaning only; original artwork, no vendor assets |
| gui-binding-41d1a1b3a5 | [Official command semantics for conditional GUI bindings](https://docs.solidcraft.io/reference/commands.html) | Command meaning only; original artwork, no vendor assets |
| gui-binding-3188d0fc7e | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/HIDD_MEASURE.htm?id=3.10) | Command meaning only; original artwork, no vendor assets |
| gui-binding-9404158c15 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/api/swcommands/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.html?id=cec41382bfc941eb83f24f6c8425852b) | Command meaning only; original artwork, no vendor assets |
| gui-binding-db8c551af6 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2024/english/SolidWorks/sldworks/t_using_make_sw_desktop.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-dd7dc4c73a | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/English/SolidWorks/DFMXpress/c_DFMXpress_overview.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-6f3e2bf88e | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_assy_facility_layout.htm?id=7.13.1) | Command meaning only; original artwork, no vendor assets |
| gui-binding-16018f6014 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/English/SolidWorks/sldworks/r_asset_publisher_propertymanager.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-3ee9115b27 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_publish_3dcloudbymePM.htm?id=5.17.0) | Command meaning only; original artwork, no vendor assets |
| gui-binding-61ac1ec318 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_share_files.htm?id=5.15) | Command meaning only; original artwork, no vendor assets |
| gui-binding-32463001c1 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Annotations_Toolbar.htm?id=2.12.4.1.2) | Command meaning only; original artwork, no vendor assets |
| gui-binding-0f21262562 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/english/SolidWorks/sldworks/c_notes.htm?id=d1b8b71f6dfd4415a1d5301ae125061f) | Command meaning only; original artwork, no vendor assets |
| gui-binding-bd40dd11ab | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_annotation_leaders.htm?id=13.7.11.0) | Command meaning only; original artwork, no vendor assets |
| gui-binding-952753343a | [Official command semantics for conditional GUI bindings](https://docs.solidcraft.io/reference/commands.html#solid--assemble) | Command meaning only; original artwork, no vendor assets |
| gui-binding-30f1eca701 | [Official command semantics for conditional GUI bindings](https://docs.solidcraft.io/guide/assemblies.html) | Command meaning only; original artwork, no vendor assets |
| gui-binding-12b8f73d64 | [Official command semantics for conditional GUI bindings](https://docs.solidcraft.io/reference/commands.html#other-joint) | Command meaning only; original artwork, no vendor assets |
| gui-binding-8a41850734 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Assembly_Toolbar.htm?id=2.12.4.1.3) | Command meaning only; original artwork, no vendor assets |
| gui-binding-90542fecaa | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/English/SolidWorks/sldworks/HIDD_NEW_ADD_MATE.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-cfb0ccd92c | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_mate_pm_advanced.htm?id=7.7.3.1) | Command meaning only; original artwork, no vendor assets |
| gui-binding-e52e39f2ba | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2024/english/SolidWorks/sldworks/r_mate_pm_mechanical.htm?id=9f5542b7de6347a99d867200d6c17f68) | Command meaning only; original artwork, no vendor assets |
| gui-binding-7b9d6a9d5a | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_machine_desing_tools_overview.htm?id=3.2) | Command meaning only; original artwork, no vendor assets |
| gui-binding-f162e6bff2 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2025/English/SolidWorks/sldworks/t_Universal_Joint_Mate_SWassy.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-682bbc8192 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_mate_icons_featuremanager_design_tree.htm?id=7.7.4) | Command meaning only; original artwork, no vendor assets |
| gui-binding-8effa5b625 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2024/english/SolidWorks/sldworks/t_Limit_Mates_SWassy.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-710dd04d55 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Sheet_Metal_Toolbar.htm?id=2.12.4.1.28) | Command meaning only; original artwork, no vendor assets |
| gui-binding-c181701d3d | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/Sldworks/t_Creating_Forming_Tools.htm) | Command meaning only; original artwork, no vendor assets |
| gui-binding-cd1e1268cc | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_Weld_Beads.htm?id=35.0.15) | Command meaning only; original artwork, no vendor assets |
| gui-binding-083a22261c | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2014/english/SolidWorks/sldworks/t_Adding_Weld_Beads_to_Sheet_Metal_Corners.htm?id=21.1.20) | Command meaning only; original artwork, no vendor assets |
| gui-binding-16771073df | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/HIDD_SHEET_METAL_WELD_BEAD.htm?id=25.1.24) | Command meaning only; original artwork, no vendor assets |
| gui-binding-82adec05d8 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/SolidWorks/sldworks/t_Adding_Weld_Beads_to_Sheet_Metal_Corners.htm?id=25.1.23) | Command meaning only; original artwork, no vendor assets |
| gui-binding-aa090f2a75 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/English/SolidWorks/sldworks/r_weldments_toolbar.htm?id=a668b8ee4e4b429aa9a10dda92a9a6f4) | Command meaning only; original artwork, no vendor assets |
| gui-binding-f767c22588 | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html?id=2.10.1.729) | Command meaning only; original artwork, no vendor assets |
| gui-binding-5886e6220c | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2024/english/SolidWorks/sldworks/c_Weldments_Fillet_Weld_Beads.htm?id=35.0.15.7) | Command meaning only; original artwork, no vendor assets |
| gui-binding-0aa6ca630b | [Official command semantics for conditional GUI bindings](https://help.solidworks.com/2026/english/api/sldworksapi/Insert_Weldment_Features_Example_CSharp.htm) | Command meaning only; original artwork, no vendor assets |
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

## Robotics extension

The [v2.3 robotics review](ROBOTICS_EXPANSION.md) records independent control-flow, planning, perception, process and kinematic functions. It also records source-backed reuse of physical components, joints, geometry, frames and general application commands without duplicate SVGs.
