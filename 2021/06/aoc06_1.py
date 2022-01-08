# https://adventofcode.com/2021/day/6
from pathlib import Path
from itertools import count

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def parse_csi(str): return tuple(map(lambda a: int(a), str.split(",")))


def run():
    fishs = [fish for fish in map(lambda a: int(a), input[0].split(","))]

    for i in range(80):
        for fish_i in range(len(fishs)):
            if fishs[fish_i] == 0:
                fishs[fish_i] = 6
                fishs.append(8)
            else:
                fishs[fish_i] = fishs[fish_i] - 1

    return len(fishs)


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
