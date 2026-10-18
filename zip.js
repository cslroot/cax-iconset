'use strict';
// Dependency-free, uncompressed ZIP32. Each file is added separately so callers
// can yield/cancel between conversions rather than block on the whole catalog.
(() => {
 const MAX32 = 0xffffffff;
 const encoder = new TextEncoder();
 const crcTable = new Uint32Array(256);
 for(let n=0;n<256;n++){
  let crc=n;
  for(let k=0;k<8;k++)crc=(crc>>>1)^((crc&1)?0xedb88320:0);
  crcTable[n]=crc;
 }
 function crc32(bytes){
  let crc=MAX32;
  for(const byte of bytes)crc=(crc>>>8)^crcTable[(crc^byte)&255];
  return (crc^MAX32)>>>0;
 }
 function header(length){const bytes=new Uint8Array(length);return {bytes,view:new DataView(bytes.buffer)};}
 class Zip {
  constructor(){this.parts=[];this.directory=[];this.names=new Set();this.offset=0;this.directorySize=0;this.finished=false;}
  add(name,bytes){
   if(this.finished)throw Error('ZIP is already finished');
   if(typeof name!=='string'||!name||/[\\\x00-\x1f\x7f:]/.test(name)||name.startsWith('/')||name.split('/').some(part=>!part||part==='.'||part==='..'))throw Error('Unsafe ZIP filename');
   if(this.names.has(name))throw Error('Duplicate ZIP filename');
   if(!(bytes instanceof Uint8Array))throw Error('ZIP data must be bytes');
   const filename=encoder.encode(name),size=bytes.byteLength;
   const localSize=30+filename.length+size,centralSize=46+filename.length;
   if(filename.length>0xffff||this.names.size>=0xffff||size>MAX32||this.offset+localSize+this.directorySize+centralSize+22>MAX32)throw Error('ZIP32 size limit exceeded');
   const crc=crc32(bytes),local=header(30),central=header(46);
   local.view.setUint32(0,0x04034b50,true);
   local.view.setUint16(4,20,true); // ZIP 2.0, stored entries, UTF-8 names.
   local.view.setUint16(6,0x0800,true);
   local.view.setUint16(12,33,true); // Stable valid DOS date: 1980-01-01.
   local.view.setUint32(14,crc,true);
   local.view.setUint32(18,size,true);local.view.setUint32(22,size,true);
   local.view.setUint16(26,filename.length,true);
   central.view.setUint32(0,0x02014b50,true);
   central.view.setUint16(4,20,true);central.view.setUint16(6,20,true);
   central.view.setUint16(8,0x0800,true);central.view.setUint16(14,33,true);
   central.view.setUint32(16,crc,true);
   central.view.setUint32(20,size,true);central.view.setUint32(24,size,true);
   central.view.setUint16(28,filename.length,true);
   central.view.setUint32(42,this.offset,true);
   this.parts.push(local.bytes,filename,bytes);
   this.directory.push(central.bytes,filename);
   this.names.add(name);this.offset+=localSize;this.directorySize+=centralSize;
  }
  finish(){
   if(this.finished)throw Error('ZIP is already finished');
   const end=header(22);
   end.view.setUint32(0,0x06054b50,true);
   end.view.setUint16(8,this.names.size,true);end.view.setUint16(10,this.names.size,true);
   end.view.setUint32(12,this.directorySize,true);end.view.setUint32(16,this.offset,true);
   const blob=new Blob([...this.parts,...this.directory,end.bytes],{type:'application/zip'});
   this.finished=true;this.parts=[];this.directory=[];this.names.clear();
   return blob;
  }
 }
 const api={Zip,crc32};
 if(typeof module==='object'&&module.exports)module.exports=api;
 else window.CAX_ZIP=api;
})();
