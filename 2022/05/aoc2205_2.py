# https://adventofcode.com/2022/day/05
from pathlib import Path
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0
    parseStack = True
    stacks = []
    for input in inputs:
        if parseStack:
            if input.find('[') < 0:
                parseStack = False
                # print(stacks)
            else:
                for i in range(0, (len(input) + 3) // 4):
                    if i + 1 > len(stacks):
                        stacks.append([])
                    if input[i * 4 + 1] != ' ':
                        stacks[i].insert(0, input[i * 4 + 1])
            continue

        m = re.match(r'^move (\d+) from (\d+) to (\d+)', input)
        if m is None:
            continue

        [amount, source, target] = [int(m[1]), int(m[2]) - 1, int(m[3]) - 1]
        stacks[target] += stacks[source][(-amount):]
        stacks[source] = stacks[source][:-amount]

    result = "".join([s[-1] for s in stacks])
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
