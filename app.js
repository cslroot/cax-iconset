'use strict';
(() => {
const $ = id => document.getElementById(id);
const catalog = window.CAX_CATALOG;
const icons = catalog.icons;
const categories = {
 Common: ['Common application tools','⊞'], CAD: ['Design & modeling','◇'], CAM: ['Manufacturing','⌁'], CAE: ['Simulation','⌗'],
 CMM: ['Measurement','⊙'], OLP: ['Robotics / OLP','⌘']
};
const state = {category:'all',usage:'all',query:'',page:1,language:'en',background:'light',theme:'light',selected:null};
const PAGE_SIZE = 96;
let lastFocus;
let previewSerial = 0;
function svg(item, exported=false, theme=state.theme) {
 const safeTitle = item.name.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#x27;');
 const variant = item.variants[theme];
 const sourceBody = variant.body || item.body;
 // A card and its open detail can coexist. Scope local references per preview.
 const prefix = exported ? '' : `preview-${++previewSerial}-`;
 const body = exported ? sourceBody : sourceBody.replace(/id="([^"]+)"/g,(_,id)=>`id="${prefix}${id}"`).replace(/url\(#([^)]+)\)/g,(_,id)=>`url(#${prefix}${id})`);
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" fill="none" stroke="${catalog.themes[theme].palette.ink}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"${exported?' role="img" aria-labelledby="title"':' aria-hidden="true"'}>${exported?`<title id="title">${safeTitle}</title>`:''}${body}</svg>${exported?'\n':''}`;
}
function detailPreview() {
 const theme = catalog.themes[state.theme];
 $('detail-preview').innerHTML=svg(state.selected);
 $('detail-preview').className='detail-preview '+state.background+'-bg';
 $('detail-theme').value=state.theme;
 $('detail-file').textContent=state.selected.variants[state.theme].file;
 $('detail-theme-note').textContent=state.theme==='dark'
  ? `Dark SVG. Opaque cutouts use ${theme.palette.cutout}; they remain visible on other surfaces.`
  : 'Light SVG. Opaque cutouts use white. Preview, copy and download use this variant.';
}
function setTheme(theme) {
 if(!Object.hasOwn(catalog.themes,theme))return;
 const openerId=lastFocus?.dataset.id;
 state.theme=theme;$('theme').value=theme;render();
 if($('detail').open){
  if(openerId)lastFocus=Array.from($('results').children).find(card=>card.dataset.id===openerId)||$('theme');
  detailPreview();
 }
}
function name(item) {return state.usage==='model-tree' ? (state.language==='ja'?item.nodeNameJa:item.nodeName) : (state.language==='ja'?item.nameJa:item.name);}
function filter() {
 const words = state.query.normalize('NFKC').toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
 return icons.filter(item => (state.category === 'all' || (item.categories || [item.category]).includes(state.category))
  && (state.usage === 'all' || item.usages.includes(state.usage))
  && words.every(word => item.searchText.includes(word)));
}
function render() {
 const matches = filter();
 const pages = Math.max(1, Math.ceil(matches.length / PAGE_SIZE));
 state.page = Math.max(1,Math.min(state.page,pages));
 $('results').replaceChildren();
 for(const item of matches.slice((state.page-1)*PAGE_SIZE,state.page*PAGE_SIZE)) {
  const button = document.createElement('button'); button.type='button'; button.className='icon-card';
  button.dataset.id=item.id; button.setAttribute('aria-label',`${name(item)} · ${item.category}`);
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
 detailPreview();
 $('detail-name').textContent=name(item);$('detail-ja').textContent=state.usage==='model-tree' ? (state.language==='en'?item.nodeNameJa:item.nodeName) : (state.language==='en'?item.nameJa:item.name);
 $('detail-id').textContent=item.id;$('detail-category').textContent=`${item.category} / ${item.role.toUpperCase()}`;
 $('detail-usage').textContent=`Use: ${item.usages.join(' / ')}${item.objectType ? ' · Node type: '+item.objectType : ''}`;
 $('detail-description').textContent=state.language==='ja' ? item.descriptionJa : item.description;
 $('detail-tags').replaceChildren();item.tags.filter(Boolean).forEach(tag=>{const el=document.createElement('span');el.textContent=tag;$('detail-tags').append(el);});
 if(!$('detail').open) $('detail').showModal();
}
function closeDetail(){if($('detail').open)$('detail').close();}
function toast(text){$('toast').textContent=text;$('toast').classList.add('visible');setTimeout(()=>$('toast').classList.remove('visible'),2500);}
function fallbackCopy(text){const area=document.createElement('textarea');area.value=text;area.style.position='fixed';area.style.opacity='0';$('detail').append(area);area.focus();area.select();try{return document.execCommand('copy');}catch{return false;}finally{area.remove();$('copy').focus();}}
icons.forEach(item=>{item.searchText=[item.id,item.name,item.nameJa,...item.categories,item.role,...item.usages,item.family,item.description,item.descriptionJa,item.nodeName||'',item.nodeNameJa||'',...(item.aliases||[]),...(item.nodeAliases||[]),...item.tags].join(' ').normalize('NFKC').toLocaleLowerCase();});
$('all-count').textContent=icons.length.toLocaleString();$('hero-count').textContent=icons.length.toLocaleString();
$('collection-scope').textContent=`${catalog.categories.Common} common application symbols + ${icons.length-catalog.categories.Common} engineering symbols. One icon per meaning, with light/dark files; command and tree uses share the same entry.`;
for(const [category,[label,mark]] of Object.entries(categories)){
 const count=icons.filter(item=>(item.categories || [item.category]).includes(category)).length;if(!count)continue;
 const button=document.createElement('button');button.className='category';button.dataset.category=category;button.title=label;
 button.innerHTML=`<span class="cat-mark">${mark}</span><span>${category}</span><span class="count">${count.toLocaleString()}</span>`;$('categories').append(button);
}
for(const id of ['common-open-file','common-save','cad-extrude','cam-end-mill','cae-tetrahedral-mesh','olp-robot-arm']){const item=icons.find(i=>i.id===id);if(item){const div=document.createElement('div');div.innerHTML=svg(item,false,'light');$('hero-icons').append(div);}}
document.querySelectorAll('.category').forEach(button=>button.addEventListener('click',()=>{state.category=button.dataset.category;state.page=1;render();}));
$('search').addEventListener('input',e=>{state.query=e.target.value;state.page=1;render();});
$('clear').addEventListener('click',()=>{state.query='';$('search').value='';state.page=1;render();$('search').focus();});
$('usage').addEventListener('change',e=>{state.usage=e.target.value;state.page=1;render();});
$('language').addEventListener('change',e=>{state.language=e.target.value;render();});
$('theme').addEventListener('change',e=>setTheme(e.target.value));
$('detail-theme').addEventListener('change',e=>setTheme(e.target.value));
$('size').addEventListener('change',e=>document.documentElement.style.setProperty('--icon-size',e.target.value+'px'));
document.querySelectorAll('[data-background]').forEach(button=>button.addEventListener('click',()=>{state.background=button.dataset.background;$('results').className='icon-grid '+state.background+'-bg';document.querySelectorAll('[data-background]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));if($('detail').open)detailPreview();}));
for(const [id,step] of [['previous',-1],['next',1]])$(id).addEventListener('click',()=>{state.page+=step;render();$('results').scrollIntoView({block:'start',behavior:'auto'});});
$('reset').addEventListener('click',()=>{state.category='all';state.usage='all';state.query='';state.page=1;$('search').value='';$('usage').value='all';render();});
$('close').addEventListener('click',closeDetail);
$('detail').addEventListener('click',event=>{if(event.target===$('detail')){const r=$('detail').getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)closeDetail();}});
$('detail').addEventListener('close',()=>{if(lastFocus?.isConnected)lastFocus.focus();});
$('copy').addEventListener('click',async()=>{const text=svg(state.selected,true);try{if(navigator.clipboard&&window.isSecureContext)await navigator.clipboard.writeText(text);else if(!fallbackCopy(text))throw Error('Clipboard blocked');toast('SVG copied');}catch{if(fallbackCopy(text))toast('SVG copied');else toast('Clipboard unavailable. Use Download SVG.');}});
$('download').addEventListener('click',()=>{const item=state.selected;const blob=new Blob([svg(item,true)],{type:'image/svg+xml'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download=item.id+(state.theme==='dark'?'.dark':'')+'.svg';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);toast('SVG download started');});
document.addEventListener('keydown',event=>{if(event.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)&&!$('detail').open){event.preventDefault();$('search').focus();}});
render();
})();
