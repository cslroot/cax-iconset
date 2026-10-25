"""Original residual joint, manufacturing and graph-status glyphs."""
from core import p,r,c,accent,PALE,TEAL
ITEMS=[]
def add(id,en,ja,desc,descja,body,family,role='command'):
    ITEMS.append(dict(id=id,domain='CAD',name=en,nameJa=ja,description=desc,
        descriptionJa=descja,body=body,family=family,role=role,
        tags=[family,en.lower(),ja,'cad'],aliases=[],sources=[]))

add('cylindrical-joint','Cylindrical joint','円筒ジョイント',
    'Allow independent rotation about and translation along one common axis, without a screw-pitch relationship.',
    '共通軸に沿った並進と軸回りの回転を独立に許可します。ねじピッチによる連動はありません。',
    p('M5 13 H24 C28 13 28 23 24 23 H5 C1 23 1 13 5 13Z',fill=PALE)
    +p('M5 13 C9 13 9 23 5 23 M24 13 C20 13 20 23 24 23 M10 18 H22',stroke_dasharray='2 2')
    +accent('M5 5 H26 M8 2 5 5 8 8 M23 2 26 5 23 8 M20 27 C27 31 31 24 28 20 M25 22 28 20 29 24'),
    'cylindrical-joint')

add('line-on-plane','Constrain line to plane','直線を平面上に拘束',
    'Keep an entire line on a reference plane, with any permitted offset explicitly specified by the command.',
    '直線全体を参照平面上に拘束します。許可されるオフセットはコマンドの設定で明示します。',
    p('M3 22 12 8 29 11 20 26Z',fill=PALE)
    +accent('M7 20 25 14')+c(7,20,1.4,fill=TEAL,stroke=TEAL)+c(25,14,1.4,fill=TEAL,stroke=TEAL),
    'line-plane-incidence')

add('linear-travel-limits','Set linear travel limits','直線移動の範囲を制限',
    'Set minimum and maximum translation along a joint or mate axis; not a fixed separation or an angular bound.',
    'ジョイントや合致の軸に沿った並進の最小値と最大値を設定します。一定距離の合致や角度制限とは区別します。',
    p('M4 12 V27 M28 12 V27 M4 23 H28')+r(12,15,8,10,1,fill=PALE)
    +accent('M6 6 H26 M9 3 6 6 9 9 M23 3 26 6 23 9 M16 15 V25'),
    'linear-motion-limits')

add('define-forming-tool','Define forming tool','フォームツールを定義',
    'Define reusable sheet-forming tool geometry through stopping/removal faces and an insertion reference; does not apply or stamp the tool.',
    '停止面・除去面と挿入参照を指定して再利用可能な板金フォームツールを定義します。ツールの適用や刻印ではありません。',
    p('M4 16 10 12 H12 V7 Q16 2 20 7 V12 H23 L28 16 V22 L22 26 H10 L4 22Z',fill=PALE)
    +p('M4 16 10 20 H22 L28 16 M10 20 V26 M22 20 V26')
    +accent('M12 12 V7 Q16 2 20 7 V12 M12 12 H20')
    +c(16,23,3,stroke=TEAL)+accent('M16 18 V28 M11 23 H21'),
    'forming-tool-definition')

add('solid-corner-weld','Create modeled corner weld','ソリッドの隅肉溶接を作成',
    'Create modeled weld material at meeting faces or a folded sheet corner; sheet-specific options and flattening behavior belong to the command binding.',
    '接合する面や折り曲げた板金のコーナーに溶接形状を作成します。板金固有の設定や展開時の扱いはコマンドの文脈で区別します。',
    p('M4 5 H10 V21 H28 V27 H4Z',fill=PALE)
    +p('M10 9 24 21 H10Z',fill=TEAL,stroke=TEAL)
    +p('M10 9 14 6 28 18 24 21 M14 6 V18 H28')
    +p('M4 5 8 2 H14 V6 M28 21 V27'),
    'modeled-corner-weld')

add('mate-path-to-ground','Mate path to ground','固定部までの合致経路',
    'Status marker identifying a mate relation on the graph path to a grounded component; not a command to fix or lock components.',
    '固定されたコンポーネントへ至るグラフ経路上の合致であることを示す状態記号です。固定やロックを行うコマンドではありません。',
    accent('M7 8 H23 V17 H16 V25')
    +r(3,4,8,8,1,fill=PALE)+r(19,13,8,8,1,fill=PALE)
    +p('M9 25 H23 M10 25 7 29 M16 25 13 29 M22 25 19 29'),
    'mate-graph-status',role='status')
