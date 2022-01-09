# https://adventofcode.com/2021/day/10
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    pair = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    score = 0
    for i in input:
        stack = ["*"]
        for c in i:
            if c in pair:
                stack.append(pair[c])
                continue
            if c != stack[-1]:
                assert c in scores, "c? " + c
                score += scores[c]
                break
            stack.pop()

    return score


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
