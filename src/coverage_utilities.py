"""Original utility and view glyphs for the frozen GUI coverage audit.

One entry represents an independent operation, not every UI option.  Vendor
documentation supplies command meaning only; all geometry is authored here.
The shared SVG wrapper supplies rounded 1.75 px strokes on a 32 px viewBox.
"""
from core import p, r, c, g, accent, fill, PALE, TEAL, INK, AMBER

ITEMS = []


def add(id, domain, name, name_ja, family, description, description_ja, body, tags):
    ITEMS.append(dict(id=id, domain=domain, name=name, nameJa=name_ja,
                      description=description, descriptionJa=description_ja,
                      family=family, role='command', body=body,
                      tags=list(dict.fromkeys(tags + [family, name.lower(), name_ja]))))


def small_cube(x, y, width=12, height=12):
    half = width / 2
    return (fill(f'M{x} {y+3} {x+half} {y} {x+width} {y+3} V{y+height} '
                 f'L{x+half} {y+height+3} {x} {y+height}Z')
            + p(f'M{x} {y+3} {x+half} {y+6} {x+width} {y+3} '
                f'M{x+half} {y+6} V{y+height+3}'))


def book():
    return (fill('M5 5 H23 Q27 5 27 9 V27 H8 Q5 27 5 24Z')
            + p('M9 5 V23 H27 M5 24 Q5 21 9 23'))


def pointer(x=19, y=17):
    return p(f'M{x} {y} V{y+11} L{x+3} {y+8} {x+6} {y+12} '
             f'{x+8} {y+10} {x+5} {y+6} H{x+10}Z', fill='white')


def eye(x=16, y=18, width=12):
    return (p(f'M{x-width/2} {y} Q{x} {y-7} {x+width/2} {y} '
              f'Q{x} {y+7} {x-width/2} {y}Z', fill='white')
            + c(x, y, 2, fill=TEAL, stroke=TEAL))


# Configuration and reversible model checkpoints.
add('activate-display-state', 'CAD', 'Activate display state', '表示状態の切替', 'display-state',
    'Activate a saved combination of visibility, appearance and display settings.',
    '表示・外観・表示方式をまとめた保存済みの表示状態を有効にします。',
    r(3,4,17,15,1) + c(11.5,11.5,4) + r(12,13,17,15,1,fill='white')
    + c(20.5,20.5,4,fill=PALE,stroke=TEAL)
    + accent('M5 24 V28 H9 M23 4 H28 V8 M25 6 28 9 30 6'),
    ['display state', 'activate', 'visibility', 'appearance', '表示状態', '切替', '外観'])

add('add-configuration', 'CAD', 'Add configuration', 'コンフィギュレーション追加', 'configuration',
    'Create a named model configuration with its own feature and parameter choices.',
    'フィーチャやパラメータの組合せを持つ名前付きモデル構成を追加します。',
    p('M4 20 V4 H21') + r(8,8,17,20,1,fill=PALE)
    + p('M12 13 H18 M12 18 H16 M12 23 H19')
    + r(20,18,10,12,2,fill='white',stroke='none')
    + accent('M25 19 V29 M20 24 H30'),
    ['configuration', 'variant', 'add', '構成', '追加', '派生'])

add('add-rebuild-on-save-mark', 'CAD', 'Mark rebuild on save', '保存時再構築マーク', 'configuration',
    'Mark a configuration to be rebuilt and saved when its document is saved.',
    '文書保存時に再構築して保存するコンフィギュレーションを指定します。',
    fill('M5 4 H23 L28 9 V28 H5Z') + p('M10 4 V12 H22 V4 M10 28 V19 H17')
    + p('M23 16 A7 7 0 1 1 17 23 M17 19 V23 H21',stroke=TEAL)
    + p('M23 16 V12 M21 14 23 12 25 14',stroke=TEAL),
    ['configuration', 'save', 'rebuild', 'mark', '構成', '保存', '再構築', 'マーク'])

add('checkpoint-save', 'Common', 'Save checkpoint', 'チェックポイント保存', 'history-checkpoint',
    'Capture the current design and undo-history state as a restorable checkpoint.',
    '現在の設計と取り消し履歴の状態を復元可能なチェックポイントとして保存します。',
    p('M4 9 H28') + c(6,9,2,fill='white') + c(26,9,2,fill='white')
    + c(16,9,3,fill=PALE,stroke=TEAL) + accent('M16 13 V20 M13 17 16 20 19 17')
    + fill('M7 23 H25 V29 H7Z') + p('M11 23 V26 H21 V23'),
    ['checkpoint', 'capture', 'undo history', 'チェックポイント', '保存', '履歴'])

add('checkpoint-restore', 'Common', 'Restore checkpoint', 'チェックポイント復元', 'history-checkpoint',
    'Restore both the design and its undo history from a saved checkpoint.',
    '保存済みチェックポイントから設計と取り消し履歴を復元します。',
    p('M4 9 H28',stroke_dasharray='2 3') + c(7,9,3,fill=PALE,stroke=TEAL)
    + c(26,9,2,fill='white') + fill('M14 22 H28 V29 H14Z')
    + p('M18 22 V25 H24 V22')
    + accent('M20 19 V16 Q20 9 12 9 M15 6 12 9 15 12'),
    ['checkpoint', 'restore', 'undo history', 'チェックポイント', '復元', '履歴'])

add('configuration-preview', 'CAD', 'Preview configuration', 'コンフィギュレーションのプレビュー', 'configuration',
    'Preview a candidate model configuration without making it the active configuration.',
    '候補のモデル構成をアクティブにせずに再構築して確認します。',
    p('M6 10 16 4 26 10 V22 L16 28 6 22Z M6 10 16 16 26 10 M16 16 V28',
      stroke_dasharray='3 3') + eye(16,18,20),
    ['configuration', 'preview', 'trial', '構成', 'プレビュー', '試行'])

add('configuration-rules', 'CAD', 'Configuration rules', 'コンフィギュレーション規則', 'configuration',
    'Inspect or define conditional rules that choose configuration values or actions.',
    '条件に応じて構成の値や処理を選ぶ規則を確認・定義します。',
    fill('M16 3 23 10 16 17 9 10Z') + p('M9 10 H5 V25 H10 M23 10 H27 V25 H22')
    + r(10,21,12,8,1,fill=PALE) + accent('M13 10 15 12 19 8 M13 25 H19'),
    ['configuration', 'rule', 'condition', 'decision', '構成', '規則', '条件', '分岐'])

add('dependency-graph', 'CAD', 'Inspect dependencies', '依存関係の表示', 'model-dependencies',
    'Show reference links and downstream users of model features or parameters.',
    'フィーチャやパラメータの参照関係と、それらを使用する下流の項目を表示します。',
    r(11,3,10,7,1,fill=PALE) + p('M16 10 V15 H6 V21 M16 15 H26 V21')
    + r(2,21,9,8,1) + r(21,21,9,8,1)
    + accent('M12 25 H20 M17 22 20 25 17 28'),
    ['reference', 'dependency', 'graph', 'users', '参照', '依存関係', 'グラフ', '使用先'])

# Inspection utilities and curated resource libraries.
add('design-check', 'CAD', 'Check design document', '設計文書チェック', 'design-validation',
    'Check document properties and design requirements against a defined check set or reference document.',
    '定義済みの検査項目や参照文書に照らし、文書属性と設計要件を検査します。',
    fill('M5 3 H20 L26 9 V28 H5Z') + p('M20 3 V9 H26 M9 13 H17 M9 18 H15')
    + accent('M16 23 20 27 28 17'),
    ['design check', 'document', 'validation', 'requirements', '設計チェック', '文書', '検査', '要件'])

add('design-check-rules', 'CAD', 'Define design checks', '設計チェックの定義', 'design-validation',
    'Build or learn reusable requirements for design-document checking.',
    '設計文書の検査で再利用する要件を作成、または既存文書から学習します。',
    r(4,4,21,24,1) + p('M8 9 H17 M8 15 H14 M8 21 H12')
    + p('M17 25 20 18 26 12 30 16 24 22Z',fill=PALE)
    + accent('M20 18 24 22 M17 25 22 24'),
    ['design check', 'rules', 'requirements', 'learn', '設計チェック', '規則', '要件', '学習'])

add('design-library', 'CAD', 'Browse design library', '設計ライブラリ参照', 'design-library',
    'Inspect curated, versioned local resources for reuse in a design.',
    '設計で再利用する、整理・版管理されたローカルのリソースを確認します。',
    p('M3 8 H29 V28 H3Z M3 18 H29')
    + p('M5 4 H27 V8') + r(6,11,8,5,1,fill=PALE)
    + c(23,13.5,2.5,fill=PALE) + p('M6 22 H11 V26 H6Z M16 25 21 20 26 25Z',fill=PALE),
    ['library', 'local', 'resource', 'reuse', 'ライブラリ', 'ローカル', 'リソース', '再利用'])

add('material-library', 'CAD', 'Manage material library', '材料ライブラリ管理', 'material-library',
    'Browse or create physical material definitions without assigning them to geometry.',
    '形状への材料割当とは別に、物性を持つ材料定義を参照・作成します。',
    book() + p('M13 11 18 8 23 11 V17 L18 20 13 17Z M13 11 18 14 23 11 M18 14 V20',fill='white'),
    ['material', 'library', 'physical properties', 'definition', '材料', 'ライブラリ', '物性', '定義'])

add('material-validation', 'CAD', 'Validate material data', '材料データ検証', 'material-validation',
    'Check physical material properties for missing, inconsistent or invalid constitutive data.',
    '材料の物性値について欠落・不整合・無効な構成則データを検証します。',
    small_cube(3,4,15,14) + p('M4 26 H13 M8 23 V29')
    + accent('M18 24 22 28 30 17'),
    ['material', 'validate', 'constitutive data', 'consistency', '材料', '検証', '構成則', '整合性'])

add('directional-modulus', 'CAD', 'Directional elastic modulus', '方向別弾性率', 'material-evaluation',
    'Evaluate how elastic modulus varies with direction in an anisotropic material.',
    '異方性材料で方向に応じて変化する弾性率を評価します。',
    p('M3 16 H29 M16 3 V29',stroke_dasharray='2 3')
    + p('M16 16 C3 17 2 5 8 5 C14 5 15 12 16 16 C29 15 30 27 24 27 C18 27 17 20 16 16Z',fill=PALE)
    + accent('M16 16 25 7 M21 7 H25 V11') + c(16,16,1.5,fill=TEAL,stroke=TEAL),
    ['material', 'anisotropic', 'modulus', 'direction', '材料', '異方性', '弾性率', '方向'])

add('appearance-library', 'CAD', 'Manage appearances', '外観の参照・選択', 'appearance-library',
    'Inspect assigned body or face appearances, browse reusable looks, and choose a library appearance to apply.',
    'ボディや面に割り当てた外観と再利用できる見本を参照し、適用する外観を選択します。',
    book() + c(15,11,2.5,fill=TEAL,stroke=TEAL) + c(22,11,2.5,fill='white')
    + r(12.5,16,5,5,1,fill='white') + r(19.5,16,5,5,1,fill=INK),
    ['appearance', 'library', 'swatch', 'visual style', '外観', 'ライブラリ', '見本', 'スタイル'])

add('assign-appearance', 'CAD', 'Assign appearance', '外観の割当', 'appearance-editing',
    'Apply a visual color or surface style to selected faces, bodies or components.',
    '選択した面・ボディ・部品に表示用の色や表面スタイルを適用します。',
    fill('M4 20 13 15 22 20 V27 L13 31 4 27Z')
    + p('M4 20 13 24 22 20 M13 24 V31')
    + p('M14 14 24 4 Q26 2 28 4 Q30 6 28 8 L18 18Z',fill=PALE)
    + accent('M13 15 Q8 14 8 22 Q16 23 17 18Z',fill=TEAL),
    ['appearance', 'color', 'surface style', 'assign', '外観', '色', '表面スタイル', '割当'])

# Camera controls are distinct from projection, model transforms or orbit.
add('camera-view', 'CAD', 'Camera view', 'カメラビュー', 'camera-navigation',
    'Look through a model camera using its position, orientation and field of view.',
    'モデル内のカメラ位置・方向・画角に従って表示します。',
    p('M11 12 27 5 V27 L11 20Z',stroke_dasharray='3 3')
    + r(3,10,10,12,2,fill=PALE) + p('M13 14 19 11 V21 L13 18Z',fill=PALE)
    + accent('M24 9 H28 V23 H24'),
    ['camera', 'view', 'field of view', 'カメラ', 'ビュー', '画角'])

add('add-walk-through', 'CAD', 'Create walk-through', 'ウォークスルー作成', 'camera-navigation',
    'Define a camera route for walking through a model or assembly scene.',
    'モデルやアセンブリの内部を歩いて確認するカメラの経路を作成します。',
    p('M4 24 V5 H27 V24') + p('M12 5 V16 H22')
    + accent('M5 29 H12 Q18 29 18 23 V16 M15 19 18 16 21 19')
    + c(7,23,2,fill=PALE) + p('M7 25 5 29 M8 26 11 28'),
    ['camera', 'walkthrough', 'route', 'navigation', 'カメラ', 'ウォークスルー', '経路', '移動'])

add('isometric-view', 'CAD', 'Isometric view', '等角投影ビュー', 'view-orientation',
    'Orient the camera to an isometric view with equally foreshortened principal axes.',
    '主軸の縮み率が等しい等角投影方向にカメラを向けます。',
    fill('M7 11 16 6 25 11 V21 L16 26 7 21Z')
    + p('M7 11 16 16 25 11 M16 16 V26')
    + accent('M16 16 V2 M16 16 3 23 M16 16 29 23')
    + p('M14 4 16 2 18 4 M3 20 V23 H6 M26 23 H29 V20',stroke=TEAL),
    ['camera', 'isometric', 'axonometric', 'orientation', 'カメラ', '等角投影', '方向'])

add('standard-view', 'CAD', 'Standard view orientation', '標準ビュー方向', 'view-orientation',
    'Choose a standard front, back, side, top or bottom model-view direction.',
    '正面・背面・側面・上面・下面などの標準方向からモデルを表示します。',
    p('M7 12 14 5 H28 V20 L21 27 H7Z M7 12 H21 V27 M21 12 28 5 M21 20 H28')
    + r(7,12,14,15,0,fill=PALE,stroke=TEAL)
    + accent('M2 19 H10 M7 16 10 19 7 22'),
    ['view orientation', 'front', 'back', 'top', 'side', 'ビュー方向', '正面', '背面', '上面', '側面'])

add('view-normal-to', 'CAD', 'View normal to selection', '選択面に垂直なビュー', 'view-orientation',
    'Align the viewing direction with the normal of a selected planar entity.',
    '選択した平面要素の法線方向に視線を合わせます。',
    fill('M3 19 13 13 29 19 19 27Z') + p('M16 20 V14 H20')
    + accent('M16 20 V3 M12 7 16 3 20 7')
    + p('M8 22 16 17 24 21',stroke_dasharray='2 3'),
    ['view', 'normal', 'plane', 'selection', 'ビュー', '法線', '平面', '選択'])

add('previous-view', 'CAD', 'Previous view', '前のビュー', 'view-history',
    'Return to the preceding camera view without undoing model edits.',
    'モデルの編集を取り消さずに、直前のカメラ表示へ戻します。',
    r(4,9,24,20,2) + p('M8 24 14 18 19 23 24 16',stroke=TEAL)
    + p('M11 4 H23 Q28 4 28 9')
    + accent('M11 1 7 4 11 7'),
    ['view', 'previous', 'camera history', 'ビュー', '前へ', 'カメラ履歴'])

add('named-view-restore', 'CAD', 'Restore named view', '名前付きビューの復元', 'view-history',
    'Apply a previously saved camera or render-view snapshot.',
    '保存済みのカメラやレンダリング表示のスナップショットを適用します。',
    r(3,5,25,22,2) + p('M7 21 13 15 18 20 24 13',stroke=TEAL)
    + p('M9 5 V14 L13 11 17 14 V5',fill=PALE)
    + accent('M23 24 H30 M27 21 30 24 27 27'),
    ['named view', 'camera', 'saved view', 'restore', '名前付きビュー', 'カメラ', '保存ビュー', '復元'])

add('roll-view', 'CAD', 'Roll view', 'ビューのロール', 'camera-navigation',
    'Rotate the camera about its viewing axis without changing the viewing target.',
    '注視点を変えずに、視線軸の周りでカメラを回転します。',
    p('M8 2 Q20 0 27 9 M23 7 27 9 28 5',stroke=TEAL)
    + g(r(7,8,18,16,1,fill=PALE) + p('M7 18 H25 M16 8 V24'),transform='rotate(25 16 16)')
    + accent('M24 30 Q12 32 5 23 M9 25 5 23 4 27'),
    ['camera', 'roll', 'view axis', 'rotate', 'カメラ', 'ロール', '視線軸', '回転'])

add('turn-camera', 'CAD', 'Turn camera', 'カメラの向き変更', 'camera-navigation',
    'Turn the camera in place to change its look direction rather than orbiting the model.',
    'モデルの周囲を回るのではなく、カメラ位置を固定して視線方向を変えます。',
    fill('M10 17 H22 V27 H10Z') + p('M13 17 V13 H19 V17 M16 27 V30')
    + p('M16 13 6 4 M16 13 27 4',stroke_dasharray='2 3')
    + accent('M5 12 C2 3 28 3 28 12 M25 9 28 12 30 8'),
    ['camera', 'turn', 'look direction', 'pivot', 'カメラ', '向き', '視線方向', '旋回'])

add('view-break', 'CAD', 'Break view', '破断ビュー', 'view-presentation',
    'Shorten a long model presentation with break lines without cutting the source geometry.',
    '元の形状を切断せずに、破断線を使って長いモデルの表示を短縮します。',
    fill('M3 8 H12 L9 13 13 19 10 24 H3Z')
    + fill('M22 8 H29 V24 H20 L23 19 19 13Z')
    + accent('M12 5 9 13 13 19 10 27 M22 5 19 13 23 19 20 27'),
    ['view', 'break', 'shorten', 'presentation', 'ビュー', '破断', '省略', '表示'])

# Grouped display options remain one operation family per glyph.
add('display-style', 'CAD', 'Choose display style', '表示スタイルの選択', 'viewport-display',
    'Choose wireframe, hidden-line, shaded or related viewport display styles.',
    'ワイヤーフレーム・隠線・シェーディングなどの表示スタイルを選択します。',
    p('M5 10 16 4 27 10 V23 L16 29 5 23Z M5 10 16 16 27 10 M16 16 V29')
    + p('M16 16 27 10 V23 L16 29Z',fill=PALE,stroke=TEAL)
    + p('M5 23 16 17 M16 4 V17',stroke_dasharray='2 3'),
    ['display style', 'wireframe', 'shaded', 'hidden lines', '表示スタイル', 'ワイヤーフレーム', 'シェーディング', '隠線'])

add('change-transparency', 'CAD', 'Change transparency', '透明度の変更', 'viewport-display',
    'Change component or assembly opacity while retaining the visible geometry.',
    '形状を表示したまま、部品やアセンブリの不透明度を変更します。',
    r(3,4,18,18,1,fill=PALE) + r(11,12,18,18,1)
    + p('M11 12 H21 V22 H11Z',stroke=TEAL,stroke_dasharray='2 2')
    + p('M15 26 25 16 M20 27 26 21',stroke=TEAL),
    ['transparency', 'opacity', 'assembly', 'component', '透明度', '不透明度', 'アセンブリ', '部品'])

add('ambient-occlusion', 'CAD', 'Ambient occlusion', 'アンビエントオクルージョン', 'viewport-display',
    'Show contact and crevice shadowing to clarify depth where surfaces are close together.',
    '面同士が近い接触部や隙間の陰影を表示して奥行きを明確にします。',
    p('M4 5 V25 H28') + fill('M10 19 20 14 27 18 17 24Z')
    + p('M10 8 20 4 27 8 V18 L17 23 10 19Z',fill=PALE)
    + p('M10 8 17 12 27 8 M17 12 V23')
    + p('M4.5 21.5 H10.5 L16.5 24.5 H27 V27.5 H15.5 L9.5 24.5 H4.5Z',
        fill=INK,stroke='none'),
    ['ambient occlusion', 'contact shadow', 'depth', 'アンビエントオクルージョン', '接触影', '奥行き'])

add('shadows-in-shaded-mode', 'CAD', 'Shaded-mode shadows', 'シェーディング時の影', 'viewport-display',
    'Display cast shadows from model geometry in the shaded viewport.',
    'シェーディング表示で、モデル形状が地面などに落とす影を表示します。',
    p('M4 28 H29') + p('M13 23 23 19 29 24 19 28Z',fill=INK,stroke=INK)
    + small_cube(5,9,13,14) + c(25,5,2,stroke=TEAL)
    + accent('M20 3 18 2 M27 10 28 12 M29 5 H30'),
    ['shadows', 'shaded', 'cast shadow', 'light', '影', 'シェーディング', '投影', '光源'])

add('viewport-quality', 'CAD', 'Viewport graphics quality', 'ビュー描画品質', 'viewport-display',
    'Choose viewport rendering quality and performance options, including draft hidden-line display.',
    '簡易隠線表示など、ビューの描画品質と処理性能に関する設定を選択します。',
    r(3,4,26,24,2) + p('M7 22 V18 H11 V12 H15 V8')
    + accent('M18 22 Q18 10 26 8') + p('M16 7 V25',stroke_dasharray='2 3'),
    ['viewport', 'graphics', 'quality', 'performance', 'ビュー', 'グラフィックス', '品質', '性能'])

# Rendering setup is separate from executing the existing photoreal renderer.
add('hdr-environment', 'CAD', 'HDR environment', 'HDR環境', 'render-environment',
    'Apply or capture high-dynamic-range environmental illumination for rendering.',
    'レンダリング用の高ダイナミックレンジ環境照明を適用または取得します。',
    p('M3 24 A13 13 0 0 1 29 24Z',fill=PALE)
    + p('M3 24 Q16 17 29 24 M16 11 V24 M8 15 Q5 21 8 24 M24 15 Q27 21 24 24')
    + c(16,5,2,stroke=TEAL) + accent('M11 5 H9 M23 5 H21 M16 1 V2'),
    ['HDR', 'environment', 'illumination', 'panorama', 'HDR', '環境', '照明', '全天球'])

add('render-lighting', 'CAD', 'Set studio lighting', 'スタジオ照明設定', 'render-lighting',
    'Apply or configure studio light emitters and lighting rigs for rendering.',
    'レンダリング用のスタジオ光源や照明リグを適用・設定します。',
    fill('M8 5 16 9 12 18 4 14Z') + p('M8 16 V25 M3 29 8 25 13 29')
    + accent('M17 12 27 11 M16 17 26 23 M14 20 20 29')
    + p('M23 4 V8 M21 6 H25'),
    ['render', 'lighting', 'studio', 'emitter', 'レンダリング', '照明', 'スタジオ', '光源'])

add('render-stage', 'CAD', 'Set render stage', 'レンダリングステージ設定', 'render-stage',
    'Create or replace render-only ground and backdrop surfaces without altering CAD geometry.',
    'CAD形状を変更せずに、レンダリング専用の地面や背景面を作成・置換します。',
    fill('M4 4 H28 V23 Q28 28 23 28 H4Z')
    + p('M4 20 H22 Q28 20 28 14')
    + small_cube(10,14,10,9) + accent('M5 8 H9 M5 12 H9'),
    ['render', 'stage', 'ground', 'backdrop', 'レンダリング', 'ステージ', '地面', '背景面'])

add('studio-preset', 'CAD', 'Apply studio preset', 'スタジオプリセット適用', 'render-scene',
    'Apply a coordinated environment, lighting and stage preset to a scene.',
    '環境・照明・ステージを組み合わせたプリセットをシーンに適用します。',
    r(3,4,26,24,2) + p('M3 21 H29') + c(22,10,3,stroke=TEAL)
    + fill('M8 19 13 16 18 19 V24 L13 27 8 24Z')
    + p('M8 19 13 22 18 19 M13 22 V27')
    + accent('M6 8 8 10 6 12'),
    ['render', 'scene', 'studio preset', 'environment', 'レンダリング', 'シーン', 'スタジオプリセット', '環境'])

add('render-library', 'CAD', 'Browse render assets', 'レンダリング素材参照', 'render-library',
    'Browse render resources such as environments, light rigs, stage surfaces and quality presets.',
    '環境・照明リグ・ステージ面・品質プリセットなどのレンダリング素材を参照します。',
    p('M7 3 H28 V24 M4 6 H25 V27') + r(2,9,20,21,1,fill=PALE)
    + c(16,15,2,stroke=TEAL)
    + p('M5 25 10 19 14 23 19 18 V27 H5Z',fill='white'),
    ['render', 'asset', 'library', 'resource', 'レンダリング', '素材', 'ライブラリ', 'リソース'])

add('render-effects', 'CAD', 'Render image effects', 'レンダリング画像効果', 'render-finishing',
    'Inspect or adjust lens, creative finishing and regrading effects on rendered images.',
    'レンダリング画像のレンズ効果・仕上げ・色調整を確認または変更します。',
    c(13,17,9,fill=PALE) + c(13,17,4)
    + accent('M23 3 25 8 30 10 25 12 23 17 21 12 16 10 21 8Z')
    + p('M25 23 V29 M22 26 H28'),
    ['render', 'effects', 'lens', 'regrade', 'finishing', 'レンダリング', '効果', 'レンズ', '色調整', '仕上げ'])

add('render-preflight', 'CAD', 'Check render request', 'レンダリング要求の検査', 'render-validation',
    'Validate a render request and its resources before dispatching the render job.',
    'レンダリングジョブを送る前に、要求内容と必要なリソースを検証します。',
    r(3,4,23,23,2) + p('M7 21 12 15 17 20 22 13')
    + c(10,10,2,stroke=TEAL)
    + p('M14 25 22 31 31 19 28 16 21 24 18 21Z',fill='white',stroke='none')
    + accent('M17 25 22 29 30 18'),
    ['render', 'preflight', 'validate', 'request', 'レンダリング', '事前検査', '検証', '要求'])

# Selection interaction and hierarchy editing.
add('magnified-selection', 'CAD', 'Magnified selection', '拡大選択', 'selection',
    'Use a local magnified view to accurately pick small or densely packed geometry.',
    '局所的に拡大した表示を使い、小さい形状や密集した形状を正確に選択します。',
    c(13,13,10,fill=PALE) + p('M20 20 29 29')
    + p('M8 7 V18 L12 14 H18Z',fill='white') + accent('M8 14 H17'),
    ['selection', 'magnified', 'precision', 'pick', '選択', '拡大', '精密', 'ピック'])

add('select-by-criteria', 'CAD', 'Select by criteria', '条件による選択', 'selection',
    'Select model entities by properties such as size, visibility, type or component identity.',
    '大きさ・表示状態・種類・部品の同一性などの条件でモデル要素を選択します。',
    fill('M3 4 H28 L19 15 V22 L12 26 V15Z')
    + p('M8 8 H23') + pointer(20,18),
    ['selection', 'criteria', 'advanced', 'properties', '選択', '条件', '詳細', '属性'])

add('select-over-geometry', 'CAD', 'Select over geometry', '形状上で範囲選択', 'selection',
    'Start a selection window over model geometry instead of picking the geometry beneath the pointer.',
    'ポインタ下の形状を直接選択せず、形状上から範囲選択を開始します。',
    small_cube(8,7,17,16) + r(3,3,19,18,1,stroke=TEAL,stroke_dasharray='3 3')
    + pointer(3,4),
    ['selection', 'window', 'over geometry', 'drag', '選択', '範囲', '形状上', 'ドラッグ'])

add('select-related', 'CAD', 'Select related components', '関連部品を選択', 'selection',
    'Select components connected by an assembly relation such as a mate or shared axis.',
    '合致や共通軸などのアセンブリ関係を持つ部品を選択します。',
    r(3,6,10,14,1,fill=PALE) + r(19,6,10,14,1)
    + accent('M8 13 H24 M16 4 V24',stroke_dasharray='2 3')
    + pointer(18,18),
    ['selection', 'related', 'mated', 'coaxial', '選択', '関連', '合致', '同軸'])

add('volume-select', 'CAD', 'Volume selection', '体積範囲による選択', 'selection',
    'Select eligible model entities inside a three-dimensional selection volume.',
    '三次元の選択領域の内部にあるモデル要素を選択します。',
    p('M4 10 15 4 28 10 V23 L17 29 4 23Z M4 10 17 16 28 10 M17 16 V29',
      stroke=TEAL,stroke_dasharray='3 3')
    + r(9,14,5,6,1,fill=PALE) + r(21,15,4,5,1,fill=PALE)
    + accent('M2 14 V8 H7 M25 27 H30 V22'),
    ['selection', 'volume', '3D', 'inside', '選択', '体積', '三次元', '内部'])

add('reorder-tree-items', 'Common', 'Move tree items', 'ツリー項目の移動', 'hierarchy',
    'Move tree items to an explicit position or container without sorting by a property.',
    '属性による並べ替えとは別に、ツリー項目を指定位置やコンテナへ移動します。',
    p('M4 4 V26 H10 M4 8 H10 M4 17 H10')
    + r(10,4,12,7,1,fill=PALE) + r(10,22,12,7,1)
    + p('M11 16 H21',stroke_dasharray='2 2')
    + accent('M26 5 V24 M23 21 26 24 29 21'),
    ['tree', 'reorder', 'move', 'hierarchy', 'ツリー', '順序変更', '移動', '階層'])

add('tree-expand-all', 'Common', 'Expand all branches', 'すべての枝を展開', 'hierarchy',
    'Expand hierarchy branches to reveal their child items without changing model visibility.',
    'モデルの表示状態を変えずに、階層の枝を展開して子項目を表示します。',
    r(4,3,11,6,1,fill=PALE) + p('M9 9 V25 H16 M9 16 H16')
    + r(16,13,12,6,1) + r(16,23,12,6,1)
    + accent('M22 2 V9 M19 6 22 9 25 6'),
    ['tree', 'expand', 'children', 'hierarchy', 'ツリー', '展開', '子項目', '階層'])

add('tree-collapse-all', 'Common', 'Collapse all branches', 'すべての枝を折りたたむ', 'hierarchy',
    'Collapse hierarchy branches without hiding model geometry.',
    'モデル形状を非表示にせずに、階層の枝を折りたたみます。',
    r(4,3,11,6,1,fill=PALE)
    + p('M9 11 V25 H16 M9 16 H16 M17 13 H28 V19 H17 M17 23 H28 V29 H17',stroke_dasharray='2 3')
    + accent('M22 10 V3 M19 6 22 3 25 6'),
    ['tree', 'collapse', 'children', 'hierarchy', 'ツリー', '折りたたみ', '子項目', '階層'])

# Application utilities that are not document creation or model operations.
add('check-read-only-files', 'Common', 'Check read-only files', '読取専用ファイルの更新確認', 'document-status',
    'Check whether externally modified read-only documents need to be reloaded.',
    '外部で変更された読取専用文書について、再読込みが必要か確認します。',
    fill('M4 3 H17 L22 8 V26 H4Z') + p('M17 3 V8 H22 M8 12 H15 M8 17 H13')
    + c(23,22,6,fill='white') + p('M27 27 30 30')
    + p('M21 22 V20 A2 2 0 0 1 25 20 V22 M20 22 H26 V25 H20Z',stroke=TEAL),
    ['file', 'read only', 'external changes', 'check', 'ファイル', '読取専用', '外部変更', '確認'])

add('crash-diagnostics', 'Common', 'Inspect crash reports', 'クラッシュレポート確認', 'diagnostics',
    'Open crash reports and diagnostic traces to investigate an application failure.',
    'アプリケーション障害を調べるため、クラッシュレポートや診断トレースを開きます。',
    fill('M5 3 H22 L27 8 V29 H5Z') + p('M22 3 V8 H27 M9 22 H20 M9 26 H17')
    + p('M3 15 H10 L13 10 17 20 20 14 H29',stroke=AMBER),
    ['crash', 'diagnostics', 'report', 'trace', 'クラッシュ', '診断', 'レポート', 'トレース'])

add('evaluate-expression', 'Common', 'Evaluate expression', '式を評価', 'expression-evaluation',
    'Evaluate a dimensional or numeric expression without creating a model parameter.',
    'モデルのパラメータを作成せずに、単位付きまたは数値の式を評価します。',
    r(5,3,22,26,2,fill=PALE) + r(9,6,14,6,1,fill='white')
    + p('M9 18 H15 M12 15 V21 M19 16 H23 M19 20 H23 M10 25 H14 M20 24 22 26 M22 24 20 26'),
    ['expression', 'evaluate', 'calculator', 'units', '式', '評価', '計算', '単位'])

add('format-painter', 'Common', 'Format painter', '書式のコピー', 'formatting',
    'Copy formatting from one document element and apply it to another.',
    '文書要素の書式をコピーして別の要素に適用します。',
    r(4,4,18,8,2,fill=PALE) + p('M22 8 H28 V18 H17 V21')
    + r(14,21,6,9,2,fill=PALE) + accent('M8 7 H18'),
    ['format', 'painter', 'copy style', '書式', 'コピー', 'スタイル'])

add('markups', 'Common', 'Create markups', 'マークアップ作成', 'review-annotation',
    'Add review markup and freehand annotations without editing the source model geometry.',
    '元のモデル形状を編集せずに、レビュー用のマークアップや手書き注釈を追加します。',
    p('M25 12 Q29 7 24 4 Q20 1 16 5 Q11 0 7 5 Q2 4 3 11 Q0 15 5 18')
    + p('M6 22 Q10 25 14 21',stroke=TEAL)
    + p('M12 26 15 19 25 9 29 13 19 23Z',fill=PALE)
    + p('M15 19 19 23 M12 26 17 25',stroke=TEAL),
    ['markup', 'review', 'freehand', 'annotation', 'マークアップ', 'レビュー', '手書き', '注釈'])

add('spell-checker', 'Common', 'Check spelling', 'スペルチェック', 'text-review',
    'Check text and annotations for spelling errors and review suggested corrections.',
    'テキストや注釈のスペルを確認し、修正候補を検討します。',
    p('M4 20 10 4 16 20 M6 15 H14 M19 5 H27 M19 10 H25')
    + p('M4 25 Q6 22 8 25 Q10 28 12 25',stroke=AMBER)
    + accent('M18 24 22 28 29 18'),
    ['spelling', 'text', 'annotation', 'proofread', 'スペル', 'テキスト', '注釈', '校正'])

add('new-window', 'Common', 'Open new window', '新しいウィンドウ', 'workspace',
    'Open another window onto an existing document without creating a new document.',
    '新しい文書を作成せずに、既存文書を表示する別のウィンドウを開きます。',
    p('M4 22 H2 V3 H23 V7') + r(7,9,23,21,2,fill=PALE)
    + p('M7 15 H30') + accent('M13 22 H24 M18.5 17 V27'),
    ['window', 'new', 'existing document', 'ウィンドウ', '追加', '既存文書'])

add('workspace-layout', 'Common', 'Arrange workspace', 'ワークスペース配置', 'workspace',
    'Arrange docked panels, history areas or tiled document windows in the workspace.',
    'ドッキングパネル・履歴領域・文書ウィンドウをワークスペース内に配置します。',
    r(3,4,26,24,2) + p('M3 10 H29 M11 10 V28 M11 22 H29')
    + r(5,12,4,14,0,fill=PALE,stroke='none') + r(13,12,14,8,0,fill=PALE,stroke='none')
    + accent('M14 25 H25'),
    ['workspace', 'layout', 'dock', 'tile', 'ワークスペース', '配置', 'ドック', '並べて表示'])

add('work-offline', 'Common', 'Work offline', 'オフライン作業', 'document-workflow',
    'Use a disconnected document workflow when the cloud connection is unavailable or disabled.',
    'クラウド接続を無効にした場合や利用できない場合に、切断状態の文書作業へ切り替えます。',
    p('M7 14 H6 A4 4 0 0 1 6 6 A7 7 0 0 1 19 5 A5 5 0 0 1 24 14 H22')
    + r(4,19,24,10,1,fill=PALE) + p('M8 25 H11 M23 24 H24')
    + accent('M16 13 V20',stroke_dasharray='1 3')
    + p('M22 3 29 10 M29 3 22 10',stroke=AMBER),
    ['offline', 'disconnected', 'cloud', 'local work', 'オフライン', '切断', 'クラウド', 'ローカル作業'])


# Exact command aliases and evidence IDs from the frozen audit.
_EVIDENCE = {'activate-display-state': {'aliases': ['Change Display States', 'Activate Display State'],
                            'sources': ['gui-audit-f30c7dc7d5', 'gui-audit-117fa3c165']},
 'add-configuration': {'aliases': ['Add Configuration'], 'sources': ['gui-audit-8ff0ee5324']},
 'add-rebuild-on-save-mark': {'aliases': ['Add Rebuild on Save Mark'],
                              'sources': ['gui-audit-8ff0ee5324']},
 'add-walk-through': {'aliases': ['Add Walk-through'], 'sources': ['gui-audit-f30c7dc7d5']},
 'ambient-occlusion': {'aliases': ['view.ambient_occlusion', 'Ambient Occlusion'],
                       'sources': ['gui-audit-875626de06', 'gui-audit-f30c7dc7d5']},
 'appearance-library': {'aliases': ['appearance.library',
                                    'appearance.list',
                                    'render.library.appearance.apply'],
                        'sources': ['gui-audit-08eeb2032b', 'gui-audit-43d4d0f047']},
 'assign-appearance': {'aliases': ['appearance.assign'], 'sources': ['gui-audit-ecd16ac847']},
 'camera-view': {'aliases': ['Camera View'], 'sources': ['gui-audit-f30c7dc7d5']},
 'change-transparency': {'aliases': ['Change Transparency',
                                     'Assembly Transparency',
                                     'Top Level Transparency (Assemblies)',
                                     'Top Level Transparency (Parts)'],
                         'sources': ['gui-audit-8a41850734']},
 'check-read-only-files': {'aliases': ['Check Read-only Files'],
                           'sources': ['gui-audit-8f5f9d7f22']},
 'checkpoint-restore': {'aliases': ['edit.restore_checkpoint'],
                        'sources': ['gui-audit-a3a82707e9']},
 'checkpoint-save': {'aliases': ['edit.checkpoint'], 'sources': ['gui-audit-a3a82707e9']},
 'configuration-preview': {'aliases': ['config.preview'], 'sources': ['gui-audit-e02b0eaa69']},
 'configuration-rules': {'aliases': ['config.rule'], 'sources': ['gui-audit-e02b0eaa69']},
 'crash-diagnostics': {'aliases': ['diagnostics.crash_reports', 'diagnostics.crash_report'],
                       'sources': ['gui-audit-a5fe59e311']},
 'dependency-graph': {'aliases': ['timeline.dependents',
                                  'parameters.users',
                                  'parameters.graph',
                                  'Dynamic Reference Visualization',
                                  'Dynamic Reference Visualization (Child)'],
                      'sources': ['gui-audit-950e136ff6',
                                  'gui-audit-676d40e2c6',
                                  'gui-audit-8a41850734']},
 'design-check': {'aliases': ['Check Active Document', 'Check Against Existing File'],
                  'sources': ['gui-audit-4396f7e3ba']},
 'design-check-rules': {'aliases': ['Build Checks', 'Learn Checks Wizard'],
                        'sources': ['gui-audit-4396f7e3ba']},
 'design-library': {'aliases': ['library.inspect'], 'sources': ['gui-audit-0b7fca4246']},
 'directional-modulus': {'aliases': ['material.properties.directional'],
                         'sources': ['gui-audit-1360b317c3']},
 'display-style': {'aliases': ['Wireframe',
                               'Hidden Lines Visible',
                               'Hidden Lines Removed',
                               'Shaded with Edges',
                               'Shaded',
                               'Cartoon'],
                   'sources': ['gui-audit-f30c7dc7d5']},
 'evaluate-expression': {'aliases': ['expr.evaluate'], 'sources': ['gui-audit-406303650d']},
 'format-painter': {'aliases': ['Format Painter'], 'sources': ['gui-audit-4396f7e3ba']},
 'hdr-environment': {'aliases': ['render.library.environment.apply', 'render.settings.capture_hdr'],
                     'sources': ['gui-audit-43d4d0f047']},
 'isometric-view': {'aliases': ['view.isometric'], 'sources': ['gui-audit-875626de06']},
 'magnified-selection': {'aliases': ['Magnified Selection'],
                         'sources': ['gui-audit-cba07c324a', 'gui-audit-8f5f9d7f22']},
 'markups': {'aliases': ['Markups'], 'sources': ['gui-audit-4396f7e3ba']},
 'material-library': {'aliases': ['material.list', 'material.create'],
                      'sources': ['gui-audit-1360b317c3']},
 'material-validation': {'aliases': ['material.properties.validate'],
                         'sources': ['gui-audit-1360b317c3']},
 'named-view-restore': {'aliases': ['view.apply', 'render.settings.apply'],
                        'sources': ['gui-audit-43d4d0f047', 'gui-audit-875626de06']},
 'new-window': {'aliases': ['New Window'], 'sources': ['gui-audit-8f5f9d7f22']},
 'previous-view': {'aliases': ['Previous View'], 'sources': ['gui-audit-f30c7dc7d5']},
 'render-effects': {'aliases': ['render.effects.describe', 'render.result.regrade'],
                    'sources': ['gui-audit-43d4d0f047']},
 'render-library': {'aliases': ['render.library.list'], 'sources': ['gui-audit-43d4d0f047']},
 'render-lighting': {'aliases': ['render.library.studio.apply'],
                     'sources': ['gui-audit-43d4d0f047']},
 'render-preflight': {'aliases': ['render.preflight'], 'sources': ['gui-audit-43d4d0f047']},
 'render-stage': {'aliases': ['render.stage.ground', 'render.stage.backdrop'],
                  'sources': ['gui-audit-43d4d0f047']},
 'reorder-tree-items': {'aliases': ['browser.move',
                                    'browser.order',
                                    'timeline.move_to_group',
                                    'timeline.move_many',
                                    'timeline.reorder',
                                    'timeline.reorder_many',
                                    'parameters.move'],
                        'sources': ['gui-audit-c14a946b6f',
                                    'gui-audit-950e136ff6',
                                    'gui-audit-676d40e2c6']},
 'roll-view': {'aliases': ['Roll View'], 'sources': ['gui-audit-f30c7dc7d5']},
 'select-by-criteria': {'aliases': ['Power Select',
                                    'Select Bodies By Size',
                                    'Select Bodies By Volume',
                                    'Select Suppressed',
                                    'Select Hidden',
                                    'Select Identical Components',
                                    'Select Internal Components',
                                    'Select By Size',
                                    'Select By Views',
                                    'Select Toolbox',
                                    'Select Flexible Subassembly',
                                    'Advanced Select'],
                        'sources': ['gui-audit-cba07c324a', 'gui-audit-4396f7e3ba']},
 'select-over-geometry': {'aliases': ['Select over Geometry'],
                          'sources': ['gui-audit-cba07c324a', 'gui-audit-8f5f9d7f22']},
 'select-related': {'aliases': ['Select Mated To', 'Select Coaxial Components'],
                    'sources': ['gui-audit-cba07c324a']},
 'shadows-in-shaded-mode': {'aliases': ['Shadows in Shaded Mode'],
                            'sources': ['gui-audit-f30c7dc7d5']},
 'spell-checker': {'aliases': ['Spell Checker'], 'sources': ['gui-audit-4396f7e3ba']},
 'standard-view': {'aliases': ['view.front',
                               'view.back',
                               'view.left',
                               'view.right',
                               'view.top',
                               'view.bottom',
                               'View Orientation'],
                   'sources': ['gui-audit-875626de06', 'gui-audit-f30c7dc7d5']},
 'studio-preset': {'aliases': ['render.preset.apply', 'Apply Scene'],
                   'sources': ['gui-audit-43d4d0f047', 'gui-audit-f30c7dc7d5']},
 'tree-collapse-all': {'aliases': ['browser.collapse_all'], 'sources': ['gui-audit-c14a946b6f']},
 'tree-expand-all': {'aliases': ['browser.expand_all'], 'sources': ['gui-audit-c14a946b6f']},
 'turn-camera': {'aliases': ['Turn Camera'], 'sources': ['gui-audit-f30c7dc7d5']},
 'view-break': {'aliases': ['Model Break View', 'Break View'],
                'sources': ['gui-audit-7830b955e2',
                            'gui-audit-8a41850734',
                            'gui-audit-c2a5f59b1b']},
 'view-normal-to': {'aliases': ['view.normal_to'], 'sources': ['gui-audit-875626de06']},
 'viewport-quality': {'aliases': ['view.graphics_preset', 'Draft Quality HLR/HLV'],
                      'sources': ['gui-audit-875626de06', 'gui-audit-f30c7dc7d5']},
 'volume-select': {'aliases': ['Volume Select'], 'sources': ['gui-audit-cba07c324a']},
 'work-offline': {'aliases': ['Work Offline'], 'sources': ['gui-audit-8f5f9d7f22']},
 'workspace-layout': {'aliases': ['view.layout',
                                  'view.history_layout',
                                  'Tile Horizontally',
                                  'Tile Vertically'],
                      'sources': ['gui-audit-875626de06', 'gui-audit-8f5f9d7f22']}}

for _item in ITEMS:
    _item.update(_EVIDENCE[_item['id']])
