"""Source-reviewed robotics semantics and original 32 px geometry.

Persistent nodes and commands share one symbol. Existing meanings are enriched
through explicit reuse records instead of emitting morphology/state variants.
"""
import json
from pathlib import Path
from core import p, r, c, g, accent, fill, nodes, PALE, TEAL

GLYPHS = {}

# Each drawing below implements one independently reviewed meaning.
GLYPHS['olp-reference-calibration'] = (
    p('M5 27 V10 M5 27 H23 M5 27 16 16',stroke_dasharray='2 3')
    + nodes([(5,10),(16,16),(23,27)])
    + accent('M13 23 V4 M13 23 H29 M13 23 24 12 M10 8 13 4 16 8 M25 20 29 23 25 26')
    + c(13,23,2,fill=PALE))
GLYPHS['olp-attach-object'] = (
    r(11,3,10,5,1,fill=PALE) + p('M11 8 6 13 V21 H10 M21 8 26 13 V21 H22')
    + r(12,20,8,8,1,fill=PALE) + accent('M16 17 V11 M13 14 16 11 19 14')
    + p('M9 25 H11 M21 25 H23',stroke=TEAL))
GLYPHS['olp-detach-object'] = (
    r(11,3,10,5,1,fill=PALE) + p('M11 8 5 12 3 18 H7 M21 8 27 12 29 18 H25')
    + r(12,22,8,7,1,fill=PALE) + accent('M16 11 V19 M13 16 16 19 19 16')
    + p('M7 29 H25',stroke_dasharray='2 3'))
GLYPHS['olp-program-if'] = (
    fill('M16 3 24 10 16 17 8 10Z') + p('M8 10 H4 V24 H10 M24 10 H28 V24 H22')
    + r(10,21,12,7,1,fill=PALE) + accent('M4 20 V24 H8 M25 21 28 24 30 21'))
GLYPHS['olp-program-loop'] = (
    r(10,10,12,12,2,fill=PALE) + p('M13 14 H19 M13 18 H17')
    + accent('M5 21 V8 Q5 4 9 4 H24 Q28 4 28 8 V24 Q28 28 24 28 H8 M2 17 5 21 8 17'))
GLYPHS['olp-variable-assignment'] = (
    r(3,6,9,20,2,fill=PALE) + p('M6 12 9 20 M9 12 6 20')
    + accent('M15 12 H28 M15 20 H28') + c(25,27,1,fill=TEAL,stroke='none'))
GLYPHS['olp-conveyor-tracking'] = (
    r(3,21,26,7,3,fill=PALE) + c(7,24.5,1.5) + c(25,24.5,1.5)
    + r(11,12,8,9,1,fill=PALE) + p('M4 4 H24 V10 M21 7 24 10 27 7')
    + accent('M12 6 H19 M16 3 19 6 16 9 M20 16 H29 M26 13 29 16 26 19'))
GLYPHS['olp-palletizing'] = (
    p('M3 26 H29 M5 26 V29 M27 26 V29')
    + r(5,17,9,9,1,fill=PALE) + r(17,17,9,9,1,fill=PALE)
    + r(11,6,9,9,1,fill=PALE) + accent('M24 5 H28 V13 M25 10 28 13 30 10')
    + p('M9 17 V26 M21 17 V26 M15 6 V15'))
GLYPHS['olp-planning-group'] = (
    r(3,4,26,24,4,stroke_dasharray='3 3') + p('M7 22 12 11 23 9')
    + nodes([(7,22),(12,11),(23,9)]) + accent('M10 25 H25 V14 M22 18 25 14 28 18'))
GLYPHS['olp-end-effector'] = (
    r(11,3,10,7,2,fill=PALE) + p('M11 10 5 16 V26 H11 V19 M21 10 27 16 V26 H21 V19')
    + accent('M12 27 H20 M15 24 12 27 15 30 M17 24 20 27 17 30'))
GLYPHS['olp-collision-matrix'] = (
    r(5,6,23,22,1) + p('M5 13 H28 M5 21 H28 M13 6 V28 M21 6 V28')
    + p('M8 9 10 11 M16 16 18 18 M24 24 26 26',stroke=TEAL)
    + accent('M15 24 17 26 20 22 M23 16 25 18 28 14')
    + p('M9 2 V3 M17 2 V3 M25 2 V3 M1 10 H2 M1 17 H2 M1 25 H2'))
GLYPHS['olp-motion-constraints'] = (
    p('M3 9 C12 1 20 16 29 7 M3 24 C12 16 20 31 29 22',stroke_dasharray='2 3')
    + accent('M3 17 C12 9 20 24 29 15') + r(12,12,8,8,1,fill=PALE)
    + p('M16 12 V6 M13 9 16 6 19 9 M20 16 H26'))
GLYPHS['olp-grasp-planning'] = (
    r(12,12,9,9,1,fill=PALE) + p('M4 9 V5 H11 M22 5 H28 V12 M4 22 V28 H11',stroke_dasharray='2 3')
    + accent('M7 16 H11 M7 16 V12 M7 16 V20 M16 7 V11 M12 7 H20 M23 24 H28 V18')
    + p('M22 26 25 29 30 23',stroke=TEAL))
GLYPHS['olp-trajectory-retiming'] = (
    p('M3 4 V28 H29') + accent('M6 24 10 16 15 16 19 24 28 24')
    + c(23,9,6,fill=PALE) + p('M23 5 V9 H26')
    + p('M8 28 V30 M17 28 V30 M26 28 V30'))
GLYPHS['olp-transform-tree'] = (
    p('M16 5 V15 M6 25 V15 H26 V25')
    + accent('M16 5 H22 M16 5 V1 M16 5 12 9 M6 25 H12 M6 25 V20 M6 25 2 29 M26 25 H31 M26 25 V20 M26 25 22 29')
    + nodes([(16,5),(6,25),(26,25)]))
GLYPHS['olp-robot-controller'] = (
    r(8,6,16,20,2,fill=PALE) + p('M4 10 H8 M4 16 H8 M4 22 H8 M24 10 H28 M24 16 H28 M24 22 H28')
    + accent('M11 16 H14 L16 10 19 22 21 16') + p('M12 2 V6 M20 2 V6 M12 26 V30 M20 26 V30'))
GLYPHS['olp-occupancy-map'] = (
    p('M7 11 18 5 29 11 V24 L18 30 7 24Z M7 11 18 17 29 11 M18 17 V30')
    + fill('M18 17 24 14 V21 L18 24Z') + fill('M7 11 12 14 V20 L7 17Z')
    + p('M7 17 18 23 29 17 M12 8 24 14 V27 M23 8 12 14 V27')
    + accent('M2 3 8 10 M1 8 6 12 M7 1 11 7'))
GLYPHS['cad-ball-joint'] = (
    p('M16 3 V9 M16 23 V29') + c(16,15,6,fill=PALE)
    + p('M6 13 C4 25 28 27 27 13')
    + accent('M6 9 C10 3 24 4 27 10 M23 9 27 10 27 6')
    + p('M16 9 C9 10 9 20 16 21',stroke=TEAL))
GLYPHS['cad-planar-joint'] = (
    fill('M3 17 16 10 29 17 16 25Z') + p('M16 25 V29')
    + accent('M7 18 23 18 M7 18 10 15 M7 18 10 21 M16 12 V23 M13 20 16 23 19 20')
    + p('M7 8 Q16 1 25 8 M21 8 H25 V4'))
GLYPHS['cad-floating-joint'] = (
    r(3,21,7,8,1,fill=PALE) + r(16,10,9,9,1,fill=PALE)
    + p('M7 20 15 16',stroke_dasharray='2 3')
    + accent('M20 9 V2 M17 5 20 2 23 5 M25 15 H30 M27 12 30 15 27 18 M18 19 12 25 M12 21 V25 H16')
    + p('M11 9 A10 10 0 0 1 28 6 M25 6 H28 V3'))
GLYPHS['cad-screw-joint'] = (
    p('M16 3 V29') + r(10,13,12,9,1,fill=PALE)
    + accent('M8 7 C8 1 25 3 25 8 C25 15 7 14 7 22 C7 29 25 29 25 23 M22 24 25 21 28 24')
    + p('M28 4 V15 M26 12 28 15 30 12'))
GLYPHS['cad-universal-joint'] = (
    p('M3 15 H11 M21 15 H29 M16 3 V10 M16 20 V29')
    + fill('M12 10 H20 V13 H23 V19 H20 V22 H12 V19 H9 V13 H12Z')
    + p('M12 10 V22 M20 10 V22') + accent('M3 9 Q3 4 8 4 M5 2 8 4 5 7 M22 23 Q27 23 27 28 M24 25 27 28 29 25'))
GLYPHS['cad-joint-coupling'] = (
    c(10,12,7,fill=PALE) + c(24,23,4,fill=PALE) + p('M10 9 V15 M7 12 H13 M24 20 V26')
    + accent('M15 17 20 21 M17 21 H20 V18 M5 24 H15 M12 21 15 24 12 27')
    + p('M21 4 H28 M21 8 H28'))
GLYPHS['olp-camera-sensor'] = (
    r(3,9,13,16,2,fill=PALE) + c(9.5,17,3)
    + p('M16 13 28 7 V27 L16 21Z',stroke=TEAL)
    + p('M6 5 H13 V9 M8 25 V29 M5 29 H12'))
GLYPHS['olp-imu-sensor'] = (
    r(10,11,12,12,2,fill=PALE) + c(16,17,2)
    + accent('M16 10 V2 M13 5 16 2 19 5 M23 17 H30 M27 14 30 17 27 20')
    + p('M6 11 C0 17 5 29 17 29 M14 26 17 29 14 31 M11 23 V26 M21 23 V26'))
GLYPHS['olp-force-torque-sensor'] = (
    r(6,12,20,5,1,fill=PALE) + r(6,21,20,5,1,fill=PALE)
    + p('M10 17 V21 M22 17 V21 M16 26 V30')
    + accent('M16 2 V10 M12 6 16 10 20 6 M4 18 C0 8 9 4 11 6 M8 3 11 6 8 8'))
GLYPHS['olp-manual-jog'] = (
    r(6,23,20,6,2,fill=PALE) + p('M16 23 V13') + c(16,10,4,fill=PALE)
    + accent('M3 11 H9 M6 8 3 11 6 14 M23 11 H29 M26 8 29 11 26 14')
    + p('M11 26 H21'))
GLYPHS['olp-hand-guiding'] = (
    p('M4 28 V21 L9 18 V9 Q9 6 12 7 V16 M12 16 V12 Q12 9 15 11 V16 M15 16 V12 Q15 10 18 12 V17 M18 17 V14 Q18 12 21 14 V23 L17 28Z',fill=PALE)
    + p('M24 4 27 10 23 16') + c(24,4,2,fill=PALE)
    + accent('M23 23 H29 M26 20 29 23 26 26'))
GLYPHS['olp-program-wait'] = (
    r(4,3,24,26,2) + p('M10 8 H22 M10 24 H22 M11 8 C11 14 21 18 21 24 M21 8 C21 14 11 18 11 24')
    + accent('M13 21 16 18 19 21Z',fill=PALE))
GLYPHS['olp-program-thread'] = (
    p('M16 3 V8 M7 13 V8 H25 V13 M7 22 V28 M25 22 V28')
    + r(3,13,8,9,1,fill=PALE) + r(21,13,8,9,1,fill=PALE)
    + accent('M4 25 7 28 10 25 M22 25 25 28 28 25'))
GLYPHS['olp-program-event'] = (
    p('M4 7 H10 L8 14 H14 L6 24 8 16 H3Z',fill=PALE)
    + accent('M14 14 H20 M17 11 20 14 17 17') + r(21,7,8,19,1,fill=PALE)
    + p('M24 12 H26 M24 17 H26 M24 22 H26'))
GLYPHS['olp-script-instruction'] = (
    r(3,4,26,24,2) + p('M3 10 H29 M7 7 H8 M12 7 H13')
    + accent('M11 14 7 18 11 22 M21 14 25 18 21 22 M18 13 14 24'))
GLYPHS['olp-operator-message'] = (
    p('M4 5 H28 V21 H15 L8 28 V21 H4Z',fill=PALE)
    + accent('M9 11 H23 M9 16 H19') + c(25,27,2,fill=TEAL))
GLYPHS['olp-force-control'] = (
    r(3,24,26,5,1,fill=PALE) + p('M11 4 H21 V9 H18 V19 H14 V9 H11Z')
    + accent('M16 11 V22 M12 18 16 22 20 18 M25 21 V8 Q25 3 29 3')
    + p('M5 22 V10 M2 13 5 10 8 13'))
GLYPHS['olp-remote-tcp'] = (
    p('M3 29 H16 M8 29 V22 L4 15 11 9 16 14') + nodes([(8,22),(4,15),(11,9)])
    + r(16,12,8,9,1,fill=PALE) + p('M25 3 H30 M28 3 V10 L24 14')
    + accent('M23 8 V17 M19 12 H28') + c(23,12,1.5,fill=TEAL))
GLYPHS['olp-point-follow'] = (
    p('M5 22 V8 H16 V22 M16 8 H27 V22',stroke_dasharray='2 3')
    + nodes([(5,27),(16,27),(27,27)])
    + accent('M5 13 V22 M2 19 5 22 8 19 M16 13 V22 M13 19 16 22 19 19 M27 13 V22 M24 19 27 22 30 19'))
GLYPHS['olp-safety-zone'] = (
    p('M3 10 16 4 29 10 V25 L16 29 3 25Z',stroke_dasharray='3 3')
    + fill('M3 10 8 8 V26 L3 25Z') + p('M12 24 V17 L20 12 25 17')
    + nodes([(12,17),(20,12)]) + accent('M16 29 V20 M16 20 29 14'))
GLYPHS['olp-io-mapping'] = (
    r(3,3,5,26,1,fill=PALE) + r(24,3,5,26,1,fill=PALE)
    + p('M8 8 H15 V24 H24 M8 24 H12 V8 H24')
    + accent('M8 16 H24 M20 13 24 16 20 19'))
GLYPHS['olp-signal-analyzer'] = (
    p('M4 3 V29 H29 M7 17 H29',stroke_dasharray='2 3')
    + accent('M7 13 H12 V6 H21 V13 H28 M7 26 C12 26 13 18 18 20 S24 28 28 21')
    + p('M17 3 V29'))
GLYPHS['olp-tcp-trace'] = (
    accent('M3 26 C13 25 5 12 15 13 S24 19 27 13',stroke_dasharray='2 3')
    + p('M20 3 H29 V7 H26 V11 H23 V7 H20Z',fill=PALE)
    + c(24.5,14,2,fill=TEAL))
GLYPHS['olp-swept-volume'] = (
    fill('M3 27 V13 Q4 3 15 3 Q27 4 29 16 V27Z')
    + p('M9 27 6 14 15 7',stroke_dasharray='2 3')
    + p('M9 27 21 21 25 10') + nodes([(9,27),(21,21),(25,10)])
    + accent('M5 29 H28'))
GLYPHS['olp-program-step'] = (
    p('M4 6 H16 M4 16 H16 M4 26 H16')
    + accent('M20 6 H25 V16 H20 M23 13 20 16 23 19')
    + p('M28 12 V20'))
GLYPHS['olp-program-breakpoint'] = (
    p('M13 6 H28 M13 16 H28 M13 26 H28')
    + c(6,16,4,fill=PALE,stroke=TEAL) + p('M6 12 V20',stroke=TEAL))
GLYPHS['olp-task-synchronization'] = (
    p('M4 16 H28',stroke_width=3) + r(6,3,6,6,1,fill=PALE) + r(20,3,6,6,1,fill=PALE)
    + accent('M9 9 V29 M5 25 9 29 13 25 M23 9 V29 M19 25 23 29 27 25'))
GLYPHS['olp-tool-contact'] = (
    p('M4 25 H28 M7 25 V29 M25 25 V29') + r(9,3,8,6,1,fill=PALE)
    + p('M13 9 V22 M10 18 13 22 16 18')
    + accent('M23 5 V20 M20 17 23 20 26 17 M5 18 8 21 M18 25 21 22')
    + c(13,25,2,fill=TEAL))
GLYPHS['olp-weld-weave'] = (
    p('M16 12 V30',stroke_dasharray='2 3')
    + accent('M16 12 7 16 25 21 7 26 16 29')
    + p('M18 3 H27 V8 L21 13 17 9 22 5 H18Z',fill=PALE))

ROBOTICS = {}
ROBOTICS_REFERENCES = {}
ROBOTICS_TREE = {}
ROBOTICS_NAMES = {}
ROBOTICS_REUSE = {}

def references(data):
    result = []
    for ref in data.pop('references'):
        ref = dict(ref)
        key = ref.pop('id')
        if key in ROBOTICS_REFERENCES and ROBOTICS_REFERENCES[key] != ref:
            raise ValueError('Conflicting robotics reference: ' + key)
        ROBOTICS_REFERENCES[key] = ref
        result.append(key)
    return result

def tree_metadata(id, data):
    node = data.pop('modelTree', None)
    if node:
        ROBOTICS_TREE[id] = {'objectType': node['objectType']}
        ROBOTICS_NAMES[id] = (node['name'], node['nameJa'])

def _load():
    records = json.loads(Path(__file__).with_name('robotics_commands.json').read_text())
    expected = {i['id'] for i in records}
    if len(expected) != len(records) or expected != set(GLYPHS):
        raise ValueError('Robotics review/drawing mismatch')
    for raw in records:
        data = dict(raw)
        id = data.pop('id')
        domain = data.pop('domain')
        data['sources'] = references(data)
        tree_metadata(id, data)
        data.pop('reviewNote')
        data['id'] = id.split('-', 1)[1]
        data['body'] = GLYPHS[id]
        data.setdefault('role', 'command')
        data['tags'] = list(dict.fromkeys(data['tags'] + [data['name'].lower(), data['nameJa'], 'robotics', 'ロボティクス']))
        ROBOTICS.setdefault(domain, []).append(data)
    for raw in json.loads(Path(__file__).with_name('robotics_reuse.json').read_text()):
        data = dict(raw)
        id = data.pop('id')
        if id in ROBOTICS_REUSE:
            raise ValueError('Duplicate robotics reuse ID: ' + id)
        data['sources'] = references(data)
        tree_metadata(id, data)
        data.pop('reviewNote')
        ROBOTICS_REUSE[id] = data

_load()

def apply_robotics_reuse(item):
    """Reuse geometry and expand reviewed vocabulary, categories or node uses."""
    data = ROBOTICS_REUSE.get(item['id'], {})
    for key in ['aliases', 'nodeAliases', 'tags', 'sources', 'sharedCategories']:
        if key in data:
            item[key] = list(dict.fromkeys(item.get(key, []) + data[key]))
    for key in ['description', 'descriptionJa']:
        if key in data:
            item[key] = data[key]
