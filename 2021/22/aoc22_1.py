# https://adventofcode.com/2021/day/22
from pathlib import Path
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    cmds = []

    for input in inputs:
        m = re.match(
            r'^(on|off) x=(-?\d+)[.][.](-?\d+),y=(-?\d+)[.][.](-?\d+),z=(-?\d+)[.][.](-?\d+)', input)
        if not m is None:
            cmd = (m.group(1) == 'on', *(int(m.group(i)) for i in range(2, 8)))
            if cmd[1] >= -50 and cmd[2] <= 50 and cmd[3] >= -50 and cmd[4] <= 50 and cmd[5] >= -50 and cmd[6] <= 50:
                cmds.append(cmd)

    coords = (set(), set(), set())
    for cmd in cmds:
        for i in range(0, 3):
            coords[i].add(cmd[i*2+1])
            coords[i].add(cmd[i*2+2] + 1)

    coords1 = []
    coords2 = (dict(), dict(), dict())
    for i in range(0, 3):
        coords1.append(sorted(iter(coords[i])))
        for index, coord in enumerate(coords1[i]):
            coords2[i][coord] = index

    values = {}
    for cmd in cmds:
        for x in range(coords2[0][cmd[1]], coords2[0][cmd[2] + 1]):
            if not x in values:
                values[x] = {}
            for y in range(coords2[1][cmd[3]], coords2[1][cmd[4] + 1]):
                if not y in values[x]:
                    values[x][y] = {}
                for z in range(coords2[2][cmd[5]], coords2[2][cmd[6] + 1]):
                    values[x][y][z] = cmd[0]

    result = 0
    for x in values.keys():
        for y in values[x].keys():
            for z in values[x][y].keys():
                if values[x][y][z]:
                    result += ((coords1[0][x + 1] - coords1[0][x])
                               * (coords1[1][y + 1] - coords1[1][y])
                               * (coords1[2][z + 1] - coords1[2][z]))
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
