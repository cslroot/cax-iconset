"""Source-reviewed independent commands and persistent model-tree objects.

Records are selected individually. Neither variants nor state × object products
are generated. Geometry is original, not adapted from vendor artwork.
"""
from core import p, r, c, g, accent, fill, cube, nodes, record, PALE, TEAL
EXTENSION = {}

def add(domain, id, en, ja, family, desc, desc_ja, body, tags, source, role='command'):
    item = record(id, en, ja, body, tags)
    item.update(family=family, description=desc, descriptionJa=desc_ja, sources=source.split(','), role=role)
    item['tags'] = list(dict.fromkeys(item['tags'] + [en.lower(), ja, domain.lower()]))
    EXTENSION.setdefault(domain, []).append(item)

# Shape-changing features. Each has different parameters and modeling effects.
add('CAD','hole','Hole feature','穴フィーチャ','solid-feature',
    'Create a parameterized hole with a diameter, depth and optional stepped termination.',
    '径、深さ、段付き形状などを指定する穴フィーチャを作成します。',
    fill('M4 10 16 4 28 10 V24 L16 29 4 24Z')+p('M4 10 16 16 28 10 M16 16 V29')+p('M11 9 C11 5 21 5 21 9 C21 13 11 13 11 9Z',fill='white')+accent('M13 12 V20 H19 V12'),
    'hole,feature,diameter,depth,穴,径,深さ','solidworks-features-2026,freecad-partdesign-commands')
add('CAD','thread','Thread feature','ねじフィーチャ','solid-feature',
    'Apply a helical thread definition to a cylindrical face.',
    '円筒面にピッチを持つねじ形状を定義します。',
    fill('M9 7 C9 2 23 2 23 7 V25 C23 30 9 30 9 25Z')+p('M9 7 C9 12 23 12 23 7')+accent('M9 15 23 10 M9 21 23 16 M9 27 23 22'),
    'thread,helix,pitch,screw,ねじ,ピッチ,円筒','solidworks-features-2026')
add('CAD','draft','Draft angle','抜き勾配','solid-feature',
    'Tilt selected faces about a neutral reference to provide a draft angle.',
    '中立基準を保ちながら選択面を傾けて抜き勾配を付けます。',
    fill('M5 27 11 6 H21 L27 27Z')+p('M11 6 V27 M21 6 V27',stroke_dasharray='2 3')+accent('M14 21 Q18 17 24 18 M18 15 18 18 21 19'),
    'draft,taper,angle,mold,抜き勾配,傾斜,金型','solidworks-features-2026,freecad-partdesign-commands')
add('CAD','rib','Rib','リブ','solid-feature',
    'Add a thin reinforcing wall between supporting faces.',
    '支持面の間に薄い補強壁を追加します。',
    fill('M5 4 H10 V23 H28 V28 H5Z')+p('M10 23 25 23 10 8Z',fill=PALE,stroke=TEAL)+p('M13 23 V14 L23 23'),
    'rib,reinforcement,wall,リブ,補強,薄壁','solidworks-features-2026')
add('CAD','split-body','Split body','ボディ分割','solid-feature',
    'Divide a solid into separate bodies using a cutting plane or surface without discarding either side.',
    '切断面を使い、両側の材料を残したままソリッドを別々のボディに分割します。',
    fill('M3 10 10 6 14 8 V24 L10 27 3 23Z')+fill('M19 8 23 6 29 10 V23 L23 27 19 24Z')+p('M3 10 10 14 14 12 M10 14 V27 M19 12 23 14 29 10 M23 14 V27')+accent('M16 3 V29',stroke_dasharray='3 3'),
    'split,body,cutting plane,分割,ボディ,切断面','onshape-split')
add('CAD','surface-thicken','Thicken surface','サーフェス厚み付け','surface',
    'Turn an open surface into a solid by adding a specified thickness.',
    '開いたサーフェスに指定厚みを付けてソリッドにします。',
    fill('M4 12 Q15 3 28 11 V19 Q15 11 4 20Z')+p('M4 20 V25 Q15 16 28 24 V19')+accent('M8 17 V23 M6 19 8 17 10 19 M6 21 8 23 10 21'),
    'surface,thicken,thickness,solid,厚み付け,肉厚,面','onshape-thicken')
add('CAD','surface-offset','Offset surface','サーフェスオフセット','surface',
    'Create a surface at a normal distance from an existing surface without adding solid thickness.',
    'ソリッドの厚みを作らず、既存面から法線方向に離れたサーフェスを作成します。',
    fill('M4 20 Q15 12 28 20 L24 28 Q14 21 4 27Z')+p('M4 7 Q15 0 28 7 L24 14 Q14 8 4 14Z')+accent('M16 22 V10 M12 14 16 10 20 14'),
    'surface,offset,normal,distance,面,オフセット,法線','onshape-offset-surface')
add('CAD','sketch-project','Project geometry','ジオメトリ投影','sketch-edit',
    'Reference external edges or curves by projecting them onto the active sketch plane.',
    '外部のエッジや曲線をスケッチ平面に投影して参照します。',
    fill('M3 22 12 16 29 22 20 29Z')+p('M7 5 H23 V11 H7Z M7 11 V22 M23 11 V22',stroke_dasharray='2 3')+accent('M7 22 H23 M15 10 V18 M12 15 15 18 18 15'),
    'sketch,project,use,reference,投影,外部参照,スケッチ','onshape-project')
add('CAD','constraint-horizontal-vertical','Horizontal/vertical constraint','水平・垂直拘束','sketch-constraint',
    'Align a sketch line with the horizontal or vertical sketch axis.',
    'スケッチ線をスケッチ座標の水平または垂直方向に拘束します。',
    p('M5 4 V27 H28',stroke_dasharray='2 3')+accent('M10 11 H27 M19 17 V27')+nodes([(10,11),(27,11),(19,17),(19,27)]),
    'constraint,horizontal,vertical,axis,水平,垂直,拘束','fusion-sketch-constraints')
add('CAD','constraint-concentric','Concentric constraint','同心拘束','sketch-constraint',
    'Keep selected circular sketch entities centered on the same point.',
    '選択した円形スケッチ図形の中心を同じ点に保ちます。',
    c(16,16,11)+c(16,16,6,stroke=TEAL)+p('M16 2 V7 M16 25 V30 M2 16 H7 M25 16 H30')+c(16,16,1.2,fill=TEAL),
    'constraint,concentric,center,circle,同心,中心,円','fusion-sketch-constraints')
add('CAD','constraint-midpoint','Midpoint constraint','中点拘束','sketch-constraint',
    'Constrain a point to the midpoint of a sketch line segment.',
    '点をスケッチ線分の中点に拘束します。',
    p('M4 18 H28 M9 14 V22 M23 14 V22')+nodes([(4,18),(28,18)])+c(16,18,3,fill=PALE,stroke=TEAL)+accent('M16 4 V12 M12 8 16 12 20 8'),
    'constraint,midpoint,half,point,中点,半分,点','fusion-sketch-constraints')

# Drawing annotations are UI illustrations, not certified production symbols.
add('CAD','drawing-section-view','Section drawing view','図面断面ビュー','drawing-view',
    'Generate a linked drawing view from a cutting line through the model.',
    'モデルの切断線から関連付けられた図面断面ビューを生成します。',
    r(3,3,26,26,1)+p('M3 24 H29 M21 24 V29')+fill('M8 8 H23 V20 H17 V13 H8Z')+accent('M12 8 8 12 M18 8 14 12 M23 9 19 13 M23 15 18 20'),
    'drawing,section,cutting line,hatch,図面,断面,ハッチ','fusion-drawing')
add('CAD','geometric-tolerance','Feature control frame','幾何公差枠','drawing-annotation',
    'Add a feature control frame that specifies a geometric tolerance and its datum references.',
    '幾何公差と参照データムを指定する公差枠を追加します。',
    r(2,10,28,12,1)+p('M12 10 V22 M22 10 V22')+c(7,16,3)+accent('M7 12 V20 M3 16 H11')+p('M15 14 H19 M15 18 H17 M25 14 V18 H28'),
    'gdt,feature control frame,geometric tolerance,幾何公差,公差枠,データム','fusion-drawing')
add('CAD','datum-identifier','Datum identifier','データム記号','drawing-annotation',
    'Attach a datum identifier annotation to a drawing feature used as a tolerance reference.',
    '公差の基準とする図面形体にデータム識別の注記を付けます。',
    r(16,3,13,11,1)+p('M19 11 22.5 6 26 11 M20 9 H25 M16 8 H9 V22 M3 28 H23')+p('M5 27 9 21 13 27Z',fill=TEAL),
    'datum,identifier,annotation,reference,データム,基準,記号','fusion-drawing')
add('CAD','surface-texture','Surface texture annotation','表面性状注記','drawing-annotation',
    'Specify a surface finish requirement on a drawing with a texture annotation.',
    '表面性状の注記で図面に仕上げの要求を指定します。',
    p('M3 28 H29')+accent('M5 16 12 25 23 5 H29 M12 16 H27')+p('M24 21 H28 M24 25 H28'),
    'surface,texture,finish,roughness,表面性状,仕上げ,粗さ','fusion-drawing')
add('CAD','drawing-balloon','Balloon annotation','バルーン注記','drawing-annotation',
    'Label a drawing component with an item balloon linked to its bill-of-materials entry.',
    '部品表の項目に対応するバルーンで図面内の部品を識別します。',
    c(23,9,7,fill=PALE)+p('M21 7 23 5 V13 M20 13 H26')+accent('M18 14 8 25 H3 M8 20 V25 H13')+p('M3 29 H19'),
    'drawing,balloon,item,bom,図面,バルーン,部品番号','fusion-drawing')
add('CAD','mass-properties','Mass properties','質量特性','model-inspection',
    'Calculate model mass, center of mass and inertia from geometry and assigned density.',
    '形状と指定密度から質量、重心、慣性などを計算します。',
    p('M16 5 V28 M10 28 H22 M5 10 H27 M6 10 3 20 H10 L6 10 M26 10 22 20 H29Z')+c(16,7,4,fill=PALE,stroke=TEAL)+accent('M16 3 V11 M12 7 H20'),
    'mass,center of mass,inertia,density,質量,重心,慣性','onshape-mass-properties')
add('CAD','mesh-to-brep','Convert mesh to B-rep','メッシュをB-repへ変換','representation-conversion',
    'Convert a faceted mesh into a boundary-representation surface or solid model.',
    '三角形メッシュを境界表現のサーフェスまたはソリッドモデルに変換します。',
    p('M3 8 9 4 14 8 V23 L9 27 3 23Z M3 8 9 15 14 8 M3 23 9 15 14 23 M9 4 V27')+fill('M22 8 26 6 30 8 V23 L26 25 22 23Z')+p('M22 8 26 10 30 8 M26 10 V25')+accent('M14 17 H21 M18 14 21 17 18 20'),
    'mesh,brep,b-rep,convert,メッシュ,境界表現,変換','fusion-mesh-convert')

# Persistent objects: part definition, volume, assembly and sketch container
# are not interchangeable; repeated instances intentionally reuse the part glyph.
add('Common','folder','Folder','フォルダー','organization',
    'Represent a container that organizes related objects without implying a create action.',
    '関連オブジェクトをまとめる入れ物を表します。',
    fill('M3 8 Q3 6 5 6 H12 L15 10 H27 Q29 10 29 12 V27 H3Z')+p('M3 15 H29'),
    'folder,container,tree,フォルダー,入れ物,ツリー','fusion-manufacture-browser','object')
add('CAD','part','Part / component','部品・コンポーネント','model-object',
    'Represent a part definition containing geometry and features, or a placed instance using the same symbol.',
    '形状とフィーチャを持つ部品定義を表し、その配置インスタンスにも同じ図柄を使います。',
    fill('M4 10 12 6 20 10 V17 L27 20 V26 L18 30 4 23Z')+p('M4 10 12 14 20 10 M12 14 V21 L18 24 27 20 M18 24 V30')+accent('M22 4 H28 V10'),
    'part,component,instance,occurrence,definition,部品,コンポーネント,インスタンス,配置','onshape-feature-parts,fusion-components','object')
add('CAD','assembly','Assembly','アセンブリ','model-object',
    'Represent an assembly that contains positioned component instances and their relationships.',
    '配置された部品インスタンスとその関係を含むアセンブリを表します。',
    p('M16 11 V17 M7 17 H25 M7 17 V21 M25 17 V21')+r(11,3,10,8,2,fill=PALE)+r(2,21,10,8,2,fill=PALE)+r(20,21,10,8,2,fill=PALE)+accent('M14 6 H18 M5 24 H9 M23 24 H27'),
    'assembly,subassembly,component,アセンブリ,組立,サブアセンブリ','onshape-instances','object')
add('CAD','solid-body','Solid body','ソリッドボディ','model-object',
    'Represent a connected boundary enclosing a solid volume inside a part.',
    '部品内で閉じた体積を囲むソリッドボディを表します。',
    cube(5,4,22,21),
    'body,solid,brep,volume,ボディ,ソリッド,体積','solidworks-multibody','object')
add('CAD','mesh-body','Mesh body','メッシュボディ','model-object',
    'Represent faceted model geometry independently of a finite-element volume mesh.',
    '三角形面などで構成されたモデル形状を表します。',
    fill('M4 11 16 4 28 11 V23 L16 29 4 23Z')+p('M4 11 16 16 28 11 M16 16 V29 M4 23 16 16 28 23 M4 11 16 4 16 16 M16 4 28 11 M4 23 16 29 28 23'),
    'mesh,body,facet,triangle,メッシュ,ボディ,三角形','fusion-mesh-convert','object')
add('CAD','sketch','Sketch','スケッチ','model-object',
    'Represent a sketch container with multiple planar entities and constraints.',
    '複数の平面図形と拘束を含むスケッチ全体を表します。',
    fill('M3 23 10 5 29 10 22 28Z')+accent('M9 21 13 11 23 14 19 23Z')+c(16,17,2.5)+p('M5 28 H11 M5 28 V22'),
    'sketch,profile,container,スケッチ,図形,拘束','onshape-feature-parts','object')
add('CAD','face','Face','面','model-topology',
    'Represent one bounded face of a body in a topology or selection tree.',
    'トポロジー表示や選択ツリーでボディを構成する1つの面を表します。',
    fill('M4 23 11 5 28 10 21 28Z')+accent('M8 21 13 10 24 13 19 24Z'),
    'face,topology,brep,boundary,面,トポロジー,境界','fusion-brep-face','object')

# CAM: a setup object and four distinct cutting/programming operations.
add('CAM','setup','Machining setup','加工セットアップ','manufacturing-setup',
    'Represent a machining job containing stock, work coordinates, fixtures and an ordered operation list.',
    '素材、ワーク座標、治具、加工工程をまとめる加工ジョブを表します。',
    r(3,24,26,5,1,fill=PALE)+fill('M6 15 14 11 24 16 16 20Z')+p('M6 15 V21 L16 25 24 21 V16 M16 20 V25')+accent('M5 10 V3 M5 10 H13 M5 10 9 6'),
    'setup,job,stock,operations,セットアップ,加工ジョブ,工程','fusion-manufacture-browser','object')
add('CAM','thread-milling','Thread milling','ねじ切りフライス','machining-operation',
    'Mill a thread by helically interpolating a smaller cutter around a bore or boss.',
    '小径の工具を穴やボスの周囲でらせん補間し、ねじを切削します。',
    p('M4 5 V27 H28 V5 M4 10 H8 M4 16 H8 M4 22 H8 M24 10 H28 M24 16 H28 M24 22 H28')+r(12,3,6,14,1,fill=PALE)+accent('M10 23 C4 17 23 13 24 21 M21 18 24 21 27 18'),
    'thread,milling,helical,interpolation,ねじ切り,フライス,らせん','fusion-thread-milling')
add('CAM','holding-tabs','Holding tabs','保持タブ','toolpath-settings',
    'Leave small stock bridges in a contour cut so the part stays attached during machining.',
    '輪郭切抜きの途中に素材の橋を残し、加工中の部品を保持します。',
    r(3,4,26,24,2)+r(8,9,16,14,2,fill=PALE)+p('M3 14 H8 V18 H3 M24 14 H29 V18 H24',fill=PALE,stroke=TEAL),
    'tab,bridge,holding,contour,保持タブ,つなぎ,素材橋','fusion-holding-tabs,freecad-holding-tags')
add('CAM','engrave','Engraving','彫刻加工','machining-operation',
    'Engrave variable-width lines and sharp corners using a V-shaped cutter.',
    'V字工具を使い、線幅の変化や鋭いコーナーを持つ溝を彫刻します。',
    p('M12 3 H20 V10 L16 18 12 10Z',fill=PALE)+fill('M3 23 15 18 29 23 17 29Z')+accent('M8 23 16 26 24 23 M16 18 V23'),
    'engrave,v carve,lettering,v cutter,彫刻,V溝,文字','fusion-engrave')
add('CAM','deburr','Deburr / chamfer machining','バリ取り・面取り加工','machining-operation',
    'Machine an edge to remove burrs or form a controlled chamfer with a cutter.',
    '工具でエッジを加工し、バリを除去するか指定の面取りを施します。',
    fill('M3 19 H18 L24 25 V29 H3Z')+p('M12 3 H20 V11 L16 18 12 11Z',fill=PALE)+accent('M17 18 22 23 M25 13 28 10 M27 18 H30')+p('M4 23 H17'),
    'deburr,chamfer,edge,finishing,バリ取り,面取り,仕上げ','fusion-cam-chamfer,mastercam-deburr')

# CAE: different boundary conditions, reusable scope, mesh control and vector results.
add('CAE','gravity-load','Gravity load','重力荷重','analysis-load',
    'Apply gravitational acceleration as a distributed body load using the model mass.',
    'モデルの質量に応じた体積力として重力加速度を適用します。',
    r(4,3,24,22,2,fill=PALE)+accent('M10 7 V20 M7 17 10 20 13 17 M22 7 V20 M19 17 22 20 25 17')+p('M3 29 H29'),
    'gravity,self weight,acceleration,body load,重力,自重,加速度','ansys-gravity')
add('CAE','moment-load','Moment load','モーメント荷重','analysis-load',
    'Apply a rotational moment or torque to a selected region of the analysis model.',
    '解析モデルの選択領域に回転モーメントやトルクを適用します。',
    r(3,12,21,8,2,fill=PALE)+p('M8 12 V20')+accent('M20 5 C31 5 31 27 20 27 M20 27 24 22 M20 27 26 29')+c(23,16,2),
    'moment,torque,rotation,モーメント,トルク,回転','ansys-moment')
add('CAE','symmetry-boundary','Symmetry boundary','対称境界','analysis-boundary',
    'Apply the degrees-of-freedom restrictions required on a simulation symmetry boundary.',
    '解析の対称境界に必要な自由度の拘束を設定します。',
    fill('M4 7 H15 V25 H4Z')+p('M18 3 V29 M21 7 H28 V25 H21',stroke_dasharray='2 3')+accent('M8 12 H17 M14 9 17 12 14 15 M8 21 H17 M14 18 17 21 14 24'),
    'symmetry,boundary,half model,対称,境界,半モデル','ansys-symmetry')
add('CAE','named-selection','Named selection','名前付き選択','analysis-scope',
    'Define a reusable set of geometry or mesh entities for material, load or boundary assignments.',
    '材料、荷重、境界条件の割当に使う形状やメッシュの集合を名前付きで定義します。',
    p('M4 6 H23 V26 H4Z',stroke_dasharray='2 3')+p('M8 21 12 11 20 20Z')+nodes([(8,21),(12,11),(20,20)])+p('M19 4 H28 V13 L23 17 19 13Z',fill=PALE,stroke=TEAL)+c(23.5,8,1.2,stroke=TEAL),
    'named selection,physical group,mesh group,scope,名前付き選択,物理グループ,節点集合','gmsh-physical-groups')
add('CAE','boundary-layer-mesh','Boundary-layer mesh','境界層メッシュ','mesh-control',
    'Grow thin graded element layers normal to a wall to resolve near-wall behavior.',
    '壁面近傍を解像するため、壁法線方向に厚みが変化する薄い要素層を生成します。',
    p('M3 28 H29 M3 25 Q16 17 29 25 M3 21 Q16 10 29 21 M3 14 Q16 1 29 14 M3 4 H29 M8 4 V26 M16 4 V22 M24 4 V26')+accent('M3 28 Q16 22 29 28'),
    'mesh,boundary layer,inflation,wall,メッシュ,境界層,インフレーション','ansys-inflation')
add('CAE','fluid-outlet','Fluid outlet','流出口','analysis-boundary',
    'Specify a fluid exit boundary using an outlet pressure or gradient condition.',
    '出口圧力や勾配条件を指定して流体の流出口を設定します。',
    p('M3 4 H20 V9 M3 28 H20 V23')+accent('M7 11 H29 M25 7 29 11 25 15 M7 21 H29 M25 17 29 21 25 25')+p('M20 12 V20',stroke_dasharray='2 3'),
    'fluid,outlet,pressure,cfd,流体,流出口,出口圧力','openfoam-boundaries')
add('CAE','wall-boundary','Wall boundary','壁面境界','analysis-boundary',
    'Set an impermeable fluid wall with an appropriate slip or no-slip velocity condition.',
    'すべりやすべりなしの速度条件を持つ不透過壁面を設定します。',
    p('M4 25 H28 M4 30 9 25 M12 30 17 25 M20 30 25 25')+accent('M5 18 H25 M21 14 25 18 21 22 M5 7 H25 M21 3 25 7 21 11'),
    'wall,boundary,no slip,fluid,壁面,境界,すべりなし','openfoam-boundaries')
add('CAE','streamline-result','Streamline result','流線表示','analysis-results',
    'Trace continuous lines through a velocity vector field to inspect flow direction and structure.',
    '速度ベクトル場に沿う線を描き、流れの方向や構造を確認します。',
    c(16,16,5,fill=PALE)+accent('M3 5 Q16 1 29 5 M25 2 29 5 25 8 M3 16 C8 16 7 7 16 7 C25 7 24 16 29 16 M26 12 29 16 25 18 M3 27 Q16 31 29 27 M25 24 29 27 25 30'),
    'streamline,flow,velocity,vector,result,流線,流速,結果','openfoam-streamline')
