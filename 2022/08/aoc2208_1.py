# https://adventofcode.com/2022/day/8
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

# 3  0  3  7  3
# 2 >5 >5  1  2
# 6 >5  3 >3  2
# 3  3 >5  4  9
# 3  5  3  9  0


def run():

    size = len(inputs)
    assert len(inputs[0]) == size

    visible = set()
    result = 0

    def one(x1, y1, dx1, dy1, dx2, dy2):
        for _ in range(1, size - 1):
            c = inputs[y1][x1]
            x2 = x1
            y2 = y1
            for _ in range(1, size - 1):
                x2 += dx2
                y2 += dy2
                next_c = inputs[y2][x2]
                if next_c > c:
                    visible.add(str(x2) + ":" + str(y2))
                    if next_c == '9':
                        break
                    c = next_c

            x1 += dx1
            y1 += dy1

    one(0, 1, 0, 1, 1, 0)
    one(size - 1, 1, 0, 1, -1, 0)
    one(1, 0, 1, 0, 0, 1)
    one(1, size - 1, 1, 0, 0, -1)
    result = (size - 1) * 4 + len(visible)

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
