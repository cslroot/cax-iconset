#!/usr/bin/env python3
"""Reproduce source-reviewed before/after comparisons at native UI sizes."""
import json, re
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
current={i['id']:i for i in json.loads((ROOT/'manifest.json').read_text())['icons']}
reviews=json.loads((ROOT/'src/quality_review.json').read_text())
width=1080
height=100+len(reviews)*156
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="#f5f8f5"/><g font-family="sans-serif" fill="#253b53"><text x="24" y="34" font-size="24">CAX / geometry corrections</text><text x="24" y="61" font-size="14">Before and after: 64 / 32 / 24 / 16 px. Rounded strokes and semantic IDs retained.</text>']
for n,review in enumerate(reviews):
    y=84+n*156
    parts.append(f'<rect x="16" y="{y}" width="1048" height="145" rx="10" fill="white" stroke="#dce6df"/><text x="30" y="{y+22}" font-size="14">{escape(review["id"])}</text><text x="30" y="{y+132}" font-size="11">{escape(review["reason"])}</text>')
    for side,body in [('Before',review['beforeBody']),('After',current[review['id']]['body'])]:
        x=30 if side=='Before' else 560
        parts.append(f'<text x="{x}" y="{y+49}" font-size="11" fill="#45665f">{side}</text>')
        for size,dx in [(64,65),(32,165),(24,230),(16,285)]:
            prefix=f'quality-{n}-{side}-{size}-'
            unique=re.sub(r'id="([^"]+)"',lambda m:f'id="{prefix}{m[1]}"',body)
            unique=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{prefix}{m[1]})',unique)
            parts.append(f'<svg x="{x+dx}" y="{y+43+(64-size)/2}" width="{size}" height="{size}" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{unique}</svg>')
parts.append('</g></svg>')
(ROOT/'qa/quality-before-after.svg').write_text(''.join(parts))
print(f'Built {len(reviews)} before/after comparisons')
