"""Color-role variants. Geometry and original SVG bytes remain the source of truth.

Opaque white fills cover earlier geometry; never replace them with transparency.
The dark variant is designed for #192c3c. Its cutouts remain that color on other
surfaces; consumers must explicitly choose or rebuild a matching surface palette.
"""
import re

THEMES = {
    'light': {'label': 'Light', 'surface': '#ffffff', 'palette': {
        'ink': '#253b53', 'body': '#d7efed', 'accent': '#178b88',
        'warning': '#c88626', 'warningBody': '#fff3da', 'cutout': 'white'}},
    'dark': {'label': 'Dark', 'surface': '#192c3c', 'palette': {
        'ink': '#d1e5ed', 'body': '#294c59', 'accent': '#63cec4',
        'warning': '#efbd63', 'warningBody': '#51432c', 'cutout': '#192c3c'}},
}
# Attribute-specific mapping avoids recoloring geometry, IDs or descriptions.
PAINT_ROLES = {
    ('stroke', '#253b53'): 'ink', ('fill', '#253b53'): 'ink',
    ('stroke', '#178b88'): 'accent', ('fill', '#178b88'): 'accent',
    ('stroke', '#c88626'): 'warning', ('fill', '#c88626'): 'warning',
    ('fill', '#d7efed'): 'body', ('fill', '#fff3da'): 'warningBody',
    ('fill', 'white'): 'cutout',
}

def themed_body(body, theme):
    palette = THEMES[theme]['palette']
    def paint(match):
        kind, color = match.groups()
        if color == 'none':
            return match[0]
        role = PAINT_ROLES.get((kind, color))
        if role is None:
            raise ValueError(f'Unmapped SVG color role: {kind}={color}')
        return f'{kind}="{palette[role]}"'
    return re.sub(r'(fill|stroke)="([^"]+)"', paint, body)
