# https://adventofcode.com/2023/day/06

from pathlib import Path
import re
from typing import List

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    temp = [0, 0]
    for i in range(0, 2):
        m = re.fullmatch(r".*:(.*)", inputs[i])
        assert m is not None
        temp[i] = int(m[1].replace(" ", ""))

    time = temp[0]
    dist = temp[1]

    result = 1
    count = 0
    for i in range(1, time):
        # print("x", i, i * (time - i))
        if i * (time - i) > dist:
            count += 1
    result *= count

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
