const c = require("crypto"); 
class Block { 
 constructor(i, t, n1, n2,ph=""){ 
 this.i = i; 
 this.t = t;
 this.ph = ph; 
 this.n1 = n1; 
 this.n2 = n2; 
 this.sum = n1 + n2; 
 this.h = this.calHash(); 
 }; 
 calHash() { 
 return c 
 .createHash("sha256") 
 .update(this.i + this.t + this.sum + this.ph)  .digest("hex"); 
 }; 
}; 

class Blockchain { 
 constructor() { 
 this.chain = [this.createGBlock()];  }; 
 createGBlock() { 
 return new Block(0, Date.now(), 0, 0,"");  }; 
 getCBlock() { 
 return this.chain[this.chain.length - 1];  } 
 addBlock(b) { 
 b.ph = this.getCBlock().h; 
 b.h = b.calHash(); 
 this.chain.push(b); 
 } 
} 

module.exports.Block=Block; 
module.exports.Blockchain=Blockchain;

