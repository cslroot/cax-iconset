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
class Element {
 constructor(tag='div') {this.tagName=tag.toUpperCase();this.children=[];this.dataset={};this.attributes={};this.listeners={};this.className='';this.textContent='';this.innerHTML='';this.hidden=false;this.disabled=false;this.open=false;this.value='';this.parent=null;this.isConnected=true;this.style={setProperty:(k,v)=>this.style[k]=v};this.classList={add:c=>this.classList.toggle(c,true),remove:c=>this.classList.toggle(c,false),toggle:(c,on)=>{const classes=new Set(this.className.split(/\s+/).filter(Boolean));if(on)classes.add(c);else classes.delete(c);this.className=[...classes].join(' ');}};}
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
 click(){if(this.tagName==='A'){downloads.push({href:this.href,name:this.download});return;}if(!this.disabled)return this.dispatch('click');}
}
for(const match of html.matchAll(/<([a-z][a-z0-9]*)\b[^>]*\bid="([^"]+)"[^>]*>/g)){const e=new Element(match[1]);e.id=match[2];e.hidden=/\bhidden\b/.test(match[0]);e.className=/class="([^"]+)"/.exec(match[0])?.[1]||'';ids.set(e.id,e);}
const all=new Element('button');all.dataset.category='all';all.className='category active';
const backgrounds=['light','dark','grid'].map(background=>{const e=new Element('button');e.dataset.background=background;return e;});
document={body:new Element('body'),documentElement:new Element('html'),activeElement:new Element('body'),listeners:{},getElementById:id=>{assert.ok(ids.has(id),'Missing DOM ID '+id);return ids.get(id);},createElement:tag=>new Element(tag),querySelectorAll:selector=>{if(selector==='.category')return [all,...ids.get('categories').children];if(selector==='[data-background]')return backgrounds;throw Error('Unhandled selector '+selector);},addEventListener(type,fn){(this.listeners[type]??=[]).push(fn);},execCommand:()=>true};
const clipboard=[];
const blobs=[];
const timers=[];
const navigator={clipboard:{writeText:async text=>clipboard.push(text)}};
const window={isSecureContext:true};
const context=vm.createContext({document,window,navigator,Blob,URL:{createObjectURL:blob=>{blobs.push(blob);return 'blob:test-'+blobs.length;},revokeObjectURL:()=>{}},setTimeout:fn=>{timers.push(fn);return timers.length;},console});
vm.runInContext(fs.readFileSync(path.join(ROOT,'catalog.js'),'utf8'),context);
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
 const pageCount=Math.ceil(total/96);
 await test('initial count, bounded first page and category controls',async()=>{assert.equal(count(),total);assert.equal(cards().length,96);assert.equal($('page-label').textContent,`1 / ${pageCount}`);assert.equal($('previous').disabled,true);assert.equal(document.querySelectorAll('.category').length,7);assert.match($('collection-scope').textContent,/common application symbols/);assert.ok(!html.includes('Context variants'));assert.ok(!ids.has('kind'));});
 await test('English, Japanese, AND and Unicode-normalized searches',async()=>{await input('common save');assert.deepEqual(cards().map(c=>c.dataset.id),['common-save','common-save-as','common-save-all']);await input('名前を付けて保存');assert.equal(cards()[0].dataset.id,'common-save-as');await input('ファイル 開く');assert.ok(cards().some(c=>c.dataset.id==='common-open-file'));await input('ＣＡＤ');const normalized=count();await input('CAD');assert.equal(count(),normalized);assert.ok(count()>=20);await input('no-such-icon-xyz');assert.equal(count(),0);assert.equal($('empty').hidden,false);assert.equal($('next').disabled,true);await $('clear').click();assert.equal(count(),total);assert.equal($('empty').hidden,true);assert.equal(document.activeElement,$('search'));});
 await test('separate common and engineering categories and query intersections',async()=>{for(const category of ['Common','CAD','CAM','CAE','CMM','OLP']){await document.querySelectorAll('.category').find(e=>e.dataset.category===category).click();assert.equal(count(),manifest.categories[category]);}await document.querySelectorAll('.category').find(e=>e.dataset.category==='Common').click();await input('save');assert.equal(count(),3);await document.querySelectorAll('.category').find(e=>e.dataset.category==='CAD').click();assert.equal(count(),0);await $('reset').click();assert.equal(count(),total);});
 await test('pagination bounds, back navigation and filter page reset',async()=>{for(let i=1;i<pageCount;i++)await $('next').click();assert.equal($('page-label').textContent,`${pageCount} / ${pageCount}`);assert.equal(cards().length,total-96*(pageCount-1));assert.equal($('next').disabled,true);await $('next').click();assert.equal(cards().length,total-96*(pageCount-1));await $('previous').click();assert.equal(cards().length,96);await input('cad-extrude');assert.equal($('page-label').textContent,'1 / 1');await $('reset').click();});
 await test('Japanese labels, preview size and background controls',async()=>{await change('language','ja');assert.equal(cards()[0].children.at(-1).textContent,manifest.icons[0].nameJa);await change('size','64');assert.equal(document.documentElement.style['--icon-size'],'64px');await backgrounds[1].click();assert.equal($('results').className,'icon-grid dark-bg');assert.equal(backgrounds[1].attributes['aria-pressed'],'true');await change('language','en');});
 await test('detail, bilingual purpose, repeated open, close, outside click and focus restore',async()=>{let card=cards()[0];card.focus();await card.click();assert.equal($('detail').open,true);assert.equal($('detail-name').textContent,manifest.icons[0].name);assert.equal($('detail-description').textContent,manifest.icons[0].description);assert.equal($('detail-preview').className,'detail-preview dark-bg');await card.click();assert.equal($('detail').open,true);await $('close').click();assert.equal($('detail').open,false);assert.equal(document.activeElement,card);await change('language','ja');card=cards()[0];await card.click();assert.equal($('detail-description').textContent,manifest.icons[0].descriptionJa);await $('detail').dispatch('click',{clientX:100,clientY:100});assert.equal($('detail').open,true);await $('detail').dispatch('click',{clientX:0,clientY:0});assert.equal($('detail').open,false);await change('language','en');});
 await test('copied SVG is standalone and matches the requested function',async()=>{await input('common-open-file');const card=cards()[0];assert.ok(card);await card.click();await $('copy').click();const item=manifest.icons.find(i=>i.id==='common-open-file');assert.ok(clipboard.at(-1).includes(`<title>${item.name}</title>`));assert.doesNotMatch(clipboard.at(-1),/preview-\d+-/);assert.ok(clipboard.at(-1).includes(item.body));});
 await test('clipboard rejection, fallback failure and fallback exception',async()=>{navigator.clipboard.writeText=async()=>{throw Error('Denied');};await $('copy').click();assert.equal($('toast').textContent,'SVG copied');document.execCommand=()=>false;await $('copy').click();assert.match($('toast').textContent,/Clipboard unavailable/);document.execCommand=()=>{throw Error('Unsupported');};await $('copy').click();assert.match($('toast').textContent,/Clipboard unavailable/);assert.equal($('detail').children.filter(e=>e.tagName==='TEXTAREA').length,0);});
 await test('SVG download filename and blob contents',async()=>{await $('download').click();assert.equal(downloads.at(-1).name,'common-open-file.svg');assert.equal(blobs.at(-1).type,'image/svg+xml');assert.match(await blobs.at(-1).text(),/<svg xmlns=/);assert.ok((await blobs.at(-1).text()).includes(manifest.icons.find(i=>i.id==='common-open-file').body));await $('close').click();});
 await test('slash shortcut respects input and open dialog',async()=>{document.activeElement=document.body;let e={key:'/',preventDefault(){this.prevented=true;}};document.listeners.keydown[0](e);assert.equal(e.prevented,true);assert.equal(document.activeElement,$('search'));e={key:'/',preventDefault(){this.prevented=true;}};document.listeners.keydown[0](e);assert.equal(e.prevented,undefined);await cards()[0].click();document.activeElement=document.body;e={key:'/',preventDefault(){this.prevented=true;}};document.listeners.keydown[0](e);assert.equal(e.prevented,undefined);await $('close').click();});
 console.log(`\n${tests.length} application interaction groups passed (script-level DOM harness, not a browser).`);
})().catch(error=>{console.error(error);process.exitCode=1;});
