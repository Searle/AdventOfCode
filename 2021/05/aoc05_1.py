# https://adventofcode.com/2021/day/5
from pathlib import Path
from itertools import count

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def parse_csi(str): return tuple(map(lambda a: int(a), str.split(",")))


def sign(a): return (a > 0) - (a < 0)


def line(xy0, xy1, onlyHorizontal):
    # Only lines and diagonals
    swap = False
    if xy0[0] == xy1[0]:
        swap = True
        xy0 = (xy0[1], xy0[0])
        xy1 = (xy1[1], xy1[0])

    if xy0[0] > xy1[0]:
        [xy0, xy1] = [xy1, xy0]

    d = sign(xy1[1] - xy0[1])
    if (d != 0 and onlyHorizontal):
        return

    while xy0[0] <= xy1[0]:
        if swap:
            yield (xy0[1], xy0[0])
        else:
            yield xy0
        xy0 = (xy0[0] + 1, xy0[1] + d)


def run():
    cells = {}
    collisionCount = 0

    for i in input:
        i1 = i.split(" -> ")
        xy0 = parse_csi(i1[0])
        xy1 = parse_csi(i1[1])
        for xy in line(xy0, xy1, True):
            key = str(xy[0]) + ":" + str(xy[1])
            cells[key] = cells[key] + 1 if key in cells else 1
            if cells[key] == 2:
                collisionCount += 1
    return collisionCount


result = str(run())

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
