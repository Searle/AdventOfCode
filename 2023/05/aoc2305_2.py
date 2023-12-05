# https://adventofcode.com/2023/day/05

from pathlib import Path
import re
from typing import List

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
inputs = [input for input in inputs if not input.startswith("#")]

# ---


def run():
    result = 0

    m = re.fullmatch(r"seeds: (.*)", inputs.pop(0))
    assert m is not None
    inputs.pop(0)

    seeds = [int(i) for i in m[1].split(" ")]

    amaps = []
    amapsName = []
    while len(inputs) > 0:
        m = re.fullmatch(r"(.*):", inputs.pop(0))
        assert m is not None

        amapsName.append(m[1])
        aranges = []
        while len(inputs):
            m = re.fullmatch(r".+", inputs.pop(0))
            if m is None:
                break

            aranges.append([int(i) for i in m[0].split(" ")])

        amaps.append(aranges)

    def run():
        nonlocal seeds

        nextSeeds = seeds
        seeds = []
        for i in range(0, len(nextSeeds), 2):
            seeds.append(nextSeeds[i])
            seeds.append(nextSeeds[i] + nextSeeds[i + 1])

        for aranges in amaps:
            nextSeeds = []
            for n in range(0, len(seeds), 2):
                seed0 = seeds[n]
                seed1 = seeds[n + 1]
                shifts = [(seed0, seed1, seed0, seed1)]

                for arange in aranges:
                    [dest, source, rlen] = arange
                    nextShifts = []
                    for i in range(0, len(shifts)):
                        s = shifts[i]
                        (s0, s1, *_) = s
                        source0 = source
                        source1 = source + rlen
                        offs = dest - source
                        if s1 <= source0 or s0 >= source1:
                            nextShifts.append(s)
                            continue

                        if s0 < source0:
                            nextShifts.append((s0, source, s0, source))
                            s0 = source0
                        if s1 > source1:
                            nextShifts.append((source1, s1, source1, s1))
                            s1 = source1
                        if s0 >= source0 and s1 <= source1 and s0 != s1:
                            nextShifts.append((s0, s1, s0 + offs, s1 + offs))

                    shifts = nextShifts

                for i in range(0, len(shifts)):
                    nextSeeds.append(shifts[i][2])
                    nextSeeds.append(shifts[i][3])

            seeds = nextSeeds

        return min(seeds)

    result = run()

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
