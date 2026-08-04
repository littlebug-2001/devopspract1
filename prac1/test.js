const { Block, Blockchain } = require('./pract1');

let sm = new Blockchain();

console.log("Developed by Raghvan");
sm.addBlock(new Block(1, Date.now(), 1));
sm.addBlock(new Block(1, Date.now(), 145));
sm.addBlock(new Block(1, Date.now(), 1000));
console.log(JSON.stringify(sm, null, 3));