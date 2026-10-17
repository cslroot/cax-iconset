#!/usr/bin/env python3
import json
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'manifest.json').read_text())['icons']
items=[i for i in data if i['kind']=='core'][:100]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1280" viewBox="0 0 1400 1280"><rect width="1400" height="1280" fill="#f5f8f5"/><text x="35" y="43" font-family="sans-serif" font-size="24" fill="#253b53">CAX / First 100 core symbols</text><text x="35" y="68" font-family="sans-serif" font-size="12" fill="#6d8277">Original rounded engineering icons · 32px grid · navy / teal / pale teal</text>']
for n,i in enumerate(items):
 x=28+(n%10)*136;y=90+(n//10)*116
 parts.append(f'<rect x="{x}" y="{y}" width="128" height="106" rx="8" fill="white" stroke="#e0e7df"/><svg x="{x+40}" y="{y+12}" width="48" height="48" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{i["body"]}</svg><text x="{x+64}" y="{y+78}" text-anchor="middle" font-family="sans-serif" font-size="8.5" fill="#253b53">{escape(i["name"])}</text><text x="{x+64}" y="{y+94}" text-anchor="middle" font-family="sans-serif" font-size="7" fill="#709387">{i["category"]}</text>')
parts.append('</svg>');(ROOT/'qa/core-100.svg').write_text(''.join(parts))
