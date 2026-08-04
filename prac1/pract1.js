const c = require("crypto");

class Block {
    constructor(i, t, n1, ph = "") {
        this.i = i;
        this.t = t;
        this.n1 = n1;
        this.sum = this.checkKrishnamoorthy();
        this.ph = ph;
        this.h = this.calHash();
    }

    calHash() {
        return c.createHash("sha256")
            .update(this.i + this.t + this.sum + this.ph)
            .digest("hex");
    }
    checkKrishnamoorthy(){
        let n=this.n1;
        let i;
        for(i=1;i<=n;i++){
            if(n*1===1)
                break;
        }
        console.log("n+"+n);
        if(n==i)
            return 'Factorial number';
        else
            return 'Not Factorial number';

    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGBlock()];
    }

    createGBlock() {
        return new Block(0, Date.now(), 0, "");
    }

    getCBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(b) {
        b.ph = this.getCBlock().h;
        b.h = b.calHash();
        this.chain.push(b);
    }
}

module.exports.Block = Block;
module.exports.Blockchain = Blockchain;
