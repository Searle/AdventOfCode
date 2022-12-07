# https://adventofcode.com/2022/day/06
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + part + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0
    input = inputs[0]
    for i in range(len(input)):
        distinct = len(set(input[i:i + 4]))
        if distinct == 4:
            result = i + 4
            break
        i += 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
