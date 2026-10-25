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

    def test_standalone_theme_variants_and_original_byte_preservation(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from themes import THEMES, PAINT_ROLES, themed_body
        self.assertEqual(M['themes'],THEMES)
        self.assertEqual(M['defaultTheme'],'light')
        baseline=json.loads((ROOT/'src/theme_baseline_hashes.json').read_text())
        self.assertEqual(baseline['commit'],'08d22603e7b21b47da35f67025ba36a6572c3c95')
        self.assertEqual(len(baseline['icons']),419)
        self.assertTrue(set(baseline['icons']) <= {i['id'] for i in M['icons']})
        self.assertEqual({p.stem for p in (ROOT/'icons-dark').glob('*.svg')},{i['id'] for i in M['icons']})
        cutouts=0
        for item in M['icons']:
            with self.subTest(icon=item['id']):
                if item['id'] in baseline['icons']:
                    self.assertEqual(item['sha256'],baseline['icons'][item['id']])
                self.assertEqual(set(item['variants']),{'light','dark'})
                self.assertEqual(item['variants']['light'],{'file':item['file'],'sha256':item['sha256']})
                variant=item['variants']['dark']
                self.assertEqual(variant['file'],'icons-dark/'+item['id']+'.svg')
                data=(ROOT/variant['file']).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(),variant['sha256'])
                self.assertEqual(variant['body'],themed_body(item['body'],'dark'))
                self.assertEqual(themed_body(item['body'],'light'),item['body'])
                self.assertNotRegex(data.decode(),r'(?i)<!doctype|<!entity|javascript:|data:|https?://(?!www.w3.org/2000/svg)|currentColor|<style|<script')
                light=ET.fromstring((ROOT/item['file']).read_bytes());dark=ET.fromstring(data)
                self.assertEqual(geometry_signature(light),geometry_signature(dark))
                self.assertEqual(dark.find(NS+'title').text,item['name'])
                ids=[e.get('id') for e in dark.iter() if e.get('id')]
                self.assertEqual(len(ids),len(set(ids)))
                for before,after in zip(light.iter(),dark.iter(),strict=True):
                    self.assertEqual(before.tag,after.tag)
                    self.assertEqual(set(before.attrib),set(after.attrib))
                    self.assertIn(after.tag.removeprefix(NS),ALLOWED)
                    for key,value in after.attrib.items():
                        self.assertFalse(key.lower().startswith('on'))
                        self.assertNotIn('href',key.lower())
                        for ref in re.findall(r'url\(#([^)]*)\)',value):self.assertIn(ref,ids)
                        self.assertNotRegex(value,r'(?i)\b(?:nan|infinity)\b')
                        original=before.get(key)
                        if key in {'fill','stroke'} and original!='none':
                            self.assertEqual(value,THEMES['dark']['palette'][PAINT_ROLES[(key,original)]])
                        else:self.assertEqual(value,original)
                    if before.get('fill')=='white':
                        if item['id'] in baseline['icons']:cutouts+=1
                        self.assertEqual(after.get('fill'),'#192c3c')
                self.assertEqual(dark.get('stroke'),THEMES['dark']['palette']['ink'])
        self.assertEqual(cutouts,184)
        with self.assertRaises(ValueError):themed_body('<path fill="#123456"/>','dark')

    def test_gui_additions_are_exactly_the_reviewed_new_set(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from gui_features import ITEMS as features
        from gui_sketch import ITEMS as sketch
        from gui_surface import ITEMS as surface
        items=features+sketch+surface
        expected={'cad-'+i['id'] for i in items}
        baseline=json.loads((ROOT/'src/theme_baseline_hashes.json').read_text())['icons']
        current={i['id']:i for i in M['icons']}
        reviewed=set('''boundary-fill emboss pattern-path mounting-boss lip-groove snap-fit
            configuration-table history-rollback curvature-comb curvature-map continuity-analysis
            isocurve-analysis minimum-radius-analysis compare-bodies sketch-ellipse sketch-polygon
            sketch-slot sketch-text sketch-construction-line constraint-collinear constraint-curvature
            sketch-auto-constrain replace-face delete-face split-face surface-extend surface-untrim
            surface-unstitch surface-ruled surface-reverse-normal'''.split())
        self.assertEqual(expected,{'cad-'+id for id in reviewed})
        self.assertEqual(len(items),30)
        self.assertEqual(len(expected),len(items))
        self.assertTrue(expected <= set(current)-set(baseline))
        self.assertFalse(expected & set(baseline))
        for record in items:
            output=current['cad-'+record['id']]
            self.assertEqual(output['body'],record['body'])
            self.assertEqual(output['usages'],['command'])
            self.assertIn('solidcraft-commands',output['sources'])
            self.assertTrue(output['aliases'])
            self.assertTrue(output['descriptionJa'])

    def test_systematic_coverage_set_and_delivered449_preservation(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from coverage import COVERAGE
        from binding_additions import BINDING_ADDITIONS
        from toolbar_additions import TOOLBAR_ADDITIONS
        baseline=json.loads((ROOT/'src/gui_expansion_baseline.json').read_text())['icons']
        self.assertEqual(len(baseline),449)
        current={i['id']:i for i in M['icons']}
        additions={domain.lower()+'-'+i['id'] for domain,items in COVERAGE.items() for i in items}
        followup={domain.lower()+'-'+i['id'] for domain,items in BINDING_ADDITIONS.items() for i in items}
        toolbar={domain.lower()+'-'+i['id'] for domain,items in TOOLBAR_ADDITIONS.items() for i in items}
        from oct25_additions import REQUIREMENTS
        requested={r['id'] for r in REQUIREMENTS}
        self.assertEqual(set(current)-set(baseline),additions|followup|toolbar|requested)
        self.assertFalse(additions & set(baseline))
        for id,record in baseline.items():
            item=current[id]
            digest=hashlib.sha256(json.dumps(item,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
            self.assertEqual(digest,record['record_sha256'],id)
            for theme in ('light','dark'):
                self.assertEqual(item['variants'][theme]['sha256'],record[theme],id)
        decisions=json.loads((ROOT/'src/coverage_decisions.json').read_text())
        covered_groups=[g for i in decisions for g in i['audit_groups']]
        audited=json.loads((ROOT/'src/coverage_audit_groups.json').read_text())
        self.assertEqual(set(covered_groups),set(audited))
        self.assertEqual(len(covered_groups),len(set(covered_groups)))
        for row in decisions:
            self.assertTrue(row['reason'])
            self.assertIn(row['decision'],{'new-glyph','reuse','uncertain','not-applicable'})
            if row['decision'] in {'new-glyph','reuse'}:
                self.assertIn(row['icon_id'],current)
            if row['decision']=='new-glyph':
                self.assertIn(row['icon_id'],additions)
        self.assertEqual({i['icon_id'] for i in decisions if i['decision']=='new-glyph'},additions)

    def test_reviewed_application_commands_and_alias_reuse(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from application import APPLICATION, GLYPHS, APPLICATION_REUSE
        by_id={i['id']:i for i in M['icons']}
        reviewed=json.loads((ROOT/'src/application_commands.json').read_text())
        self.assertEqual(set(GLYPHS),{i['id'] for i in reviewed})
        self.assertEqual(len(GLYPHS),sum(len(v) for v in APPLICATION.values()))
        self.assertTrue(set(GLYPHS) <= set(by_id))
        self.assertTrue(set(APPLICATION_REUSE) <= set(by_id))
        for i in reviewed:
            output=by_id[i['id']]
            self.assertEqual(output['role'],'command')
            self.assertIn(i['sourceId'],output['sources'])
            self.assertEqual(output['body'],GLYPHS[i['id']])
        for i in M['icons']:
            self.assertEqual(len(i.get('aliases',[])),len(set(i.get('aliases',[]))))
            for alias in i.get('aliases',[]):self.assertTrue(isinstance(alias,str) and alias.strip())
        for id in ['cad-mesh-merge-vertices','cad-mesh-smooth']:
            self.assertIn('CAE',by_id[id]['categories'])
            self.assertTrue(by_id[id]['aliases'])
            self.assertEqual(len(by_id[id]['sources']),2)
        self.assertIn('CAD',by_id['cae-orient-faces']['categories'])
        self.assertIn('ICP',by_id['cmm-best-fit-alignment']['aliases'])
        self.assertIn('raster finishing',by_id['cam-parallel-finishing']['aliases'])
        self.assertIn('shut-off patch',by_id['cad-surface-patch']['aliases'])
        self.assertFalse({'cae-merge-nodes','cae-smooth-mesh','cmm-filter-outliers','cmm-subsample-cloud','cmm-reconstruct-mesh','cad-mold-shutoff'} & set(by_id))
        for id in ['cad-sheet-metal-form-tool','cae-harmonic-response','cae-composite-layup','cae-rigid-connection']:
            self.assertEqual(by_id[id]['usages'],['command','model-tree'])

    def test_reviewed_studio_commands_and_reuse(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from studio import GLYPHS, STUDIO, STUDIO_REUSE, STUDIO_TREE, STUDIO_NAMES
        by_id={i['id']:i for i in M['icons']}
        reviewed=json.loads((ROOT/'src/studio_commands.json').read_text())
        reused=json.loads((ROOT/'src/studio_reuse.json').read_text())
        self.assertEqual(set(GLYPHS),{i['id'] for i in reviewed})
        self.assertEqual(len(GLYPHS),sum(len(v) for v in STUDIO.values()))
        self.assertTrue(set(STUDIO_REUSE) <= set(by_id))
        self.assertEqual(set(STUDIO_TREE),set(STUDIO_NAMES))
        self.assertEqual(set(STUDIO_TREE),{'cad-face-offset','cad-helix','cad-defeature'})
        for i in reviewed+reused:
            out=by_id[i['id']]
            self.assertTrue(i['reviewNote'],i['id'])
            for ref in i['references']:
                self.assertIn(ref['id'],out['sources'])
                # Pin implementation evidence; a moving branch cannot silently
                # broaden the claim about commands that existed at review time.
                self.assertRegex(ref['url'],r'/blob/[0-9a-f]{40}/')
            for field in ['aliases','nodeAliases']:
                for alias in i.get(field,[]):self.assertIn(alias,out.get(field,[]))
            if i['id'] in GLYPHS:
                self.assertEqual(out['body'],GLYPHS[i['id']])
                self.assertEqual(out['role'],'command')
        for id in ['cad-suppress-feature','cad-recognize-features','common-screenshot','cad-photoreal-render']:
            self.assertEqual(by_id[id]['usages'],['command'])
        self.assertFalse({'cad-recognized-thread','cad-suppressed-part','cad-helix-small','cad-mesh2brep-via-voxel'} & set(by_id))

    def test_reviewed_pdxadv_meanings_and_preserved_baseline(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from pdxadv import GLYPHS, PDXADV, PDXADV_REUSE
        by_id={i['id']:i for i in M['icons']}
        reviewed=json.loads((ROOT/'src/pdxadv_commands.json').read_text())
        reused=json.loads((ROOT/'src/pdxadv_reuse.json').read_text())
        self.assertEqual(set(GLYPHS),{i['id'] for i in reviewed})
        self.assertEqual(len(GLYPHS),sum(len(v) for v in PDXADV.values()))
        self.assertEqual(len(GLYPHS),9)
        self.assertEqual(set(PDXADV_REUSE),{'cae-deformation-result'})
        self.assertFalse(set(PDXADV_REUSE)&set(GLYPHS))
        for i in reviewed+reused:
            out=by_id[i['id']]
            self.assertTrue(i['reviewNote'])
            for ref in i['references']:
                self.assertIn(ref['id'],out['sources'])
                self.assertIn('/blob/40cc394fd59e18b76f48efa1161a25d460bafc6d/',ref['url'])
            for alias in i.get('aliases',[]):self.assertIn(alias,out.get('aliases',[]))
            if i['id'] in GLYPHS:
                self.assertEqual(out['body'],GLYPHS[i['id']])
                self.assertEqual(out['usages'],['command'])
                self.assertEqual(out['category'],'CAE')
        self.assertIn('isotropic linear shrinkage',by_id['cae-sensitivity-result']['description'])
        self.assertIn('remeshing and reanalysis',by_id['cae-thickness-optimization']['description'])
        self.assertIn('fixed back plane',by_id['cae-local-wall-offset']['description'])
        self.assertIn('uncalibrated',by_id['cae-sink-tendency']['description'])
        self.assertIn('in memory',by_id['cae-set-baseline']['description'])
        self.assertFalse({'cae-warpage-result','cae-raw-sensitivity','cae-normalized-sensitivity','cae-sensitivity-density','cae-html-report','cae-pptx-report'}&set(by_id))
        baseline=json.loads((ROOT/'src/pdxadv_baseline_hashes.json').read_text())
        self.assertEqual(baseline['commit'],'490d20684866e39c7075485bf2dc95abb95dd341')
        self.assertEqual(len(baseline['icons']),410)
        self.assertTrue(set(GLYPHS) <= set(by_id)-set(baseline['icons']))
        for id,sha in baseline['icons'].items():self.assertEqual(by_id[id]['sha256'],sha,id)

    def test_reviewed_occlusion_and_projected_mesh(self):
        by_id={i['id']:i for i in M['icons']}
        reviews=json.loads((ROOT/'src/quality_review.json').read_text())
        self.assertEqual(len(reviews),11)
        self.assertEqual(len({i['id'] for i in reviews}),len(reviews))
        for review in reviews:
            self.assertIn(review['id'],by_id)
            self.assertTrue(review['reason'])
            self.assertNotEqual(review['beforeBody'],by_id[review['id']]['body'])
            ET.fromstring('<svg>'+review['beforeBody']+'</svg>')
        cutter=ET.fromstring((ROOT/by_id['cam-swarf-milling']['file']).read_text())
        flutes=[e for e in cutter.iter(NS+'rect') if e.get('x')=='12' and e.get('y')=='10']
        self.assertEqual(len(flutes),1)
        self.assertEqual(flutes[0].get('fill'),'white')
        # Grid endpoints meet the projected cube edges rather than running
        # through the top face or pointing into an unrelated face plane.
        mesh=by_id['cae-hexahedral-mesh']['body']
        self.assertIn('M10.5 7.5 19.5 12.5 M19.5 7.5 10.5 12.5',mesh)
        self.assertIn('M6 17.5 15 22.5 24 17.5',mesh)
        self.assertNotIn('M11 8 V27',mesh)

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

    def test_reviewed_robotics_commands_and_reuse(self):
        import sys
        sys.path.insert(0,str(ROOT/'src'))
        from robotics import GLYPHS, ROBOTICS, ROBOTICS_REUSE, ROBOTICS_TREE, ROBOTICS_NAMES
        by_id={i['id']:i for i in M['icons']}
        reviewed=json.loads((ROOT/'src/robotics_commands.json').read_text())
        reused=json.loads((ROOT/'src/robotics_reuse.json').read_text())
        self.assertEqual(set(GLYPHS),{i['id'] for i in reviewed})
        self.assertEqual(len(GLYPHS),sum(len(v) for v in ROBOTICS.values()))
        self.assertTrue(set(ROBOTICS_REUSE) <= set(by_id))
        self.assertFalse(set(ROBOTICS_REUSE) & set(GLYPHS))
        self.assertEqual(set(ROBOTICS_TREE),set(ROBOTICS_NAMES))
        for i in reviewed+reused:
            self.assertTrue(i['reviewNote'],i['id'])
            self.assertTrue(i['references'],i['id'])
            out=by_id[i['id']]
            for ref in i['references']:
                self.assertIn(ref['id'],out['sources'])
                self.assertTrue(ref['url'].startswith('https://'))
            for alias in i.get('aliases',[]):self.assertIn(alias,out['aliases'])
            for category in i.get('sharedCategories',[]):self.assertIn(category,out['categories'])
            if i.get('modelTree'):
                self.assertIn('model-tree',out['usages'])
                self.assertEqual(out['nodeName'],i['modelTree']['name'])
                self.assertEqual(out['nodeNameJa'],i['modelTree']['nameJa'])
            if i['id'] in GLYPHS:
                self.assertEqual(out['body'],GLYPHS[i['id']])
                self.assertEqual(out['role'],i.get('role','command'))
        # Robot morphology and UI state remain contextual data, not new glyphs.
        self.assertFalse({'olp-hidden-robot','olp-selected-robot','olp-error-robot','olp-scara-arm','olp-six-axis-arm','olp-robot-revolute-joint'} & set(by_id))

if __name__ == '__main__':
    unittest.main(verbosity=2)
