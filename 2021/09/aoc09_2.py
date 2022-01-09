# https://adventofcode.com/2021/day/9
from pathlib import Path
from functools import reduce

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    width = len(input[0]) + 1
    cave_ = "a".join(input)
    caveLen = len(cave_)
    cave = [ord(c) - ord("0") for c in ("a" * width) + cave_ + ("a" * width)]

    mark = 0
    marks = [-1] * len(cave)
    for i in range(width, caveLen + width):
        if (cave[i - 1] > cave[i]
                and cave[i + 1] > cave[i]
                and cave[i - width] > cave[i]
                and cave[i + width] > cave[i]):
            marks[i] = mark
            mark += 1

    basins = []
    while True:
        found = False
        basins = [0] * mark
        for i in range(width, caveLen + width):
            for ofs in [-1, 1, -width, width]:
                if cave[i] < 9 and marks[i] < 0 and marks[i + ofs] >= 0 and cave[i + ofs] < cave[i]:
                    marks[i] = marks[i + ofs]
                    found = True
            if marks[i] >= 0:
                basins[marks[i]] += 1

        if not found:
            break

    return reduce(lambda a, b: a*b, sorted(basins)[-3:])


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
