const{Block,Blockchain}=require('./practical2') 
let sm = new Blockchain(); 
console.log("Developed by Hafsa"); 
sm.addBlock(new Block(1,Date.now(),24,12)); 
console.log(JSON.stringify(sm,null,3)) 
