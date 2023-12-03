# https://adventofcode.com/2023/day/01

from pathlib import Path
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result= 0
    for input in inputs:
        m = re.fullmatch(
            r'.*?(\d)(?:.*(\d))?.*?', input)
        assert m is not None
        m2= m[1] if m[2] is None else m[2]
        result += int(m[1] + m2)

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
