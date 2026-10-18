# Bulk icon download

Date: 2026-10-18. Adds one client-side ZIP download for all 419 icons or the complete current result set. No SVG, metadata, theme palette or semantic count is changed.

## Use

1. Click **Download ZIP** beside search.
2. Choose **Current results** (category + usage + search) or **All 419 icons**. Scrolling does not limit the selection.
3. Choose **SVG** or **PNG**, then **Light / Dark**. The initial theme matches the gallery. PNG sizes are 16, 24, 32, 48, 64, 128 and 256 px, independent of preview size; the initial PNG size is 32 px.
4. Click **Download ZIP**. One archive contains one file per icon.

With no results, the dialog still opens so **All icons** is accessible. The empty **Current results** selection disables export. Native dialog focus behavior, labels, live status, progress and **Cancel export** support keyboard use. Escape, × and backdrop dismissal cancel active work and return focus to the opener.

SVG entries keep exact source bytes and established filenames: `<id>.svg` or `<id>.dark.svg`. PNG entries use `<id>.<light|dark>.<size>.png`. The archive is named `cax-icons-<all|filtered>-<count>.<theme>[.<png-size>].<svg|png>.zip`.

The PNG canvas surrounding each icon is transparent. Preview backgrounds are excluded. Authored opaque cutouts remain white or #192c3c to hide covered geometry; they are not erased. See [PNG details](PNG_EXPORT.md).

## Implementation and limits

- `zip.js` is a small dependency-free ZIP32 writer. Entries use the standard stored method (no compression), CRC-32, UTF-8 filenames, matching local/central headers and an end-of-central-directory record.
- Unsafe paths, duplicate filenames and ZIP32 size/count overflow are rejected. Current 419-file exports are far below these limits. No ZIP64, compression, CDN or external conversion service is needed.
- The complete icon list, format, theme and raster size are captured before work starts. Later UI changes cannot change a request. Controls are disabled while it runs, and duplicate starts are ignored.
- SVG bytes come from the same tested exact serializer used by individual copy/download. PNGs use the same alpha-enabled Canvas pipeline as individual export, now with an optional cancellation signal.
- PNG conversion is sequential; each canvas and image URL is cleaned up before the next icon. The event loop is yielded after each PNG and each 16 SVG files. Progress updates avoid announcing every single file.
- Cancellation aborts pending decoding/encoding, clears timers and URLs, and prevents late callbacks from triggering a download. It also works before conversion starts and before ZIP finalization. Closing the dialog cancels; there is no background surprise download.
- Any conversion, encoding, ZIP, object-URL or download-trigger error fails the whole request. No intentionally partial archive is downloaded; the dialog allows retry.
- The ZIP is assembled in memory. Larger selections and PNG dimensions use more memory and time. A saved download is requested once; the browser controls its destination and may prompt according to user settings.
- Local conversion does not upload icons or request third-party resources. Download filenames do not contain search-query text.

## Verification

```sh
python3 tests/test_catalog.py
node --check app.js
node --check zip.js
node tests/test_zip.js
node tests/test_app.js
NO_INTERSECTION_OBSERVER=1 node tests/test_app.js
```

`test_zip.js` verifies known CRC vectors, binary/empty/UTF-8 entries, path safety, duplicate names, format limits and one-time finalization. An independently implemented reader checks each local/central header, filename, offset, size and CRC. Both 419-file theme archives match their original SVG files byte-for-byte. Python `zipfile` and `unzip -t` accept them and the UTF-8 archive.

The application harness passes **38 interaction groups**, nine focused on bulk export. It tests all 419 SVG entries in each theme without scrolling, filtered/all scope, 186 model-tree entries beyond the initial batch, 419 mocked PNG entries per theme, all seven PNG sizes, stable snapshots, repeated clicks, cancellation at several phases, late callbacks, closing/reopening, failures without partial downloads, retries, focus and object-URL cleanup. It is not a browser renderer; mocked PNG bytes are not real raster evidence.

## Live Chrome verification

The public catalog at commit `b74db306f7faa85805ec58fa06ab53a5c0e85efa` was tested after its [successful Pages deployment](https://github.com/cslroot/cax-iconset/actions/runs/39110884595), using the supported cloud Chrome browser and actual downloaded archives:

- Full light and dark SVG ZIPs each contain 419 entries with exact ordered internal names, valid CRC and byte-for-byte equality against every repository SVG.
- Full light and dark 32 px PNG ZIPs each contain 419 nonblank valid RGBA images, all exactly 32 × 32 with transparent corners. Alpha is identical across all 419 light/dark pairs; palette RGB differs.
- The `common save` filter produces exactly three light SVG entries and exactly three dark 128 px PNG entries, with valid CRC, dimensions and transparency.
- Cancel and native Escape during all-icon 256 px PNG jobs produce no download and restore controls/opener. A subsequent export works. A double-click on the full light PNG export produced one observed download; duplicate suppression is also tested in the harness.
- With no matches, Current results cannot export and All 419 remains available.
- The visible trigger and confirmation button both read **Download ZIP ↓**.

The browser download API exposes opaque saved paths, so actual outer archive save names were not established through that API. The expected outer names are harness-verified. Access to the browser's internal downloads page was denied by protocol policy; no alternate route was used. Internal archive filenames and content were verified from the actual ZIP bytes.

Existing live navigation, selected SVG clipboard and 64 px individual-PNG checks are documented separately in [QA](QA.md). Mobile, other browsers, the full seven-size browser matrix and assistive-technology behavior remain unverified.
