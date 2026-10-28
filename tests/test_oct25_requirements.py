import hashlib,json,unittest,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'src'))
from oct25_additions import REQUIREMENTS
# Icons added after the October 25 checkpoint.
LATER_ADDITIONS={'cad-primitive-cone','cad-solid-pipe'}
class October25Requirements(unittest.TestCase):
 def test_exact_42_requests(self):
  expected='''cad-rotate-selected-face cad-silhouette-edges cad-ground-shadow cad-shadow-maps cad-selection-filter-component cad-selection-filter-face cad-selection-filter-face-edge cad-face-reblend cad-copy-face-feature cad-sketch-fillet cad-sketch-chamfer cad-sketch-radius-dimension cad-sketch-clear cad-edit-feature cad-attach-reference cad-component-list cad-open-sheet-metal-sample common-reset common-background-color cad-surface-lit cad-markup-freehand cad-markup-circle cad-markup-rectangle cae-export-pptx-report common-tree-node-expanded cad-implicit-body cad-sdf-convert cad-csg-tree cad-lattice-gyroid cad-lattice-rod cae-mesh-settings cae-mesh-refine-region cae-boundary-layer common-timeline common-record common-loop common-playback-speed common-step-forward common-step-back cad-pmi-edit cad-pmi-associate cad-quad-remesh'''.split()
  self.assertEqual(len(expected),42)
  self.assertEqual({r['id'] for r in REQUIREMENTS},set(expected))
  self.assertEqual(sum(r['section']=='A' for r in REQUIREMENTS),25)
  self.assertEqual(sum(r['section']=='B' for r in REQUIREMENTS),17)
  self.assertTrue(all(not r['consumer_ui_integrated'] for r in REQUIREMENTS))
  m=json.loads((R/'manifest.json').read_text());base=json.loads((R/'src/published758_baseline.json').read_text())['icons'];icons={i['id']:i for i in m['icons']}
  self.assertEqual(set(icons)-set(base),set(expected)|LATER_ADDITIONS);self.assertEqual(m['count'],800+len(LATER_ADDITIONS))
 def test_all758_preserved(self):
  icons={i['id']:i for i in json.loads((R/'manifest.json').read_text())['icons']}
  base=json.loads((R/'src/published758_baseline.json').read_text())['icons']
  self.assertEqual(len(base),758)
  for id,b in base.items():
   item=icons[id]
   self.assertEqual(hashlib.sha256(json.dumps(item,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest(),b['record_sha256'],id)
   for t in ('light','dark'):self.assertEqual(hashlib.sha256((R/item['variants'][t]['file']).read_bytes()).hexdigest(),b[t],(id,t))
 def test_distinct_substitutes(self):
  icons={i['id']:i for i in json.loads((R/'manifest.json').read_text())['icons']}
  pairs=[('cad-rotate-selected-face','cad-transform-selected-face'),('cad-ground-shadow','cad-shadow-maps'),('common-reset','common-refresh'),('cad-sketch-fillet','cad-fillet'),('cad-sketch-chamfer','cad-chamfer'),('cad-open-sheet-metal-sample','common-open-sample'),('cae-export-pptx-report','cae-analysis-report')]
  for a,b in pairs:self.assertNotEqual(icons[a]['body'],icons[b]['body'],(a,b))
