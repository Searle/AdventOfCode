# https://adventofcode.com/2021/day/6
from pathlib import Path
from functools import reduce

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    arr = [0] * 9
    for i in input[0].split(","):
        arr[int(i)] += 1
    for i in range(256):
        arr = arr[1:7] + [arr[7] + arr[0], arr[8], arr[0]]

    return reduce(lambda a, b: a + b, arr)


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
