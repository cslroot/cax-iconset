"""Additional command glyphs justified by the bounded uncertain-row review."""
import json
from pathlib import Path
from binding_geometry_additions import ITEMS as GEOMETRY
from binding_utility_additions import ITEMS as UTILITIES
from binding_route_additions import ITEMS as ROUTES

TRACE = json.loads((Path(__file__).parent/'binding_art_trace.json').read_text(encoding='utf-8'))
BINDING_ADDITIONS = {}
for source in (GEOMETRY, UTILITIES, ROUTES):
    for raw in source:
        item = dict(raw)
        domain = item.pop('domain')
        full_id = domain.lower()+'-'+item['id']
        item.update(TRACE[full_id])
        BINDING_ADDITIONS.setdefault(domain, []).append(item)

BINDING_REFERENCES = json.loads((Path(__file__).parent/'binding_sources.json').read_text(encoding='utf-8'))
