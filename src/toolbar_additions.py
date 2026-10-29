"""Distinct toolbar meanings requested after the source-scoped GUI audit."""
from toolbar_display_additions import ITEMS as DISPLAY
from toolbar_model_additions import ITEMS as MODEL
from toolbar_context_additions import ITEMS as CONTEXT
TOOLBAR_ADDITIONS={}
for group in (DISPLAY, MODEL, CONTEXT):
    for raw in group:
        item=dict(raw)
        domain=item.pop('domain')
        TOOLBAR_ADDITIONS.setdefault(domain, []).append(item)

# Exact consumer spellings improve search; existing records stay immutable.
import json
from pathlib import Path
_binding_path=Path(__file__).resolve().parents[1]/'toolbar-bindings.json'
if _binding_path.exists():
    _bindings={r['icon_id']:r for r in json.loads(_binding_path.read_text(encoding='utf-8'))['bindings']}
    for domain,items in TOOLBAR_ADDITIONS.items():
        for item in items:
            row=_bindings[domain.lower()+'-'+item['id']]
            item['aliases']=list(dict.fromkeys(item.get('aliases',[])+row['consumer_command_values']))
