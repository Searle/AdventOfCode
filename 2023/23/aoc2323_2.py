# https://adventofcode.com/2023/day/23

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

    mw = len(inputs[0])
    mh = len(inputs)
    tr = {"#": 0, "*": 1, ".": 2, "^": 3, ">": 4, "v": 5, "<": 6}

    maze = [tr[ch] for ch in "".join(inputs)]
    maze[1] = 0
    maze[len(maze) - 2] = 1
    start = mw + 1

    dirs = (-mw, 1, mw, -1)
    fills = {}

    def co(pos):
        return str(pos % mw) + "," + str(pos // mw)

    def print_maze():
        for y in range(0, mh):
            s = ""
            for x in range(0, mw):
                pos = y * mw + x
                c = maze[pos]
                if c == 0:
                    s += "<->"
                elif pos in fills:
                    s += str(fills[pos][0]).rjust(2) + str(len(fills[pos][2]))
                else:
                    s += " " + "#*.^>v<"[c] + " "
            print("MAZE", s)
        print("")

    def print_dot(edges):
        print("graph {")
        for node0, node1, len1 in edges:
            print(
                '"' + co(node0) + '" -- "' + co(node1) + '" [label="' + str(len1) + '"]'
            )
        print("}")

    toFill = {start: (0, 1, set())}
    foundOne = True
    while foundOne:
        foundOne = False
        nextToFill = {}
        for pos in toFill:
            fill, prevPos, prevs = toFill[pos]
            fills[pos] = (fill, prevPos, prevs)
            nextFill = fill + 1
            for dir in dirs:
                pos1 = pos + dir

                if maze[pos1] < 2:
                    if maze[pos1] == 1:
                        fills[pos1] = (nextFill, pos, {pos})
                        result = nextFill + 1
                    continue

                if pos1 in fills:
                    fills[pos1][2].add(pos)
                    fills[pos][2].add(pos1)
                    continue

                nextToFill[pos1] = (nextFill, pos, {pos})

            foundOne = True
        toFill = nextToFill

    edges = set()
    for pos, fill in fills.items():
        if len(fill[2]) > 2:
            for prev in fill[2]:
                pos1 = pos
                prevPrevs = list(fills[prev][2])
                next = pos
                len1 = 1
                while len(prevPrevs) == 2:
                    next = prevPrevs[0] if prevPrevs[0] != pos1 else prevPrevs[1]
                    pos1 = prev
                    prev = next
                    prevPrevs = list(fills[prev][2])
                    len1 += 1

                if not (next, pos, len1) in edges:
                    edges.add((pos, next, len1))

    def find_longest_path_length(
        edges: List[Tuple[int, int, int]], start: int, end: int
    ) -> int:
        graph = {}
        for edge in edges:
            node0, node1, length = edge
            if node0 not in graph:
                graph[node0] = []
            if node1 not in graph:
                graph[node1] = []
            graph[node0].append((node1, length))
            graph[node1].append((node0, length))

        def backtrack(node, visited, current_length):
            nonlocal longest_length
            if node == end:
                longest_length = max(longest_length, current_length)
                return
            for neighbor, length in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    backtrack(neighbor, visited, current_length + length)
                    visited.remove(neighbor)

        longest_length = 0
        backtrack(start, {start}, 0)
        return longest_length

    result = find_longest_path_length(list(edges), mw + 1, len(maze) - mw - 2) + 2

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
