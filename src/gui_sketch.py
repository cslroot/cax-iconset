"""Original sketch GUI symbols on the existing 32 px engineering grid.

Application command names inform semantics only, never the artwork. Alternate
input methods share one icon rather than multiplying the same geometric meaning.
"""

from core import p, r, c, accent, nodes, PALE, TEAL


def _item(id, name, name_ja, family, description, description_ja,
          body, tags, aliases):
    return {
        'id': id,
        'name': name,
        'nameJa': name_ja,
        'description': description,
        'descriptionJa': description_ja,
        'family': family,
        'role': 'command',
        'tags': list(dict.fromkeys(tags + [name.lower(), name_ja, 'sketch',
                                         'スケッチ', 'cad', 'SolidCraft', 'SOLIDWORKS'])),
        'aliases': aliases,
        'sources': ['solidcraft-commands', 'solidworks-sketch'],
        'body': body,
    }


ITEMS = [
    _item(
        'sketch-ellipse', 'Sketch ellipse', 'スケッチ楕円', 'sketch',
        'Draw an elliptical sketch profile using its center and two axis lengths.',
        '中心と長短軸の長さを指定して楕円のスケッチを描きます。',
        p('M4 16 A12 8 0 1 0 28 16 A12 8 0 1 0 4 16Z', fill=PALE)
        + accent('M16 8 V16 H28', stroke_dasharray='2 3')
        + c(16, 16, 1.5, fill=TEAL, stroke='none'),
        ['ellipse', 'major axis', 'minor axis', '楕円', '長軸', '短軸', '作図'],
        ['sketch.ellipse', 'SolidCraft ellipse', 'SOLIDWORKS Ellipse'],
    ),
    _item(
        'sketch-polygon', 'Sketch polygon', 'スケッチ正多角形', 'sketch',
        'Draw a regular polygon by its inscribed circle, circumscribed circle or edge.',
        '内接円、外接円、または辺を基準に正多角形のスケッチを描きます。',
        p('M16 4 27 10 V22 L16 28 5 22 V10Z', fill=PALE)
        + accent('M16 16 27 10', stroke_dasharray='2 3')
        + c(16, 16, 1.5, fill=TEAL, stroke='none'),
        ['polygon', 'regular polygon', 'inscribed', 'circumscribed',
         '多角形', '正多角形', '内接', '外接', '作図'],
        ['sketch.polygon.inscribed', 'sketch.polygon.circumscribed',
         'sketch.polygon.edge', 'SolidCraft polygon', 'SOLIDWORKS Polygon'],
    ),
    _item(
        'sketch-slot', 'Sketch straight slot', 'スケッチ直線スロット', 'sketch',
        'Draw a straight slot profile with parallel sides and semicircular ends.',
        '平行な直線と半円の端部で構成される直線スロットを描きます。',
        r(4, 10, 24, 12, 6, fill=PALE)
        + accent('M10 16 H22', stroke_dasharray='2 3')
        + c(10, 16, 1.5, fill=TEAL, stroke='none')
        + c(22, 16, 1.5, fill=TEAL, stroke='none'),
        ['slot', 'straight slot', 'obround', 'center distance',
         'スロット', '長穴', '直線スロット', '中心間距離', '作図'],
        ['sketch.slot.center_point', 'sketch.slot.center_to_center',
         'sketch.slot.overall', 'SolidCraft straight slot',
         'SOLIDWORKS Straight Slot', 'SOLIDWORKS Centerpoint Straight Slot'],
    ),
    _item(
        'sketch-text', 'Sketch text', 'スケッチ文字', 'sketch',
        'Insert text into a sketch for use in profiles, labels or engraved features.',
        '輪郭、ラベル、刻印フィーチャに使用する文字をスケッチへ挿入します。',
        p('M7 24 14 6 21 24 M10 17 H18')
        + accent('M4 28 H28 M26 8 V24 M23 8 H29 M23 24 H29'),
        ['text', 'lettering', 'engrave', '文字', 'テキスト', '刻印', '作図'],
        ['sketch.text', 'SolidCraft sketch text', 'SOLIDWORKS Sketch Text'],
    ),
    _item(
        'sketch-construction-line', 'Sketch construction line',
        'スケッチ補助線', 'sketch',
        'Create or designate a construction line used as a sketch reference rather than a profile edge.',
        '輪郭の一部ではなくスケッチの基準として使用する補助線を作成または指定します。',
        accent('M5 25 27 7', stroke_dasharray='5 3')
        + nodes([(5, 25), (27, 7)])
        + p('M4 7 H11 M7.5 3.5 V10.5', stroke_dasharray='2 2'),
        ['construction line', 'construction geometry', 'centerline',
         '補助線', '構築線', '構築ジオメトリ', '中心線', '基準'],
        ['sketch.centerline', 'sketch.construction', 'SolidCraft construction line',
         'SOLIDWORKS Centerline', 'SOLIDWORKS For Construction'],
    ),
    _item(
        'constraint-collinear', 'Collinear constraint', '同一直線上拘束',
        'sketch-constraint',
        'Keep separate sketch line segments on the same infinite straight line.',
        '離れたスケッチ線分を同じ無限直線上に保ちます。',
        accent('M12 19 20 13', stroke_dasharray='2 3')
        + p('M4 25 12 19 M20 13 28 7')
        + nodes([(4, 25), (12, 19), (20, 13), (28, 7)]),
        ['constraint', 'collinear', 'aligned', '拘束', '同一直線上', '共線', '整列'],
        ['sketch.constraint.collinear', 'SolidCraft collinear constraint',
         'SOLIDWORKS Collinear Relation'],
    ),
    _item(
        'constraint-curvature', 'Curvature constraint', '曲率連続拘束',
        'sketch-constraint',
        'Match the tangent direction and curvature of two curves at their shared endpoint.',
        '接続する2本の曲線の端点で接線方向と曲率を一致させます。',
        p('M4 23 C4 15 8 8 16 8')
        + accent('M16 8 C24 8 28 15 28 23')
        + c(16, 8, 2, fill=PALE, stroke=TEAL)
        + accent('M12 23 H20 M12 27 H20'),
        ['constraint', 'curvature', 'G2 continuity', 'equal curvature',
         '拘束', '曲率', '曲率連続', '等曲率', 'G2連続'],
        ['sketch.constraint.curvature', 'SolidCraft curvature constraint',
         'SOLIDWORKS Equal Curvature Relation'],
    ),
    _item(
        'sketch-auto-constrain', 'Auto constrain sketch', 'スケッチ自動拘束',
        'sketch-constraint',
        'Automatically detect and apply geometric constraints to sketch entities.',
        'スケッチ図形の幾何学的関係を検出して拘束を自動適用します。',
        p('M6 7 V25 H25')
        + r(6, 19, 6, 6, 0, fill=PALE, stroke=TEAL)
        + nodes([(6, 7), (25, 25)])
        + accent('M23 4 24.5 9.5 30 11 24.5 12.5 23 18 21.5 12.5 16 11 21.5 9.5Z'),
        ['constraint', 'automatic', 'auto constrain', 'infer relations',
         '拘束', '自動', '自動拘束', '幾何拘束', '関係検出'],
        ['sketch.auto_constrain', 'SolidCraft auto constrain',
         'SOLIDWORKS Fully Define Sketch relations'],
    ),
]
