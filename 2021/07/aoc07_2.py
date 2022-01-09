# https://adventofcode.com/2021/day/7
from pathlib import Path

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    # print(input[0])

    crabs = sorted([int(i) for i in input[0].split(",")])

    crabs = [int(i) for i in input[0].split(",")]

    lookup = {}
    for i in crabs:
        lookup[i] = lookup[i] + 1 if i in lookup else 1

    values = sorted(list(lookup.items()))

    result = -1
    for i in range(values[0][0], values[-1][0] + 1):
        score = 0
        for value in values:
            dist = abs(value[0] - i)
            triangular = (dist * (dist + 1)) / 2
            score += int(triangular) * value[1]
        if result < 0 or score < result:
            result = score

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
