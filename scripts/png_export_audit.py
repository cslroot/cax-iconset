#!/usr/bin/env python3
"""Audit transparent PNG rasterization of actual standalone SVG file bytes.

Requires the already-installed Inkscape, Pillow, and NumPy. No SVG, catalog,
or application files are changed. Inkscape's shell batches direct exports of
the original files at each exact size. Every resulting PNG is decoded before
checking its dimensions, visible content, transparency, and opaque cutouts.

This is independent Inkscape raster evidence, NOT a browser Canvas/download
test. The companion browser/unit tests must cover the application's export
code. Optional --preview writes a diagnostic checkerboard PNG.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image, ImageColor, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SIZES = (16, 24, 32, 48, 64, 128, 256)
THEMES = ("light", "dark")
CUTOUT = {"light": "white", "dark": "#192c3c"}
CUTOUT_RGBA = {"light": (255, 255, 255, 255), "dark": (25, 44, 60, 255)}
SENTINEL = "#ff00ff"
SENTINEL_RGBA = (255, 0, 255, 255)
DIRECT_IDS = ("cad-shell", "cad-sketch-line")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def render(source, target, size=None):
    command = [
        "inkscape", str(source), "--export-type=png", "--export-area-page",
        "--export-background-opacity=0", "--export-filename=" + str(target),
    ]
    if size is not None:
        command.extend((f"--export-width={size}", f"--export-height={size}"))
    subprocess.run(command, check=True, capture_output=True, text=True)
    with Image.open(target) as image:
        return image.convert("RGBA")


def output_path(directory, entry, size, marked=False):
    suffix = "-cutouts" if marked else ""
    return directory / f'{entry["theme"]}-{entry["id"]}-{size}{suffix}.png'


def batch_render(entries, directory):
    """Use native Inkscape actions, avoiding intrinsic-size image resampling."""
    commands = []
    for entry in entries:
        for marked in (False, True) if entry["cutoutShapes"] else (False,):
            source = ROOT / entry["file"]
            if marked:
                # Probe source only: keep every other fill/stroke and layer intact.
                # Pure magenta identifies exposed cutout fill without mistaking
                # strokes or later-painted geometry for transparent holes.
                old = ('fill="' + CUTOUT[entry["theme"]] + '"').encode()
                raw = entry["raw"].replace(old, ('fill="' + SENTINEL + '"').encode())
                source = directory / f'{entry["theme"]}-{entry["id"]}-cutouts.svg'
                source.write_bytes(raw)
            # Inkscape action delimiters cannot be escaped portably.
            if any(c in str(source) for c in ";\n\r"):
                raise ValueError(f"Unsupported path for Inkscape actions: {source}")
            commands.append(f"file-open:{source};export-area-page;export-background-opacity:0")
            for size in SIZES:
                target = output_path(directory, entry, size, marked)
                commands.append(f"export-width:{size};export-height:{size};export-filename:{target};export-do")
            commands.append("file-close")
    commands.append("quit")
    subprocess.run(["inkscape", "--shell"], input="\n".join(commands) + "\n",
                   check=True, capture_output=True, text=True)


def verified_occlusion(entry):
    """Prove the two known no-witness cases rather than exempting by ID alone."""
    specs = {
        "cad-mesh-merge-vertices": {
            "centers": [(10, 10), (22, 10), (10, 22), (22, 22)],
            "path": "M10 10 16 16 22 10 M10 22 16 16 22 22",
        },
        "cmm-cloud-normals": {
            "centers": [(7, 24), (16, 20), (25, 23)],
            "path": "M7 24 3 13 M2 17 3 13 7 15 M16 20 V7 M13 10 16 7 19 10 M25 23 29 12 M25 14 29 12 30 16",
        },
    }
    spec = specs.get(entry["id"])
    if spec is None:
        return None
    root = ET.fromstring(entry["raw"])
    elements = list(root.iter())
    circles = [e for e in elements if e.get("fill") == CUTOUT[entry["theme"]]]
    paths = [e for e in elements if e.get("d") == spec["path"]]
    if len(paths) != 1 or len(circles) != len(spec["centers"]):
        return None
    path = paths[0]
    if any(e.tag.split("}")[-1] != "circle" for e in circles):
        return None
    centers = [(float(e.get("cx")), float(e.get("cy"))) for e in circles]
    if centers != spec["centers"] or any(float(e.get("r")) != 1.5 for e in circles):
        return None
    if elements.index(path) <= max(elements.index(e) for e in circles):
        return None
    # These sources use direct children, inherited opaque 1.75-width strokes,
    # and a round cap at every listed center. Reject altered styles/geometry.
    if any(e not in list(root) for e in circles + [path]):
        return None
    for element in [root, *circles, path]:
        if any(name in element.attrib for name in ("style", "transform", "opacity", "stroke-opacity", "fill-opacity")):
            return None
        if float(element.get("stroke-width", root.get("stroke-width"))) != 1.75:
            return None
        if element.get("stroke-linecap", root.get("stroke-linecap")) != "round":
            return None
        if element.get("stroke", root.get("stroke")) in (None, "none"):
            return None
    return {
        "id": entry["id"], "theme": entry["theme"], "centersInViewBox": centers,
        "circleRadius": 1.5, "outlineWidth": 1.75, "uncoveredInnerRadius": 0.625,
        "laterRoundCapRadius": 0.875, "laterPath": spec["path"],
        "explanation": "The circle's own outline covers its outer fill. A later round-capped path starts or ends at every circle center; its 0.875 radius completely covers the remaining 0.625-radius interior. No pure cutout-color pixel is expected.",
        "expectedCoveredCenterRgba": list(ImageColor.getrgb(path.get("stroke"))) + [255],
    }


def preview(images, target):
    ids = ("common-new-file", "cad-shell", "cad-sketch-line", "cmm-measure-circle")
    width, height = 900, 76 + len(ids) * 170
    result = Image.new("RGB", (width, height), "#f5f8f5")
    draw = ImageDraw.Draw(result)
    draw.text((18, 16), "Actual SVG -> Inkscape PNG | 128 px | light / dark", fill="#253b53")
    draw.text((18, 36), "Checkerboard is diagnostic only; PNG alpha is transparent outside painted geometry.", fill="#253b53")
    for row, icon_id in enumerate(ids):
        y = 76 + row * 170
        draw.text((18, y + 58), icon_id, fill="#253b53")
        for col, theme in enumerate(THEMES):
            x = 250 + col * 310
            for yy in range(y, y + 144, 12):
                for xx in range(x, x + 288, 12):
                    color = "#e0e4e8" if ((xx - x) // 12 + (yy - y) // 12) % 2 else "#ffffff"
                    draw.rectangle((xx, yy, xx + 11, yy + 11), fill=color)
            image = images[(icon_id, theme)]
            result.paste(image, (x + 80, y + 8), image)
            draw.text((x + 6, y + 148), theme, fill="#253b53")
    target.parent.mkdir(parents=True, exist_ok=True)
    result.save(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "qa/png-export-audit.json")
    parser.add_argument("--preview", type=Path, help="Optional diagnostic PNG path")
    args = parser.parse_args()
    if not shutil.which("inkscape"):
        parser.error("Inkscape must already be installed")
    manifest = json.loads((ROOT / "manifest.json").read_text())
    entries = []
    failures = {key: [] for key in (
        "sourceHashMismatch", "dimensions", "nonRgbaPng", "blank",
        "noTransparentPixels", "nontransparentTopLeftMargin",
        "themeAlphaMismatch", "directRasterMismatch", "cutoutPixelMismatch",
        "cutoutMissingHighResolutionWitness", "cutoutProbeAlphaMismatch",
        "occludedCutoutCenterMismatch", "sourceChangedDuringAudit",
    )}
    for theme in THEMES:
        for item in manifest["icons"]:
            variant = item["variants"][theme]
            path = ROOT / variant["file"]
            raw = path.read_bytes()
            root = ET.fromstring(raw)
            cutouts = sum(e.get("fill") == CUTOUT[theme] for e in root.iter())
            if sha256(raw) != variant["sha256"]:
                failures["sourceHashMismatch"].append(variant["file"])
            entries.append({"id": item["id"], "theme": theme,
                            "file": variant["file"], "sha256": sha256(raw),
                            "cutoutShapes": cutouts, "raw": raw})
    report = {
        "schemaVersion": 1,
        "method": "Direct Inkscape exports of unchanged original standalone SVG files, batched with native shell actions at explicit requested width/height and transparent page background. Every actual output PNG is decoded before inspection; no embedded-SVG atlas or bitmap rescaling is used.",
        "scope": "Independent raster evidence only. This does not execute browser Canvas, PNG download code, image-load events, or browser antialiasing.",
        "renderer": subprocess.run(["inkscape", "--version"], check=True,
                                   capture_output=True, text=True).stdout.strip(),
        "sizes": list(SIZES), "themes": list(THEMES),
        "semanticIcons": len(manifest["icons"]), "sourceFiles": len(entries),
        "pngCases": len(entries) * len(SIZES),
        "pngEncoding": "Directly exported RGBA PNG, decoded for inspection; exact requested width and height",
        "transparencyChecks": [
            "Every PNG has nonzero painted alpha and at least one alpha=0 pixel.",
            "The known-empty top-left margin pixel is alpha=0 in every PNG; all four corner alpha values are inspected and any painted corners are recorded as diagnostics.",
            "No background rectangle is composited. Painted corner pixels are not treated as a transparency failure because antialiased geometry can legitimately reach a corner.",
            "Light and dark variants have identical alpha at each requested size.",
        ],
        "cutoutCheck": {
            "method": "Separate diagnostic renders change only cutout-role fills to opaque magenta. Every pure-magenta exposed pixel must be the exact expected opaque cutout color in the original-file PNG. Other interior pixels are not assumed transparent. Antialiased cutouts can have no pure-color witness at small sizes. At 256 px each cutout-bearing source must have a witness, unless complete overpainting is verified from its actual geometry/layer order and opaque overpaint-color center samples.",
            "sourceFilesWithCutouts": sum(e["cutoutShapes"] > 0 for e in entries),
            "sourceCutoutShapes": sum(e["cutoutShapes"] for e in entries),
            "palette": {theme: list(CUTOUT_RGBA[theme]) for theme in THEMES},
            "verifiedFullyOverpaintedSources": [],
            "cases": [],
        },
        "directRasterChecks": {"ids": list(DIRECT_IDS), "cases": 0,
                               "method": "Pixel-for-pixel RGBA comparison of batch exports against separate single-file Inkscape invocations, at all seven sizes."},
        "resultsBySize": [],
        "inputs": [{k: v for k, v in e.items() if k != "raw"} for e in entries],
        "failures": failures,
    }
    png_digest = hashlib.sha256()
    preview_images = {}
    with tempfile.TemporaryDirectory(prefix="cax-png-audit-") as temp:
        directory = Path(temp)
        print(f"Directly exporting {len(entries)} originals plus cutout probes at seven sizes", flush=True)
        batch_render(entries, directory)
        for size in SIZES:
            light_alpha = {}
            for theme in THEMES:
                subset = [e for e in entries if e["theme"] == theme]
                cutouts = [e for e in subset if e["cutoutShapes"]]
                stats = {"theme": theme, "size": size, "pngCases": len(subset),
                         "transparentPixels": 0, "paintedPixels": 0,
                         "fullyOpaquePixels": 0, "minimumTransparentPixelsPerPng": size * size,
                         "minimumPaintedPixelsPerPng": size * size,
                         "cornerPixelsChecked": 0, "paintedCornerDiagnostics": [],
                         "cutoutWitnessPixels": 0, "cutoutCasesWithWitness": 0,
                         "cutoutCasesWithoutPurePixelWitness": []}
                for n, entry in enumerate(subset):
                    key = [entry["id"], theme, size]
                    png = output_path(directory, entry, size)
                    data = png.read_bytes()
                    with Image.open(png) as image:
                        file_format, mode, decoded = image.format, image.mode, image.convert("RGBA")
                    rgba = np.asarray(decoded)
                    alpha = rgba[:, :, 3]
                    png_digest.update(f'{entry["file"]}:{size}:'.encode() + data)
                    if decoded.size != (size, size):
                        failures["dimensions"].append(key + [list(decoded.size)])
                    if file_format != "PNG" or mode != "RGBA":
                        failures["nonRgbaPng"].append(key + [file_format, mode])
                    transparent = int(np.count_nonzero(alpha == 0))
                    painted = int(np.count_nonzero(alpha))
                    opaque = int(np.count_nonzero(alpha == 255))
                    stats["transparentPixels"] += transparent
                    stats["paintedPixels"] += painted
                    stats["fullyOpaquePixels"] += opaque
                    stats["minimumTransparentPixelsPerPng"] = min(stats["minimumTransparentPixelsPerPng"], transparent)
                    stats["minimumPaintedPixelsPerPng"] = min(stats["minimumPaintedPixelsPerPng"], painted)
                    if not painted:
                        failures["blank"].append(key)
                    if not transparent:
                        failures["noTransparentPixels"].append(key)
                    corners = alpha[[0, 0, -1, -1], [0, -1, 0, -1]]
                    stats["cornerPixelsChecked"] += 4
                    if np.any(corners):
                        stats["paintedCornerDiagnostics"].append({"id": entry["id"], "alpha": corners.tolist()})
                    if alpha[0, 0]:
                        failures["nontransparentTopLeftMargin"].append(key + [int(alpha[0, 0])])
                    if theme == "light":
                        light_alpha[entry["id"]] = sha256(alpha.tobytes())
                    elif light_alpha[entry["id"]] != sha256(alpha.tobytes()):
                        failures["themeAlphaMismatch"].append(key)
                    if entry["cutoutShapes"]:
                        with Image.open(output_path(directory, entry, size, marked=True)) as probe_image:
                            probe = np.asarray(probe_image.convert("RGBA"))
                        mask = np.all(probe == SENTINEL_RGBA, axis=2)
                        witnesses = int(np.count_nonzero(mask))
                        mismatch = int(np.count_nonzero(np.any(rgba[mask] != CUTOUT_RGBA[theme], axis=1)))
                        case = {"id": entry["id"], "theme": theme, "size": size,
                                "opaqueWitnessPixels": witnesses, "mismatchedPixels": mismatch}
                        if witnesses:
                            yy, xx = np.argwhere(mask)[witnesses // 2]
                            case["sample"] = {"x": int(xx), "y": int(yy), "rgba": rgba[yy, xx].tolist()}
                        report["cutoutCheck"]["cases"].append(case)
                        stats["cutoutWitnessPixels"] += witnesses
                        stats["cutoutCasesWithWitness"] += bool(witnesses)
                        if not witnesses:
                            stats["cutoutCasesWithoutPurePixelWitness"].append(entry["id"])
                            if size == max(SIZES):
                                proof = verified_occlusion(entry)
                                if proof is None:
                                    failures["cutoutMissingHighResolutionWitness"].append(key)
                                else:
                                    samples = []
                                    for cx, cy in proof["centersInViewBox"]:
                                        xx, yy = int(cx * size / 32), int(cy * size / 32)
                                        actual = rgba[yy, xx].tolist()
                                        samples.append({"x": xx, "y": yy, "rgba": actual})
                                        if actual != proof["expectedCoveredCenterRgba"]:
                                            failures["occludedCutoutCenterMismatch"].append(key + [xx, yy, actual])
                                    proof["samplesAt256px"] = samples
                                    report["cutoutCheck"]["verifiedFullyOverpaintedSources"].append(proof)
                        if mismatch:
                            failures["cutoutPixelMismatch"].append(key + [mismatch])
                        if not np.array_equal(alpha, probe[:, :, 3]):
                            failures["cutoutProbeAlphaMismatch"].append(key)
                    if entry["id"] in DIRECT_IDS:
                        direct = render(ROOT / entry["file"], directory / "direct.png", size)
                        report["directRasterChecks"]["cases"] += 1
                        if direct.size != (size, size) or direct.tobytes() != decoded.tobytes():
                            failures["directRasterMismatch"].append(key)
                    if args.preview and size == 128:
                        preview_images[(entry["id"], theme)] = decoded.copy()
                report["resultsBySize"].append(stats)
                print(f'{theme} {size}px: {len(subset)} PNGs, '
                      f'{stats["cutoutCasesWithWitness"]}/{len(cutouts)} cutout sources with pure opaque witnesses', flush=True)
    for entry in entries:
        if sha256((ROOT / entry["file"]).read_bytes()) != entry["sha256"]:
            failures["sourceChangedDuringAudit"].append(entry["file"])
    report["pngCaseDigestSha256"] = png_digest.hexdigest()
    report["inputDigestSha256"] = sha256(json.dumps(report["inputs"], sort_keys=True).encode())
    report["passed"] = not any(failures.values())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.preview:
        preview(preview_images, args.preview)
    print(json.dumps({"passed": report["passed"], "sourceFiles": len(entries),
                      "pngCases": report["pngCases"], "failures": failures,
                      "report": str(args.output)}, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
