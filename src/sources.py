"""Primary references for feature taxonomy, never for tracing vendor artwork."""
SOURCE_IDS = {'CAD':['freecad','solidworks'], 'CAM':['fusion','linuxcnc'], 'CAE':['ansys','openfoam','gmsh'], 'CMM':['pcdmis','calypso'], 'OLP':['robodk','moveit']}
REFERENCES = {
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
