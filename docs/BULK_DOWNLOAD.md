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

Live bulk ZIP/browser verification is pending publication. Existing live navigation, selected SVG clipboard and 64 px PNG checks are documented separately in [QA](QA.md). Mobile, other browsers and assistive-technology behavior remain unverified.
