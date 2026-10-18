"""Source-verified CAX commands; new meanings, never UI-state variants."""
import json
from pathlib import Path
from core import p, r, c, accent, fill, PALE, TEAL

GLYPHS = {}

# The selected face moves; the neighboring faces still form a closed solid.
GLYPHS['cad-face-offset'] = (fill('M4 17 15 12 26 17 V26 L15 30 4 26Z')
    + p('M4 17 15 22 26 17 M15 22 V30')
    + p('M4 12 15 7 26 12 15 17Z',stroke=TEAL,fill=PALE)
    + accent('M15 7 V2 M12 5 15 2 18 5'))

# One unprofiled 3D wire. A thread is a separate solid feature.
GLYPHS['cad-helix'] = (p('M16 3 V29',stroke_dasharray='2 3')
    + accent('M7 27 C7 30 25 26 25 23 S7 19 7 16 S25 12 25 9 S7 5 7 8')
    + c(7,27,1.4,fill=PALE) + c(7,8,1.4,fill=PALE))

# Remove a local raised feature and heal the continuous supporting face.
GLYPHS['cad-defeature'] = (r(4,18,24,11,1,fill=PALE)
    + p('M11 17 V7 H21 V17',stroke_dasharray='2 3')
    + accent('M5 18 H27 M13 11 H19'))

# One DAG action, not hidden/suppressed copies of every feature symbol.
GLYPHS['cad-suppress-feature'] = (r(3,3,8,7,1,fill=PALE)
    + r(21,22,8,7,1,fill=PALE) + p('M7 10 V25 H21')
    + r(19,5,10,10,2,stroke_dasharray='2 3')
    + p('M11 6 H15 M24 15 V19',stroke_dasharray='2 3')
    + accent('M18 16 30 4'))

# A recognized pocket and round feature, framed by inspection corners.
GLYPHS['cad-recognize-features'] = (p('M3 10 V3 H10 M22 3 H29 V10 M29 22 V29 H22 M10 29 H3 V22',stroke=TEAL)
    + r(7,8,18,17,2,fill=PALE) + c(12,13,2.5)
    + p('M18 11 H22 V21 H13 V18'))

GLYPHS['common-screenshot'] = (p('M3 9 V3 H9 M23 3 H29 V9 M29 23 V29 H23 M9 29 H3 V23',stroke=TEAL)
    + fill('M7 11 H11 L13 8 H19 L21 11 H25 V24 H7Z')
    + c(16,17,4))

GLYPHS['cad-photoreal-render'] = (r(3,3,26,26,2)
    + c(14,18,7,fill=PALE) + p('M10 13 Q7 21 16 24',stroke=TEAL)
    + p('M7 26 H24')
    + accent('M24 6 V12 M21 9 H27'))

STUDIO = {}
STUDIO_REFERENCES = {}
STUDIO_TREE = {}
STUDIO_NAMES = {}
STUDIO_REUSE = {}

def references(data):
    ids = []
    for raw in data.pop('references'):
        ref = dict(raw)
        key = ref.pop('id')
        if key in STUDIO_REFERENCES and STUDIO_REFERENCES[key] != ref:
            raise ValueError('Conflicting CAX source reference: ' + key)
        STUDIO_REFERENCES[key] = ref
        ids.append(key)
    return ids

def _load():
    records = json.loads(Path(__file__).with_name('studio_commands.json').read_text())
    if len({i['id'] for i in records}) != len(records) or {i['id'] for i in records} != set(GLYPHS):
        raise ValueError('CAX review/drawing mismatch')
    for raw in records:
        data = dict(raw)
        id = data.pop('id')
        domain = data.pop('domain')
        data['sources'] = references(data)
        node = data.pop('modelTree', None)
        if node:
            STUDIO_TREE[id] = {'objectType': node['objectType']}
            STUDIO_NAMES[id] = (node['name'], node['nameJa'])
        data.pop('reviewNote')
        data['id'] = id.split('-', 1)[1]
        data['body'] = GLYPHS[id]
        data.setdefault('role', 'command')
        data['tags'] = list(dict.fromkeys(data['tags'] + [data['name'].lower(), data['nameJa'], 'cax-studio']))
        STUDIO.setdefault(domain, []).append(data)
    for raw in json.loads(Path(__file__).with_name('studio_reuse.json').read_text()):
        data = dict(raw)
        id = data.pop('id')
        if id in STUDIO_REUSE or id in GLYPHS:
            raise ValueError('Duplicate CAX reuse ID: ' + id)
        data['sources'] = references(data)
        data.pop('reviewNote')
        STUDIO_REUSE[id] = data

_load()

def apply_studio_reuse(item):
    """Enrich existing meanings instead of emitting CAX-specific copies."""
    data = STUDIO_REUSE.get(item['id'], {})
    for key in ['aliases', 'nodeAliases', 'tags', 'sources']:
        if key in data:
            item[key] = list(dict.fromkeys(item.get(key, []) + data[key]))

    for key in ['description', 'descriptionJa']:
        if key in data:
            item[key] = data[key]
