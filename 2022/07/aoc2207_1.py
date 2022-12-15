# https://adventofcode.com/2022/day/7
from pathlib import Path
import re
from functools import reduce

ref = 0
part = "_1"

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

    result = reduce(lambda a, b: a+b,
                    (sizes[i] for i in sizes.keys() if sizes[i] <= 100000))

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
