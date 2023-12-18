# https://adventofcode.com/2023/day/18

from pathlib import Path
import re
from typing import Dict, Set, List
from PIL import Image

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    maze = set()
    mx0 = 0
    mx1 = 9999999
    my0 = 0
    my1 = 9999999

    def print_maze(msg):
        print("---", msg, "---")

        # s0 = ""
        for y in range(my0, my1 + 1):
            s = ""
            for x in range(mx0, mx1 + 1):
                s += "#" if (x, y) in maze else " "
            print(s)
            # s0 += s + "\n"

        # with open("maze.txt", "w") as file:
        #     file.write(s0)

    def save_maze_png(prefix):
        # Create a new image with RGB mode
        width, height = mx1 - mx0 + 1, my1 - my0 + 1  # Define the size of the image
        image = Image.new("RGB", (width, height))

        # Draw some pixels (example)
        pixels = image.load()
        for x in range(width):
            for y in range(height):
                if (x + mx0, y + my0) in maze:
                    pixels[x, y] = (0, 0, 0)
                else:
                    pixels[x, y] = (255, 255, 255)

        pixels[(mx1 - mx0) // 2, (my1 - my0) * 12 // 20] = (255, 50, 50)

        # Save the image
        image.save("2023/18/maze-" + prefix + ext + ".png")

    px = 0
    py = 0
    for input in inputs:
        m = re.fullmatch(r"(\S) (\d+).*", input)
        assert m is not None, "NOT MATCHED: " + input

        dirs = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}
        dx = dirs[m[1]][0]
        dy = dirs[m[1]][1]
        for _ in range(0, int(m[2])):
            px += dx
            py += dy
            maze.add((px, py))

        pass

    mx0 = min([xy[0] for xy in maze])
    mx1 = max([xy[0] for xy in maze])
    my0 = min([xy[1] for xy in maze])
    my1 = max([xy[1] for xy in maze])

    save_maze_png("outline")

    cx = (mx0 + mx1) // 2
    cy = (my0 + my1) * 8 // 20
    print("CENTER", cx, cy, mx0, mx1, my0, my1)

    dirs2 = ((-1, 0), (1, 0), (0, -1), (0, 1))

    toFill = set()
    toFill.add((cx, cy))
    foundOne = True
    while foundOne:
        foundOne = False
        nextToFill = set()
        for pos in toFill:
            maze.add(pos)
            for dir in dirs2:
                next = (pos[0] + dir[0], pos[1] + dir[1])
                if not next in toFill and not next in maze:
                    nextToFill.add(next)
                    foundOne = True
        toFill = nextToFill

    # print_maze("DONE")
    save_maze_png("fill")

    result = len(maze)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
