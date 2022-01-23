# https://adventofcode.com/2021/day/21
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    space = [int(input[0].split(':')[1]) - 1,  int(input[1].split(':')[1]) - 1]
    score = [0, 0]
    die = 0
    rollCount = 0

    def roll():
        nonlocal die, rollCount

        rollCount += 1
        if die == 100:
            die = 1
        else:
            die += 1
        return die

    while True:
        for pi in range(0, 2):
            rolled = roll() + roll() + roll()
            space[pi] = (space[pi] + rolled) % 10
            score[pi] += space[pi] + 1
            if score[pi] >= 1000:
                return score[1 - pi] * rollCount


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
