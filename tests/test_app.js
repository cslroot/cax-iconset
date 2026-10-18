'use strict';
// Runs the real application in a minimal DOM harness. This is not a browser or
// layout engine; browser rendering/clipboard/download integration need manual QA.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const ROOT = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
const ids = new Map();
let document;
const downloads = [];
// These stand-ins check the real app's async Canvas pipeline and selected SVG
// bytes, not raster pixels. scripts/png_export_audit.py checks actual PNG alpha
// independently with Inkscape; browser Canvas/download integration is unverified.
const png={mode:'ok',images:[],canvases:[],pendingImages:[],pendingEncodes:[]};
class Image {
 constructor(){png.images.push(this);}
 set src(value){this.sourceURL=value;const complete=()=>{if(png.mode==='image-error')this.onerror?.();else this.onload?.();};if(png.mode==='image-hang')return;if(png.mode==='hold-image')png.pendingImages.push(complete);else queueMicrotask(complete);}
}
class Element {
 constructor(tag='div') {this.tagName=tag.toUpperCase();this.children=[];this.dataset={};this.attributes={};this.listeners={};this.className='';this.textContent='';this.innerHTML='';this.hidden=false;this.disabled=false;this.open=false;this.value='';this.parent=null;this.isConnected=true;this.style={setProperty:(k,v)=>this.style[k]=v};this.classList={add:c=>this.classList.toggle(c,true),remove:c=>this.classList.toggle(c,false),toggle:(c,on)=>{const classes=new Set(this.className.split(/\s+/).filter(Boolean));if(on)classes.add(c);else classes.delete(c);this.className=[...classes].join(' ');}};}
 set innerHTML(value){this.replaceChildren();this._innerHTML=value;}
 get innerHTML(){return this._innerHTML;}
 set disabled(value){this._disabled=Boolean(value);if(value&&document?.activeElement===this)document.activeElement=document.body;}
 get disabled(){return this._disabled;}
 setAttribute(k,v){this.attributes[k]=String(v);}
 append(...nodes){for(const n of nodes){n.parent=this;n.isConnected=true;this.children.push(n);}}
 replaceChildren(...nodes){for(const n of this.children){n.isConnected=false;n.parent=null;}this.children=[];this.append(...nodes);}
 addEventListener(type,fn){(this.listeners[type]??=[]).push(fn);}
 async dispatch(type,extra={}) {const event={target:this,key:'',preventDefault(){this.defaultPrevented=true;},...extra};for(const fn of this.listeners[type]||[])await fn(event);return event;}
 focus(){document.activeElement=this;}
 select(){}
 scrollIntoView(){this.scrolled=true;}
 remove(){this.isConnected=false;if(this.parent)this.parent.children=this.parent.children.filter(n=>n!==this);}
 showModal(){assert.equal(this.open,false);this.open=true;}
 close(){this.open=false;for(const fn of this.listeners.close||[])fn({target:this});}
 getBoundingClientRect(){return {left:10,top:10,right:600,bottom:500};}
 click(){if(this.tagName==='A'){if(png.mode==='anchor-error')throw Error('Download blocked');downloads.push({href:this.href,name:this.download});return;}if(!this.disabled)return this.dispatch('click');}
}
class Canvas extends Element {
 constructor(){super('canvas');png.canvases.push(this);}
 getContext(kind,options){assert.equal(kind,'2d');assert.equal(options.alpha,true);if(png.mode==='canvas-null')return null;return {drawImage:(image,x,y,width,height)=>{if(png.mode==='draw-error')throw Error('Draw failed');assert.equal(x,0);assert.equal(y,0);assert.equal(width,this.width);assert.equal(height,this.height);this.draw={image,width,height};},fillRect:()=>{throw Error('Canvas background must not be painted');}};}
 toBlob(callback,type){assert.equal(type,'image/png');assert.ok(this.draw);if(png.mode==='encode-error')throw Error('Encode failed');if(png.mode==='encode-hang')return;const complete=()=>callback(png.mode==='null-blob'?null:new Blob(png.mode==='empty-blob'?[]:['mock PNG pixels'],{type:png.mode==='wrong-mime'?'image/jpeg':'image/png'}));if(png.mode==='hold-encode')png.pendingEncodes.push(complete);else queueMicrotask(complete);}
}
for(const match of html.matchAll(/<([a-z][a-z0-9]*)\b[^>]*\bid="([^"]+)"[^>]*>/g)){const e=new Element(match[1]);e.id=match[2];e.hidden=/\bhidden\b/.test(match[0]);e.className=/class="([^"]+)"/.exec(match[0])?.[1]||'';ids.set(e.id,e);}
const all=new Element('button');all.dataset.category='all';all.className='category active';
const backgrounds=['light','dark','grid'].map(background=>{const e=new Element('button');e.dataset.background=background;return e;});
document={body:new Element('body'),documentElement:new Element('html'),activeElement:new Element('body'),listeners:{},getElementById:id=>{assert.ok(ids.has(id),'Missing DOM ID '+id);return ids.get(id);},createElement:tag=>tag==='canvas'?new Canvas():new Element(tag),querySelectorAll:selector=>{if(selector==='.category')return [all,...ids.get('categories').children];if(selector==='[data-background]')return backgrounds;throw Error('Unhandled selector '+selector);},addEventListener(type,fn){(this.listeners[type]??=[]).push(fn);},execCommand:()=>true};
const clipboard=[];
const blobs=[];
const timers=[];
const liveURLs=new Map();
const revokedURLs=[];
function runTimers(delay){for(const timer of timers){if(timer.active&&timer.delay===delay){timer.active=false;timer.fn();}}}
const navigator={clipboard:{writeText:async text=>clipboard.push(text)}};
const observers=[];
class IntersectionObserver {
 constructor(callback,options){this.callback=callback;this.options=options;this.disconnected=false;observers.push(this);}
 observe(target){this.target=target;}
 disconnect(){this.disconnected=true;}
 emit(intersecting=true){this.callback([{target:this.target,isIntersecting:intersecting}]);}
}
const window={isSecureContext:true};
if(!process.env.NO_INTERSECTION_OBSERVER)window.IntersectionObserver=IntersectionObserver;
const context=vm.createContext({document,window,navigator,Blob,Image,TextEncoder,Uint8Array,AbortController,URL:{createObjectURL:blob=>{if(png.mode==='source-url-error'&&blob.type==='image/svg+xml'||png.mode==='png-url-error'&&blob.type==='image/png'||png.mode==='zip-url-error'&&blob.type==='application/zip')throw Error('Object URL unavailable');blobs.push(blob);const url='blob:test-'+blobs.length;liveURLs.set(url,blob);return url;},revokeObjectURL:url=>{assert.ok(liveURLs.has(url),'Object URL must be revoked exactly once: '+url);liveURLs.delete(url);revokedURLs.push(url);}},setTimeout:(fn,delay)=>{if(delay===0)return setTimeout(fn,0);timers.push({fn,delay,active:true});return timers.length;},clearTimeout:id=>{if(typeof id==='object'){clearTimeout(id);return;}if(timers[id-1])timers[id-1].active=false;},console});
vm.runInContext(fs.readFileSync(path.join(ROOT,'catalog.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(ROOT,'zip.js'),'utf8'),context);
for(const [id,value] of Object.entries({'bulk-scope':'filtered','bulk-format':'svg','bulk-theme':'light','bulk-size':'32'}))ids.get(id).value=value;
vm.runInContext(fs.readFileSync(path.join(ROOT,'app.js'),'utf8'),context);
const $=id=>document.getElementById(id);
const count=()=>Number($('result-count').textContent.replace(/\D/g,''));
const cards=()=>$('results').children;
async function input(value){$('search').value=value;await $('search').dispatch('input');}
async function change(id,value){$(id).value=value;await $(id).dispatch('change');}
const tests=[];
async function test(name,fn){await fn();tests.push(name);console.log('PASS '+name);}
(async()=>{
 const manifest=window.CAX_CATALOG;
 const total=manifest.count;
 const batchCount=Math.ceil(total/96);
 await test('initial count, bounded first batch and category controls',async()=>{assert.equal(count(),total);assert.equal(cards().length,96);assert.equal($('load-status').textContent,`96 of ${total} icons shown`);assert.equal($('load-more').disabled,false);assert.equal(document.querySelectorAll('.category').length,7);assert.match($('collection-scope').textContent,/common application symbols/);assert.ok(!html.includes('Context variants'));assert.ok(!ids.has('kind'));});
 await test('English, Japanese, AND and Unicode-normalized searches',async()=>{await input('common save');assert.deepEqual(cards().map(c=>c.dataset.id),['common-save','common-save-as','common-save-all']);await input('名前を付けて保存');assert.equal(cards()[0].dataset.id,'common-save-as');await input('ファイル 開く');assert.ok(cards().some(c=>c.dataset.id==='common-open-file'));await input('ＣＡＤ');const normalized=count();await input('CAD');assert.equal(count(),normalized);assert.ok(count()>=20);await input('no-such-icon-xyz');assert.equal(count(),0);assert.equal($('empty').hidden,false);assert.equal($('load-more').disabled,true);await $('clear').click();assert.equal(count(),total);assert.equal($('empty').hidden,true);assert.equal(document.activeElement,$('search'));});
 await test('separate common and engineering categories and query intersections',async()=>{for(const category of ['Common','CAD','CAM','CAE','CMM','OLP']){await document.querySelectorAll('.category').find(e=>e.dataset.category===category).click();assert.equal(count(),manifest.categoryMemberships[category]);}await document.querySelectorAll('.category').find(e=>e.dataset.category==='Common').click();await input('save');assert.equal(count(),3);await document.querySelectorAll('.category').find(e=>e.dataset.category==='CAD').click();assert.equal(count(),0);await $('reset').click();assert.equal(count(),total);});
 await test('usage filter, node labels, category intersections and reuse without duplicate cards',async()=>{await change('usage','model-tree');assert.equal(count(),manifest.usageCounts['model-tree']);assert.equal(cards().length,Math.min(96,count()));await input('cae-material-assignment');assert.equal(count(),1);assert.equal(cards()[0].children.at(-1).textContent,'Material');await cards()[0].click();assert.equal($('detail-name').textContent,'Material');assert.match($('detail-usage').textContent,/command \/ model-tree/);await $('close').click();await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,'材料');await document.querySelectorAll('.category').find(e=>e.dataset.category==='CAD').click();assert.equal(count(),1);await change('usage','status');assert.equal(count(),0);await $('reset').click();assert.equal($('usage').value,'all');assert.equal(count(),total);await change('language','en');await change('usage','tool');assert.equal(count(),manifest.usageCounts.tool);await change('usage','status');assert.equal(count(),manifest.usageCounts.status);await change('usage','command');assert.equal(count(),manifest.usageCounts.command);await change('usage','model-tree');await input('cad-part component instance');assert.equal(count(),1);assert.equal(cards()[0].dataset.id,'cad-part');await $('reset').click();});
 await test('application-family aliases, shared categories and advanced tree names',async()=>{await input('raster finishing');assert.deepEqual(cards().map(c=>c.dataset.id),['cam-parallel-finishing']);await input('ICP');assert.deepEqual(cards().map(c=>c.dataset.id),['cmm-best-fit-alignment']);await input('shut-off patch');assert.deepEqual(cards().map(c=>c.dataset.id),['cad-surface-patch']);await input('merge coincident nodes');assert.deepEqual(cards().map(c=>c.dataset.id),['cad-mesh-merge-vertices']);await document.querySelectorAll('.category').find(e=>e.dataset.category==='CAE').click();assert.equal(count(),1);await input('重複 節点');assert.equal(count(),1);await $('reset').click();await input('cad-sheet-metal-form-tool');await change('usage','model-tree');assert.equal(cards()[0].children.at(-1).textContent,'Formed feature');await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,'成形フィーチャ');await change('language','en');await $('reset').click();});
 await test('robotics commands, reused joints and bilingual persistent-node names',async()=>{await document.querySelectorAll('.category').find(e=>e.dataset.category==='OLP').click();await input('olp-program-if');assert.equal(count(),1);await change('usage','model-tree');assert.equal(cards()[0].children.at(-1).textContent,'Conditional branch');await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,'条件分岐');await change('language','en');await input('planning group');assert.ok(cards().some(c=>c.dataset.id==='olp-planning-group'));await input('cad-revolute-joint');assert.equal(count(),1);await input('cad-part robot link');assert.deepEqual(cards().map(c=>c.dataset.id),['cad-part']);await input('olp-reference-calibration');assert.equal(count(),0);await change('usage','command');assert.equal(count(),1);await $('reset').click();});
 await test('CAX source-verified commands, recognized result reuse and persistent feature names',async()=>{await input('cad-face-offset');assert.equal(count(),1);await change('usage','model-tree');assert.equal(cards()[0].children.at(-1).textContent,'Face-offset feature');await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,'ソリッド面オフセットフィーチャ');await change('language','en');await input('cad-helix');assert.equal(count(),1);await input('cad-defeature');assert.equal(count(),1);await input('cad-recognize-features');assert.equal(count(),0);await change('usage','command');assert.equal(count(),1);await input('unsuppress feature');assert.deepEqual(cards().map(c=>c.dataset.id),['cad-suppress-feature']);await input('recognized thread');assert.deepEqual(cards().map(c=>c.dataset.id),['cad-thread']);await input('common-screenshot');assert.equal(count(),1);await input('cad-photoreal-render');assert.equal(count(),1);await $('reset').click();});
 await test('pdxadv result families, bounded design actions and reuse without variants',async()=>{await document.querySelectorAll('.category').find(e=>e.dataset.category==='CAE').click();for(const [query,id] of [['normalized sensitivity','cae-sensitivity-result'],['sensitivity density','cae-sensitivity-result'],['肉厚対策','cae-thickness-optimization'],['局所肉厚変更','cae-local-wall-offset'],['肉厚分布','cae-thickness-result'],['有効線収縮率','cae-shrinkage-result'],['ヒケ傾向指標','cae-sink-tendency'],['side-by-side results','cae-compare-results'],['pin baseline','cae-set-baseline'],['PPTX analysis report','cae-analysis-report'],['warpage cae-deformation-result','cae-deformation-result']]){await input(query);assert.deepEqual(cards().map(c=>c.dataset.id),[id]);}await input('cae-set-baseline');await cards()[0].click();assert.match($('detail-description').textContent,/in memory/);await $('close').click();await change('usage','model-tree');assert.equal(count(),0);await change('usage','command');assert.equal(count(),1);await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,'比較基準に保持');await change('language','en');await $('reset').click();});
 await test('SVG themes synchronize preview surfaces and keep manual backgrounds available',async()=>{
  const css=fs.readFileSync(path.join(ROOT,'styles.css'),'utf8');
  assert.ok(!css.includes('svg [fill='));assert.ok(!css.includes('svg [stroke='));assert.ok(!css.includes('drop-shadow'));
  await input('common-info');
  for(const theme of ['dark','light','dark']){
   await change('theme',theme);assert.equal(count(),1);assert.equal($('results').className,'icon-grid '+theme+'-bg');assert.equal(backgrounds.find(b=>b.dataset.background===theme).attributes['aria-pressed'],'true');
   for(const i of [0,1,2,1,0]){await backgrounds[i].click();assert.equal($('results').className,'icon-grid '+['light','dark','grid'][i]+'-bg');assert.ok(cards()[0].innerHTML.includes(`stroke="${manifest.themes[theme].palette.ink}"`));}
   await cards()[0].click();assert.equal($('detail-theme').value,theme);assert.ok($('detail-file').textContent.startsWith(theme==='dark'?'icons-dark/':'icons/'));
   assert.ok($('detail-preview').innerHTML.includes(`stroke="${manifest.themes[theme].palette.ink}"`));
   await backgrounds[1].click();assert.equal($('detail-preview').className,'detail-preview dark-bg');
   const other=theme==='dark'?'light':'dark';await change('detail-theme',other);assert.equal($('theme').value,other);assert.equal($('results').className,'icon-grid '+other+'-bg');assert.equal($('detail-preview').className,'detail-preview '+other+'-bg');assert.equal(backgrounds.find(b=>b.dataset.background===other).attributes['aria-pressed'],'true');await backgrounds[2].click();assert.equal($('detail-preview').className,'detail-preview grid-bg');assert.equal($('theme').value,other);
   await $('close').click();
  }
  await change('theme','light');await $('reset').click();assert.equal(count(),419);
 });
 await test('theme and language updates preserve loaded cards and the original opener',async()=>{
  await $('reset').click();await $('load-more').click();const before=cards()[130];before.focus();await before.click();
  await change('detail-theme','dark');await change('detail-theme','light');
  await change('language','ja');assert.equal(cards().length,192);assert.equal(before.isConnected,true);const after=cards()[130];assert.equal(after,before);assert.equal(after.children.length,2);assert.equal($('detail-name').textContent,manifest.icons[130].nameJa);await change('language','en');
  await $('close').click();assert.equal(document.activeElement,after);assert.equal(after.isConnected,true);
  await $('reset').click();
 });
 await test('append-only loading, complete state, keyboard fallback and filter reset',async()=>{
  const first=cards()[0];first.focus();
  for(let i=1;i<batchCount;i++)await $('load-more').click();
  assert.equal(cards().length,total);assert.equal(cards()[0],first);assert.equal(document.activeElement,first);
  assert.equal(new Set(cards().map(c=>c.dataset.id)).size,total);
  assert.equal($('load-status').textContent,`All ${total} icons shown`);assert.equal($('load-more').hidden,true);
  await $('load-more').dispatch('click');assert.equal(cards().length,total);
  await input('cad-extrude');assert.equal(cards().length,1);assert.equal($('load-status').textContent,'All 1 icons shown');
  await $('reset').click();assert.equal(cards().length,96);assert.equal($('load-more').hidden,false);
  $('load-more').focus();await $('load-more').click();assert.equal(cards().length,192);assert.equal(document.activeElement,cards()[96]);
  await change('usage','model-tree');assert.equal(cards().length,96);
  await document.querySelectorAll('.category').find(e=>e.dataset.category==='Common').click();assert.ok(cards().length<96);
  await $('reset').click();
 });
 await test('observer batches ignore stale callbacks and pause behind details',async()=>{
  if(!window.IntersectionObserver){assert.equal(observers.length,0);await $('load-more').click();assert.equal(cards().length,192);await $('reset').click();return;}
  const first=observers.at(-1);assert.equal(first.target,$('load-sentinel'));assert.equal(first.options.rootMargin,'0px 0px 240px 0px');
  first.emit(false);assert.equal(cards().length,96);first.emit();assert.equal(cards().length,192);assert.equal(first.disconnected,true);
  first.emit();assert.equal(cards().length,192);
  const old=observers.at(-1);await input('common save');old.emit();assert.equal(cards().length,3);assert.equal(old.disconnected,true);
  await $('reset').click();const beforeOpen=observers.at(-1);await cards()[0].click();assert.equal(beforeOpen.disconnected,true);beforeOpen.emit();assert.equal(cards().length,96);
  await $('close').click();assert.notEqual(observers.at(-1),beforeOpen);
  for(let i=1;i<batchCount;i++)observers.at(-1).emit();
  assert.equal(cards().length,total);assert.equal(new Set(cards().map(c=>c.dataset.id)).size,total);assert.equal(observers.at(-1).disconnected,true);
  await input('no-such-icon-xyz');assert.equal($('load-sentinel').hidden,true);await $('reset').click();
 });
 await test('dialog buttons navigate the whole filtered list beyond loaded cards with bounded edges',async()=>{
  const opener=cards()[95];opener.focus();await opener.click();$('detail-next').focus();await $('detail-next').click();
  assert.equal($('detail-id').textContent,manifest.icons[96].id);assert.equal(cards().length,96);assert.equal(document.activeElement,$('detail-next'));
  for(let i=97;i<total;i++)await $('detail-next').click();
  assert.equal($('detail-id').textContent,manifest.icons.at(-1).id);assert.equal($('detail-next').disabled,true);assert.equal(document.activeElement,$('detail-previous'));
  await $('detail-next').dispatch('click');assert.equal($('detail-id').textContent,manifest.icons.at(-1).id);
  await $('close').click();assert.equal(document.activeElement,opener);
  await input('common save');await cards()[0].click();assert.equal($('detail-previous').disabled,true);await $('detail-previous').dispatch('click');assert.equal($('detail-id').textContent,'common-save');
  await $('detail-next').click();assert.equal($('detail-id').textContent,'common-save-as');await $('detail-next').click();assert.equal($('detail-id').textContent,'common-save-all');assert.equal($('detail-next').disabled,true);
  await $('close').click();await change('usage','model-tree');await input('cae-material-assignment');await change('language','ja');await cards()[0].click();
  assert.equal($('detail-position').textContent,'1 / 1 · 材料');assert.equal($('detail-previous').disabled,true);assert.equal($('detail-next').disabled,true);await $('close').click();await change('language','en');await $('reset').click();
 });
 await test('dialog arrow keys respect controls, modifiers, composition, Escape and focus',async()=>{
  const key=(value,extra={})=>{const event={key:value,target:document.activeElement,preventDefault(){this.prevented=true;},...extra};document.listeners.keydown[0](event);return event;};
  const opener=cards()[0];opener.focus();assert.equal(key('ArrowRight').prevented,undefined);await opener.click();$('copy').focus();
  assert.equal(key('ArrowRight').prevented,true);assert.equal($('detail-id').textContent,manifest.icons[1].id);assert.equal(document.activeElement,$('copy'));
  key('ArrowLeft');assert.equal($('detail-id').textContent,manifest.icons[0].id);key('ArrowLeft');assert.equal($('detail-id').textContent,manifest.icons[0].id);
  for(const tag of ['input','textarea','select']){new Element(tag).focus();assert.equal(key('ArrowRight').prevented,undefined);}
  const editable=new Element();editable.isContentEditable=true;editable.focus();assert.equal(key('ArrowRight').prevented,undefined);$('copy').focus();
  for(const prop of ['altKey','ctrlKey','metaKey','shiftKey','isComposing','defaultPrevented'])assert.equal(key('ArrowRight',{[prop]:true}).prevented,undefined);
  assert.equal($('detail-id').textContent,manifest.icons[0].id);
  assert.equal(key('Escape').prevented,undefined); // Native dialog owns cancel/Escape and focus trapping.
  $('detail').close();assert.equal(document.activeElement,opener);await $('reset').click();
 });
 await test('Japanese labels, preview size and background controls',async()=>{await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,manifest.icons[0].nameJa);await change('size','64');assert.equal(document.documentElement.style['--icon-size'],'64px');await backgrounds[1].click();assert.equal($('results').className,'icon-grid dark-bg');assert.equal(backgrounds[1].attributes['aria-pressed'],'true');await change('language','en');});
 await test('detail, bilingual purpose, repeated open, close, outside click and focus restore',async()=>{let card=cards()[0];card.focus();await card.click();assert.equal($('detail').open,true);assert.equal($('detail-name').textContent,manifest.icons[0].name);assert.equal($('detail-description').textContent,manifest.icons[0].description);assert.equal($('detail-preview').className,'detail-preview dark-bg');await card.click();assert.equal($('detail').open,true);await $('close').click();assert.equal($('detail').open,false);assert.equal(document.activeElement,card);await change('language','ja');card=cards()[0];await card.click();assert.equal($('detail-description').textContent,manifest.icons[0].descriptionJa);await $('detail').dispatch('click',{clientX:100,clientY:100});assert.equal($('detail').open,true);await $('detail').dispatch('click',{clientX:0,clientY:0});assert.equal($('detail').open,false);await change('language','en');});
 await test('copied SVG is standalone and matches the requested function',async()=>{await input('common-open-file');const card=cards()[0];assert.ok(card);await card.click();await $('copy').click();const item=manifest.icons.find(i=>i.id==='common-open-file');assert.ok(clipboard.at(-1).includes(`<title id="title">${item.name}</title>`));assert.doesNotMatch(clipboard.at(-1),/preview-\d+-/);assert.ok(clipboard.at(-1).includes(item.body));});
 await test('clipboard rejection, fallback failure and fallback exception',async()=>{navigator.clipboard.writeText=async()=>{throw Error('Denied');};await $('copy').click();assert.equal($('toast').textContent,'SVG copied');document.execCommand=()=>false;await $('copy').click();assert.match($('toast').textContent,/Clipboard unavailable/);document.execCommand=()=>{throw Error('Unsupported');};await $('copy').click();assert.match($('toast').textContent,/Clipboard unavailable/);assert.equal($('detail').children.filter(e=>e.tagName==='TEXTAREA').length,0);});
 await test('SVG download filename and blob contents',async()=>{await $('download').click();assert.equal(downloads.at(-1).name,'common-open-file.svg');assert.equal(blobs.at(-1).type,'image/svg+xml');assert.match(await blobs.at(-1).text(),/<svg xmlns=/);assert.ok((await blobs.at(-1).text()).includes(manifest.icons.find(i=>i.id==='common-open-file').body));await $('close').click();});
 await test('navigated selection drives SVG exports and preserves an in-flight PNG snapshot',async()=>{
  navigator.clipboard.writeText=async text=>clipboard.push(text);
  await input('common save');await cards()[0].click();await $('detail-next').click();await change('detail-theme','dark');
  const item=manifest.icons.find(i=>i.id==='common-save-as');const exact=fs.readFileSync(path.join(ROOT,item.variants.dark.file),'utf8');
  await $('copy').click();assert.equal(clipboard.at(-1),exact);await $('download').click();assert.equal(downloads.at(-1).name,'common-save-as.dark.svg');assert.equal(await blobs.at(-1).text(),exact);runTimers(1000);
  await change('png-size','64');png.mode='hold-image';const index=blobs.length;const pending=$('download-png').click();
  await $('detail-next').click();assert.equal($('detail-id').textContent,'common-save-all');await change('detail-theme','light');await change('png-size','16');
  png.mode='ok';png.pendingImages.shift()();await pending;
  assert.equal(downloads.at(-1).name,'common-save-as.dark.64.png');assert.equal(await blobs[index].text(),exact.replace('width="32" height="32"','width="64" height="64"'));
  assert.equal($('detail-id').textContent,'common-save-all');assert.equal($('download-png').disabled,false);runTimers(1000);
  await $('download-png').click();assert.equal(downloads.at(-1).name,'common-save-all.light.16.png');runTimers(1000);assert.equal(liveURLs.size,0);
  await $('close').click();await $('reset').click();
 });
 await test('both themes copy and download every exact standalone file without count inflation',async()=>{
  navigator.clipboard.writeText=async text=>clipboard.push(text);
  await $('reset').click();assert.equal(count(),419);
  for(const item of manifest.icons){
   await input(item.id);const card=cards().find(c=>c.dataset.id===item.id);assert.ok(card);await card.click();
   for(const theme of ['light','dark']){
    await change('detail-theme',theme);await $('copy').click();
    const exact=fs.readFileSync(path.join(ROOT,item.variants[theme].file),'utf8');
    assert.equal(clipboard.at(-1),exact,`${item.id} ${theme} copied bytes`);
    await $('download').click();assert.equal(await blobs.at(-1).text(),exact,`${item.id} ${theme} download bytes`);
    assert.equal(downloads.at(-1).name,item.id+(theme==='dark'?'.dark':'')+'.svg');
    assert.equal($('detail-file').textContent,item.variants[theme].file);
    if(theme==='dark')assert.match($('detail-theme-note').textContent,/#192c3c/);
   }
   await $('close').click();
  }
  await change('theme','light');await $('reset').click();assert.equal(count(),419);
 });
 await test('PNG controls offer seven exact sizes with an independent 32 px default',async()=>{
  const select=/<select id="png-size"[^>]*>([\s\S]*?)<\/select>/.exec(html)[1];
  assert.deepEqual([...select.matchAll(/value="(\d+)"/g)].map(m=>Number(m[1])),[16,24,32,48,64,128,256]);
  assert.match(select,/<option value="32" selected>/);
  assert.match(html,/aria-describedby="png-note"/);
  assert.match(html,/opaque cutouts are preserved/);
  assert.match(html,/<p id="detail-status"[^>]*role="status"[^>]*aria-live="polite"/);
  await change('size','64');await change('png-size','32');
  assert.equal(document.documentElement.style['--icon-size'],'64px');
  runTimers(1000);assert.equal(liveURLs.size,0);
 });
 await test('all 838 selected SVG variants feed transparent PNG exports at all seven sizes',async()=>{
  const before=downloads.length;
  for(const item of manifest.icons){
   await input(item.id);await cards().find(c=>c.dataset.id===item.id).click();
   for(const theme of ['light','dark']){
    await change('detail-theme',theme);
    const exact=fs.readFileSync(path.join(ROOT,item.variants[theme].file),'utf8');
    for(const size of [16,24,32,48,64,128,256]){
     await change('png-size',String(size));const index=blobs.length;
     await $('download-png').click();
     assert.equal(downloads.at(-1).name,`${item.id}.${theme}.${size}.png`);
     assert.equal(blobs[index].type,'image/svg+xml');
     assert.equal(await blobs[index].text(),exact.replace('width="32" height="32"',`width="${size}" height="${size}"`));
     assert.equal(blobs[index+1].type,'image/png');assert.ok(blobs[index+1].size);
     assert.equal(png.canvases.at(-1).draw.width,size);assert.equal(png.canvases.at(-1).draw.height,size);
     assert.equal(png.canvases.at(-1).width,0);assert.equal(png.canvases.at(-1).height,0);
     assert.equal(png.images.at(-1).onload,null);assert.equal(png.images.at(-1).onerror,null);
     assert.equal($('download-png').disabled,false);assert.equal($('download-png').attributes['aria-busy'],'false');
     assert.equal(timers.filter(t=>t.active&&t.delay===15000).length,0);
     runTimers(1000);assert.equal(liveURLs.size,0);
    }
   }
   await $('close').click();
  }
  assert.equal(downloads.length-before,5866);
  await change('theme','light');await $('reset').click();assert.equal(count(),419);
 });
 await test('PNG exports never include light, dark or checker preview backgrounds',async()=>{
  await input('common-info');await cards()[0].click();await change('png-size','64');
  for(const theme of ['light','dark']){
   await change('detail-theme',theme);const sources=[];
   for(const background of backgrounds){await background.click();const index=blobs.length;await $('download-png').click();sources.push(await blobs[index].text());runTimers(1000);}
   assert.equal(sources[0],sources[1]);assert.equal(sources[1],sources[2]);
   assert.doesNotMatch(sources[0],/preview-\d+-|checker|background/);
  }
  await $('close').click();
 });
 await test('PNG request snapshots survive repeated clicks, theme/size changes and reopening details',async()=>{
  await input('common-open-file');await cards()[0].click();await change('detail-theme','dark');await change('png-size','128');
  png.mode='hold-image';const index=blobs.length,before=downloads.length,imageCount=png.images.length;
  const pending=$('download-png').click();assert.equal($('download-png').disabled,true);assert.equal($('download-png').attributes['aria-busy'],'true');
  await $('download-png').dispatch('click');assert.equal(png.images.length,imageCount+1);
  await change('detail-theme','light');await change('png-size','16');await $('close').click();
  await input('cad-extrude');await cards()[0].click();await $('download-png').dispatch('click');
  png.mode='ok';png.pendingImages.shift()();await pending;
  assert.equal(downloads.length,before+1);assert.equal(downloads.at(-1).name,'common-open-file.dark.128.png');
  const item=manifest.icons.find(i=>i.id==='common-open-file');
  assert.equal(await blobs[index].text(),fs.readFileSync(path.join(ROOT,item.variants.dark.file),'utf8').replace('width="32" height="32"','width="128" height="128"'));
  runTimers(1000);assert.equal(liveURLs.size,0);assert.equal($('download-png').disabled,false);
  png.mode='hold-encode';const second=$('download-png').click();await Promise.resolve();
  assert.equal(png.pendingEncodes.length,1);await change('detail-theme','dark');await change('png-size','256');
  png.mode='ok';png.pendingEncodes.shift()();await second;
  assert.equal(downloads.at(-1).name,'cad-extrude.light.16.png');runTimers(1000);assert.equal(liveURLs.size,0);
  await $('download-png').click();assert.equal(downloads.at(-1).name,'cad-extrude.dark.256.png');runTimers(1000);
  await $('close').click();
 });
 await test('PNG errors produce no download and release URLs, Canvas memory and busy state',async()=>{
  await input('common-save');await cards()[0].click();await change('png-size','32');
  for(const mode of ['canvas-null','image-error','draw-error','encode-error','null-blob','empty-blob','wrong-mime','source-url-error','png-url-error','anchor-error','image-hang','encode-hang']){
   png.mode=mode;const before=downloads.length;const pending=$('download-png').click();
   if(mode.endsWith('-hang')){await Promise.resolve();runTimers(15000);}
   await pending;assert.equal(downloads.length,before,mode);assert.match($('toast').textContent,/PNG export failed/,mode);
   assert.equal($('download-png').disabled,false);assert.equal($('download-png').attributes['aria-busy'],'false');
   assert.equal($('download-png').textContent,'Download PNG ↓');
   assert.match($('detail-status').textContent,/PNG export failed/,mode);
   assert.equal(png.canvases.at(-1).width,0);assert.equal(png.canvases.at(-1).height,0);
   assert.equal(document.body.children.filter(e=>e.tagName==='A').length,0);
   runTimers(1000);assert.equal(liveURLs.size,0,mode);assert.equal(timers.filter(t=>t.active&&t.delay===15000).length,0);
  }
  png.mode='ok';await $('download-png').click();assert.match($('toast').textContent,/transparent PNG download started/);runTimers(1000);
  await $('close').click();
 });
 await test('late PNG decode or encode after timeout cannot download or disturb a retry',async()=>{
  await input('common-info');await cards()[0].click();await change('png-size','48');
  for(const mode of ['hold-image','hold-encode']){
   png.mode=mode;const before=downloads.length;const pending=$('download-png').click();await Promise.resolve();
   runTimers(15000);await pending;assert.equal(downloads.length,before);assert.equal(liveURLs.size,0);
   png.mode='ok';await $('download-png').click();assert.equal(downloads.length,before+1);
   if(mode==='hold-image')png.pendingImages.shift()();else png.pendingEncodes.shift()();
   await Promise.resolve();assert.equal(downloads.length,before+1);assert.equal($('download-png').disabled,false);
   runTimers(1000);assert.equal(liveURLs.size,0);
  }
  await $('close').click();
 });
 await test('PNG invalid sizes are rejected before allocating or downloading',async()=>{
  await input('common-info');await cards()[0].click();const before=downloads.length,imageCount=png.images.length;
  for(const size of ['','0','-1','33','4096','bad']){await change('png-size',size);await $('download-png').click();assert.match($('toast').textContent,/Choose a PNG size/);}
  assert.equal(downloads.length,before);assert.equal(png.images.length,imageCount);assert.equal(liveURLs.size,0);
  await change('png-size','32');await $('close').click();await $('reset').click();
 });
 await test('slash shortcut respects input and open dialog',async()=>{document.activeElement=document.body;let e={key:'/',preventDefault(){this.prevented=true;}};document.listeners.keydown[0](e);assert.equal(e.prevented,true);assert.equal(document.activeElement,$('search'));e={key:'/',preventDefault(){this.prevented=true;}};document.listeners.keydown[0](e);assert.equal(e.prevented,undefined);await cards()[0].click();document.activeElement=document.body;e={key:'/',preventDefault(){this.prevented=true;}};document.listeners.keydown[0](e);assert.equal(e.prevented,undefined);await $('close').click();});
 await test('bulk controls inherit theme, describe complete results and reject empty filters',async()=>{
  await $('reset').click();await change('theme','dark');$('bulk-download').focus();await $('bulk-download').click();
  assert.equal($('bulk').open,true);assert.equal($('bulk-theme').value,'dark');assert.equal($('bulk-scope').value,'filtered');
  assert.match($('bulk-summary').textContent,/419 icons · Dark SVG · one ZIP/);assert.equal($('bulk-size-label').hidden,true);
  assert.match($('bulk-scope-all').textContent,/419/);assert.match($('bulk-scope-filtered').textContent,/419/);
  const select=/<select id="bulk-size"[^>]*>([\s\S]*?)<\/select>/.exec(html)[1];
  assert.deepEqual([...select.matchAll(/value="(\d+)"/g)].map(m=>Number(m[1])),[16,24,32,48,64,128,256]);assert.match(select,/<option value="32" selected>/);
  await $('bulk-download').dispatch('click');assert.equal($('bulk').open,true);
  await $('bulk-close').click();assert.equal(document.activeElement,$('bulk-download'));
  await input('no-such-icon-xyz');assert.equal($('bulk-download').disabled,false);await $('bulk-download').click();assert.equal($('bulk').open,true);assert.equal($('bulk-start').disabled,true);await $('bulk-close').click();
  await $('reset').click();await $('bulk-download').click();await input('no-such-icon-xyz');
  assert.equal($('bulk-start').disabled,true);const before=downloads.length;await $('bulk-start').dispatch('click');assert.equal(downloads.length,before);assert.match($('bulk-status').textContent,/No matching icons/);
  await change('bulk-scope','all');assert.equal($('bulk-start').disabled,false);await $('bulk-close').click();await $('reset').click();
 });
 await test('bulk SVG ZIP contains every exact file in both themes without loading more cards',async()=>{
  const {readZip}=require('./zip_helpers.js');
  await change('theme','light');await $('reset').click();assert.equal(cards().length,96);
  for(const theme of ['light','dark']){
   await $('bulk-download').click();await change('bulk-format','svg');await change('bulk-theme',theme);await change('bulk-scope','all');
   const before=downloads.length;await $('bulk-start').click();assert.equal(downloads.length,before+1);assert.equal(cards().length,96);
   assert.equal(downloads.at(-1).name,`cax-icons-all-419.${theme}.svg.zip`);assert.equal(blobs.at(-1).type,'application/zip');
   const entries=await readZip(blobs.at(-1));assert.equal(entries.size,419);
   for(const item of manifest.icons)assert.deepEqual(entries.get(item.id+(theme==='dark'?'.dark':'')+'.svg'),fs.readFileSync(path.join(ROOT,item.variants[theme].file)));
   assert.match($('bulk-status').textContent,/ZIP download started: 419/);assert.equal($('bulk-start').disabled,false);assert.equal($('bulk-start').attributes['aria-busy'],'false');
   await $('bulk-close').click();runTimers(1000);assert.equal(liveURLs.size,0);
  }
 });
 await test('bulk filtered selection respects category, usage and query while all scope ignores them',async()=>{
  const {readZip}=require('./zip_helpers.js');
  await input('common save');await $('bulk-download').click();await change('bulk-theme','light');
  await $('bulk-start').click();let entries=await readZip(blobs.at(-1));assert.deepEqual([...entries.keys()],['common-save.svg','common-save-as.svg','common-save-all.svg']);
  assert.equal(downloads.at(-1).name,'cax-icons-filtered-3.light.svg.zip');
  await change('bulk-scope','all');await $('bulk-start').click();assert.equal((await readZip(blobs.at(-1))).size,419);await $('bulk-close').click();
  await $('reset').click();await change('usage','model-tree');await document.querySelectorAll('.category').find(e=>e.dataset.category==='CAD').click();await input('cae-material-assignment');
  await $('bulk-download').click();await $('bulk-start').click();entries=await readZip(blobs.at(-1));assert.deepEqual([...entries.keys()],['cae-material-assignment.svg']);
  await $('bulk-close').click();await $('reset').click();await change('usage','model-tree');assert.equal(cards().length,96);
  await $('bulk-download').click();await $('bulk-start').click();entries=await readZip(blobs.at(-1));assert.equal(entries.size,186);assert.equal(cards().length,96);
  await $('bulk-close').click();await $('reset').click();runTimers(1000);assert.equal(liveURLs.size,0);
 });
 await test('bulk PNG ZIP captures all 419 images per theme and all seven supported sizes',async()=>{
  const {readZip}=require('./zip_helpers.js');
  for(const theme of ['light','dark']){
   await $('bulk-download').click();await change('bulk-format','png');await change('bulk-theme',theme);await change('bulk-size','32');await change('bulk-scope','all');
   assert.equal($('bulk-size-label').hidden,false);assert.equal($('bulk-size').disabled,false);
   const before=downloads.length,imageStart=png.images.length;await $('bulk-start').click();assert.equal(downloads.length,before+1);assert.equal(png.images.length-imageStart,419);
   const entries=await readZip(blobs.at(-1));assert.equal(entries.size,419);
   for(const item of manifest.icons)assert.equal(entries.get(`${item.id}.${theme}.32.png`).toString(),'mock PNG pixels');
   assert.equal(downloads.at(-1).name,`cax-icons-all-419.${theme}.32.png.zip`);await $('bulk-close').click();runTimers(1000);assert.equal(liveURLs.size,0);
  }
  await input('common-info');await $('bulk-download').click();
  for(const theme of ['light','dark'])for(const size of [16,24,32,48,64,128,256]){
   await change('bulk-theme',theme);await change('bulk-size',String(size));await backgrounds[size%3].click();const start=blobs.length;
   await $('bulk-start').click();const entries=await readZip(blobs.at(-1));assert.deepEqual([...entries.keys()],[`common-info.${theme}.${size}.png`]);
   const item=manifest.icons.find(i=>i.id==='common-info');const exact=fs.readFileSync(path.join(ROOT,item.variants[theme].file),'utf8');
   assert.equal(await blobs[start].text(),exact.replace('width="32" height="32"',`width="${size}" height="${size}"`));
   assert.equal(png.canvases.at(-1).draw.width,size);assert.equal(png.canvases.at(-1).width,0);assert.equal(png.images.at(-1).onload,null);
   runTimers(1000);assert.equal(liveURLs.size,0);
  }
  await $('bulk-close').click();await $('reset').click();
 });
 await test('bulk snapshot and repeated-click guard survive changes to filters, theme, format and size',async()=>{
  const {readZip}=require('./zip_helpers.js');
  const waitFor=async predicate=>{for(let i=0;i<1000&&!predicate();i++)await new Promise(resolve=>setTimeout(resolve,1));assert.ok(predicate());};
  await input('common save');await $('bulk-download').click();await change('bulk-theme','dark');await change('bulk-size','128');
  png.mode='hold-image';const before=downloads.length,imageCount=png.images.length,blobStart=blobs.length;const pending=$('bulk-start').click();
  assert.equal($('bulk-start').disabled,true);assert.equal($('bulk-start').attributes['aria-busy'],'true');assert.equal(document.activeElement,$('bulk-cancel'));
  await waitFor(()=>png.pendingImages.length>0);await $('bulk-start').dispatch('click');assert.equal(png.images.length,imageCount+1);
  for(const id of ['bulk-scope','bulk-theme','bulk-format','bulk-size'])assert.equal($(id).disabled,true);
  await input('cad-extrude');await change('theme','light');await change('bulk-size','16');await change('bulk-theme','light');await change('bulk-format','svg');await change('bulk-scope','all');
  png.mode='ok';png.pendingImages.shift()();await pending;
  assert.equal(downloads.length,before+1);assert.equal(downloads.at(-1).name,'cax-icons-filtered-3.dark.128.png.zip');
  const entries=await readZip(blobs.at(-1));assert.deepEqual([...entries.keys()],['common-save.dark.128.png','common-save-as.dark.128.png','common-save-all.dark.128.png']);
  const sourceBlobs=blobs.slice(blobStart).filter(blob=>blob.type==='image/svg+xml');assert.equal(sourceBlobs.length,3);
  for(const [i,id] of ['common-save','common-save-as','common-save-all'].entries())assert.equal(await sourceBlobs[i].text(),fs.readFileSync(path.join(ROOT,'icons-dark',id+'.svg'),'utf8').replace('width="32" height="32"','width="128" height="128"'));
  assert.equal($('bulk-start').disabled,false);assert.equal($('bulk-cancel').hidden,true);await $('bulk-close').click();await $('reset').click();runTimers(1000);assert.equal(liveURLs.size,0);
 });
 await test('bulk cancellation before work, during decode/encode and before final download is atomic',async()=>{
  const waitFor=async predicate=>{for(let i=0;i<1000&&!predicate();i++)await new Promise(resolve=>setTimeout(resolve,1));assert.ok(predicate());};
  await input('common save');await $('bulk-download').click();await change('bulk-format','svg');const before=downloads.length;
  let pending=$('bulk-start').click();await $('bulk-cancel').click();await pending;assert.equal(downloads.length,before);assert.match($('bulk-status').textContent,/cancelled/);
  await change('bulk-format','png');await change('bulk-size','32');
  for(const mode of ['hold-image','hold-encode']){
   png.mode=mode;pending=$('bulk-start').click();await waitFor(()=>mode==='hold-image'?png.pendingImages.length>0:png.pendingEncodes.length>0);
   await $('bulk-cancel').click();await pending;assert.equal(downloads.length,before);assert.equal(liveURLs.size,0);assert.equal($('bulk-start').disabled,false);
   assert.equal(png.canvases.at(-1).width,0);assert.equal(png.images.at(-1).onload,null);assert.equal(timers.filter(t=>t.active&&t.delay===15000).length,0);
   png.mode='ok';const retry=$('bulk-start').click();if(mode==='hold-image')png.pendingImages.shift()();else png.pendingEncodes.shift()();
   await $('bulk-cancel').click();await retry;assert.equal(downloads.length,before);
  }
  png.mode='ok';pending=$('bulk-start').click();await waitFor(()=>$('bulk-progress').value===3);await $('bulk-cancel').click();await pending;assert.equal(downloads.length,before);
  await $('bulk-close').click();await $('reset').click();
 });
 await test('bulk Escape, close and backdrop cancel pending work, guard shortcuts and restore focus',async()=>{
  const waitFor=async predicate=>{for(let i=0;i<1000&&!predicate();i++)await new Promise(resolve=>setTimeout(resolve,1));assert.ok(predicate());};
  await input('common-info');
  for(const close of ['escape','button','backdrop']){
   $('bulk-download').focus();await $('bulk-download').click();const before=downloads.length;
   const event={key:'/',target:$('bulk-start'),preventDefault(){this.prevented=true;}};document.listeners.keydown[0](event);assert.equal(event.prevented,undefined);
   png.mode='hold-image';const pending=$('bulk-start').click();await waitFor(()=>png.pendingImages.length>0);
   if(close==='escape'){await $('bulk').dispatch('cancel');$('bulk').close();}
   else if(close==='button')await $('bulk-close').click();
   else{await $('bulk').dispatch('click',{clientX:100,clientY:100});assert.equal($('bulk').open,true);await $('bulk').dispatch('click',{clientX:0,clientY:0});}
   await pending;png.mode='ok';png.pendingImages.shift()();await Promise.resolve();
   assert.equal($('bulk').open,false);assert.equal(document.activeElement,$('bulk-download'));assert.equal(downloads.length,before);assert.equal(liveURLs.size,0);
   await $('bulk-download').click();await $('bulk-start').click();assert.equal(downloads.length,before+1);await $('bulk-close').click();runTimers(1000);
  }
  await $('reset').click();
  if(window.IntersectionObserver){const old=observers.at(-1);await $('bulk-download').click();assert.equal(old.disconnected,true);old.emit();assert.equal(cards().length,96);await $('bulk-close').click();assert.notEqual(observers.at(-1),old);}
 });
 await test('bulk conversion and ZIP failures never download partial files and allow retry',async()=>{
  const waitFor=async predicate=>{for(let i=0;i<1000&&!predicate();i++)await new Promise(resolve=>setTimeout(resolve,1));assert.ok(predicate());};
  await input('common save');await $('bulk-download').click();await change('bulk-format','png');
  const before=downloads.length;png.mode='hold-image';let pending=$('bulk-start').click();await waitFor(()=>png.pendingImages.length>0);png.pendingImages.shift()();await waitFor(()=>png.pendingImages.length>0);png.mode='image-error';png.pendingImages.shift()();await pending;
  assert.equal(downloads.length,before);assert.match($('bulk-status').textContent,/failed at common-save-as/);assert.equal(liveURLs.size,0);
  for(const mode of ['canvas-null','draw-error','encode-error','null-blob','empty-blob','wrong-mime','source-url-error','zip-url-error','anchor-error','image-hang','encode-hang']){
   png.mode=mode;pending=$('bulk-start').click();
   if(mode.endsWith('-hang')){await waitFor(()=>timers.some(t=>t.active&&t.delay===15000));if(mode==='encode-hang')await waitFor(()=>png.canvases.at(-1).draw);runTimers(15000);}
   await pending;assert.equal(downloads.length,before,mode);assert.match($('bulk-status').textContent,/No partial ZIP downloaded/,mode);assert.equal($('bulk-start').disabled,false);assert.equal($('bulk-start').attributes['aria-busy'],'false');
   runTimers(1000);assert.equal(liveURLs.size,0,mode);assert.equal(timers.filter(t=>t.active&&t.delay===15000).length,0);
  }
  png.mode='ok';const original=window.CAX_ZIP.Zip.prototype.add;let added=0;window.CAX_ZIP.Zip.prototype.add=function(...args){if(++added===2)throw Error('ZIP failure');return original.apply(this,args);};
  await $('bulk-start').click();window.CAX_ZIP.Zip.prototype.add=original;assert.equal(downloads.length,before);assert.match($('bulk-status').textContent,/No partial ZIP/);
  await $('bulk-start').click();assert.equal(downloads.length,before+1);await $('bulk-close').click();runTimers(1000);assert.equal(liveURLs.size,0);await $('reset').click();
 });
 await test('bulk invalid options allocate nothing and cannot download',async()=>{
  await $('bulk-download').click();await change('bulk-format','png');const before=downloads.length,imageCount=png.images.length;
  for(const [id,value] of [['bulk-size','4096'],['bulk-theme','bad'],['bulk-format','bad'],['bulk-scope','bad']]){
   const original=$(id).value;await change(id,value);await $('bulk-start').click();assert.match($('bulk-status').textContent,/Choose a scope/);await change(id,original);
  }
  assert.equal(downloads.length,before);assert.equal(png.images.length,imageCount);assert.equal(liveURLs.size,0);await $('bulk-close').click();
 });
 console.log(`\n${tests.length} application interaction groups passed (script-level DOM harness, not a browser).`);
})().catch(error=>{console.error(error);process.exitCode=1;});
