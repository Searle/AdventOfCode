# https://adventofcode.com/2023/day/10

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

    mazeRecs = []
    width = 0
    height = 0
    spos = 0
    maze = ""
    inputs.append("")
    for input in inputs:
        if input == "":
            assert spos >= 0
            mazeRecs.append((width, height, spos, "." * width + maze + "." * width))
            width = 0
            maze = ""
        else:
            if width == 0:
                width = len(input) + 1
                height = 2
                spos = -1

            if input.find("S") >= 0:
                spos = input.find("S") + (height - 1) * width

            height += 1
            maze += input + "."

    mazeRec = mazeRecs[0]
    width, height, spos, maze = mazeRec

    dirs = (-width, 1, width, -1)

    def pmaze(msg: str, next: int):
        print("---", msg, ":", next)
        maze2 = maze[:next] + "*" + maze[next + 1 :]
        print(
            "   ",
            "\n    ".join(
                [maze2[i * width : (i + 1) * width - 1] for i in range(1, height - 1)]
            ),
        )

    assert maze[spos] == "S"

    n = 1
    e = 2
    s = 4
    w = 8
    tileDirs = {
        ".": 0,
        "|": n + s,
        "-": e + w,
        "L": n + e,
        "J": n + w,
        "7": s + w,
        "F": s + e,
        "S": n + e + s + w,
    }

    otherDirs = (s, w, n, e)

    nextDirs = []
    for dir in range(0, 4):
        nextDirs2 = {}
        for tile0, v0 in tileDirs.items():
            for tile1, v1 in tileDirs.items():
                if ((1 << dir) & v0) and (otherDirs[dir] & v1):
                    nextDirs2[tile0 + tile1] = dirs[dir]
        nextDirs.append(nextDirs2)

    # pmaze("START", spos)

    pos = spos
    seen = set()
    steps = 0

    while True:
        next = None
        tile01 = None
        for dir, nextDirs2 in enumerate(nextDirs):
            tile01 = maze[pos] + maze[pos + dirs[dir]]
            if tile01 in nextDirs2:
                next = pos + nextDirs2[tile01]
                if not next in seen:
                    break

        assert next is not None
        pos = next
        if maze[pos] == "S":
            break

        assert not pos in seen
        seen.add(pos)
        steps += 1
        # pmaze("NEXT", pos)

    result = int((steps + 1) / 2)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
