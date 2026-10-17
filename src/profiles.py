"""56 engineering cross-sections / planar boundaries for contextual symbols.

These are geometry contexts, not claims that commercial products expose 56
separate commands. The exact same operation can legitimately apply to each
closed, non-self-intersecting profile. Compound profiles preserve their holes.
"""
from math import sin,cos,pi

def polygon(points):return 'M'+' L'.join(f'{x:.3f} {y:.3f}' for x,y in points)+' Z'
def regular(n,rx=10,ry=None,phase=-pi/2):
 ry=rx if ry is None else ry
 return [(16+rx*cos(phase+2*pi*i/n),16+ry*sin(phase+2*pi*i/n)) for i in range(n)]
def gear(teeth,inner=8,outer=11):
 return [(16+(outer if i%4 in (1,2) else inner)*cos(2*pi*i/(teeth*4)),16+(outer if i%4 in (1,2) else inner)*sin(2*pi*i/(teeth*4))) for i in range(teeth*4)]
def rounded(points,ratio=.15):
 # Quadratic corner rounding of a polygon, preserving its actual corner order.
 chunks=[]
 for i,b in enumerate(points):
  a=points[i-1];c=points[(i+1)%len(points)]
  pre=(b[0]+(a[0]-b[0])*ratio,b[1]+(a[1]-b[1])*ratio)
  post=(b[0]+(c[0]-b[0])*ratio,b[1]+(c[1]-b[1])*ratio)
  chunks.append((pre,b,post))
 d=f'M{chunks[0][0][0]:.3f} {chunks[0][0][1]:.3f}'
 for pre,b,post in chunks:d+=f' L{pre[0]:.3f} {pre[1]:.3f} Q{b[0]:.3f} {b[1]:.3f} {post[0]:.3f} {post[1]:.3f}'
 return d+' Z'
PROFILES=[]
def add(id,en,ja,points,d=None,holes=False):
 PROFILES.append(dict(id=id,en=en,ja=ja,points=points,d=d or rounded(points,.09),holes=holes))
add('square','square','正方形',[(6,6),(26,6),(26,26),(6,26)])
add('rectangle','rectangular','長方形',[(4,10),(28,10),(28,22),(4,22)])
add('rounded-rectangle','rounded rectangular','角丸長方形',[(5,9),(27,9),(27,23),(5,23)],'M9 9 H23 Q27 9 27 13 V19 Q27 23 23 23 H9 Q5 23 5 19 V13 Q5 9 9 9Z')
add('circle','circular','円形',regular(32),'M16 5 A11 11 0 1 1 16 27 A11 11 0 1 1 16 5Z')
add('ellipse','elliptical','楕円',regular(32,12,8),'M4 16 A12 8 0 1 1 28 16 A12 8 0 1 1 4 16Z')
add('triangle','triangular','三角形',[(16,4),(28,26),(4,26)])
add('right-triangle','right triangular','直角三角形',[(5,5),(27,27),(5,27)])
add('pentagon','pentagonal','五角形',regular(5,12))
add('hexagon','hexagonal','六角形',regular(6,12))
add('octagon','octagonal','八角形',regular(8,11,phase=pi/8))
add('trapezoid','trapezoidal','台形',[(11,6),(21,6),(28,26),(4,26)])
add('parallelogram','parallelogram','平行四辺形',[(11,7),(28,7),(21,25),(4,25)])
add('rhombus','rhombic','菱形',[(16,3),(25,16),(16,29),(7,16)])
add('capsule','obround','長円',regular(32,12,6),'M10 10 H22 A6 6 0 0 1 22 22 H10 A6 6 0 0 1 10 10Z')
add('round-end-slot','round-end slot','片丸溝',[(10,4),(22,4),(22,22),(20,26),(16,28),(12,26),(10,22)],'M10 4 H22 V22 A6 6 0 0 1 10 22Z')
add('semicircle','semicircular','半円',[(5+22*i/24,23-18*sin(pi*i/24)) for i in range(25)],'M5 23 A11 16 0 0 1 27 23Z')
add('quarter-circle','quarter-circle','四分円',[(5,27),(5,5)]+[(5+22*sin(pi*i/32),27-22*cos(pi*i/32)) for i in range(17)],'M5 27 V5 A22 22 0 0 1 27 27Z')
add('sector','sector','扇形',[(16,27),(4,10),(8,6),(16,4),(24,6),(28,10)])
add('arch','arched','アーチ形',[(5,26),(5,16)]+[(16+11*cos(pi+pi*i/20),16+11*sin(pi+pi*i/20)) for i in range(21)]+[(27,26)],'M5 26 V16 A11 11 0 0 1 27 16 V26Z')
add('teardrop','teardrop','涙滴形',[(16,3),(25,17),(25,23),(21,27),(11,27),(7,23),(7,17)],'M16 3 Q27 16 27 21 A11 8 0 0 1 5 21 Q5 16 16 3Z')
add('l-section','L-section','L形',[(5,5),(12,5),(12,21),(27,21),(27,27),(5,27)])
add('t-section','T-section','T形',[(4,5),(28,5),(28,12),(20,12),(20,28),(12,28),(12,12),(4,12)])
add('u-section','U-section','U形',[(5,5),(12,5),(12,21),(20,21),(20,5),(27,5),(27,28),(5,28)])
add('i-section','I-section','I形',[(5,4),(27,4),(27,10),(20,10),(20,22),(27,22),(27,28),(5,28),(5,22),(12,22),(12,10),(5,10)])
add('c-section','lipped C-section','リップC形',[(5,5),(27,5),(27,13),(22,13),(22,10),(11,10),(11,22),(22,22),(22,19),(27,19),(27,27),(5,27)])
add('z-section','Z-section','Z形',[(4,5),(28,5),(28,12),(14,21),(28,21),(28,27),(4,27),(4,20),(18,11),(4,11)])
add('hat-section','hat-section','ハット形',[(4,21),(9,21),(9,5),(23,5),(23,21),(28,21),(28,27),(18,27),(18,11),(14,11),(14,27),(4,27)])
add('cross','cruciform','十字形',[(12,4),(20,4),(20,12),(28,12),(28,20),(20,20),(20,28),(12,28),(12,20),(4,20),(4,12),(12,12)])
add('stepped','stepped','段付き',[(5,4),(14,4),(14,11),(21,11),(21,18),(28,18),(28,28),(5,28)])
add('dovetail','dovetail','ダブテール',[(8,5),(24,5),(19,22),(28,22),(28,28),(4,28),(4,22),(13,22)])
add('dogbone','dog-bone','ドッグボーン',[(5,5),(12,5),(12,11),(20,11),(20,5),(27,5),(27,27),(20,27),(20,21),(12,21),(12,27),(5,27)])
add('keyhole','keyhole','鍵穴形',[(12,16),(8,12),(9,6),(16,3),(23,6),(24,12),(20,16),(23,28),(9,28)],'M12 17 A7.5 7.5 0 1 1 20 17 L23 28 H9Z')
add('keyway','keyed round','キー溝付き円',regular(32),'M12 6 A11 11 0 1 0 20 6 V12 H12Z')
add('d-shaft','D-shaped','Dカット',[(6,5),(16,5)]+[(16+11*cos(-pi/2+pi*i/24),16+11*sin(-pi/2+pi*i/24)) for i in range(25)]+[(6,27)],'M6 5 H16 A11 11 0 0 1 16 27 H6Z')
add('double-d','double-D','両側Dカット',[(8,7),(24,7),(27,16),(24,25),(8,25),(5,16)],'M8 7 H24 Q30 16 24 25 H8 Q2 16 8 7Z')
add('gear-6','six-tooth gear','6歯歯車',gear(6))
add('gear-8','eight-tooth gear','8歯歯車',gear(8))
add('gear-12','twelve-tooth gear','12歯歯車',gear(12))
add('star-5','five-lobe','5葉形',[(16+(12 if i%2==0 else 7)*cos(-pi/2+i*pi/5),16+(12 if i%2==0 else 7)*sin(-pi/2+i*pi/5)) for i in range(10)])
add('star-6','six-lobe','6葉形',[(16+(12 if i%2==0 else 7)*cos(-pi/2+i*pi/6),16+(12 if i%2==0 else 7)*sin(-pi/2+i*pi/6)) for i in range(12)])
add('three-lobe','three-lobe','3葉形',[(16+(10+2*cos(3*t))*cos(t),16+(10+2*cos(3*t))*sin(t)) for t in [i*2*pi/48 for i in range(48)]])
add('four-lobe','four-lobe','4葉形',[(16+(10+2*cos(4*t))*cos(t),16+(10+2*cos(4*t))*sin(t)) for t in [i*2*pi/48 for i in range(48)]])
add('kidney','kidney-shaped','腎臓形',[(5,8),(15,4),(26,8),(28,18),(22,28),(13,27),(15,18),(7,17)],'M5 8 C14 0 28 6 28 16 C28 29 12 32 12 24 C12 19 18 19 13 16 C8 14 2 16 5 8Z')
add('airfoil','airfoil','翼型',[(4,16),(8,9),(16,10),(28,16),(17,20),(8,22)],'M4 16 C4 5 16 8 28 16 C14 18 4 28 4 16Z')
add('chevron','chevron','山形',[(4,12),(16,4),(28,12),(28,26),(16,18),(4,26)])
add('fork','forked','フォーク形',[(5,4),(12,4),(12,13),(20,13),(20,4),(27,4),(27,20),(20,20),(20,28),(12,28),(12,20),(5,20)])
add('rack','rack-tooth','ラック歯形',[(4,10),(7,10),(7,5),(11,5),(11,10),(15,10),(15,5),(19,5),(19,10),(23,10),(23,5),(27,5),(27,27),(4,27)])
add('arrow','arrowhead','矢じり形',[(4,11),(18,11),(18,4),(29,16),(18,28),(18,21),(4,21)])
add('annulus','annular','環状',regular(32),'M16 4 A12 12 0 1 1 16 28 A12 12 0 1 1 16 4Z M16 10 A6 6 0 1 0 16 22 A6 6 0 1 0 16 10Z',True)
add('square-tube','square hollow','角形中空',[(4,4),(28,4),(28,28),(4,28)],'M5 5 H27 V27 H5Z M11 11 V21 H21 V11Z',True)
add('rectangular-tube','rectangular hollow','矩形中空',[(4,8),(28,8),(28,24),(4,24)],'M4 8 H28 V24 H4Z M9 13 V19 H23 V13Z',True)
add('hexagonal-tube','hexagonal hollow','六角中空',regular(6,12),polygon(regular(6,12))+polygon(list(reversed(regular(6,6)))),True)
add('slotted-plate','slotted plate','長穴付き板',[(4,5),(28,5),(28,27),(4,27)],'M4 5 H28 V27 H4Z M11 12 A4 4 0 1 0 11 20 H21 A4 4 0 1 0 21 12Z',True)
add('two-hole-plate','two-hole plate','2穴付き板',[(4,6),(28,6),(28,26),(4,26)],'M4 6 H28 V26 H4Z M10 12 A4 4 0 1 0 10 20 A4 4 0 1 0 10 12Z M22 12 A4 4 0 1 0 22 20 A4 4 0 1 0 22 12Z',True)
add('flange','flange','フランジ',regular(8,12),polygon(regular(8,12))+' M16 11 A5 5 0 1 0 16 21 A5 5 0 1 0 16 11Z',True)
add('annular-sector','annular sector','円弧帯',[(4,25),(8,10),(16,4),(25,5),(28,10),(20,11),(15,16),(12,25)],'M4 26 A22 22 0 0 1 28 4 L26 12 A14 14 0 0 0 12 26Z')
assert len(PROFILES)==56,len(PROFILES)
