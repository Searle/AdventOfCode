# https://adventofcode.com/2022/day/03
from pathlib import Path
from functools import reduce

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def prio(c):
    if c >= 'a':
        return ord(c) - ord('a')+1
    return ord(c) - ord('A')+27


def or_arr(arr):
    return reduce(lambda a, b: a | b, arr)


def toBits(input):
    return or_arr([1 << prio(c) for c in input])


def run():
    result = 0
    for i in range(0, len(inputs), 3):
        a = toBits(inputs[i]) & toBits(inputs[i+1]) & toBits(inputs[i+2])
        while a != 1:
            result += 1
            a >>= 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
