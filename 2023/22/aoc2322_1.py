# https://adventofcode.com/2023/day/22

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple
from copy import deepcopy

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    space = {}
    bricks = []

    def print_space():
        minx = min([v[0] for v in space])
        maxx = max([v[0] for v in space])
        miny = min([v[1] for v in space])
        maxy = max([v[1] for v in space])
        minz = min([v[2] for v in space])
        maxz = max([v[2] for v in space])

        lines = ""
        for z in range(minz, maxz + 1):
            line = ""
            for x in range(minx, maxx + 1):
                ch = "."
                for y in range(miny, maxy + 1):
                    if (x, y, z) in space:
                        ch = chr(65 + space[(x, y, z)])
                        break
                line += ch
            line += " | "
            for y in range(miny, maxy + 1):
                ch = "."
                for x in range(minx, maxx + 1):
                    if (x, y, z) in space:
                        ch = chr(65 + space[(x, y, z)])
                        break
                line += ch
            lines = line + "\n" + lines

        print(lines)

    for input in inputs:
        m = re.fullmatch(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", input)
        assert m is not None, "NOT MATCHED: " + input

        x0, y0, z0, x1, y1, z1 = (
            int(m[1]),
            int(m[2]),
            int(m[3]),
            int(m[4]),
            int(m[5]),
            int(m[6]),
        )

        if x0 != x1:
            assert y0 == y1 and z0 == z1
            if x0 > x1:
                x0, x1 = x1, x0
            dirs = []
            for i in range(0, x1 - x0 + 1):
                dirs.append((i, 0, 0))
            bricks.append([len(bricks), (x0, y0, z0), dirs])
        elif y0 != y1:
            assert x0 == x1 and z0 == z1
            if y0 > y1:
                y0, y1 = y1, y0
            dirs = []
            for i in range(0, y1 - y0 + 1):
                dirs.append((0, i, 0))
            bricks.append([len(bricks), (x0, y0, z0), dirs])
        else:
            assert x0 == x1 and y0 == y1
            if z0 > z1:
                z0, z1 = z1, z0
            dirs = []
            for i in range(0, z1 - z0 + 1):
                dirs.append((0, 0, i))
            bricks.append([len(bricks), (x0, y0, z0), dirs])

    for inx, xyz, dirs in bricks:
        for dir in dirs:
            space[(xyz[0] + dir[0], xyz[1] + dir[1], xyz[2] + dir[2])] = inx
            pass

    def drop(bricks, space, skipInx):
        foundDrop = True
        while foundDrop:
            foundDrop = False
            for inx, xyz, dirs in bricks:
                if inx == skipInx:
                    continue
                foundOne = False
                if xyz[2] == 1:
                    continue
                for dir in dirs:
                    xyz1 = (xyz[0] + dir[0], xyz[1] + dir[1], xyz[2] + dir[2] - 1)
                    if xyz1 in space and space[xyz1] != inx and space[xyz1] != skipInx:
                        foundOne = True
                        break
                if not foundOne:
                    if skipInx != None:
                        return True
                    for dir in dirs:
                        xyz1 = (xyz[0] + dir[0], xyz[1] + dir[1], xyz[2] + dir[2])
                        space.pop((xyz1))
                        xyz1 = (xyz[0] + dir[0], xyz[1] + dir[1], xyz[2] + dir[2] - 1)
                        space[xyz1] = inx

                    bricks[inx][1] = (xyz[0], xyz[1], xyz[2] - 1)
                    # print("DROP", inx, xyz, dirs)
                    foundDrop = True
                    pass

        return False

    # print_space()
    drop(bricks, space, None)

    for brick in bricks:
        if not drop(deepcopy(bricks), deepcopy(space), brick[0]):
            result += 1

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
