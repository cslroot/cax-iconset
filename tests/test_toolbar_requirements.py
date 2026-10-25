"""User-defined toolbar acceptance, separate from the frozen source audit."""
import hashlib,json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class ToolbarRequirements(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.icons={i['id']:i for i in json.loads((R/'manifest.json').read_text())['icons']}
  cls.baseline=json.loads((R/'src/published714_baseline.json').read_text())['icons']
  cls.requirements=json.loads((R/'toolbar-bindings.json').read_text())
 def test_published714_immutable(self):
  self.assertEqual(len(self.baseline),714)
  for id,b in self.baseline.items():
   i=self.icons[id]
   self.assertEqual(hashlib.sha256(json.dumps(i,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest(),b['record_sha256'],id)
   for t in ('light','dark'):
    self.assertEqual(hashlib.sha256((R/i['variants'][t]['file']).read_bytes()).hexdigest(),b[t],(id,t))
 def test_all18_groups_and_exact_buttons(self):
  rows=self.requirements['bindings']
  self.assertEqual({r['group'] for r in rows},set(range(1,19)))
  keys=[r['semantic'] for r in rows];self.assertEqual(len(keys),len(set(keys)))
  for r in rows:
   self.assertIn(r['icon_id'],self.icons)
   self.assertIn(r['status'],('new-art','existing-exact'))
   self.assertTrue(r['reason']);self.assertFalse(r['consumer_ui_integrated'])
   self.assertIn('consumer_command_values',r)
   self.assertNotIn('consumer_commands',r)
   if r['group'] in (1,2): self.assertEqual(len(r['consumer_command_values']),1)
  for family,n in [('display-mode',7),('standard-view',6),('selection-filter',2),('navigation-mode',2),('gadget-toggle',2),('visual-effect',3)]:
   selected=[r for r in rows if r.get('distinct_family')==family]
   self.assertEqual(len(selected),n,family)
   self.assertEqual(len({r['icon_id'] for r in selected}),n,family)
   self.assertEqual(len({self.icons[r['icon_id']]['body'] for r in selected}),n,family)
 def test_new_art_fully_accounted_for(self):
  # This historical acceptance unit covers 714 -> 758, not later additions.
  published758=json.loads((R/'src/published758_baseline.json').read_text())['icons']
  added=set(published758)-set(self.baseline)
  mapped={r['icon_id'] for r in self.requirements['bindings'] if r['status']=='new-art'}
  self.assertEqual(added,mapped)
  self.assertTrue(self.requirements['source_snapshot'])
  self.assertFalse(self.requirements['claims_all_product_commands'])
