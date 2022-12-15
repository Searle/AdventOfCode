# https://adventofcode.com/2022/day/13

from pathlib import Path
from functools import cmp_to_key

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result = 0

    inputs1 = [[[2]], [[6]]]
    for input in inputs:
        if len(input):
            inputs1.append(eval(input))

    def cmp1(in1, in2):
        ix1 = [in1] if type(in1) is int else in1
        ix2 = [in2] if type(in2) is int else in2

        for i, i1 in enumerate(ix1):
            if i >= len(ix2):
                return 1

            i2 = ix2[i]
            if type(i1) is int and type(i2) is int:
                if i1 < i2:
                    return -1
                if i1 > i2:
                    return 1
            else:
                res = cmp1(i1, i2)
                if res != 0:
                    return res

        if len(ix1) < len(ix2):
            return -1

        return 0

    di1 = di2 = -1
    for i, in1 in enumerate(sorted(inputs1, key=cmp_to_key(cmp1))):
        if str(in1) == '[[2]]':
            di1 = i + 1
        elif str(in1) == '[[6]]':
            di2 = i + 1

    result = di1 * di2

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
