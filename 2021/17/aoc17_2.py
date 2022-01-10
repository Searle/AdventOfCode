# https://adventofcode.com/2021/day/17
from pathlib import Path
import re

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def sign(a): return (a > 0) - (a < 0)


def run():

    m = re.search(
        '^target area: x=(-?\\d+)..(-?\\d+), y=(-?\\d+)..(-?\\d+)', input[0])
    assert m, "Regex failed"
    (x0, x1, y0, y1) = map(int, m.groups())
    # print(x0, x1, y0, y1)

    # Precalc all possible x-positions
    checks = []
    for vxStart in range(1, x1 + 1):
        vx = vxStart
        x = 0
        xSteps = 0
        while vx >= 0 and x <= x1:
            if x >= x0:
                checks.append((x, xSteps, vx, vxStart))
            x += vx
            vx -= 1
            xSteps += 1

    lookup = {}
    for check in checks:
        for vyStart in range(y0, -y0):
            (x, xSteps, vx, vxStart) = check

            vy = vyStart
            y = 0
            for _ in range(xSteps):
                y += vy
                vy -= 1

            while y >= y0 and x <= x1:
                if y <= y1:
                    lookup[(vxStart, vyStart)] = True
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy -= 1

    return len(lookup.keys())


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
