"""Validate the source-scoped command binding contract, not a deployed consumer UI."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class BindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT/'manifest.json').read_text())
        cls.icons = {i['id']: i for i in cls.catalog['icons']}
        cls.policy = json.loads((ROOT/'command-bindings.json').read_text())
        cls.baseline = json.loads((ROOT/'src/published693_baseline.json').read_text())['icons']

    def test_all_180_rows_once_and_source_identity(self):
        rows = self.policy['bindings']
        self.assertEqual(len(rows), 180)
        self.assertEqual({r['uncertain_index'] for r in rows}, set(range(180)))
        frozen = json.loads((ROOT/'src/binding_audit_rows.json').read_text())
        for r in rows:
            original = frozen[r['uncertain_index']]
            for key in ('product','command'):
                self.assertEqual(r[key], original[key])
            self.assertEqual(r['original_audit_status'], 'uncertain')
            self.assertFalse(r['consumer_ui_verified'])
            self.assertTrue(r['reason'])
            self.assertTrue(r['source_urls'])
            self.assertTrue(all(u.startswith('https://') for u in r['source_urls']))
            self.assertIn(r['outcome'], {'direct','conditional-reuse','new-art','unresolved','not-discrete'})
            if r['outcome'] == 'unresolved':
                self.assertTrue(r['remaining_unknown'])
            if r['outcome'] in {'conditional-reuse','new-art'}:
                self.assertTrue(r['required_ui_conditions'])
            for binding in r['bindings']:
                self.assertIn(binding['icon_id'], self.icons)
                for key in ('condition','label','semantic_scope'):
                    self.assertTrue(isinstance(binding[key], str) and binding[key].strip())

    def test_published_693_records_and_svg_bytes_unchanged(self):
        self.assertEqual(len(self.baseline), 693)
        for id, baseline in self.baseline.items():
            icon = self.icons[id]
            digest = hashlib.sha256(json.dumps(icon, sort_keys=True, separators=(',',':'), ensure_ascii=False).encode()).hexdigest()
            self.assertEqual(digest, baseline['record_sha256'], id)
            for theme in ('light','dark'):
                path = ROOT/icon['variants'][theme]['file']
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), baseline[theme], (id,theme))

    def test_new_art_has_explicit_row_and_source_trace(self):
        trace = json.loads((ROOT/'src/binding_art_trace.json').read_text())
        new_ids = set(self.icons)-set(self.baseline)
        self.assertEqual(new_ids, set(trace))
        bound_new = set()
        for row in self.policy['bindings']:
            for binding in row['bindings']:
                if binding['icon_id'] in new_ids:
                    bound_new.add(binding['icon_id'])
        self.assertEqual(new_ids, bound_new)
        for id, record in trace.items():
            self.assertTrue(record['sources'], id)
            for source in record['sources']:
                self.assertIn(source, self.catalog['sourceReferences'])

if __name__ == '__main__':
    unittest.main()
