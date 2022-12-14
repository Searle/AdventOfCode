# https://adventofcode.com/2022/day/12
import math
from pathlib import Path
import random

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

# Scheint ohne Schätzfunktion zu funktionieren, aber ich weiss nicht warum


def run():

    w = len(inputs[0])
    h = len(inputs)

    sx = sy = ex = ey = -1

    for y, input in enumerate(inputs):
        x = input.find('S')
        if x >= 0:
            sx = x
            sy = y
        x = input.find('E')
        if x >= 0:
            ex = x
            ey = y

    assert sx >= 0 and ex >= 0

    print(sx, sy, ex, ey)

    open = {}
    closed = set()
    prev = {}

    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def ord2(s):
        if s == 'S':
            return ord('a') - 1
        if s == 'E':
            return ord('z') + 1
        return ord(s)

    open[(sx, sy)] = (sx, sy)

    prev[(sx, sy)] = None
    path = set()

    while len(open):
        oks = list(open.keys())
        # oks.sort(key=lambda cell: (cell[0]-ex)**2 + (cell[1]-ey)**2)
        cell = oks[0]
        open.pop(cell)

        if cell[0] == ex and cell[1] == ey:
            while cell is not None:
                path.add(cell)
                cell = prev[cell]
            break

        closed.add(cell)

        max_height = ord2(inputs[cell[1]][cell[0]]) + 1

        for dir in dirs:
            cell2 = (cell[0] + dir[0], cell[1] + dir[1])
            if cell2 in closed:
                continue

            if cell2[0] < 0 or cell2[0] >= w or cell2[1] < 0 or cell2[1] >= h:
                continue

            if ord2(inputs[cell2[1]][cell2[0]]) > max_height:
                continue

            prev[cell2] = cell
            open[cell2] = None

    def render_map():
        map1 = ""
        for y in range(h):
            s = ""
            for x in range(w):
                if (x, y) in path:
                    s += '#'
                elif (x, y) in closed:
                    s += '-'
                else:
                    s += inputs[y][x]
            map1 += s + "\n"
        return map1

    result = render_map()

    # result = len(path) - 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
