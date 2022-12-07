// https://adventofcode.com/2021/day/24
"use strict";

const fs = require("fs");
const ref = 0;
const part = "_1";

const ext = ref ? "_ref" + ref + ".txt" : ".txt";
const inputs = fs
    .readFileSync("input" + part + ext, { encoding: "utf8" })
    .trim()
    .split("\n");

function run() {
    let result = 0;

    const INP = 1;
    const ADD = 2;
    const MUL = 3;
    const DIV = 4;
    const MOD = 5;
    const EQL = 6;

    const mne_lookup = {
        inp: INP,
        add: ADD,
        mul: MUL,
        div: DIV,
        mod: MOD,
        eql: EQL,
    };

    const prg = [];
    for (const input of inputs) {
        const m = input.split(" ");

        const cmd = mne_lookup[m[0]];

        const reg = m[1].charCodeAt(0) - "w".charCodeAt(0);
        let reg1 = -1;
        let val1 = -1;
        if (m.length > 2) {
            if (m[2] >= "w" && m[2] <= "z") {
                reg1 = m[2].charCodeAt(0) - "w".charCodeAt(0);
            } else {
                val1 = +m[2];
            }
        }

        prg.push([cmd, reg, reg1, val1]);
    }

    function run_prg(in_list) {
        const regs = [0, 0, 0, 0];
        let in_index = 0;

        const limit = Math.pow(2, 31);
        // onsole.log("LIMIT", limit);

        // for (const [cmd, reg, reg1, val1] of prg) {

        for (let i = 0; i < prg.length; ++i) {
            const line = prg[i];
            const cmd = line[0];
            const reg = line[1];
            const reg1 = line[2];
            const val1 = line[3];
            const val = reg1 >= 0 ? regs[reg1] : val1;
            if (cmd === INP) {
                regs[reg] = in_list[in_index];
                // console.log("IN", regs[reg]);
                ++in_index;
            } else if (cmd === ADD) {
                regs[reg] += val;
            } else if (cmd === MUL) {
                regs[reg] *= val;
            } else if (cmd === DIV) {
                regs[reg] = (regs[reg] / val) | 0;
            } else if (cmd === MOD) {
                regs[reg] %= val;
            } else if (cmd === EQL) {
                regs[reg] = regs[reg] === val ? 1 : 0;
            } else {
                console.error("Unknown command " + cmd);
            }
            if (
                regs[0] >= limit ||
                regs[1] >= limit ||
                regs[2] >= limit ||
                regs[3] >= limit
            )
                console.log("REGS", regs);
        }

        return regs;
    }

    function check_model_nos() {
        let li = 0;
        const nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9];
        // const nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9];
        const largest = [...nums];
        let running = true;

        while (running) {
            ++li;
            if (li > 10000000) {
                console.log("AT", nums);
                li = 0;
            }

            const regs = run_prg(nums);

            // running = false;

            if (regs[3] === 0) {
                largest = [...nums];
                console.log("FOUND", largest);
            }

            for (let i = 13; i >= 0; --i) {
                if (nums[i] > 1) {
                    --nums[i];
                    break;
                }
                nums[i] = 9;
                if (i == 0) {
                    running = false;
                }
            }
        }
    }

    check_model_nos();

    return result;
}

result = run();
console.log(result);

// open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
