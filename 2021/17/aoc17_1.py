# https://adventofcode.com/2021/day/17
from pathlib import Path
import re

ref = False
part = "_1"

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

    return int(y0 * (y0 + 1) / 2)


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
