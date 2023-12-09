# https://adventofcode.com/2023/day/09

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

    for input in inputs:
        nums = [int(s) for s in re.split(r"\s+", input)]
        numss = [nums[0]]

        while any([num != 0 for num in nums]):
            nums = [nums[i + 1] - nums[i] for i in range(0, len(nums) - 1)]
            numss.append(nums[0])

        numss = numss[::-1]
        nums3 = [0] * len(numss)
        num2 = 0
        for i, num in enumerate(numss[1:]):
            nums3[i + 1] = num - nums3[i]
            num2 -= num

        result += nums3[-1]

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
