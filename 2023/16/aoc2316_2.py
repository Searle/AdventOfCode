# https://adventofcode.com/2023/day/16

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    mw = len(inputs[0]) + 1
    maze = "?" * (mw) + "".join(["?" + i for i in inputs]) + "?" * (mw)

    def print_maze(visited):
        v = set() if visited is None else visited
        for y in range(1, mw):
            s = ""
            for x in range(0, mw - 1):
                xy = y * mw + x
                s += "#" if xy in v else maze[xy]
            print(s)

    def run(start):
        nonlocal result

        # print(len(maze), start)
        # assert False

        beams: List[Tuple[int, int]] = [start]
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

        if len(visited) > result:
            result = len(visited)

    for i in range(1, mw):
        run((mw * i, 1))
        run((mw + mw * i, -1))
        run((i, mw))
        run((mw + mw * len(inputs) + i, -mw))

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")


""""
    r
        |
        \
        /
        
    

"""
