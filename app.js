'use strict';
(() => {
const $ = id => document.getElementById(id);
const catalog = window.CAX_CATALOG;
const icons = catalog.icons;
const categories = {
 Common: ['Common application tools','⊞'], CAD: ['Design & modeling','◇'], CAM: ['Manufacturing','⌁'], CAE: ['Simulation','⌗'],
 CMM: ['Measurement','⊙'], OLP: ['Robotics / OLP','⌘']
};
const state = {category:'all',usage:'all',query:'',loaded:0,language:'en',background:'light',theme:'light',selected:null};
const BATCH_SIZE = 96;
const PNG_SIZES = [16,24,32,48,64,128,256];
let lastFocus;
let previewSerial = 0;
let matches = [];
let resultObserver;
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
 state.theme=theme;$('theme').value=theme;
 setBackground(theme);
 render(false);
}
function setBackground(background) {
 if(!['light','dark','grid'].includes(background))return;
 state.background=background;
 $('results').className='icon-grid '+background+'-bg';
 document.querySelectorAll('[data-background]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.background===background)));
 if($('detail').open)detailPreview();
}
function name(item) {return state.usage==='model-tree' ? (state.language==='ja'?item.nodeNameJa:item.nodeName) : (state.language==='ja'?item.nameJa:item.name);}
function filter() {
 const words = state.query.normalize('NFKC').toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
 return icons.filter(item => (state.category === 'all' || (item.categories || [item.category]).includes(state.category))
  && (state.usage === 'all' || item.usages.includes(state.usage))
  && words.every(word => item.searchText.includes(word)));
}
function updateCard(button,item) {
 button.setAttribute('aria-label',`${name(item)} · ${item.category}`);
 button.innerHTML=svg(item);
 const small=document.createElement('small');small.textContent=item.category;button.append(small);
 const label=document.createElement('span');label.textContent=name(item);button.append(label);
}
function stopObserving() {resultObserver?.disconnect();resultObserver=null;}
function observeMore() {
 stopObserving();
 if(state.loaded>=matches.length||$('detail').open||!window.IntersectionObserver)return;
 const observer=new window.IntersectionObserver(entries=>{
  // A disconnected observer may still have a queued callback after a filter reset.
  if(resultObserver!==observer)return;
  if(entries.some(entry=>entry.isIntersecting))loadMore();
 },{rootMargin:'0px 0px 240px 0px'});
 resultObserver=observer;observer.observe($('load-sentinel'));
}
function loadMore(focusNew=false) {
 const start=state.loaded,end=Math.min(start+BATCH_SIZE,matches.length);
 for(const item of matches.slice(start,end)) {
  const button=document.createElement('button');button.type='button';button.className='icon-card';button.dataset.id=item.id;
  updateCard(button,item);button.addEventListener('click',()=>openDetail(item));$('results').append(button);
 }
 state.loaded=end;
 const complete=end===matches.length;
 $('load-status').textContent=matches.length ? (complete?`All ${matches.length.toLocaleString()} icons shown`:`${end.toLocaleString()} of ${matches.length.toLocaleString()} icons shown`) : 'No matching icons';
 $('load-more').hidden=complete;$('load-more').disabled=complete;
 $('load-sentinel').hidden=complete;
 if(focusNew&&end>start)$('results').children[start].focus();
 observeMore();
}
function render(reset=true) {
 if(reset){stopObserving();matches=filter();state.loaded=0;$('results').replaceChildren();loadMore();}
 else Array.from($('results').children).forEach((button,index)=>updateCard(button,matches[index]));
 $('section-title').textContent=state.category==='all'?'All icons':state.category;
 $('result-count').textContent=`${matches.length.toLocaleString()} icons`;
 $('empty').hidden=!!matches.length;
 $('clear').hidden=!state.query;
 document.querySelectorAll('.category').forEach(b=>{const active=b.dataset.category===state.category;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
 if($('detail').open){if(matches.includes(state.selected))renderDetail();else closeDetail();}
}
function openDetail(item) {
 if(!$('detail').open)lastFocus=document.activeElement;
 state.selected=item;renderDetail();
 if(!$('detail').open){stopObserving();$('detail').showModal();}
}
function renderDetail() {
 const item=state.selected;
 // Disabling a focused button can blur it immediately in the browser.
 const focused=document.activeElement;
 if(!$('download-png').disabled)$('detail-status').textContent='';
 detailPreview();
 $('detail-name').textContent=name(item);$('detail-ja').textContent=state.usage==='model-tree' ? (state.language==='en'?item.nodeNameJa:item.nodeName) : (state.language==='en'?item.nameJa:item.name);
 $('detail-id').textContent=item.id;$('detail-category').textContent=`${item.category} / ${item.role.toUpperCase()}`;
 $('detail-usage').textContent=`Use: ${item.usages.join(' / ')}${item.objectType ? ' · Node type: '+item.objectType : ''}`;
 $('detail-description').textContent=state.language==='ja' ? item.descriptionJa : item.description;
 $('detail-tags').replaceChildren();item.tags.filter(Boolean).forEach(tag=>{const el=document.createElement('span');el.textContent=tag;$('detail-tags').append(el);});
 const index=matches.indexOf(item);
 $('detail-previous').disabled=index<=0;
 $('detail-next').disabled=index<0||index===matches.length-1;
 $('detail-position').textContent=`${index+1} / ${matches.length} · ${name(item)}`;
 // Keep keyboard focus inside the dialog if a navigation button reaches its edge.
 if((focused===$('detail-previous')||focused===$('detail-next'))&&focused.disabled){
  const other=focused===$('detail-previous')?$('detail-next'):$('detail-previous');
  (other.disabled?$('close'):other).focus();
 }
}
function moveDetail(step) {
 if(!$('detail').open)return;
 const index=matches.indexOf(state.selected),next=index+step;
 if(index<0||next<0||next>=matches.length)return;
 state.selected=matches[next];renderDetail();
}
function closeDetail(){if($('detail').open)$('detail').close();}
function toast(text){$('detail-status').textContent=$('detail').open?text:'';$('toast').textContent=text;$('toast').classList.add('visible');setTimeout(()=>$('toast').classList.remove('visible'),2500);}
function fallbackCopy(text){const area=document.createElement('textarea');area.value=text;area.style.position='fixed';area.style.opacity='0';$('detail').append(area);area.focus();area.select();try{return document.execCommand('copy');}catch{return false;}finally{area.remove();$('copy').focus();}}
function downloadBlob(blob,filename) {
 const url=URL.createObjectURL(blob);
 const a=document.createElement('a');
 try{a.href=url;a.download=filename;document.body.append(a);a.click();}
 finally{a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);}
}
function pngBlob(source,size) {
 return new Promise((resolve,reject)=>{
  let image,canvas,url,timer,finished=false;
  const finish=(error,blob)=>{
   if(finished)return;finished=true;clearTimeout(timer);
   if(image){image.onload=null;image.onerror=null;}
   if(url)URL.revokeObjectURL(url);
   if(canvas)canvas.width=canvas.height=0;
   if(error)reject(error);else resolve(blob);
  };
  try{
   canvas=document.createElement('canvas');canvas.width=canvas.height=size;
   // A fresh alpha-enabled canvas stays transparent. Preview surfaces are CSS only.
   const context=canvas.getContext('2d',{alpha:true});
   if(!context)throw Error('Canvas unavailable');
   image=new Image();
   image.onload=()=>{try{
    context.drawImage(image,0,0,size,size);
    canvas.toBlob(blob=>{
     if(!blob||!blob.size||blob.type!=='image/png')finish(Error('PNG encoding failed'));
     else finish(null,blob);
    },'image/png');
   }catch(error){finish(error);}};
   image.onerror=()=>finish(Error('SVG decoding failed'));
   // Set the SVG's intrinsic raster size without altering its viewBox or geometry.
   const sizedSource=source.replace('width="32" height="32"',`width="${size}" height="${size}"`);
   url=URL.createObjectURL(new Blob([sizedSource],{type:'image/svg+xml'}));
   timer=setTimeout(()=>finish(Error('PNG export timed out')),15000);
   image.src=url;
  }catch(error){finish(error);}
 });
}
icons.forEach(item=>{item.searchText=[item.id,item.name,item.nameJa,...item.categories,item.role,...item.usages,item.family,item.description,item.descriptionJa,item.nodeName||'',item.nodeNameJa||'',...(item.aliases||[]),...(item.nodeAliases||[]),...item.tags].join(' ').normalize('NFKC').toLocaleLowerCase();});
$('all-count').textContent=icons.length.toLocaleString();$('hero-count').textContent=icons.length.toLocaleString();
$('collection-scope').textContent=`${catalog.categories.Common} common application symbols + ${icons.length-catalog.categories.Common} engineering symbols. One icon per meaning, with light/dark files; command and tree uses share the same entry.`;
for(const [category,[label,mark]] of Object.entries(categories)){
 const count=icons.filter(item=>(item.categories || [item.category]).includes(category)).length;if(!count)continue;
 const button=document.createElement('button');button.className='category';button.dataset.category=category;button.title=label;
 button.innerHTML=`<span class="cat-mark">${mark}</span><span>${category}</span><span class="count">${count.toLocaleString()}</span>`;$('categories').append(button);
}
for(const id of ['common-open-file','common-save','cad-extrude','cam-end-mill','cae-tetrahedral-mesh','olp-robot-arm']){const item=icons.find(i=>i.id===id);if(item){const div=document.createElement('div');div.innerHTML=svg(item,false,'light');$('hero-icons').append(div);}}
document.querySelectorAll('.category').forEach(button=>button.addEventListener('click',()=>{state.category=button.dataset.category;render();}));
$('search').addEventListener('input',e=>{state.query=e.target.value;render();});
$('clear').addEventListener('click',()=>{state.query='';$('search').value='';render();$('search').focus();});
$('usage').addEventListener('change',e=>{state.usage=e.target.value;render();});
$('language').addEventListener('change',e=>{state.language=e.target.value;render(false);});
$('theme').addEventListener('change',e=>setTheme(e.target.value));
$('detail-theme').addEventListener('change',e=>setTheme(e.target.value));
$('size').addEventListener('change',e=>document.documentElement.style.setProperty('--icon-size',e.target.value+'px'));
document.querySelectorAll('[data-background]').forEach(button=>button.addEventListener('click',()=>setBackground(button.dataset.background)));
$('load-more').addEventListener('click',()=>loadMore(document.activeElement===$('load-more')));
for(const [id,step] of [['detail-previous',-1],['detail-next',1]])$(id).addEventListener('click',()=>moveDetail(step));
$('reset').addEventListener('click',()=>{state.category='all';state.usage='all';state.query='';$('search').value='';$('usage').value='all';render();});
$('close').addEventListener('click',closeDetail);
$('detail').addEventListener('click',event=>{if(event.target===$('detail')){const r=$('detail').getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)closeDetail();}});
$('detail').addEventListener('close',()=>{(lastFocus?.isConnected?lastFocus:$('search')).focus();observeMore();});
$('copy').addEventListener('click',async()=>{const text=svg(state.selected,true);try{if(navigator.clipboard&&window.isSecureContext)await navigator.clipboard.writeText(text);else if(!fallbackCopy(text))throw Error('Clipboard blocked');toast('SVG copied');}catch{if(fallbackCopy(text))toast('SVG copied');else toast('Clipboard unavailable. Use Download SVG.');}});
$('download').addEventListener('click',()=>{const item=state.selected;downloadBlob(new Blob([svg(item,true)],{type:'image/svg+xml'}),item.id+(state.theme==='dark'?'.dark':'')+'.svg');toast('SVG download started');});
$('download-png').addEventListener('click',async()=>{
 const button=$('download-png');
 if(button.disabled||!state.selected)return;
 // Snapshot the request: later theme, size or detail changes cannot mix exports.
 const item=state.selected,theme=state.theme,size=Number($('png-size').value);
 if(!PNG_SIZES.includes(size)){toast('Choose a PNG size from 16 to 256 px.');return;}
 button.disabled=true;button.textContent='Preparing PNG…';button.setAttribute('aria-busy','true');
 $('detail-status').textContent=`Preparing ${item.id}.${theme}.${size}.png…`;
 try{
  const blob=await pngBlob(svg(item,true,theme),size);
  downloadBlob(blob,`${item.id}.${theme}.${size}.png`);
  toast(`${size} × ${size} transparent PNG download started`);
 }catch{toast('PNG export failed. Try again or download SVG.');}
 finally{button.disabled=false;button.textContent='Download PNG ↓';button.setAttribute('aria-busy','false');}
});
document.addEventListener('keydown',event=>{
 if(event.defaultPrevented||event.altKey||event.ctrlKey||event.metaKey||event.shiftKey||event.isComposing)return;
 const target=event.target||document.activeElement;
 if(['INPUT','TEXTAREA','SELECT'].includes(target?.tagName)||target?.isContentEditable)return;
 if($('detail').open){
  if(event.key==='ArrowLeft'||event.key==='ArrowRight'){event.preventDefault();moveDetail(event.key==='ArrowLeft'?-1:1);}
 }else if(event.key==='/'){event.preventDefault();$('search').focus();}
});
setBackground(state.background);
render();
})();
