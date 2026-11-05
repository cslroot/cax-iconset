#!/usr/bin/env python3
"""Paged native 16/24/32px light/dark previews of the binding additions."""
from sheet_common import read_json, write_preview_pages, ROOT
m=read_json(ROOT/'manifest.json')
ids=set(read_json(ROOT/'src/binding_art_trace.json'))
items=[i for i in m['icons'] if i['id'] in ids]
pages=write_preview_pages(items,'qa/binding-preview','CAX binding additions')
print(f'{len(items)} new meanings across {len(pages)} preview pages')
