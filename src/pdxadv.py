"""Original symbols for source-verified pdxadv analysis workflows.

All result variants are alternate views of one meaning, never extra SVGs.
"""
import json
from pathlib import Path
from core import p, r, c, accent, fill, PALE, TEAL

GLYPHS = {}

# A local derivative: tangent at one point on the response curve. This is
# sensitivity to isotropic linear shrinkage, not a wall-thickness derivative.
GLYPHS['cae-sensitivity-result'] = (p('M4 4 V28 H29')
    + p('M7 24 C13 24 14 20 17 15 S24 7 28 7')
    + accent('M10 26 24 4') + c(17,15,2.3,fill=PALE,stroke=TEAL))

# Two wall-thickness candidates and an iteration loop. There is no material
# removal/topology metaphor and no claim of a guaranteed global optimum.
GLYPHS['cae-thickness-optimization'] = (r(6,17,20,10,1,fill=PALE)
    + p('M6 12 H26',stroke_dasharray='2 3')
    + accent('M6 9 A11 7 0 0 1 26 9 M22 7 26 9 28 5')
    + p('M11 21 H21'))

# Compactly supported local deformation with an unchanged back plane. The
# raised surface is smooth; the command is not generic mesh smoothing.
GLYPHS['cae-local-wall-offset'] = (fill('M3 19 H7 C11 19 11 13 16 13 S21 19 25 19 H29 V26 H3Z')
    + p('M7 19 H25',stroke_dasharray='2 3')
    + accent('M16 11 V3 M13 6 16 3 19 6')
    + p('M3 29 6 26 M10 29 13 26 M18 29 21 26 M26 29 29 26'))

# A varying wall section with one through-thickness span. It represents the
# distributed thickness field, not a generic two-point measurement command.
GLYPHS['cae-thickness-result'] = (fill('M4 12 28 5 V27 H4Z')
    + p('M11 10 V27 M18 8 V27',stroke_dasharray='2 3')
    + accent('M24 10 V23 M21 13 24 10 27 13 M21 20 24 23 27 20'))

# Reference envelope and contracted field with opposing inward indications.
# No scale handle, volume symbol or editable transform origin is used.
GLYPHS['cae-shrinkage-result'] = (r(3,5,26,23,2,stroke_dasharray='2 3')
    + r(10,12,12,9,1,fill=PALE)
    + accent('M4 8 10 12 M6 12 H10 V8 M28 25 22 21 M22 25 V21 H26'))

# Surface hotspot on a wall: an uncalibrated tendency, without a depth arrow,
# numeric defect limit, measured dent or pass/fail mark.
GLYPHS['cae-sink-tendency'] = (fill('M3 12 16 5 29 12 16 19Z')
    + p('M3 12 V21 L16 28 29 21 V12 M16 19 V28')
    + p('M9 12 C9 7 23 7 23 12 S9 17 9 12',stroke=TEAL)
    + c(16,12,1.6,fill=TEAL,stroke='none'))

# Two result views plus a shared comparison span; not measured/CAD deviation.
GLYPHS['cae-compare-results'] = (r(3,3,10,19,1,fill=PALE)
    + r(19,3,10,19,1,fill=PALE)
    + p('M5 11 Q8 6 11 11 M21 14 Q24 9 27 14',stroke=TEAL)
    + accent('M6 27 H26 M9 24 6 27 9 30 M23 24 26 27 23 30'))

# Pin a copy of a result in memory for comparisons. The backing sheet is not
# a disk/save symbol and this does not imply persistent file storage.
GLYPHS['cae-set-baseline'] = (r(4,6,18,23,2)
    + p('M8 19 Q12 14 17 19 M8 24 H16',stroke=TEAL)
    + fill('M18 3 H28 L26 8 V12 L29 15 H17 L20 12 V8Z')
    + accent('M23 15 V23'))

# An analysis field in a report page, rather than the existing inspection
# report's measurement bars. HTML and PPTX are formats of this one operation.
GLYPHS['cae-analysis-report'] = (p('M6 3 H21 L27 9 V29 H6Z M21 3 V9 H27')
    + fill('M10 13 H23 V22 H10Z')
    + accent('M10 16 Q16 12 23 17 M10 20 Q16 16 23 21')
    + p('M10 26 H20'))

PDXADV = {}
PDXADV_REFERENCES = {}
PDXADV_REUSE = {}

def references(data):
    ids = []
    for raw in data.pop('references'):
        ref = dict(raw)
        key = ref.pop('id')
        if key in PDXADV_REFERENCES and PDXADV_REFERENCES[key] != ref:
            raise ValueError('Conflicting pdxadv source reference: ' + key)
        PDXADV_REFERENCES[key] = ref
        ids.append(key)
    return ids

def _load():
    records = json.loads(Path(__file__).with_name('pdxadv_commands.json').read_text())
    if len({i['id'] for i in records}) != len(records) or {i['id'] for i in records} != set(GLYPHS):
        raise ValueError('pdxadv review/drawing mismatch')
    for raw in records:
        data = dict(raw)
        id = data.pop('id')
        domain = data.pop('domain')
        data['sources'] = references(data)
        data.pop('reviewNote')
        data['id'] = id.split('-', 1)[1]
        data['body'] = GLYPHS[id]
        data.setdefault('role', 'command')
        data['tags'] = list(dict.fromkeys(data['tags'] + [data['name'].lower(), data['nameJa'], 'pdxadv']))
        PDXADV.setdefault(domain, []).append(data)
    for raw in json.loads(Path(__file__).with_name('pdxadv_reuse.json').read_text()):
        data = dict(raw)
        id = data.pop('id')
        if id in PDXADV_REUSE or id in GLYPHS:
            raise ValueError('Duplicate pdxadv reuse ID: ' + id)
        data['sources'] = references(data)
        data.pop('reviewNote')
        PDXADV_REUSE[id] = data

_load()

def apply_pdxadv_reuse(item):
    """Add vocabulary to existing geometry without changing SVG bytes."""
    data = PDXADV_REUSE.get(item['id'], {})
    for key in ['aliases', 'tags', 'sources']:
        if key in data:
            item[key] = list(dict.fromkeys(item.get(key, []) + data[key]))
