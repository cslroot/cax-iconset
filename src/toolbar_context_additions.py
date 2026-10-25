"""Original contextual toolbar glyphs for cable, BIM and document commands.

These are operation-specific silhouettes, not generic icons with text badges.
User-requested semantic scope; consumer binding evidence is recorded separately.
"""
from core import p, r, c, accent, PALE, TEAL

ITEMS = []

def add(domain, id, en, ja, desc, descja, body, family, aliases, tags, role='command'):
    ITEMS.append(dict(domain=domain, id=id, name=en, nameJa=ja,
        description=desc, descriptionJa=descja, body=body, family=family,
        role=role, aliases=aliases + [ja], tags=[family, ja] + tags,
        sources=['cax-toolbar-requirements-2026-10-25']))

add('CAD', 'cable', 'Cable', 'ケーブル',
    'Create or inspect a flexible cable route with end connections; not a rigid pipe or a generic spline.',
    '両端の接続を持つ柔軟なケーブル経路を作成・確認します。剛体配管や汎用スプラインとは区別します。',
    # Two continuous outlines form a flexible U-bend; asymmetric terminal plugs.
    p('M7 8 V19 C7 28 23 28 23 19 V13', stroke=TEAL, stroke_width=4)
    +r(3,3,8,7,1,fill=PALE)+p('M5 3 V1.5 M9 3 V1.5')
    +r(19,6,8,8,1,fill=PALE)+p('M21 6 V3 M25 6 V3'),
    'flexible-cable', ['cable route', 'cax-cable-sim cable'],
    ['cable', 'flexible', 'route', 'connector'])

add('OLP', 'dresspack', 'Robot dress pack', 'ロボットドレスパック',
    'Create or inspect a bundled service cable or hose routed along an articulated robot arm, including its slack loop.',
    '関節ロボットに沿うケーブル・ホース束と余長ループを作成・確認します。単体のケーブルとは区別します。',
    # Robot links behind a clearly external, curved service bundle.
    p('M4 29 H16 M9 29 V23 L7 13 21 7 26 14',stroke_width=3)
    +c(9,23,2.5,fill=PALE)+c(7,13,2.5,fill=PALE)+c(21,7,2.5,fill=PALE)
    +accent('M3 24 C1 15 2 6 10 5 L18 2 C27 1 31 7 29 14 L27 20',stroke_width=2.5)
    +p('M24 18 29 20 M24 20 28 22',stroke=TEAL),
    'robot-service-bundle', ['dress pack', 'dresspack', 'robot cable bundle'],
    ['robot', 'cable', 'hose', 'bundle', 'slack'])

add('CAD', 'minimum-clearance', 'Minimum clearance', '最小クリアランス',
    'Measure the shortest separation between the surfaces of two objects; not a prescribed mate distance or an arbitrary point-to-point measurement.',
    '2つの対象の表面間で最短の隔たりを測定します。指定距離の合致や任意の2点間測定とは区別します。',
    # Nonparallel bulged boundaries make the local nearest gap unambiguous.
    p('M3 4 H7 Q15 16 7 28 H3Z',fill=PALE)
    +p('M29 4 H25 Q17 16 25 28 H29Z',fill=PALE)
    +accent('M11 16 H21 M14 13 11 16 14 19 M18 13 21 16 18 19')
    +c(11,16,1.1,fill=TEAL,stroke=TEAL)+c(21,16,1.1,fill=TEAL,stroke=TEAL),
    'minimum-surface-separation', ['minimum distance', 'clearance'],
    ['clearance', 'closest points', 'minimum distance'])

add('Common', 'open-sample', 'Open sample', 'サンプルを開く',
    'Open a bundled example or demonstration document, distinct from browsing for an arbitrary user file.',
    '同梱の例題やデモ文書を開きます。任意のユーザーファイルを探す操作とは区別します。',
    # A miniature example model emerges from an open sample folder.
    p('M3 26 V11 H10 L13 14 H28 L25 28 H3Z',fill=PALE)
    +p('M3 26 7 18 H29 L25 28 H3Z',fill=PALE)
    +p('M13 6 20 2 27 6 V13 L20 17 13 13Z',fill=PALE,stroke=TEAL)
    +accent('M13 6 20 10 27 6 M20 10 V17'),
    'open-example-document', ['open example', 'open sample model'],
    ['sample', 'example', 'demo', 'document'])

add('CAD', 'bim-building', 'BIM building', 'BIM建物',
    'Identify or create a whole building in an IFC/BIM spatial hierarchy, distinct from one storey or one enclosed space.',
    'IFC/BIMの空間階層における建物全体を識別・作成します。1つの階や室とは区別します。',
    p('M6 29 V7 L16 2 26 7 V29Z',fill=PALE)
    +p('M6 7 H26 M3 29 H29 M13 29 V22 H19 V29')
    +accent('M10 11 H13 M19 11 H22 M10 17 H13 M19 17 H22'),
    'bim-building', ['IfcBuilding', 'building'],
    ['BIM', 'IFC', 'spatial hierarchy', 'building'], role='object')

add('CAD', 'bim-storey', 'BIM storey', 'BIM階',
    'Identify or create one building storey or level in an IFC/BIM spatial hierarchy, not the whole building.',
    'IFC/BIMの空間階層における1つの階・レベルを識別・作成します。建物全体とは区別します。',
    # Exploded horizontal slabs, with only the middle level emphasized.
    p('M3 8 16 2 29 8 16 14Z')
    +p('M3 23 16 17 29 23 16 29Z')
    +p('M3 14 16 8 29 14 V18 L16 24 3 18Z',fill=PALE,stroke=TEAL)
    +accent('M3 14 16 20 29 14 M16 20 V24'),
    'bim-storey', ['IfcBuildingStorey', 'floor level', 'storey'],
    ['BIM', 'IFC', 'floor', 'level', 'spatial hierarchy'], role='object')

add('CAD', 'bim-space', 'BIM space', 'BIMスペース',
    'Identify or create a bounded room or spatial volume in an IFC/BIM hierarchy, distinct from a building element or a complete storey.',
    'IFC/BIM階層の室・空間領域を識別・作成します。建築部材や階全体とは区別します。',
    # Architectural plan enclosure, doorway gap and inward quarter-circle swing.
    p('M4 4 H28 V28 H20 M12 28 H4Z',stroke_width=2.5)
    +r(9,9,14,14,1,fill=PALE,stroke=TEAL,stroke_dasharray='3 2')
    +p('M12 28 V20 A8 8 0 0 1 20 28'),
    'bim-space', ['IfcSpace', 'room', 'spatial volume'],
    ['BIM', 'IFC', 'room', 'space', 'spatial hierarchy'], role='object')

add('Common', 'export-report', 'Export report', 'レポートを書き出す',
    'Export a general structured report document; does not imply physics analysis, inspection results or a particular output format.',
    '汎用の構造化レポート文書を書き出します。物理解析・検査結果や特定の出力形式を前提としません。',
    p('M5 3 H20 L25 8 V29 H5Z',fill=PALE,stroke='none')
    +p('M5 3 H20 L25 8 V14 M5 3 V29 H25 V25 M20 3 V8 H25')
    +p('M9 9 H16 M9 14 H17 M9 19 H14 M9 24 H14')
    +accent('M18 20 H30 M26 16 30 20 26 24'),
    'export-general-report', ['report export', 'export report document'],
    ['report', 'document', 'export'])

# Register these alongside usage.TREE during integration; object-only records
# intentionally denote spatial hierarchy nodes, not ambiguous creation commands.
TREE = {
    'cad-bim-building': {'objectType': 'bim-building'},
    'cad-bim-storey': {'objectType': 'bim-storey'},
    'cad-bim-space': {'objectType': 'bim-space'},
}
