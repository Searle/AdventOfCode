# https://adventofcode.com/2022/day/13

from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result = 0

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

    for i in range(0, (len(inputs) + 1) // 3):
        input1 = eval(inputs[i * 3])
        input2 = eval(inputs[i * 3 + 1])

        if cmp1(input1, input2) < 0:
            # print("*", input1)
            # print(" ", input2)
            result += i + 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
