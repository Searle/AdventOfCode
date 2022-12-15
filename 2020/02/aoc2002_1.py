# https://adventofcode.com/2020/day/2
from pathlib import Path
import re
from functools import reduce

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result = 0
    for input in inputs:
        m = re.match(r'^(\d+)-(\d+) (\S): (\S+)', input)
        if m:
            n = m[4].count(m[3])
            if n >= int(m[1]) and n <= int(m[2]):
                result += 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
