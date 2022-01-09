# https://adventofcode.com/2021/day/3
from pathlib import Path

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

inxs = range(len(input[0]))


def rating(keep, drop):
    bits = [i for i in input]
    for inx in inxs:
        partitioned = {'0': [], '1': []}
        for bit in bits:
            partitioned[bit[inx]].append(bit)
        bits = partitioned[keep] if len(partitioned['1']) >= len(
            partitioned['0']) else partitioned[drop]

        assert len(bits) > 0, "len(bits) == 0 ???"

        if len(bits) == 1:
            return int(bits[0], 2)


result = str(rating('1', '0') * rating('0', '1'))

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
