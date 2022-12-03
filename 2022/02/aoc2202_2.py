# https://adventofcode.com/2022/day/02
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

rps = [
    0+3, 3+1, 6+2,
    0+1, 3+2, 6+3,
    0+2, 3+3, 6+1,
]


def run():
    inElf = {'A': 0, 'B': 1, 'C': 2}
    inMe = {'X': 0, 'Y': 1, 'Z': 2}
    sum = 0
    for i in input:
        elf = inElf[i[0]]
        me = inMe[i[2]]
        sum += rps[elf*3+me]

    return sum


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
