# https://adventofcode.com/2020/day/01
from pathlib import Path
import re
from functools import reduce

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    in1 = set(inputs)

    adds = {}
    for sn1 in in1:
        for sn2 in in1:
            adds[str(int(sn1) + int(sn2))] = (sn1, sn2)

    result = 0
    for sn in in1:
        n = 2020 - int(sn)
        if str(n) in adds:
            result = int(sn) * int(adds[str(n)][0]) * int(adds[str(n)][1])
            break

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
