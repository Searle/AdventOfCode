# https://adventofcode.com/2021/day/11
from pathlib import Path
from itertools import count

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
            for c in ("A" * width * 2) + cave_ + ("A" * width * 2)]
    BORDER = ord("A") - ord("0")

    def printCave():

        def ch(x):
            if x < 0:
                return "-"
            if x >= 10:
                return ":"
            return str(x)

        print()
        for c in range(int(caveLen / width) + 1):
            print("".join([ch(x)
                  for x in cave[(c + 2) * width:(c + 3) * width - 1]]))

    # printCave()

    flashes = 0
    for z in range(100):

        for i in range(width * 2, caveLen + width * 2):
            if cave[i] != BORDER:
                cave[i] += 1

        while True:
            found = False
            for i in range(width * 2, caveLen + width * 2):
                if cave[i] != BORDER and cave[i] > 9:
                    for ofs in [-1, 1, -width - 1, -width, -width + 1, width - 1, width, width + 1]:
                        if cave[i + ofs] != BORDER:
                            cave[i + ofs] += 1
                            found = True
                    cave[i] = -10000
            if not found:
                break

        # printCave()

        for i in range(width * 2, caveLen + width * 2):
            if cave[i] != BORDER and cave[i] < 0:
                cave[i] = 0
                flashes += 1

        # printCave()

    return flashes


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
