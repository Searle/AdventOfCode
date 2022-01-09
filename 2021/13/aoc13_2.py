# https://adventofcode.com/2021/day/13
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    dots = []
    folds = []
    for i in input:
        if i.startswith('fold along'):
            folds.append((i[11], int(i[13:])))
            continue
        coords = i.split(',')
        if len(coords) == 2:
            dots.append((int(coords[0]), int(coords[1])))

    # folds = [folds[0]]

    def mirror(pos, mpos): return mpos * 2 - pos if pos > mpos else pos

    for f in folds:
        for di in range(len(dots)):
            if f[0] == 'x':
                dots[di] = (mirror(dots[di][0], f[1]), dots[di][1])
            else:
                dots[di] = (dots[di][0], mirror(dots[di][1], f[1]))

    gridWidth = max(map(lambda d: d[0], dots)) + 1
    gridHeight = max(map(lambda d: d[1], dots)) + 1
    grid = [[' '] * gridWidth for _ in range(gridHeight)]
    lookup = {}
    for d in dots:
        lookup[str(d[0]) + ':' + str(d[1])] = True
        grid[d[1]][d[0]] = '#'  # '█'

    return("\n".join(["".join([x for x in y]) for y in grid]))


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
