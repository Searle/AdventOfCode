# https://adventofcode.com/2023/day/14

from pathlib import Path
import re
from typing import Dict, Set, List
import hashlib
import json
from copy import deepcopy

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    rows = []
    for y in range(0, len(inputs)):
        rows.append([1 if ch == "#" else 0 if ch == "." else 2 for ch in inputs[y]])

    def show():
        platform = ""
        for y in range(0, len(rows)):
            platform += (
                "".join(["#" if ch == 1 else "." if ch == 0 else "0" for ch in rows[y]])
                + "\n"
            )
        print(platform, "\n")

    def score(rows):
        score1 = 0
        for y in range(0, len(rows)):
            for x in range(0, len(rows[0])):
                if rows[y][x] == 2:
                    score1 += len(rows) - y
        return score1

    def cycle():
        foundOne = True
        while foundOne:
            foundOne = False
            for y in range(0, len(rows) - 1):
                for x in range(0, len(rows[0])):
                    if rows[y][x] == 0 and rows[y + 1][x] == 2:
                        rows[y][x] = 2
                        rows[y + 1][x] = 0
                        foundOne = True
        foundOne = True
        while foundOne:
            foundOne = False
            for y in range(0, len(rows)):
                for x in range(0, len(rows[0]) - 1):
                    if rows[y][x] == 0 and rows[y][x + 1] == 2:
                        rows[y][x] = 2
                        rows[y][x + 1] = 0
                        foundOne = True
        foundOne = True
        while foundOne:
            foundOne = False
            for y in range(len(rows) - 1, 0, -1):
                for x in range(0, len(rows[0])):
                    if rows[y][x] == 0 and rows[y - 1][x] == 2:
                        rows[y][x] = 2
                        rows[y - 1][x] = 0
                        foundOne = True
        foundOne = True
        while foundOne:
            foundOne = False
            for y in range(0, len(rows)):
                for x in range(len(rows[0]) - 1, 0, -1):
                    if rows[y][x] == 0 and rows[y][x - 1] == 2:
                        rows[y][x] = 2
                        rows[y][x - 1] = 0
                        foundOne = True

    cycles = {}
    hashvs = []
    for i in range(1000000):
        cycle()
        hashv = hashlib.md5(json.dumps(rows).encode()).hexdigest()
        if hashv in cycles:
            i1, _ = cycles[hashv]
            offset = (1000000000 - i1) % (i - i1)
            _, rows1 = cycles[hashvs[i1 + offset - 1]]
            result = score(rows1)
            break
        cycles[hashv] = (i, deepcopy(rows))
        hashvs.append(hashv)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
