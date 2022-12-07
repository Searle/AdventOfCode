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

    prg = []
    for input in inputs:
        m = input.split(' ')

        cmd = mne_lookup[m[0]]
        assert cmd,  "Unknown command " + m[0]

        reg = ord(m[1]) - ord('w')
        reg1 = -1
        val1 = -1
        if len(m) > 2:
            if m[2] >= 'w' and m[2] <= 'z':
                reg1 = ord(m[2]) - ord('w')
            else:
                val1 = int(m[2])

        prg.append((cmd, reg, reg1, val1, input))

    def run_prg(in_list):
        regs = [0, 0, 0, 0]
        in_index = 0

        for (cmd, reg, reg1, val1, input) in prg:
            val = regs[reg1] if reg1 >= 0 else val1
            if cmd == INP:
                regs[reg] = in_list[in_index]
                in_index += 1
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

            print("# ", input, regs)

        return regs

    def check_model_nos():
        li = 0
        nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        largest = nums.copy()
        running = True

        while running:
            li += 1
            if li > 100000:
                print("AT", nums)
                li = 0

            # print(nums)
            regs = run_prg(nums)

            if regs[3] == 0:
                largest = nums.copy()
                print("FOUND", largest)

            # print("REGS", regs)
            # running = False

            for i in range(13, -1, -1):
                if nums[i] > 1:
                    nums[i] -= 1
                    break
                nums[i] = 9
                if i == 0:
                    running = False

    def test1():
        nums0 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 7]
        nums0 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        nums0 = [9, 5, 2, 9, 9, 8, 9, 7, 9, 9, 9, 8, 9, 7]
        # nums0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        nums1 = nums0.copy()

        run_prg(nums1)

    # check_model_nos()
    test1()

    return result


# ---
result = run()
# print(result)
# open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
