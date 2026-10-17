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
