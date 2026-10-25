"""Reuse existing geometry for persistent nodes; no duplicate SVGs are emitted.

role is the primary semantic role. usages are supported UI contexts, and may
contain model-tree alongside command/tool. Tree labels name the resulting object.
"""
# Additional families have explicitly reviewed node metadata in their records.
from application import APPLICATION_TREE, APPLICATION_NAMES
from robotics import ROBOTICS_TREE, ROBOTICS_NAMES
from studio import STUDIO_TREE, STUDIO_NAMES
# Explicitly reviewed reuse, grouped only to keep metadata maintainable.
TREE = {}
def reuse(domain, ids, kind):
    for id in ids.split():
        TREE[f'{domain}-{id}'] = {'objectType':kind}
reuse('common','folder','folder')
reuse('common','group','group')
reuse('common','layers','layer')
reuse('common','link','external-reference')
reuse('common','history','history')
reuse('cad','part','component')
reuse('cad','assembly','assembly')
reuse('cad','solid-body','solid-body')
reuse('cad','mesh-body','mesh-body')
reuse('cad','sketch','sketch')
reuse('cad','face','face')
reuse('cad','extrude revolve sweep loft pocket fillet chamfer shell boolean-union boolean-subtract boolean-intersection linear-pattern circular-pattern mirror sheet-metal-bend sheet-metal-flange sheet-metal-unfold sheet-metal-flat-pattern surface-sew surface-trim hole thread draft rib split-body surface-thicken surface-offset mesh-to-brep','feature')
reuse('cad','surface-patch','surface-body')
reuse('cad','datum-plane','datum-plane')
reuse('cad','datum-axis','datum-axis')
reuse('cad','revolute-joint fixed-joint prismatic-joint','joint')
reuse('cam','setup','machining-setup')
reuse('cam','stock-setup','stock')
reuse('cam','work-coordinate-system','coordinate-system')
reuse('cam','fixture-clamp','fixture')
reuse('cam','end-mill ball-end-mill','cutting-tool')
reuse('cam','face-milling contour-milling pocket-milling adaptive-clearing rest-machining parallel-finishing swarf-milling drilling peck-drilling tapping external-turning internal-boring parting thread-milling engrave deburr','machining-operation')
reuse('cam','holding-tabs','operation-control')
reuse('cam','post-process','nc-program')
reuse('cae','tetrahedral-mesh hexahedral-mesh','finite-element-mesh')
reuse('cae','mesh-refinement boundary-layer-mesh','mesh-control')
reuse('cae','material-assignment','material')
reuse('cae','shell-element beam-element','element-property')
reuse('cae','fixed-support displacement-boundary thermal-boundary fluid-inlet symmetry-boundary fluid-outlet wall-boundary','boundary-condition')
reuse('cae','force-load pressure-load gravity-load moment-load','load')
reuse('cae','contact-pair','contact')
reuse('cae','static-structural modal-analysis buckling-analysis new-study','analysis-study')
reuse('cae','stress-contour result-probe result-plot deformation-result streamline-result','result')
reuse('cae','named-selection','named-selection')
reuse('cae','solver-settings','analysis-settings')
reuse('cmm','point-cloud','point-cloud')
reuse('cmm','tactile-probe laser-scanner','probe')
reuse('cmm','inspection-plan','inspection-program')
reuse('olp','robot-arm','robot')
reuse('olp','robot-cell','robot-cell')
reuse('olp','external-linear-axis positioner','mechanism')
reuse('olp','reference-frame tool-frame tool-center-point','coordinate-system')
reuse('olp','joint-target cartesian-target','robot-target')
reuse('olp','joint-move linear-move circular-move digital-output wait-signal call-program','program-instruction')

# Contextual noun labels avoid displaying an action such as "New study" as a node.
NAMES = {
 'common-group':('Group','グループ'),
 'common-layers':('Layer','レイヤー'),
 'common-link':('External reference','外部参照'),
 'cad-datum-plane':('Datum plane','基準平面'),
 'cad-datum-axis':('Datum axis','基準軸'),
 'cad-surface-patch':('Surface body','サーフェスボディ'),
 'cad-surface-sew':('Sew feature','縫合フィーチャ'),
 'cad-surface-trim':('Surface trim feature','サーフェストリムフィーチャ'),
 'cad-sheet-metal-unfold':('Unfold feature','曲げ解除フィーチャ'),
 'cad-sheet-metal-flat-pattern':('Flat pattern','展開形状'),
 'cad-mirror':('Mirror feature','ミラーフィーチャ'),
 'cad-mesh-to-brep':('Mesh conversion','メッシュ変換'),
 'cae-solver-settings':('Analysis settings','解析設定'),
 'cad-split-body':('Split feature','分割フィーチャ'),
 'cad-surface-thicken':('Thicken feature','厚み付けフィーチャ'),
 'cad-surface-offset':('Offset surface feature','面オフセットフィーチャ'),
 'cam-stock-setup':('Stock','素材'),
 'cam-post-process':('NC program','NCプログラム'),
 'cae-new-study':('Simulation study','解析スタディ'),
 'cae-material-assignment':('Material','材料'),
 'cae-result-probe':('Result probe','結果プローブ'),
 'cae-result-plot':('Result plot','結果グラフ'),
 'olp-reference-frame':('Coordinate system','座標系'),
 'olp-call-program':('Subprogram call','サブプログラム呼出し'),
}
SHARED = {
 'cae-material-assignment':['CAD'],
 'cmm-point-cloud':['CAD'],
 'olp-reference-frame':['CAD','CAM','CAE'],
}
TREE.update(APPLICATION_TREE)
NAMES.update(APPLICATION_NAMES)
TREE.update(ROBOTICS_TREE)
NAMES.update(ROBOTICS_NAMES)
TREE.update(STUDIO_TREE)
NAMES.update(STUDIO_NAMES)

from toolbar_context_additions import TREE as TOOLBAR_CONTEXT_TREE
TREE.update(TOOLBAR_CONTEXT_TREE)

TREE['cad-implicit-body']={'objectType':'implicit-body'}

def apply_usage(item):
    role = item['role']
    item['usages'] = [] if role == 'object' else [role]
    if item['id'] in TREE:
        item['usages'].append('model-tree')
        item.update(TREE[item['id']])
        item['nodeName'],item['nodeNameJa'] = NAMES.get(item['id'],(item['name'],item['nameJa']))
        item['tags'] = list(dict.fromkeys(item['tags'] + ['model tree','tree node','object','モデルツリー','ツリーノード',item['nodeName'].lower(),item['nodeNameJa']]))
        if item['category']=='CAD' and item['objectType']=='feature':
            item['sources']=list(dict.fromkeys(item['sources']+['onshape-feature-parts']))
    if role == 'object' and 'model-tree' not in item['usages']:
        raise ValueError('Object lacks explicit tree metadata: '+item['id'])
    if item['id']=='cae-solver-settings':
        item['sources']=list(dict.fromkeys(item['sources']+['ansys-analysis-tree']))
    if item['id']=='cam-post-process':
        item['sources']=list(dict.fromkeys(item['sources']+['fusion-nc-program']))
    if item['id']=='cad-part':
        item['nodeAliases']=list(dict.fromkeys(item.get('nodeAliases',[])+['component instance','occurrence','部品インスタンス','配置部品']))
    item['categories'] = list(dict.fromkeys(item['categories']+SHARED.get(item['id'],[])+item.pop('sharedCategories',[])))
