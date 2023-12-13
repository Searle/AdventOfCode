# https://adventofcode.com/2023/day/04

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
        def process1(maze):
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
                if dist > best_dist:
                    best_dist = dist
                    best = i
            return best + 1

        t_maze = [""] * len(maze[0])
        for x in range(0, len(maze[0])):
            for y in range(0, len(maze)):
                t_maze[x] += maze[y][x]

        vbest = process1(maze)
        hbest = process1(t_maze)
        assert vbest != hbest, maze

        return vbest * 100 if vbest > hbest else hbest

    mazes = re.split(r"\n\n", "\n".join(inputs))
    for maze in mazes:
        result += process(maze.split("\n"))

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
