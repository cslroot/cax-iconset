"""Curated independent engineering commands, hand drawn on the original 32 px grid.

No operation × profile generation, state-badge proliferation or visual variants.
Every record represents a specific usable application command.
"""
from core import p, r, c, g, accent, fill, cube, nodes, record, PALE, TEAL, AMBER

ENGINEERING = {}

def add(domain, id, en, ja, family, description, description_ja, body, tags):
    item = record(id, en, ja, body, tags)
    item.update(family=family, description=description, descriptionJa=description_ja)
    item['tags'] = list(dict.fromkeys(item['tags'] + [en.lower(), ja, domain.lower()]))
    ENGINEERING.setdefault(domain, []).append(item)

# CAD: sketch editing and constraints.
add('CAD', 'sketch-circle', 'Sketch circle', 'スケッチ円', 'sketch',
    'Draw a sketch circle from its center and radius.', '中心と半径を指定してスケッチに円を描きます。',
    c(16,16,10,fill=PALE)+accent('M16 16 24 10')+c(16,16,1.6,fill=TEAL)+nodes([(24,10)]),
    'sketch,circle,radius,円,半径,作図')
add('CAD', 'sketch-rectangle', 'Sketch rectangle', 'スケッチ長方形', 'sketch',
    'Draw a rectangular sketch profile from opposing corners.', '対角の2点を指定して長方形のスケッチを描きます。',
    r(6,8,20,16,1,fill=PALE)+p('M6 19 H11 V24')+nodes([(6,8),(26,24)]),
    'sketch,rectangle,corners,長方形,矩形,作図')
add('CAD', 'sketch-trim', 'Trim sketch', 'スケッチトリム', 'sketch-edit',
    'Remove a sketch segment up to its neighboring intersections.', '交点で区切られた不要なスケッチ線分を切り取ります。',
    p('M6 5 V27 M5 17 H15 M23 17 H28')+accent('M15 17 H23',stroke_dasharray='2 3')+c(20,6,2.6)+c(27,6,2.6)+p('M21 8 27 15 M26 8 20 15'),
    'sketch,trim,intersection,トリム,切取り,交点')
add('CAD', 'sketch-extend', 'Extend sketch', 'スケッチ延長', 'sketch-edit',
    'Extend a sketch entity until it meets a selected boundary.', 'スケッチ線を延長して指定した境界まで到達させます。',
    p('M26 4 V28 M4 23 14 16')+accent('M14 16 26 8 M20 9 26 8 24 14')+c(14,16,1.7,fill=PALE),
    'sketch,extend,boundary,延長,境界')
add('CAD', 'sketch-offset', 'Offset sketch', 'スケッチオフセット', 'sketch-edit',
    'Create a parallel copy of sketch geometry at a specified distance.', 'スケッチ図形から指定した距離だけ離れた平行な図形を作成します。',
    p('M5 25 V13 Q5 5 13 5 H26')+accent('M12 26 V16 Q12 12 16 12 H27')+p('M7 21 H20 M16 18 20 21 16 24'),
    'sketch,offset,distance,オフセット,平行距離')
add('CAD', 'sketch-dimension', 'Sketch dimension', 'スケッチ寸法', 'sketch-constraint',
    'Apply a driving length, radius or angle dimension to sketch geometry.', 'スケッチ図形の長さ、半径、角度を制御する寸法を設定します。',
    p('M6 5 V27 M26 5 V27 M6 23 H26')+accent('M6 11 H26 M10 8 6 11 10 14 M22 8 26 11 22 14')+p('M14 20 V23 M18 20 V23'),
    'dimension,driving,size,寸法,寸法拘束')
add('CAD', 'constraint-perpendicular', 'Perpendicular constraint', '垂直拘束', 'sketch-constraint',
    'Keep two selected sketch lines at a right angle.', '選択した2本のスケッチ線を直角に保ちます。',
    p('M6 5 V25 H28')+r(6,17,8,8,0,fill=PALE)+accent('M21 5 V14 M17 14 H25'),
    'constraint,perpendicular,right angle,垂直,直角,拘束')
add('CAD', 'constraint-equal', 'Equal constraint', '等値拘束', 'sketch-constraint',
    'Make selected sketch lengths or radii equal.', '選択したスケッチ線の長さや円の半径を等しくします。',
    p('M5 5 27 11 M5 22 27 28')+accent('M11 14 H22 M11 18 H22')+nodes([(5,5),(27,11),(5,22),(27,28)]),
    'constraint,equal,length,radius,等値,同じ長さ,拘束')
add('CAD', 'constraint-symmetric', 'Symmetric constraint', '対称拘束', 'sketch-constraint',
    'Keep selected sketch entities symmetric about a construction line.', '選択したスケッチ図形を基準線に対して対称に保ちます。',
    p('M16 3 V29',stroke_dasharray='2 3')+p('M5 7 10 25 M27 7 22 25')+accent('M7 16 H13 M10 13 13 16 10 19 M25 16 H19 M22 13 19 16 22 19'),
    'constraint,symmetry,centerline,対称,中心線,拘束')
# CAD: solid, assembly and reference commands.
add('CAD', 'mirror', 'Mirror features', 'フィーチャミラー', 'feature-pattern',
    'Reflect selected features or bodies across a reference plane.', '基準平面に対して選択したフィーチャやボディを対称複写します。',
    p('M16 3 V29',stroke_dasharray='2 3')+fill('M4 9 H12 V25 H4Z')+accent('M20 9 H28 V25 H20Z')+p('M8 5 Q16 1 24 5 M21 3 24 5 21 7'),
    'mirror,reflect,feature,body,ミラー,対称複写')
add('CAD', 'boolean-intersection', 'Boolean intersection', '積演算', 'solid-boolean',
    'Keep only the shared volume of selected intersecting solid bodies.', '選択したソリッドボディが共通して占める体積だけを残します。',
    r(4,4,17,17,2,stroke_dasharray='2 3')+r(12,12,16,16,2,stroke_dasharray='2 3')+r(12,12,9,9,1,fill=PALE,stroke=TEAL)+accent('M14 19 19 14'),
    'boolean,intersection,common volume,積,共通部分')
add('CAD', 'move-body', 'Move body', 'ボディ移動', 'body-transform',
    'Translate or rotate a selected body using a transform control.', '移動量や回転角を指定してボディの配置を変更します。',
    fill('M5 13 11 10 17 13 V21 L11 24 5 21Z')+p('M5 13 11 16 17 13 M11 16 V24')+accent('M20 20 H28 M25 17 28 20 25 23 M20 20 V5 M17 8 20 5 23 8'),
    'move,translate,rotate,body,移動,回転,ボディ')
add('CAD', 'scale-body', 'Scale body', 'ボディ拡大縮小', 'body-transform',
    'Resize a selected body using a uniform or directional scale factor.', '一様または方向別の倍率を指定してボディを拡大縮小します。',
    r(5,18,9,9,1,fill=PALE)+r(5,5,22,22,2,stroke_dasharray='2 3')+accent('M14 18 26 6 M20 6 H26 V12')+c(5,27,1.5,fill=TEAL),
    'scale,resize,factor,body,倍率,拡大,縮小')
add('CAD', 'datum-plane', 'Create datum plane', '基準平面作成', 'reference-geometry',
    'Create a construction plane for sketches, features or measurements.', 'スケッチ、フィーチャ、測定に使用する構築平面を作成します。',
    fill('M3 22 12 10 29 16 20 28Z')+p('M6 13 15 4 27 9',stroke_dasharray='2 3')+accent('M16 20 V6 M13 10 16 6 19 10'),
    'datum,construction,plane,基準平面,構築平面')
add('CAD', 'datum-axis', 'Create datum axis', '基準軸作成', 'reference-geometry',
    'Create a reference axis for revolutions, patterns or assembly constraints.', '回転、パターン、アセンブリ拘束で使用する基準軸を作成します。',
    fill('M6 22 13 14 25 19 18 27Z')+accent('M6 28 26 4',stroke_dasharray='4 3')+c(16,16,3,fill='white')+p('M22 4 H26 V8'),
    'datum,construction,axis,基準軸,構築軸')
add('CAD', 'fixed-joint', 'Fixed joint', '固定ジョイント', 'assembly',
    'Connect two components with no relative degrees of freedom.', '2つの部品の相対的な移動と回転をすべて拘束します。',
    r(4,8,9,17,2,fill=PALE)+r(19,8,9,17,2,fill=PALE)+p('M13 13 H19 M13 20 H19')+accent('M10 28 H22 M12 28 10 30 M17 28 15 30 M22 28 20 30'),
    'assembly,joint,rigid,固定,剛体,結合')
add('CAD', 'prismatic-joint', 'Prismatic joint', '直動ジョイント', 'assembly',
    'Connect components so that only translation along one axis remains.', '部品間に1軸方向の直動だけを許すジョイントを設定します。',
    r(4,12,24,10,2,fill=PALE)+r(11,8,10,18,2)+p('M4 17 H28')+accent('M7 4 H25 M10 2 7 4 10 6 M22 2 25 4 22 6'),
    'assembly,joint,slider,prismatic,直動,スライダ,結合')
add('CAD', 'interference-check', 'Assembly interference', 'アセンブリ干渉検査', 'assembly-inspection',
    'Find overlapping solid volumes between assembly components.', 'アセンブリ部品間でソリッドが重なる干渉体積を検出します。',
    fill('M4 8 12 4 20 8 V20 L12 24 4 20Z')+p('M13 14 21 10 28 14 V26 L21 29 13 25Z')+p('M13 14 20 10 V20 L13 24Z',fill='#fff3da',stroke=AMBER)+p('M14 18 18 14 M14 22 18 18',stroke=AMBER),
    'assembly,interference,overlap,干渉,重なり,体積')
# CAD: distinct sheet-metal and surface operations.
add('CAD', 'sheet-metal-flange', 'Sheet-metal flange', '板金フランジ', 'sheet-metal',
    'Create a bent flange along a selected sheet-metal edge.', '選択した板金エッジに沿って曲がったフランジを作成します。',
    fill('M4 22 15 16 27 21 16 28Z')+fill('M15 16 V5 L27 10 V21Z')+p('M15 16 27 21',stroke_dasharray='2 3')+accent('M8 14 V5 M5 8 8 5 11 8'),
    'sheet metal,flange,edge,板金,フランジ,つば')
add('CAD', 'sheet-metal-unfold', 'Unfold sheet metal', '板金曲げ解除', 'sheet-metal',
    'Temporarily unfold selected bends so features can be added across them.', '曲げを一時的に開き、曲げ部をまたぐフィーチャを追加できる状態にします。',
    fill('M4 23 14 18 28 23 18 28Z')+p('M14 18 V6 L26 10 V22',stroke_dasharray='2 3')+accent('M10 5 C3 6 2 14 7 17 M4 17 H8 V13'),
    'sheet metal,unfold,bend,板金,曲げ解除,展開')
add('CAD', 'sheet-metal-flat-pattern', 'Create flat pattern', '板金展開図作成', 'sheet-metal',
    'Generate the manufacturing flat pattern of an entire sheet-metal part.', '板金部品全体の加工用展開形状を生成します。',
    fill('M11 4 H21 V10 H28 V22 H21 V28 H11 V22 H4 V10 H11Z')+p('M11 10 H21 V22 H11Z',stroke_dasharray='2 3')+accent('M14 15 H18 M16 13 V19'),
    'sheet metal,flat pattern,blank,板金,展開図,ブランク')
add('CAD', 'surface-patch', 'Surface patch', 'サーフェスパッチ', 'surface',
    'Create a surface that fills a selected closed boundary.', '選択した閉じた境界を埋めるサーフェスを作成します。',
    fill('M5 10 Q16 3 27 10 L23 25 Q14 19 5 25Z')+accent('M9 12 Q16 8 23 12 M10 17 Q16 13 24 18 M10 10 9 23 M18 7 18 23')+nodes([(5,10),(27,10),(23,25),(5,25)]),
    'surface,patch,fill,boundary,サーフェス,穴埋め,境界')
add('CAD', 'surface-sew', 'Sew surfaces', 'サーフェス縫合', 'surface',
    'Join adjacent surface patches into a connected surface or closed solid.', '隣接するサーフェスを縫合して一体の面または閉じたソリッドにします。',
    fill('M4 8 15 4 V25 L4 28Z')+fill('M18 4 28 8 V28 L18 25Z')+accent('M12 10 H21 M12 16 H21 M12 22 H21')+p('M15 4 V25 M18 4 V25',stroke_dasharray='2 3'),
    'surface,sew,stitch,join,サーフェス,縫合,結合')
add('CAD', 'surface-trim', 'Trim surface', 'サーフェストリム', 'surface',
    'Remove part of a surface using an intersecting curve or surface.', '交差する曲線や面を境界にしてサーフェスの一部を切り取ります。',
    fill('M4 9 Q15 3 28 9 L23 20 Q14 14 4 21Z')+p('M4 21 V28 Q15 21 23 27 V20',stroke_dasharray='2 3')+accent('M3 22 Q14 13 28 22'),
    'surface,trim,split,boundary,サーフェス,トリム,切取り')
# CAD: model inspection and practical document/assembly commands.
add('CAD', 'section-view', 'Section view', '断面表示', 'model-view',
    'Cut the display of a model with a plane to inspect its interior.', '平面でモデルの表示を切断し、内部形状を確認します。',
    fill('M5 10 16 5 27 10 V25 L16 29 5 25Z')+p('M5 10 16 15 27 10 M16 15 V29')+accent('M5 18 16 23 27 18 M7 20 10 19 M11 23 14 21 M18 22 21 20 M23 20 26 18'),
    'view,section,cutaway,inspection,断面,内部,切断表示')
add('CAD', 'orthographic-view', 'Orthographic projection', '平行投影', 'model-view',
    'Display the model using parallel projection without perspective scaling.', '遠近による縮小を使わず、平行投影でモデルを表示します。',
    r(4,10,17,17,1,fill=PALE)+p('M4 10 11 4 H28 V21 L21 27 M21 10 28 4 M21 10 V27')+accent('M8 14 H17 M8 19 H17 M8 24 H17'),
    'view,orthographic,parallel projection,平行投影,正投影')
add('CAD', 'perspective-view', 'Perspective projection', '透視投影', 'model-view',
    'Display the model with perspective so distant geometry appears smaller.', '遠い形状が小さく見える透視投影でモデルを表示します。',
    r(4,9,17,19,1,fill=PALE)+p('M4 9 17 4 H27 V16 L21 28 M21 9 27 4 M21 9 V28')+accent('M8 15 17 12 M8 22 17 17'),
    'view,perspective,projection,透視投影,遠近法')
add('CAD', 'parameters', 'Edit parameters', 'パラメータ編集', 'parametric-model',
    'Edit named dimensions, expressions and user parameters that drive the model.', 'モデルを制御する寸法、数式、ユーザーパラメータを編集します。',
    r(4,4,24,24,3)+p('M8 10 H13 M8 16 H13 M8 22 H13')+accent('M18 8 V12 M16 10 H20 M17 15 H23 M17 18 H23 M18 22 H24')+c(23,10,1,fill=TEAL),
    'parameter,expression,dimension,パラメータ,変数,数式')
add('CAD', 'recompute', 'Recompute model', 'モデル再計算', 'parametric-model',
    'Rebuild dependent features after dimensions or parameters change.', '寸法やパラメータの変更後に依存フィーチャを再計算します。',
    fill('M10 13 16 10 22 13 V21 L16 24 10 21Z')+p('M10 13 16 16 22 13 M16 16 V24')+accent('M5 13 A12 12 0 0 1 25 7 M21 7 H25 V3 M27 20 A12 12 0 0 1 7 26 M7 22 V26 H11'),
    'recompute,rebuild,update,feature,再計算,再構築,更新')
add('CAD', 'assembly-place', 'Place component', '部品配置', 'assembly',
    'Insert an existing component into the active assembly.', '既存の部品をアクティブなアセンブリに挿入します。',
    p('M4 19 12 15 20 19 V27 L12 30 4 27Z')+fill('M17 5 23 2 29 5 V12 L23 15 17 12Z')+p('M17 5 23 8 29 5 M23 8 V15')+accent('M15 11 9 18 M9 13 V18 H14'),
    'assembly,place,insert,component,部品配置,部品挿入')
add('CAD', 'assembly-explode', 'Exploded assembly view', 'アセンブリ分解表示', 'assembly-view',
    'Separate assembly components visually to show their relationship and order.', '部品を視覚的に離してアセンブリの構成や組立順序を示します。',
    fill('M3 18 9 15 15 18 9 21Z')+p('M3 18 V24 L9 27 15 24 V18 M9 21 V27')+fill('M17 6 23 3 29 6 23 9Z')+p('M17 6 V12 L23 15 29 12 V6 M23 9 V15')+accent('M13 15 19 9 M16 9 H19 V12 M13 12 V15 H16'),
    'assembly,explode,exploded,分解表示,分解図')
add('CAD', 'bill-of-materials', 'Bill of materials', '部品表', 'assembly-documentation',
    'Create or inspect the quantities and properties of assembly components.', 'アセンブリ部品の数量と属性を部品表で作成または確認します。',
    r(4,4,24,25,2)+p('M4 11 H28 M4 17 H28 M4 23 H28 M11 4 V29 M22 4 V29')+accent('M15 8 H19 M15 14 H18 M15 20 H19 M15 26 H18'),
    'bom,parts list,quantity,assembly,部品表,数量,構成部品')

# CAM: setup and programming actions missing from the original operation set.
add('CAM', 'tool-library', 'Tool library', '工具ライブラリ', 'cutting-tool',
    'Browse and manage reusable cutter and holder definitions.', '再利用する工具とホルダーの定義を検索、管理します。',
    r(3,5,26,23,3)+p('M3 11 H29 M9 15 V24 M8 20 H10 M16 14 V24 M14 22 18 18 M23 14 V21 L20 25 H26Z')+accent('M7 8 H12'),
    'tool,library,cutter,holder,工具,ライブラリ,ホルダー')
add('CAM', 'setup-orientation', 'Tool orientation', '工具方向設定', 'manufacturing-setup',
    'Define the tool-axis orientation for an indexed or multi-axis operation.', '割出し加工や多軸加工で使用する工具軸の向きを設定します。',
    fill('M4 23 15 18 28 23 17 28Z')+g(r(13,4,6,12,1,fill=PALE)+p('M16 16 V21'),transform='rotate(25 16 20)')+accent('M5 15 A13 13 0 0 1 14 3 M10 3 H14 V7'),
    'setup,tool axis,orientation,multi axis,工具方向,工具軸,多軸')
add('CAM', 'regenerate-toolpath', 'Regenerate toolpath', '工具軌跡再生成', 'toolpath-management',
    'Recalculate an operation toolpath after geometry or machining settings change.', '形状や加工条件の変更後に加工工程の工具軌跡を再計算します。',
    p('M6 26 V12 H16 V25 H22 V13')+accent('M7 6 A12 12 0 0 1 27 10 M23 10 H27 V6 M26 18 A10 10 0 0 1 19 28'),
    'toolpath,regenerate,calculate,update,工具軌跡,再生成,計算')
add('CAM', 'lead-in-out', 'Lead-in and lead-out', '進入退出設定', 'toolpath-settings',
    'Set how the cutter enters and leaves a machining contour.', '工具が加工輪郭に進入し、退出する経路を設定します。',
    r(10,6,16,20,4,fill=PALE)+p('M10 10 V22')+accent('M3 6 Q10 6 10 13 M6 10 10 13 13 9 M10 21 Q10 28 3 28 M6 25 3 28 6 30'),
    'toolpath,lead in,lead out,entry,exit,進入,退出,アプローチ')
add('CAM', 'feeds-speeds', 'Feeds and speeds', '送りと回転数', 'toolpath-settings',
    'Set the spindle speed and cutting feed values for an operation.', '加工工程の主軸回転数と切削送り速度を設定します。',
    c(13,13,9,fill=PALE)+p('M13 13 18 7 M6 9 8 10 M6 16 8 15 M17 19 16 17')+accent('M5 27 H28 M24 23 28 27 24 30')+p('M25 4 V13 M22 10 25 13 28 10'),
    'feed,spindle,speed,rpm,送り,主軸,回転数,切削条件')
add('CAM', 'tool-change', 'Tool change', '工具交換', 'nc-program',
    'Insert a change to another cutter in the machining sequence.', '加工順序の途中に別の工具への交換を挿入します。',
    p('M6 4 H12 V19 H6Z M5 14 13 10 M21 4 H27 V15 L24 21 21 15Z')+accent('M6 26 H27 M10 23 6 26 10 29 M23 23 27 26 23 29'),
    'tool,change,sequence,工具交換,工具変更,工程')

# CAE: study lifecycle and result interrogation.
add('CAE', 'new-study', 'New simulation study', '新規解析スタディ', 'analysis-study',
    'Create an analysis study with its own setup, loads and result set.', '設定、荷重、結果を独立して管理する解析スタディを作成します。',
    p('M5 4 H20 L26 10 V28 H5Z M20 4 V10 H26')+p('M8 23 14 12 20 23Z M8 23 14 19 20 23 M14 12 V19')+accent('M23 13 V24 M22 17 H25 M22 21 H25'),
    'study,new,simulation,analysis,解析,新規スタディ')
add('CAE', 'model-precheck', 'Model precheck', '解析モデル事前確認', 'analysis-solver',
    'Check study setup for missing inputs or inconsistent conditions before solving.', '計算前に解析設定の不足や条件の不整合を確認します。',
    p('M4 23 11 7 24 10 28 24Z M11 7 17 18 24 10 M4 23 17 18 28 24')+c(23,23,6,fill='white')+accent('M20 23 22 25 26 21'),
    'precheck,validate,setup,solver,事前確認,入力検査,解析設定')
add('CAE', 'run-solver', 'Run solver', '解析実行', 'analysis-solver',
    'Start the numerical solution of the active simulation study.', 'アクティブな解析スタディの数値計算を開始します。',
    r(4,4,16,24,2)+p('M8 9 H16 M8 15 H12 M8 21 H12')+p('M17 13 29 20 17 27Z',fill=PALE,stroke=TEAL),
    'solver,solve,run,calculate,解析実行,計算開始,ソルバー')
add('CAE', 'solver-settings', 'Solver settings', 'ソルバー設定', 'analysis-solver',
    'Configure solution controls such as increments, tolerances and iteration limits.', '計算の増分、許容誤差、反復上限などの制御条件を設定します。',
    r(4,4,24,24,2)+p('M9 8 V24 M16 8 V24 M23 8 V24')+r(7,11,4,5,1,fill=PALE)+r(14,18,4,5,1,fill=PALE)+r(21,8,4,5,1,fill=PALE),
    'solver,settings,tolerance,iteration,ソルバー,設定,反復,許容誤差')
add('CAE', 'result-probe', 'Probe result', '解析結果プローブ', 'analysis-results',
    'Read a result value at a selected model location.', 'モデル上の指定位置における解析結果の値を読み取ります。',
    fill('M4 10 15 5 27 11 23 26 9 27Z')+p('M5 17 Q14 10 25 17 M8 24 Q16 17 24 23')+c(18,14,4,fill='white',stroke=TEAL)+accent('M18 7 V11 M18 17 V21 M11 14 H15 M21 14 H28'),
    'results,probe,value,node,解析結果,値,プローブ,節点')
add('CAE', 'result-plot', 'Result XY plot', '解析結果グラフ', 'analysis-results',
    'Plot a result quantity along a path or over time or frequency.', '経路、時間、周波数に対する解析結果をグラフ化します。',
    p('M5 4 V27 H29')+accent('M8 23 C12 23 11 9 16 9 S22 20 27 5')+nodes([(8,23),(16,9),(27,5)])+p('M10 27 V29 M18 27 V29 M26 27 V29'),
    'results,plot,graph,time,frequency,解析結果,グラフ,時刻歴,周波数')
add('CAE', 'deformation-result', 'Deformed shape', '変形表示', 'analysis-results',
    'Display the computed displacement as a scaled deformed model shape.', '計算した変位を倍率付きの変形形状として表示します。',
    p('M5 7 H27 V14 H5Z',stroke_dasharray='2 3')+fill('M5 13 Q15 14 27 23 V29 Q15 20 5 20Z')+p('M5 5 V28 M2 10 5 7 M2 18 5 15 M2 26 5 23')+accent('M26 11 V19 M23 16 26 19 29 16'),
    'results,deformation,displacement,scale,解析結果,変形,変位')

# CMM: measurement programming, constructions and evaluations.
add('CMM', 'probe-definition', 'Define probe assembly', 'プローブ構成定義', 'inspection-probe',
    'Define the probe head, extensions and stylus geometry used by a routine.', '測定ルーチンで使用するヘッド、延長棒、スタイラスの構成を定義します。',
    r(5,4,9,7,2,fill=PALE)+p('M9.5 11 V17 H20 V24')+c(20,27,2,fill=TEAL)+p('M17 4 H28 M17 8 H24')+accent('M24 14 H29 M26.5 11.5 V16.5'),
    'probe,assembly,definition,stylus,プローブ構成,ヘッド,スタイラス')
add('CMM', 'construct-feature', 'Construct feature', '測定形体構築', 'feature-construction',
    'Derive a geometric feature from existing measured features or point data.', '既存の測定形体や測定点から新しい幾何形体を構築します。',
    nodes([(5,22),(10,13),(18,9),(27,14),(25,24)])+accent('M5 24 Q5 5 25 11 Q29 17 25 25')+p('M16 4 V28 M4 17 H29',stroke_dasharray='2 3'),
    'construct,fit,derived feature,測定形体,構築,フィッティング')
add('CMM', 'dimension-distance', 'Measure feature distance', '形体間距離評価', 'dimensional-inspection',
    'Create a recorded distance inspection between measured features with nominal and tolerance values.', '測定形体間の距離を基準値と公差付きの検査寸法として記録します。',
    c(8,7,3,fill=PALE)+c(24,7,3,fill=PALE)+p('M8 10 V20 M24 10 V20')+accent('M8 16 H24 M11 13 8 16 11 19 M21 13 24 16 21 19')+r(5,23,22,6,1)+p('M14 23 V29 M21 23 V29 M8 26 H11'),
    'dimension,distance,feature,measurement,距離,寸法,形体間')
add('CMM', 'evaluate-tolerance', 'Evaluate tolerance', '公差判定', 'inspection-evaluation',
    'Compare measured dimensions with nominal values and tolerance limits.', '測定寸法を基準値と公差限界に照らして判定します。',
    r(4,5,24,23,2)+p('M8 10 H24 M8 23 H24 M11 14 V20 M21 14 V20')+accent('M8 17 H24')+c(17,17,2.5,fill=PALE)+p('M13 24 15 26 19 22'),
    'tolerance,evaluate,nominal,limits,公差,判定,基準値,限界')
add('CMM', 'run-inspection', 'Run inspection routine', '検査ルーチン実行', 'inspection-program',
    'Execute the programmed sequence of probe moves and measurements.', 'プログラムされたプローブ移動と測定の順序を実行します。',
    p('M4 4 H15 V15 L11 18 M4 9 H15')+c(11,20,2,fill=TEAL)+p('M4 27 H15 M6 27 V30 M13 27 V30')+p('M20 10 29 17 20 24Z',fill=PALE,stroke=TEAL),
    'inspection,run,routine,execute,検査,実行,測定ルーチン')

# OLP: program lifecycle and instructions not present in the initial core.
add('OLP', 'generate-program', 'Generate robot program', 'ロボットプログラム生成', 'robot-program',
    'Translate an offline sequence into controller-specific robot program code.', 'オフラインの動作列をロボットコントローラー用コードに変換します。',
    p('M4 5 H17 V27 H4Z M7 10 H13 M7 15 H11 M7 20 H13')+accent('M18 16 H28 M24 12 28 16 24 20')+p('M23 6 H28 V10 M23 26 H28 V22'),
    'program,generate,postprocess,code,プログラム,生成,ポスト処理')
add('OLP', 'transfer-program', 'Transfer robot program', 'ロボットプログラム転送', 'robot-program',
    'Send a generated robot program to the configured controller destination.', '生成したロボットプログラムを設定済みコントローラーへ転送します。',
    r(3,5,10,17,2,fill=PALE)+p('M6 10 H10 M6 15 H10')+r(22,10,7,18,1)+c(25.5,24,1,fill=TEAL)+accent('M14 17 H21 M17 13 21 17 17 21')+p('M24 14 H27 M24 18 H27'),
    'program,transfer,controller,upload,プログラム転送,コントローラー')
add('OLP', 'tool-frame', 'Set tool frame', 'ツール座標系設定', 'robot-frame',
    'Activate the tool coordinate frame used by subsequent motion instructions.', '後続の移動命令で使用するツール座標系を選択します。',
    fill('M5 4 H17 V10 L12 15 7 10Z')+p('M12 15 V22')+c(12,22,2,fill=TEAL)+accent('M14 22 H28 M25 19 28 22 25 25 M12 20 V10 M9 13 12 10 15 13 M10 24 5 29 M5 25 V29 H9'),
    'tool,frame,coordinate,active,ツール座標系,工具座標,選択')
add('OLP', 'payload', 'Set robot payload', '可搬質量設定', 'robot-tool',
    'Specify tool and carried-load mass properties for the robot configuration.', 'ロボット設定に工具や搬送物の質量特性を指定します。',
    p('M5 5 H13 V12 M9 12 V16')+fill('M6 19 H24 L28 28 H3Z')+p('M12 19 V15 Q12 11 16 11 Q20 11 20 15 V19')+accent('M23 3 V12 M20 9 23 12 26 9'),
    'payload,mass,center of gravity,tool,可搬質量,負荷,重心')
add('OLP', 'set-speed', 'Set motion speed', '動作速度設定', 'robot-motion',
    'Insert a speed instruction for subsequent robot motions.', '後続のロボット移動に適用する速度命令を挿入します。',
    p('M4 24 A12 12 0 0 1 28 24 H4Z',fill=PALE)+accent('M16 23 24 12')+c(16,23,2,fill=TEAL)+p('M7 17 10 19 M13 12 14 15 M22 23 H26')+accent('M4 5 H13 M10 2 13 5 10 8'),
    'speed,motion,velocity,instruction,速度,動作速度,命令')
add('OLP', 'simulate-program', 'Simulate robot program', 'ロボットプログラムシミュレーション', 'robot-verification',
    'Preview a robot program through its commanded motions and events.', 'ロボットプログラムの移動命令とイベントを仮想環境で再生します。',
    r(3,4,26,24,3)+p('M6 24 H15 M9 24 V17 L6 13 13 9 18 13')+nodes([(9,17),(6,13),(13,9)])+p('M20 15 27 20 20 25Z',fill=PALE,stroke=TEAL),
    'simulation,preview,program,motion,シミュレーション,再生,動作確認')
add('OLP', 'call-program', 'Call subprogram', 'サブプログラム呼出し', 'robot-program',
    'Insert an instruction that calls a reusable robot subprogram.', '再利用するロボットサブプログラムを呼び出す命令を挿入します。',
    r(3,4,12,23,2)+p('M6 9 H12 M6 14 H10 M6 22 H12')+r(21,10,8,18,2,fill=PALE)+accent('M11 18 H20 M17 15 20 18 17 21')+p('M24 14 H26 M24 19 H26 M24 24 H26'),
    'program,call,subprogram,reuse,呼出し,サブプログラム,再利用')

# CAD drawings: document creation, view derivation and manufacturing annotation.
add('CAD', 'drawing-create', 'Create drawing', '図面作成', 'drawing-document',
    'Create a drawing document linked to the current design or assembly.', '現在の設計またはアセンブリを参照する図面ドキュメントを作成します。',
    r(3,5,26,23,1)+p('M3 23 H29 M19 23 V28 M24 23 V28')+fill('M7 12 12 9 17 12 V18 L12 21 7 18Z')+p('M7 12 12 15 17 12 M12 15 V21')+accent('M24 10 V18 M20 14 H28'),
    'drawing,new,sheet,document,図面,新規作成,製図')
add('CAD', 'drawing-base-view', 'Base drawing view', '図面基本ビュー', 'drawing-view',
    'Place the first model view on a drawing sheet with a selected orientation and scale.', '方向と尺度を選び、図面シートに最初のモデルビューを配置します。',
    r(3,4,26,25,1)+p('M3 24 H29 M20 24 V29')+fill('M8 10 H22 V20 H8Z')+c(15,15,3)+accent('M7 7 H12 M7 7 V12'),
    'drawing,base view,orientation,scale,図面,基本ビュー,尺度')
add('CAD', 'drawing-projected-view', 'Projected drawing view', '図面投影ビュー', 'drawing-view',
    'Create an orthographic drawing view aligned with an existing parent view.', '既存の親ビューから整列した正投影ビューを作成します。',
    r(4,18,10,10,1,fill=PALE)+c(9,23,2.5)+r(19,18,10,10,1)+r(4,3,10,9,1)+p('M9 12 V18 M14 23 H19',stroke_dasharray='2 3')+accent('M19 7 25 13 M21 13 H25 V9'),
    'drawing,projected view,orthographic,parent,図面,投影ビュー,親ビュー')
add('CAD', 'drawing-detail-view', 'Detail drawing view', '図面詳細ビュー', 'drawing-view',
    'Place an enlarged drawing view of a selected region for local detail.', '選択した領域を拡大した詳細ビューを図面に配置します。',
    p('M4 23 V10 H15 V23Z M4 17 H15')+c(11,17,4,stroke=TEAL,stroke_dasharray='2 2')+p('M15 14 19 10')+c(24,9,6,fill=PALE)+p('M20 9 H28 M24 5 V13')+accent('M20 23 H28 M24 19 V27'),
    'drawing,detail view,enlarge,region,図面,詳細ビュー,拡大図')
add('CAD', 'drawing-dimension', 'Drawing dimension', '図面寸法記入', 'drawing-annotation',
    'Add a displayed manufacturing dimension to geometry in a drawing view.', '図面ビューの形状に製造用の寸法注記を追加します。',
    r(3,4,26,25,1)+r(8,16,16,9,1,fill=PALE)+p('M8 9 V16 M24 9 V16')+accent('M8 12 H24 M11 10 8 12 11 14 M21 10 24 12 21 14')+p('M13 7 H19'),
    'drawing,dimension,annotation,manufacturing,図面,寸法記入,製造寸法')
add('CAD', 'drawing-leader', 'Leader annotation', '引出線注記', 'drawing-annotation',
    'Attach a text note to drawing geometry with a leader line.', '引出線を使って図面形状に注記を関連付けます。',
    r(4,20,12,8,1,fill=PALE)+accent('M10 23 19 10 H28 M10 18 V23 H15')+p('M18 4 H28 M18 7 H25 M22 13 H28'),
    'drawing,leader,text,note,図面,引出線,注記,文字')
