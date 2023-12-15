# https://adventofcode.com/2023/day/15

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    for input in "".join(inputs).split(","):
        current = 0
        for i in range(0, len(input)):
            co = ord(input[i])
            current = ((current + co) * 17) & 255

        result += current

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
