# https://adventofcode.com/2022/day/10
from pathlib import Path

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    x = 1
    cycle = 0

    pixel = ["."] * 240

    def noop():
        nonlocal cycle

        pos = cycle % 40
        if x >= pos - 1 and x <= pos + 1:
            pixel[cycle % 240] = "#"

        cycle += 1

    for input in inputs:
        noop()
        if input.startswith("addx "):
            noop()
            x += int(input[5:])

    result = ""
    for i in range(0, 240, 40):
        result += "".join(pixel[i:i+40]) + "\n"

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
