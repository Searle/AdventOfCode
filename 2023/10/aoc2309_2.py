# https://adventofcode.com/2023/day/10

from pathlib import Path
import re
from typing import List

ref = 0
part = "_2"

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
        mazeWithMark = maze[:next] + "*" + maze[next + 1 :]
        print(
            "   ",
            "\n    ".join(
                [
                    mazeWithMark[i * width : (i + 1) * width - 1]
                    for i in range(1, height - 1)
                ]
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
                    nextDirs2[tile0 + tile1] = dir
        nextDirs.append(nextDirs2)

    # pmaze("START", spos)

    width2 = width * 2
    height2 = height * 2
    dirs2 = (-width2, 1, width2, -1)
    maze2i = ["."] * (width2 * height2)

    def pmaze2(msg: str, next: int):
        print("---", msg, ":", next)
        maze2 = "".join(maze2i)
        mazeWithMark = maze2[:next] + "*" + maze2[next + 1 :]
        print(
            "   ",
            "\n    ".join(
                [
                    mazeWithMark[i * width2 : (i + 1) * width2 - 1]
                    for i in range(1, height2 - 1)
                ]
            ),
        )

    pos = spos
    seen = set()
    # seen.add(spos)
    steps = 0

    i = 0
    while True:
        next = None
        next2b = 0
        next2c = 0
        tile01 = None
        pos2 = (pos % width) * 2 + int(pos / width) * width2 * 2

        for dir, nextDirs2 in enumerate(nextDirs):
            tile01 = maze[pos] + maze[pos + dirs[dir]]
            if tile01 in nextDirs2:
                next = pos + dirs[nextDirs2[tile01]]
                next2b = pos2 + dirs2[nextDirs2[tile01]]
                next2c = next2b + dirs2[nextDirs2[tile01]]
                if not next in seen and (next != spos or i > 2):
                    break

        assert next is not None

        i += 1

        if next in seen:
            assert next == spos

        seen.add(next)

        maze2i[next2b] = "#"
        maze2i[next2c] = "#"

        if next == spos:
            break

        pos = next
        steps += 1

    toFill = set()
    toFill.add(0)
    foundOne = True
    while foundOne:
        foundOne = False
        nextToFill = set()
        for pos in toFill:
            maze2i[pos] = "O"
            for dir in dirs2:
                if pos + dir >= 0 and pos + dir < len(maze2i):
                    if not pos + dir in toFill and maze2i[pos + dir] == ".":
                        nextToFill.add(pos + dir)
                        foundOne = True
        toFill = nextToFill

    for y in range(0, height2, 2):
        for x in range(0, width2, 2):
            pos = y * width2 + x
            if maze2i[pos] == ".":
                # maze2i[pos] = "/"
                result += 1

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
