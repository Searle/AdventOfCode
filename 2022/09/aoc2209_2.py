# https://adventofcode.com/2022/day/09
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def sign(n):
    if n < 0:
        return -1
    if n > 0:
        return 1
    return 0


def run():

    dirs = {
        "U": (0, 1),
        "R": (1, 0),
        "D": (0, -1),
        "L": (-1, 0),
    }

    trail = set()

    def print_trail():
        w = max([i[0] for i in trail])
        h = max([i[1] for i in trail])
        for y in range(0, h + 1):
            cc = list(["X" if (x, y) in trail else "." for x in range(0, w + 1)])
            print("".join(cc), "\n")

    tl = 10
    z = [(0, 0)] * tl

    for input in inputs:
        dir1 = dirs[input[0]]
        len1 = int(input[2:])
        for _ in range(0, len1):
            dir = dir1
            for i in range(0, tl):
                z[i] = (z[i][0] + dir[0], z[i][1] + dir[1])
                if i < tl - 1:
                    dx = z[i][0] - z[i+1][0]
                    dy = z[i][1] - z[i+1][1]
                    if abs(dx) > 1 or abs(dy) > 1:
                        dir = (sign(dx), sign(dy))
                    else:
                        dir = (0, 0)
                else:
                    trail.add(z[i])

    print_trail()

    result = len(trail)

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
