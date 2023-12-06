# https://adventofcode.com/2023/day/06

from pathlib import Path
import re
from typing import List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    times = [int(s) for s in re.split(r"\s+", inputs[0])[1:]]
    dists = [int(s) for s in re.split(r"\s+", inputs[1])[1:]]
    list1 = list(zip(times, dists))

    result = 1
    for time, dist in list1:
        # print(time, dist)
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
