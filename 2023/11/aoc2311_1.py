# https://adventofcode.com/2023/day/11

from pathlib import Path
import re
from typing import List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    ymap = []
    ofs = 0
    for input in inputs:
        ymap.append(ofs)
        if input.count("#") == 0:
            ofs += 1
        ofs += 1

    t_inputs = [""] * len(inputs[0])
    for x in range(0, len(inputs[0])):
        for j in range(0, len(inputs)):
            t_inputs[x] += inputs[j][x]

    xmap = []
    ofs = 0
    for t_input in t_inputs:
        xmap.append(ofs)
        if t_input.count("#") == 0:
            ofs += 1
        ofs += 1

    stars = []
    for y, input in enumerate(inputs):
        for x in range(0, len(input)):
            if input[x] == "#":
                stars.append((xmap[x], ymap[y]))

    for i in range(0, len(stars)):
        for j in range(i + 1, len(stars)):
            result += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
