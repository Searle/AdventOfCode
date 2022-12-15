# https://adventofcode.com/2022/day/7
from pathlib import Path
import re

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    paths = []
    in_ls = False

    sizes = {}

    for input in inputs:
        if in_ls:
            if not input.startswith('$'):
                m = re.match(r'^(\d+) (\S+)', input)
                if m:
                    for pi in range(0, len(paths) + 1):
                        path = "/".join(paths[:pi])
                        if path in sizes:
                            sizes[path] += int(m[1])
                        else:
                            sizes[path] = int(m[1])
                continue

        if input == '$ cd ..':
            paths = paths[:-1]
            continue

        if input == '$ cd /':
            paths = []
            continue

        if input.startswith('$ cd '):
            paths.append(input[5:])
            continue

        if input == '$ ls':
            in_ls = True
            continue

        assert False, "Unknown command: " + input

    needed = sizes[""] - 40_000_000
    dirs = sorted([i for i in sizes.keys() if sizes[i]
                   >= needed], key=lambda i: sizes[i])

    result = sizes[dirs[0]]

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
