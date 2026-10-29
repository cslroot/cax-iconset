"""Source-reviewed GUI gap expansion; fixed audit scope, no count target."""
import json
from pathlib import Path
from coverage_sketch_surface import ITEMS as SKETCH_SURFACE
from coverage_model_assembly import ITEMS as MODEL_ASSEMBLY
from coverage_drawing_analysis import ITEMS as DRAWING_ANALYSIS
from coverage_utilities import ITEMS as UTILITIES

COVERAGE = {}
for source in (SKETCH_SURFACE, MODEL_ASSEMBLY, DRAWING_ANALYSIS, UTILITIES):
    for raw in source:
        item = dict(raw)
        domain = item.pop('domain')
        COVERAGE.setdefault(domain, []).append(item)

COVERAGE_REFERENCES = json.loads((Path(__file__).parent/'coverage_sources.json').read_text(encoding='utf-8'))
