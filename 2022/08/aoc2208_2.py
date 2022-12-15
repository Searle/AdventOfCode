# https://adventofcode.com/2022/day/8
from pathlib import Path

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    size = len(inputs)
    assert len(inputs[0]) == size

    map1 = []
    map2 = []
    for input in inputs:
        map1.append([ord(i) - ord('0') for i in input])
        map2.append([1 for _ in input])

    def print_map(prefix, m):
        for line in m:
            print(prefix, " ", " ".join(map(str, line)))

    def one(x1, y1, dx1, dy1, dx2, dy2):
        nonlocal result

        for _ in range(0, size):
            last = [0] * 10
            x2 = x1
            y2 = y1
            for pos in range(0, size):
                c = map1[y2][x2]
                map2[y2][x2] *= pos - max(last[c:])
                last[c] = pos
                x2 += dx2
                y2 += dy2

            x1 += dx1
            y1 += dy1

    one(0, 0, 0, 1, 1, 0)
    one(size - 1, 0, 0, 1, -1, 0)
    one(0, 0, 1, 0, 0, 1)
    one(0, size - 1, 1, 0, 0, -1)

    # print_map("map1", map1)
    # print()
    # print_map("map2", map2)

    result = 0
    for line in map2:
        result = max(result, max(line))

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
