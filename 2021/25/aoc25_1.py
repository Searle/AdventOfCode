# https://adventofcode.com/2021/day/25
from pathlib import Path

ref = 0
part = "_1"
debug = False

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + part + ext), "r").read().rstrip().split("\n")
# ---

E = ord('.')
R = ord('>')
D = ord('v')


def run():

    size_x = len(inputs[0])
    size_y = len(inputs)
    map1 = []

    for input in inputs:
        map1.append([ord(i) for i in input])

    def print_map():
        for line in map1:
            print("".join(chr(i) for i in line))
        print("\n")

    print_map()

    def move(x, y, dx, dy, size, c):
        moved = False
        x0 = x
        y0 = y
        first = map1[y0][x0]
        i = 0
        while i < size - 1:
            if map1[y][x] == c:
                y1 = (y + dy)
                x1 = (x + dx)
                if map1[y1][x1] == E:
                    map1[y1][x1] = c
                    map1[y][x] = E
                    moved = True
                    x += dx
                    y += dy
                    i += 1
            x += dx
            y += dy
            i += 1

        if x == x0 + dx * (size - 1) and y == y0 + dy * (size - 1):
            if map1[y][x] == c and first == E:
                map1[y0][x0] = c
                map1[y][x] = E
                moved = True

        return moved

    round = 0
    while True:
        moved = False
        round += 1
        for y in range(size_y):
            moved = move(0, y, 1, 0, size_x, R) or moved
        for x in range(size_x):
            moved = move(x, 0, 0, 1, size_y, D) or moved
        if not moved:
            break

        # print("ROUND", round)
        # print_map()
        # pass

    result = round

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
