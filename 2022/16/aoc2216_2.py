# https://adventofcode.com/2022/day/16

from pathlib import Path
import re

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    rows = 4_000_000 if ref == 0 else 20

    devices = set()
    sensors = []

    for input in inputs:
        m = re.match(
            r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', input)
        assert m is not None

        [sx, sy, bx, by] = [int(m[1]), int(m[2]), int(m[3]), int(m[4])]
        devices.add((sx, sy))
        devices.add((bx, by))

        slen = abs(bx - sx) + abs(by - sy)
        sensors.append((sx, sy, slen))

    result = 0

    for y in range(0, rows):
        ranges = []
        for (sx, sy, slen) in sensors:
            slen1 = slen - y + sy if y > sy else slen + y - sy
            if slen1 >= 0:
                ranges.append((sx - slen1, sx + slen1))

        ranges.sort(key=lambda r: r[0])
        i = 0
        while i < len(ranges) - 1:
            r0 = ranges[i]
            r1 = ranges[i + 1]
            if r0[1] >= r1[0] - 1:
                ranges.pop(i + 1)
                ranges[i] = (r0[0], max(r0[1], r1[1]))
            else:
                i += 1

        if len(ranges) > 1:
            result = (ranges[0][1] + 1) * 4_000_000 + y
            break

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
