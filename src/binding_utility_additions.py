"""Original utility glyphs for source-verified gaps in conditional bindings.

These records supply neutral operation geometry, not vendor artwork. Explicit
command labels and binding conditions retain the destination, mode and scope.
The 693 existing semantic records and their two theme variants are unchanged.
Sources are official URLs pending registration by the integration build.
"""
from core import p, r, c, accent, PALE, TEAL

ITEMS = []


def add(domain, id, en, ja, desc, desc_ja, body, family, aliases, sources, tags):
    ITEMS.append(dict(domain=domain, id=id, name=en, nameJa=ja,
        description=desc, descriptionJa=desc_ja, family=family,
        role='command', tags=[family, en.lower(), ja, domain.lower()] + tags,
        aliases=aliases, sources=sources, body=body))


SW_TOOLS = 'https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_tools_toolbar.htm?id=2.12.4.1.39'
SW_COMMANDS = 'https://help.solidworks.com/2025/english/api/swcommands/SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swCommands_e.html?id=cec41382bfc941eb83f24f6c8425852b'

add('CAE', 'simulation-overlay', 'Display simulation in model context', 'モデル上に解析結果を表示',
    'Overlay a stored simulation result on its CAD model or assembly context, without selecting a particular result type or starting a solver.',
    '保存済みの解析結果をCADモデルやアセンブリの文脈に重ねて表示します。特定の結果種類の指定やソルバーの実行は意味しません。',
    # The unshaded rear/right component preserves CAD context. A neutral tiled
    # field occupies the front component, rather than stress arrows or a graph.
    p('M14 4 28 10 V22 L20 27 6 21 V9Z')
    +p('M14 4 V15 L28 22 M14 15 6 21 M14 15 28 10')
    +p('M3 14 11 10 21 15 V25 L13 29 3 24Z', fill=PALE)
    +p('M3 14 13 19 21 15 M13 19 V29')
    +p('M3 19 8 21.5 V16.5 M8 21.5 13 24 M13 24 21 20', stroke=TEAL)
    +p('M3 19 8 21.5 V26.5 L3 24Z', fill=TEAL, stroke='none'),
    'result-display', ['Simulation Display'],
    ['https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_view_toolbar.htm?id=d7123216e4cc48df9f6b6be904699b39',
     'https://help.solidworks.com/2026/english/simtutorialonline/t_viewing_optimization_results.htm?id=0.2.6.8',
     'https://help.solidworks.com/2022/english/SolidWorks/sldworks/t_displaying_sw_sim_results_inga.htm'],
    ['simulation', 'result overlay', 'assembly', '解析結果', '重ね合わせ'])

add('CAD', 'design-study', 'Evaluate design scenarios', '設計シナリオを評価',
    'Evaluate or optimize candidate designs from variables, constraints and goals; the visible mode distinguishes evaluation from optimization and does not imply a physics solve.',
    '変数・制約・目標に基づいて設計候補を評価または最適化します。評価と最適化はモードで区別し、物理解析の実行を前提としません。',
    # Three parameter candidates and their evaluated responses. One candidate
    # is selected, but there is no success check or promised global optimum.
    r(3, 3, 7, 14, 1, fill=PALE)
    +r(13, 3, 7, 14, 1, fill=PALE, stroke=TEAL)
    +r(23, 3, 6, 14, 1, fill=PALE)
    +p('M5 7 H8 M5 13 H8 M15 10 H18 M15 14 H18 M25 6 H27 M25 11 H27')
    +p('M4 21 V29 H29')
    +accent('M7 23 16.5 26 26 21')
    +c(7, 23, 1.4, fill=PALE)
    +c(16.5, 26, 2.2, fill=PALE, stroke=TEAL)
    +c(26, 21, 1.4, fill=PALE),
    'design-evaluation', ['Design Study', 'Design Studies'],
    [SW_TOOLS,
     'https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_Design_Studies_SOLIDWORKS.htm?id=e0490acf4f374e5a800fca910b819154',
     'https://help.solidworks.com/2026/english/SolidWorks/cworks/c_Design_Study.htm?id=26.13'],
    ['scenario', 'optimization', 'variable', '設計検討', '最適化'])

add('Common', 'measure-geometry', 'Measure geometry', '形状を測定',
    'Inspect geometric measurements such as distance, angle, radius, coordinates or area without creating a persistent model or drawing dimension.',
    '距離・角度・半径・座標・面積などの形状情報を測定します。モデルや図面に永続的な寸法は作成しません。',
    # A protractor and ruled base communicate a multipurpose inspection tool,
    # not a dimension annotation attached to two model points.
    p('M4 22 A12 12 0 0 1 28 22', fill=PALE)
    +r(3, 22, 26, 7, 1)
    +p('M8 22 V26 M13 22 V25 M18 22 V26 M23 22 V25')
    +p('M6 15 8 16 M16 10 V12 M25.5 15 23.5 16')
    +accent('M16 22 23 7')
    +c(16, 22, 1.7, fill=PALE, stroke=TEAL),
    'geometry-measurement', ['Measure', 'inspect.measure'],
    [SW_TOOLS,
     'https://help.solidworks.com/2026/english/SolidWorks/sldworks/HIDD_MEASURE.htm?id=3.10',
     'https://docs.solidcraft.io/reference/commands.html'],
    ['inspection', 'angle', 'radius', 'area', '測定', '角度', '面積'])

add('Common', 'launch-external-service', 'Open external application or service', '外部アプリ・サービスを開く',
    'Open the explicitly named external application or service; launching alone does not mean transferring a model, solving, requesting a quote or placing an order.',
    '明示された外部アプリやサービスを開きます。起動だけでモデル転送・解析・見積依頼・注文が実行されることは意味しません。',
    # A window and outward navigation arrow, not an export document or a play
    # control. The destination must remain visible in a command binding.
    p('M16 6 H5 Q3 6 3 8 V27 Q3 29 5 29 H24 Q26 29 26 27 V17', fill=PALE)
    +p('M3 12 H13')
    +accent('M12 21 29 4 M20 4 H29 V13'),
    'external-launch', ['3DEXPERIENCE Simulation Connector', 'On Demand Manufacturing', '3DEXPERIENCE Make'],
    [SW_TOOLS, SW_COMMANDS,
     'https://help.solidworks.com/2024/english/SolidWorks/sldworks/t_using_make_sw_desktop.htm'],
    ['application', 'service', 'launch', '外部サービス', '起動'])

add('CAD', 'manufacturability-check', 'Check manufacturability', '製造性を検証',
    'Check a part against configured design-for-manufacture rules without implying geometric validity checks, automatic repair or fabrication execution.',
    '設定された製造設計ルールに照らして部品の製造性を検証します。形状妥当性の検査・自動修復・実加工は意味しません。',
    # A manufactured bracket with holes makes this a fabrication-rule check,
    # unlike the existing generic cube, document or analysis-mesh check marks.
    p('M4 4 H12 V20 H28 V28 H4Z', fill=PALE)
    +c(8, 11, 1.7)
    +c(21, 24, 1.7)
    +p('M4 20 H12 M12 20 V28', stroke_dasharray='2 2')
    +accent('M17 10 21 14 29 5'),
    'manufacturing-validation', ['DFMXpress Analysis Wizard', 'DFM', 'Design for Manufacture'],
    [SW_TOOLS,
     'https://help.solidworks.com/2026/English/SolidWorks/DFMXpress/c_DFMXpress_overview.htm'],
    ['manufacturability', 'process rules', 'fabrication', '製造性', '製造ルール'])

add('CAD', 'author-asset-references', 'Define asset placement references', 'アセット配置参照を定義',
    'Prepare a local layout asset by defining its ground attachment and outward connection points or directions, not by mating existing assets or uploading them.',
    '接地参照と外向きの接続点・方向を定義してローカルなレイアウト用アセットを準備します。既存アセットの結合やアップロードは行いません。',
    # Ground plane plus outward reference connectors. No second mating part
    # and no remote-service/cloud cue is present.
    p('M3 24 15 18 29 24 17 30Z', fill=PALE)
    +p('M9 8 16 4 23 8 V21 L16 25 9 21Z', fill=PALE)
    +p('M9 8 16 12 23 8 M16 12 V25')
    +accent('M9 16 H2 M5 13 2 16 5 19 M23 16 H30 M27 13 30 16 27 19')
    +c(9, 16, 1.5, fill=PALE, stroke=TEAL)
    +c(23, 16, 1.5, fill=PALE, stroke=TEAL)
    +accent('M3 24 17 30 29 24'),
    'asset-reference-authoring', ['Asset Publisher'],
    [SW_TOOLS,
     'https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_assy_facility_layout.htm?id=7.13.1',
     'https://help.solidworks.com/2025/English/SolidWorks/sldworks/r_asset_publisher_propertymanager.htm'],
    ['ground plane', 'connection point', 'asset', 'アセット', '接地', '接続参照'])

add('CAD', 'publish-model-cloud', 'Publish model to remote service', 'モデルを外部サービスに公開',
    'Transfer a model for publication to an explicitly named remote service; the workflow defines the audience and does not imply local export or continuous synchronization.',
    '明示された外部サービスへモデルを転送して公開します。公開範囲は手順で指定し、ローカル書き出しや常時同期は意味しません。',
    # An actual model, cloud and one-way upload. No vendor logo, audience or
    # public-visibility assertion is encoded in this reusable geometry.
    p('M13 14 H25 C30 14 30 6 25 6 C24 1 16 1 14 6 C8 5 8 14 13 14Z')
    +p('M3 19 10 15 17 19 V26 L10 30 3 26Z', fill=PALE)
    +p('M3 19 10 23 17 19 M10 23 V30')
    +accent('M24 28 V18 M20 22 24 18 28 22'),
    'remote-model-publication', ['Publish to 3DCloudByMe', 'Publish to HomeByMe'],
    [SW_TOOLS,
     'https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_publish_3dcloudbymePM.htm?id=5.17.0',
     'https://help.solidworks.com/2026/english/SolidWorks/sldworks/c_share_files.htm?id=5.15',
     SW_COMMANDS],
    ['cloud', 'publish', 'upload', 'クラウド', 'モデル公開'])

add('CAD', 'annotation-note', 'Place annotation note', '注記を配置',
    'Place plain or property-linked annotation text without requiring a geometry leader or creating sketch profiles.',
    '引出線を必須とせず、通常の文字やプロパティにリンクした注記を配置します。スケッチ輪郭は作成しません。',
    # An open text frame and multiline typographic strokes. There is no
    # attachment arrow, baseline dimension or solid-profile construction cue.
    p('M8 3 H3 V8 M24 3 H29 V8 M3 24 V29 H8 M29 24 V29 H24')
    +accent('M7 17 10.5 7 14 17 M8.5 13 H12.5')
    +p('M19 9 H25 M19 15 H25 M7 22 H25 M7 26 H20'),
    'text-annotation', ['Note', 'No Leader note'],
    ['https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_Annotations_Toolbar.htm?id=2.12.4.1.2',
     'https://help.solidworks.com/2025/english/SolidWorks/sldworks/c_notes.htm?id=d1b8b71f6dfd4415a1d5301ae125061f',
     'https://help.solidworks.com/2026/english/SolidWorks/sldworks/r_annotation_leaders.htm?id=13.7.11.0'],
    ['annotation', 'text', 'leaderless', '注記', '引出線なし'])
