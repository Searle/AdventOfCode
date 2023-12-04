# https://adventofcode.com/2023/day/04

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
        m = re.fullmatch(r"Card\s+(\d+):(.+)\|(.+)", input)
        assert m is not None
        winning = {}
        for number in re.split(r"\s+", m[3].strip()):
            winning[number] = True
        found = 0
        for number in re.split(r"\s+", m[2].strip()):
            if number in winning:
                found += 1
        if found:
            result += 1 << (found - 1)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
