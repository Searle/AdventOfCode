# https://adventofcode.com/2022/day/9
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
    t = (0, 0)
    h = (0, 0)
    for input in inputs:
        dir = dirs[input[0]]
        len1 = int(input[2:])
        for _ in range(0, len1):
            h = (h[0] + dir[0], h[1] + dir[1])
            dx = abs(h[0]-t[0])
            dy = abs(h[1]-t[1])
            if dx > 1:
                t = (h[0] + sign(t[0] - h[0]), h[1])
            elif dy > 1:
                t = (h[0], h[1] + sign(t[1] - h[1]))
            trail.add(t)

    w = max([i[0] for i in trail])
    h = max([i[1] for i in trail])
    for y in range(0, h + 1):
        cc = list(["X" if (x, y) in trail else "." for x in range(0, w + 1)])
        print("".join(cc), "\n")

    result = len(trail)

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
