# https://adventofcode.com/2023/day/08

from pathlib import Path
import re
from typing import List
import math
from functools import reduce

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def kgv(a, b):
    return abs(a * b) // math.gcd(a, b)


def kgv_list(numbers):
    return reduce(kgv, numbers)


def run():
    result = 0

    dirs = inputs.pop(0)
    inputs.pop(0)

    nexts = {}
    currents = []

    for i, input in enumerate(inputs):
        m = re.fullmatch(r"([A-Z0-9]+)\s*=\s*\(([A-Z0-9]+),\s*([A-Z0-9]+)\)", input)
        assert m is not None, input

        if m[1][2] == "A":
            currents.append(m[1])
        nexts[m[1]] = (m[2], m[3])

    assert len(currents) > 0

    nums = []
    for current in currents:
        dinx = 0
        count = 0
        while current[2] != "Z":
            d = dirs[dinx]
            dinx += 1
            if dinx >= len(dirs):
                dinx = 0
            current = nexts[current][0 if d == "L" else 1]
            count += 1
        nums.append(count)

    result = print(kgv_list(nums))
    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
