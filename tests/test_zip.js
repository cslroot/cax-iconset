'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const {execFileSync}=require('node:child_process');
const {Zip,crc32}=require('../zip.js');
const {readZip}=require('./zip_helpers.js');
const root=path.resolve(__dirname,'..');
(async()=>{
 assert.equal(crc32(new TextEncoder().encode('123456789')),0xcbf43926);
 assert.equal(crc32(new Uint8Array()),0);
 const files=new Map([['plain.txt',Buffer.from('exact bytes\n')],['日本語/保存.svg',Buffer.from('透明な背景')],['binary.bin',Buffer.from(Array.from({length:256},(_,i)=>i))],['empty.txt',Buffer.alloc(0)]]);
 const zip=new Zip();for(const [name,bytes] of files)zip.add(name,bytes);
 const blob=zip.finish();assert.equal(blob.type,'application/zip');
 const entries=await readZip(blob);assert.deepEqual(entries,files);
 assert.throws(()=>zip.finish(),/finished/);assert.throws(()=>zip.add('x',new Uint8Array()),/finished/);
 assert.equal(zip.parts.length,0);assert.equal(zip.directory.length,0);
 assert.equal((await readZip(new Zip().finish())).size,0);
 const invalid=new Zip();
 for(const name of ['', '/abs.svg', '../escape.svg', 'dir/../escape.svg', './file.svg', 'dir//file.svg', 'dir/', 'C:file.svg', 'back\\slash.svg','nul\0.svg','newline\n.svg'])assert.throws(()=>invalid.add(name,new Uint8Array()),/filename/);
 assert.throws(()=>invalid.add('text','not bytes'),/bytes/);
 invalid.add('same.svg',new Uint8Array());assert.throws(()=>invalid.add('same.svg',new Uint8Array()),/Duplicate/);
 assert.throws(()=>invalid.add('é'.repeat(32768),new Uint8Array()),/limit/);
 const huge=new Zip();huge.offset=0xffffffff-40;assert.throws(()=>huge.add('a',new Uint8Array(1)),/limit/);
 const many=new Zip();for(let i=0;i<65535;i++)many.names.add(String(i));assert.throws(()=>many.add('more',new Uint8Array()),/limit/);
 const temp=fs.mkdtempSync(path.join(os.tmpdir(),'cax-zip-'));
 try{
  fs.writeFileSync(path.join(temp,'utf8.zip'),Buffer.from(await blob.arrayBuffer()));
  const manifest=JSON.parse(fs.readFileSync(path.join(root,'manifest.json'),'utf8'));
  for(const theme of ['light','dark']){
   const bundle=new Zip();
   for(const icon of manifest.icons)bundle.add(icon.id+(theme==='dark'?'.dark':'')+'.svg',fs.readFileSync(path.join(root,icon.variants[theme].file)));
   const archive=bundle.finish(),contents=await readZip(archive);assert.equal(contents.size,419);
   for(const icon of manifest.icons)assert.deepEqual(contents.get(icon.id+(theme==='dark'?'.dark':'')+'.svg'),fs.readFileSync(path.join(root,icon.variants[theme].file)));
   fs.writeFileSync(path.join(temp,theme+'.zip'),Buffer.from(await archive.arrayBuffer()));
  }
  for(const file of ['utf8','light','dark']){
   const archive=path.join(temp,file+'.zip');
   const output=execFileSync('unzip',['-t',archive],{encoding:'utf8'});
   assert.match(output,/No errors detected/);
   execFileSync('python3',['-c',`import sys,zipfile\nwith zipfile.ZipFile(sys.argv[1]) as z:\n assert z.testzip() is None\n assert all(i.flag_bits & 0x800 for i in z.infolist())\n assert all(i.compress_type == zipfile.ZIP_STORED for i in z.infolist())`,archive]);
  }
 }finally{fs.rmSync(temp,{recursive:true,force:true});}
 console.log('PASS ZIP32 headers, offsets, UTF-8 names, binary bytes, CRC-32, safe paths, limits, finalization and empty archive');
 console.log('PASS all 838 exact SVG entries; independent Node reader, Python zipfile and unzip -t');
})().catch(error=>{console.error(error);process.exitCode=1;});
