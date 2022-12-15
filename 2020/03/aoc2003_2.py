# https://adventofcode.com/2020/day/3
from pathlib import Path

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    r1 = r2 = r3 = r4 = r5 = 0
    for i, input in enumerate(inputs):
        if input[i % len(input)] == '#':
            r1 += 1
        if input[(i * 3) % len(input)] == '#':
            r2 += 1
        if input[(i * 5) % len(input)] == '#':
            r3 += 1
        if input[(i * 7) % len(input)] == '#':
            r4 += 1
        if i % 2 == 0 and input[(i // 2) % len(input)] == '#':
            r5 += 1

    result = r1 * r2 * r3 * r4 * r5

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
