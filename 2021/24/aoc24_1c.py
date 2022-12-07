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
    prgs = []
    prg = []

    def padd(line):
        prg.append(line)

    def prg_flush():
        source = "\n".join([
            '[w, x, y, z] = regs',
        ] + prg + [
            "regs[0] = w",
            "regs[1] = x",
            "regs[2] = y",
            "regs[3] = z",
        ])
        code = compile(source, "<string>", "exec", optimize=2)
        prgs.append(code)

    for input in inputs:
        m = input.split(' ')
        cmd = m[0]
        reg = m[1]
        val = m[2] if len(m) > 2 else "0"
        if cmd == 'inp':
            if len(prg):
                prg_flush()
                prg = []
            padd(reg + ' = in1')
        elif cmd == 'add':
            padd(reg + ' += ' + val)
        elif cmd == 'mul':
            if val == "0":
                padd(reg + ' = ' + val)
            else:
                padd(reg + ' *= ' + val)
        elif cmd == 'div':
            if val != "1":
                padd(reg + ' //= ' + val)
        elif cmd == 'mod':
            padd(reg + ' %= ' + val)
        elif cmd == 'eql':
            padd(reg + ' = int(' + reg + ' == ' + val + ')')

    prg_flush()

    def run_prg(prg_i, regs, in1):
        exec(prgs[prg_i], {"regs": regs, "in1": in1})

    cache = {}

    def test1():

        # 95299897999897
        #   inp w [9, 0, 0, 429]

        regs = [0, 0, 0, 429]

        # run_prg(len(prgs)-2, regs, 9)

        def chk(prg_i, target_z):
            for n in range(9, 0, -1):
                cache_key = str(prg_i) + ":" + str(target_z) + ":" + str(n)
                if cache_key in cache:
                    return
                cache[cache_key] = True
                for z in range(0, 1000000):
                    # print("Z", z)
                    regs[3] = z
                    run_prg(prg_i, regs, n)
                    if regs[3] == target_z:
                        print("I!", prg_i, n, z)
                        if prg_i > 0:
                            chk(prg_i - 1, z)
                        break

        chk(len(prgs) - 1, 0)

    test1()

    result = 0
    return result


# ---
result = run()
# print(result)
# open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
