const { Block, Blockchain } = require("./armstrong");

let bc = new Blockchain();

bc.addBlock(new Block(1, Date.now(), 153)); // Armstrong
bc.addBlock(new Block(2, Date.now(), 123)); // Not Armstrong
bc.addBlock(new Block(3, Date.now(), 370)); // Armstrong

console.log(bc.chain);
console.log("Valid:", bc.validate());