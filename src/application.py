"""Reviewed command families from other applications, with original geometry.

Every key is an individually selected operation, never a generated variant.
The adjacent JSON keeps bilingual semantics and primary references reviewable.
"""
import json
from pathlib import Path
from core import p, r, c, g, accent, fill, nodes, PALE, TEAL

GLYPHS = {}

# Surface-mesh editing operates on vertices, edges, faces and texture coordinates.
GLYPHS['cad-mesh-bridge'] = (p('M3 8 10 5 V25 L3 28Z M22 5 29 8 V28 L22 25Z')
    + accent('M10 5 22 5 M10 15 H22 M10 25 22 25') + p('M16 5 V25',stroke_dasharray='2 3'))
GLYPHS['cad-mesh-inset'] = (r(4,4,24,24,1) + r(10,10,12,12,1,fill=PALE,stroke=TEAL)
    + p('M4 4 10 10 M28 4 22 10 M4 28 10 22 M28 28 22 22'))
GLYPHS['cad-mesh-loop-cut'] = (fill('M4 9 16 4 28 9 V24 L16 29 4 24Z')
    + p('M4 9 16 14 28 9 M16 14 V29') + accent('M4 16 16 21 28 16'))
GLYPHS['cad-mesh-knife'] = (r(3,10,23,19,1,fill=PALE) + p('M14 10 V29')
    + accent('M3 24 11 17 19 22 26 16') + p('M20 9 25 3 29 6 24 12 19 14Z',fill='white'))
GLYPHS['cad-mesh-merge-vertices'] = (p('M3 4 10 10 M29 4 22 10 M3 28 10 22 M29 28 22 22')
    + nodes([(10,10),(22,10),(10,22),(22,22)])
    + accent('M10 10 16 16 22 10 M10 22 16 16 22 22') + c(16,16,3,fill=TEAL))
GLYPHS['cad-mesh-dissolve'] = (r(4,5,24,22,1,fill=PALE)
    + p('M16 5 V27',stroke_dasharray='3 4') + accent('M9 13 6 16 9 19 M6 16 H12 M23 13 26 16 23 19 M20 16 H26'))
GLYPHS['cad-mesh-fill-holes'] = (p('M4 5 H28 V27 H4Z M4 5 11 12 M28 5 22 11 M28 27 22 21 M4 27 10 22')
    + fill('M11 12 22 11 22 21 10 22Z') + accent('M11 12 22 21 M10 22 22 11')
    + p('M4 16 H10 M22 16 H28 M16 5 V11 M16 22 V27'))
GLYPHS['cad-mesh-decimate'] = (p('M3 5 H14 V27 H3Z M3 5 14 13 3 20 14 27 M3 13 14 5 M3 27 14 20')
    + fill('M22 5 H29 V27 H22Z') + p('M22 5 29 27')
    + accent('M14 16 H22 M18 12 22 16 18 20'))
GLYPHS['cad-mesh-remesh'] = (p('M3 4 H13 V28 H3Z M3 4 13 12 3 18 13 28 M3 28 13 12')
    + r(20,4,9,24,1,fill=PALE) + accent('M20 12 H29 M20 20 H29 M24.5 4 V28')
    + p('M14 16 H19 M16 13 19 16 16 19'))
GLYPHS['cad-mesh-smooth'] = (p('M3 24 9 6 17 24 24 7 29 21',stroke_dasharray='2 3')
    + accent('M3 24 C10 4 11 28 18 17 S26 8 29 21') + nodes([(3,24),(9,6),(17,24),(24,7),(29,21)]))
GLYPHS['cad-mesh-shrinkwrap'] = (p('M4 5 H28 M4 3 V10 M16 3 V10 M28 3 V10')
    + fill('M3 28 Q16 10 29 28Z') + accent('M7 11 V20 M4 17 7 20 10 17 M16 11 V16 M13 13 16 16 19 13 M25 11 V20 M22 17 25 20 28 17'))
GLYPHS['cad-uv-unwrap'] = (fill('M3 6 9 3 15 6 V16 L9 19 3 16Z')
    + p('M3 6 9 9 15 6 M9 9 V19') + accent('M21 9 H26 V14 H30 V19 H26 V24 H21 V19 H16 V14 H21Z')
    + p('M3 24 V29 H13 M21 14 H26 V19 H21Z'))

# Manufacturing operations and machine compensation.
# Free-form surfacing and inspection, with distinct input/output relationships.
GLYPHS['cad-surface-blend'] = (fill('M3 4 H10 V16 H3Z') + fill('M22 16 H29 V28 H22Z')
    + accent('M10 4 C19 4 13 16 22 16 M10 16 C19 16 13 28 22 28') + p('M10 10 C19 10 13 22 22 22',stroke_dasharray='2 3'))
GLYPHS['cad-surface-match'] = (fill('M3 8 Q9 4 16 10 V26 Q9 20 3 24Z')
    + p('M16 10 Q23 16 29 9 V25 Q23 32 16 26Z') + accent('M16 10 V26 M6 14 13 17 M19 20 26 23')
    + p('M10 13 13 17 9 18 M23 19 26 23 22 24'))
GLYPHS['cad-surface-network'] = (fill('M3 9 Q15 2 29 9 L25 26 Q15 19 7 27Z')
    + accent('M5 16 Q15 9 27 17 M6 22 Q15 15 26 22')
    + p('M10 6 Q8 15 13 24 M20 6 Q17 15 20 24'))
GLYPHS['cad-nurbs-rebuild'] = (p('M3 9 8 4 14 11 20 4 29 9',stroke_dasharray='2 3')
    + nodes([(3,9),(8,4),(14,11),(20,4),(29,9)])
    + accent('M3 27 C9 12 22 12 29 27') + p('M3 27 9 17 H23 L29 27',stroke_dasharray='2 3')
    + nodes([(3,27),(9,17),(23,17),(29,27)]))
GLYPHS['cad-extract-isocurve'] = (fill('M3 10 Q12 2 22 8 L22 22 Q12 16 3 24Z')
    + p('M9 6 V20 M16 6 V20 M3 17 Q12 9 22 15')
    + accent('M9 26 Q17 18 28 23 M25 19 28 23 24 26'))
GLYPHS['cad-cage-deform'] = (p('M3 9 15 3 29 7 25 25 14 29 3 24Z M3 9 14 14 29 7 M14 14 V29 M15 3 14 14')
    + p('M3 24 15 19 25 25 M15 3 V19',stroke_dasharray='2 3')
    + c(15,18,5,fill=PALE,stroke=TEAL) + nodes([(3,9),(15,3),(29,7),(25,25),(14,29),(3,24)]))
GLYPHS['cad-flow-along-surface'] = (p('M3 10 H28 M5 3 H10 V8 H5Z M15 3 H20 V8 H15Z')
    + fill('M3 26 Q16 11 29 26') + p('M6 21 10 17 14 21 10 25Z M20 18 25 21 22 26 17 23Z',stroke=TEAL)
    + accent('M28 11 V17 M25 14 28 17 30 14'))
GLYPHS['cad-zebra-analysis'] = (fill('M4 7 Q15 1 28 8 V25 Q15 31 4 24Z')
    + p('M7 6 C22 8 5 23 20 28 M14 5 C29 7 12 22 27 25',stroke=TEAL,stroke_width=3)
    + p('M4 17 Q15 11 28 18',stroke_dasharray='2 3'))
GLYPHS['cad-draft-analysis'] = (p('M3 28 H23 M4 24 10 8 H18 L24 24Z',fill=PALE)
    + accent('M4 24 10 8 M18 8 24 24 M28 25 V4 M25 7 28 4 30 7')
    + p('M10 8 V24',stroke_dasharray='2 3') + p('M7 18 Q11 16 15 18'))

# Point-cloud processing changes samples, attributes or reconstruction.
# Sheet-metal, weldment and mold features describe different manufacturing intent.
GLYPHS['cad-sheet-metal-hem'] = (p('M3 22 H23 A7 7 0 0 0 23 8 H14 V12 H23 A3 3 0 0 1 23 18 H3Z',fill=PALE)
    + accent('M18 8 H23 A7 7 0 0 1 30 15') + p('M4 26 H20',stroke_dasharray='2 3'))
GLYPHS['cad-sheet-metal-jog'] = (fill('M3 22 H12 L20 8 H29 V13 H23 L15 27 H3Z')
    + accent('M12 22 20 8 M3 16 H8 M25 20 H29') + p('M7 7 H16 M11 4 7 7 11 10'))
GLYPHS['cad-sheet-metal-form-tool'] = (fill('M7 3 H25 V7 H21 V12 H11 V7 H7Z')
    + fill('M3 28 V24 H10 V19 H22 V24 H29 V28Z')
    + accent('M16 11 V19 M13 16 16 19 19 16'))
GLYPHS['cad-sheet-metal-corner-relief'] = (fill('M3 5 H25 V10 H10 V26 H3Z')
    + fill('M10 10 H29 V29 H10Z') + p('M10 10 29 29')
    + c(10,10,4,fill='white',stroke=TEAL))
GLYPHS['cad-sheet-metal-tab-slot'] = (fill('M3 5 H11 V12 H16 V20 H11 V27 H3Z')
    + r(21,4,8,24,1,fill=PALE) + p('M24 11 H27 V21 H24Z',fill='white')
    + accent('M14 7 H20 M17 4 20 7 17 10'))
GLYPHS['cad-convert-sheet-metal'] = (fill('M3 4 H8 V17 H14 V23 H3Z')
    + p('M22 3 V21 H29 V27 H18 V10',fill=PALE) + accent('M18 21 H25',stroke_dasharray='2 3')
    + accent('M10 10 H22 M18 6 22 10 18 14'))
GLYPHS['cad-weldment-member'] = (fill('M3 21 20 4 H29 V8 H26 L9 25 H12 V29 H3Z')
    + p('M3 21 H12 V25 H9 M20 4 V8 H23 L6 25 M12 29 29 12 V8')
    + accent('M6 18 18 6',stroke_dasharray='2 3'))
GLYPHS['cad-weldment-trim-extend'] = (fill('M3 4 H10 V22 H28 V29 H3Z')
    + p('M10 22 H27 V15 H17 V4 H10 M10 22 3 29')
    + accent('M4 23 10 17 M14 19 23 10 M19 10 H23 V14'))
GLYPHS['cad-weldment-end-cap'] = (fill('M3 8 17 3 26 7 12 13Z')
    + p('M3 8 V21 L12 26 26 20 V7 M12 13 V26 M6 11 V19 L10 21 V14Z')
    + fill('M17 17 28 13 V26 L17 30Z') + accent('M20 20 25 18 M20 25 25 23'))
GLYPHS['cad-weldment-gusset'] = (fill('M3 3 H9 V23 H29 V29 H3Z')
    + p('M12 8 26 21 H12Z',fill=PALE,stroke=TEAL)
    + c(15,17,1,fill=TEAL,stroke='none') + p('M10 26 H23',stroke_dasharray='2 3'))
GLYPHS['cad-weld-bead'] = (fill('M3 4 H9 V23 H29 V29 H3Z')
    + accent('M10 13 Q17 13 13 18 Q20 17 17 22 Q24 21 22 26')
    + p('M12 4 V10 M29 20 H25',stroke_dasharray='2 3'))
GLYPHS['cad-mold-parting-line'] = (p('M5 14 Q16 4 27 14 V22 Q16 30 5 22Z',fill=PALE)
    + accent('M5 18 Q16 26 27 18') + p('M16 3 V8 M13 6 16 3 19 6 M16 27 V31'))
GLYPHS['cad-mold-tooling-split'] = (fill('M3 3 H29 V10 H23 Q16 4 9 10 H3Z')
    + fill('M3 23 H9 Q16 29 23 23 H29 V29 H3Z')
    + p('M8 16 Q16 10 24 16 Q16 22 8 16Z',stroke=TEAL,fill=PALE)
    + accent('M3 17 V13 M29 16 V20'))
GLYPHS['cad-auto-route'] = (r(3,3,8,7,1,fill=PALE) + r(21,22,8,7,1,fill=PALE)
    + p('M5 10 V18 Q5 25 13 25 H21 M9 10 V17 Q9 21 15 21 H23')
    + accent('M7 10 V17 Q7 23 14 23 H21') + p('M11 18 V27 M15 19 V28 M5 3 V6 M9 3 V6 M24 26 H29'))

# Vector paths and drawing entities: editing, conversion and reusable definitions.
GLYPHS['cad-edit-path-nodes'] = (accent('M3 26 C6 5 25 28 29 6')
    + p('M6 8 23 24') + c(6,8,2,fill='white') + c(23,24,2,fill='white')
    + r(11,12,7,7,1,fill=PALE) + p('M24 3 29 6 26 11'))
GLYPHS['cad-stroke-to-path'] = (p('M4 25 Q14 16 5 5',stroke_width=4)
    + p('M23 4 Q32 16 23 28 L19 24 Q25 16 19 8Z',fill=PALE)
    + nodes([(23,4),(23,28),(19,24),(19,8)]) + accent('M10 16 H20 M16 12 20 16 16 20'))
GLYPHS['cad-trace-bitmap'] = (fill('M3 25 V15 H7 V8 H12 V4 H16 V25Z')
    + p('M3 19 H16 M7 8 V25 M12 4 V25 M7 13 H16')
    + accent('M21 27 C20 13 25 11 29 4') + nodes([(21,27),(24,14),(29,4)]))
GLYPHS['cad-drawing-hatch'] = (fill('M4 4 H20 L28 12 V28 H4Z')
    + accent('M4 12 12 4 M4 20 20 4 M4 28 24 8 M12 28 28 12 M20 28 28 20'))
GLYPHS['cad-create-block'] = (r(6,3,23,23,2) + c(14,11,4,fill=PALE) + p('M20 11 V20 H11')
    + accent('M3 26 H11 M7 22 V30') + c(7,26,1.5,fill=TEAL))
GLYPHS['cad-explode-entities'] = (r(11,11,10,10,1,stroke_dasharray='2 3')
    + c(7,5,3,fill=PALE) + p('M23 3 29 9 M3 22 V29 H10 M24 21 29 29 H21Z',fill=PALE)
    + accent('M12 12 9 9 M21 11 24 8 M11 21 8 24 M21 21 24 24'))
GLYPHS['common-align-objects'] = (p('M5 3 V29') + r(9,4,19,5,1,fill=PALE)
    + r(9,14,11,5,1,fill=PALE) + r(9,24,15,5,1,fill=PALE)
    + accent('M3 6 H5 M3 16 H5 M3 26 H5'))
GLYPHS['common-distribute-objects'] = (r(3,4,5,15,1,fill=PALE) + r(13,4,7,15,1,fill=PALE) + r(25,4,4,15,1,fill=PALE)
    + accent('M8 26 H13 M8 23 V29 M13 23 V29 M20 26 H25 M20 23 V29 M25 23 V29') + p('M10 23 H11 M22 23 H23'))

# Point-cloud processing changes samples, attributes or reconstruction.
GLYPHS['cmm-cloud-subsample'] = (''.join(c(x,y,1.2,fill=TEAL,stroke='none') for x,y in [(3,5),(8,5),(13,5),(3,11),(8,11),(13,11),(3,17),(8,17),(13,17),(3,23),(8,23),(13,23),(3,29),(8,29),(13,29)])
    + nodes([(25,6),(25,16),(25,26)]) + accent('M15 16 H21 M18 13 21 16 18 19'))
GLYPHS['cmm-cloud-outlier-removal'] = (''.join(c(x,y,1.5,fill=TEAL,stroke='none') for x,y in [(6,17),(12,15),(17,18),(5,23),(11,23),(17,25),(23,20),(24,27)])
    + c(25,5,2,fill=PALE) + p('M5 3 12 10 M12 3 5 10') + accent('M14 6 H20',stroke_dasharray='2 3'))
GLYPHS['cmm-cloud-normals'] = (p('M3 28 Q16 12 29 25',stroke_dasharray='2 3')
    + nodes([(7,24),(16,20),(25,23)])
    + accent('M7 24 3 13 M2 17 3 13 7 15 M16 20 V7 M13 10 16 7 19 10 M25 23 29 12 M25 14 29 12 30 16'))
GLYPHS['cmm-cloud-components'] = (''.join(c(x,y,1.6,fill=TEAL,stroke='none') for x,y in [(6,8),(10,12),(6,17),(11,22),(22,10),(26,15),(21,21),(26,25)])
    + p('M10 3 H3 V26 H7 M23 5 H29 V29 H20') + p('M16 5 V28',stroke_dasharray='2 3'))
GLYPHS['cmm-cloud-primitive-detection'] = (''.join(c(x,y,1.1,fill=TEAL,stroke='none') for x,y in [(3,8),(5,16),(4,24),(12,3),(25,8),(29,15),(28,24),(14,29),(17,19),(11,15)])
    + p('M9 9 C9 3 23 3 23 9 V24 C23 30 9 30 9 24Z M9 9 C9 15 23 15 23 9',fill='none')
    + accent('M9 19 C9 25 23 25 23 19',stroke_dasharray='2 3'))
GLYPHS['cmm-cloud-reconstruct'] = (''.join(c(x,y,1.4,fill=TEAL,stroke='none') for x,y in [(4,12),(9,7),(13,4),(5,21),(11,16),(13,27),(9,24)])
    + fill('M18 4 27 10 29 21 18 28Z') + p('M18 4 23 16 27 10 M18 28 23 16 29 21 M18 16 H23'))
GLYPHS['cmm-cloud-rasterize'] = (''.join(c(x,y,1.3,fill=TEAL,stroke='none') for x,y in [(4,8),(9,5),(14,8),(20,4),(26,8),(6,12),(16,11),(24,12)])
    + fill('M3 19 16 15 29 19 V26 L16 30 3 26Z') + p('M3 19 16 23 29 19 M16 23 V30 M9 17 22 21 V28 M23 17 9 21 V28')
    + accent('M16 7 V14 M13 11 16 14 19 11'))

# Manufacturing operations and machine compensation.
GLYPHS['cam-wire-edm'] = (r(12,3,8,5,1,fill=PALE) + r(12,25,8,4,1,fill=PALE)
    + fill('M3 12 H12 V21 H3Z') + fill('M20 12 H29 V21 H20Z')
    + accent('M16 8 V25 M5 8 H10 M7 5 10 8 7 11 M22 25 H28'))
GLYPHS['cam-cutter-compensation'] = (p('M5 27 V9 Q5 5 9 5 H27')
    + accent('M12 27 V16 Q12 12 16 12 H27') + c(21,21,5,fill=PALE)
    + p('M21 21 H26 M21 21 V16') + c(21,21,1,fill=TEAL))
GLYPHS['cam-tool-touch-off'] = (r(9,3,8,12,1,fill=PALE) + p('M13 15 V22 M3 25 H20 M7 28 H18')
    + accent('M24 5 V25 M21 8 24 5 27 8 M21 22 24 25 27 22') + c(13,24,1.5,fill=TEAL))
GLYPHS['cam-stock-model'] = (fill('M3 10 H16 V17 H28 V28 H3Z')
    + p('M3 22 H21 V28') + r(20,3,5,10,1,fill=PALE)
    + accent('M7 4 H15 M12 1 15 4 12 7 M18 17 H28'))
GLYPHS['cam-recognize-holes'] = (r(7,7,18,18,2,fill=PALE)
    + c(12,12,2) + c(20,12,2) + c(16,20,2)
    + accent('M3 11 V3 H11 M21 3 H29 V11 M29 21 V29 H21 M11 29 H3 V21'))
GLYPHS['cam-groove-turning'] = (fill('M3 16 H12 V23 H20 V16 H29 V29 H3Z')
    + p('M3 25 H29',stroke_dasharray='2 3') + r(14,3,4,16,1,fill=PALE)
    + accent('M24 3 V12 M21 9 24 12 27 9'))
GLYPHS['cam-thread-turning'] = (r(3,16,26,12,2,fill=PALE)
    + p('M6 28 11 16 M12 28 17 16 M18 28 23 16 M24 28 29 16')
    + fill('M10 6 H20 L15 15Z') + accent('M22 8 H29 M26 5 29 8 26 11'))
GLYPHS['cam-constant-z-finishing'] = (fill('M3 26 12 6 H20 L29 26Z')
    + accent('M8 15 Q16 20 24 15 M5 21 Q16 27 27 21 M11 9 Q16 12 21 9')
    + p('M3 26 Q16 32 29 26'))
GLYPHS['cam-pencil-finishing'] = (fill('M3 15 16 23 29 15 V23 L16 30 3 23Z')
    + accent('M16 23 V30') + p('M13 3 H19 V17 A3 3 0 0 1 13 17Z',fill='white')
    + p('M16 20 V23') + accent('M24 4 V12 M21 9 24 12 27 9'))
GLYPHS['cam-nesting'] = (r(3,3,26,26,1)
    + fill('M7 7 H17 V11 H11 V21 H7Z')
    + p('M15 15 H25 V25 H15 V21 H21 V19 H15Z',fill=PALE,stroke=TEAL)
    + c(23,8,2.5))
GLYPHS['cam-port-machining'] = (fill('M3 28 V16 Q3 5 15 5 H27 V12 H16 Q10 12 10 19 V28Z')
    + p('M3 28 Q7 24 10 28 M27 5 Q23 8 27 12')
    + accent('M7 23 V17 Q7 9 18 9')
    + g(r(19,16,5,12,1,fill=PALE)+p('M19 24 24 20'),transform='rotate(34 21 22)'))
GLYPHS['cam-trim-toolpath'] = (accent('M4 6 H17 V12 H4 V18 H17 V24 H4')
    + p('M22 3 V29 M22 6 H29 V12 H22 M22 18 H29 V24 H22',stroke_dasharray='2 3')
    + p('M18 28 H27 M23 25 27 28 23 31'))
GLYPHS['cam-reorder-toolpath'] = (p('M3 6 H17 M3 16 H17 M3 26 H17')
    + accent('M25 4 V26 M22 23 25 26 28 23 M20 9 23 6 20 3')
    + p('M17 6 20 10 17 16 M17 16 20 21 17 26',stroke_dasharray='2 3'))

# Finite-element topology repair.
GLYPHS['cae-sew-mesh'] = (p('M3 5 H11 V27 H3Z M3 5 11 16 3 27 M21 5 H29 V27 H21Z M29 5 21 16 29 27')
    + accent('M11 5 H21 M11 16 H21 M11 27 H21') + nodes([(11,5),(21,5),(11,16),(21,16),(11,27),(21,27)]))
GLYPHS['cae-orient-faces'] = (fill('M3 25 9 14 16 25Z') + fill('M16 25 23 14 29 25Z')
    + accent('M9 19 V4 M6 7 9 4 12 7 M23 19 V4 M20 7 23 4 26 7')
    + p('M13 10 Q16 7 19 10 M16 11 19 10 18 7'))
GLYPHS['cae-element-order'] = (fill('M4 27 16 5 28 27Z')
    + nodes([(4,27),(16,5),(28,27)]) + ''.join(c(x,y,2,fill=TEAL,stroke=TEAL) for x,y in [(10,16),(22,16),(16,27)])
    + p('M13 17 H19 M16 14 V20'))
GLYPHS['cae-boundary-elements'] = (p('M3 9 10 5 17 9 V23 L10 27 3 23Z M3 9 10 13 17 9 M10 13 V27')
    + fill('M23 9 29 5 V23 L23 27Z') + accent('M23 9 29 23 M23 27 29 5')
    + p('M17 16 H22 M19 13 22 16 19 19'))
GLYPHS['cae-material-orientation'] = (fill('M3 25 10 5 27 10 20 29Z')
    + p('M8 23 13 9 M12 25 17 10 M16 26 21 11')
    + accent('M22 22 V4 M19 7 22 4 25 7 M22 22 H30 M27 19 30 22 27 25'))
GLYPHS['cae-composite-layup'] = (fill('M3 21 16 15 29 21 16 28Z')
    + fill('M3 15 16 9 29 15 16 22Z') + fill('M3 9 16 3 29 9 16 16Z')
    + accent('M9 7 22 13 M14 5 27 11 M4 15 16 21 M7 23 17 18'))
GLYPHS['cae-rigid-connection'] = (p('M16 16 5 6 M16 16 27 6 M16 16 5 27 M16 16 27 27',stroke_width=2.5)
    + nodes([(5,6),(27,6),(5,27),(27,27)]) + c(16,16,4,fill=PALE,stroke=TEAL)
    + accent('M16 4 V8 M4 16 H8 M24 16 H28 M16 24 V28'))
GLYPHS['cae-spring-connection'] = (p('M3 12 H7 L10 5 14 19 18 5 22 19 25 12 H29')
    + nodes([(3,12),(29,12)]) + accent('M5 27 H27 M8 24 5 27 8 30 M24 24 27 27 24 30'))
GLYPHS['cae-bolt-pretension'] = (r(12,6,8,20,1,fill=PALE) + r(8,4,16,4,1) + r(9,24,14,5,1)
    + p('M12 18 H20 M12 21 H20') + accent('M4 16 V3 M2 6 4 3 7 6 M28 16 V29 M25 26 28 29 30 26'))
GLYPHS['cae-map-loads'] = (r(3,12,9,16,1)+p('M3 20 H12 M7.5 12 V28')
    + r(21,12,9,16,1,fill=PALE)+p('M21 17 H30 M21 22 H30 M24 12 V28 M27 12 V28')
    + accent('M5 3 V9 M3 7 5 9 7 7 M26 3 V9 M24 7 26 9 28 7 M12 19 H20 M17 16 20 19 17 22'))
GLYPHS['cae-harmonic-response'] = (p('M16 4 V27 H30')
    + accent('M3 14 Q5 3 7 14 T11 14 M19 24 C22 24 20 7 24 7 C28 7 25 24 29 24')
    + p('M2 21 H12 M9 18 12 21 9 24'))
GLYPHS['cae-coupling-interface'] = (p('M16 3 V29',stroke_dasharray='2 3')
    + accent('M3 7 Q6 3 9 7 M3 24 Q6 20 9 24 M7 12 H24 M21 9 24 12 21 15 M24 21 H7 M10 18 7 21 10 24')
    + p('M22 3 H29 V29 H22 M22 6 H29 M25 3 V8 M22 26 H29 M25 25 V29'))
GLYPHS['cae-isosurface'] = (p('M3 9 16 3 29 9 V24 L16 30 3 24Z M3 9 16 15 29 9 M16 15 V30',stroke_dasharray='2 3')
    + p('M9 21 C5 13 17 7 23 14 C30 24 15 27 9 21Z',fill=PALE,stroke=TEAL)
    + p('M19 17 28 4 M25 4 H28 V7'))
GLYPHS['cae-vector-glyphs'] = (r(3,3,26,26,1)+p('M3 16 H29 M16 3 V29',stroke_dasharray='2 3')
    + accent('M7 12 V6 M4 9 7 6 10 9 M20 12 26 6 M22 6 H26 V10 M7 25 13 19 M9 19 H13 V23 M20 24 H27 M24 21 27 24 24 27'))
GLYPHS['cae-integrate-results'] = (fill('M3 7 H14 V25 H3Z') + p('M3 13 H14 M3 19 H14 M8 7 V25')
    + accent('M15 16 H20 M17 13 20 16 17 19')
    + p('M29 4 Q25 1 25 8 V24 Q25 31 21 28'))
GLYPHS['cae-field-calculator'] = (r(3,3,10,10,1,fill=PALE) + p('M3 8 H13 M8 3 V13')
    + r(19,19,10,10,1,fill=PALE) + p('M19 24 H29 M24 19 V29')
    + accent('M21 5 H29 M25 1 V9 M4 22 H12 M4 27 H12')
    + p('M10 18 18 10 M14 10 H18 V14'))
GLYPHS['cae-temporal-statistics'] = (p('M3 18 V3 H18 M7 22 V7 H22') + r(11,11,18,18,1,fill=PALE)
    + accent('M14 23 17 16 20 25 23 17 26 21') + p('M13 21 H27',stroke_dasharray='2 3'))

# Inspection-specific environment compensation and path planning.
GLYPHS['cmm-temperature-compensation'] = (r(4,17,16,11,1,fill=PALE)
    + p('M4 12 H20 M4 9 V15 M20 9 V15') + accent('M8 10 6 12 8 14 M16 10 18 12 16 14')
    + p('M24 6 A2 2 0 0 1 28 6 V19 A4 4 0 1 1 24 19Z') + accent('M26 12 V23'))
GLYPHS['cmm-optimize-path'] = (p('M8 6 4 26 27 26 23 16 8 6',stroke_dasharray='2 3')
    + accent('M8 6 23 16 4 26') + nodes([(8,6),(23,16),(4,26)])
    + r(21,3,7,5,1,fill=PALE) + p('M24.5 8 V12') + c(24.5,13,1.5,fill=TEAL))

# Robot path generation is distinct from testing or individual Move instructions.
GLYPHS['olp-curve-follow'] = (accent('M3 26 C10 10 20 29 29 9')
    + p('M7 20 V8 M4 11 7 8 10 11 M17 21 V9 M14 12 17 9 20 12 M26 16 V4 M23 7 26 4 29 7')
    + nodes([(7,20),(17,21),(26,16)]))
GLYPHS['olp-plan-collision-free'] = (r(12,11,9,14,1,fill=PALE)
    + accent('M3 25 V10 Q3 4 9 4 H23 Q29 4 29 10 V25 M25 21 29 25 31 21')
    + nodes([(3,25),(29,25)]) + p('M7 28 H25',stroke_dasharray='2 3'))
GLYPHS['olp-synchronize-axes'] = (r(3,25,26,4,1,fill=PALE) + p('M8 25 V18 L4 12 13 6 17 11')
    + nodes([(8,18),(4,12),(13,6)]) + accent('M19 19 A6 6 0 1 1 28 14 M24 14 H28 V10')
    + p('M3 22 H13 M7 20 3 22 7 24 M25 18 25 25'))
GLYPHS['olp-robot-calibration'] = (p('M6 28 13 18 22 9',stroke_dasharray='2 3')
    + p('M6 28 10 16 20 6') + nodes([(6,28),(10,16),(20,6)])
    + accent('M15 18 H28 M17 15 V21 M22 15 V21 M27 15 V21 M20 6 25 10')
    + c(25,10,2,fill=PALE))
GLYPHS['olp-change-configuration'] = (p('M5 25 8 7 27 7',stroke_dasharray='2 3')
    + accent('M5 25 24 25 27 7') + nodes([(5,25),(8,7),(24,25),(27,7)])
    + p('M12 16 H20 M16 12 20 16 16 20'))

# The loader is deliberately strict: each reviewed command needs one drawing.
APPLICATION = {}
APPLICATION_REFERENCES = {}
APPLICATION_TREE = {}
APPLICATION_NAMES = {}
APPLICATION_REUSE = {}

def _load():
    records = json.loads(Path(__file__).with_name('application_commands.json').read_text(encoding='utf-8'))
    expected = {item['id'] for item in records}
    if len(expected) != len(records):
        raise ValueError('Duplicate reviewed command ID')
    if expected != set(GLYPHS):
        raise ValueError(f'Command/drawing mismatch: missing={expected-set(GLYPHS)}, unreviewed={set(GLYPHS)-expected}')
    for data in records:
        data = dict(data)
        full_id = data.pop('id')
        domain = data.pop('domain')
        reference = data.pop('sourceId')
        APPLICATION_REFERENCES[reference] = {
            'title': data.pop('sourceTitle'), 'url': data.pop('sourceUrl'), 'scope': data.pop('sourceScope')}
        sources = [reference]
        for extra in data.pop('additionalReferences', []):
            extra = dict(extra)
            key = extra.pop('id')
            APPLICATION_REFERENCES[key] = extra
            sources.append(key)
        data.pop('priority', None)
        data.pop('rationale', None)
        data.pop('glyph', None)
        data.pop('reviewNote', None)
        node = data.pop('modelTree', None)
        if node:
            APPLICATION_TREE[full_id] = {'objectType': node['objectType']}
            APPLICATION_NAMES[full_id] = (node['name'], node['nameJa'])
        data['id'] = full_id.split('-', 1)[1]
        data['body'] = GLYPHS[full_id]
        data['sources'] = sources
        data.setdefault('role', 'command')
        data['tags'] = list(dict.fromkeys(data['tags'] + [data['name'].lower(), data['nameJa'], domain.lower()]))
        APPLICATION.setdefault(domain, []).append(data)

_load()

for entry in json.loads(Path(__file__).with_name('application_reuse.json').read_text(encoding='utf-8')):
    data = dict(entry)
    id = data.pop('id')
    source = data.pop('sourceId')
    APPLICATION_REFERENCES[source] = {'title': data.pop('sourceTitle'), 'url': data.pop('sourceUrl'), 'scope': data.pop('sourceScope')}
    data['sources'] = [source]
    APPLICATION_REUSE[id] = data

def apply_reuse(item):
    """Enrich one existing symbol rather than emitting a synonym SVG."""
    data = APPLICATION_REUSE.get(item['id'], {})
    for key in ['aliases', 'tags', 'sources']:
        if key in data:
            item[key] = list(dict.fromkeys(item.get(key, []) + data[key]))
    for key in ['description', 'descriptionJa']:
        if key in data:
            item[key] = data[key]
