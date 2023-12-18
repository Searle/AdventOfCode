# https://adventofcode.com/2023/day/18

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    px = 0
    py = 0
    maze: Set[Tuple[int, int]] = set()

    maze.add((px, py))
    xxs = []
    left = False
    size = 0
    dir = 0
    plus = 0
    for i, input in enumerate(inputs[len(inputs) - 1 :] + inputs + inputs[0:1]):
        m = re.fullmatch(r"(?:\S) (?:\d+) \(#(.*)(\d)\)", input)
        assert m is not None, "NOT MATCHED: " + input

        last_left = left
        last_size = size
        last_dir = dir

        size, dir = int(m[1], 16), int(m[2])
        dirs = {0: (1, 0), 3: (0, -1), 2: (-1, 0), 1: (0, 1)}
        left = last_dir == (dir + 1) & 3

        if left and last_left:
            plus = -1
        elif not left and not last_left:
            plus = 1
        else:
            plus = 0

        if i > 1:
            px2 = px + dirs[last_dir][0] * (last_size + plus)
            py2 = py + dirs[last_dir][1] * (last_size + plus)

            if dirs[last_dir][0] == 0:
                if dirs[last_dir][1] > 0:
                    xxs.append((px, py, py2))
                else:
                    xxs.append((px, py2, py))

            px = px2
            py = py2
            maze.add((px, py))

    ys = sorted(set([xy[1] for xy in maze]))

    for yi in range(0, len(ys) - 1):
        xs = []
        for xx in xxs:
            if xx[1] <= ys[yi] and xx[2] >= ys[yi + 1]:
                xs.append(xx[0])
        xs.sort()
        assert len(xs) % 2 == 0
        for xi in range(0, len(xs), 2):
            result += (xs[xi + 1] - xs[xi]) * (ys[yi + 1] - ys[yi])

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
