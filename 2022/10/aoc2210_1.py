# https://adventofcode.com/2022/day/10
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result = 0
    x = 1
    cycle = 0

    def noop():
        nonlocal cycle, result
        cycle += 1
        if (cycle + 20) % 40 == 0:
            result += cycle * x

    for input in inputs:
        noop()
        if input.startswith("addx "):
            noop()
            x += int(input[5:])

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
