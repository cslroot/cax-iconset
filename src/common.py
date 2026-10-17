"""Distinct, hand-drawn commands shared by engineering applications."""

from core import p, r, c, g, accent, fill, TEAL, PALE


COMMON = []


def _add(id, en, ja, body, tags, description, description_ja, family, role='command'):
    COMMON.append({
        'id': id,
        'name': en,
        'nameJa': ja,
        'body': body,
        'tags': tags,
        'description': description,
        'descriptionJa': description_ja,
        'family': family,
        'role': role,
    })


# Files and output: recognizable documents, folders, disks and paper handling.
_add('new-file', 'New file', '新規ファイル',
     p('M7 3 H20 L26 9 V29 H7 Z M20 3 V9 H26')
     + accent('M16 14 V24 M11 19 H21'),
     ['file', 'new', 'document', 'ファイル', '新規作成'],
     'Create a new untitled document in the active application.',
     '使用中のアプリケーションで新しい名称未設定の文書を作成します。', 'file')

_add('open-file', 'Open file', 'ファイルを開く',
     p('M3 25 V8 Q3 6 5 6 H12 L15 10 H25 Q27 10 27 12 V14')
     + fill('M3 26 7 14 H29 L25 26 Z'),
     ['file', 'open', 'folder', 'ファイル', '開く'],
     'Browse for an existing file and open it in the application.',
     '既存のファイルを参照してアプリケーションで開きます。', 'file')

_add('recent-files', 'Recent files', '最近使ったファイル',
     r(4, 6, 16, 20, 2) + p('M8 3 H23 V15 M8 11 H15 M8 16 H12')
     + c(22, 23, 6, fill='white') + accent('M22 19 V23 L25 25'),
     ['file', 'recent', 'history', 'ファイル', '最近使った項目'],
     'List previously opened files for quick access.',
     '最近開いたファイルの一覧から目的のファイルにアクセスします。', 'file')

_add('close-file', 'Close file', 'ファイルを閉じる',
     p('M7 3 H20 L26 9 V29 H7 Z M20 3 V9 H26')
     + accent('M12 15 21 24 M21 15 12 24'),
     ['file', 'close', 'document', 'ファイル', '閉じる'],
     'Close the current document without exiting the application.',
     'アプリケーションを終了せずに現在の文書を閉じます。', 'file')

_add('save', 'Save', '保存',
     p('M6 4 H23 L28 9 V28 H4 V6 Q4 4 6 4 Z')
     + r(9, 4, 12, 9, 1, fill=PALE) + p('M18 5 V10')
     + r(9, 19, 14, 9, 1),
     ['file', 'save', 'disk', 'ファイル', '上書き保存'],
     'Write changes to the current file at its existing location.',
     '現在のファイルを元の保存先へ上書き保存します。', 'file')

_add('save-as', 'Save as', '名前を付けて保存',
     p('M21 11 V8 L17 4 H4 V25 H12') + r(8, 4, 9, 7, 1, fill=PALE)
     + p('M8 25 V17 H15')
     + fill('M14 24 24 14 28 18 18 28 13 29 Z')
     + accent('M22 16 26 20 M14 24 18 28'),
     ['file', 'save as', 'name', 'ファイル', '別名保存'],
     'Save the current document with a chosen name, location or format.',
     '名前、保存先、形式を指定して現在の文書を保存します。', 'file')

_add('save-all', 'Save all', 'すべて保存',
     p('M3 21 V3 H22 M7 25 V7 H26')
     + fill('M11 11 H25 L29 15 V29 H11 Z')
     + p('M15 11 V17 H23 V11 M15 29 V23 H25 V29'),
     ['file', 'save all', 'documents', 'ファイル', '一括保存'],
     'Save changes in every open document.',
     '開いているすべての文書の変更を保存します。', 'file')

_add('import', 'Import', 'インポート',
     p('M12 11 V3 H22 L28 9 V29 H12 V23 M22 3 V9 H28')
     + accent('M3 17 H22 M17 12 22 17 17 22'),
     ['file', 'import', 'read', 'ファイル', '読み込み'],
     'Bring data from an external file into the active document.',
     '外部ファイルのデータを現在の文書に取り込みます。', 'file')

_add('export', 'Export', 'エクスポート',
     p('M20 11 V8 L15 3 H4 V29 H20 V23 M15 3 V8 H20')
     + accent('M11 17 H29 M24 12 29 17 24 22'),
     ['file', 'export', 'write', 'ファイル', '書き出し'],
     'Write document data to a file for use in another application.',
     '別のアプリケーションで利用するために文書のデータを書き出します。', 'file')

_add('print', 'Print', '印刷',
     p('M9 11 V3 H23 V11 M8 23 H4 V11 H28 V23 H24')
     + r(8, 19, 16, 10, 1, fill=PALE) + p('M12 23 H20 M12 26 H18')
     + c(24, 15, 0.9, fill=TEAL, stroke='none'),
     ['file', 'print', 'printer', 'ファイル', '印刷'],
     'Send the current document or drawing to a printer.',
     '現在の文書または図面をプリンターに送信します。', 'output')

_add('print-preview', 'Print preview', '印刷プレビュー',
     p('M7 10 V3 H21 V10 M8 23 H3 V10 H25 V16')
     + r(7, 18, 10, 10, 1, fill=PALE) + p('M10 22 H13')
     + c(22, 21, 5, fill='white') + accent('M25.5 24.5 29 28'),
     ['file', 'print preview', 'page', '印刷', 'プレビュー'],
     'Inspect page layout and printable content before printing.',
     '印刷前にページのレイアウトと印刷内容を確認します。', 'output')


# Editing: each symbol depicts its particular clipboard or object operation.
_add('undo', 'Undo', '元に戻す',
     accent('M12 6 4 13 12 20')
     + p('M5 13 H19 C31 13 31 27 19 27 H15'),
     ['edit', 'undo', 'back', '編集', '取り消し'],
     'Reverse the most recent reversible editing action.',
     '直前に行った取り消し可能な編集操作を元に戻します。', 'edit')

_add('redo', 'Redo', 'やり直し',
     accent('M20 6 28 13 20 20')
     + p('M27 13 H13 C1 13 1 27 13 27 H17'),
     ['edit', 'redo', 'forward', '編集', 'やり直し'],
     'Reapply the most recently undone editing action.',
     '直前に元に戻した編集操作を再実行します。', 'edit')

_add('cut', 'Cut', '切り取り',
     c(8, 24, 4, fill=PALE) + c(24, 24, 4, fill=PALE)
     + p('M11 21 25 4 M21 21 7 4') + c(16, 15, 1.3, fill=TEAL),
     ['edit', 'cut', 'clipboard', '編集', '切り取り'],
     'Move the selected content to the clipboard.',
     '選択した内容をクリップボードへ移します。', 'edit')

_add('copy', 'Copy', 'コピー',
     p('M10 23 H4 V4 H22 V10') + r(10, 10, 18, 19, 2, fill=PALE)
     + p('M15 16 H23 M15 21 H23'),
     ['edit', 'copy', 'clipboard', '編集', '複写'],
     'Copy the selected content to the clipboard without removing it.',
     '選択した内容を残したままクリップボードへコピーします。', 'edit')

_add('paste', 'Paste', '貼り付け',
     r(6, 6, 21, 23, 2) + r(11, 3, 11, 6, 2, fill=PALE)
     + accent('M3 18 H18 M14 14 18 18 14 22')
     + p('M13 25 H22'),
     ['edit', 'paste', 'clipboard', '編集', '貼り付け'],
     'Insert the clipboard content into the active document.',
     'クリップボードの内容を現在の文書へ挿入します。', 'edit')

_add('delete', 'Delete', '削除',
     p('M5 8 H27 M11 8 V4 H21 V8')
     + fill('M8 8 H24 L22 28 H10 Z') + p('M13 13 V23 M19 13 V23'),
     ['edit', 'delete', 'remove', '編集', '削除'],
     'Remove the selected objects or content from the document.',
     '選択したオブジェクトや内容を文書から削除します。', 'edit')

_add('duplicate', 'Duplicate', '複製',
     r(4, 4, 12, 12, 2, stroke_dasharray='2 2')
     + r(16, 16, 12, 12, 2, fill=PALE)
     + accent('M21 5 H27 V11 M27 5 19 13')
     + p('M5 21 V27 H11'),
     ['edit', 'duplicate', 'clone', '編集', '複製'],
     'Create an independent copy of the selected object in place.',
     '選択したオブジェクトの独立したコピーを文書内に作成します。', 'edit')

_add('rename', 'Rename', '名前の変更',
     r(3, 10, 26, 14, 2) + p('M7 17 H12')
     + accent('M16 5 H23 M19.5 5 V28 M16 28 H23'),
     ['edit', 'rename', 'label', '編集', '名称変更'],
     'Edit the name of the selected file or object.',
     '選択したファイルやオブジェクトの名前を変更します。', 'edit')


# Find, filter and application guidance.
_add('search', 'Search', '検索',
     c(13, 13, 9, fill=PALE) + p('M19.5 19.5 28 28'),
     ['find', 'search', 'query', '検索', '探す'],
     'Find content or objects matching a search term.',
     '検索語に一致する内容やオブジェクトを探します。', 'find')

_add('replace', 'Replace', '置換',
     c(10, 10, 6) + p('M14.5 14.5 18 18')
     + r(20, 20, 8, 8, 1, fill=PALE)
     + accent('M4 20 V26 H15 M11 22 15 26 11 29'),
     ['find', 'replace', 'substitute', '検索', '置換'],
     'Find matching content and substitute a specified replacement.',
     '一致する内容を検索し、指定した内容に置き換えます。', 'find')

_add('filter', 'Filter', 'フィルター',
     fill('M4 5 H28 L19 16 V25 L13 28 V16 Z')
     + accent('M9 10 H23'),
     ['find', 'filter', 'criteria', '絞り込み', '条件'],
     'Limit the displayed items to those matching selected criteria.',
     '指定した条件に一致する項目だけを表示します。', 'find')

_add('clear-filter', 'Clear filter', 'フィルター解除',
     p('M4 5 H28 L19 16 V21 M13 28 V16 L4 5')
     + accent('M20 23 28 29 M28 23 20 29') + p('M13 28 16 26'),
     ['find', 'filter', 'reset', '絞り込み', '解除'],
     'Remove the active filter and show all available items.',
     '適用中のフィルターを解除してすべての項目を表示します。', 'find')

_add('settings', 'Settings', '設定',
     p('M14 3 H18 L19 7 22 8 26 7 28 11 25 14 V18 L28 21 26 25 '
       '22 24 19 25 18 29 H14 L13 25 10 24 6 25 4 21 7 18 V14 '
       'L4 11 6 7 10 8 13 7 Z')
     + c(16, 16, 5, fill=PALE),
     ['application', 'settings', 'preferences', '設定', '環境設定'],
     'Configure application preferences and general behavior.',
     'アプリケーションの環境設定や基本動作を変更します。', 'application')

_add('help', 'Help', 'ヘルプ',
     c(16, 16, 12) + accent('M11 11 C11 5 22 5 22 12 C22 16 16 16 16 20')
     + c(16, 25, 0.9, fill=TEAL, stroke='none'),
     ['application', 'help', 'documentation', 'ヘルプ', '使い方'],
     'Open help topics or documentation for the application.',
     'アプリケーションのヘルプや操作説明を開きます。', 'application')

_add('info', 'Information', '情報',
     c(16, 16, 12, fill=PALE) + c(16, 9, 1, fill=TEAL, stroke='none')
     + p('M13 14 H16 V24 M12 24 H20'),
     ['application', 'info', 'about', '情報', '詳細'],
     'Identify a message that provides contextual information or explanation.',
     '補足情報や説明を伝える情報メッセージであることを示します。', 'status', 'status')


# Selection and visibility are separate commands with separate outcomes.
_add('select', 'Select', '選択',
     fill('M7 3 27 18 18 19 14 29 Z') + accent('M18 19 24 28'),
     ['selection', 'select', 'pointer', '選択', 'ポインター'],
     'Pick an object or region as the target of subsequent commands.',
     '後続の操作の対象となるオブジェクトや領域を選択します。', 'selection')

_add('select-all', 'Select all', 'すべて選択',
     r(4, 4, 24, 24, 1, stroke_dasharray='2 3')
     + ''.join(r(x, y, 6, 6, 1, fill=PALE, stroke=TEAL)
               for x, y in [(8, 8), (18, 8), (8, 18), (18, 18)]),
     ['selection', 'select all', 'objects', '選択', '全選択'],
     'Select every eligible object in the current editing context.',
     '現在の編集範囲で選択可能なすべてのオブジェクトを選択します。', 'selection')

_add('deselect', 'Deselect', '選択解除',
     p('M17 4 H4 V28 H17 M28 4 V17', stroke_dasharray='2 3')
     + r(9, 9, 10, 10, 1)
     + accent('M22 22 28 28 M28 22 22 28'),
     ['selection', 'deselect', 'clear selection', '選択', '解除'],
     'Clear the current selection without changing the objects.',
     'オブジェクトを変更せずに現在の選択状態を解除します。', 'selection')

_add('invert-selection', 'Invert selection', '選択を反転',
     r(9, 9, 7, 7, 0.7, fill=PALE, stroke=TEAL)
     + r(16, 9, 7, 7, 0.7) + r(9, 16, 7, 7, 0.7)
     + r(16, 16, 7, 7, 0.7, fill=PALE, stroke=TEAL)
     + accent('M4 14 V5 H23 M20 2.5 23 5 20 7.5 '
              'M28 18 V27 H9 M12 24.5 9 27 12 29.5'),
     ['selection', 'invert', 'complement', '選択', '反転'],
     'Exchange the selected and unselected objects in the current context.',
     '現在の編集範囲で選択済みと未選択のオブジェクトを入れ替えます。', 'selection')

_add('selection-window', 'Window selection', '内包選択',
     c(8, 18, 5) + r(8, 9, 20, 19, 1)
     + c(21, 18, 3, fill=PALE, stroke=TEAL)
     + accent('M5 4 H25 M21 2.5 25 4 21 5.5'),
     ['selection', 'window', 'enclosed', '選択', '内包', '矩形'],
     'Select only objects fully enclosed by a left-to-right rectangular window.',
     '左から右に指定した矩形の内部に完全に収まるオブジェクトだけを選択します。', 'selection')

_add('selection-crossing', 'Crossing selection', '交差選択',
     r(4, 9, 20, 19, 1, stroke_dasharray='2 2')
     + r(9, 14, 6, 8, 1, fill=PALE, stroke=TEAL)
     + c(24, 18, 5, fill=PALE, stroke=TEAL)
     + accent('M27 4 H7 M11 2.5 7 4 11 5.5'),
     ['selection', 'crossing', 'intersect', '選択', '交差', '矩形'],
     'Select objects inside or crossing a right-to-left rectangular window.',
     '右から左に指定した矩形の内部にあるか境界と交差するオブジェクトを選択します。', 'selection')

_add('selection-lasso', 'Lasso selection', '投げ縄選択',
     p('M4 15 C2 7 11 3 19 6 C31 9 30 16 26 23 '
       'C23 30 13 30 8 24 C5 20 10 18 4 15 Z', stroke_dasharray='2 2')
     + r(11, 11, 6, 6, 1, fill=PALE, stroke=TEAL)
     + c(20, 22, 3, fill=PALE, stroke=TEAL) + p('M4 15 3 24 8 21'),
     ['selection', 'lasso', 'freeform', '選択', '投げ縄', '自由領域'],
     'Select objects using a freehand boundary drawn around the desired region.',
     '目的の範囲を自由な輪郭で囲んでオブジェクトを選択します。', 'selection')

_add('show', 'Show', '表示',
     fill('M3 16 Q16 1 29 16 Q16 31 3 16 Z')
     + c(16, 16, 5) + c(16, 16, 1.5, fill=TEAL, stroke='none'),
     ['visibility', 'show', 'visible', '表示', '可視'],
     'Make the selected hidden objects visible in the viewport.',
     '非表示の選択オブジェクトをビューポートに表示します。', 'visibility')

_add('hide', 'Hide', '非表示',
     p('M3 16 Q8 10 12 9 M18 8 Q24 9 29 16 Q24 22 20 23 '
       'M14 24 Q8 23 3 16') + p('M12 13 A5 5 0 0 0 19 20')
     + accent('M5 4 27 28'),
     ['visibility', 'hide', 'invisible', '非表示', '隠す'],
     'Hide the selected objects while retaining them in the document.',
     '選択したオブジェクトを文書に残したまま非表示にします。', 'visibility')

_add('isolate', 'Isolate', '選択のみ表示',
     r(3, 4, 6, 6, 1, stroke_dasharray='2 2')
     + r(23, 4, 6, 6, 1, stroke_dasharray='2 2')
     + r(3, 23, 6, 6, 1, stroke_dasharray='2 2')
     + r(23, 23, 6, 6, 1, stroke_dasharray='2 2')
     + r(11, 11, 10, 10, 2, fill=PALE, stroke=TEAL),
     ['visibility', 'isolate', 'focus', '表示', '選択のみ'],
     'Temporarily display only the selected objects to reduce visual clutter.',
     '選択したオブジェクトだけを一時的に表示して確認しやすくします。', 'visibility')


# View navigation, including the actual difference between fitting and zooming.
_add('zoom-in', 'Zoom in', '拡大',
     c(13, 13, 9) + p('M19.5 19.5 28 28')
     + accent('M13 8 V18 M8 13 H18'),
     ['view', 'zoom in', 'magnify', '表示', '拡大'],
     'Increase the viewport magnification around the current focus.',
     '現在の注目位置を中心にビューポートの表示倍率を上げます。', 'view')

_add('zoom-out', 'Zoom out', '縮小',
     c(13, 13, 9) + p('M19.5 19.5 28 28') + accent('M8 13 H18'),
     ['view', 'zoom out', 'reduce', '表示', '縮小'],
     'Decrease the viewport magnification to show a wider area.',
     '表示倍率を下げてビューポートにより広い範囲を表示します。', 'view')

_add('zoom-fit', 'Zoom to fit', '全体表示',
     r(3, 4, 26, 24, 2) + r(12, 12, 8, 8, 1, fill=PALE)
     + accent('M7 8 11 12 M7 12 H11 V8 '
              'M25 8 21 12 M21 8 V12 H25 '
              'M7 24 11 20 M7 20 H11 V24 '
              'M25 24 21 20 M21 24 V20 H25'),
     ['view', 'fit', 'extents', '表示', '全体'],
     'Adjust the view so that all visible document content fits on screen.',
     '表示中の文書内容全体が画面に収まるように表示倍率を調整します。', 'view')

_add('zoom-selection', 'Zoom to selection', '選択範囲を拡大',
     c(13, 13, 10) + p('M20 20 28 28')
     + r(8, 8, 10, 10, 1, stroke=TEAL, stroke_dasharray='2 2'),
     ['view', 'zoom selection', 'focus', '表示', '選択範囲'],
     'Fit the selected objects or region tightly within the viewport.',
     '選択したオブジェクトや領域が画面に収まる大きさまで拡大します。', 'view')

_add('pan', 'Pan', '画面移動',
     fill('M9 16 V9 C9 6 13 6 13 9 V14 V5 C13 2 17 2 17 5 V14 '
          'V7 C17 4 21 4 21 7 V15 V11 C21 8 25 8 25 11 V21 '
          'C25 25 22 29 18 29 H14 C11 29 9 27 7 24 L3 18 '
          'C2 16 5 14 7 16 L9 18 Z')
     + accent('M13 21 V24 M18 20 V24'),
     ['view', 'pan', 'hand', '表示', '平行移動'],
     'Move the view horizontally or vertically without changing its scale.',
     '表示倍率を変えずに表示範囲を上下左右に移動します。', 'view')

_add('rotate-view', 'Rotate view', 'ビューを回転',
     fill('M10 10 16 6 22 10 V20 L16 24 10 20 Z')
     + p('M10 10 16 14 22 10 M16 14 V24')
     + accent('M7 13 C0 16 4 22 16 22 C26 22 30 18 27 15 '
              'M24 15 H28 V19'),
     ['view', 'rotate view', 'orbit', '表示', '回転'],
     'Orbit the camera around the model to inspect it from another angle.',
     'モデルの周囲で視点を回転させて別の角度から確認します。', 'view')

_add('refresh', 'Refresh', '更新',
     p('M5 13 A11 11 0 0 1 24 8 M27 19 A11 11 0 0 1 8 24')
     + accent('M24 3 V9 H18 M8 29 V23 H14'),
     ['view', 'refresh', 'reload', '更新', '再読み込み'],
     'Reload current data or redraw the view to show its latest state.',
     '現在のデータを読み直すか画面を再描画し、最新の状態を表示します。', 'view')

_add('fullscreen', 'Full screen', '全画面表示',
     accent('M4 12 V4 H12 M20 4 H28 V12 M28 20 V28 H20 M12 28 H4 V20')
     + p('M11 11 4 4 M21 11 28 4 M21 21 28 28 M11 21 4 28'),
     ['view', 'fullscreen', 'maximize', '表示', '全画面'],
     'Expand the workspace to occupy the full display.',
     '作業領域をディスプレイ全体に広げます。', 'view')

_add('exit-fullscreen', 'Exit full screen', '全画面表示を終了',
     p('M4 4 11 11 M28 4 21 11 M28 28 21 21 M4 28 11 21')
     + accent('M4 11 H11 V4 M21 4 V11 H28 M28 21 H21 V28 M11 28 V21 H4'),
     ['view', 'exit fullscreen', 'restore', '表示', '全画面終了'],
     'Return from full-screen mode to the normal workspace window.',
     '全画面表示を終了して通常の作業ウィンドウに戻します。', 'view')


# Object organization and precision aids.
_add('properties', 'Properties', 'プロパティ',
     p('M4 7 H28 M4 16 H28 M4 25 H28')
     + r(9, 3, 5, 8, 1, fill=PALE)
     + r(20, 12, 5, 8, 1, fill=PALE)
     + r(6, 21, 5, 8, 1, fill=PALE),
     ['object', 'properties', 'attributes', '属性', 'プロパティ'],
     'Inspect or edit the attributes of the selected object.',
     '選択したオブジェクトの属性を確認または編集します。', 'object')

_add('lock', 'Lock', 'ロック',
     p('M9 14 V10 A7 7 0 0 1 23 10 V14')
     + r(5, 14, 22, 15, 2, fill=PALE)
     + c(16, 20, 1.8) + accent('M16 22 V25'),
     ['object', 'lock', 'protect', 'ロック', '編集禁止'],
     'Prevent the selected object from being edited or moved.',
     '選択したオブジェクトの編集や移動を禁止します。', 'object')

_add('unlock', 'Unlock', 'ロック解除',
     p('M14 14 V9 A7 7 0 0 1 28 9')
     + r(5, 14, 22, 15, 2, fill=PALE)
     + c(16, 20, 1.8) + accent('M16 22 V25'),
     ['object', 'unlock', 'unprotect', 'ロック', '解除'],
     'Allow a locked object to be edited or moved again.',
     'ロックされたオブジェクトを再び編集や移動できるようにします。', 'object')

_add('group', 'Group', 'グループ化',
     r(3, 3, 26, 26, 3, stroke=TEAL)
     + r(7, 8, 10, 10, 1, fill=PALE)
     + c(21, 21, 5) + p('M17 13 H24 V16'),
     ['object', 'group', 'combine', '整理', 'グループ化'],
     'Combine selected objects into a group that can be selected together.',
     '選択した複数のオブジェクトをまとめて選択できるグループにします。', 'organization')

_add('ungroup', 'Ungroup', 'グループ解除',
     r(4, 5, 10, 10, 1, fill=PALE) + c(23, 23, 5)
     + accent('M19 13 28 4 M22 4 H28 V10 M13 19 4 28 M4 22 V28 H10'),
     ['object', 'ungroup', 'separate', '整理', 'グループ解除'],
     'Release a group so its component objects can be selected individually.',
     'グループを解除し、構成オブジェクトを個別に選択できるようにします。', 'organization')

_add('layers', 'Layers', 'レイヤー',
     fill('M3 10 16 3 29 10 16 17 Z')
     + p('M3 16 16 23 29 16 M3 22 16 29 29 22'),
     ['organization', 'layers', 'stack', 'レイヤー', '階層'],
     'Manage named layers and their visibility or object membership.',
     'レイヤーの名前、表示状態、所属オブジェクトを管理します。', 'organization')

_add('grid', 'Grid', 'グリッド',
     r(4, 4, 24, 24, 1) + p('M4 12 H28 M4 20 H28 M12 4 V28 M20 4 V28')
     + r(12, 12, 8, 8, 0, fill=PALE, stroke=TEAL),
     ['precision', 'grid', 'workspace', 'グリッド', '格子'],
     'Show or hide the workspace grid used as a positioning reference.',
     '位置決めの基準となる作業領域のグリッドを表示または非表示にします。', 'precision')

_add('snap', 'Snap', 'スナップ',
     fill('M5 5 H12 V18 A4 4 0 0 0 20 18 V5 H27 V18 '
          'A11 11 0 0 1 5 18 Z')
     + accent('M5 11 H12 M20 11 H27') + p('M16 3 V7'),
     ['precision', 'snap', 'magnet', 'スナップ', '吸着'],
     'Constrain pointer placement to enabled geometric or grid targets.',
     '有効な図形要素やグリッドの位置にポインターを吸着させます。', 'precision')

_add('measure-distance', 'Measure distance', '距離測定',
     p('M3 23 9 29 M23 3 29 9')
     + accent('M8 28 28 8 M8 22 V28 H14 M22 8 H28 V14')
     + c(4, 24, 1.2, fill=PALE) + c(24, 4, 1.2, fill=PALE),
     ['precision', 'measure', 'distance', '測定', '距離'],
     'Calculate the distance between two selected points or entities.',
     '選択した2点または2つの要素の間の距離を測定します。', 'precision')

_add('document-units', 'Document units', '文書の単位',
     p('M7 16 V3 H20 L26 9 V16 M20 3 V9 H26')
     + r(3, 19, 26, 10, 1, fill=PALE)
     + p('M8 19 V24 M13 19 V26 M18 19 V24 M23 19 V26'),
     ['document', 'units', 'measurement', '文書', '単位', '設定'],
     'Set the measurement units used to display and enter document values.',
     '文書内の値の表示や入力に使用する測定単位を設定します。', 'precision')

_add('folder-new', 'New folder', '新規フォルダー',
     fill('M3 8 Q3 6 5 6 H12 L15 10 H27 Q29 10 29 12 V27 H3 Z')
     + accent('M16 14 V24 M11 19 H21'),
     ['organization', 'new folder', 'directory', 'フォルダー', '新規作成'],
     'Create a folder for organizing files or project items.',
     'ファイルやプロジェクト項目を整理するためのフォルダーを作成します。', 'organization')

_add('link', 'Link', 'リンク',
     p('M13 19 10 22 C7 25 3 22 3 19 C3 17 4 16 5 15 '
       'L11 9 C14 6 18 8 19 10')
     + p('M19 13 22 10 C25 7 29 10 29 13 C29 15 28 16 27 17 '
         'L21 23 C18 26 14 24 13 22')
     + accent('M11 21 21 11'),
     ['relationship', 'link', 'connect', 'リンク', '関連付け'],
     'Create an association between selected items or an external reference.',
     '選択した項目同士や外部参照との関連付けを作成します。', 'relationship')

_add('unlink', 'Unlink', 'リンク解除',
     p('M11 17 8 20 C5 23 3 20 3 17 C3 15 5 14 6 13 '
       'L10 9 C12 7 15 8 16 10 '
       'M21 15 24 12 C27 9 29 12 29 15 C29 17 27 18 26 19 '
       'L22 23 C20 25 17 24 16 22')
     + accent('M9 3 12 6 M19 26 22 29 M19 6 22 3 M10 29 13 26'),
     ['relationship', 'unlink', 'disconnect', 'リンク', '関連付け解除'],
     'Remove an association while keeping the linked items themselves.',
     'リンクされている項目を残したまま関連付けを解除します。', 'relationship')

_add('history', 'History', '履歴',
     p('M6 10 A12 12 0 1 1 4 20')
     + accent('M3 5 V12 H10') + p('M16 9 V16 L22 20'),
     ['application', 'history', 'timeline', '履歴', '操作記録'],
     'Review the chronological record of actions or document changes.',
     '操作や文書の変更を時系列で確認します。', 'application')

_add('home', 'Home', 'ホーム',
     p('M3 15 16 4 29 15')
     + fill('M7 12 V28 H13 V20 H19 V28 H25 V12'),
     ['navigation', 'home', 'start', 'ホーム', '開始画面'],
     'Return to the application start page or project home.',
     'アプリケーションの開始画面やプロジェクトのホームに戻ります。', 'navigation')

_add('bookmark', 'Bookmark', 'ブックマーク',
     fill('M8 4 H24 V29 L16 23 8 29 Z')
     + accent('M12 10 H20 M12 14 H20'),
     ['navigation', 'bookmark', 'favorite', 'ブックマーク', 'お気に入り'],
     'Mark the current item or location for quick access later.',
     '現在の項目や場所を後ですぐ開けるように登録します。', 'navigation')

_add('sort', 'Sort', '並べ替え',
     p('M14 7 H28 M14 14 H24 M14 21 H20')
     + accent('M6 4 V28 M3 24 6 28 10 24'),
     ['organization', 'sort', 'order', '並べ替え', '順序'],
     'Reorder displayed items by the selected field and direction.',
     '指定した項目と昇順・降順に従って表示項目を並べ替えます。', 'organization')


# Execution controls and status feedback.
_add('run', 'Run', '実行',
     fill('M9 4 28 16 9 28 Z'),
     ['execution', 'run', 'play', '実行', '開始'],
     'Start the active application task or command sequence.',
     '現在のアプリケーションタスクやコマンド列の実行を開始します。', 'execution')

_add('pause', 'Pause', '一時停止',
     r(7, 5, 6, 22, 1.5, fill=PALE) + r(19, 5, 6, 22, 1.5, fill=PALE),
     ['execution', 'pause', 'suspend', '実行', '一時停止'],
     'Suspend the active task or command sequence so it can resume.',
     '現在のタスクやコマンド列を再開できる状態で一時停止します。', 'execution')

_add('stop', 'Stop', '停止',
     r(6, 6, 20, 20, 3, fill=PALE),
     ['execution', 'stop', 'terminate', '実行', '停止'],
     'Terminate the active application task or command sequence.',
     '現在のアプリケーションタスクやコマンド列の実行を終了します。', 'execution')

_add('confirm', 'Confirm', '確定',
     accent('M4 16 12 24 28 7'),
     ['action', 'confirm', 'accept', '確定', '承認'],
     'Accept the current settings or complete the pending command.',
     '現在の設定を受け入れるか、操作中のコマンドを確定します。', 'action')

_add('cancel', 'Cancel', 'キャンセル',
     p('M7 7 25 25 M25 7 7 25'),
     ['action', 'cancel', 'dismiss', 'キャンセル', '中止'],
     'Dismiss the current dialog or abandon the pending command.',
     '現在のダイアログを閉じるか、操作中のコマンドを中止します。', 'action')

_add('warning', 'Warning', '警告',
     fill('M14.3 4 Q16 1.5 17.7 4 L29 25 Q30 28 27 28 H5 '
          'Q2 28 3 25 Z')
     + accent('M16 10 V19') + c(16, 24, 1, fill=TEAL, stroke='none'),
     ['status', 'warning', 'attention', '警告', '注意'],
     'Indicate a condition that requires attention before proceeding.',
     '処理を続ける前に注意や確認が必要な状態を示します。', 'status', 'status')

_add('error', 'Error', 'エラー',
     c(16, 16, 12, fill=PALE) + accent('M11 11 21 21 M21 11 11 21'),
     ['status', 'error', 'failure', 'エラー', '失敗'],
     'Indicate that an operation failed or cannot continue.',
     '処理が失敗したか続行できない状態を示します。', 'status', 'status')
