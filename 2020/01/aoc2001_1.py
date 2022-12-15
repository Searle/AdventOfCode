# https://adventofcode.com/2020/day/1
from pathlib import Path
import re
from functools import reduce

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    in1 = set(inputs)

    result = 0
    for sn in in1:
        n = 2020 - int(sn)
        if str(n) in in1:
            result = n * (2020 - n)
            break

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
