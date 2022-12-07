# https://adventofcode.com/2021/day/24
from pathlib import Path
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + part + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    INP = 1
    ADD = 2
    MUL = 3
    DIV = 4
    MOD = 5
    EQL = 6

    mne_lookup = {
        "inp": INP,
        "add": ADD,
        "mul": MUL,
        "div": DIV,
        "mod": MOD,
        "eql": EQL,
    }

    prgs = []
    prg = []
    for input in inputs:
        m = input.split(' ')

        cmd = mne_lookup[m[0]]
        assert cmd,  "Unknown command " + m[0]

        if cmd == INP and len(prg):
            prgs.append(prg)
            prg = []

        reg = ord(m[1]) - ord('w')
        reg1 = -1
        val1 = -1
        if len(m) > 2:
            if m[2] >= 'w' and m[2] <= 'z':
                reg1 = ord(m[2]) - ord('w')
            else:
                val1 = int(m[2])

        prg.append((cmd, reg, reg1, val1, input))

    prgs.append(prg)

    def run_prg(prg, regs, in1):

        for (cmd, reg, reg1, val1, input) in prg:
            val = regs[reg1] if reg1 >= 0 else val1
            if cmd == INP:
                regs[reg] = in1
            elif cmd == ADD:
                regs[reg] += val
            elif cmd == MUL:
                regs[reg] *= val
            elif cmd == DIV:
                regs[reg] //= val
            elif cmd == MOD:
                regs[reg] %= val
            elif cmd == EQL:
                regs[reg] = 1 if regs[reg] == val else 0
            else:
                assert False, "Unknown command " + cmd

            # print("# ", input, regs)

        return regs

    cache = {}

    def test1():

        nums0 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 7]
        nums0 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        nums0 = [9, 5, 2, 9, 9, 8, 9, 7, 9, 9, 9, 8, 9, 7]
        nums0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        nums1 = nums0.copy()

        # 95299897999897

        def chk(prg_i, target_z):
            prg = prgs[prg_i]
            for n in range(9, 0, -1):
                for z in range(0, 1000000):
                    # print("Z", z)
                    cache_key = str(prg_i) + ":" + str(z) + ":" + str(n)
                    if cache_key in cache:
                        return
                    regs = run_prg(prg, [0, 0, 0, z], n)
                    cache[cache_key] = True
                    if regs[3] == target_z:
                        print("I!", prg_i, n, z)
                        if prg_i > 0:
                            chk(prg_i - 1, z)
                        break

        chk(len(prgs)-1, 0)

    test1()

    return result


# ---
result = run()
# print(result)
# open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
