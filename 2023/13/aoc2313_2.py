# https://adventofcode.com/2023/day/13

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    def process(maze):
        def process1(maze, omit):
            best = -1
            best_dist = 0
            for i in range(0, len(maze)):
                dist = 0
                j = i
                while True:
                    if j - dist < 0 or j + 1 + dist >= len(maze):
                        break
                    if maze[j - dist] != maze[j + dist + 1]:
                        dist = -1
                        break
                    dist += 1
                if dist > best_dist and i + 1 != omit:
                    best_dist = dist
                    best = i
            return best + 1

        t_maze = [""] * len(maze[0])
        for x in range(0, len(maze[0])):
            for y in range(0, len(maze)):
                t_maze[x] += maze[y][x]

        vbest0 = process1(maze, 0)
        hbest0 = process1(t_maze, 0)

        vbest1 = 0
        hbest1 = 0

        for y0 in range(0, len(maze)):
            for x0 in range(0, len(maze[0])):
                maze1 = [""] * len(maze)
                t_maze1 = [""] * len(maze[0])
                for y in range(0, len(maze)):
                    for x in range(0, len(maze[0])):
                        ch = maze[y][x]
                        if y0 == y and x0 == x:
                            ch = "." if ch == "#" else "#"
                        maze1[y] += ch
                        t_maze1[x] += ch

                vbest = process1(maze1, vbest0)
                hbest = process1(t_maze1, hbest0)
                if vbest > 0 or hbest > 0:
                    if vbest1 == 0 and hbest1 == 0:
                        vbest1 = vbest
                        hbest1 = hbest
                    else:
                        if vbest1 != vbest or hbest1 != hbest:
                            assert False, "MISMATCH"

        assert vbest1 != hbest1, maze

        return vbest1 * 100 if vbest1 > hbest1 else hbest1

    mazes = re.split(r"\n\n", "\n".join(inputs))
    for maze in mazes:
        result += process(maze.split("\n"))

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
