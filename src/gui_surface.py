"""Original face and surface commands selected from the reviewed GUI audit.

These are distinct modeling operations, not vendor artwork or state variants.
Surface matching and body splitting reuse their existing catalog entries.
"""
from core import p, accent, fill, PALE, TEAL


def item(id, name, name_ja, family, description, description_ja, body,
         tags, aliases):
    return {
        'id': id,
        'name': name,
        'nameJa': name_ja,
        'description': description,
        'descriptionJa': description_ja,
        'family': family,
        'role': 'command',
        'tags': list(dict.fromkeys(tags + [name.lower(), name_ja, 'cad'])),
        'aliases': aliases,
        'sources': ['solidcraft-commands', 'solidworks-surfaces'],
        'body': body,
    }


ITEMS = [
    item(
        'replace-face', 'Replace face', '面の置換', 'direct-modeling',
        'Replace selected solid faces with a target surface and update the adjoining faces.',
        'ソリッドの選択面を指定したサーフェスで置き換え、隣接面を更新します。',
        # The curved target replaces the dashed former top of the same body.
        fill('M4 16 Q15 8 27 16 V25 L16 29 4 25Z')
        + p('M4 16 16 21 27 16 M16 21 V29', stroke_dasharray='2 3')
        + accent('M4 16 Q15 8 27 16')
        + accent('M16 3 V10 M13 7 16 10 19 7'),
        ['face', 'replace', 'target surface', 'solid', '面', '置換', '参照曲面'],
        ['solid.replace_face', 'replace faces', '面を置換'],
    ),
    item(
        'delete-face', 'Delete face', '面の削除', 'direct-modeling',
        'Remove selected faces from a body; this is a face-level edit, not deletion of the entire body.',
        'ボディから選択面を削除します。ボディ全体の削除とは異なる面単位の編集です。',
        # The left face remains; the right face is a dashed removable boundary.
        fill('M4 10 15 15 V28 L4 23Z')
        + p('M4 10 15 5 27 10 15 15')
        + p('M15 15 27 10 V23 L15 28', stroke_dasharray='2 3')
        + accent('M20 16 27 23 M27 16 20 23'),
        ['face', 'delete', 'remove', 'boundary', '面', '削除', '境界'],
        ['face.delete', 'delete faces', '面を削除'],
    ),
    item(
        'split-face', 'Split face', '面の分割', 'direct-modeling',
        'Divide a face into separate face regions using a curve or tool without splitting the body.',
        '曲線や分割ツールで面を複数の領域に分けます。ボディ自体は分割しません。',
        # One intact sheet gains an internal seam, rather than two separated bodies.
        fill('M4 10 24 5 28 23 8 28Z')
        + p('M4 10 17 7 11 27 8 28Z', fill='white', stroke='none')
        + p('M4 10 24 5 28 23 8 28Z')
        + accent('M18 3 11 29')
        + p('M21 12 25 11 M19 20 27 18', stroke_dasharray='2 3'),
        ['face', 'split', 'divide', 'curve', '面', '分割', '領域', '分割線'],
        ['solid.split_face', 'split face regions', '面領域を分割'],
    ),
    item(
        'surface-extend', 'Extend surface', 'サーフェス延長', 'surface-editing',
        'Extend an existing surface beyond selected boundary edges.',
        '選択した境界エッジの外側へ既存のサーフェスを延長します。',
        # A former edge remains dashed inside a newly extended sheet.
        fill('M4 13 Q15 7 28 13 L25 27 Q14 21 4 27Z')
        + p('M17 10 15 24', stroke_dasharray='2 3')
        + accent('M17 10 Q22 10 28 13 L25 27 Q20 24 15 24')
        + accent('M15 4 H28 M24 1 28 4 24 7'),
        ['surface', 'extend', 'edge', 'boundary', 'サーフェス', '延長', '境界', 'エッジ'],
        ['surface.extend', 'extend surface edge', '曲面延長'],
    ),
    item(
        'surface-untrim', 'Untrim surface', 'サーフェスのトリム解除', 'surface-editing',
        'Remove trimming boundaries to restore the underlying surface region.',
        'トリム境界を取り除き、元のサーフェス領域を復元します。',
        # An obsolete inner trim boundary and a return arrow on the restored sheet.
        fill('M4 10 Q14 4 28 10 L25 27 Q14 21 4 27Z')
        + p('M9 16 Q15 11 21 16 Q21 22 14 22 Q8 22 9 16Z', stroke_dasharray='2 3')
        + accent('M22 21 C30 19 29 7 20 6 H15 M18 3 15 6 18 9'),
        ['surface', 'untrim', 'restore', 'trim boundary', 'サーフェス', 'トリム解除', '境界解除', '復元'],
        ['surface.untrim', 'remove surface trim', '曲面のトリム解除'],
    ),
    item(
        'surface-unstitch', 'Unstitch surfaces', 'サーフェス縫合解除', 'surface-editing',
        'Disconnect stitched surface faces into separate surface bodies.',
        '縫合された面の接続を解除し、独立したサーフェスボディに分離します。',
        # Surface edges pull apart; there is no volumetric cutting plane.
        fill('M3 13 Q8 9 13 13 V27 Q8 23 3 27Z')
        + fill('M19 13 Q24 17 29 13 V27 Q24 31 19 27Z')
        + accent('M13 13 V27 M19 13 V27')
        + accent('M12 5 H3 M6 2 3 5 6 8 M20 5 H29 M26 2 29 5 26 8'),
        ['surface', 'unstitch', 'unsew', 'separate', 'サーフェス', '縫合解除', '分離', '接続解除'],
        ['surface.unstitch', 'unsew surfaces', '曲面を分離'],
    ),
    item(
        'surface-ruled', 'Ruled surface', 'ルールドサーフェス', 'surface-modeling',
        'Create a surface with straight-line generators extending from a selected edge.',
        '選択したエッジから直線の母線を伸ばし、ルールドサーフェスを作成します。',
        # Straight generators connect a curved source edge to the opposite edge.
        fill('M4 9 Q16 1 28 9 V27 H4Z')
        + p('M10 6 V27 M16 5 V27 M22 6 V27')
        + accent('M4 9 Q16 1 28 9 M4 27 H28'),
        ['surface', 'ruled', 'generator', 'edge', 'サーフェス', 'ルールド', '線織面', '母線'],
        ['surface.ruled', 'ruled surface from edge', '線織面'],
    ),
    item(
        'surface-reverse-normal', 'Reverse surface normal', 'サーフェス法線反転', 'surface-editing',
        'Reverse the orientation of a surface normal without changing its geometric shape.',
        '形状を変えずにサーフェスの法線方向を反転します。',
        # The old upward normal is dashed; the resulting normal points downward.
        fill('M4 18 15 12 28 18 17 24Z')
        + p('M16 17 V3 M13 6 16 3 19 6', stroke_dasharray='2 3')
        + accent('M16 17 V30 M12 26 16 30 20 26')
        + accent('M24 5 Q31 10 25 14 M25 10 V14 H29'),
        ['surface', 'normal', 'reverse', 'orientation', 'サーフェス', '法線', '反転', '向き'],
        ['surface.reverse_normal', 'flip surface normal', '曲面方向反転'],
    ),
]
