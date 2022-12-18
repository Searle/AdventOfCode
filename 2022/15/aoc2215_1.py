# https://adventofcode.com/2022/day/15

from pathlib import Path
from itertools import chain
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    y = 2000000 if ref == 0 else 10

    ymap = set()
    stuff = set()

    for input in inputs:
        m = re.match(
            r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', input)
        assert m is not None

        [sx, sy, bx, by] = [int(m[1]), int(m[2]), int(m[3]), int(m[4])]
        if sy == y:
            stuff.add(sx)
        if by == y:
            stuff.add(bx)

        slen = abs(bx - sx) + abs(by - sy)
        slen1 = slen - y + sy if y > sy else slen + y - sy
        if slen1 >= 0:
            for i in range(sx - slen1, sx + slen1 + 1):
                if i not in stuff:
                    ymap.add(i)

    result = len(ymap)

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
