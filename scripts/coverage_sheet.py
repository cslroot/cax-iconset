#!/usr/bin/env python3
"""Paged native 16/24/32px light/dark previews of the coverage additions."""
from sheet_common import read_json, write_preview_pages, ROOT
m=read_json(ROOT/'manifest.json')
ids={r['icon_id'] for r in read_json(ROOT/'src/coverage_decisions.json') if r['decision']=='new-glyph'}
items=[i for i in m['icons'] if i['id'] in ids]
pages=write_preview_pages(items,'qa/coverage-preview','CAX coverage additions')
print(f'{len(items)} new meanings across {len(pages)} preview pages')
