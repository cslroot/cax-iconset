"""Original model-toolbar glyphs. Distinct action silhouettes, not label-only modes."""
from core import p,r,c,accent,PALE,TEAL
ITEMS=[]
def add(id,en,ja,desc,descja,body,group,aliases=()):
    ITEMS.append(dict(id=id,domain='CAD',name=en,nameJa=ja,description=desc,descriptionJa=descja,
        body=body,family=id,role='command',tags=['toolbar','model',en.lower(),ja],
        aliases=list(aliases),sources=['cax-toolbar-requirements-2026-10-25'],requirementGroup=group))

# Selection eligibility is depicted with a cursor targeting a single topological entity.
def select_cursor():
    return p('M21 19 V30 L24 27 27 30 29 28 26 25 H31Z',fill='white')
add('selection-filter-edge','Select edges only','エッジ選択フィルタ',
    'Restrict picking to topological edges; this is not edge visibility or hidden-line rendering.',
    '選択対象を位相エッジに限定します。エッジの表示・非表示ではありません。',
    p('M4 9 14 4 26 10 V22 L14 28 4 22Z M4 9 14 15 26 10 M14 15 V28')
    +accent('M4 9 14 15',stroke_width=3.5)+select_cursor(),3,['filter.edges','select-edge'])
add('selection-filter-vertex','Select vertices only','頂点選択フィルタ',
    'Restrict picking to topological vertices; not a generic point creation tool.',
    '選択対象を位相頂点に限定します。点を作成するコマンドではありません。',
    p('M4 9 14 4 26 10 V22 L14 28 4 22Z M4 9 14 15 26 10 M14 15 V28')
    +c(14,15,3.5,fill=TEAL,stroke=TEAL)+select_cursor(),3,['filter.vertices','select-vertex'])
add('primitive-box','Create box primitive','直方体プリミティブ',
    'Create a solid rectangular cuboid with three dimensions, not an extrusion or a mesh bounding box.',
    '幅・奥行き・高さを持つソリッド直方体を作成します。押し出しや境界ボックス表示とは区別します。',
    p('M4 10 13 5 28 10 V23 L19 28 4 23Z',fill=PALE)
    +p('M4 10 19 15 28 10 M19 15 V28')+accent('M7 8 13 5 25 9 M28 13 V21'),4,['primitive.box','cuboid'])
add('work-coordinate-system','Set CAD work coordinates','CAD作業座標系',
    'Set the working origin and axes for CAD modeling; independent of machining setup or robot tool frames.',
    'CADモデリングで使用する原点と座標軸を設定します。加工セットアップやロボットのツール座標系とは独立です。',
    p('M3 23 12 17 29 21 20 28Z',fill=PALE)
    +accent('M12 21 V4 M9 7 12 4 15 7 M12 21 H28 M25 18 28 21 25 24 M12 21 4 28 M4 24 V28 H8')
    +c(12,21,2,fill='white'),5,['cad.work-frame','workplane-coordinate-system'])
add('reset-work-coordinate-system','Reset CAD work coordinates','CAD作業座標系をリセット',
    'Restore the CAD working frame to its defined default origin and orientation; does not reset the camera.',
    'CAD作業座標系を既定の原点と向きへ戻します。カメラのリセットではありません。',
    p('M13 24 V13 M13 24 H24 M13 24 7 29 M11 15 13 13 15 15 M22 22 24 24 22 26')
    +accent('M5 17 A12 12 0 1 1 27 22 M5 10 V17 H12'),5,['cad.reset-work-frame'])
add('constraint','Geometric constraints','幾何拘束',
    'Open or apply geometric relations to sketch entities; the icon does not assert a particular constraint type.',
    'スケッチ要素間の幾何拘束を設定します。特定の拘束種別を意味する記号ではありません。',
    p('M4 7 13 12 M19 20 28 25')+c(4,7,2,fill=PALE)+c(28,25,2,fill=PALE)
    +p('M10 15 14 11 Q17 8 20 11 Q23 14 20 17 L17 20 Q14 23 11 20',stroke=TEAL)
    +p('M12 17 15 14 M17 18 20 15'),6,['geometric-constraint','sketch.constraints'])
add('mate','Assembly mates','汎用合致',
    'Create or edit a relation between assembly components without choosing a particular mate type.',
    'アセンブリ部品間の合致関係を設定します。固定や距離などの特定の合致種別を示しません。',
    p('M3 6 10 3 14 6 V17 L10 20 3 17Z M18 15 22 12 29 15 V26 L22 29 18 26Z',fill=PALE)
    +p('M3 6 10 9 14 6 M10 9 V20 M18 15 22 18 29 15 M22 18 V29')
    +accent('M9 24 H16 V9 H23 M20 6 23 9 20 12 M12 21 9 24 12 27'),6,['assembly.mate','generic-mate'])
add('sketch-scale','Scale sketch geometry','スケッチを拡大縮小',
    'Resize selected planar sketch entities about a reference point; not a body scale or view zoom.',
    '基準点を中心にスケッチ要素を拡大縮小します。ボディの拡大縮小や表示のズームではありません。',
    p('M4 28 V7 L25 28Z',stroke_dasharray='2 2')+p('M4 28 V18 L14 28Z',fill=PALE)
    +accent('M15 15 27 3 M20 3 H27 V10')+c(4,28,1.5,fill=TEAL),8,['sketch.scale'])
add('sketch-mirror','Mirror sketch geometry','スケッチミラー',
    'Reflect selected planar sketch entities about a sketch line; not a solid-feature mirror.',
    'スケッチの線を軸に平面要素を反転複製します。ソリッドフィーチャーのミラーとは区別します。',
    p('M16 3 V29',stroke_dasharray='2 3')+p('M4 11 H11 V26 H4Z',fill=PALE)
    +p('M28 11 H21 V26 H28Z',fill=PALE,stroke=TEAL)
    +accent('M5 7 Q16 0 27 7 M23 4 27 7 23 9'),8,['sketch.mirror'])
add('sketch-close-contour','Close sketch contour','輪郭を閉じる',
    'Join the open ends of a sketch contour to form a closed loop, without filling or extruding it.',
    '開いた輪郭の両端をつないで閉ループにします。塗りつぶしや押し出しは行いません。',
    p('M9 5 H5 V27 H27 V5 H23')+c(9,5,2,fill='white')+c(23,5,2,fill='white')
    +accent('M9 5 H23 M13 2 16 5 13 8 M19 2 16 5 19 8'),8,['sketch.close','close-wire'])
add('lattice','Create lattice','格子を作成',
    'Create a spatial network of connected struts or cells; not a screen grid or tessellation overlay.',
    '空間内に連結したストラット・セルの格子構造を作成します。画面グリッドやメッシュ表示ではありません。',
    p('M4 9 16 3 28 9 V23 L16 29 4 23Z M4 9 16 15 28 9 M16 15 V29')
    +accent('M4 9 16 29 28 9 M4 23 16 3 28 23 M4 23 28 23')
    +''.join(c(x,y,1.4,fill=TEAL,stroke=TEAL) for x,y in [(4,9),(16,3),(28,9),(4,23),(16,29),(28,23)]),9,['lattice.create'])
add('lattice-fill','Fill volume with lattice','格子充填',
    'Fill a bounded volume with an internal lattice while retaining its enclosing shape.',
    '境界形状を保ちながら内部の体積を格子構造で充填します。',
    p('M4 10 16 4 28 10 V23 L16 29 4 23Z',fill=PALE)
    +p('M4 10 16 16 28 10 M16 16 V29')
    +accent('M7 13 13 26 M7 22 13 16 M7 17 13 20 M19 16 25 23 M19 25 25 13 M19 20 25 18'),9,['lattice.fill','infill-lattice'])
add('set-face-distance','Set planar face distance','面間距離を設定',
    'Move a selected planar face to a specified separation from a parallel target face; edits geometry, not a measurement or persistent assembly mate.',
    '選択した平面を平行な対象面から指定の距離へ移動して形状を編集します。測定や永続的な合致ではありません。',
    p('M3 11 10 5 V23 L3 29Z M22 9 29 3 V21 L22 27Z',fill=PALE)
    +accent('M7 16 H25 M11 12 7 16 11 20 M21 12 25 16 21 20')
    +p('M13 7 V23',stroke_dasharray='2 2'),10,['face-distance','faceDistance'])
add('stretch-volume','Stretch 3D region','3D範囲ストレッチ',
    'Move faces wholly inside a body-coordinate selection box and stretch faces crossing its boundary; geometry outside the affected region remains fixed.',
    'ボディ座標系の選択ボックス内に完全に入る面を移動し、境界を横切る面を伸縮します。影響範囲外の形状は固定します。',
    p('M3 14 9 10 22 14 V24 L16 28 3 24Z',fill=PALE)+p('M3 14 16 18 22 14 M16 18 V28')
    +p('M14 9 21 5 29 9 V25 L22 29 14 25Z M14 9 22 13 29 9 M22 13 V29',stroke=TEAL,stroke_dasharray='2 2')
    +accent('M14 3 H28 M24 1 28 3 24 5'),10,['3d-stretch','stretch-region'])
add('make-editable','Make geometry editable','編集可能にする・ソース解除',
    'Release an imported source to make its bodies independently editable; source names, layers and drawings are dropped, while Undo can restore them.',
    'インポート元を解除してボディを編集可能にします。ソースの名前・レイヤー・図面は除去され、Undoで復元できます。',
    p('M3 8 H15 V26 H3Z',fill=PALE)+p('M6 12 H11 M6 16 H9')
    +p('M18 7 21 4 Q24 1 27 4 Q30 7 27 10 L24 13 M16 9 13 12 Q10 15 13 18 Q16 21 19 18 L22 15')
    +accent('M13 3 27 21 M19 28 22 22 27 17 30 20 25 25Z M22 22 25 25'),10,['unlink-source','make-independent'])
add('face-normal-condition','Set face-normal condition','法線条件を設定',
    'Set a face-normal direction and a minimum cosine threshold for directional acceptance; not normal-map display, a pressure load, or a geometric mate.',
    '面法線の基準方向と許容範囲を最小コサイン値で設定します。法線表示、圧力荷重、幾何合致とは異なります。',
    p('M3 24 12 19 29 24 20 29Z',fill=PALE)
    +p('M16 24 6 7 Q16 1 26 7Z',fill=PALE,stroke_dasharray='2 2')
    +accent('M16 24 V4 M12 8 16 4 20 8 M11 16 Q16 12 21 16')
    +c(16,24,1.5,fill=TEAL,stroke=TEAL),15,['face-normal-condition','minimum-cosine'])
