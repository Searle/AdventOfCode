# https://adventofcode.com/2022/day/14

from pathlib import Path
from itertools import chain

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    map1 = {}

    for input in inputs:
        last_pt = None
        for pt in input.split(' -> '):
            pt = list(map(int, pt.split(',')))
            if last_pt is not None:
                if last_pt[0] == pt[0]:
                    r = range(last_pt[1], pt[1] + 1) if pt[1] > last_pt[1] \
                        else range(pt[1], last_pt[1] + 1)
                    for i in r:
                        map1[(pt[0], i)] = 1
                else:
                    r = range(last_pt[0], pt[0] + 1) if pt[0] > last_pt[0] \
                        else range(pt[0], last_pt[0] + 1)
                    for i in r:
                        map1[(i, pt[1])] = 1
            last_pt = pt

    x0 = min(map(lambda cell: cell[0], map1)) - 10
    x1 = max(map(lambda cell: cell[0], map1)) + 10
    y0 = min(chain([0], map(lambda cell: cell[1], map1)))
    y1 = max(map(lambda cell: cell[1], map1)) + 1

    def print_map():
        for y in range(y0, y1 + 1):
            line = ""
            for x in range(x0, x1 + 1):
                line += ".#o"[map1[(x, y)] if (x, y) in map1 else 0::9]
            print(line)

    def simulate():
        px = 500
        py = 0
        if (px, py) in map1:
            return False
        while py < y1:
            if (px, py + 1) not in map1:
                py += 1
            elif (px - 1, py + 1) not in map1:
                px -= 1
                py += 1
            elif (px + 1, py + 1) not in map1:
                px += 1
                py += 1
            else:
                break
        map1[(px, py)] = 2
        return True

    result = 0
    while True:
        if not simulate():
            break
        result += 1

    # print_map()

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
