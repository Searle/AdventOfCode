# https://adventofcode.com/2022/day/03
from pathlib import Path
from functools import reduce

ref = 0
part = "_1"

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


def run():
    result = 0
    for input in inputs:
        itemBits = [1 << prio(c) for c in input]
        xlen = int(len(itemBits)/2)
        x0 = itemBits[0:xlen]
        x1 = itemBits[xlen:]
        a = or_arr(x0) & or_arr(x1)
        while a != 1:
            result += 1
            a >>= 1
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
