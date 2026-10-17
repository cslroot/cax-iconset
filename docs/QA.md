# QA report

Date: 2026-10-17. Collection: 4,805 SVGs, 100 core / 4,705 context variants.

## Executed checks

| Check | Result | Method |
| --- | --- | --- |
| Rebuild | Pass | `python3 scripts/build.py`; generated assets match source |
| Catalog safety / integrity | Pass | Three `unittest` groups inspecting every SVG and metadata entry |
| Normalized XML geometry uniqueness | 0 duplicate groups | Ignores label text, colors and local ID spelling; preserves geometry |
| Blank raster detection | 0 | All 4,805 SVG bodies rendered at 2× with Inkscape |
| Painting outside viewBox | 0 | Atlas places each icon without a per-icon viewport clip, then measures alpha bounds |
| Identical raster detection | 0 groups | Color-normalized 2× images compared byte-for-byte |
| JavaScript syntax | Pass | `node --check app.js` and `node --check catalog.js` |
| Application behavior | 10 groups passed | Real scripts executed in Node's VM with a minimal DOM harness |
| Contact sheets | Reviewed | Core 100 and representative CAD/CAM/CAE/CMM/OLP contexts at 48 / 24 px |

The raster results are saved in [`qa/raster-audit.json`](../qa/raster-audit.json). `scripts/raster_audit.py` exits with a failure code if it finds blanks, overflow, or duplicate rasters. Raster intermediates are not committed.

## Application interaction coverage

1. Initial total, bounded 96-item page and category controls
2. English / Japanese / multi-term / Unicode-normalized search, empty state and clear
3. Category and type intersections, including shared centroid counts
4. All 51 pages, last-page bounds, previous navigation and query page reset
5. Japanese labels, preview sizes, background controls
6. Detail open, repeated open, close, backdrop targeting and restored focus
7. Unique preview clip IDs and standalone copied SVG
8. Clipboard rejection, failed fallback, throwing fallback and temporary-element cleanup
9. Download filename and SVG blob content
10. `/` shortcut guarding input fields and an open dialog

These checks found and fixed a thrown clipboard-fallback error, duplicate preview clip IDs, an inaccessible search name and a mismatched dark-detail background. Four previously overflowing keyhole drawings were corrected and the full raster audit was repeated.

## Not executed / limits

- **No real browser UI run.** Browser execution was unavailable in the implementation environment. The separate browser could not access its localhost server or local files. No deployment was made to work around that limitation.
- No claim of tested desktop/mobile layout, computed CSS, native Escape/focus trapping, browser history, real system clipboard, or actual saved downloads.
- The DOM harness simulates the APIs used by the app; it cannot establish browser integration or visual correctness of the webpage.
- Alpha bounds use a threshold of 10/255 at 2×. This catches visible clipping, not every theoretical subpixel paint extent.
- Exact raster and XML uniqueness do not guarantee that all variants are perceptually easy to distinguish at 16 px.
- Contact-sheet review is representative, not an expert semantic certification of each of the 4,805 icons.
- No install/build dependency was added, and no external font or vendor artwork is required.

## Manual browser checklist

Run the local server from the README, then check at desktop and narrow mobile widths:

- Search by `extrude`, `押し出し` and a nonsense term; clear and reset
- Combine each category with core / context filters; test the last page and Previous
- Switch labels, all sizes and backgrounds; inspect overflow and color contrast
- Open several details, close with ×, click the backdrop and press Escape; check keyboard focus
- Copy SVG on a secure localhost origin; paste into a text editor and verify valid SVG
- Download SVG; open the saved file and confirm the filename and appearance
- Confirm no console errors or external requests

## Visual samples

- [Core 100](../qa/core-100.png)
- [CAD variants](../qa/variants-cad.png)
- [CAM variants](../qa/variants-cam.png)
- [CAE variants](../qa/variants-cae.png)
- [CMM variants](../qa/variants-cmm.png)
- [OLP variants](../qa/variants-olp.png)
