# https://adventofcode.com/2023/day/03

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
    inputs.insert(0, "." * len(inputs[0]))
    inputs.append("." * len(inputs[0]))
    for i in range(0, len(inputs)):
        inputs[i] = "." + inputs[i] + "."
    reDigit = re.compile(r"\d+")
    reNoSymbol = re.compile(r"[^\d\.]")
    for i in range(1, len(inputs) - 1):
        for match in re.finditer(reDigit, inputs[i]):
            start = match.start()
            end = match.end()
            s = (
                inputs[i - 1][start - 1 : end + 1]
                + inputs[i + 1][start - 1 : end + 1]
                + inputs[i][start - 1]
                + inputs[i][end]
            )
            if reNoSymbol.search(s):
                result += int(match.group())
    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
