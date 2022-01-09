# https://adventofcode.com/2021/day/9
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    width = len(input[0]) + 1
    cave_ = "a".join(input)
    caveLen = len(cave_)
    cave = ("a" * width) + cave_ + ("a" * width)

    # print(width, cave)

    sum = 0
    for i in range(width, caveLen + width):
        if (cave[i - 1] > cave[i]
                and cave[i + 1] > cave[i]
                and cave[i - width] > cave[i]
                and cave[i + width] > cave[i]):
            sum += int(cave[i]) + 1

    return sum


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
