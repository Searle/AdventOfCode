# https://adventofcode.com/2021/day/15
from pathlib import Path

# Based on https://de.wikipedia.org/wiki/Dijkstra-Algorithmus

ref = 1
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def expandInput(input):
    width = len(input[0])
    lookup = {'1': '2', '2': '3', '3': '4', '4': '5',
              '5': '6', '6': '7', '7': '8', '8': '9', '9': '1'}
    nextInput = []
    for i in input:
        for x in range(width * 4):
            i += lookup[i[x]]
        nextInput.append(i)
    for y in range(width * 4):
        i = ""
        for x in range(width * 5):
            i += lookup[nextInput[y][x]]
        nextInput.append(i)

    return nextInput


def run(input):

    input = expandInput(input)

    width = len(input[0]) + 1
    cave_ = "|".join(input)
    caveLen = len(cave_)
    cave = [-1 if c == '|' else ord(c) - ord("0")
            for c in ("|" * width) + cave_ + ("|" * width)]
    BORDER = -1

    def getCave(cave):

        def ch(x):
            if x < 0:
                return '|----'
            return '|' + "{x:4d}".format(x=x)

        result = ""
        for c in range(int(caveLen / width) + 1):
            result += "".join([ch(x)
                               for x in cave[(c + 1) * width:(c + 2) * width - 1]]) + "\n"
        return result

    def printCave(cave):
        print("\n" + getCave(cave))

    def dumpCave(name, cave):
        open(path/("result_" + name + part + ext), "w").write(getCave(cave))

    dists = [-1] * len(cave)
    visited = [False] * len(cave)
    dists[width] = 0
    todos = {width: 0}

    while True:
        items = todos.items()
        if len(items) == 0:
            break

        pick = sorted(items, key=lambda a: a[1])[0]
        c = pick[0]
        visited[c] = True
        del todos[c]
        for ofs in [-1, 1, -width, width]:
            if cave[c + ofs] != BORDER and not visited[c + ofs]:
                dist = dists[c] + cave[c + ofs]
                dists[c + ofs] = (dist if dists[c + ofs] < 0
                                  else min(dists[c + ofs], dist))
                todos[c + ofs] = dists[c + ofs]

    return dists[width + caveLen - 1]


# ---
result = run(input)
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
