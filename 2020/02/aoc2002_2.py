# https://adventofcode.com/2020/day/2
from pathlib import Path
import re
from functools import reduce

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result = 0
    for input in inputs:
        m = re.match(r'^(\d+)-(\d+) (\S): (\S+)', input)
        if m:
            if (m[4][int(m[1]) - 1] == m[3]) != (m[4][int(m[2]) - 1] == m[3]):
                result += 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
