# https://adventofcode.com/2023/day/09

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

    for input in inputs:
        nums = [int(s) for s in re.split(r"\s+", input)]
        numss = [nums[-1]]

        while any([num != 0 for num in nums]):
            nums = [nums[i + 1] - nums[i] for i in range(0, len(nums) - 1)]
            numss.append(nums[-1])

        result += sum(numss)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
