# https://adventofcode.com/2021/day/14
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    poly = input[0]
    rules = {}

    for i in input[2:]:
        rule = i.split(' -> ')
        rules[rule[0]] = rule[1] + rule[0][1]

    for i in range(10):
        newPoly = poly[0]
        for p in range(len(poly) - 1):
            pp = poly[p] + poly[p + 1]
            newPoly += rules[pp] if pp in rules else pp[1]

        poly = newPoly

    lookup = {}
    for p in poly:
        lookup[p] = lookup[p] + 1 if p in lookup else 1

    units = sorted((b, a) for (a, b) in lookup.items())

    return units[-1][0] - units[0][0]


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
