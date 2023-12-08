# https://adventofcode.com/2023/day/08

from pathlib import Path
import re
from typing import List

ref = 2
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    dirs = inputs.pop(0)
    inputs.pop(0)

    nexts = {}
    current = "AAA"

    for input in inputs:
        m = re.fullmatch(r"([A-Z]+)\s*=\s*\(([A-Z]+),\s*([A-Z]+)\)", input)
        assert m is not None, input
        nexts[m[1]] = (m[2], m[3])

    result = 0
    while current != "ZZZ":
        for c in dirs:
            current = nexts[current][0 if c == "L" else 1]
            if current == "ZZZ":
                break
            result += 1

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
