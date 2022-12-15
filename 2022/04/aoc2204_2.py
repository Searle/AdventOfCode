# https://adventofcode.com/2022/day/4
from pathlib import Path
from functools import reduce
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0
    for input in inputs:
        m = re.split('[-,]', input)
        a0 = int(m[0])
        a1 = int(m[1])
        b0 = int(m[2])
        b1 = int(m[3])
        if not((a1 < b0) or (a0 > b1)):
            result += 1
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
