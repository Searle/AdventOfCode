# https://adventofcode.com/2021/day/3
from pathlib import Path
from functools import reduce

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

inxs = []
bitSums = []
for i in input:
    if len(inxs) == 0:
        inxs = range(len(i))
        bitSums = [0 for _ in inxs]
    bitSums = [bitSums[inx] + int(i[inx]) for inx in inxs]
pivot = len(input) / 2
gamma = reduce(lambda a, b: a + b,  [2 ** (len(inxs) - inx - 1) if bitSums[inx] >=
                                     pivot else 0 for inx in inxs])
result = str(gamma * (2 ** len(inxs) - gamma - 1))

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
