# https://adventofcode.com/2023/day/05

from pathlib import Path
import re
from typing import List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    m = re.fullmatch(r"seeds: (.*)", inputs.pop(0))
    assert m is not None
    inputs.pop(0)

    seeds = [int(i) for i in m[1].split(" ")]
    print(seeds)

    amaps = []
    while len(inputs) > 0:
        m = re.fullmatch(r"(.*):", inputs.pop(0))
        assert m is not None

        aranges = []
        while len(inputs):
            m = re.fullmatch(r".+", inputs.pop(0))
            if m is None:
                break

            aranges.append([int(i) for i in m[0].split(" ")])

        amaps.append(aranges)

    def xxx_2(amapi: int, seeds: List[int]):
        aranges = amaps[amapi]
        seeds2 = []
        for seed in seeds:
            seed2 = seed
            for arange in aranges:
                [dest, source, rlen] = arange
                sdiff = seed - source
                if sdiff >= 0 and sdiff < rlen:
                    seed2 = dest + sdiff
            seeds2.append(seed2)

        # if amapi < len(amaps) - 1:
        #     xxx(amapi + 1, seeds2)
        # else:
        #    print(seeds2)

        print(seeds2)

    # 177942185

    def xxx():
        nonlocal seeds
        nonlocal result
        for aranges in amaps:
            seeds2 = []
            for seed in seeds:
                seed2 = seed
                for arange in aranges:
                    [dest, source, rlen] = arange
                    sdiff = seed - source
                    if sdiff >= 0 and sdiff < rlen:
                        seed2 = dest + sdiff
                seeds2.append(seed2)
            seeds = seeds2

        print(seeds)

        # if amapi < len(amaps) - 1:
        #     xxx(amapi + 1, seeds2)
        # else:
        #    print(seeds2)
        result = min(seeds)

    xxx()

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
