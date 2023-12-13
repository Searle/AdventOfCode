# https://adventofcode.com/2023/day/04

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    for input in inputs:
        m = re.fullmatch(r"Card\s+(\d+):(.+)\|(.+)", input)
        assert m is not None

        pass

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
