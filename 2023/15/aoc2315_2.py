# https://adventofcode.com/2023/day/15

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    order = 0
    boxs = [{} for _ in range(256)]
    for input in "".join(inputs).split(","):
        m = re.fullmatch(r"(\S+)(-|=\S+)", input)
        assert m is not None, "NOT MATCHED: " + input

        label, op = m[1], m[2]

        current = 0
        for i in range(0, len(label)):
            co = ord(label[i])
            current = ((current + co) * 17) & 255

        box = boxs[current]

        if op[0] == "-":
            if label in box:
                box.pop(label)

        elif op[0] == "=":
            if label in box:
                box[label] = (box[label][0], op[1:])
            else:
                box[label] = (order, op[1:])
                order += 1

    for boxi, box in enumerate(boxs):
        if len(box.values()):
            for i, value in enumerate(sorted(box.values(), key=lambda a: a[0])):
                result += (boxi + 1) * (i + 1) * int(value[1])

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
