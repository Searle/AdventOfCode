# https://adventofcode.com/2021/day/14
from pathlib import Path

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    poly = input[0]
    rules = {}

    for i in input[2:]:
        rule = i.split(' -> ')
        rules[rule[0]] = (rule[0][0] + rule[1], rule[1] + rule[0][1])

    def add(arr, key, value):
        arr[key] = arr[key] + value if key in arr else value

    polys = {}
    for p in range(len(poly) - 1):
        pp = poly[p] + poly[p + 1]
        add(polys, pp, 1)

    for i in range(40):
        newPolys = polys.copy()
        for p in polys.keys():
            if p in rules:
                count = polys[p]
                newPolys[p] -= count
                add(newPolys, rules[p][0], count)
                add(newPolys, rules[p][1], count)

        polys = newPolys

    lookup = {poly[0]: 1}
    for p in polys:
        add(lookup, p[1], polys[p])

    units = sorted((b, a) for (a, b) in lookup.items())

    return units[-1][0] - units[0][0]


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
