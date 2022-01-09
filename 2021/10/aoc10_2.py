# https://adventofcode.com/2021/day/10
from pathlib import Path

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    pair = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 1, "]": 2, "}": 3, ">": 4}

    iscores = []
    for i in input:
        stack = ["*"]
        isBroken = False
        for c in i:
            if c in pair:
                stack.append(pair[c])
                continue
            if c != stack[-1]:
                isBroken = True
                break
            stack.pop()
        if not isBroken:
            score = 0
            for f in stack[:0:-1]:
                score = score * 5 + scores[f]
            iscores.append(score)

    # print(iscores)

    return sorted(iscores)[len(iscores) >> 1]


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
