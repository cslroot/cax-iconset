"""Primary references for feature taxonomy, never for tracing vendor artwork."""
SOURCE_IDS = {'Common':['solidworks-standard','inventor-files','fusion-selection'], 'CAD':['freecad','solidworks','inventor-assembly','fusion-drawing'], 'CAM':['fusion','linuxcnc','fusion-milling'], 'CAE':['ansys','openfoam','gmsh','fusion-simulation'], 'CMM':['pcdmis','calypso','pcdmis-quickstart'], 'OLP':['robodk','moveit']}
REFERENCES = {
 'fusion-drawing': {'title':'Fusion Drawing toolbar', 'url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-Drawing/files/DWG-REF-DRAWING-TAB.htm', 'scope':'Drawing creation, projected/detail views, dimensions and annotations'},
 'solidworks-standard': {'title':'SOLIDWORKS standard toolbar', 'url':'https://help.solidworks.com/2017/english/SolidWorks/sldworks/r_Standard.htm?id=2.11.3.1.31', 'scope':'File and edit commands; historical taxonomy reference'},
 'inventor-files': {'title':'Inventor save and export files', 'url':'https://help.autodesk.com/cloudhelp/2025/ENU/Inventor-Help/files/GUID-08D6DD13-3066-4210-9F19-5F7E8DB8AD5D.htm', 'scope':'Save, save as, and export operations'},
 'fusion-selection': {'title':'Fusion selection tools', 'url':'https://help.autodesk.com/view/fusion360/ENU/?guid=SLD-SELECTION', 'scope':'Window, crossing and freeform selection semantics'},
 'inventor-assembly': {'title':'Inventor assembly workflow', 'url':'https://help.autodesk.com/cloudhelp/2024/ENU/Inventor-Help/files/GUID-AB69CA08-CD95-410C-9E72-49CCBB858915.htm', 'scope':'Assembly placement, constraints, and analysis'},
 'fusion-milling': {'title':'Fusion milling workflow', 'url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/MFG-OVERVIEW-MILLING-WORKFLOW.htm', 'scope':'Setup, tooling, toolpath generation, simulation and NC output'},
 'fusion-simulation': {'title':'Fusion simulation setup', 'url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-Simulate/files/SIM-SETUP-TAB.htm', 'scope':'Study, materials, constraints, loads, contacts, mesh, precheck and solve'},
 'pcdmis-quickstart': {'title':'PC-DMIS Quick Start interface', 'url':'https://docs.hexagonmi.com/pcdmis/2023.1/en/helpcenter/mergedprojects/core/10_view_topics/Quick_Start_Interface.htm', 'scope':'Probe setup, calibration, alignment, features and dimensions'},
 'freecad': {'title':'FreeCAD features', 'url':'https://www.freecad.org/features', 'scope':'Parametric modeling, sketches, parts and workbenches'},
 'solidworks': {'title':'SOLIDWORKS Features Overview', 'url':'https://help.solidworks.com/2012/english/SolidWorks/sldworks/Features_Overview.htm', 'scope':'Feature-based solids, cuts, fillets, chamfers and patterns; historical taxonomy reference'},
 'fusion': {'title':'Autodesk Fusion features', 'url':'https://www.autodesk.com/products/fusion-360/features', 'scope':'CAD/CAM, manufacturing, milling and toolpath workflows'},
 'linuxcnc': {'title':'LinuxCNC G-code reference', 'url':'https://linuxcnc.org/docs/html/gcode.html', 'scope':'Motion, coordinates, interpolation and machining cycles'},
 'ansys': {'title':'Ansys Mechanical datasheet', 'url':'https://www.ansys.com/content/dam/product/structures/mechanical-datasheet.pdf', 'scope':'Structural, thermal, modal and contact analysis'},
 'openfoam': {'title':'OpenFOAM user guide', 'url':'https://www.openfoam.com/documentation/user-guide', 'scope':'Mesh, boundary conditions, flow and field concepts'},
 'gmsh': {'title':'Gmsh reference manual', 'url':'https://www.gmsh.info/doc/texinfo/gmsh.html', 'scope':'Geometry, meshing and mesh elements'},
 'pcdmis': {'title':'Hexagon PC-DMIS', 'url':'https://hexagon.com/products/pc-dmis', 'scope':'Dimensional inspection, probing and metrology'},
 'calypso': {'title':'ZEISS CALYPSO', 'url':'https://www.zeiss.com/metrology/en/software/zeiss-calypso.html', 'scope':'Dimensional metrology and measurement planning'},
 'robodk': {'title':'RoboDK robot programs', 'url':'https://robodk.com/doc/en/Robot-Programs.html', 'scope':'Robot programming, targets and motion instructions'},
 'moveit': {'title':'MoveIt concepts', 'url':'https://moveit.ai/documentation/concepts/', 'scope':'Motion planning, kinematics and collision checking'},
}

# Reviewed 2026-10-17: per-entry references for newly added commands/objects.
# These documents establish semantics only; no vendor artwork is bundled.
REFERENCES.update({
 'solidworks-features-2026':{'title':'SOLIDWORKS 2026 Features toolbar','url':'https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Features_Toolbar.htm?id=2.12.4.1.11','scope':'Hole, thread, draft and rib feature commands'},
 'onshape-split':{'title':'Onshape Split','url':'https://cad.onshape.com/help/Content/PartStudio/split.htm','scope':'Split parts using surfaces or planes'},
 'onshape-thicken':{'title':'Onshape Thicken','url':'https://cad.onshape.com/help/Content/PartStudio/thicken.htm','scope':'Add thickness to surfaces to create solids'},
 'onshape-offset-surface':{'title':'Onshape Offset surface','url':'https://cad.onshape.com/help/Content/PartStudio/offset_surface.htm','scope':'Create a normal offset surface'},
 'onshape-project':{'title':'Onshape Use projected geometry','url':'https://cad.onshape.com/help/Content/Sketch/use.htm','scope':'Reference projected external geometry in a sketch'},
 'fusion-sketch-constraints':{'title':'Fusion sketch constraints','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-Sketch/files/SKT-CONSTRAINTS.htm','scope':'Horizontal/vertical, concentric and midpoint constraints'},
 'onshape-mass-properties':{'title':'Onshape Mass properties','url':'https://cad.onshape.com/help/Content/View/mass_properties_tool.htm','scope':'Mass, center of mass and inertia'},
 'fusion-mesh-convert':{'title':'Fusion Convert Mesh','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-Mesh/files/MESH-CONVERT-TO-SOLID.htm','scope':'Mesh bodies and conversion to B-rep'},
 'onshape-feature-parts':{'title':'Onshape feature and parts lists','url':'https://cad.onshape.com/help/Content/PartStudio/features_and_parts_lists.htm','scope':'Part, sketch and feature list objects; feature nodes reuse their creating tool icons'},
 'onshape-instances':{'title':'Onshape assembly instances list','url':'https://cad.onshape.com/help/Content/Assembly/instances_list.htm','scope':'Assemblies, component instances and their containment'},
 'solidworks-multibody':{'title':'SOLIDWORKS multibody overview','url':'https://help.solidworks.com/2026/English/SolidWorks/Sldworks/c_Multibody_Overview.htm','scope':'One part can contain multiple solid and surface bodies'},
 'fusion-components':{'title':'Fusion components, occurrences and proxies','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ComponentsProxies_UM.htm','scope':'Component definitions versus placed occurrences'},
 'fusion-manufacture-browser':{'title':'Fusion Manufacture browser','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/GUIDB87E0180-7CDD-41B0-866C-EEDACB946E09.htm','scope':'Setups, operation groups, folders and NC program tree organization'},
 'fusion-nc-program':{'title':'Fusion NC programs','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/MFG-NC-PROGRAM-OVERVIEW.htm','scope':'NC program nodes and post-processing output'},
 'fusion-thread-milling':{'title':'Fusion 2D Thread','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/2D-THREAD-STEPS.htm','scope':'Helical thread milling operation'},
 'fusion-holding-tabs':{'title':'Fusion 2D Contour reference','url':'https://help.autodesk.com/view/fusion360/ENU/?contextId=MFG-REF-2D-CONTOUR-CMD','scope':'Holding tabs left in contour cutting'},
 'fusion-engrave':{'title':'Fusion Engrave reference','url':'https://help.autodesk.com/view/fusion360/ENU/?contextId=MFG-REF-2D-ENGRAVE-CMD','scope':'V-tool engraving with sharp corners'},
 'fusion-cam-chamfer':{'title':'Fusion 2D Chamfer','url':'https://help.autodesk.com/view/fusion360/ENU/?contextId=2D-CHAMFER-STEPS','scope':'Machining edge chamfers with a cutter'},
 'ansys-gravity':{'title':'Ansys Mechanical Standard Earth Gravity','url':'https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/wb_sim/ds_Gravity.html','scope':'Gravity as an acceleration/body load'},
 'ansys-moment':{'title':'Ansys Mechanical Moment','url':'https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/wb_sim/ds_Moment.html','scope':'Moment loading of scoped model regions'},
 'ansys-symmetry':{'title':'Ansys Mechanical Symmetry Region','url':'https://ansyshelp.ansys.com/public/Views/Secured/corp/v251/en/mech_obj/ds_Symmetry_Region_o_r.html','scope':'Symmetry boundary object and constraints'},
 'gmsh-physical-groups':{'title':'Gmsh elementary entities and physical groups','url':'https://gmsh.info/doc/texinfo/gmsh.html#Elementary-entities-vs-physical-groups','scope':'Reusable semantic groups of geometry/mesh entities'},
 'ansys-inflation':{'title':'Ansys Meshing Inflation','url':'https://ansyshelp.ansys.com/public/views/secured/corp/v252/en/wb_msh/ds_Inflation.html','scope':'Graded wall-normal boundary-layer elements'},
 'openfoam-boundaries':{'title':'OpenFOAM boundary conditions','url':'https://doc.openfoam.com/2306/tools/processing/boundary-conditions/','scope':'Distinct inlet, outlet and wall condition families; version 2306 reference'},
 'openfoam-streamline':{'title':'OpenFOAM streamLine','url':'https://doc.openfoam.com/2306/tools/post-processing/function-objects/field/streamLine/','scope':'Vector-field streamline tracing; version 2306 reference'},
})
REFERENCES.update({
 'fusion-brep-face':{'title':'Fusion BRepFace API object','url':'https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_BRepFace.htm','scope':'One bounded face and its parent body/shell; topology-object use, not a claim about a default browser node'},
 'freecad-partdesign-commands':{'title':'FreeCAD PartDesign command registration','url':'https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/PartDesign/Gui/Workbench.cpp','scope':'Official source registration of Hole, Draft and other PartDesign commands'},
 'freecad-holding-tags':{'title':'FreeCAD CAM holding tags','url':'https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/CAM_DressupTag.md','scope':'Holding-tag dressup object beneath an operation; archived official documentation, not a current-version UI claim'},
 'mastercam-deburr':{'title':'Mastercam 2025 feature overview','url':'https://www.mastercam.com/community/blog/10-mastercam-2025-features-you-need-to-know/','scope':'Independent Deburr machining command, separate from modeled CAD chamfers'},
 'ansys-analysis-tree':{'title':'Ansys Mechanical analysis environment object','url':'https://ansyshelp.ansys.com/public/Views/Secured/corp/v252/en/mech_obj/ds_Environment_o_r.html','scope':'Analysis tree children including Analysis Settings'},
})

# Individually researched application command families.
from application import APPLICATION_REFERENCES
REFERENCES.update(APPLICATION_REFERENCES)
from robotics import ROBOTICS_REFERENCES
REFERENCES.update(ROBOTICS_REFERENCES)
from studio import STUDIO_REFERENCES
REFERENCES.update(STUDIO_REFERENCES)
