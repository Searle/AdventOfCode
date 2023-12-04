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
    for gearMatch in re.finditer(reGear, inputs2):
        gearPos = gearMatch.start()
        numbers = []

        def collectDigits(ofs: int):
            c = inputs2[gearPos + ofs]
            if reDigit.match(c):
                number = int(c)
                for i in range(1, 10):
                    c = inputs2[gearPos + ofs - i]
                    if not reDigit.match(c):
                        break
                    number += int(c) * (10**i)
                for i in range(1, 10):
                    c = inputs2[gearPos + ofs + i]
                    if not reDigit.match(c):
                        break
                    number = number * 10 + int(c)

                numbers.append(number)
                return True
            return False

        def isDigit(ofs: int):
            return reDigit.match(inputs2[gearPos + ofs])

        collectDigits(-1)
        collectDigits(+1)
        if collectDigits(-lineLen - 1):
            if not (isDigit(-lineLen)):
                collectDigits(-lineLen + 1)
        else:
            collectDigits(-lineLen + 1)
        if collectDigits(lineLen - 1):
            if not (isDigit(lineLen)):
                collectDigits(lineLen + 1)
        else:
            collectDigits(lineLen + 1)

        if len(numbers) == 2:
            result += numbers[0] * numbers[1]

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
