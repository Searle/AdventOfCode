# https://adventofcode.com/2023/day/23

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

    mw = len(inputs[0])
    mh = len(inputs)
    tr = {"#": 0, "*": 1, ".": 2, "^": 3, ">": 4, "v": 5, "<": 6}

    maze = [tr[ch] for ch in "".join(inputs)]
    maze[1] = 0
    maze[len(maze) - 2] = 1
    start = mw + 1

    dirs = (-mw, 1, mw, -1)
    fills = {}

    def print_maze():
        for y in range(0, mh):
            s = ""
            for x in range(0, mw):
                c = maze[y * mw + x]
                if c == 0:
                    s += "###"
                elif y * mw + x in fills:
                    s += str(fills[y * mw + x][0]).rjust(3)
                else:
                    s += " " + "#*.^>v<"[c] + " "
            print("MAZE", s)
        print("")

    toFill = {start: (0, 1)}
    foundOne = True
    while foundOne:
        foundOne = False
        nextToFill = {}
        for pos in toFill:
            fill, prevPos = toFill[pos]
            fills[pos] = (fill, prevPos)
            nextFill = fill + 1
            for diri, dir in enumerate(dirs):
                pos1 = pos + dir
                if maze[pos1] >= 3 and maze[pos1] != diri + 3:
                    continue

                if maze[pos1] < 2:
                    if maze[pos1] == 1:
                        result = nextFill + 1
                    continue

                if pos1 in fills:
                    if fills[pos][1] == pos1 or fills[pos1][0] >= nextFill:
                        continue

                nextToFill[pos1] = (nextFill, pos)
                foundOne = True
        toFill = nextToFill

    print_maze()

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
