const c = require("crypto");

class Block {
    constructor(i, t, n1, n = 0, ph = "") {
        this.i = i;
        this.t = t;
        this.ph = ph;
        this.n1 = n1;
        this.r = this.checkArmstrong();
        this.nonce = n;
        this.h = this.calHash();
    }

    calHash() {
        return c.createHash("sha256")
            .update(this.i + this.t + this.r + this.nonce + this.ph)
            .digest("hex");
    }

    mineblock(difficulty) {
        let target = "0".repeat(difficulty);

        while (this.h.substring(0, difficulty) != target) {
            this.nonce++;
            this.h = this.calHash();
        }

        console.log("Block mined");
        console.log("Nonce:", this.nonce);
    }

    // Armstrong Number Check
    checkArmstrong() {
        let n = this.n1;
        let original = n;
        let sum = 0;

        let digits = n.toString().length;

        while (n > 0) {
            let digit = n % 10;
            sum += Math.pow(digit, digits);
            n = Math.floor(n / 10);
        }

        if (sum === original)
            return "Is Armstrong number";
        else
            return "Not Armstrong number";
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGBlock()];
    }

    createGBlock() {
        return new Block(0, Date.now(), 0);
    }

    getCBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(b) {
        b.ph = this.getCBlock().h;
        b.h = b.calHash();

        // Mine every block (same behavior as original)
        if (b.checkArmstrong()) {
            b.mineblock(4);
            this.chain.push(b);
        }
    }

    validate() {
        for (let i = 1; i < this.chain.length; i++) {
            if (this.chain[i].ph != this.chain[i - 1].h) {
                return false;
            }
        }
        return true;
    }
}

module.exports.Block = Block;
module.exports.Blockchain = Blockchain;