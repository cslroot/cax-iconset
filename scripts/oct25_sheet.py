#!/usr/bin/env python3
"""Paged native 16/24/32px light/dark previews of the October 25 additions."""
from sheet_common import read_json, write_preview_pages, ROOT
m=read_json(ROOT/'manifest.json')
from oct25_additions import ADDITIONS
ids={d.lower()+'-'+i['id'] for d,its in ADDITIONS.items() for i in its}
items=[i for i in m['icons'] if i['id'] in ids]
pages=write_preview_pages(items,'qa/oct25-preview','CAX October 25 additions')
print(f'{len(items)} new meanings across {len(pages)} preview pages')
