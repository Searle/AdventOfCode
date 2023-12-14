# https://adventofcode.com/2023/day/04

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    rows = []
    for y in range(0, len(inputs)):
        rows.append([1 if ch == "#" else 0 if ch == "." else 2 for ch in inputs[y]])

    foundOne = True
    while foundOne:
        foundOne = False
        for y in range(0, len(rows) - 1):
            for x in range(0, len(rows[0])):
                if rows[y][x] == 0 and rows[y + 1][x] == 2:
                    rows[y][x] = 2
                    rows[y + 1][x] = 0
                    foundOne = True

            pass

    for y in range(0, len(rows)):
        for x in range(0, len(rows[0])):
            if rows[y][x] == 2:
                result += len(rows) - y

    if False:
        platform = ""
        for y in range(0, len(rows) - 1):
            platform += (
                "".join(["#" if ch == 1 else "." if ch == 0 else "0" for ch in rows[y]])
                + "\n"
            )
        print(platform)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
