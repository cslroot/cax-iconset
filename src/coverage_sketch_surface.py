"""Original semantic geometry for the reviewed sketch and surface coverage gaps.

Each command is drawn on the existing 32 px grid, using the shared 1.75 px
rounded stroke and palette. Vendor documentation informs meaning, not artwork.
Input methods, target spline representations and related mode labels share one
semantic glyph. Aliases and source IDs below are preserved from the frozen audit.
"""
from core import p, r, c, g, accent, fill, nodes, PALE, TEAL, INK, AMBER

_AUDIT = {'accessibility-analysis': {'aliases': ['inspect.accessibility'],
                            'sources': ['gui-audit-aad95a4813']},
 'apply-decal': {'aliases': ['canvas.decal'], 'sources': ['gui-audit-cf394eb201']},
 'canvas-calibrate': {'aliases': ['canvas.calibrate'], 'sources': ['gui-audit-770ce672d7']},
 'canvas-insert': {'aliases': ['canvas.insert', 'Sketch Picture'],
                   'sources': ['gui-audit-cf394eb201', 'gui-audit-5952aec4b6']},
 'constraint-regular-polygon': {'aliases': ['sketch.constraint.polygon'],
                                'sources': ['gui-audit-27d4ba3bf3']},
 'convert-spline-representation': {'aliases': ['Convert to Spline',
                                               'Convert to Style Spline',
                                               'Convert to Generic Spline'],
                                   'sources': ['gui-audit-318833252a']},
 'curve-offset-on-surface': {'aliases': ['Offset On Surface'], 'sources': ['gui-audit-5952aec4b6']},
 'curve-reverse-tangent': {'aliases': ['Reverse Endpoint Tangent', 'Flip Endpoint Tangent'],
                           'sources': ['gui-audit-5952aec4b6']},
 'dimension-driven': {'aliases': ['sketch.toggle_driven', 'Sketch Dimension Driven'],
                      'sources': ['gui-audit-4023a9e23d', 'gui-audit-5952aec4b6']},
 'edit-block-definition': {'aliases': ['Edit Block'], 'sources': ['gui-audit-1bed7f8e51']},
 'environment-map-analysis': {'aliases': ['inspect.environment_map'],
                              'sources': ['gui-audit-aad95a4813']},
 'intersection-curve': {'aliases': ['sketch.intersection_curve', 'Intersection Curve'],
                        'sources': ['gui-audit-3762e45220', 'gui-audit-5952aec4b6']},
 'sketch-arc-slot': {'aliases': ['sketch.slot.arc_three_point',
                                 'sketch.slot.arc_center',
                                 '3 Point Arc Slot',
                                 'Centerpoint Arc Slot'],
                     'sources': ['gui-audit-3762e45220', 'gui-audit-5952aec4b6']},
 'sketch-blend-curve': {'aliases': ['sketch.blend_curve'], 'sources': ['gui-audit-f00a42accf']},
 'sketch-conic': {'aliases': ['sketch.conic', 'Parabola', 'Conic'],
                  'sources': ['gui-audit-3762e45220', 'gui-audit-5952aec4b6']},
 'sketch-detach-on-drag': {'aliases': ['Detach Segment On Drag'],
                           'sources': ['gui-audit-5952aec4b6']},
 'sketch-divide': {'aliases': ['Segment'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-edit': {'aliases': ['sketch.edit'], 'sources': ['gui-audit-4023a9e23d']},
 'sketch-equation-curve': {'aliases': ['Equation Driven Curve'],
                           'sources': ['gui-audit-5952aec4b6']},
 'sketch-fit-section-curves': {'aliases': ['sketch.fit_curves_to_section'],
                               'sources': ['gui-audit-3762e45220']},
 'sketch-infinite-line': {'aliases': ['sketch.infinite'], 'sources': ['gui-audit-4023a9e23d']},
 'sketch-instant-edit': {'aliases': ['Instant2D'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-intersect': {'aliases': ['sketch.intersect'], 'sources': ['gui-audit-3762e45220']},
 'sketch-loose-ends': {'aliases': ['sketch.loose_ends'], 'sources': ['gui-audit-4023a9e23d']},
 'sketch-make-path': {'aliases': ['Make Path'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-move': {'aliases': ['sketch.move', 'Move Entities'],
                 'sources': ['gui-audit-f00a42accf', 'gui-audit-5952aec4b6']},
 'sketch-no-solve-move': {'aliases': ['No Solve Move'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-parallelogram': {'aliases': ['Parallelogram'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-partial-ellipse': {'aliases': ['Partial Ellipse'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-pen-input': {'aliases': ['Insert Pen Sketch'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-point': {'aliases': ['sketch.point', 'sketch.point3d', 'Point'],
                  'sources': ['gui-audit-4023a9e23d',
                              'gui-audit-3762e45220',
                              'gui-audit-5952aec4b6']},
 'sketch-project-to-surface': {'aliases': ['sketch.project_to_surface'],
                               'sources': ['gui-audit-3762e45220']},
 'sketch-redefine-plane': {'aliases': ['sketch.redefine'], 'sources': ['gui-audit-4023a9e23d']},
 'sketch-repair-reference': {'aliases': ['Auto Repair Sketch Relation or Dimension'],
                             'sources': ['gui-audit-5952aec4b6']},
 'sketch-rotate': {'aliases': ['Rotate Entities'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-rounded-rectangle': {'aliases': ['sketch.rectangle.rounded'],
                              'sources': ['gui-audit-3762e45220']},
 'sketch-shaded-contours': {'aliases': ['Shaded Sketch Contours'],
                            'sources': ['gui-audit-5952aec4b6']},
 'sketch-slicing': {'aliases': ['Slicing'], 'sources': ['gui-audit-5952aec4b6']},
 'sketch-spline-on-surface': {'aliases': ['Spline on Surface'],
                              'sources': ['gui-audit-5952aec4b6']},
 'sketch-split': {'aliases': ['sketch.break', 'Split Entities'],
                  'sources': ['gui-audit-f00a42accf', 'gui-audit-5952aec4b6']},
 'sketch-spun-profile': {'aliases': ['sketch.spun_profile'], 'sources': ['gui-audit-3762e45220']},
 'sketch-stretch': {'aliases': ['Stretch Entities'], 'sources': ['gui-audit-5952aec4b6']},
 'surface-aging': {'aliases': ['render.aging.describe'], 'sources': ['gui-audit-43d4d0f047']},
 'surface-extrude': {'aliases': ['surface.extrude', 'Extruded Surface'],
                     'sources': ['gui-audit-64d1c36155', 'gui-audit-f42456e152']},
 'surface-fair': {'aliases': ['surface.fair'], 'sources': ['gui-audit-efdc5a5641']},
 'surface-flatten': {'aliases': ['Surface Flatten'], 'sources': ['gui-audit-f42456e152']},
 'surface-loft': {'aliases': ['surface.loft', 'Lofted Surface'],
                  'sources': ['gui-audit-64d1c36155', 'gui-audit-f42456e152']},
 'surface-mid': {'aliases': ['Mid-Surface'], 'sources': ['gui-audit-f42456e152']},
 'surface-revolve': {'aliases': ['surface.revolve', 'Revolved Surface'],
                     'sources': ['gui-audit-64d1c36155', 'gui-audit-f42456e152']},
 'surface-sweep': {'aliases': ['surface.sweep', 'Swept Surface'],
                   'sources': ['gui-audit-64d1c36155', 'gui-audit-f42456e152']}}

ITEMS = []

def add(id, name, name_ja, family, description, description_ja, body, tags):
    evidence = _AUDIT[id]
    ITEMS.append(dict(
        id=id, domain='CAD', name=name, nameJa=name_ja,
        description=description, descriptionJa=description_ja,
        family=family, role='command',
        tags=list(dict.fromkeys(tags + [name.lower(), name_ja, 'CAD'])),
        aliases=list(evidence['aliases']), sources=list(evidence['sources']), body=body,
    ))

# Approach rays terminate on either the exposed pocket floor or an overhang.
add('accessibility-analysis', 'Analyze tool accessibility', '工具アクセス解析', 'inspection',
    'Inspect whether model surfaces can be reached along a tool approach direction.',
    '工具の進入方向に沿ってモデルの各面へアクセスできるかを検査します。',
    fill('M3 12 H12 V17 H7 V25 H25 V17 H29 V29 H3Z')
    + accent('M20 3 V23 M17 19 20 23 23 19')
    + p('M7 3 V10 M4 7 7 10 10 7', stroke=AMBER)
    + p('M4 15 H11', stroke=AMBER),
    ['inspection', 'accessibility', 'approach direction', 'tool access', '検査', '工具進入', '到達可否'])

# A small image is applied on, not cut into, the bowed face.
add('apply-decal', 'Apply decal', 'デカール貼付', 'appearance',
    'Place an image decal on a model face without modifying its geometry.',
    'モデルの形状を変更せずに、画像デカールを面へ貼り付けます。',
    fill('M4 13 Q16 7 28 13 V27 Q16 21 4 27Z')
    + p('M11 14 23 15 V24 L11 23Z', fill='white')
    + accent('M12 21 16 17 19 21 21 19 23 22')
    + c(21, 17, 1, fill=TEAL, stroke='none')
    + accent('M5 4 H14 Q19 4 19 9 M16 6 19 9 22 6'),
    ['decal', 'image', 'face', 'appearance', 'デカール', '画像', '面', '外観'])

# The image is calibrated between two picked points, rather than merely measured.
add('canvas-calibrate', 'Calibrate reference image', '参照画像の尺度校正', 'reference-image',
    'Set the physical scale of a reference image from a known distance between two image points.',
    '画像上の2点間の既知の距離を使い、参照画像の実寸尺度を校正します。',
    r(4, 4, 24, 18, 1, fill=PALE)
    + p('M5 19 11 10 17 17 21 13 27 20')
    + c(23, 8, 1.5, fill=TEAL, stroke='none')
    + p('M7 22 V29 M25 22 V29')
    + accent('M7 26 H25 M10 23 7 26 10 29 M22 23 25 26 22 29')
    + c(7, 22, 1.5, fill=TEAL) + c(25, 22, 1.5, fill=TEAL),
    ['canvas', 'calibrate', 'known distance', 'image scale', '参照画像', '尺度', '校正', '既知寸法'])

add('canvas-insert', 'Insert reference image', '参照画像を挿入', 'reference-image',
    'Insert a raster image as a sketch picture or reference canvas without tracing it into curves.',
    'ラスター画像を曲線に変換せず、スケッチ画像または参照キャンバスとして挿入します。',
    p('M3 23 13 18 29 24 19 29Z', fill=PALE)
    + r(5, 3, 18, 15, 1, fill='white')
    + accent('M6 15 11 9 15 13 18 10 22 16')
    + c(18, 6.5, 1.3, fill=TEAL, stroke='none')
    + accent('M26 10 V21 M23 18 26 21 29 18'),
    ['canvas', 'insert', 'raster', 'sketch picture', '参照画像', '挿入', 'キャンバス', 'スケッチ画像'])

# A polygon with a central equality relation communicates constraint, not creation.
add('constraint-regular-polygon', 'Constrain regular polygon', '正多角形拘束', 'sketch-constraint',
    'Constrain a polygon chain to equal side lengths and a common circumscribed circle.',
    '多角形を構成する辺を等長にし、各頂点が同一円上に並ぶよう拘束します。',
    p('M16 4 26.4 10 V22 L16 28 5.6 22 V10Z', fill=PALE)
    + accent('M11 13 H21 M11 19 H21')
    + c(16, 4, 1.5, fill=TEAL, stroke=TEAL)
    + c(16, 28, 1.5, fill=TEAL, stroke=TEAL),
    ['constraint', 'regular polygon', 'equal sides', 'cocircular', '拘束', '正多角形', '等辺', '共円'])

add('convert-spline-representation', 'Convert spline representation', 'スプライン形式変換', 'curve-editing',
    'Convert an existing curve between spline representations without creating separate commands for each target type.',
    '既存曲線のスプライン表現を変換します。変換先の形式ごとに図記号を分割しません。',
    p('M4 25 9 6 23 25 28 8', stroke_dasharray='2 3')
    + accent('M4 25 C8 2 24 31 28 8')
    + r(7.5, 4.5, 3, 3, 0, fill='white')
    + r(21.5, 23.5, 3, 3, 0, fill='white')
    + nodes([(4, 25), (28, 8)])
    + accent('M13 4 H23 M20 1 23 4 20 7'),
    ['spline', 'convert', 'representation', 'style spline', 'generic spline', 'スプライン', '形式変換', '制御点'])

add('curve-offset-on-surface', 'Offset curve on surface', '面上の曲線オフセット', 'curve-on-surface',
    'Create a parallel offset of an existing curve while keeping the result on its support surface.',
    '既存曲線から離れた曲線を、同じ支持サーフェス上に作成します。',
    fill('M3 10 Q16 3 29 10 L26 28 Q14 21 3 28Z')
    + p('M6 16 Q14 9 26 16')
    + accent('M6 23 Q14 16 26 23')
    + accent('M16 12 V20 M13 15 16 12 19 15 M13 17 16 20 19 17'),
    ['curve', 'offset', 'support surface', 'parallel', '曲線', 'オフセット', '面上', '支持面'])

add('curve-reverse-tangent', 'Reverse endpoint tangent', '端点の接線方向を反転', 'curve-editing',
    'Reverse or flip an endpoint tangent direction while retaining the connected curve context.',
    '接続する曲線との関係を保ちながら、端点の接線方向を反転します。',
    p('M3 16 H15 M15 16 C24 16 25 5 28 5', stroke_dasharray='2 3')
    + p('M3 16 H15')
    + accent('M15 16 C6 16 6 27 15 27')
    + c(15, 16, 2, fill=PALE, stroke=TEAL)
    + accent('M25 11 Q31 16 25 21 M25 17 V21 H29'),
    ['tangent', 'endpoint', 'reverse', 'flip', '接線', '端点', '反転', '曲線'])

# Parenthesized dimension arrows are the conventional reference-dimension cue.
add('dimension-driven', 'Set driven dimension', '従動寸法に切替', 'sketch-dimension',
    'Mark a dimension as driven or reference-only so that it reports rather than controls sketch geometry.',
    'スケッチ形状を駆動せず、値を参照表示する従動寸法に切り替えます。',
    p('M7 20 V28 M25 20 V28 M7 25 H25')
    + accent('M9 10 H23 M12 7 9 10 12 13 M20 7 23 10 20 13')
    + p('M5 5 Q1 10 5 15 M27 5 Q31 10 27 15')
    + p('M7 16 V20 M25 16 V20', stroke_dasharray='2 3'),
    ['dimension', 'driven', 'reference', 'parenthesized', '寸法', '従動', '参照寸法', '駆動しない'])

add('edit-block-definition', 'Edit block definition', 'ブロック定義を編集', 'block-editing',
    'Enter a reusable block definition to edit its member geometry.',
    '再利用するブロックの定義を開き、構成する図形を編集します。',
    r(3, 7, 23, 22, 1, stroke_dasharray='3 3')
    + p('M7 24 V13 H15 V24Z', fill=PALE)
    + c(19, 23, 3, fill=PALE)
    + p('M16 15 25 4 29 7 20 18 15 20Z', fill='white')
    + accent('M16 15 20 18 M23 7 27 10'),
    ['block', 'definition', 'edit', 'member geometry', 'ブロック', '定義', '編集', '構成図形'])

# A broad warped window reflection distinguishes this from zebra stripes/render.
add('environment-map-analysis', 'Analyze environment reflections', '環境マップ反射解析', 'inspection',
    'Inspect surface shape and continuity using reflections of an environment map.',
    '環境マップの反射を利用して、面の形状と連続性を検査します。',
    p('M3 10 V3 H10 M22 3 H29 V10 M3 22 V29 H10 M22 29 H29 V22')
    + c(16, 16, 11, fill=PALE)
    + p('M9 9 Q16 5 23 10 L21 22 Q14 17 8 21Z', fill='white')
    + accent('M16 7 Q13 14 14 19 M8 15 Q15 10 22 15'),
    ['inspection', 'environment map', 'reflection', 'surface continuity', '検査', '環境マップ', '反射', '面連続性'])

add('intersection-curve', 'Create intersection curve', '交差曲線を作成', 'curve-on-surface',
    'Create a spatial curve where two faces or surfaces intersect.',
    '2つの面またはサーフェスが交差する位置に空間曲線を作成します。',
    fill('M3 13 Q16 5 29 13 L25 26 Q14 18 3 26Z')
    + p('M13 3 21 7 V29 L13 25Z', fill='white')
    + p('M3 13 Q16 5 29 13', stroke_dasharray='2 3')
    + accent('M13 9 C19 10 15 19 21 24')
    + nodes([(13, 9), (21, 24)]),
    ['intersection', 'curve', 'two surfaces', '3D curve', '交差', '曲線', '面同士', '空間曲線'])

add('sketch-arc-slot', 'Sketch arc slot', 'スケッチ円弧スロット', 'sketch',
    'Create a curved slot bounded by concentric arcs and rounded ends.',
    '同心円弧と丸い端部で囲まれた円弧状のスロットを作成します。',
    fill('M5 23 A19 19 0 0 1 24 4 A4 4 0 0 1 24 12 A11 11 0 0 0 13 23 A4 4 0 0 1 5 23Z')
    + accent('M9 23 A15 15 0 0 1 24 8', stroke_dasharray='2 3')
    + c(9, 23, 1.5, fill=TEAL, stroke='none')
    + c(13.4, 12.4, 1.5, fill=TEAL, stroke='none')
    + c(24, 8, 1.5, fill=TEAL, stroke='none'),
    ['sketch', 'arc slot', 'curved slot', 'three point', 'スケッチ', '円弧スロット', '曲線長穴', '3点'])

add('sketch-blend-curve', 'Create blend curve', 'ブレンド曲線を作成', 'curve-modeling',
    'Add a transition curve between existing curve ends with continuity control.',
    '既存曲線の端点間に、連続性を指定した遷移曲線を追加します。',
    p('M3 27 8 20 M24 8 H29')
    + p('M8 20 15 10 M16 8 H24', stroke_dasharray='2 3')
    + accent('M8 20 C14 11 16 8 24 8')
    + nodes([(8, 20), (24, 8)])
    + p('M3 20 7 23 M25 5 V11', stroke=TEAL),
    ['blend', 'curve', 'transition', 'continuity', 'ブレンド', '曲線', '遷移', '連続性'])

add('sketch-conic', 'Sketch conic', 'スケッチ円錐曲線', 'sketch',
    'Create a conic segment from its endpoints, apex and shape control.',
    '両端点、頂点、および形状制御値から円錐曲線の区間を作成します。',
    p('M4 27 16 4 28 27 M16 4 V27', stroke_dasharray='2 3')
    + accent('M4 27 Q16 2 28 27')
    + nodes([(4, 27), (16, 4), (28, 27)])
    + r(14, 12.5, 4, 4, 0, fill=PALE, stroke=TEAL),
    ['conic', 'rho', 'apex', 'curve', '円錐曲線', '頂点', '形状制御', 'スケッチ'])

add('sketch-detach-on-drag', 'Detach segment on drag', 'ドラッグ時に線分を分離', 'sketch-editing',
    'Allow a dragged segment endpoint to separate from adjoining sketch geometry.',
    '線分をドラッグするとき、端点を隣接するスケッチ図形から分離できるようにします。',
    p('M4 25 H13 M13 25 V5', stroke_dasharray='2 3')
    + p('M4 25 H13')
    + accent('M23 5 V17')
    + c(13, 25, 2, fill='white', stroke=AMBER)
    + c(23, 17, 2, fill=PALE, stroke=TEAL)
    + accent('M17 24 27 21 M23 19 27 21 25 25'),
    ['drag', 'detach', 'endpoint', 'segment', 'ドラッグ', '分離', '端点', '線分'])

add('sketch-divide', 'Divide sketch entity', 'スケッチ要素を等分', 'sketch-editing',
    'Partition a sketch entity into evenly spaced segments or division points.',
    'スケッチ要素を等間隔の区間または分割点に分けます。',
    accent('M4 25 Q16 1 28 25')
    + nodes([(4, 25), (8.7, 17.4), (16, 13), (23.3, 17.4), (28, 25)])
    + p('M4 14 8.7 17.4 M16 6 V13 M28 14 23.3 17.4'),
    ['divide', 'segment', 'equal spacing', 'division points', '分割', '等分', '等間隔', '分割点'])

add('sketch-edit', 'Edit sketch', 'スケッチを編集', 'sketch-editing',
    'Enter an existing sketch to edit its geometry and constraints.',
    '既存のスケッチを開き、図形と拘束を編集します。',
    fill('M3 21 12 12 28 18 19 28Z')
    + p('M9 22 13 17 20 20 16 25Z')
    + p('M14 14 24 3 28 7 18 18 13 20Z', fill='white')
    + accent('M14 14 18 18 M22 5 26 9'),
    ['sketch', 'edit', 'geometry', 'constraints', 'スケッチ', '編集', '図形', '拘束'])

# A small function/equality mark accompanies the dominant plotted curve.
add('sketch-equation-curve', 'Create equation-driven curve', '数式駆動曲線を作成', 'curve-modeling',
    'Construct a curve by evaluating an explicit or parametric equation.',
    '明示式または媒介変数式を評価して曲線を作成します。',
    p('M5 15 V27 H29 M5 11 V6 Q5 2 9 3 M3 7 H10 M13 5 H18 M13 9 H18')
    + accent('M8 24 C18 26 22 19 26 5')
    + c(8, 24, 1.5, fill=TEAL, stroke='none')
    + c(26, 5, 1.5, fill=TEAL, stroke='none'),
    ['equation', 'parametric curve', 'function', 'plot', '数式', '媒介変数', '曲線', '関数'])

add('sketch-fit-section-curves', 'Fit curves to mesh section', 'メッシュ断面に曲線を近似', 'mesh-section',
    'Fit sketch lines or curves to the section of a mesh.',
    'メッシュの断面形状にスケッチの線分や曲線をフィットさせます。',
    p('M3 8 13 4 16 24 4 27Z M3 8 16 24 M13 4 4 27 M3 17 15 13')
    + p('M2 19 16 15', stroke=AMBER)
    + accent('M21 26 C18 12 25 24 28 6')
    + accent('M13 28 H21 M18 25 21 28 18 31'),
    ['mesh', 'section', 'fit curves', 'sketch', 'メッシュ', '断面', '曲線近似', 'スケッチ'])

add('sketch-infinite-line', 'Sketch infinite line', 'スケッチ無限直線', 'sketch',
    'Create a construction line that extends without finite endpoints in both directions.',
    '両方向に有限の端点を持たず延びる補助直線を作成します。',
    p('M4 6 V3 H11 M21 29 H28 V22', stroke_dasharray='2 3')
    + accent('M3 28 29 2', stroke_dasharray='5 3')
    + accent('M3 22 V28 H9 M23 2 H29 V8')
    + p('M13 13 19 19'),
    ['infinite line', 'construction', 'unbounded', 'both directions', '無限直線', '補助線', '無限', '両方向'])

add('sketch-instant-edit', 'Direct-edit sketch dimensions', 'スケッチ寸法の直接編集', 'sketch-editing',
    'Interactively change sketch dimensions or drag dimension handles for direct editing.',
    '寸法値や寸法ハンドルを直接操作して、スケッチ形状を編集します。',
    p('M4 13 H20 V27 H4Z', fill=PALE)
    + p('M4 5 H20 M4 3 V8 M20 3 V8')
    + accent('M9 3 6 5 9 7 M15 3 18 5 15 7')
    + r(18, 11, 4, 4, 0, fill=TEAL, stroke=TEAL)
    + accent('M24 13 H30 M27 10 30 13 27 16')
    + p('M24 21 29 25 26 26 25 29Z', fill='white'),
    ['instant2d', 'dimension handles', 'direct edit', 'drag', '寸法ハンドル', '直接編集', 'ドラッグ', 'スケッチ'])

# A solid crosses a plane, and its resulting planar contour is highlighted.
add('sketch-intersect', 'Intersect geometry with sketch plane', 'スケッチ平面との交線を作成', 'sketch-reference',
    'Create sketch geometry at the intersection of a body and the active sketch plane.',
    'ボディと作業中のスケッチ平面が交差する位置にスケッチ図形を作成します。',
    p('M10 7 18 3 25 7 V24 L18 28 10 24Z M10 7 18 11 25 7 M18 11 V28')
    + fill('M3 18 20 9 29 15 12 24Z')
    + accent('M10 15 18 11 25 15 18 19Z')
    + p('M10 19 V24 L18 28 25 24 V19', stroke_dasharray='2 3'),
    ['intersect', 'sketch plane', 'body section', 'section curve', '交線', 'スケッチ平面', '断面', 'ボディ'])

add('sketch-loose-ends', 'Find loose sketch ends', '未接続のスケッチ端点を検出', 'sketch-diagnostics',
    'Locate open or unconnected endpoints in sketch geometry.',
    'スケッチ図形の開いた端点や未接続の端点を探します。',
    p('M17 6 H5 V27 H27 V16')
    + c(17, 6, 2.5, fill=PALE, stroke=AMBER)
    + c(27, 16, 2.5, fill=PALE, stroke=AMBER)
    + p('M23 4 21 7 M29 8 26 10 M30 13 H27', stroke=AMBER),
    ['loose ends', 'open contour', 'unconnected', 'diagnostic', '未接続端点', '開いた輪郭', '検出', '診断'])

add('sketch-make-path', 'Make sketch path', 'スケッチパスを作成', 'sketch-editing',
    'Combine end-connected sketch segments into a continuous path chain.',
    '端点で接続したスケッチ要素を、連続したパスの連鎖としてまとめます。',
    p('M4 27 10 17')
    + accent('M10 17 C15 8 19 7 24 12')
    + p('M24 12 29 18')
    + c(10, 17, 2.2, fill=PALE, stroke=TEAL)
    + c(24, 12, 2.2, fill=PALE, stroke=TEAL)
    + accent('M12 5 Q20 1 26 6 M22 6 H26 V2'),
    ['path', 'chain', 'connected segments', 'continuous', 'パス', '連鎖', '接続要素', '連続'])

add('sketch-move', 'Move or copy sketch entities', 'スケッチ要素を移動・複製', 'sketch-transform',
    'Translate selected planar sketch entities, optionally leaving copies in place.',
    '選択した平面スケッチ要素を移動します。元の位置に複製を残すこともできます。',
    p('M3 18 H14 V28 H3Z', stroke_dasharray='2 3')
    + p('M18 4 H28 V14 H18Z', fill=PALE)
    + accent('M8 15 17 6 M12 6 H17 V11')
    + accent('M15 23 H27 M23 19 27 23 23 27'),
    ['move', 'copy', 'translate', 'sketch entities', '移動', '複製', '並進', 'スケッチ要素'])

# Geometry moves while the old right-angle relation is crossed out in-place.
add('sketch-no-solve-move', 'Move sketch without solving', '拘束計算なしでスケッチを移動', 'sketch-transform',
    'Move sketch geometry in a mode that bypasses constraint solving.',
    '拘束ソルバーによる計算を省略するモードで、スケッチ図形を移動します。',
    p('M4 26 H28 M8 26 V5', stroke_dasharray='2 3')
    + p('M4 26 H28')
    + accent('M8 26 21 6')
    + nodes([(8, 26), (21, 6)])
    + p('M8 20 H14 V26 M6 27 16 18', stroke=AMBER)
    + accent('M9 5 H17 M14 2 17 5 14 8'),
    ['no solve', 'move', 'bypass constraints', 'solver', '拘束計算なし', '移動', '拘束', 'ソルバー'])

add('sketch-parallelogram', 'Sketch parallelogram', 'スケッチ平行四辺形', 'sketch',
    'Create an oblique quadrilateral with both pairs of opposite sides parallel.',
    '向かい合う2組の辺が平行な、斜めの四角形を作成します。',
    fill('M4 26 11 6 H28 L21 26Z')
    + accent('M15 3 15 9 M18 23 V29 M5 15 11 17 M22 15 28 17')
    + p('M11 6 21 26', stroke_dasharray='2 3'),
    ['parallelogram', 'oblique', 'parallel sides', 'quadrilateral', '平行四辺形', '斜辺', '平行', '四角形'])

add('sketch-partial-ellipse', 'Sketch elliptic arc', 'スケッチ部分楕円', 'sketch',
    'Create an open arc of an ellipse between two endpoints.',
    '楕円の一部を、2つの端点を持つ開いた曲線として作成します。',
    p('M3 16 H29 M16 5 V27', stroke_dasharray='2 3')
    + accent('M27.3 12.9 A12 8 0 1 0 16 24')
    + nodes([(27.3, 12.9), (16, 24)])
    + c(16, 16, 1.3, fill=TEAL, stroke='none'),
    ['ellipse', 'partial ellipse', 'elliptic arc', 'open curve', '楕円', '部分楕円', '楕円弧', '開曲線'])

add('sketch-pen-input', 'Insert pen sketch', 'ペンスケッチを挿入', 'sketch-input',
    'Capture freehand pen or stylus strokes as sketch input.',
    'ペンやスタイラスによる自由な筆跡をスケッチ入力として取り込みます。',
    accent('M3 22 C3 12 12 13 10 21 C8 30 14 29 17 23')
    + p('M15 18 25 4 29 7 19 21 14 23Z', fill=PALE)
    + p('M15 18 19 21 M23 7 27 10')
    + accent('M14 23 17 18'),
    ['pen', 'stylus', 'freehand', 'stroke input', 'ペン', 'スタイラス', 'フリーハンド', '筆跡'])

add('sketch-point', 'Create sketch point', 'スケッチ点を作成', 'sketch',
    'Place a geometric point in the active sketch.',
    '作業中のスケッチに幾何学的な点を配置します。',
    p('M3 22 H25 M11 30 V7', stroke_dasharray='2 3')
    + c(11, 22, 3, fill=TEAL, stroke=TEAL)
    + p('M19 3 27 11 22 12 21 17Z', fill=PALE)
    + accent('M16 17 20 13'),
    ['point', 'create', 'sketch', 'position', '点', '作成', 'スケッチ', '位置'])

# Ghost projection rays link an off-surface profile to a curved target face.
add('sketch-project-to-surface', 'Project curve to surface', '曲線をサーフェスに投影', 'curve-on-surface',
    'Project existing sketch curves onto a selected curved surface.',
    '既存のスケッチ曲線を選択した曲面へ投影します。',
    p('M5 4 15 3 11 10Z')
    + p('M5 4 8 20 M15 3 23 19 M11 10 17 26', stroke_dasharray='2 3')
    + fill('M3 18 Q16 10 29 18 L27 29 Q14 21 4 29Z')
    + accent('M8 20 Q16 16 23 19 L17 26 Q12 22 8 20Z')
    + accent('M26 4 V12 M23 9 26 12 29 9'),
    ['project', 'curve', 'curved surface', 'projection rays', '投影', '曲線', '曲面', '投影線'])

add('sketch-redefine-plane', 'Redefine sketch plane', 'スケッチ平面を再定義', 'sketch-reference',
    'Reattach an existing sketch to another support plane while retaining its sketch definition.',
    'スケッチの定義を保持したまま、支持平面を別の平面へ変更します。',
    p('M3 6 12 3 V18 L3 21Z', stroke_dasharray='2 3')
    + p('M6 10 10 8 V15 L6 17Z')
    + fill('M9 24 20 18 29 23 18 29Z')
    + accent('M14 24 20 21 24 23 18 26Z')
    + accent('M17 5 Q27 4 26 16 M23 12 26 16 29 13'),
    ['sketch plane', 'redefine', 'reattach', 'support', 'スケッチ平面', '再定義', '再配置', '支持平面'])

add('sketch-repair-reference', 'Repair sketch references', 'スケッチ参照を修復', 'sketch-diagnostics',
    'Find replacement references for dangling sketch relations or dimensions.',
    '参照が切れたスケッチ拘束や寸法について、代わりの参照先を見つけて修復します。',
    p('M6 5 V28 M6 9 H26 M9 6 6 9 9 12 M23 6 26 9 23 12')
    + p('M26 5 V17 M6 25 H26', stroke_dasharray='2 3')
    + c(26, 25, 2.2, stroke=AMBER, stroke_dasharray='1 2')
    + p('M6 25 H19')
    + c(19, 25, 2, fill=PALE, stroke=TEAL)
    + accent('M26 17 Q26 21 21 24 M22 20 21 24 25 25'),
    ['repair', 'dangling reference', 'dimension', 'relation', '修復', '参照切れ', '寸法', '拘束'])

add('sketch-rotate', 'Rotate sketch entities', 'スケッチ要素を回転', 'sketch-transform',
    'Rotate planar sketch entities about a selected center.',
    '選択した中心のまわりで、平面スケッチ要素を回転します。',
    p('M3 18 11 27 H3Z', stroke_dasharray='2 3')
    + p('M19 9 H28 V17Z', fill=PALE)
    + p('M16 25 7 22 M16 25 25 13', stroke_dasharray='2 3')
    + c(16, 25, 2, fill=TEAL, stroke=TEAL)
    + accent('M4 12 C9 2 21 2 27 6 M23 6 H27 V2'),
    ['rotate', 'sketch entities', 'center', 'angle', '回転', 'スケッチ要素', '中心', '角度'])

add('sketch-rounded-rectangle', 'Sketch rounded rectangle', 'スケッチ角丸長方形', 'sketch',
    'Create a complete rectangular profile with four rounded corners.',
    '4つの角に丸みを持つ長方形の閉じた輪郭を作成します。',
    r(4, 6, 24, 21, 7, fill=PALE)
    + accent('M21 6 A7 7 0 0 1 28 13 M21 13 26 8')
    + c(21, 13, 1.4, fill=TEAL, stroke='none')
    + p('M4 13 V6 H11', stroke_dasharray='2 3'),
    ['rounded rectangle', 'corner radius', 'four corners', 'profile', '角丸長方形', 'コーナー半径', '四隅', '輪郭'])

add('sketch-shaded-contours', 'Display shaded sketch contours', 'スケッチ輪郭をシェーディング', 'sketch-display',
    'Toggle filled display of closed sketch regions without creating hatch geometry.',
    'ハッチング図形を作成せずに、閉じたスケッチ領域の塗りつぶし表示を切り替えます。',
    fill('M4 5 H21 V13 H28 V28 H4Z')
    + r(9, 11, 7, 11, 1, fill='white')
    + accent('M21 13 H28 V28 H4')
    + p('M24 4 H29 V9'),
    ['shaded contours', 'filled regions', 'display', 'closed sketch', 'シェーディング', '塗りつぶし', '表示', '閉じた輪郭'])

add('sketch-slicing', 'Create section slices', '複数の断面スケッチを作成', 'sketch-reference',
    'Create multiple sketch sections where parallel slicing planes intersect model geometry.',
    '平行な切断平面とモデルの交差から、複数の断面スケッチを作成します。',
    p('M8 5 Q16 1 24 5 V27 Q16 31 8 27Z', fill=PALE)
    + p('M8 5 Q16 9 24 5')
    + accent('M3 11 Q16 4 29 11 Q16 18 3 11Z')
    + accent('M3 18 Q16 11 29 18 Q16 25 3 18Z')
    + accent('M3 25 Q16 18 29 25 Q16 32 3 25Z'),
    ['slicing', 'multiple sections', 'parallel planes', 'sketches', 'スライス', '複数断面', '平行平面', 'スケッチ'])

add('sketch-spline-on-surface', 'Draw spline on surface', '面上スプラインを作成', 'curve-on-surface',
    'Create a spline directly on a selected support surface.',
    '選択した支持サーフェス上に直接スプラインを作成します。',
    fill('M3 10 Q16 3 29 10 L26 28 Q14 21 3 28Z')
    + accent('M6 23 C8 7 23 30 26 13')
    + c(6, 23, 1.7, fill='white', stroke=TEAL)
    + c(16, 18.5, 1.7, fill='white', stroke=TEAL)
    + c(26, 13, 1.7, fill='white', stroke=TEAL),
    ['spline', 'surface', 'on-surface curve', 'create', 'スプライン', '面上', '支持面', '作成'])

# Both portions survive the split; there is no discarded trim interval.
add('sketch-split', 'Split sketch entity', 'スケッチ要素を分割', 'sketch-editing',
    'Break a sketch curve at a selected location while retaining both resulting portions.',
    '選択位置でスケッチ曲線を分割し、分割後の両方の区間を残します。',
    p('M3 25 C4 10 9 10 14 14')
    + accent('M18 18 C23 23 28 21 29 7')
    + c(14, 14, 1.8, fill='white')
    + c(18, 18, 1.8, fill=PALE, stroke=TEAL)
    + p('M20 7 11 25', stroke=AMBER, stroke_dasharray='2 3'),
    ['split', 'break', 'retain both sides', 'curve portions', '分割', '切断', '両側を保持', '曲線区間'])

add('sketch-spun-profile', 'Extract spun profile', '回転包絡輪郭を抽出', 'sketch-reference',
    'Derive the silhouette profile of a body swept around a selected axis.',
    '選択した軸のまわりにボディを回したときの包絡輪郭を抽出します。',
    p('M16 2 V30', stroke_dasharray='2 3')
    + p('M10 6 H18 L22 12 19 17 21 23 H10Z', fill=PALE)
    + accent('M7 6 V10 L4 13 7 18 V23 M25 6 V10 L28 13 25 18 V23')
    + accent('M6 26 Q16 33 26 26 M22 26 H26 V30'),
    ['spun profile', 'silhouette', 'rotational envelope', 'axis', '回転輪郭', 'シルエット', '回転包絡', '軸'])

add('sketch-stretch', 'Stretch sketch entities', 'スケッチ要素をストレッチ', 'sketch-transform',
    'Move selected portions of sketch geometry while keeping unselected endpoints fixed.',
    '選択していない端点を固定したまま、スケッチ図形の選択部分を引き伸ばします。',
    fill('M4 11 H28 V27 H4Z')
    + p('M16 11 V27', stroke_dasharray='2 3')
    + accent('M16 5 H28 M24 2 28 5 24 8 M28 11 V27')
    + c(4, 11, 1.8, fill=INK) + c(4, 27, 1.8, fill=INK),
    ['stretch', 'fixed endpoints', 'selected region', 'sketch transform', 'ストレッチ', '固定端点', '部分変形', 'スケッチ変換'])

# An irregular patina region and exposed underlayer depict wear rather than material assignment.
add('surface-aging', 'Control layered surface aging', '多層表面の経年変化を設定', 'appearance',
    'Control layered patina, weathering or wear on rendered surfaces.',
    'レンダリングする表面の多層のパティナ、風化、摩耗を設定します。',
    fill('M4 6 Q16 1 28 6 V25 Q16 30 4 25Z')
    + p('M4 13 10 11 12 16 9 19 12 25 4 25Z', fill='#c88626', stroke=AMBER)
    + p('M18 6 16 11 20 13 18 18 24 20 28 16', stroke=TEAL)
    + p('M20 27 24 21 28 25Z', fill='white')
    + c(9, 8, 1, fill=AMBER, stroke='none')
    + c(23, 8, 1.2, fill=TEAL, stroke='none'),
    ['aging', 'patina', 'weathering', 'wear layers', '経年変化', 'パティナ', '風化', '摩耗レイヤー'])

# A single open arc translates vertically; neither rim is a closed cap.
add('surface-extrude', 'Extrude open surface', 'サーフェス押し出し', 'surface-modeling',
    'Extrude an open profile along a direction to create a surface without solid caps.',
    '開いた輪郭を指定方向へ押し出し、端面で閉じないサーフェスを作成します。',
    fill('M4 11 Q14 2 24 11 V27 Q14 18 4 27Z')
    + accent('M4 11 Q14 2 24 11 M4 27 Q14 18 24 27')
    + p('M10 7 V23 M18 7 V23', stroke_dasharray='2 3')
    + accent('M29 22 V4 M26 8 29 4 31 8'),
    ['surface', 'extrude', 'open profile', 'uncapped', 'サーフェス', '押し出し', '開輪郭', '端面なし'])

add('surface-fair', 'Fair surface curvature', 'サーフェスの曲率を平滑化', 'surface-editing',
    'Smooth curvature variation across a surface while retaining its boundary context.',
    '境界を維持しながら、サーフェス内部の曲率の変動を滑らかにします。',
    fill('M4 10 Q16 3 28 10 L26 27 Q16 20 4 27Z')
    + p('M5 19 C9 9 12 27 17 14 S23 26 27 18', stroke=AMBER, stroke_dasharray='2 3')
    + accent('M5 19 Q16 12 27 19')
    + c(4, 10, 1.5, fill='white') + c(28, 10, 1.5, fill='white')
    + c(4, 27, 1.5, fill='white') + c(26, 27, 1.5, fill='white'),
    ['surface', 'fair', 'curvature smoothing', 'held boundaries', 'サーフェス', 'フェアリング', '曲率平滑化', '境界保持'])

add('surface-flatten', 'Flatten surface', 'サーフェスを平坦化', 'surface-editing',
    'Flatten a curved sheet into a planar surface rather than a texture-coordinate layout.',
    'テクスチャ座標ではなく、曲面を平坦なサーフェスへ展開します。',
    fill('M3 10 Q13 0 23 10 L20 17 Q11 9 3 17Z')
    + p('M8 24 20 18 29 23 17 29Z', fill=PALE, stroke=TEAL)
    + accent('M27 8 V17 M24 14 27 17 30 14'),
    ['surface', 'flatten', 'planar sheet', 'develop', 'サーフェス', '平坦化', '平面', '展開'])

# Open section arcs connect through changing widths; no top or bottom cap.
add('surface-loft', 'Loft open surfaces', 'サーフェスロフト', 'surface-modeling',
    'Create an uncapped surface interpolating between section profiles.',
    '複数の断面輪郭を補間し、端面で閉じないサーフェスを作成します。',
    fill('M3 5 Q16 14 29 5 C23 13 21 19 27 28 Q16 19 5 28 C11 19 9 13 3 5Z')
    + accent('M3 5 Q16 14 29 5 M9 16 Q16 12 23 16 M5 28 Q16 19 27 28')
    + p('M10 9 Q16 16 11 25 M22 9 Q16 16 21 25', stroke_dasharray='2 3'),
    ['surface', 'loft', 'open sections', 'uncapped', 'サーフェス', 'ロフト', '開いた断面', '端面なし'])

add('surface-mid', 'Create mid-surface', '中央サーフェスを作成', 'surface-modeling',
    'Derive a surface midway between two opposing or offset faces.',
    '向かい合う2つの面の中間にサーフェスを生成します。',
    p('M4 8 16 3 28 8 16 13Z', fill='white')
    + p('M4 24 16 19 28 24 16 29Z', fill='white')
    + p('M4 16 16 11 28 16 16 21Z', fill=PALE, stroke=TEAL)
    + p('M3 8 V24 M1 12 3 8 5 12 M1 20 3 24 5 20', stroke_dasharray='2 3')
    + accent('M10 16 H22'),
    ['mid-surface', 'paired faces', 'midway', 'derived sheet', '中央面', '対向面', '中間', '抽出面'])

# Revolved profile edges border an open sheet, with a visible gap at the axis.
add('surface-revolve', 'Revolve open surface', 'サーフェス回転', 'surface-modeling',
    'Rotate an open profile around an axis to form an uncapped surface of revolution.',
    '開いた輪郭を軸のまわりに回転させ、端面で閉じない回転サーフェスを作成します。',
    p('M10 2 V29', stroke_dasharray='2 3')
    + fill('M15 5 C23 4 28 7 28 11 V24 C28 20 23 17 15 18Z')
    + accent('M15 5 V18')
    + p('M15 5 C23 4 28 7 28 11 M15 18 C23 17 28 20 28 24')
    + accent('M4 20 C1 28 19 32 27 27 M23 27 H27 V31'),
    ['surface', 'revolve', 'open profile', 'axis', 'サーフェス', '回転', '開輪郭', '回転軸'])

# Open end arcs and two side rails define a swept sheet, not a filled tube.
add('surface-sweep', 'Sweep open surface', 'サーフェススイープ', 'surface-modeling',
    'Sweep an open section along a path to create a surface without solid end caps.',
    '開いた断面をパスに沿って移動させ、端面を持たないサーフェスを作成します。',
    fill('M4 26 C4 11 12 7 22 10 Q25 3 29 10 C18 13 11 17 11 26 Q7 19 4 26Z')
    + accent('M4 26 Q7 19 11 26 M22 10 Q25 3 29 10')
    + p('M7 24 C8 12 18 9 25 8', stroke_dasharray='2 3')
    + accent('M14 4 H21 M18 1 21 4 18 7'),
    ['surface', 'sweep', 'open section', 'path', 'サーフェス', 'スイープ', '開断面', 'パス'])

assert len(ITEMS) == len(_AUDIT) == 50
assert {item['id'] for item in ITEMS} == set(_AUDIT)
