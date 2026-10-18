'use strict';
// Independent ZIP reader/CRC implementation for testing the emitted container.
const assert=require('node:assert/strict');
function crc32(bytes){let crc=0xffffffff;for(const byte of bytes){crc^=byte;for(let n=0;n<8;n++)crc=(crc&1)?(crc>>>1)^0xedb88320:crc>>>1;}return (crc^0xffffffff)>>>0;}
async function readZip(blob){
 const bytes=Buffer.from(await blob.arrayBuffer()),end=bytes.length-22;
 assert.equal(bytes.readUInt32LE(end),0x06054b50);
 assert.equal(bytes.readUInt16LE(end+4),0);assert.equal(bytes.readUInt16LE(end+6),0);
 assert.equal(bytes.readUInt16LE(end+20),0);
 const count=bytes.readUInt16LE(end+10),directorySize=bytes.readUInt32LE(end+12),directoryOffset=bytes.readUInt32LE(end+16);
 assert.equal(bytes.readUInt16LE(end+8),count);assert.equal(directoryOffset+directorySize,end);
 const entries=new Map();let central=directoryOffset,local=0;
 for(let index=0;index<count;index++){
  assert.equal(bytes.readUInt32LE(central),0x02014b50);
  assert.equal(bytes.readUInt16LE(central+8),0x0800);assert.equal(bytes.readUInt16LE(central+10),0);
  assert.equal(bytes.readUInt32LE(central+42),local);
  const crc=bytes.readUInt32LE(central+16),size=bytes.readUInt32LE(central+20),nameLength=bytes.readUInt16LE(central+28);
  assert.equal(bytes.readUInt32LE(central+24),size);
  assert.equal(bytes.readUInt16LE(central+30),0);assert.equal(bytes.readUInt16LE(central+32),0);
  const name=bytes.subarray(central+46,central+46+nameLength).toString('utf8');
  assert.equal(entries.has(name),false);
  assert.equal(bytes.readUInt32LE(local),0x04034b50);
  assert.equal(bytes.readUInt16LE(local+6),0x0800);assert.equal(bytes.readUInt16LE(local+8),0);
  assert.equal(bytes.readUInt32LE(local+14),crc);
  assert.equal(bytes.readUInt32LE(local+18),size);assert.equal(bytes.readUInt32LE(local+22),size);
  assert.equal(bytes.readUInt16LE(local+26),nameLength);assert.equal(bytes.readUInt16LE(local+28),0);
  assert.equal(bytes.subarray(local+30,local+30+nameLength).toString('utf8'),name);
  const data=bytes.subarray(local+30+nameLength,local+30+nameLength+size);
  assert.equal(data.length,size);assert.equal(crc32(data),crc);
  entries.set(name,data);local+=30+nameLength+size;central+=46+nameLength;
 }
 assert.equal(local,directoryOffset);assert.equal(central,end);
 return entries;
}
module.exports={readZip,crc32};
