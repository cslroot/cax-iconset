"""Helpers shared by the preview and audit scripts.

Files are read and written as UTF-8 with LF line endings on every platform
(manifest.json and the docs contain Japanese), matching build.py.
"""
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_text(path, text):
    Path(path).write_text(text, encoding='utf-8', newline='\n')


def load_font(size=12):
    """DejaVu Sans where it is installed, found by name elsewhere, else PIL's default."""
    from PIL import ImageFont
    for name in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 'DejaVuSans.ttf'):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def write_preview_pages(items, out_dir, title, per_page=24):
    """Paged native 16/24/32px light/dark previews; returns the page paths."""
    from PIL import Image, ImageDraw
    out = ROOT / out_dir
    out.mkdir(exist_ok=True)
    font = load_font(12)
    W = 1200; row = 100; cols = 3
    pages = []
    with tempfile.TemporaryDirectory() as tmp:
        actions = []
        for n, item in enumerate(items):
            for theme in ['light', 'dark']:
                for size in [16, 24, 32]:
                    path = Path(tmp) / f'{n}-{theme}-{size}.png'
                    actions.append(f'file-open:{ROOT/item["variants"][theme]["file"]};export-filename:{path};export-width:{size};export-height:{size};export-do;file-close')
        subprocess.run(['inkscape', '--shell'], input='\n'.join(actions) + '\n', text=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for page in range(math.ceil(len(items) / per_page)):
            chunk = items[page * per_page:(page + 1) * per_page]
            H = 60 + math.ceil(len(chunk) / cols) * row
            im = Image.new('RGB', (W, H), '#eef3f5'); draw = ImageDraw.Draw(im)
            draw.text((20, 12), f'{title} {page+1} | native 16 / 24 / 32 px | light and dark', font=font, fill='#253b53')
            for n, item in enumerate(chunk):
                number = page * per_page + n; x = (n % cols) * 400; y = 50 + (n // cols) * row
                draw.text((x + 12, y), item['name'], font=font, fill='#253b53')
                for j, theme in enumerate(['light', 'dark']):
                    bx = x + 12 + j * 184; by = y + 22
                    draw.rectangle((bx, by, bx + 174, by + 60), fill='white' if theme == 'light' else '#192c3c')
                    for k, size in enumerate([16, 24, 32]):
                        icon = Image.open(Path(tmp) / f'{number}-{theme}-{size}.png').convert('RGBA')
                        im.paste(icon, (bx + 12 + k * 52, by + 12 + (32 - size) // 2), icon)
            file = out / f'page-{page+1:02}.png'; im.save(file); pages.append(str(file.relative_to(ROOT)))
    write_text(out / 'pages.json', json.dumps(pages, indent=2) + '\n')
    return pages
