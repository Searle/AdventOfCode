# https://adventofcode.com/2021/day/20
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    iea = input[0]

    cells = {}
    for y, line in enumerate(input[2:len(input[2]) + 2]):
        for x, char in enumerate(line):
            cells[(x, y)] = char == '#'

    x0 = 0
    y0 = 0
    x1 = len(input[2]) - 1
    y1 = len(input[2]) - 1

    print("BOUNDS", x0, y0, x1, y1)

    def nine(xy):
        x, y = xy
        return ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))

    def printCells(cells):
        print("CELLS", x0, y0, x1, y1)
        for y in range(y0, y1 + 1):
            print(['#' if cells[(x, y)] else '.' for x in range(x0, x1 + 1)])

    def enhance2(cells, emptyBit):
        nonlocal x0, x1, y0, y1

        cells2 = {}
        (nextX0, nextY0, nextX1, nextY1) = (x0, y0, x1, y1)
        for y in range(y0 - 2, y1 + 3):
            for x in range(x0 - 2, x1 + 3):
                value = 0
                for n in nine((x, y)):
                    value = value * 2
                    if n[0] < x0 or n[0] > x1 or n[1] < y0 or n[1] > y1:
                        value += emptyBit
                    else:
                        value += cells[n]

                cells2[(x, y)] = iea[value] == '#'
                nextX0 = min(nextX0, x)
                nextY0 = min(nextY0, y)
                nextX1 = max(nextX1, x)
                nextY1 = max(nextY1, y)

        # printCells(cells)

        (x0, y0, x1, y1) = (nextX0, nextY0, nextX1, nextY1)
        # printCells(cells2)
        return cells2

    for i in range(0, 1):
        cells = enhance2(cells, 0)
        cells = enhance2(cells, 1 if iea[0] == '#' else 0)

    return sum([i for i in cells.values()])


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
