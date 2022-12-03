# https://adventofcode.com/2022/day/01
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    sum = 0
    max = 0
    for i in input:
        if i == '':
            sum = 0
            continue
        sum = sum+int(i)
        if sum > max:
            max = sum
    return max


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
