"""Original model/assembly command glyphs from the frozen GUI coverage review.

Documentation supplies command meaning, never vendor artwork. Geometry uses
32-unit coordinates and the inherited rounded 1.75-unit engineering stroke.
Options and enable/disable states share their semantic command-family glyph.
"""
from core import p, r, c, g, accent, fill, cube, PALE, TEAL, INK, AMBER

ITEMS = []


def add(id, en, ja, description, description_ja, body, family):
    ITEMS.append(dict(
        id=id, domain='CAD', name=en, nameJa=ja,
        description=description, descriptionJa=description_ja,
        family=family, role='command',
        tags=[family, en.lower(), ja, 'cad', '設計'], body=body,
    ))


def block(x, y, w=9, h=10, color=PALE):
    """Compact isometric component, without an action badge."""
    z = w / 2
    return (p(f'M{x} {y+3} {x+z} {y} {x+w} {y+3} V{y+h} '
              f'L{x+z} {y+h+3} {x} {y+h}Z', fill=color)
            + p(f'M{x} {y+3} {x+z} {y+6} {x+w} {y+3} M{x+z} {y+6} V{y+h+3}'))


# Assembly structure and component state.
add('activate-component', 'Activate component', 'コンポーネントをアクティブ化',
    'Enter a component editing context inside the assembly.',
    'アセンブリ内でコンポーネントの編集コンテキストに入ります。',
    p('M3 11 V4 H10 M22 4 H29 V11 M29 22 V29 H22 M10 29 H3 V22', stroke_dasharray='2 2')
    + block(11, 10, 12, 12) + accent('M3 16 H11 M7 12 11 16 7 20'), 'assembly-context')
add('assembly-contact', 'Assembly contact sets', 'アセンブリ接触セット',
    'Define or enable geometric contact stops between assembly components.',
    'アセンブリ部品間の幾何学的な接触停止を定義または有効化します。',
    fill('M3 9 H12 V23 H3Z M20 9 H29 V23 H20Z')
    + accent('M16 6 V26 M7 16 H13 M10 13 13 16 10 19 M25 16 H19 M22 13 19 16 22 19'), 'assembly-contact')
add('assembly-to-multibody', 'Assembly to multibody part', 'マルチボディ部品に変換',
    'Convert an assembly structure to a part containing separate solid bodies.',
    'アセンブリ構造を複数の独立したソリッドを持つ部品に変換します。',
    p('M5 4 H27 V7 M5 7 V4 M16 4 V8')
    + r(3, 8, 7, 6, 1) + r(22, 8, 7, 6, 1)
    + accent('M16 9 V17 M13 14 16 17 19 14')
    + r(4, 19, 24, 10, 2, fill=PALE) + p('M8 22 H13 V26 H8Z M19 22 H24 V26 H19Z'), 'assembly-structure')
add('assembly-visualization', 'Assembly visualization', 'アセンブリ可視化',
    'Compare component properties in a ranked assembly visualization.',
    '部品属性を順位付けしたアセンブリ表示で比較します。',
    block(3, 4, 8, 7) + block(3, 17, 8, 7)
    + r(16, 5, 13, 5, 1, fill=TEAL, stroke=TEAL)
    + r(16, 13, 9, 5, 1, fill=PALE) + r(16, 21, 5, 5, 1, fill=PALE), 'assembly-inspection')
add('belt-chain', 'Belt or chain drive', 'ベルト・チェーンドライブ',
    'Create a belt or chain path and couple the motion of its pulleys or sprockets.',
    'プーリーやスプロケットを結ぶベルト・チェーン経路と連動運動を作成します。',
    p('M10 8 H24 A7 7 0 0 1 24 22 L10 26 A9 9 0 0 1 10 8Z')
    + c(10, 17, 6, fill=PALE) + c(24, 15, 3, fill=PALE)
    + accent('M10 17 13 14 M24 15 26 13 M12 3 H22 M19 1 22 3 19 5'), 'assembly-mechanism')
add('bodies-to-components', 'Bodies to components', 'ボディからコンポーネントを作成',
    'Create separate component definitions from existing bodies.',
    '既存のボディから個別のコンポーネント定義を作成します。',
    r(7, 3, 18, 10, 2) + p('M10 6 H14 V10 H10Z M18 6 H22 V10 H18Z', fill=PALE)
    + accent('M16 13 V18 M7 18 H25 M7 18 V21 M25 18 V21')
    + block(3, 21, 8, 5) + block(21, 21, 8, 5), 'assembly-structure')
add('bounding-solid', 'Bounding solid', '境界ソリッド',
    'Create a solid envelope enclosing selected geometry with an optional margin.',
    '選択形状を囲む包絡ソリッドを必要な余白付きで作成します。',
    p('M4 8 16 3 28 8 V24 L16 29 4 24Z M4 8 16 13 28 8 M16 13 V29', stroke_dasharray='3 2')
    + p('M9 19 Q9 10 15 12 Q23 10 23 19 Q21 26 15 24 Q10 25 9 19Z', fill=PALE, stroke=TEAL), 'solid-creation')
add('brep-to-mesh', 'Convert B-rep to mesh', 'B-repをメッシュに変換',
    'Tessellate a boundary-representation body into a faceted mesh body.',
    '境界表現のボディを三角形分割したメッシュボディに変換します。',
    p('M3 8 Q8 3 13 8 V23 Q8 28 3 23Z', fill=PALE) + p('M3 8 Q8 13 13 8')
    + p('M22 5 29 9 V24 L22 28 19 23 V10Z', fill=PALE)
    + p('M22 5 24 16 29 9 M19 10 24 16 19 23 M24 16 29 24 22 28Z')
    + accent('M11 16 H21 M18 13 21 16 18 19'), 'geometry-conversion')
add('capture-position', 'Capture component position', 'コンポーネント位置を記録',
    'Commit pending component placements to the assembly position state.',
    '保留中のコンポーネント配置をアセンブリの位置状態として確定します。',
    p('M4 11 V4 H11 M21 4 H28 V11 M4 21 V28 H11 M21 28 H28 V21')
    + block(9, 7, 14, 11) + accent('M11 23 15 27 23 19'), 'assembly-position')
add('component-loading-state', 'Component loading state', 'コンポーネントの読み込み状態',
    'Choose lightweight or resolved component representations, including selective loading.',
    '選択読み込みを含め、軽量または完全なコンポーネント表現を選びます。',
    p('M4 9 14 4 24 9 V23 L14 28 4 23Z M4 9 14 14 24 9 M14 14 V28', stroke_dasharray='3 2')
    + fill('M14 14 24 9 V23 L14 28Z')
    + accent('M28 4 V16 M25 13 28 16 30 13'), 'assembly-loading')
add('component-preview', 'Component preview window', 'コンポーネントプレビュー',
    'Open a separate component preview for inspection and selection in the assembly.',
    'アセンブリ内の部品を確認・選択するための独立したプレビューを開きます。',
    r(3, 4, 26, 24, 2) + p('M3 10 H29 M8 7 H11')
    + block(10, 13, 12, 10) + accent('M6 14 V24'), 'assembly-inspection')
add('copy-with-mates', 'Copy with mates', '合致と共にコピー',
    'Copy a component while preserving or rebinding selected mate relationships.',
    '選択した合致関係を保持または再設定してコンポーネントをコピーします。',
    r(4, 13, 8, 10, 1, fill=PALE) + r(20, 13, 8, 10, 1, fill=PALE)
    + p('M3 28 H29 M8 23 V28 M24 23 V28')
    + c(8, 25, 2, fill='white', stroke=TEAL) + c(24, 25, 2, fill='white', stroke=TEAL)
    + accent('M8 8 H24 M20 4 24 8 20 12'), 'assembly-copy')
add('create-weldment', 'Create weldment', '溶接構造を作成',
    'Create the weldment feature that organizes structural bodies and their fabrication properties.',
    '構造ボディと製作属性を管理する溶接構造フィーチャを作成します。',
    p('M4 11 V5 H10 M22 5 H28 V11 M4 23 V29 H10 M22 29 H28 V23')
    + fill('M8 8 H13 V21 H25 V26 H8Z')
    + accent('M13 14 Q18 14 16 18 Q21 18 19 22'), 'weldment')
add('datum-point', 'Create reference point', '参照点を作成',
    'Create a persistent reference point from vertices, intersections or geometric parameters.',
    '頂点・交点・形状パラメータから永続的な参照点を作成します。',
    fill('M4 23 12 13 28 19 20 29Z')
    + p('M16 20 V5 M6 10 16 20 27 9', stroke_dasharray='3 3')
    + c(16, 20, 3.5, fill=TEAL, stroke=TEAL), 'reference-geometry')
add('derive-part', 'Create derived part', '派生部品を作成',
    'Create a linked derived part from source model geometry.',
    '元モデルの形状からリンク付きの派生部品を作成します。',
    p('M3 4 H11 L15 8 V19 H3Z M11 4 V8 H15')
    + p('M18 13 H25 L29 17 V29 H18Z M25 13 V17 H29', fill=PALE)
    + accent('M8 11 V24 H18 M14 20 18 24 14 28') + p('M21 21 H26 M21 25 H26'), 'derived-geometry')
add('direct-feature-edit', 'Direct feature editing', 'フィーチャ直接編集',
    'Interactively drag feature dimensions and faces to edit the modeled shape.',
    'フィーチャの寸法や面を直接ドラッグして形状を編集します。',
    fill('M5 14 H13 V7 H24 V26 H5Z')
    + p('M13 14 H24 M13 14 V26', stroke_dasharray='2 2')
    + accent('M24 7 H29 M28 3 V18 M25 6 28 3 30 6 M25 15 28 18 30 15')
    + c(13, 7, 2.5, fill='white', stroke=TEAL), 'direct-modeling')
add('disable-external-references', 'Prevent external references', '外部参照の作成を禁止',
    'Prevent new external model references without breaking references that already exist.',
    '既存の参照は切らず、新しい外部モデル参照の作成を禁止します。',
    p('M3 4 H13 V17 H3Z M19 15 H29 V28 H19Z')
    + accent('M8 17 V24 H16 M13 21 16 24 13 27')
    + p('M18 4 H28 V11 H18Z', fill=PALE) + p('M20 4 V2 H26 V4 M23 7 V9'), 'assembly-references')
add('explode-lines', 'Explode line sketch', '分解ラインスケッチ',
    'Create connection traces that document the relationships of exploded components.',
    '分解した部品の関係を示す接続軌跡をスケッチとして作成します。',
    block(3, 3, 8, 6) + block(21, 20, 8, 6)
    + accent('M7 12 V20 H25', stroke_dasharray='3 2')
    + p('M14 7 19 2 23 6 18 11 13 12Z M18 3 22 7'), 'assembly-documentation')
add('find-equivalent-components', 'Find equivalent components', '同等コンポーネントを検索',
    'Find independently defined components that match a source component geometrically.',
    '元部品と幾何学的に一致する独立定義のコンポーネントを検索します。',
    fill('M3 5 H11 V9 H15 V16 H3Z') + fill('M16 6 H22 V9 H26 V15 H16Z')
    + p('M6 20 H12 M6 24 H12', stroke=TEAL)
    + c(22, 22, 5.5) + accent('M26 26 30 30'), 'assembly-inspection')
add('flexible-part', 'Make part flexible', '部品を柔軟化',
    'Allow a part to adapt its internal geometry to references in the assembly.',
    'アセンブリ内の参照に応じて部品の内部形状が適応するようにします。',
    p('M5 5 V27 M27 5 V27')
    + fill('M5 11 C12 3 20 25 27 17 V23 C20 31 12 9 5 17Z')
    + accent('M6 7 C13 1 20 21 27 13', stroke_dasharray='2 3'), 'assembly-flexibility')
add('flexible-subassembly', 'Flexible subassembly', 'サブアセンブリの柔軟性',
    'Control whether a subassembly solves its internal mates in the parent assembly.',
    'サブアセンブリの内部合致を親アセンブリ内で解くかどうかを設定します。',
    r(3, 3, 26, 26, 3, stroke_dasharray='3 2')
    + p('M8 23 15 14 24 9') + c(8, 23, 3, fill=PALE) + c(24, 9, 3, fill=PALE)
    + c(15, 14, 3.5, fill=PALE) + accent('M7 10 A9 9 0 0 1 19 6 M16 3 19 6 15 8'), 'assembly-flexibility')
add('grid-system', 'Create grid system', 'グリッドシステムを作成',
    'Create persistent intersecting reference grids for spatial modeling.',
    '空間モデリング用に交差する永続的な参照グリッドを作成します。',
    p('M5 23 19 9 29 14 15 28Z M10 18 24 23 M15 13 29 18 M10 26 24 12')
    + accent('M5 23 V7 L19 3 V9 M12 16 V5 M5 14 19 9')
    + c(5, 7, 2, fill='white') + c(19, 3, 1.5, fill='white'), 'reference-geometry')
add('heal-edges', 'Heal B-rep edges', 'B-repエッジを修復',
    'Repair and merge problematic boundary-representation edges without removing the modeled feature.',
    'フィーチャを削除せずに、境界表現の問題のあるエッジを修復・結合します。',
    fill('M4 7 H28 V25 H4Z')
    + p('M4 16 H12 L14 13 M18 19 20 16 H28', stroke_dasharray='3 2')
    + accent('M10 16 H22 M13 12 V20 M19 12 V20'), 'geometry-repair')
add('insert-fastener', 'Insert standard hardware', '標準機械部品を挿入',
    'Insert sized standard library parts such as fasteners and bearings.',
    '部品ライブラリから締結部品や軸受など、寸法を指定した標準機械部品を挿入します。',
    fill('M9 3 H21 L24 7 21 11 H9 L6 7Z')
    + p('M11 11 V21 L15 25 19 21 V11 M11 15 H19 M11 19 H19')
    + p('M4 29 H26 M9 26 V29 M22 26 V29')
    + accent('M28 9 V22 M25 19 28 22 30 19'), 'assembly-library')
add('insert-structural-profile', 'Insert structural profile', '構造プロファイルを挿入',
    'Insert a standard structural section as editable sketch geometry.',
    '標準構造断面を編集可能なスケッチ形状として挿入します。',
    p('M3 29 H29 M3 29 V5', stroke_dasharray='2 3')
    + fill('M9 8 H25 V13 H20 V23 H25 V28 H9 V23 H14 V13 H9Z')
    + accent('M16 2 V8 M13 5 16 8 19 5'), 'sketch-profile')
add('joint-cam', 'Cam mate', 'カム合致',
    'Keep a follower in contact with a rotating cam profile.',
    'フォロワを回転するカム輪郭に接触させた状態で拘束します。',
    p('M5 22 C3 14 11 13 14 9 C21 3 28 11 26 20 C24 29 8 29 5 22Z', fill=PALE)
    + c(15, 21, 3) + c(19, 6, 3, fill='white') + p('M19 3 V1')
    + accent('M7 7 A10 10 0 0 0 2 15 M2 11 V15 H6'), 'assembly-mechanism')
add('joint-origin', 'Create joint origin', 'ジョイント原点を作成',
    'Create an attachment point and orientation frame used to define a joint.',
    'ジョイント定義に使う接続点と方向フレームを作成します。',
    block(3, 13, 16, 10) + c(11, 16, 3.5, fill='white', stroke=TEAL)
    + accent('M11 12 V3 M8 6 11 3 14 6 M15 16 H29 M26 13 29 16 26 19 M14 13 24 4 M20 4 H24 V8'), 'assembly-reference')
add('joint-pin-slot', 'Pin-slot mate', 'ピン・スロット合致',
    'Constrain a pin to travel inside a slot while allowing the specified rotation.',
    '指定された回転を許しつつ、ピンの移動をスロット内に拘束します。',
    r(3, 11, 26, 12, 6, fill=PALE) + p('M8 17 H24', stroke_dasharray='2 3')
    + c(12, 17, 4, fill='white') + p('M12 17 V7')
    + accent('M6 5 H26 M9 2 6 5 9 8 M23 2 26 5 23 8'), 'assembly-mechanism')
add('joint-rack-pinion', 'Rack and pinion mate', 'ラック・ピニオン合致',
    'Couple pinion rotation to rack translation using the specified pitch radius.',
    '指定したピッチ半径でピニオン回転とラックの並進を連動させます。',
    p('M3 22 H7 V18 H11 V22 H15 V18 H19 V22 H23 V18 H27 V22 H29 V27 H3Z', fill=PALE)
    + c(16, 11, 6, fill=PALE) + p('M16 3 V6 M8 11 H11 M21 11 H24 M11 6 13 8 M21 6 19 8')
    + c(16, 11, 1.5) + accent('M5 30 H26 M23 28 26 30 23 31'), 'assembly-mechanism')
add('magnetic-mates', 'Magnetic mates', 'マグネット合致',
    'Snap component connection points together using magnetic mate connections.',
    'マグネット合致の接続点を使ってコンポーネントを吸着配置します。',
    fill('M4 4 H10 V15 Q10 21 16 21 Q22 21 22 15 V4 H28 V15 Q28 27 16 27 Q4 27 4 15Z')
    + p('M4 10 H10 M22 10 H28')
    + accent('M10 4 H14 M12 2 14 4 12 6 M22 4 H18 M20 2 18 4 20 6'), 'assembly-mates')
add('make-smart-component', 'Make smart component', 'スマート構成部品を作成',
    'Define a component with associated parts and features for automatic insertion.',
    '関連部品とフィーチャを含む自動挿入用のスマート構成部品を定義します。',
    block(9, 3, 14, 10) + p('M16 16 V21 M6 21 H26 M6 21 V25 M26 21 V25')
    + r(3, 25, 6, 5, 1, fill=PALE) + c(16, 27.5, 2.5, fill=PALE)
    + p('M23 30 V25 H29 V30', stroke=TEAL), 'assembly-library')

# Assembly relations: geometry expresses the relation, not a generic chain badge.
add('mate-angle', 'Angle mate', '角度合致',
    'Maintain a specified angle between assembly entities.',
    'アセンブリの要素間に指定した角度を維持します。',
    fill('M4 25 H28 V29 H4Z M4 25 18 4 22 7 8 28Z')
    + accent('M12 24 A12 12 0 0 0 9 16 M13 19 12 24 17 23')
    + p('M4 25 24 13', stroke_dasharray='2 3'), 'assembly-mates')
add('mate-distance', 'Distance mate', '距離合致',
    'Maintain a specified separation between assembly entities.',
    'アセンブリの要素間に指定した間隔を維持します。',
    fill('M3 7 H8 V27 H3Z M24 7 H29 V27 H24Z')
    + accent('M8 16 H24 M12 12 8 16 12 20 M20 12 24 16 20 20')
    + p('M8 3 V8 M24 3 V8 M8 4 H24', stroke_dasharray='2 2'), 'assembly-mates')
add('mate-in-place', 'In-place mate', '位置固定合致',
    'Fix an in-context component to its current location in the parent assembly.',
    '親アセンブリ内で作成した部品を現在の位置に固定します。',
    p('M3 9 V3 H9 M23 3 H29 V9 M3 23 V29 H9 M23 29 H29 V23')
    + block(9, 8, 14, 10)
    + accent('M10 25 H22 M12 25 9 28 M18 25 15 28 M24 25 21 28'), 'assembly-mates')
add('mate-lock-sketch', 'Lock to layout sketch', 'レイアウトスケッチに固定',
    'Constrain a component to a layout sketch rather than to another solid component.',
    '別のソリッド部品ではなく、レイアウトスケッチにコンポーネントを拘束します。',
    p('M3 26 12 17 28 22 M8 28 17 19 M12 17 V7', stroke_dasharray='3 2')
    + block(13, 4, 12, 10) + accent('M19 17 V23 H12 M15 20 12 23 15 26')
    + c(12, 23, 2, fill='white'), 'assembly-mates')
add('mate-path', 'Path mate', 'パス合致',
    'Constrain a component point to move along a selected curve.',
    '選択した曲線に沿ってコンポーネント上の点が移動するよう拘束します。',
    accent('M3 27 Q6 13 15 20 Q25 28 28 5 M24 7 28 5 30 9')
    + block(9, 4, 12, 10) + p('M15 17 V20') + c(15, 20, 2.5, fill='white', stroke=TEAL), 'assembly-mates')
add('mate-profile-center', 'Profile center mate', '輪郭中心合致',
    'Center assembly profiles relative to each other and control their orientation.',
    'アセンブリの輪郭同士を中心合わせし、向きを拘束します。',
    r(3, 6, 26, 20, 2) + p('M16 3 V29 M1 16 H31', stroke_dasharray='2 3')
    + p('M16 10 22 16 16 22 10 16Z', fill=PALE, stroke=TEAL)
    + c(16, 16, 2, fill=TEAL, stroke=TEAL), 'assembly-mates')
add('mate-width', 'Width mate', '幅合致',
    'Center or position a component tab between two planar boundaries.',
    '二つの平面境界の間で部品タブを中心配置または位置決めします。',
    fill('M3 6 H7 V25 H25 V6 H29 V29 H3Z') + r(12, 5, 8, 16, 1, fill=PALE)
    + accent('M7 15 H12 M9 12 12 15 9 18 M25 15 H20 M23 12 20 15 23 18')
    + p('M16 2 V29', stroke_dasharray='2 3'), 'assembly-mates')

# Mold tooling and keyed assembly motion.
add('mold-cavity', 'Create mold cavity', '金型キャビティを作成',
    'Create cavity geometry from a design part with mold reference and shrinkage settings.',
    '設計部品を参照し、金型の参照・収縮設定に従ってキャビティ形状を作成します。',
    fill('M3 14 16 8 29 14 V25 L16 30 3 25Z') + p('M3 14 16 20 29 14 M16 20 V30')
    + p('M9 13 Q16 7 23 13 V17 Q16 23 9 17Z', fill='white', stroke=TEAL)
    + accent('M16 2 V10 M13 7 16 10 19 7'), 'mold-tooling')
add('mold-core', 'Create side core', 'スライドコアを作成',
    'Create a side or sliding core that forms an undercut in a molded part.',
    '成形部品のアンダーカットを形成するサイドコア・スライドコアを作成します。',
    fill('M3 6 H18 V12 H24 V22 H18 V28 H3Z')
    + p('M18 12 H29 V22 H18Z', fill='white')
    + accent('M19 17 H30 M27 14 30 17 27 20') + p('M8 9 V25', stroke_dasharray='2 3'), 'mold-tooling')
add('mold-parting-surface', 'Create parting surface', 'パーティング面を作成',
    'Extend a separating mold surface outward from the parting line.',
    'パーティングラインから外側へ金型を分離する面を延長します。',
    p('M10 8 Q16 3 22 8 V24 Q16 29 10 24Z')
    + p('M2 14 14 8 30 17 18 25Z', fill=PALE)
    + accent('M10 16 Q16 21 22 16 M4 15 9 17 M23 18 28 19')
    + p('M10 8 Q16 13 22 8'), 'mold-tooling')
add('motion-study', 'Create motion study', 'モーションスタディを作成',
    'Create a keyed timeline of component motion in a CAD assembly.',
    'CADアセンブリのコンポーネント運動をキーフレーム付き時間軸で作成します。',
    block(4, 3, 9, 8) + p('M13 11 23 7', stroke_dasharray='2 3') + c(25, 7, 3, fill=PALE)
    + p('M3 21 H29 M3 29 H29 M8 18 V30')
    + p('M8 18 11 21 8 24 5 21Z M23 26 26 29 23 31 20 29Z', fill=TEAL, stroke=TEAL), 'assembly-motion')

# Patterns deliberately encode their placement driver and instance topology.
add('pattern-chain', 'Chain component pattern', 'チェーン構成部品パターン',
    'Pattern connected chain links along a path while retaining link relationships.',
    'リンク関係を維持しながら、連結したチェーン部品をパスに沿って配列します。',
    p('M4 27 Q4 6 27 6', stroke_dasharray='2 3')
    + g(r(3, 18, 8, 12, 4, fill=PALE), transform='rotate(18 7 24)')
    + g(r(9, 9, 8, 12, 4, fill=PALE), transform='rotate(44 13 15)')
    + g(r(20, 3, 8, 12, 4, fill=PALE), transform='rotate(75 24 9)')
    + accent('M8 21 12 16 M16 12 21 10'), 'component-pattern')
add('pattern-driven-pattern', 'Pattern-driven component pattern', '既存パターン駆動配列',
    'Place component instances using the locations of an existing feature or component pattern.',
    '既存のフィーチャまたは部品パターンの位置を使って部品を配列します。',
    p('M6 8 V20 M16 8 V20 M26 8 V20', stroke_dasharray='2 3')
    + c(6, 7, 3) + c(16, 7, 3) + c(26, 7, 3)
    + r(3, 21, 6, 7, 1, fill=PALE) + r(13, 21, 6, 7, 1, fill=PALE) + r(23, 21, 6, 7, 1, fill=PALE)
    + accent('M13 16 16 19 19 16'), 'component-pattern')
add('pattern-fill', 'Fill pattern', '領域フィルパターン',
    'Fill a bounded region with repeated feature instances.',
    '境界で囲まれた領域にフィーチャを繰り返し配置します。',
    fill('M4 4 H28 V18 L19 28 H4Z')
    + ''.join(c(x, y, 2, fill='white', stroke=TEAL) for x, y in [(10,10),(21,10),(10,20),(21,20)]), 'feature-pattern')
add('pattern-sketch-points', 'Sketch-driven pattern', 'スケッチ駆動パターン',
    'Place pattern instances at arbitrary points in a driving sketch.',
    '駆動スケッチ内の任意の点にパターンのインスタンスを配置します。',
    p('M5 25 10 8 26 14 21 26Z', stroke_dasharray='2 3')
    + r(2, 22, 6, 6, 1, fill=PALE) + r(7, 5, 6, 6, 1, fill=PALE)
    + r(23, 11, 6, 6, 1, fill=PALE) + r(18, 23, 6, 6, 1, fill=PALE)
    + ''.join(c(x, y, 1.2, fill=TEAL, stroke='none') for x, y in [(5,25),(10,8),(26,14),(21,26)]), 'feature-pattern')
add('pattern-table', 'Table-driven pattern', 'テーブル駆動パターン',
    'Place pattern instances at coordinates supplied in a table.',
    'テーブルで指定された座標にパターンのインスタンスを配置します。',
    r(3, 3, 13, 16, 1) + p('M3 8 H16 M3 13 H16 M9 3 V19')
    + accent('M16 11 H23 V18 M20 15 23 18 26 15')
    + r(5, 24, 5, 5, 1, fill=PALE) + r(16, 21, 5, 5, 1, fill=PALE) + r(25, 26, 5, 5, 1, fill=PALE), 'feature-pattern')
add('pattern-variable', 'Variable pattern', '可変パターン',
    'Repeat features while varying their dimensions between instances.',
    'インスタンスごとに寸法を変えながらフィーチャを配列します。',
    r(3, 21, 5, 7, 1, fill=PALE) + r(12, 15, 6, 13, 1, fill=PALE)
    + r(22, 7, 7, 21, 1, fill=PALE)
    + accent('M4 15 24 3 M20 2 24 3 23 7') + p('M2 31 H30'), 'feature-pattern')
add('plastic-rest', 'Plastic rest feature', '樹脂支持座',
    'Create a support pedestal with a planar or round contact footprint on a plastic part.',
    '樹脂部品に平面または円形の接触面を持つ支持座を作成します。',
    p('M3 28 H29 M6 25 H26', stroke_dasharray='2 3')
    + fill('M7 25 11 12 H21 L25 25Z') + fill('M8 8 H24 V13 H8Z')
    + accent('M8 8 H24') + p('M12 25 V18 H20 V25'), 'plastic-feature')

# Primitive construction is distinct from a tree object or measurement command.
add('primitive-cylinder', 'Create cylinder', '円柱を作成',
    'Create a cylindrical solid primitive from radius and height.',
    '半径と高さを指定して円柱ソリッドを作成します。',
    p('M7 9 C7 3 25 3 25 9 V25 C25 31 7 31 7 25Z', fill=PALE)
    + p('M7 9 C7 15 25 15 25 9')
    + accent('M16 9 H25 M22 6 25 9 22 12') + p('M3 9 V25 M1 9 H5 M1 25 H5'), 'solid-primitive')
add('primitive-sphere', 'Create sphere', '球を作成',
    'Create a spherical solid primitive from a center and radius.',
    '中心と半径を指定して球ソリッドを作成します。',
    c(16, 16, 12, fill=PALE) + p('M4 16 Q16 25 28 16 M16 4 C5 10 5 22 16 28')
    + accent('M16 16 24 8 M20 8 H24 V12') + c(16, 16, 1.5, fill=TEAL, stroke=TEAL), 'solid-primitive')
add('primitive-torus', 'Create torus', 'トーラスを作成',
    'Create a toroidal solid primitive from ring and section radii.',
    'リング半径と断面半径を指定してトーラスソリッドを作成します。',
    p('M3 16 C3 3 29 3 29 16 C29 29 3 29 3 16Z', fill=PALE)
    + p('M10 15 C10 9 22 9 22 15 C22 21 10 21 10 15Z', fill='white')
    + p('M10 15 Q16 12 22 15') + accent('M16 15 H28 M25 12 28 15 25 18'), 'solid-primitive')
add('primitive-cone', 'Create cone', '円錐を作成',
    'Create a conical solid primitive from bottom and top radii and height.',
    '底面と上面の半径、高さを指定して円錐ソリッドを作成します。',
    p('M7 25 L16 4 L25 25 C25 31 7 31 7 25Z', fill=PALE)
    + p('M7 25 C7 19 25 19 25 25')
    + accent('M16 25 H25 M22 22 25 25 22 28') + p('M3 4 V25 M1 4 H5 M1 25 H5'), 'solid-primitive')

# Repair, ownership and reference replacement are not rigid transforms.
add('repair-mates', 'Repair assembly mates', 'アセンブリ合致を修復',
    'Repair broken mate references in an assembly.',
    'アセンブリ内で壊れた合致参照を修復します。',
    r(3, 6, 8, 14, 1, fill=PALE) + r(21, 6, 8, 14, 1, fill=PALE)
    + p('M11 12 H14 M18 12 H21', stroke_dasharray='2 2')
    + accent('M9 25 H23 M12 22 9 25 12 28 M20 22 23 25 20 28')
    + p('M11 12 H21 M14 9 V15 M18 9 V15', stroke=TEAL), 'assembly-repair')
add('repair-pattern', 'Repair component pattern', '構成部品パターンを修復',
    'Repair failed references in an assembly component pattern.',
    'アセンブリの部品パターンで無効になった参照を修復します。',
    r(3, 5, 6, 8, 1, fill=PALE) + r(13, 5, 6, 8, 1, stroke_dasharray='2 2')
    + r(23, 5, 6, 8, 1, fill=PALE)
    + accent('M27 20 C23 29 8 29 4 20 M4 25 V20 H9 M16 21 V13 M13 16 16 13 19 16'), 'assembly-repair')
add('reparent-geometry', 'Move geometry to component', '形状の所属コンポーネントを変更',
    'Change the owning component of selected geometry without changing its world position.',
    'ワールド座標での位置を変えずに、選択形状の所属コンポーネントを変更します。',
    r(3, 3, 9, 7, 1, fill=PALE) + r(20, 3, 9, 7, 1, fill=PALE)
    + p('M7 10 V23 H14', stroke_dasharray='2 2')
    + block(13, 19, 8, 8) + accent('M24 10 V23 H21 M24 14 27 17 M24 14 21 17'), 'assembly-structure')
add('replace-mate-reference', 'Replace mate entities', '合致参照を置換',
    'Retarget an existing mate to different faces or other geometric entities.',
    '既存の合致を別の面や幾何要素へ付け替えます。',
    r(3, 11, 7, 12, 1, fill=PALE)
    + p('M26 3 V12 M26 21 V30 M10 17 H17 L26 8', stroke_dasharray='2 2')
    + accent('M17 17 26 25 M20 25 H26 V19 M20 11 V20 M17 17 20 20 23 17'), 'assembly-references')
add('replace-with-linked-component', 'Replace with linked component', 'リンク部品に置換',
    'Replace independent component definitions with a linked source while remapping their instances.',
    'インスタンスを再対応付けして、独立した部品定義をリンク元の部品に置き換えます。',
    block(3, 3, 9, 8) + block(20, 17, 9, 8)
    + accent('M15 7 H25 V15 M22 12 25 15 28 12')
    + p('M9 20 6 23 A3 3 0 0 0 10 27 L14 23 M12 24 15 21 A3 3 0 0 0 11 17 L8 20'), 'assembly-references')
add('revert-position', 'Revert component position', 'コンポーネント位置を復元',
    'Discard pending placement edits and restore the last captured component position.',
    '保留中の配置編集を破棄し、最後に記録したコンポーネント位置へ戻します。',
    p('M3 14 8 11 13 14 V23 L8 26 3 23Z M3 14 8 17 13 14 M8 17 V26', stroke_dasharray='2 2')
    + block(20, 12, 9, 10)
    + accent('M25 8 Q16 1 8 8 M8 3 V8 H13'), 'assembly-position')
add('save-motion-trace', 'Keep motion trace', 'モーション軌跡をスケッチ化',
    'Create a persistent associative sketch from a sampled assembly component trajectory.',
    'サンプリングした部品運動の軌跡から、関連付けられた永続スケッチを作成します。',
    p('M3 27 H29 M3 27 V7', stroke_dasharray='2 3')
    + accent('M6 23 Q13 6 23 20') + c(6, 23, 1.5, fill='white') + c(14, 15, 1.5, fill='white')
    + c(23, 20, 1.5, fill='white') + p('M23 14 V18') + block(18.5, 3, 9, 8), 'assembly-motion')
add('segment-mesh', 'Segment imported mesh', 'インポートメッシュを領域分割',
    'Partition an imported mesh into recognized facet or face regions.',
    'インポートしたメッシュを認識されたファセット・面領域に分割します。',
    p('M3 7 16 3 29 9 25 27 10 29 3 18Z', fill=PALE)
    + p('M3 7 12 13 16 3 20 16 29 9 M3 18 12 13 10 29 20 16 25 27')
    + accent('M12 4 12 13 20 16 18 28'), 'mesh-processing')

# Sheet-metal construction and manufacturing operations.
add('sheet-base-flange', 'Base flange or tab', 'ベースフランジ・タブ',
    'Create a constant-thickness base sheet or add a coplanar tab.',
    '一定厚さのベース板を作成するか、同一平面上のタブを追加します。',
    fill('M3 16 16 7 29 14 16 23Z') + p('M3 16 V21 L16 28 29 19 V14 M16 23 V28')
    + accent('M16 2 V9 M13 6 16 9 19 6'), 'sheet-metal')
add('sheet-bend-notch', 'Bend notch', '曲げ位置ノッチ',
    'Create locating notches where bend lines meet sheet edges.',
    '曲げ線が板の縁に達する位置に位置決めノッチを作成します。',
    fill('M4 5 H13 L16 10 19 5 H28 V27 H19 L16 22 13 27 H4Z')
    + accent('M16 10 V22', stroke_dasharray='3 2')
    + p('M13 5 16 10 19 5 M13 27 16 22 19 27', stroke=TEAL), 'sheet-metal')
add('sheet-close-corner', 'Close sheet corner', '板金コーナーを閉じる',
    'Extend adjacent flange faces to close their corner gap.',
    '隣接するフランジ面を延長してコーナーの隙間を閉じます。',
    fill('M3 26 V7 H10 V19 H22 V12 H29 V26Z')
    + p('M13 19 V26 M19 19 V26', stroke_dasharray='2 2')
    + accent('M5 14 H13 M10 11 13 14 10 17 M27 8 H19 M22 5 19 8 22 11'), 'sheet-metal')
add('sheet-cross-break', 'Sheet cross-break', '板金クロスブレーク',
    'Add shallow crossing stiffening bends to a sheet panel.',
    '板金パネルに交差する浅い補強曲げを追加します。',
    fill('M3 10 23 4 29 22 9 28Z')
    + accent('M3 10 16 14 29 22 M23 4 16 14 9 28')
    + p('M16 14 V19', stroke_dasharray='2 2'), 'sheet-metal')
add('sheet-gusset', 'Sheet-metal gusset', '板金ガセット',
    'Form a reinforcing deformation across an existing sheet-metal bend.',
    '既存の板金曲げをまたいで補強用の成形形状を作成します。',
    fill('M4 4 H9 V22 H28 V27 H4Z')
    + p('M9 10 Q15 17 23 22 L23 25 Q13 23 7 12Z', fill=PALE, stroke=TEAL)
    + p('M9 10 V22 H23', stroke_dasharray='2 3'), 'sheet-metal')
add('sheet-insert-bends', 'Insert sheet bends', '板金曲げを挿入',
    'Add bend definitions and bend radii to an existing thin-walled part.',
    '既存の薄肉部品に曲げ定義と曲げ半径を追加します。',
    fill('M4 5 H9 V18 Q9 23 14 23 H28 V28 H12 Q4 28 4 20Z')
    + accent('M9 16 Q9 23 16 23 M12 15 A7 7 0 0 1 19 22')
    + p('M4 20 H17 M12 28 V17', stroke_dasharray='2 3'), 'sheet-metal')
add('sheet-lofted-bend', 'Lofted sheet bend', '板金ロフトベンド',
    'Create a sheet-metal transition between differing profiles.',
    '異なる輪郭間を接続する板金トランジションを作成します。',
    p('M10 5 H22 L29 24 16 29 3 24Z', fill=PALE)
    + p('M10 5 16 8 22 5 M16 8 V29 M10 5 8 24 M22 5 24 24')
    + p('M6 23 16 26 26 23 M12 7 H20', stroke=TEAL), 'sheet-metal')
add('sheet-normal-cut', 'Normal sheet cut', '板面に垂直なカット',
    'Make sheet-cut side walls perpendicular to the broad sheet faces for manufacture.',
    '製造に適した形状になるよう、切断面を板面に垂直（板厚方向に平行）にします。',
    fill('M3 13 H12 V21 H20 V13 H29 V26 H3Z')
    + p('M3 13 V9 H12 M20 9 H29 V13 M12 9 V21 M20 9 V21', stroke_dasharray='2 2')
    + accent('M16 2 V17 M13 14 16 17 19 14')
    + p('M21 21 H25 V17', stroke=TEAL), 'sheet-metal')
add('sheet-perforate', 'Perforate sheet', '板金に通気穴を作成',
    'Create a perforation field while respecting sheet margins and bend regions.',
    '板の余白と曲げ領域を考慮して、穴の配列を作成します。',
    fill('M3 5 H25 V21 L29 27 H7 L3 21Z')
    + p('M3 21 H25', stroke_dasharray='3 2')
    + ''.join(c(x, y, 2, fill='white') for x, y in [(8,10),(16,10),(8,17),(16,17)])
    + accent('M22 8 V18'), 'sheet-metal')
add('sheet-refold', 'Refold sheet metal', '板金を再曲げ',
    'Restore selected bends after a temporary sheet-metal unfold.',
    '板金の一時的な展開後に、選択した曲げを復元します。',
    p('M4 24 15 18 28 24 17 30Z', stroke_dasharray='2 3')
    + fill('M4 24 15 18 27 23 16 29Z M15 18 V6 L27 11 V23Z')
    + accent('M5 17 C1 9 5 4 12 5 M9 2 12 5 9 8'), 'sheet-metal')
add('sheet-rip', 'Rip sheet seam', '板金にリップを作成',
    'Open a narrow seam in a sheet body so that it can unfold.',
    '板金ボディを展開できるよう、細い切れ目を作成します。',
    p('M4 9 16 3 28 9 V24 L18 29 V15 L28 9 M4 9 14 15 V29 L4 24Z', fill=PALE)
    + accent('M16 14 V30') + p('M9 20 H13 M19 20 H23'), 'sheet-metal')
add('sheet-swept-flange', 'Swept sheet flange', 'スイープフランジ',
    'Sweep a constant-thickness sheet flange along a path.',
    'パスに沿って一定厚さの板金フランジをスイープします。',
    p('M4 25 C5 11 16 9 28 15 V7 C15 1 4 5 3 18Z', fill=PALE)
    + p('M4 25 C5 11 16 9 28 15 L26 20 C17 15 11 17 10 28Z', fill=PALE)
    + accent('M4 25 C5 11 16 9 28 15', stroke_dasharray='3 2'), 'sheet-metal')

# Solid feature profiles, physical material and cutting results.
add('solid-boundary', 'Boundary solid', '境界ボス・ベース',
    'Build a solid blend controlled by boundary profiles in two directions.',
    '二方向の境界輪郭で制御したソリッドのブレンドを作成します。',
    p('M4 24 C8 16 6 9 10 5 Q16 11 26 5 C22 13 25 18 28 23 Q16 29 4 24Z', fill=PALE)
    + p('M4 24 V28 Q16 32 28 27 V23')
    + accent('M8 15 Q16 21 25 15 M16 8 Q12 16 16 27'), 'solid-creation')
add('solid-boundary-cut', 'Boundary cut', '境界カット',
    'Remove a volume controlled by boundary profiles in two directions.',
    '二方向の境界輪郭で制御した体積をソリッドから除去します。',
    fill('M3 8 H29 V28 H3Z')
    + p('M8 7 Q16 12 24 7 C19 14 21 20 26 23 Q16 28 6 23 C11 17 13 13 8 7Z', fill='white')
    + accent('M10 15 Q16 20 22 15 M16 10 Q13 17 16 25', stroke_dasharray='3 2'), 'solid-cut')
add('solid-coil', 'Create solid coil', 'ソリッドコイルを作成',
    'Create a solid helical coil with a finite cross-section.',
    '厚みを持つ断面で螺旋状のソリッドコイルを作成します。',
    p('M7 6 C7 1 25 1 25 6 C25 12 7 11 7 17 C7 23 25 22 25 27 L22 29 C22 25 4 26 4 20 C4 13 22 15 22 9 C22 5 10 4 10 7Z', fill=PALE)
    + p('M7 14 C7 9 25 9 25 14 C25 20 7 19 7 25 L10 28 C10 23 28 23 28 17 C28 11 10 13 10 9Z', fill=PALE)
    + accent('M7 6 C7 11 25 10 25 14 M7 17 C7 22 25 21 25 27'), 'solid-creation')
add('solid-pipe', 'Create solid pipe', 'ソリッドパイプを作成',
    'Sweep a round or hollow section along a path curve into a solid pipe.',
    '円形または中空の断面を経路曲線に沿って掃引し、ソリッドのパイプを作成します。',
    p('M4 28 V16 C4 9 9 4 16 4 H26 V12 H16 C14 12 12 14 12 16 V28Z', fill=PALE)
    + p('M26 4 C29 4 29 12 26 12 C23 12 23 4 26 4Z', fill='white')
    + p('M26 6.5 C27.2 6.5 27.2 9.5 26 9.5 C24.8 9.5 24.8 6.5 26 6.5Z')
    + accent('M8 28 V16 C8 11 11 8 16 8 H23', stroke_dasharray='3 2'), 'solid-creation')
add('solid-dome', 'Dome feature', 'ドームフィーチャ',
    'Bulge a selected face into a dome-shaped solid feature.',
    '選択面を膨らませてドーム状のソリッドフィーチャを作成します。',
    p('M4 22 C5 2 27 2 28 22 Q16 29 4 22Z', fill=PALE)
    + p('M4 22 V26 Q16 32 28 26 V22 M4 22 Q16 16 28 22', stroke_dasharray='3 2')
    + accent('M16 22 V7 M13 10 16 7 19 10'), 'solid-deformation')
add('solid-flex', 'Flex solid', 'ソリッドをフレックス変形',
    'Bend, twist, taper or stretch a solid body with a flex feature.',
    'フレックスフィーチャでソリッドを曲げ・ねじり・テーパ・伸縮変形します。',
    p('M5 28 V6 H12 V28', stroke_dasharray='3 2')
    + p('M5 28 C5 17 11 9 26 5 L29 12 C18 15 13 21 13 28Z', fill=PALE)
    + p('M26 5 23 11 29 12 M23 11 C13 14 9 20 9 28')
    + accent('M14 5 Q19 2 25 2 M22 1 25 2 23 5'), 'solid-deformation')
add('solid-indent', 'Indent solid', 'ソリッドにインデントを作成',
    'Form a shape-fitting indentation around tool bodies with thickness or clearance.',
    '工具ボディに沿って、厚みやすきまを持つくぼみを作成します。',
    fill('M3 18 H8 Q8 27 16 27 Q24 27 24 18 H29 V30 H3Z')
    + p('M11 6 H21 V17 Q21 23 16 23 Q11 23 11 17Z', fill=PALE)
    + accent('M16 2 V10 M13 7 16 10 19 7')
    + p('M7 15 H10 M22 15 H25'), 'solid-deformation')
add('solid-loft-cut', 'Lofted cut', 'ロフトカット',
    'Remove material through a blend of multiple cutting sections.',
    '複数の切断断面をブレンドした体積を除去します。',
    fill('M3 5 H29 V29 H3Z')
    + p('M8 7 Q16 3 24 7 C19 14 20 22 22 26 Q16 30 10 26 C12 19 13 14 8 7Z', fill='white')
    + p('M8 7 Q16 12 24 7 M10 26 Q16 22 22 26', stroke=TEAL)
    + p('M16 10 V24', stroke=TEAL, stroke_dasharray='3 2'), 'solid-cut')
add('solid-revolve-cut', 'Revolved cut', '回転カット',
    'Remove material by revolving a cutting profile about an axis.',
    '軸の周りに切断輪郭を回転させて材料を除去します。',
    fill('M4 5 H28 V27 H4Z')
    + p('M16 10 C3 10 3 23 16 23 C29 23 29 10 16 10Z M16 14 C23 14 23 19 16 19 C9 19 9 14 16 14Z', fill='white', fill_rule='evenodd')
    + p('M16 2 V30', stroke_dasharray='3 2')
    + accent('M7 13 A10 6 0 0 1 25 14 M22 11 25 14 27 10'), 'solid-cut')
add('solid-stud', 'Create threaded stud', 'ねじスタッドを作成',
    'Create a standard threaded protrusion attached to a solid part.',
    'ソリッド部品に接続した標準ねじ突起を作成します。',
    fill('M3 23 16 18 29 23 V27 L16 31 3 27Z')
    + p('M11 6 Q16 2 21 6 V23 Q16 27 11 23Z', fill=PALE)
    + p('M11 6 Q16 10 21 6 M11 11 21 8 M11 16 21 13 M11 21 21 18')
    + accent('M25 16 V4 M22 7 25 4 28 7'), 'solid-creation')
add('solid-surface-cut', 'Cut with surface', 'サーフェスでカット',
    'Remove the side of a solid selected by an intersecting surface tool.',
    '交差するサーフェスを工具として、指定した側のソリッドを除去します。',
    p('M5 4 H26 V14', stroke_dasharray='3 2')
    + fill('M5 15 Q15 7 26 15 V28 H5Z')
    + p('M2 17 Q14 4 30 16', stroke=TEAL)
    + accent('M16 11 V2 M13 5 16 2 19 5'), 'solid-cut')
add('solid-sweep-cut', 'Swept cut', 'スイープカット',
    'Remove material using a cutting section swept along a path.',
    'パスに沿って切断断面をスイープして材料を除去します。',
    fill('M3 4 H29 V29 H3Z')
    + p('M7 29 V19 C7 7 19 5 29 10 V18 C21 13 15 14 15 22 V29Z', fill='white')
    + accent('M11 27 V20 C11 10 20 9 27 14 M23 10 27 14 22 16'), 'solid-cut')
add('solid-thicken-cut', 'Thickened surface cut', '厚み付きサーフェスカット',
    'Remove a thin solid region generated by thickening a surface.',
    'サーフェスに厚みを付けて生成した薄い領域をソリッドから除去します。',
    fill('M3 5 H29 V28 H3Z')
    + p('M3 12 Q16 3 29 12 V19 Q16 10 3 19Z', fill='white', stroke=TEAL)
    + p('M3 15.5 Q16 6.5 29 15.5', stroke_dasharray='3 2')
    + accent('M16 19 V26 M13 23 16 26 19 23'), 'solid-cut')
add('texture-to-geometry', 'Texture to 3D geometry', 'テクスチャを立体形状に変換',
    'Convert a texture appearance into physical three-dimensional mesh relief.',
    'テクスチャの外観を実体のある三次元メッシュの起伏に変換します。',
    r(3, 3, 11, 9, 1) + p('M3 7 H14 M8 3 V12')
    + p('M4 27 9 17 15 23 22 15 29 24 24 29 15 27 9 30Z', fill=PALE)
    + p('M9 17 9 30 M15 23 V27 M22 15 24 29 M4 27 15 23 29 24')
    + accent('M20 3 V11 M17 8 20 11 23 8'), 'geometry-conversion')


# Frozen command aliases and provenance supplied by the reviewed audit.
_TRACE = {'activate-component': {'aliases': ['component.activate', 'Edit Component'],
                        'sources': ['gui-audit-e00cc276d0', 'gui-audit-8a41850734']},
 'assembly-contact': {'aliases': ['contact.enable_sets',
                                  'contact.enable_all',
                                  'contact.disable_all',
                                  'contact.create'],
                      'sources': ['gui-audit-952753343a']},
 'assembly-to-multibody': {'aliases': ['Make Multibody Part'], 'sources': ['gui-audit-8a41850734']},
 'assembly-visualization': {'aliases': ['Assembly Visualization'], 'sources': ['gui-audit-4396f7e3ba']},
 'belt-chain': {'aliases': ['Belt/Chain', 'Belt'],
                'sources': ['gui-audit-8a41850734', 'gui-audit-1bed7f8e51', 'gui-audit-682bbc8192']},
 'bodies-to-components': {'aliases': ['component.from_bodies'], 'sources': ['gui-audit-e00cc276d0']},
 'bounding-solid': {'aliases': ['solid.bounding_solid'], 'sources': ['gui-audit-5b19650212']},
 'brep-to-mesh': {'aliases': ['Convert to Mesh Body'], 'sources': ['gui-audit-c2a5f59b1b']},
 'capture-position': {'aliases': ['component.capture_position'], 'sources': ['gui-audit-2bf9f54b30']},
 'component-loading-state': {'aliases': ['Selective Open in Lightweight',
                                         'Set All to Resolved',
                                         'Set All to Lightweight',
                                         'Open in Lightweight'],
                             'sources': ['gui-audit-8a41850734']},
 'component-preview': {'aliases': ['Component Preview Window'], 'sources': ['gui-audit-8a41850734']},
 'copy-with-mates': {'aliases': ['Copy with Mates'], 'sources': ['gui-audit-8a41850734']},
 'create-weldment': {'aliases': ['Weldment'], 'sources': ['gui-audit-aa090f2a75']},
 'datum-point': {'aliases': ['construct.point.vertex',
                             'construct.point.two_edges',
                             'construct.point.three_planes',
                             'construct.point.center',
                             'construct.point.edge_plane',
                             'construct.point.along_path'],
                 'sources': ['gui-audit-48d928339e']},
 'derive-part': {'aliases': ['Create Derived Parts'], 'sources': ['gui-audit-c2a5f59b1b']},
 'direct-feature-edit': {'aliases': ['Instant3D'], 'sources': ['gui-audit-c2a5f59b1b']},
 'disable-external-references': {'aliases': ['No External References'], 'sources': ['gui-audit-8a41850734']},
 'explode-lines': {'aliases': ['Explode Line Sketch', 'Insert/Edit Smart Explode Lines'],
                   'sources': ['gui-audit-8a41850734']},
 'find-equivalent-components': {'aliases': ['component.copies'], 'sources': ['gui-audit-e00cc276d0']},
 'flexible-part': {'aliases': ['Make Part Flexible'], 'sources': ['gui-audit-8a41850734']},
 'flexible-subassembly': {'aliases': ['Flexible or Rigid'], 'sources': ['gui-audit-8a41850734']},
 'grid-system': {'aliases': ['Grid System'], 'sources': ['gui-audit-c2a5f59b1b']},
 'heal-edges': {'aliases': ['Heal Edges'], 'sources': ['gui-audit-c2a5f59b1b']},
 'insert-fastener': {'aliases': ['parts.fastener', 'parts.insert', 'Smart Fasteners'],
                     'sources': ['gui-audit-3abc9063cf', 'gui-audit-c977662189', 'gui-audit-8a41850734']},
 'insert-structural-profile': {'aliases': ['frame.profile.insert'], 'sources': ['gui-audit-2f3c6a71c2']},
 'joint-cam': {'aliases': ['joint.cam', 'Cam'], 'sources': ['gui-audit-952753343a', 'gui-audit-682bbc8192']},
 'joint-origin': {'aliases': ['joint.origin'], 'sources': ['gui-audit-5b19650212']},
 'joint-pin-slot': {'aliases': ['Slot', 'Slot - Locked', 'Slot - Unlocked'],
                    'sources': ['gui-audit-682bbc8192']},
 'joint-rack-pinion': {'aliases': ['joint.rack_pinion', 'Rack and Pinion'],
                       'sources': ['gui-audit-952753343a', 'gui-audit-682bbc8192']},
 'magnetic-mates': {'aliases': ['Magnetic Mates'], 'sources': ['gui-audit-4396f7e3ba']},
 'make-smart-component': {'aliases': ['Make Smart Component'], 'sources': ['gui-audit-8a41850734']},
 'mate-angle': {'aliases': ['Angle'], 'sources': ['gui-audit-682bbc8192']},
 'mate-distance': {'aliases': ['Distance'], 'sources': ['gui-audit-682bbc8192']},
 'mate-in-place': {'aliases': ['In Place'], 'sources': ['gui-audit-682bbc8192']},
 'mate-lock-sketch': {'aliases': ['Lock To Sketch'], 'sources': ['gui-audit-682bbc8192']},
 'mate-path': {'aliases': ['Path Mate'], 'sources': ['gui-audit-682bbc8192']},
 'mate-profile-center': {'aliases': ['Profile Center', 'Profile Center - Locked'],
                         'sources': ['gui-audit-682bbc8192']},
 'mate-width': {'aliases': ['Width'], 'sources': ['gui-audit-682bbc8192']},
 'mold-cavity': {'aliases': ['Cavity'], 'sources': ['gui-audit-319974c257']},
 'mold-core': {'aliases': ['Core'], 'sources': ['gui-audit-319974c257']},
 'mold-parting-surface': {'aliases': ['Parting Surfaces'],
                          'sources': ['gui-audit-f42456e152', 'gui-audit-319974c257']},
 'motion-study': {'aliases': ['motion.study', 'New Motion Study'],
                  'sources': ['gui-audit-952753343a', 'gui-audit-8a41850734']},
 'pattern-chain': {'aliases': ['Chain Component Pattern'], 'sources': ['gui-audit-8a41850734']},
 'pattern-driven-pattern': {'aliases': ['Pattern Driven Component Pattern'],
                            'sources': ['gui-audit-8a41850734']},
 'pattern-fill': {'aliases': ['Fill Pattern'], 'sources': ['gui-audit-c2a5f59b1b']},
 'pattern-sketch-points': {'aliases': ['Sketch Driven Pattern', 'Sketch Driven Component Pattern'],
                           'sources': ['gui-audit-8a41850734', 'gui-audit-c2a5f59b1b']},
 'pattern-table': {'aliases': ['Table Driven Pattern'], 'sources': ['gui-audit-c2a5f59b1b']},
 'pattern-variable': {'aliases': ['Variable Pattern'], 'sources': ['gui-audit-c2a5f59b1b']},
 'plastic-rest': {'aliases': ['plastic.rest'], 'sources': ['gui-audit-73a2f59c6c']},
 'primitive-cone': {'aliases': ['solid.cone'], 'sources': ['gui-audit-5b19650212']},
 'primitive-cylinder': {'aliases': ['solid.cylinder'], 'sources': ['gui-audit-5b19650212']},
 'primitive-sphere': {'aliases': ['solid.sphere'], 'sources': ['gui-audit-5b19650212']},
 'primitive-torus': {'aliases': ['solid.torus'], 'sources': ['gui-audit-5b19650212']},
 'repair-mates': {'aliases': ['Auto Repair Mate'], 'sources': ['gui-audit-8a41850734']},
 'repair-pattern': {'aliases': ['Auto Repair Pattern'], 'sources': ['gui-audit-8a41850734']},
 'reparent-geometry': {'aliases': ['component.move_bodies', 'component.move_sketches'],
                       'sources': ['gui-audit-e00cc276d0']},
 'replace-mate-reference': {'aliases': ['Replace Mate Entities'], 'sources': ['gui-audit-8a41850734']},
 'replace-with-linked-component': {'aliases': ['component.replace_with_link'],
                                   'sources': ['gui-audit-e00cc276d0']},
 'revert-position': {'aliases': ['component.revert_position'], 'sources': ['gui-audit-2bf9f54b30']},
 'save-motion-trace': {'aliases': ['motion.trace.keep'], 'sources': ['gui-audit-1b7d149ee8']},
 'segment-mesh': {'aliases': ['Segmented Imported Mesh Body'], 'sources': ['gui-audit-c2a5f59b1b']},
 'sheet-base-flange': {'aliases': ['Base-Flange/Tab'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-bend-notch': {'aliases': ['Bend-Notch'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-close-corner': {'aliases': ['Closed Corner'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-cross-break': {'aliases': ['Cross-Break'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-gusset': {'aliases': ['Sheet Metal Gusset'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-insert-bends': {'aliases': ['Insert Bends'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-lofted-bend': {'aliases': ['Lofted-Bend'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-normal-cut': {'aliases': ['Normal Cut'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-perforate': {'aliases': ['sheet.perforate'], 'sources': ['gui-audit-749742060e']},
 'sheet-refold': {'aliases': ['sheet.refold', 'Fold'],
                  'sources': ['gui-audit-f87ed3acf1', 'gui-audit-710dd04d55']},
 'sheet-rip': {'aliases': ['Rip'], 'sources': ['gui-audit-710dd04d55']},
 'sheet-swept-flange': {'aliases': ['Swept Flange'], 'sources': ['gui-audit-710dd04d55']},
 'solid-boundary': {'aliases': ['Boundary Boss/Base'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-boundary-cut': {'aliases': ['Boundary Cut'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-coil': {'aliases': ['solid.coil'], 'sources': ['gui-audit-5b19650212']},
 'solid-pipe': {'aliases': ['solid.pipe', 'Pipe'], 'sources': ['gui-audit-5b19650212']},
 'solid-dome': {'aliases': ['Dome'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-flex': {'aliases': ['Flex'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-indent': {'aliases': ['Indent'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-loft-cut': {'aliases': ['Lofted Cut'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-revolve-cut': {'aliases': ['Revolved Cut'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-stud': {'aliases': ['Stud Wizard'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-surface-cut': {'aliases': ['Cut with Surface'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-sweep-cut': {'aliases': ['Swept Cut'], 'sources': ['gui-audit-c2a5f59b1b']},
 'solid-thicken-cut': {'aliases': ['Thickened Cut'], 'sources': ['gui-audit-c2a5f59b1b']},
 'texture-to-geometry': {'aliases': ['3D Texture'], 'sources': ['gui-audit-c2a5f59b1b']}}
for _item in ITEMS:
    _item.update(_TRACE[_item['id']])
