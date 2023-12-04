# https://adventofcode.com/2023/day/03

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
    lineLen = len(inputs[0]) + 1
    inputs2 = ("." * lineLen * 2) + ".".join(inputs) + ("." * lineLen * 2)
    reDigit = re.compile(r"\d+")
    reGear = re.compile(r"[*]")
    gears = {}
    for numberMatch in re.finditer(reDigit, inputs2):
        start = numberMatch.start()
        end = numberMatch.end()
        number = numberMatch.group()
        s = (
            inputs2[start - lineLen - 1 : end - lineLen + 1]
            + inputs2[start + lineLen - 1 : end + lineLen + 1]
            + inputs2[start - 1]
            + inputs2[end]
        )
        matches = [match for match in re.finditer(reGear, s)]
        if len(matches):
            numberLen = len(number) + 2
            for gearMatch in matches:
                gearPos = gearMatch.start()
                if gearPos < numberLen:
                    gearPos += start - lineLen - 1
                elif gearPos < numberLen * 2:
                    gearPos += start - numberLen + lineLen - 1
                elif gearPos == numberLen * 2:
                    gearPos += start - numberLen * 2 - 1
                else:
                    gearPos += start - numberLen - 3
                assert inputs2[gearPos] == "*"

                if gearPos in gears:
                    gears[gearPos].append(number)
                else:
                    gears[gearPos] = [number]

    for numbers in gears.values():
        if len(numbers) == 2:
            result += int(numbers[0]) * int(numbers[1])

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
