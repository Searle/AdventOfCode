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
    lineLen = len(inputs[0]) + 1
    inputs2 = ("." * lineLen) + ".".join(inputs) + ("." * lineLen)
    reDigit = re.compile(r"\d+")
    reNoSymbol = re.compile(r"[^\d\.]")
    for match in re.finditer(reDigit, inputs2):
        start = match.start()
        end = match.end()
        s = (
            inputs2[start - lineLen - 1 : end - lineLen + 1]
            + inputs2[start + lineLen - 1 : end + lineLen + 1]
            + inputs2[start - 1]
            + inputs2[end]
        )
        if reNoSymbol.search(s):
            result += int(match.group())
    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
