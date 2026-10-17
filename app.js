'use strict';
(() => {
const $ = id => document.getElementById(id);
const catalog = window.CAX_CATALOG;
const icons = catalog.icons;
const categories = {
 CAD: ['Design & modeling','◇'], CAM: ['Manufacturing','⌁'], CAE: ['Simulation','⌗'],
 CMM: ['Measurement','⊙'], OLP: ['Robotics / OLP','⌘'], Common: ['Common tools','⊞']
};
const state = {category:'all',query:'',kind:'all',page:1,language:'en',background:'light',selected:null};
const PAGE_SIZE = 96;
let lastFocus;
let previewSerial = 0;
function svg(item, title=false) {
 const safeTitle = item.name.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
 // A card and its open detail can coexist. Scope paint-server IDs per preview.
 const prefix = title ? '' : `preview-${++previewSerial}-`;
 const body = title ? item.body : item.body.replace(/id="([^"]+)"/g,(_,id)=>`id="${prefix}${id}"`).replace(/url\(#([^)]+)\)/g,(_,id)=>`url(#${prefix}${id})`);
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"${title?' role="img"':' aria-hidden="true"'}>${title?`<title>${safeTitle}</title>`:''}${body}</svg>`;
}
function name(item) {return state.language === 'ja' ? item.nameJa : item.name;}
function filter() {
 const words = state.query.normalize('NFKC').toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
 return icons.filter(item => (state.category === 'all' || (item.categories || [item.category]).includes(state.category))
  && (state.kind === 'all' || item.kind === state.kind)
  && words.every(word => item.searchText.includes(word)));
}
function render() {
 const matches = filter();
 const pages = Math.max(1, Math.ceil(matches.length / PAGE_SIZE));
 state.page = Math.max(1,Math.min(state.page,pages));
 $('results').replaceChildren();
 for(const item of matches.slice((state.page-1)*PAGE_SIZE,state.page*PAGE_SIZE)) {
  const button = document.createElement('button'); button.type='button'; button.className='icon-card';
  button.dataset.id=item.id; button.setAttribute('aria-label',`${name(item)} · ${item.category} · ${item.kind}`);
  button.innerHTML=svg(item);
  const small=document.createElement('small');small.textContent=item.category; button.append(small);
  const label=document.createElement('span');label.textContent=name(item);button.append(label);
  button.addEventListener('click',()=>openDetail(item)); $('results').append(button);
 }
 $('section-title').textContent=state.category==='all'?'All icons':state.category;
 $('result-count').textContent=`${matches.length.toLocaleString()} icons`;
 $('page-label').textContent=`${state.page} / ${pages}`;
 $('previous').disabled=state.page===1;$('next').disabled=state.page===pages;
 $('empty').hidden=!!matches.length;
 $('clear').hidden=!state.query;
 document.querySelectorAll('.category').forEach(b=>{const active=b.dataset.category===state.category;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
}
function openDetail(item) {
 lastFocus=document.activeElement;state.selected=item;
 $('detail-preview').innerHTML=svg(item);$('detail-preview').className='detail-preview '+state.background+'-bg';
 $('detail-name').textContent=name(item);$('detail-ja').textContent=state.language==='en'?item.nameJa:item.name;
 $('detail-id').textContent=item.id;$('detail-category').textContent=`${item.category} / ${item.kind==='core'?'CORE SYMBOL':'CONTEXT VARIANT'}`;
 $('detail-description').textContent=item.description || 'Original engineering symbol, drawn on a consistent rounded 32 px grid.';
 $('detail-tags').replaceChildren();item.tags.filter(Boolean).forEach(tag=>{const el=document.createElement('span');el.textContent=tag;$('detail-tags').append(el);});
 if(!$('detail').open) $('detail').showModal();
}
function closeDetail(){if($('detail').open)$('detail').close();}
function toast(text){$('toast').textContent=text;$('toast').classList.add('visible');setTimeout(()=>$('toast').classList.remove('visible'),2500);}
function fallbackCopy(text){const area=document.createElement('textarea');area.value=text;area.style.position='fixed';area.style.opacity='0';$('detail').append(area);area.focus();area.select();try{return document.execCommand('copy');}catch{return false;}finally{area.remove();$('copy').focus();}}
icons.forEach(item=>{item.searchText=[item.id,item.name,item.nameJa,item.category,item.family,...item.tags].join(' ').normalize('NFKC').toLocaleLowerCase();});
$('all-count').textContent=icons.length.toLocaleString();$('hero-count').textContent=icons.length.toLocaleString();
$('collection-scope').textContent=`${catalog.counts.core.toLocaleString()} core symbols + ${catalog.counts.variant.toLocaleString()} geometry / process context variants. Shared symbols count once in the total.`;
for(const [category,[label,mark]] of Object.entries(categories)){
 const count=icons.filter(item=>(item.categories || [item.category]).includes(category)).length;if(!count)continue;
 const button=document.createElement('button');button.className='category';button.dataset.category=category;button.title=label;
 button.innerHTML=`<span class="cat-mark">${mark}</span><span>${category}</span><span class="count">${count.toLocaleString()}</span>`;$('categories').append(button);
}
for(const id of ['cad-extrude','cam-end-mill','cae-tetrahedral-mesh','cmm-tactile-probe','olp-robot-arm','cad-fillet']){const item=icons.find(i=>i.id===id);if(item){const div=document.createElement('div');div.innerHTML=svg(item);$('hero-icons').append(div);}}
document.querySelectorAll('.category').forEach(button=>button.addEventListener('click',()=>{state.category=button.dataset.category;state.page=1;render();}));
$('search').addEventListener('input',e=>{state.query=e.target.value;state.page=1;render();});
$('clear').addEventListener('click',()=>{state.query='';$('search').value='';state.page=1;render();$('search').focus();});
$('kind').addEventListener('change',e=>{state.kind=e.target.value;state.page=1;render();});
$('language').addEventListener('change',e=>{state.language=e.target.value;render();});
$('size').addEventListener('change',e=>document.documentElement.style.setProperty('--icon-size',e.target.value+'px'));
document.querySelectorAll('[data-background]').forEach(button=>button.addEventListener('click',()=>{state.background=button.dataset.background;$('results').className='icon-grid '+state.background+'-bg';document.querySelectorAll('[data-background]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));}));
for(const [id,step] of [['previous',-1],['next',1]])$(id).addEventListener('click',()=>{state.page+=step;render();$('results').scrollIntoView({block:'start',behavior:'auto'});});
$('reset').addEventListener('click',()=>{state.category='all';state.kind='all';state.query='';state.page=1;$('search').value='';$('kind').value='all';render();});
$('close').addEventListener('click',closeDetail);
$('detail').addEventListener('click',event=>{if(event.target===$('detail')){const r=$('detail').getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)closeDetail();}});
$('detail').addEventListener('close',()=>{if(lastFocus?.isConnected)lastFocus.focus();});
$('copy').addEventListener('click',async()=>{const text=svg(state.selected,true);try{if(navigator.clipboard&&window.isSecureContext)await navigator.clipboard.writeText(text);else if(!fallbackCopy(text))throw Error('Clipboard blocked');toast('SVG copied');}catch{if(fallbackCopy(text))toast('SVG copied');else toast('Clipboard unavailable. Use Download SVG.');}});
$('download').addEventListener('click',()=>{const item=state.selected;const blob=new Blob([svg(item,true)+'\n'],{type:'image/svg+xml'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=item.id+'.svg';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);toast('SVG download started');});
document.addEventListener('keydown',event=>{if(event.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)&&!$('detail').open){event.preventDefault();$('search').focus();}});
render();
})();
