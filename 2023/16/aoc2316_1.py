# https://adventofcode.com/2023/day/16

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    mw = len(inputs[0]) + 1
    maze = "?" * (mw) + "".join(["?" + i for i in inputs]) + "?" * (mw)
    beams: List[Tuple[int, int]] = [(mw, 1)]
    visited = set()
    visited1 = set()

    while len(beams):
        xy, d = beams.pop(0)

        while True:
            xy += d
            ch = maze[xy]
            if (xy, d) in visited1 or ch == "?":
                break
            visited.add(xy)
            visited1.add((xy, d))
            if ch == ".":
                continue
            if d == 1:
                if ch == "|":
                    beams.append((xy, -mw))
                    d = mw
                elif ch == "/":
                    d = -mw
                elif ch == "\\":
                    d = mw
            elif d == -1:
                if ch == "|":
                    beams.append((xy, -mw))
                    d = mw
                elif ch == "/":
                    d = mw
                elif ch == "\\":
                    d = -mw
            elif d == -mw:
                if ch == "-":
                    beams.append((xy, -1))
                    d = 1
                elif ch == "/":
                    d = 1
                elif ch == "\\":
                    d = -1
            elif d == mw:
                if ch == "-":
                    beams.append((xy, -1))
                    d = 1
                elif ch == "/":
                    d = -1
                elif ch == "\\":
                    d = 1
            else:
                assert False, "d?=" + str(d)

    result = len(visited)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
