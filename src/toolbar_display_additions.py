"""Distinct viewport toolbar glyphs, drawn for the CAX 18-group acceptance list.

These are state/mode choices, not replacements for their existing menu icons.
No vendor artwork is used. Selected face geometry identifies view directions.
"""
from core import p, r, c, accent, PALE, TEAL, INK
ITEMS=[]
def add(id,en,ja,desc,body,family):
    ITEMS.append(dict(id=id,domain='CAD',name=en,nameJa=ja,description=desc,
        descriptionJa=ja+'を選択または切り替えます。',body=body,family=family,role='command',
        tags=['viewport','toolbar',family,en.lower(),ja],aliases=[en,ja],sources=['cax-toolbar-requirements-2026-10-25']))

# A common model silhouette lets the rendering treatment, not a badge, carry meaning.
outline='M5 10 16 4 27 10 V23 L16 29 5 23Z'
seams='M5 10 16 16 27 10 M16 16 V29'
add('display-shaded','Shaded display','シェーディング表示',
    'Display filled, lit surfaces without explicit model-edge overlays.',
    p('M5 10 16 4 27 10 16 16Z',fill=PALE,stroke='none')
    +p('M5 10 16 16 V29 L5 23Z',fill=TEAL,stroke='none')
    +p('M16 16 27 10 V23 L16 29Z',fill=INK,stroke='none')+p(outline), 'display-mode')
add('display-shaded-edges','Shaded display with edges','エッジ付きシェーディング',
    'Display filled surfaces with explicit visible model edges.',
    p(outline,fill=PALE)+p(seams)+accent('M5 10 16 16 27 10 M16 16 V29'), 'display-mode')
add('display-wireframe','Wireframe display','ワイヤフレーム表示',
    'Display model edges without filled surfaces, including edges behind the model.',
    p(outline)+p(seams)+accent('M5 23 16 17 27 23 M16 4 V17'), 'display-mode')
add('display-hidden-line','Hidden-line display','隠線表示',
    'Display opaque-looking visible outlines while hidden model edges are dashed; renderer settings may omit hidden edges.',
    p(outline)+p(seams)+p('M5 23 16 17 27 23 M16 4 V17',stroke_dasharray='2 3'), 'display-mode')
add('display-depth','Depth display','深度表示',
    'Display a camera-depth field rather than material shading or surface orientation.',
    r(4,4,24,24,1)+p('M5 5 H27 V11 H5Z',fill=PALE,stroke='none')
    +p('M5 11 H27 V19 H5Z',fill=TEAL,stroke='none')
    +p('M5 19 H27 V27 H5Z',fill=INK,stroke='none')
    +p('M8 8 H10 V20 H13 L9 25 5 20 H8Z',fill='white',stroke='none'), 'display-mode')
add('display-normals','Surface-normal display','法線表示',
    'Visualize surface-normal directions as a viewport diagnostic; does not reverse or recompute normals.',
    p('M5 22 16 15 27 22 16 29Z',fill=PALE)
    +accent('M16 22 V4 M12 8 16 4 20 8 M8 23 3 13 M3 17 V13 H7 M24 23 29 13 M25 13 H29 V17'), 'display-mode')
add('display-tessellation','Tessellation display','テッセレーション表示',
    'Show the triangular tessellation of displayed model surfaces without converting the source geometry.',
    p(outline,fill=PALE)+p(seams)+accent('M5 10 16 4 16 16 27 23 16 29 5 10 M5 23 16 16 27 10'), 'display-mode')

# Fixed projection of a cube. Each direction selects a different geometric face.
visible='M5 12 12 5 H27 V20 L20 27 H5Z M5 12 H20 V27 M20 12 27 5'
hidden='M12 5 V20 H27 M5 27 12 20'
faces={
 'front':('M5 12 H20 V27 H5Z','Front view','正面ビュー'),
 'back':('M12 5 H27 V20 H12Z','Back view','背面ビュー'),
 'top':('M5 12 12 5 H27 L20 12Z','Top view','上面ビュー'),
 'bottom':('M5 27 12 20 H27 L20 27Z','Bottom view','底面ビュー'),
 'left':('M5 12 12 5 V20 L5 27Z','Left view','左側面ビュー'),
 'right':('M20 12 27 5 V20 L20 27Z','Right view','右側面ビュー'),
}
for direction,(face,en,ja) in faces.items():
    add('view-'+direction,en,ja,
        'Orient the camera to the '+direction+' standard view. The selected cube face identifies the direction; axis conventions remain the consumer contract.',
        p(face,fill=TEAL,stroke='none')+p(hidden,stroke_dasharray='2 3')+p(visible)
        +p(face,stroke=TEAL,stroke_width=2.5), 'standard-view')

add('navigate-turntable','Turntable navigation','ターンテーブル操作',
    'Orbit the camera around a fixed up-axis and model center, preserving an upright horizon.',
    p('M9 11 16 7 23 11 V20 L16 24 9 20Z',fill=PALE)
    +p('M9 11 16 15 23 11 M16 15 V24 M16 3 V7',stroke_dasharray='2 2')
    +accent('M5 15 C0 20 4 28 16 28 C27 28 31 23 27 18 M24 19 27 18 29 22'), 'navigation-mode')
add('navigate-fly','Fly navigation','フライ操作',
    'Translate and turn a freely moving camera through the scene; unlike orbit, movement is not anchored to a model center.',
    p('M3 17 28 4 19 29 14 20Z',fill=PALE)
    +accent('M14 20 28 4 M7 23 3 27 M12 26 9 30'), 'navigation-mode')
add('toggle-navigation-cube','Toggle navigation cube','ナビキューブ表示切替',
    'Show or hide the viewport orientation cube gadget; does not change the model geometry or projection.',
    r(3,3,26,26,2)+p('M14 11 20 7 26 11 V19 L20 23 14 19Z',fill=PALE)
    +accent('M14 11 20 15 26 11 M20 15 V23')+p('M6 24 H11 M6 20 V24'), 'viewport-gadget')
add('toggle-axis-triad','Toggle axis triad','軸トライアド表示切替',
    'Show or hide the viewport orientation-axis triad gadget; does not reset or modify a work coordinate system.',
    r(3,3,26,26,2)+accent('M11 22 V9 M8 12 11 9 14 12 M11 22 H25 M22 19 25 22 22 25')
    +p('M11 22 20 14 M16 14 H20 V18')+c(11,22,1.7,fill=TEAL,stroke=TEAL), 'viewport-gadget')
add('effect-matcap','Matcap shading','マットキャップ',
    'Use a view-dependent material-capture image to shade surfaces, distinct from scene environment reflections.',
    c(16,16,12,fill=PALE)+p('M7 9 C14 6 9 22 22 26 A12 12 0 0 1 7 9Z',fill=TEAL,stroke='none')
    +p('M12 7 C15 5 21 7 23 11 C19 15 14 13 12 7Z',fill='white',stroke='none'), 'viewport-effect')
add('effect-bloom','Bloom glow','ブルーム',
    'Add a glow around bright rendered regions; not a geometric light-source command.',
    c(16,16,5,fill=PALE,stroke=TEAL)+accent('M16 2 V6 M16 26 V30 M2 16 H6 M26 16 H30 M6 6 9 9 M23 23 26 26 M6 26 9 23 M23 9 26 6')
    +c(16,16,9,stroke_dasharray='1 4'), 'viewport-effect')
add('effect-reflections','Rendered reflections','反射効果',
    'Display reflected model or scene imagery on reflective surfaces; not environment-map surface inspection.',
    p('M9 4 H23 V13 H9Z',fill=PALE)+accent('M3 17 H29')
    +p('M9 21 H23 V28 H9Z',stroke_dasharray='2 2')+p('M9 13 12 10 H26 V3 M23 4 26 3 M23 13 26 10'), 'viewport-effect')
