# https://adventofcode.com/2021/day/15
from pathlib import Path

# This algorithm is wrong and worked by chance
# aoc15_2 has the working algorithm

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    width = len(input[0]) + 1
    cave_ = "A".join(input)
    caveLen = len(cave_)
    cave = [ord(c) - ord("0")
            for c in ("A" * width) + cave_ + ("A" * width)]
    BORDER = ord("A") - ord("0")

    def printCave():

        def ch(x): return '|' + str(x + 1000)[1:]

        print()
        for c in range(int(caveLen / width) + 1):
            print("".join([ch(x)
                  for x in cave[(c + 1) * width:(c + 2) * width - 1]]))

    # printCave()

    for i in range(width, caveLen + width):
        cost = 0
        if (cave[i - 1] != BORDER):
            cost = cave[i - 1]
        if (cave[i - width] != BORDER) and (cost == 0 or cave[i - width] < cost):
            cost = cave[i - width]
        cave[i] += cost

    return cave[width + caveLen - 1] - cave[width]


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
