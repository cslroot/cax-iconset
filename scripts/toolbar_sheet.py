#!/usr/bin/env python3
"""Paged native 16/24/32px light/dark previews of the toolbar additions."""
from sheet_common import read_json, write_preview_pages, ROOT
m=read_json(ROOT/'manifest.json')
from toolbar_additions import TOOLBAR_ADDITIONS
ids={d.lower()+'-'+i['id'] for d,its in TOOLBAR_ADDITIONS.items() for i in its}
items=[i for i in m['icons'] if i['id'] in ids]
pages=write_preview_pages(items,'qa/toolbar-preview','CAX toolbar additions')
print(f'{len(items)} new meanings across {len(pages)} preview pages')
