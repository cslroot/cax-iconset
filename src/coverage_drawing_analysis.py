"""Original drawing, annotation and model-evaluation command pictograms.

The source references describe command semantics, not artwork. Symbols are UI
schematics, not production drawing annotations or certified GD&T notation.
All artwork uses the existing 32 px, rounded 1.75 px engineering vocabulary.
"""

from core import p, r, c, accent, fill, PALE, TEAL, AMBER


VIEW = 'gui-audit-f30c7dc7d5'
EVALUATE = 'gui-audit-4396f7e3ba'
DRAWING = 'gui-audit-7830b955e2'
STANDARD = 'gui-audit-8f5f9d7f22'
ANNOTATION = 'gui-audit-32463001c1'
TABLE = 'gui-audit-9b51c95f92'
ASSEMBLY = 'gui-audit-8a41850734'

ITEMS = []


def add(id, name, ja, family, description, description_ja, body,
        tags, aliases, sources):
    ITEMS.append(dict(
        id=id, domain='CAD', name=name, nameJa=ja, family=family,
        description=description, descriptionJa=description_ja, role='command',
        tags=list(dict.fromkeys(tags + [family, 'CAD', name.lower(), ja])),
        aliases=aliases, sources=sources, body=body,
    ))


# Drawing views: the changing geometry is the command, not a corner badge.
add('3d-drawing-view', 'Manipulate drawing view in 3D', '図面ビューの3D操作',
    'drawing-view',
    'Temporarily rotate a drawing view out of its sheet plane to inspect or select obscured geometry.',
    '図面ビューを一時的にシート面外へ回転し、隠れた形状を確認または選択します。',
    r(3, 3, 26, 26, 1)
    + fill('M10 13 17 9 24 13 V21 L17 25 10 21Z')
    + p('M10 13 17 17 24 13 M17 17 V25')
    + accent('M7 19 C2 12 7 6 15 6 M12 3 15 6 12 9'),
    ['drawing', 'rotate', 'inspect', '図面', '回転', '隠れた形状'],
    ['3D Drawing View'], [VIEW])

add('3d-pmi-compare', 'Compare 3D PMI', '3D PMI比較', 'model-inspection',
    'Compare product and manufacturing information associated with two three-dimensional models.',
    '二つの3次元モデルに関連付けられた製品・製造情報を比較します。',
    fill('M3 13 8 10 13 13 V21 L8 24 3 21Z')
    + p('M3 13 8 16 13 13 M8 16 V24')
    + fill('M19 13 24 10 29 13 V21 L24 24 19 21Z')
    + p('M19 13 24 16 29 13 M24 16 V24')
    + accent('M3 5 H13 M3 3 V7 M13 3 V7 M19 5 H29 M19 3 V7 M29 3 V7')
    + p('M12 28 H20 M14 26 12 28 14 30 M18 26 20 28 18 30', stroke=TEAL),
    ['PMI', 'annotation', 'comparison', '製造情報', '注記', '比較'],
    ['3D PMI Compare'], [EVALUATE])

add('alternate-position-view', 'Alternate-position drawing view', '代替位置ビュー',
    'drawing-view',
    'Overlay an alternate component position on a drawing view using phantom-style geometry.',
    '図面ビューに部品の代替位置を仮想線の形状として重ねて表示します。',
    p('M5 27 H28') + c(8, 23, 4, fill=PALE)
    + fill('M9 19 26 19 V25 H12Z')
    + p('M7 19 18 4 23 8 12 23Z', stroke=TEAL, stroke_dasharray='3 2')
    + accent('M23 15 Q26 10 24 6 M21 7 24 6 26 9'),
    ['drawing', 'motion', 'overlay', '図面', '代替位置', '可動範囲'],
    ['Alternate Position View'], [DRAWING])

add('auto-generate-drawing', 'Auto-generate drawing', '図面の自動生成',
    'drawing-document',
    'Automatically populate a drawing with model views and associated drawing content.',
    'モデルのビューと関連する図面要素を自動配置して図面を生成します。',
    p('M3 11 V29 H29 V3 H13')
    + fill('M9 14 H17 V20 H9Z') + r(21, 14, 5, 6, 0, fill=PALE)
    + p('M9 24 H17 M9 22 V26 M17 22 V26 M21 24 H26')
    + accent('M8 2 9.5 6.5 14 8 9.5 9.5 8 14 6.5 9.5 2 8 6.5 6.5Z'),
    ['drawing', 'automatic', 'layout', '図面', '自動生成', '配置'],
    ['Auto-Generate Drawing'], [STANDARD])

add('auxiliary-view', 'Auxiliary drawing view', '補助投影ビュー', 'drawing-view',
    'Create a drawing view normal to a selected inclined edge or viewing direction.',
    '選択した傾斜エッジまたは投影方向に直交する補助投影ビューを作成します。',
    fill('M3 26 V18 L13 8 18 13 V26Z')
    + accent('M13 8 18 13')
    + p('M16 10 23 3 M19 13 28 4', stroke_dasharray='2 3')
    + fill('M22 3 29 10 24 15 17 8Z')
    + accent('M9 11 15 5 M11 5 H15 V9'),
    ['drawing', 'projection', 'inclined face', '図面', '補助投影', '傾斜面'],
    ['Auxiliary View'], [DRAWING])

add('broken-out-section', 'Broken-out section', '部分断面図', 'drawing-view',
    'Expose a local interior region of a drawing view with an irregular break boundary and specified depth.',
    '不規則な破断境界と深さを指定し、図面ビューの一部分だけを断面として表示します。',
    r(4, 5, 24, 23, 1, fill=PALE)
    + p('M4 15 C8 12 8 19 12 16 S17 13 19 18 25 17 28 20 V28 H4Z', fill='white')
    + p('M7 18 4 21 M12 18 4 26 M18 19 9 28 M24 21 17 28 M28 24 24 28', stroke=TEAL)
    + p('M10 10 H22', stroke_dasharray='2 3'),
    ['drawing', 'local section', 'break boundary', '図面', '部分断面', '破断'],
    ['Broken-out Section'], [DRAWING])

# Annotation pictograms intentionally omit real production tolerance values.
add('caterpillar', 'Caterpillar weld annotation', '溶接ビードの波形注記', 'drawing-annotation',
    'Annotate the visible length of a weld with a repeated caterpillar pattern, without creating weld geometry.',
    '溶接ビードの長手方向を波形の図面注記で示します。溶接形状は作成しません。',
    p('M3 8 H29 M3 24 H29')
    + accent('M7 11 Q1 16 7 21 M13 11 Q7 16 13 21 M19 11 Q13 16 19 21 M25 11 Q19 16 25 21')
    + p('M29 11 Q23 16 29 21'),
    ['weld', 'annotation', 'bead', '溶接', '図面注記', '波形'],
    ['Caterpillar'], [ANNOTATION])

add('center-mark', 'Center mark', '中心マーク', 'drawing-annotation',
    'Add a center mark to a circular drawing feature.',
    '図面の円形形状に中心マークを追加します。',
    c(16, 16, 9, fill=PALE)
    + accent('M16 3 V10 M16 13 V19 M16 22 V29 M3 16 H10 M13 16 H19 M22 16 H29'),
    ['center', 'circle', 'annotation', '中心', '円', '図面注記'],
    ['Center Mark'], [ANNOTATION])

add('centerline', 'Drawing centerline', '図面中心線', 'drawing-annotation',
    'Annotate a drawing feature with a centerline representing its axis or symmetry center.',
    '形状の軸や対称中心を示す中心線を図面に追加します。',
    r(7, 6, 18, 20, 1, fill=PALE)
    + p('M7 12 H25 M7 20 H25')
    + accent('M16 2 V9 M16 12 V14 M16 17 V20 M16 23 V30'),
    ['axis', 'centerline', 'drawing', '軸', '中心線', '図面'],
    ['Centerline'], [ANNOTATION])

add('check', 'Check model validity', 'モデル形状チェック', 'model-inspection',
    'Check solid and surface geometry for invalid faces, edges and other boundary-representation defects.',
    'ソリッドやサーフェスの面・エッジなどを調べ、境界表現の不正箇所を検出します。',
    fill('M4 10 14 5 24 10 V23 L14 28 4 23Z')
    + p('M4 10 14 15 24 10 M14 15 V28')
    + p('M18 24 24 31 31 18 28 16 23 24 21 21Z', fill='white', stroke='none')
    + accent('M20 24 24 28 30 18'),
    ['validity', 'B-rep', 'geometry', '妥当性', '境界表現', '形状検査'],
    ['Check'], [EVALUATE])

add('compare-boms', 'Compare bills of materials', '部品表の比較', 'model-inspection',
    'Compare component rows and properties in two bills of materials.',
    '二つの部品表の構成部品行やプロパティを比較します。',
    r(2, 4, 11, 20, 1) + r(19, 4, 11, 20, 1)
    + p('M2 10 H13 M6 4 V24 M2 17 H13 M19 10 H30 M23 4 V24 M19 17 H30')
    + r(7, 11, 5, 5, 0, fill=PALE, stroke='none')
    + r(24, 18, 5, 5, 0, fill=PALE, stroke='none')
    + accent('M8 29 H24 M11 26 8 29 11 31 M21 26 24 29 21 31'),
    ['BOM', 'table', 'compare', '部品表', '表', '比較'],
    ['Compare BOMs'], [EVALUATE])

add('compare-documents', 'Compare document properties', '文書プロパティ比較', 'model-inspection',
    'Compare document properties and file-level information between two model documents.',
    '二つのモデル文書のプロパティとファイル単位の情報を比較します。',
    p('M3 4 H10 L14 8 V25 H3Z M10 4 V8 H14 M18 4 H25 L29 8 V25 H18Z M25 4 V8 H29')
    + p('M6 13 H11 M6 18 H10 M21 13 H26')
    + accent('M21 18 H26 M11 29 H21 M13 27 11 29 13 31 M19 27 21 29 19 31'),
    ['document', 'properties', 'comparison', '文書', 'プロパティ', '比較'],
    ['Compare Documents'], [EVALUATE])

add('compare-features', 'Compare model features', 'フィーチャ比較', 'model-inspection',
    'Compare feature definitions and parameters between two parts, separately from geometric body comparison.',
    '二つの部品のフィーチャ定義とパラメータを比較します。ボディ形状だけの比較とは区別します。',
    p('M4 4 V22 H10 M4 10 H10 M20 4 V22 H26 M20 10 H26')
    + r(8, 6, 6, 7, 1, fill=PALE) + r(24, 6, 6, 7, 1, fill=PALE)
    + p('M8 18 H14 V25 H8Z M24 18 H30 V21 H27 V25 H24Z', fill=PALE)
    + accent('M9 29 H25 M12 27 9 29 12 31 M22 27 25 29 22 31'),
    ['feature', 'parameter', 'compare', 'フィーチャ', 'パラメータ', '比較'],
    ['Compare Features'], [EVALUATE])

add('costing', 'Estimate manufacturing cost', '製造コスト見積り', 'model-evaluation',
    'Estimate manufacturing cost using model geometry, materials and process assumptions.',
    'モデル形状、材料、工程の条件から製造コストを見積もります。',
    fill('M3 7 11 3 19 7 V18 L11 22 3 18Z')
    + p('M3 7 11 11 19 7 M11 11 V22')
    + p('M17 17 C17 13 29 13 29 17 V26 C29 30 17 30 17 26Z', fill='white')
    + accent('M17 17 C17 21 29 21 29 17 M17 22 C17 26 29 26 29 22'),
    ['cost', 'manufacturing', 'estimate', 'コスト', '製造', '見積り'],
    ['Costing'], [EVALUATE])

add('crop-view', 'Crop drawing view', '図面ビューのトリミング', 'drawing-view',
    'Restrict a drawing view to geometry inside a selected crop boundary.',
    '選択したトリミング境界の内側だけを図面ビューに表示します。',
    p('M4 4 H28 V28 H4Z', stroke_dasharray='2 3')
    + fill('M9 9 H23 V15 H18 V23 H9Z')
    + accent('M3 9 H9 V3 M29 23 H23 V29 M9 9 H26 M23 23 H6'),
    ['drawing', 'crop', 'boundary', '図面', 'トリミング', '境界'],
    ['Crop View'], [DRAWING])

add('datum-target', 'Datum target annotation', 'データムターゲット', 'drawing-annotation',
    'Identify a limited point, line or area used to establish a datum with a target annotation.',
    'データムを設定するための限定された点、線、領域をターゲット注記で示します。',
    fill('M3 24 12 18 21 24 12 29Z')
    + accent('M8 22 15 26 M15 22 8 26')
    + p('M12 22 19 15') + c(23, 9, 7, fill='white')
    + p('M16 9 H30 M21 5 H25 M22 12 H24'),
    ['datum', 'target', 'annotation', 'データム', 'ターゲット', '図面注記'],
    ['Datum Target'], [ANNOTATION])

add('dowel-pin-symbol', 'Dowel-pin drawing symbol', 'ダウエルピン記号', 'drawing-annotation',
    'Add a schematic dowel-pin symbol to a circular edge in a drawing.',
    '図面の円形エッジに位置決め用ダウエルピンの模式記号を追加します。',
    c(16, 16, 11)
    + p('M16 16 V5 A11 11 0 0 1 27 16Z M16 16 V27 A11 11 0 0 1 5 16Z', fill=PALE, stroke='none')
    + accent('M16 5 V27 M5 16 H27')
    + p('M3 3 7 7 M25 25 29 29'),
    ['dowel', 'pin', 'annotation', '位置決め', 'ピン', '図面記号'],
    ['Dowel Pin Symbol'], [ANNOTATION])

add('drawing-table', 'Insert drawing table', '図面テーブル挿入', 'drawing-table',
    'Insert a drawing table using a chosen general, hole, revision, weld, bend, punch or tolerance schema.',
    '一般、穴、改訂、溶接、曲げ、パンチ、公差などの形式を選び、図面テーブルを挿入します。',
    p('M3 4 H29 V28 H3Z')
    + r(7, 9, 18, 15, 0, fill=PALE)
    + p('M7 14 H25 M7 19 H25 M13 9 V24 M20 14 V24')
    + accent('M7 6 H17'),
    ['drawing', 'table', 'schema', '図面', '表', '一覧'],
    ['General Table', 'Hole Table', 'Revision Table', 'Weld Table',
     'Bend Table', 'Punch Table', 'General Tolerance Table'], [TABLE])

add('empty-view', 'Create empty drawing view', '空の図面ビュー', 'drawing-view',
    'Create an empty drawing-view container for drawing geometry without inserting a model view.',
    'モデルビューを挿入せず、作図要素を配置する空の図面ビューを作成します。',
    r(3, 3, 26, 26, 1)
    + r(8, 8, 16, 16, 0, stroke=TEAL, stroke_dasharray='3 3')
    + p('M6 26 H11 M6 26 V21'),
    ['drawing', 'empty', 'container', '図面', '空', 'ビュー'],
    ['Empty View'], [DRAWING])

add('end-treatment', 'Weld end-treatment annotation', '溶接端部の断面注記', 'drawing-annotation',
    'Represent a weld bead in end view with a drawing annotation, without adding weld geometry.',
    '溶接ビードを端面から見た断面注記として示します。溶接形状は追加しません。',
    fill('M4 4 H10 V22 H28 V28 H4Z')
    + p('M10 10 Q14 20 24 22 H10Z', fill=PALE, stroke=TEAL)
    + accent('M11 15 15 19 M11 20 13 22 M16 19 19 22'),
    ['weld', 'section', 'annotation', '溶接', '端面', '図面注記'],
    ['End Treatment'], [ANNOTATION])

add('envelope-publisher', 'Publish reference envelopes', '参照エンベロープの公開', 'assembly-reference',
    'Make selected top-level assembly components available as reference envelopes in a destination subassembly.',
    'トップレベルアセンブリの選択部品を、子アセンブリ内の参照エンベロープとして利用可能にします。',
    r(2, 3, 13, 15, 1, stroke_dasharray='3 2')
    + fill('M5 7 9 5 13 7 V13 L9 15 5 13Z')
    + r(17, 16, 13, 14, 1)
    + p('M20 20 H27 V27 H20Z', stroke=TEAL, stroke_dasharray='2 2')
    + accent('M16 7 H24 V13 M21 10 24 13 27 10'),
    ['assembly', 'envelope', 'reference', 'アセンブリ', 'エンベロープ', '参照'],
    ['Envelope Publisher'], [EVALUATE])

add('feature-paint', 'Copy feature parameters', 'フィーチャ属性の転写', 'feature-editing',
    'Copy eligible dimensional or appearance parameters from a source feature to selected target features.',
    '元フィーチャの寸法や外観など、転写可能なパラメータを選択フィーチャへコピーします。',
    fill('M3 15 H7 V8 H13 V27 H3Z')
    + fill('M19 27 V15 H25 V21 H29 V27Z')
    + accent('M10 4 H23 V10 M20 7 23 10 26 7')
    + p('M18 17 23 12 27 16 22 21Z', fill='white')
    + accent('M18 17 Q15 18 16 23 Q21 23 22 21'),
    ['feature', 'copy parameters', 'appearance', 'フィーチャ', '属性転写', '外観'],
    ['Feature Paint'], [EVALUATE])

add('find-modify-features', 'Find and modify features', 'フィーチャ検索と変更', 'feature-editing',
    'Find features matching specified criteria and change supported parameters on the matched features.',
    '指定条件に一致するフィーチャを検索し、該当フィーチャの対応パラメータを変更します。',
    p('M3 4 V26 H14 M3 9 H8 M3 18 H8')
    + r(8, 5, 7, 8, 1, fill=PALE)
    + c(21, 20, 7, fill='white') + p('M26 25 30 29')
    + accent('M17 18 H25 M17 22 H25 M20 16 V20 M23 20 V24'),
    ['feature', 'search', 'modify', 'フィーチャ', '検索', '変更'],
    ['Find/Modify Features'], [EVALUATE])

add('geometry-analysis', 'Analyze problematic geometry', '問題形状の解析', 'model-inspection',
    'Locate small faces, short edges, slivers, sharp features and discontinuities that can hinder downstream use.',
    '小さい面、短いエッジ、細長い面、鋭角部、不連続箇所など、後工程に影響する形状を検出します。',
    fill('M3 6 H25 V12 L19 13 22 27 H3Z')
    + p('M19 6 V13 L22 27', stroke=TEAL)
    + c(22, 16, 7, fill='white')
    + accent('M20 11 21 21 M24 11 21 21')
    + p('M27 21 30 25'),
    ['geometry', 'sliver', 'short edge', '形状解析', '微小面', '短いエッジ'],
    ['Geometry Analysis'], [EVALUATE])

add('hole-alignment-check', 'Check hole alignment', '穴位置合わせチェック', 'assembly-inspection',
    'Check whether corresponding holes in assembly components are aligned along a common axis.',
    'アセンブリの対応する穴が共通軸に沿って整列しているか検査します。',
    fill('M3 9 15 4 29 9 17 14Z')
    + fill('M3 23 15 18 29 23 17 28Z')
    + p('M11 9 C11 5 21 5 21 9 C21 13 11 13 11 9 M11 23 C11 19 21 19 21 23 C21 27 11 27 11 23')
    + accent('M16 2 V30', stroke_dasharray='3 3'),
    ['assembly', 'hole', 'coaxiality', 'アセンブリ', '穴', '同軸確認'],
    ['Hole Alignment'], [ASSEMBLY])

add('hole-callout', 'Hole callout', '穴寸法注記', 'drawing-annotation',
    'Add a model-linked hole callout describing the selected hole specification.',
    '選択した穴の仕様を示す、モデルに連動した穴寸法注記を追加します。',
    r(3, 17, 16, 12, 1, fill=PALE) + c(11, 23, 4)
    + p('M12 21 22 11 H30 M14 20 12 21 13 18')
    + c(23, 5, 3, stroke=TEAL) + accent('M20 8 26 2 M28 5 H30'),
    ['hole', 'callout', 'diameter', '穴', '寸法注記', '直径'],
    ['Hole Callout'], [ANNOTATION])

add('import-diagnostics', 'Diagnose imported geometry', 'インポート形状診断', 'model-inspection',
    'Identify and repair faulty faces or gaps in imported solid and surface geometry.',
    'インポートしたソリッドやサーフェスの不良面や隙間を診断・修復します。',
    p('M13 6 20 3 29 8 V24 L19 29 9 24 V15')
    + p('M9 15 19 20 29 15 M19 20 V29')
    + accent('M2 8 H13 M9 4 13 8 9 12')
    + p('M16 12 24 8', stroke_dasharray='2 3')
    + accent('M17 9 20 15 M21 7 24 13'),
    ['import', 'repair', 'gap', 'インポート', '修復', '隙間'],
    ['Import Diagnostics'], [EVALUATE])

add('location-label', 'Drawing location label', '図面位置ラベル', 'drawing-annotation',
    'Label the sheet or zone location of a related parent or child drawing view.',
    '関連する親ビューまたは子ビューのシート番号やゾーン位置をラベルで示します。',
    r(3, 3, 23, 25, 1) + p('M3 10 H26 M10 3 V28', stroke_dasharray='2 3')
    + r(5, 14, 6, 6, 0, fill=PALE) + p('M11 18 17 21')
    + c(23, 22, 7, fill='white') + accent('M16 22 H30 M21 18 H25 M22 26 H24'),
    ['drawing', 'zone', 'sheet location', '図面', 'ゾーン', 'シート位置'],
    ['Location Label'], [ANNOTATION])

add('magnetic-line', 'Align balloons on magnetic line', 'マグネットライン', 'drawing-annotation',
    'Arrange drawing balloons along a magnetic alignment line.',
    '図面のバルーンをマグネットラインに沿って整列させます。',
    accent('M3 8 H29')
    + c(7, 8, 3.5, fill='white') + c(16, 8, 3.5, fill='white') + c(25, 8, 3.5, fill='white')
    + p('M7 12 5 23 M16 12 V25 M25 12 27 23')
    + fill('M6 25 16 21 26 25 16 29Z'),
    ['balloon', 'alignment', 'magnetic', 'バルーン', '整列', '磁力線'],
    ['Magnetic Line'], [ANNOTATION])

add('make-assembly-from-part-assembly', 'Make assembly from model', 'モデルからアセンブリ作成',
    'assembly-document',
    'Create a new assembly document containing the current part or assembly as an initial component.',
    '現在の部品またはアセンブリを初期構成部品に含む、新しいアセンブリ文書を作成します。',
    fill('M3 7 8 4 13 7 V14 L8 17 3 14Z') + p('M3 7 8 10 13 7 M8 10 V17')
    + accent('M16 7 H25 V12 M22 9 25 12 28 9')
    + r(15, 15, 15, 15, 1) + p('M22 18 V22 H18 V25 M22 22 H27 V25')
    + r(17, 25, 3, 3, 0, fill=PALE) + r(25, 25, 3, 3, 0, fill=PALE),
    ['assembly', 'new document', 'component', 'アセンブリ', '新規文書', '構成部品'],
    ['Make Assembly from Part/Assembly'], [STANDARD])

add('model-items', 'Insert model annotations', 'モデルアイテム挿入', 'drawing-annotation',
    'Import selected model dimensions and annotations into a drawing view.',
    '選択したモデルの寸法や注記を図面ビューへ取り込みます。',
    fill('M3 10 8 7 13 10 V17 L8 20 3 17Z') + p('M3 10 8 13 13 10 M8 13 V20')
    + accent('M3 3 H13 M3 1 V5 M13 1 V5')
    + p('M17 11 H29 V29 H17Z') + r(20, 15, 6, 6, 0, fill=PALE)
    + accent('M20 25 H26 M20 23 V27 M26 23 V27 M8 24 H16 M13 21 16 24 13 27'),
    ['model', 'dimension', 'annotation transfer', 'モデル', '寸法', '注記転送'],
    ['Model Items'], [ANNOTATION])

add('multi-jog-leader', 'Multi-jog leader', '多段引出線', 'drawing-annotation',
    'Add an annotation leader with several adjustable bends to route around drawing content.',
    '図面要素を避けて配置できる、複数の折れ点を持つ引出線を追加します。',
    fill('M3 23 H13 V29 H3Z')
    + accent('M8 25 14 18 H20 V11 H29 M8 25 9 20 M8 25 13 24')
    + p('M22 5 H29 M22 8 H27'),
    ['leader', 'jog', 'annotation', '引出線', '多段', '図面注記'],
    ['Multi-jog Leader'], [ANNOTATION])

add('part-reviewer', 'Review part feature history', '部品フィーチャの順次確認', 'model-inspection',
    'Step through a part feature by feature to inspect its construction and associated comments.',
    '部品のフィーチャを順にたどり、作成過程と関連コメントを確認します。',
    fill('M5 9 12 5 19 9 V18 L12 22 5 18Z') + p('M5 9 12 13 19 9 M12 13 V22')
    + p('M22 4 H29 V13 H25 L22 16Z')
    + accent('M3 28 H28 M24 24 28 28 24 31')
    + c(6, 28, 2, fill='white') + c(14, 28, 2, fill=TEAL),
    ['history', 'feature', 'review', '作成履歴', 'フィーチャ', '順次確認'],
    ['Part Reviewer'], [EVALUATE])

add('parting-line-analysis', 'Analyze mold parting line', 'パーティングライン解析', 'mold-inspection',
    'Visualize candidate mold parting lines as the pull direction changes, without creating a parting-line feature.',
    '抜き方向に応じた金型分割線の候補を可視化します。分割線フィーチャは作成しません。',
    fill('M6 18 10 9 H22 L26 18 22 27 H10Z')
    + p('M6 18 Q16 13 26 18')
    + accent('M6 18 Q16 23 26 18 M16 10 V2 M13 5 16 2 19 5')
    + p('M10 9 16 12 22 9 M16 12 V17', stroke_dasharray='2 3'),
    ['mold', 'parting line', 'pull direction', '金型', '分割線', '抜き方向'],
    ['Parting Line Analysis'], [VIEW])

add('performance-evaluation', 'Evaluate model performance', 'モデル性能評価', 'model-evaluation',
    'Inspect model rebuild, loading and display costs to locate performance bottlenecks in parts or assemblies.',
    '部品やアセンブリの再構築、読込み、表示の負荷を調べ、性能上のボトルネックを特定します。',
    p('M4 21 A12 12 0 1 1 28 21 M6 10 9 12 M16 5 V8 M26 10 23 12')
    + accent('M16 17 23 10') + c(16, 17, 2, fill=TEAL)
    + r(6, 24, 4, 5, 0, fill=PALE) + r(14, 21, 4, 8, 0, fill=PALE)
    + r(22, 26, 4, 3, 0, fill=PALE),
    ['performance', 'rebuild', 'bottleneck', '性能', '再構築', '負荷'],
    ['Performance Evaluation (Assemblies)', 'Performance Evaluation (Parts)'], [ASSEMBLY, EVALUATE])

add('predefined-view', 'Predefine drawing view', '定義済みビュー', 'drawing-view',
    'Place a view placeholder with predefined orientation and scale for later model insertion.',
    '後からモデルを挿入できるよう、方向や尺度を定めたビューの枠を配置します。',
    p('M3 10 V3 H10 M22 3 H29 V10 M29 22 V29 H22 M10 29 H3 V22', stroke_dasharray='3 2')
    + accent('M11 22 V10 M8 13 11 10 14 13 M11 22 H24 M21 19 24 22 21 25')
    + p('M11 22 20 13', stroke_dasharray='2 3'),
    ['drawing', 'placeholder', 'orientation', '図面', 'プレースホルダー', '方向'],
    ['Predefined View'], [DRAWING])

add('previous-release-check', 'Check previous-release compatibility', '旧バージョン互換性チェック', 'model-inspection',
    'Identify model and document items incompatible with a selected earlier software release before saving.',
    '保存前に、指定した旧バージョンに対応しないモデルや文書の項目を確認します。',
    p('M12 3 H23 L29 9 V29 H12 M23 3 V9 H29')
    + accent('M24 15 H5 M9 11 5 15 9 19')
    + p('M16 23 19 26 24 20')
    + p('M5 7 V4 H9', stroke_dasharray='2 2'),
    ['compatibility', 'previous release', 'check', '互換性', '旧バージョン', '確認'],
    ['Previous Release Check'], [EVALUATE])

add('print3d', 'Prepare 3D print', '3Dプリント準備', 'additive-output',
    'Prepare model geometry and print settings for a physical additive-manufacturing output.',
    '物理的な積層造形出力に向けて、モデル形状と印刷設定を準備します。',
    p('M4 26 V4 H28 V26 M4 8 H28 M12 8 V13 L16 17 20 13 V8')
    + r(3, 26, 26, 4, 1, fill=PALE)
    + fill('M10 22 16 19 22 22 V26 H10Z')
    + accent('M10 23 H22 M16 17 V19'),
    ['3D printing', 'additive', 'output', '3Dプリント', '積層造形', '出力'],
    ['Print3D'], [STANDARD])

add('relative-view', 'Relative drawing view', '相対ビュー', 'drawing-view',
    'Create a drawing orientation relative to selected model faces or planes.',
    '選択したモデルの面や平面を基準に、向きを定めた図面ビューを作成します。',
    fill('M3 13 12 8 21 13 V24 L12 29 3 24Z')
    + p('M3 13 12 18 21 13 M12 18 V29')
    + p('M3 13 12 18 V29 L3 24Z', fill=PALE, stroke=TEAL)
    + accent('M24 23 V5 H14 M17 2 14 5 17 8 M21 20 24 23 27 20')
    + p('M24 5 H29 V11'),
    ['drawing', 'orientation', 'reference face', '図面', '向き', '基準面'],
    ['Relative View'], [DRAWING])

add('removed-section', 'Removed section view', '取り出し断面図', 'drawing-view',
    'Place only the cross-section at a selected cutting location away from the parent drawing view.',
    '選択した切断位置の断面だけを、元の図面ビューから離れた場所に配置します。',
    fill('M3 5 H29 V13 H3Z')
    + accent('M16 2 V16', stroke_dasharray='3 2')
    + p('M16 16 V20', stroke_dasharray='2 2')
    + r(10, 22, 12, 8, 0, fill=PALE)
    + p('M10 27 15 22 M13 30 21 22 M19 30 22 27', stroke=TEAL),
    ['drawing', 'section', 'relocated slice', '図面', '断面', '取り出し'],
    ['Removed Section'], [DRAWING])

add('replace-model', 'Replace drawing reference model', '図面参照モデルの置換', 'drawing-document',
    'Replace the part or assembly referenced by selected drawing views.',
    '選択した図面ビューが参照する部品またはアセンブリを別モデルへ置き換えます。',
    r(3, 3, 26, 26, 1)
    + p('M6 9 H13 V16 H6Z', stroke_dasharray='2 2')
    + fill('M19 18 H26 V25 H16 V21 H19Z')
    + accent('M8 21 H13 M10 18 13 21 10 24 M24 11 H17 M20 8 17 11 20 14'),
    ['drawing', 'reference', 'replace model', '図面', '参照', 'モデル置換'],
    ['Replace Model'], [DRAWING])

add('resolve-drawing', 'Resolve drawing model data', '図面モデルデータの読込み', 'drawing-document',
    'Load referenced model data for a drawing opened without full model resolution.',
    'モデルを完全に読み込まずに開いた図面へ、参照モデルのデータを読み込みます。',
    p('M3 3 H16 V29 H3Z') + r(6, 18, 7, 7, 0, stroke_dasharray='2 2')
    + fill('M20 5 25 2 30 5 V13 L25 16 20 13Z')
    + p('M20 5 25 8 30 5 M25 8 V16')
    + accent('M25 20 V24 H18 M21 21 18 24 21 27'),
    ['drawing', 'resolve', 'load model', '図面', '解決', 'モデル読込み'],
    ['Resolve Drawing'], [ANNOTATION])

add('revision-cloud', 'Revision cloud', '改訂雲マーク', 'drawing-annotation',
    'Enclose a changed drawing region with a revision cloud.',
    '図面の変更領域を改訂雲マークで囲みます。',
    p('M7 8 C5 2 13 1 16 5 C20 1 27 3 26 9 C32 11 31 18 27 20 C30 26 24 31 19 27 C15 32 8 29 8 25 C2 27 0 20 5 17 C0 12 2 7 7 8Z', stroke=TEAL)
    + p('M10 13 H22 V21 H10Z', fill=PALE),
    ['revision', 'cloud', 'change', '改訂', '雲マーク', '変更'],
    ['Revision Cloud'], [ANNOTATION])

add('revision-symbol', 'Revision symbol', '改訂記号', 'drawing-annotation',
    'Mark a drawing change with a revision identifier symbol linked to revision documentation.',
    '図面の変更箇所に、改訂情報に対応する識別記号を配置します。',
    p('M16 3 29 26 H3Z', fill=PALE)
    + accent('M12 13 H19 V17 H13 V21 H20')
    + p('M8 29 H24'),
    ['revision', 'identifier', 'annotation', '改訂', '識別', '図面注記'],
    ['Revision Symbol'], [ANNOTATION])

add('section-properties', 'Calculate section properties', '断面特性', 'model-evaluation',
    'Calculate area, centroid and area moments for a selected planar section.',
    '選択した平面断面の面積、図心、断面二次モーメントなどを計算します。',
    fill('M6 5 H25 V10 H18 V23 H25 V28 H6 V23 H13 V10 H6Z')
    + accent('M16 2 V30 M3 17 H29', stroke_dasharray='3 3')
    + c(16, 17, 2, fill=TEAL),
    ['section', 'centroid', 'area moment', '断面', '図心', '断面二次モーメント'],
    ['Section Properties'], [EVALUATE])

add('sensor', 'Monitor model properties', 'モデルプロパティ監視', 'model-evaluation',
    'Monitor selected model properties or conditions and flag values that meet specified alert criteria.',
    '選択したモデルのプロパティや状態を監視し、設定した条件に該当する値を通知します。',
    fill('M3 9 10 5 17 9 V19 L10 23 3 19Z') + p('M3 9 10 13 17 9 M10 13 V23')
    + r(14, 16, 16, 13, 1, fill='white')
    + accent('M16 24 H19 L21 19 24 26 26 22 H28')
    + p('M19 11 Q24 11 24 15'),
    ['monitor', 'property', 'threshold', '監視', 'プロパティ', 'しきい値'],
    ['Sensor'], [EVALUATE])

add('stacked-balloons', 'Stacked balloons', '積み上げバルーン', 'drawing-annotation',
    'Group multiple component balloons into a stack sharing a common drawing leader.',
    '複数の部品バルーンを積み重ね、共通の引出線にまとめます。',
    c(24, 6, 4, fill=PALE) + c(24, 14, 4, fill=PALE) + c(24, 22, 4, fill=PALE)
    + accent('M20 14 H15 L6 26 M6 26 7 21 M6 26 11 25')
    + p('M3 29 H15 M23 6 H25 M23 14 H25 M23 22 H25'),
    ['balloon', 'stack', 'common leader', 'バルーン', '積み上げ', '共通引出線'],
    ['Stacked Balloons'], [ANNOTATION])

add('standard-3-view', 'Standard three-view drawing', '標準三面図', 'drawing-view',
    'Insert a coordinated set of three standard orthographic drawing views.',
    '標準的な三つの正投影ビューを、互いの対応を保って配置します。',
    r(4, 3, 11, 8, 0, fill=PALE)
    + fill('M4 18 H10 V15 H15 V28 H4Z')
    + r(22, 15, 7, 13, 0, fill=PALE)
    + p('M4 11 V15 M15 11 V13 M17 15 H20 M17 28 H20', stroke_dasharray='2 2')
    + accent('M7 7 H12 M25 18 V25'),
    ['drawing', 'orthographic', 'three views', '図面', '正投影', '三面図'],
    ['Standard 3 View'], [DRAWING])

add('sustainability', 'Evaluate environmental impact', '環境影響評価', 'model-evaluation',
    'Estimate environmental impacts of material and manufacturing choices across a product life cycle.',
    '材料や製造工程の選択による、製品ライフサイクル全体の環境影響を見積もります。',
    p('M5 15 A11 11 0 0 1 24 7 M20 7 H24 V3 M27 17 A11 11 0 0 1 8 25 M12 25 H8 V29')
    + p('M10 22 C7 12 15 9 23 9 C24 18 18 24 10 22Z', fill=PALE, stroke=TEAL)
    + accent('M10 22 20 12 M15 17 H20'),
    ['sustainability', 'life cycle', 'environment', '環境影響', 'ライフサイクル', '持続可能性'],
    ['Sustainability'], [EVALUATE])

add('symmetry-check', 'Check model symmetry', 'モデル対称性チェック', 'model-inspection',
    'Compare geometry on opposite sides of a reference plane to identify symmetric and asymmetric regions.',
    '基準面の両側の形状を比較し、対称領域と非対称領域を確認します。',
    fill('M4 8 H12 V27 H4 V21 H8 V14 H4Z')
    + fill('M20 8 H28 V14 H24 V21 H28 V27 H20Z')
    + accent('M16 2 V30', stroke_dasharray='3 3')
    + p('M8 4 H24 M11 2 8 4 11 6 M21 2 24 4 21 6'),
    ['symmetry', 'compare', 'reference plane', '対称性', '比較', '基準面'],
    ['Symmetry Check'], [EVALUATE])

add('title-block-table', 'Title-block table', '表題欄テーブル', 'drawing-table',
    'Insert or edit the drawing title-block table containing document identification and administrative fields.',
    '図面の識別情報や管理項目を記載する表題欄テーブルを挿入または編集します。',
    r(3, 3, 26, 26, 1)
    + p('M6 6 H26 M6 6 V26')
    + r(13, 18, 16, 11, 0, fill=PALE)
    + p('M13 23 H29 M21 18 V29')
    + accent('M15 26 H19 M23 20 H27'),
    ['drawing', 'title block', 'document fields', '図面', '表題欄', '管理項目'],
    ['Title Block Table'], [TABLE])

add('undercut-analysis', 'Analyze mold undercuts', 'アンダーカット解析', 'mold-inspection',
    'Highlight geometry trapped relative to a mold pull direction that may prevent straightforward ejection.',
    '金型の抜き方向に対して引っ掛かり、単純な離型を妨げる形状を可視化します。',
    fill('M4 8 H22 V13 H13 V20 H22 V27 H4Z')
    + p('M13 13 H22 V20 H13Z', fill=PALE, stroke='none')
    + p('M13 13 H22', stroke=AMBER, stroke_width=2.5)
    + accent('M27 27 V4 M24 7 27 4 30 7')
    + p('M17 18 V14 M15 16 17 14 19 16', stroke=AMBER),
    ['mold', 'undercut', 'ejection', '金型', 'アンダーカット', '離型'],
    ['Undercut Analysis'], [VIEW])

add('weld-symbol', 'Weld symbol annotation', '溶接記号注記', 'drawing-annotation',
    'Place a schematic weld specification annotation with a reference line and leader, not a modeled weld bead.',
    '基準線と引出線を持つ溶接仕様の模式注記を配置します。溶接ビード形状は作成しません。',
    p('M4 26 12 15 H27 M4 26 5 21 M4 26 9 25 M27 15 30 12 M27 15 30 18')
    + p('M16 15 V7 L23 15Z', fill=PALE, stroke=TEAL)
    + p('M3 29 H14'),
    ['weld', 'specification', 'annotation', '溶接', '仕様', '図面注記'],
    ['Weld Symbol'], [ANNOTATION])

add('weldment-cut-list', 'Weldment cut-list table', '溶接構造のカットリスト', 'drawing-table',
    'List cut lengths, quantities and properties of structural members or weldment bodies.',
    '構造部材や溶接構造ボディの切断長さ、数量、プロパティを一覧表にします。',
    fill('M3 9 7 5 14 12 10 16Z') + fill('M3 18 7 14 14 21 10 25Z')
    + r(17, 4, 13, 25, 1)
    + p('M17 11 H30 M17 18 H30 M17 24 H30 M22 4 V29')
    + accent('M25 15 H28 M25 21 H28'),
    ['weldment', 'cut list', 'member length', '溶接構造', 'カットリスト', '部材長さ'],
    ['Weldment Cut List'], [TABLE])
