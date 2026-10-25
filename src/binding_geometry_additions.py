"""Original geometry for verified gaps found while resolving conditional bindings.

No vendor artwork. Existing 693 records remain immutable; command bindings carry
context-specific method semantics separately from these reusable glyph families.
"""
from core import p, r, c, accent, PALE, TEAL, INK

ITEMS = []
def add(id, en, ja, desc, desc_ja, body, family):
    ITEMS.append(dict(id=id, domain='CAD', name=en, nameJa=ja,
        description=desc, descriptionJa=desc_ja, family=family,
        role='command', tags=[family,en.lower(),ja,'cad'], body=body,
        aliases=[], sources=[]))

add('replace-selected-object', 'Replace selected object', '選択オブジェクトを置換',
    'Substitute one selected geometric object or component for another; the command context specifies reference-transfer policy.',
    '選択した幾何要素やコンポーネントを別の対象に置き換えます。参照の引き継ぎ方法はコマンドの文脈で明示します。',
    p('M3 12 9 9 15 12 V22 L9 25 3 22Z',fill=PALE)
    +p('M3 12 9 15 15 12 M9 15 V25')
    +p('M21 12 28 16 V24 L21 28 17 24 V16Z',fill=PALE)
    +accent('M6 6 H24 M20 2 24 6 20 10'), 'object-substitution')

add('transform-selected-face', 'Transform selected face', '選択面を変換',
    'Translate or rotate a selected face while retaining the surrounding body context; normal offset is one mode, not the entire operation.',
    '周囲のボディを参照しながら選択面を移動または回転します。法線方向のオフセットはその一つのモードです。',
    p('M4 11 15 6 25 11 V24 L15 29 4 24Z',fill=PALE,stroke='none')
    +p('M4 11 15 6 25 11 V24 L15 29 M15 16 25 11')
    +p('M4 11 15 16 V29 L4 24Z',stroke_dasharray='2 2')
    +p('M2 8 10 11 V23 L2 20Z',fill=PALE,stroke=TEAL)
    +accent('M13 3 H25 M22 1 25 3 22 5'), 'face-transform')

add('deform-shape', 'Deform shape', '形状を変形',
    'Change surface or solid shape without implying an enclosing control cage; the labeled command selects its actual deformation method.',
    '外側の制御ケージを前提にせずサーフェスやソリッドの形状を変更します。実際の変形方式はコマンド名と設定で区別します。',
    p('M3 8 H12 V26 H3Z M3 14 H12 M3 20 H12 M7.5 8 V26')
    +p('M20 8 Q28 11 29 18 Q29 24 20 26 Q23 17 20 8Z',fill=PALE)
    +p('M21.5 14 Q26 15 28.5 17 M21.5 20 Q26 21 28.5 20')
    +accent('M9 3 H23 M20 1 23 3 20 5'), 'shape-deformation')

add('align-body', 'Align body to reference', 'ボディを参照に整列',
    'Move and orient a body by matching a selected source reference to a target point, face, or plane; this does not create a persistent mate.',
    '選択したボディ側の参照を目標の点・面・平面に合わせて位置と姿勢を調整します。永続的な合致は作成しません。',
    p('M3 13 9 9 15 12 V22 L9 26 3 23Z',fill=PALE)
    +p('M3 13 9 16 15 12 M9 16 V26')
    +p('M22 10 29 7 V25 L22 29Z',fill=PALE)
    +accent('M5 5 Q18 1 25 9 M21 8 25 9 25 5 M21 19 H28 M25 16 28 19 25 22'),
    'reference-alignment')

add('surface-planar', 'Create planar surface', '平面サーフェスを作成',
    'Create a bounded flat surface body without thickness; not a curved fill or construction datum plane.',
    '厚みのない平らなサーフェスボディを境界内に作成します。曲面の穴埋めや作業用の基準平面とは区別します。',
    p('M3 22 12 7 29 10 20 25Z',fill=PALE)
    +p('M6 17 23 20 M9 12 26 15 M8.7 23 17.7 8 M14.3 24 23.3 9')
    +accent('M12 7 29 10'), 'planar-surface')

add('wrap-profile', 'Wrap profile onto face', '輪郭を面へラップ',
    'Map sketch contours onto a face, including no-depth Scribe imprints; material addition or removal is a separately labeled mode.',
    'スケッチの輪郭を面に沿って写します。深さを持たないスクライブも含み、材料の追加・除去はモード名で区別します。',
    p('M14 8 Q22 3 29 8 V26 Q22 21 14 26Z',fill=PALE)
    +p('M14 8 Q22 13 29 8')
    +accent('M18 22 V14 Q22 11 26 14 V21 M18 18 Q22 15 26 18')
    +p('M3 20 V12 H9 V20 M3 16 H9')
    +accent('M6 7 Q11 2 17 7 M14 3 17 7 13 8'), 'surface-profile-wrap')

add('groove-bead', 'Create solid gap weld', 'ソリッドの隙間溶接を作成',
    'Create weld material as a solid body in the gap between selected surfaces; not a cosmetic bead annotation.',
    '選択した面の間の隙間に、ソリッドボディとして溶接材料を作成します。表示だけの溶接ビード注記とは区別します。',
    p('M3 10 9 7 13 10 V25 L7 28 3 25Z',fill=PALE)
    +p('M19 10 25 7 29 10 V25 L23 28 19 25Z',fill=PALE)
    +p('M13 13 19 10 V25 L13 28Z',fill=TEAL,stroke=TEAL)
    +p('M3 10 7 13 13 10 M7 13 V28 M19 10 23 13 29 10 M23 13 V28')
    +p('M13 13 16 14.5 19 13 M13 19 16 20.5 19 19'), 'solid-weld')
