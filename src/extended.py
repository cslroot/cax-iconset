"""Contextual engineering symbols, with explicit compatible recipe families.

This module does not manufacture new software commands. A context icon denotes
an operation applied to a named boundary, face, or trajectory. The operation is
integrated into the drawing (meshing, paths, sections, probes), not a generic
status badge. See docs/REFERENCE.md for scope and limitations.
"""
from math import sin,cos,pi
from core import p,r,c,g,fill,accent,nodes,PALE,TEAL,INK,AMBER
from profiles import PROFILES,polygon,rounded
from sources import SOURCE_IDS as SOURCES

def outline(q, **attrs):return p(q['d'],fill_rule='evenodd',**attrs)
def solid(q):return outline(q,fill=PALE)
def reduced(q,scale=.72,dx=0,dy=0):return g(solid(q),transform=f'translate({16*(1-scale)+dx:.3f} {16*(1-scale)+dy:.3f}) scale({scale})')
def clipped(q,id,content):
 return '<defs><clipPath id="clip-'+id+'">'+p(q['d'],clip_rule='evenodd')+'</clipPath></defs>'+g(content,clip_path='url(#clip-'+id+')')
def field(q,id,content,edge=True):
 return solid(q)+clipped(q,id,content)+(outline(q) if edge else '')
def arrow(x,y,dx,dy,color=TEAL):
 a=(x+dx,y+dy);l=(dx*dx+dy*dy)**.5
 if l==0:return ''
 ux,uy=dx/l,dy/l
 return p(f'M{x:.3f} {y:.3f} l{dx:.3f} {dy:.3f} M{a[0]-ux*2-uy*1.7:.3f} {a[1]-uy*2+ux*1.7:.3f} L{a[0]:.3f} {a[1]:.3f} L{a[0]-ux*2+uy*1.7:.3f} {a[1]-uy*2-ux*1.7:.3f}',stroke=color,stroke_width=1.4)
def spokes(n=8,inner=3,outer=11):
 return ''.join(p(f'M{16+inner*cos(t):.2f} {16+inner*sin(t):.2f} L{16+outer*cos(t):.2f} {16+outer*sin(t):.2f}',stroke=TEAL,stroke_width=1.2) for t in [i*2*pi/n for i in range(n)])
def stripes(step=5,diagonal=False,color=TEAL):
 return ''.join(p(f'M{-10 if diagonal else 2} {y} H40' if not diagonal else f'M-10 {y} L40 {y-25}',stroke=color,stroke_width=1.2) for y in range(-5,58,step))
def zigzag():return accent('M3 7 H29 V12 H3 V17 H29 V22 H3 V27 H29',stroke_width=1.3)
def spiral():
 pts=[(16+(1+t/(7*pi)*12)*cos(t),16+(1+t/(7*pi)*12)*sin(t)) for t in [i*7*pi/100 for i in range(101)]]
 return p(polygon(pts)[:-2],stroke=TEAL,stroke_width=1.2)
def dots(points,rad=1.3):return ''.join(c(x,y,rad,fill=TEAL,stroke='none') for x,y in points)
def centroid(q):
 pts=q['points'];area=xsum=ysum=0
 for a,b in zip(pts,pts[1:]+pts[:1]):
  cross=a[0]*b[1]-b[0]*a[1];area+=cross;xsum+=(a[0]+b[0])*cross;ysum+=(a[1]+b[1])*cross
 return (xsum/(3*area),ysum/(3*area)) if abs(area)>1e-8 else (16,16)

def perimeter_points(q,n=7):
 pts=q['points'];return [pts[int(i*len(pts)/n)%len(pts)] for i in range(n)]

CAD=[
 ('profile','sketch profile','スケッチ輪郭'),('extrusion','extruded section','断面押し出し'),('pocket','pocket cut','ポケット切削'),('through-cut','through cut','貫通カット'),
 ('thin-wall','thin-wall extrusion','薄肉押し出し'),('loft','lofted transition','ロフト遷移'),('sweep','swept section','断面スイープ'),('fillet','rounded profile corners','輪郭フィレット'),
 ('chamfer','chamfered profile corners','輪郭面取り'),('linear-pattern','linear pattern','直線配列'),('circular-pattern','circular pattern','円形配列'),('mirror','mirrored profile','輪郭ミラー'),
 ('offset-out','outward offset','外側オフセット'),('offset-in','inward offset','内側オフセット'),('projection','projected profile','輪郭投影'),('section','section view','断面表示'),
 ('dimension','overall width dimension','全幅寸法'),('construction','construction profile','補助輪郭'),('region','planar region','平面領域'),('centroid','profile centroid','断面図心')]
CAM=[
 ('outside-contour','outside contour milling','外周輪郭加工'),('inside-contour','inside contour milling','内周輪郭加工'),('offset-pocket','offset pocket clearing','等高オフセット加工'),('zigzag-pocket','zigzag pocket clearing','ジグザグ加工'),
 ('oneway-raster','one-way raster milling','一方向走査加工'),('crosshatch','crosshatch finishing','交差走査仕上げ'),('radial','radial finishing','放射状仕上げ'),('spiral','spiral clearing','渦巻き荒取り'),
 ('trochoidal','trochoidal path','トロコイド軌跡'),('helical-entry','helical entry','ヘリカル進入'),('tangential-in','tangential lead-in','接線進入'),('tangential-out','tangential lead-out','接線退出'),
 ('ramp-entry','ramp entry','傾斜進入'),('boundary-drill','boundary hole pattern','輪郭上の穴パターン'),('tabs','tabbed profile cutting','タブ付き輪郭切断'),('rest-corners','corner rest machining','隅部の残り加工'),
 ('avoidance','avoidance boundary','回避境界'),('finish-pass','finishing allowance pass','仕上げ代加工'),('plunge','plunge roughing','プランジ荒取り'),('stepover','stepover verification','ピックフィード確認')]
CAE=[
 ('tri-mesh','triangular surface mesh','三角形面メッシュ'),('quad-dominant','quad-dominant surface mesh','四角形主体面メッシュ'),('local-refinement','locally refined mesh','局所細分化メッシュ'),('temperature','prescribed temperature','温度境界'),
 ('heat-flux','heat-flux boundary','熱流束境界'),('convection','convective boundary','対流境界'),('radiation','radiative boundary','放射境界'),('pressure','normal pressure','法線圧力'),
 ('traction','surface traction','表面トラクション'),('point-force','point force','点荷重'),('body-force','body force','物体力'),('moment','remote moment','リモートモーメント'),
 ('fixed','fixed boundary','固定境界'),('symmetry','symmetry boundary','対称境界'),('displacement','prescribed displacement','変位境界'),('stress','stress field','応力場'),
 ('strain','strain field','ひずみ場'),('thermal-field','temperature field','温度場'),('velocity','velocity field','速度場'),('diffusion','diffusion field','拡散場')]
CMM=[
 ('perimeter-scan','perimeter scan','輪郭スキャン'),('discrete-probe','discrete point probing','離散点測定'),('raster-scan','raster surface scan','面ラスタースキャン'),('spiral-scan','spiral surface scan','面渦巻きスキャン'),
 ('radial-sample','radial sampling','放射状サンプリング'),('laser-line','laser-line scan','レーザー線スキャン'),('structured-light','structured-light measurement','構造化光測定'),('vision-edge','vision edge detection','画像エッジ検出'),
 ('nominal-fit','nominal profile fit','公称輪郭フィット'),('deviation','profile deviation','輪郭偏差'),('profile-tolerance','profile tolerance evaluation','輪郭度評価'),('flatness','face flatness evaluation','面平面度評価'),
 ('parallelism','face parallelism evaluation','面平行度評価'),('perpendicularity','face perpendicularity evaluation','面直角度評価'),('angularity','face angularity evaluation','面傾斜度評価'),('datum','datum face establishment','基準面設定'),
 ('width','overall width measurement','全幅測定'),('perimeter-length','perimeter length measurement','周長測定'),('area','surface area measurement','表面積測定'),('centroid','measured centroid','測定図心')]

def cad(q,op,id):
 if op=='profile':return outline(q)+nodes(perimeter_points(q,4))
 if op=='extrusion':
  body=g(solid(q),transform='translate(0 4) scale(1 .8)')
  body+=''.join(p(f'M{x:.2f} {y*.8+4:.2f} V{y*.8-1:.2f}') for x,y in perimeter_points(q,4))
  return body+g(solid(q),transform='translate(0 -1) scale(1 .8)')
 if op=='pocket':return r(3,3,26,26,3,fill=PALE)+reduced(q,.72,0,2)+g(outline(q,stroke=TEAL),transform='translate(4.48 2.48) scale(.72)')
 if op=='through-cut':return r(3,4,26,23,2,fill=PALE)+g(outline(q,fill='white'),transform='translate(4.48 4.48) scale(.72)')+arrow(16,1,0,6)+arrow(16,26,0,5)
 if op=='thin-wall':return solid(q)+g(outline(q,fill='white'),transform='translate(3.2 3.2) scale(.8)')
 if op=='loft':
  return g(outline(q,fill=PALE),transform='translate(0 16) scale(1 .45)')+p('M7 23 12 6 M25 23 20 6')+g(outline(q,fill='white'),transform='translate(8 0) scale(.5 .45)')
 if op=='sweep':return fill('M5 23 Q5 6 25 6 L27 12 Q12 11 12 27Z')+g(outline(q,fill='white'),transform='translate(2 18) scale(.36)')+accent('M9 20 Q10 10 23 10')
 if op=='fillet':return p(rounded(q['points'],.33),fill=PALE)+g(outline(q,stroke=TEAL,stroke_dasharray='1 3'),opacity='.6')
 if op=='chamfer':
  pts=[]
  for i,b in enumerate(q['points']):
   a=q['points'][i-1];z=q['points'][(i+1)%len(q['points'])]
   pts.extend([(b[0]+(a[0]-b[0])*.2,b[1]+(a[1]-b[1])*.2),(b[0]+(z[0]-b[0])*.2,b[1]+(z[1]-b[1])*.2)])
  return p(polygon(pts),fill=PALE)+g(outline(q,stroke=TEAL,stroke_dasharray='1 4'),opacity='.5')
 if op=='linear-pattern':return ''.join(g(solid(q),transform=f'translate({x} 10) scale(.36)') for x in [-1,10,21])+arrow(5,5,22,0)
 if op=='circular-pattern':return c(16,16,9,stroke_dasharray='1 3')+''.join(g(solid(q),transform=f'translate({x-5} {y-5}) scale(.32)') for x,y in [(16,6),(6,21),(26,21)])
 if op=='mirror':return p('M16 2 V30',stroke=TEAL,stroke_dasharray='2 3')+g(solid(q),transform='translate(0 9) scale(.42)')+g(solid(q),transform='translate(32 9) scale(-.42 .42)')
 if op=='offset-out':return outline(q,stroke=TEAL,stroke_dasharray='3 2')+reduced(q,.65)+arrow(23,16,6,0)
 if op=='offset-in':return solid(q)+g(outline(q,stroke=TEAL,stroke_dasharray='3 2'),transform='translate(5.6 5.6) scale(.65)')+arrow(27,16,-6,0)
 if op=='projection':return g(outline(q,stroke=TEAL,stroke_dasharray='2 2'),transform='translate(0 14) scale(1 .5)')+g(solid(q),transform='translate(0 -1) scale(1 .5)')+p('M6 10 V24 M26 10 V24',stroke_dasharray='2 3')
 if op=='section':return field(q,id,stripes(5,True))+p('M2 16 H30',stroke=TEAL,stroke_dasharray='6 2 1 2')
 if op=='dimension':return reduced(q,.8,0,2)+p('M5 2 V8 M27 2 V8 M5 5 H27 M8 3 5 5 8 7 M24 3 27 5 24 7',stroke=TEAL,stroke_width=1.4)
 if op=='construction':return outline(q,stroke_dasharray='5 2 1 2')+p('M3 16 H29 M16 3 V29',stroke=TEAL,stroke_dasharray='2 3')
 if op=='region':return field(q,id,dots([(x,y) for x in [8,13,18,23] for y in [8,13,18,23]],.8))
 if op=='centroid':
  x,y=centroid(q)
  return solid(q)+c(round(x,3),round(y,3),3.5,stroke=TEAL)+p(f'M{x:.3f} {y-6:.3f} V{y+6:.3f} M{x-6:.3f} {y:.3f} H{x+6:.3f}',stroke=TEAL)
 raise ValueError(op)

def cam(q,op,id):
 if op=='outside-contour':return reduced(q,.7)+outline(q,stroke=TEAL)+arrow(24,6,4,3)
 if op=='inside-contour':return solid(q)+g(outline(q,stroke=TEAL),transform='translate(4.8 4.8) scale(.7)')+arrow(20,11,2,3)
 if op=='offset-pocket':return solid(q)+''.join(g(outline(q,stroke=TEAL,stroke_width=1.2/s),transform=f'translate({16*(1-s)} {16*(1-s)}) scale({s})') for s in [.78,.48,.2])
 if op=='zigzag-pocket':return field(q,id,zigzag())
 if op=='oneway-raster':return field(q,id,''.join(arrow(5,y,22,0) for y in [8,14,20,26])+p('M27 8 5 14 M27 14 5 20 M27 20 5 26',stroke=TEAL,stroke_dasharray='1 3',stroke_width=1))
 if op=='crosshatch':return field(q,id,stripes(6,True)+g(stripes(6,True),transform='rotate(90 16 16)'))
 if op=='radial':return field(q,id,spokes(10))
 if op=='spiral':return field(q,id,spiral())
 if op=='trochoidal':return field(q,id,accent('M3 22 C0 5 14 5 10 18 C7 30 6 8 17 9 C26 9 16 30 17 18 C18 4 31 4 29 23',stroke_width=1.25))
 if op=='helical-entry':return solid(q)+accent('M12 10 C25 6 25 15 12 15 C3 15 6 9 15 11 M12 15 C25 11 25 20 12 20 C3 20 6 14 15 16 M12 20 C25 16 25 25 12 25',stroke_width=1.2)+arrow(16,2,0,7)
 if op=='tangential-in':return reduced(q,.77)+g(outline(q,stroke=TEAL),transform='translate(2.6 2.6) scale(.85)')+accent('M2 4 Q12 3 6 16')+arrow(6,12,0,4)
 if op=='tangential-out':return reduced(q,.77)+g(outline(q,stroke=TEAL),transform='translate(2.6 2.6) scale(.85)')+accent('M26 16 Q20 29 30 28')+arrow(26,28,4,0)
 if op=='ramp-entry':return field(q,id,p('M5 11 11 15 17 19 27 23',stroke=TEAL)+p('M5 11 V25 M27 23 V25',stroke_dasharray='2 2'))+arrow(5,3,0,7)
 if op=='boundary-drill':return solid(q)+''.join(c(x,y,1.9,fill='white',stroke=TEAL) for x,y in perimeter_points(q,7))
 if op=='tabs':return outline(q,stroke=TEAL)+''.join(r(x-2,y-1,4,2,0,fill=PALE) for x,y in perimeter_points(q,4))
 if op=='rest-corners':return solid(q)+g(outline(q,stroke=TEAL,stroke_width=3,stroke_dasharray='3 12'),opacity='.9')+g(outline(q),transform='translate(5.6 5.6) scale(.65)')
 if op=='avoidance':return outline(q,stroke=AMBER,stroke_dasharray='3 2')+accent('M2 29 Q16 17 30 29 M2 3 Q16 15 30 3')
 if op=='finish-pass':return outline(q)+g(outline(q,stroke=TEAL,stroke_width=1.3),transform='translate(1.28 1.28) scale(.92)')+arrow(8,28,16,0)
 if op=='plunge':return field(q,id,''.join(c(x,y,2.6,stroke=TEAL,stroke_width=1.1) for x in [7,13,19,25] for y in [8,14,20,26]))+arrow(16,1,0,6)
 if op=='stepover':return field(q,id,stripes(7))+p('M3 9 V16 M1 11 3 9 5 11 M1 14 3 16 5 14',stroke=TEAL,stroke_width=1.2)
 raise ValueError(op)

def cae(q,op,id):
 if op in ['tri-mesh','quad-dominant','local-refinement']:
  content=stripes(6)+g(stripes(6),transform='rotate(90 16 16)')
  if op=='tri-mesh':content+=stripes(6,True)
  if op=='local-refinement':content+=p('M16 10 H29 M16 16 H29 M16 22 H29 M16 28 H29 M16 4 V28 M22 4 V28 M28 4 V28',stroke=TEAL,stroke_width=.8)
  return field(q,id,content)
 if op=='temperature':return reduced(q,.8,-2,1)+r(22,4,4,18,2,fill='white')+c(24,24,4,fill=PALE)+p('M24 9 V24',stroke=TEAL,stroke_width=2)
 if op=='heat-flux':return field(q,id,''.join(arrow(x,4,0,24) for x in [7,16,25]))
 if op=='convection':return field(q,id,accent('M3 8 Q10 3 17 8 T31 8 M3 16 Q10 11 17 16 T31 16 M3 24 Q10 19 17 24 T31 24',stroke_width=1.4))+arrow(5,29,22,0)
 if op=='radiation':return field(q,id,spokes(12,2,14))+c(16,16,3,fill='white',stroke=TEAL)
 if op=='pressure':return reduced(q,.8)+''.join(arrow(x,1,0,7) for x in [7,16,25])+''.join(arrow(x,31,0,-7) for x in [7,16,25])
 if op=='traction':return solid(q)+''.join(arrow(9,y,16,0) for y in [8,16,24])
 if op=='point-force':return reduced(q,.8,0,2)+arrow(16,2,0,16)+c(16,18,1.8,fill=TEAL)
 if op=='body-force':return field(q,id,''.join(arrow(x,y,0,5) for x in [7,16,25] for y in [6,14,22]))
 if op=='moment':return reduced(q,.75)+accent('M5 21 A13 13 0 0 1 27 8 M22 7 27 8 27 3')+p('M16 11 V24',stroke_dasharray='2 2')
 if op=='fixed':return solid(q)+''.join(p(f'M{x:.2f} {y:.2f} l-3 {min(3,30-y):.2f}') for x,y in perimeter_points(q,8))+dots(perimeter_points(q,8),1)
 if op=='symmetry':return solid(q)+p('M16 1 V31',stroke=TEAL,stroke_dasharray='5 2 1 2')+p('M11 13 V19 M9 13 V19 M21 13 V19 M23 13 V19',stroke=TEAL,stroke_width=1.2)
 if op=='displacement':return g(outline(q,stroke_dasharray='2 2'),transform='translate(-2 0) scale(.85)')+g(outline(q,stroke=TEAL),transform='translate(6 4.8) scale(.7)')+arrow(7,4,15,0)
 if op=='stress':return field(q,id,''.join(c(7,16,t,stroke=TEAL,stroke_width=1.3) for t in [3,7,12,18,24]))
 if op=='strain':return field(q,id,accent('M3 6 Q13 14 29 6 M3 15 Q13 23 29 15 M3 24 Q13 32 29 24 M8 2 Q16 15 8 30 M18 2 Q26 15 18 30',stroke_width=1.2))
 if op=='thermal-field':return field(q,id,''.join(p(f'M2 {y} Q16 {y-8} 30 {y}',stroke=TEAL,stroke_width=1.2) for y in [6,12,18,24,30]))
 if op=='velocity':return field(q,id,''.join(arrow(x,y,6,(-1 if x==16 else 1)*2) for x in [5,16,24] for y in [8,16,24]))
 if op=='diffusion':return field(q,id,dots([(5+i*2,5+j*3) for i in range(11) for j in range(8) if (i+j)%(1+i//3)==0],.65))
 raise ValueError(op)

def cmm(q,op,id):
 if op=='perimeter-scan':return outline(q)+g(outline(q,stroke=TEAL,stroke_dasharray='1 3'),transform='translate(-1.6 -1.6) scale(1.1)')
 if op=='discrete-probe':return solid(q)+nodes(perimeter_points(q,7))+p('M28 2 V11 L23 15')+c(23,15,1.8,fill=TEAL)
 if op=='raster-scan':return field(q,id,zigzag())+dots([(8,7),(18,12),(11,17),(23,22)])
 if op=='spiral-scan':return field(q,id,spiral())+c(16,16,2,fill=TEAL)
 if op=='radial-sample':return field(q,id,spokes(6)+dots([(16+8*cos(i*pi/3),16+8*sin(i*pi/3)) for i in range(6)]))
 if op=='laser-line':return reduced(q,.85,0,2)+p('M7 5 H25',stroke=TEAL,stroke_width=2.5)+p('M11 5 5 25 M21 5 27 25',stroke=TEAL)+r(11,1,10,4,1,fill=PALE)
 if op=='structured-light':return field(q,id,stripes(4,True))+p('M3 3 H9 V7 M23 3 H29 V7 M3 25 V29 H9 M23 29 H29 V25',stroke=TEAL)
 if op=='vision-edge':return outline(q,stroke=TEAL,stroke_width=2)+p('M3 9 V3 H9 M23 3 H29 V9 M29 23 V29 H23 M9 29 H3 V23')
 if op=='nominal-fit':return outline(q)+g(outline(q,stroke=TEAL,stroke_dasharray='1 3'),transform='translate(1.6 -.8) scale(.95)')+arrow(9,26,9,-5)
 if op=='deviation':return outline(q)+g(outline(q,stroke=TEAL),transform='translate(3 1) scale(.82 .95)')+p('M6 16 H10 M22 16 H27 M16 5 V9 M16 24 V28',stroke=TEAL)
 if op=='profile-tolerance':return outline(q)+g(outline(q,stroke=TEAL,stroke_dasharray='2 2'),transform='translate(2.08 2.08) scale(.87)')+g(outline(q,stroke=TEAL,stroke_dasharray='2 2'),transform='translate(-1.6 -1.6) scale(1.1)')
 if op=='flatness':return g(solid(q),transform='translate(0 10) scale(1 .6)')+p('M4 8 H28 M4 28 H28',stroke=TEAL)+nodes([(10,16),(17,21),(23,17)])
 if op=='parallelism':return g(solid(q),transform='translate(0 9) scale(1 .6)')+p('M3 5 H29 M3 28 H29 M11 3 15 7 M18 3 22 7',stroke=TEAL)
 if op=='perpendicularity':return reduced(q,.78,2,-1)+p('M3 3 V29 H29 M3 23 H9 V29',stroke=TEAL)
 if op=='angularity':return reduced(q,.74,2,-2)+p('M3 28 H29 M3 28 20 3 M10 28 A7 7 0 0 0 7 22',stroke=TEAL)
 if op=='datum':return reduced(q,.82,0,-1)+p('M16 27 V31 M11 31 H21')+p('M13 25 16 20 19 25Z',fill=TEAL,stroke=TEAL)
 if op=='width':return reduced(q,.78,0,-2)+p('M5 23 V30 M27 23 V30 M5 27 H27 M8 25 5 27 8 29 M24 25 27 27 24 29',stroke=TEAL,stroke_width=1.3)
 if op=='perimeter-length':return outline(q,stroke=TEAL,stroke_dasharray='3 2')+r(9,12,12,9,2,fill='white')+p('M21 17 H27 V21 H21 M13 13 V16 M17 13 V16 M24 18 V20',stroke=TEAL,stroke_width=1.3)
 if op=='area':return field(q,id,stripes(5)+g(stripes(5),transform='rotate(90 16 16)'))+r(12,12,8,8,1,fill='white')+p('M14 18 16 14 18 18 M15 17 H17',stroke=TEAL,stroke_width=1.2)
 if op=='centroid':return solid(q)+dots(perimeter_points(q,6))+p('M9 16 H23 M16 9 V23',stroke=TEAL)+c(16,16,2,fill='white',stroke=TEAL)
 raise ValueError(op)

# Robot trajectory families. These encode process motion, not robot controller
# interpolation modes. The paths remain fully visible and tools meet the path.
PATHS=[
 ('straight','straight','直線','M4 25 L25 7'),('arc','arc','円弧','M4 25 Q3 5 25 7'),('circle','circular','円周','M25 7 A11 11 0 1 0 26 8'),
 ('rectangular','rectangular perimeter','矩形周回','M25 7 H5 V27 H27 V7Z'),('rounded','rounded perimeter','角丸周回','M25 7 H10 Q5 7 5 12 V22 Q5 27 10 27 H22 Q27 27 27 22 V12 Q27 7 25 7'),
 ('zigzag','zigzag','ジグザグ','M4 27 11 18 4 15 17 10 12 4 25 7'),('spline','spline','スプライン','M4 25 C27 30 2 2 25 7'),
 ('sine','sinusoidal','波形','M4 24 C10 2 11 30 17 16 C22 2 21 15 25 7'),('spiral','spiral','渦巻き','M15 17 C4 8 29 8 20 24 C9 36 -2 4 25 7'),
 ('helix','helical','螺旋','M4 27 C0 19 27 19 23 27 C19 33 0 9 4 9 C15 1 30 20 23 20 C15 20 15 3 25 7'),
 ('figure-eight','figure-eight','8の字','M25 7 C5 -1 0 17 16 18 C29 19 27 32 8 27 C-2 24 22 12 25 7'),
 ('stepped','stepped','階段状','M4 27 H10 V20 H17 V14 H25 V7'),('serpentine','serpentine','蛇行','M4 27 H23 Q29 27 26 22 Q25 19 20 19 H8 Q2 19 5 14 Q6 11 11 11 H23 Q29 11 25 7'),
 ('radial','radial passes','放射パス','M4 27 16 17 7 7 M16 17 25 7 M16 17 28 21 M16 17 18 28'),
 ('approach-retract','approach / retract','接近・退避','M4 4 V25 H25 V7'),('point-array','point array','点配列','M5 7 H25 V17 H5 V27 H25')]
PROCESSES=[
 ('arc-weld','arc welding','アーク溶接'),('laser-weld','laser welding','レーザー溶接'),('spot-weld','spot welding','スポット溶接'),('sealant','sealing','シーリング'),
 ('adhesive','adhesive dispensing','接着剤塗布'),('paint','spray painting','塗装'),('powder-coat','powder coating','粉体塗装'),('polish','polishing','研磨'),
 ('grind','grinding','研削'),('deburr','deburring','バリ取り'),('mill','robot milling','ロボット切削'),('laser-cut','laser cutting','レーザー切断'),
 ('waterjet','waterjet cutting','ウォータージェット'),('plasma','plasma cutting','プラズマ切断'),('inspect','optical inspection','光学検査'),('touch-probe','touch probing','接触測定'),
 ('scan','surface scanning','面スキャン'),('flame','flame treatment','火炎処理'),('print','additive deposition','積層造形'),('tape','tape laying','テープ積層'),
 ('fibre','fibre placement','繊維配置'),('ultrasonic','ultrasonic welding','超音波溶接'),('screw','screwdriving sequence','ねじ締め順序'),('drill','drilling sequence','穴あけ順序')]

def robot(path,process):
 key,_,_,d=path
 op=process[0]
 body=p(d,stroke=TEAL,stroke_width=1.4)
 # The machine endpoint is at (25,7). Each distinct process has a pictorial tool
 # and physically relevant path marking; no generic label/status badges.
 tool=''
 if op=='arc-weld':tool=p('M21 2 25 7 M21 9 18 9 M25 11 V14 M28 9 30 10',stroke=INK)+c(25,7,1.5,fill=PALE)
 elif op=='laser-weld':tool=r(21,1,8,3,1,fill=PALE)+p('M25 4 V8 M20 10 22 8 M28 8 30 10',stroke=TEAL)
 elif op=='spot-weld':tool=p('M20 1 V5 L25 7 M30 14 H26 V10')+c(25,7,2,fill=TEAL)+dots([(6,23),(13,17),(20,11)])
 elif op=='sealant':tool=p('M20 1 H29 L25 7Z',fill=PALE)+p(d,stroke=TEAL,stroke_width=3,stroke_dasharray='1 3')
 elif op=='adhesive':tool=r(21,1,8,4,1,fill=PALE)+p('M23 5 25 8 27 5')+p(d,stroke=TEAL,stroke_width=3,stroke_dasharray='4 3')
 elif op=='paint':tool=p('M20 1 H29 V5 H20Z M25 5 20 12 M25 5 29 12',fill=PALE)+p(d,stroke=TEAL,stroke_width=4,opacity='.25')
 elif op=='powder-coat':tool=p('M20 1 H29 V5 H20Z M25 5 V8',fill=PALE)+dots([(20,10),(25,11),(29,10),(22,14),(28,14)],.8)
 elif op=='polish':tool=c(25,7,5,fill=PALE)+c(25,7,2,stroke=TEAL)+p('M23 2 V1')
 elif op=='grind':tool=c(25,7,5,fill=PALE)+p('M21 4 29 10 M22 10 28 4 M19 12 17 15',stroke=TEAL)
 elif op=='deburr':tool=p('M25 1 V8 M22 6 25 10 28 6')+p(d,stroke=TEAL,stroke_dasharray='1 2',stroke_width=2.5)
 elif op=='mill':tool=r(22,1,6,9,1,fill=PALE)+p('M22 4 28 7 M22 8 26 10')
 elif op=='laser-cut':tool=p('M20 1 H30 L27 5 H23Z',fill=PALE)+p('M25 5 V11',stroke=TEAL)+p('M18 10 21 10 M29 11 31 13',stroke=TEAL)
 elif op=='waterjet':tool=p('M22 1 H28 V5 L25 7Z',fill=PALE)+p('M25 7 V13 M21 15 25 13 29 15',stroke=TEAL)
 elif op=='plasma':tool=p('M22 1 H28 V5 H22Z',fill=PALE)+p('M25 5 22 9 H27 L24 14',stroke=TEAL)
 elif op=='inspect':tool=r(20,1,10,8,2,fill=PALE)+c(25,5,2)+p('M22 11 25 14 28 11',stroke=TEAL)
 elif op=='touch-probe':tool=r(22,1,6,4,1,fill=PALE)+p('M25 5 V10')+c(25,11,2,fill=TEAL)
 elif op=='scan':tool=r(21,1,8,4,1,fill=PALE)+p('M25 5 20 13 M25 5 30 13 M20 13 H30',stroke=TEAL)
 elif op=='flame':tool=p('M25 1 C21 5 29 5 25 11 C17 8 20 4 25 1Z',fill=PALE)+p('M25 11 V14',stroke=TEAL)
 elif op=='print':tool=p('M21 1 H29 V5 L25 9 21 5Z',fill=PALE)+p(d,stroke=TEAL,stroke_width=2.4)+p('M20 13 H30',stroke=TEAL)
 elif op=='tape':tool=c(25,5,4,fill=PALE)+c(25,5,1)+p('M25 9 V13 H18',stroke=TEAL,stroke_width=3)
 elif op=='fibre':tool=p('M21 1 H29 V6 H21Z M22 6 V12 M25 6 V12 M28 6 V12',stroke=TEAL)+p(d,stroke=TEAL,stroke_width=2,stroke_dasharray='8 2')
 elif op=='ultrasonic':tool=p('M22 1 H28 V8 H22Z',fill=PALE)+p('M19 4 Q16 7 19 10 M29 4 Q32 7 29 10',stroke=TEAL)
 elif op=='screw':tool=p('M22 1 H28 M25 1 V11 M22 5 H28 M22 8 H28')+nodes([(5,25),(14,17)])
 elif op=='drill':tool=p('M22 1 H28 V8 L25 12 22 8Z M22 4 28 7',fill=PALE)+''.join(c(x,y,2,stroke=TEAL) for x,y in [(5,25),(14,17)])
 return body+tool


def extend():
 for domain,recipes,draw in [('CAD',CAD,cad),('CAM',CAM,cam),('CAE',CAE,cae),('CMM',CMM,cmm)]:
  for q in PROFILES:
   for op,en,ja in recipes:
    # Hollow boundaries already have inner walls. A generic inset of a hollow
    # profile would not represent a valid thin-wall feature, so omit it.
    if domain=='CAD' and q['holes'] and op in ['thin-wall','fillet','chamfer']:continue
    if domain=='CMM' and op=='centroid':continue
    # Corner treatments require explicit polygonal corners. Curved outlines
    # have no discrete polygonal corners; do not approximate them into fake ones.
    if domain=='CAD' and op in ['fillet','chamfer'] and q['id'] in ['circle','ellipse','capsule','round-end-slot','semicircle','quarter-circle','arch','teardrop','keyhole','keyway','double-d','three-lobe','four-lobe','kidney','airfoil','annulus','annular-sector','slotted-plate','two-hole-plate','flange']:continue
    shared=domain=='CAD' and op=='centroid'
    category='Common' if shared else domain
    id=f'{category.lower()}-{op}-{q["id"]}'
    entity='face' if domain in ['CAE','CMM'] else 'profile'
    yield dict(id=id,name=f'{q["en"].capitalize()} · {en}',nameJa=f'{q["ja"]}・{ja}',category=category,categories=['Common','CAD','CMM'] if shared else [domain],kind='variant',family=op,context=q['id'],file='icons/'+id+'.svg',body=draw(q,op,id),tags=[domain,q['en'],q['ja'],en,ja,entity,'context variant'],sources=SOURCES[domain],description=f'{en.capitalize()} applied to a {q["en"]} {entity}. This is an original context-specific symbol, not a separate vendor command.')
 for path in PATHS:
  for process in PROCESSES:
   # Contact sequences are point-to-point tasks, not continuous curves.
   if process[0] in ['spot-weld','touch-probe','screw','drill'] and path[0] not in ['straight','rectangular','zigzag','stepped','point-array']:continue
   # Fibre and tape laying use continuous paths; branch paths are inapplicable.
   if process[0] in ['tape','fibre'] and path[0] in ['radial','point-array','approach-retract']:continue
   id=f'olp-{process[0]}-{path[0]}'
   yield dict(id=id,name=f'{process[1].capitalize()} · {path[1]}',nameJa=f'{process[2]}・{path[2]}',category='OLP',kind='variant',family=process[0],context=path[0],file='icons/'+id+'.svg',body=robot(path,process),tags=['robot','OLP',path[1],path[2],process[1],process[2],'process trajectory'],sources=SOURCES['OLP'],description=f'{process[1].capitalize()} following a {path[1]} process trajectory. Schematic process notation; not a safe or executable robot program.')
