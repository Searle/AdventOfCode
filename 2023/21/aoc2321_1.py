# https://adventofcode.com/2023/day/21

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    mw = len(inputs[0]) + 1
    mh = len(inputs) + 2
    maze = "*" * (mw) + "".join(["*" + i for i in inputs]) + "*" * (mw)
    start = maze.index("S")
    maze = list(maze)
    maze[start] = "."

    def print_maze():
        for y in range(1, mh - 1):
            s = ""
            for x in range(1, mw):
                s += maze[y * mw + x]
            print("MAZE", s)

    dirs2 = (-mw, 1, mw, -1)

    toFill = set()
    toFill.add(start)
    foundOne = True
    for i in range(0, (6 if ref else 64) + 1):
        foundOne = False
        nextToFill = set()
        for pos in toFill:
            maze[pos] = "O"
            for dir in dirs2:
                if pos + dir >= 0 and pos + dir < len(maze):
                    if not pos + dir in toFill and maze[pos + dir] == ".":
                        nextToFill.add(pos + dir)
                        foundOne = True
        toFill = nextToFill
        if not foundOne:
            break

    for y in range(1, mh - 1):
        for x in range(1, mw):
            p = y * mw + x
            if ((x + y) & 1) == 0 and maze[p] == "O":
                result += 1

    # print_maze()

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
