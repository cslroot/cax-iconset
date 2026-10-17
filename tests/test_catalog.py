#!/usr/bin/env python3
"""Dependency-free XML, metadata, integrity and normalized-geometry checks."""
import collections
import hashlib
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
M = json.loads((ROOT / 'manifest.json').read_text())
NS = '{http://www.w3.org/2000/svg}'
ALLOWED = {'svg', 'title', 'path', 'rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'g', 'defs', 'clipPath'}

def geometry_signature(root):
    # Ignore labels, paint colors, and local ID spellings, preserving geometry.
    ids = {e.attrib['id']: f'ref{n}' for n, e in enumerate(root.iter()) if 'id' in e.attrib}
    def walk(e):
        tag = e.tag.removeprefix(NS)
        if tag == 'title':
            return None
        attrs = []
        for key, value in sorted(e.attrib.items()):
            if key in {'id', 'aria-labelledby', 'role'}:
                continue
            value = re.sub(r'url\(#([^)]*)\)', lambda m: f'url(#{ids[m[1]]})', value)
            if key in {'fill', 'stroke'} and value != 'none':
                value = 'paint'
            attrs.append((key, value))
        return [tag, attrs, [v for child in e if (v := walk(child)) is not None]]
    return json.dumps(walk(root), separators=(',', ':'))

class CatalogTests(unittest.TestCase):
    def test_counts_and_metadata(self):
        self.assertGreater(M['count'], 0)
        self.assertEqual(M['count'], len(M['icons']))
        self.assertEqual(M['counts'], dict(collections.Counter(i['role'] for i in M['icons'])))
        self.assertEqual(M['categories'], dict(collections.Counter(i['category'] for i in M['icons'])))
        self.assertEqual(len({i['id'] for i in M['icons']}), M['count'])
        self.assertEqual({str(p.relative_to(ROOT)) for p in (ROOT/'icons').glob('*.svg')}, {i['file'] for i in M['icons']})
        self.assertEqual(set(M['categories']), {'Common','CAD','CAM','CAE','CMM','OLP'})
        for i in M['icons']:
            for key in ['id', 'name', 'nameJa', 'family', 'body', 'tags', 'sources', 'description', 'descriptionJa', 'role']:
                self.assertTrue(i[key], (i['id'], key))
            self.assertRegex(i['id'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
            self.assertEqual(i['file'], 'icons/' + i['id'] + '.svg')
            self.assertEqual(i['categories'][0], i['category'])
            self.assertEqual(len(i['categories']),len(set(i['categories'])))
            self.assertTrue(set(i['categories']) <= set(M['categories']))
            self.assertNotIn('context', i)
            self.assertNotEqual(i.get('kind'), 'variant')
            self.assertIn(i['role'], {'command', 'tool', 'status', 'object'})
            self.assertTrue(set(i['sources']) <= set(M['sourceReferences']))
            self.assertTrue(any(re.search('[a-zA-Z]', t) for t in i['tags']), i['id'])
            self.assertTrue(any(re.search('[ぁ-んァ-ヶ一-龠]', t) for t in i['tags']), i['id'])
            self.assertNotIn('Original core symbol', i['description'])
        self.assertFalse((ROOT/'src/extended.py').exists())
        self.assertFalse((ROOT/'src/profiles.py').exists())
        common = [i for i in M['icons'] if i['category'] == 'Common']
        self.assertGreaterEqual(len(common), 60)
        required = 'new-file open-file recent-files close-file save save-as save-all import export print undo redo cut copy paste delete search filter settings help select show hide zoom-in zoom-out zoom-fit pan rotate-view'.split()
        ids = {i['id'] for i in common}
        for operation in required:
            self.assertIn('common-' + operation, ids)

    def test_usage_metadata_and_reuse(self):
        self.assertEqual(M['categoryMemberships'], dict(collections.Counter(c for i in M['icons'] for c in i['categories'])))
        self.assertEqual(M['usageCounts'], dict(collections.Counter(u for i in M['icons'] for u in i['usages'])))
        by_id={i['id']:i for i in M['icons']}
        for i in M['icons']:
            self.assertTrue(i['usages'],i['id'])
            self.assertEqual(len(i['usages']),len(set(i['usages'])))
            self.assertTrue(set(i['usages']) <= {'command','model-tree','tool','status'})
            if i['role']=='object':self.assertEqual(i['usages'],['model-tree'])
            else:self.assertIn(i['role'],i['usages'])
            if 'model-tree' in i['usages']:
                for field in ['nodeName','nodeNameJa','objectType']:self.assertTrue(i.get(field), (i['id'],field))
            else:self.assertNotIn('objectType',i)
        for id in ['cad-extrude','cae-material-assignment','cae-fixed-support','cam-post-process']:
            self.assertEqual(by_id[id]['usages'],['command','model-tree'])
        self.assertIn('CAD',by_id['cae-material-assignment']['categories'])
        self.assertIn('component instance',by_id['cad-part']['nodeAliases'])
        self.assertFalse({'cad-material','cad-component-instance','cam-nc-program'} & set(by_id))
        # Every explicit reuse key names one real entry; no orphan metadata.
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from usage import TREE, NAMES, SHARED
        self.assertTrue(set(TREE) <= set(by_id))
        self.assertTrue(set(NAMES) <= set(TREE))
        self.assertTrue(set(SHARED) <= set(by_id))

    def test_no_profile_cartesian_product(self):
        # Removing the old generator is an architectural guard; semantic review
        # remains necessary because exact geometry checks cannot establish meaning.
        self.assertFalse({'cad-extrusion-circle','cad-extrusion-semicircle','cad-section-circle','common-centroid-circle'} & {i['id'] for i in M['icons']})
        descriptions = [i['description'].strip().lower() for i in M['icons']]
        self.assertEqual(len(descriptions), len(set(descriptions)))

    def test_svg_safety_integrity_and_geometry_uniqueness(self):
        seen = {}
        for item in M['icons']:
            with self.subTest(icon=item['id']):
                data = (ROOT/item['file']).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), item['sha256'])
                self.assertNotRegex(data.decode(), r'(?i)<!doctype|<!entity|javascript:|data:|https?://(?!www.w3.org/2000/svg)')
                root = ET.fromstring(data)
                self.assertEqual(root.tag, NS+'svg')
                self.assertEqual(root.attrib['viewBox'], '0 0 32 32')
                self.assertEqual(root.attrib['stroke-linecap'], 'round')
                self.assertEqual(root.attrib['stroke-linejoin'], 'round')
                self.assertEqual(root.find(NS+'title').text, item['name'])
                ids = [e.attrib['id'] for e in root.iter() if 'id' in e.attrib]
                self.assertEqual(len(ids), len(set(ids)))
                for e in root.iter():
                    self.assertIn(e.tag.removeprefix(NS), ALLOWED)
                    for key, value in e.attrib.items():
                        self.assertFalse(key.lower().startswith('on'), key)
                        self.assertNotIn('href', key.lower())
                        for ref in re.findall(r'url\(#([^)]*)\)', value):
                            self.assertIn(ref, ids)
                        self.assertNotRegex(value, r'(?i)\b(?:nan|infinity)\b')
                signature = geometry_signature(root)
                self.assertNotIn(signature, seen, (item['id'], seen.get(signature)))
                seen[signature] = item['id']

    def test_bundle_and_document_links(self):
        bundle = (ROOT/'catalog.js').read_text()
        self.assertEqual(json.loads(bundle.removeprefix('window.CAX_CATALOG=').strip().removesuffix(';')), M)
        html = (ROOT/'index.html').read_text()
        ids = re.findall(r'\bid="([^"]+)"', html)
        self.assertEqual(len(ids), len(set(ids)))
        for target in re.findall(r'(?:src|href)="([^"]+)"', html):
            if not target.startswith(('https:', '#')):
                self.assertTrue((ROOT/target).is_file(), target)
        self.assertIn('Content-Security-Policy', html)
        self.assertIn('aria-label="Search icons', html)
        self.assertIn('aria-labelledby="detail-name"', html)

if __name__ == '__main__':
    unittest.main(verbosity=2)
