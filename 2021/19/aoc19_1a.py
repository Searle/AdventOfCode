# https://adventofcode.com/2021/day/19
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def add(arr, key, value):
    arr[key] = arr[key] + value if key in arr else value


def run():

    orients = [
        lambda p: (-p[0], -p[1], p[2]),
        lambda p: (-p[0], -p[2], -p[1]),
        lambda p: (-p[0], p[1], -p[2]),
        lambda p: (-p[0], p[2], p[1]),
        lambda p: (-p[1], -p[0], -p[2]),
        lambda p: (-p[1], -p[2], p[0]),
        lambda p: (-p[1], p[0], p[2]),
        lambda p: (-p[1], p[2], -p[0]),
        lambda p: (-p[2], -p[0], p[1]),
        lambda p: (-p[2], -p[1], -p[0]),
        lambda p: (-p[2], p[0], -p[1]),
        lambda p: (-p[2], p[1], p[0]),
        lambda p: (p[0], -p[1], -p[2]),
        lambda p: (p[0], -p[2], p[1]),
        lambda p: (p[0], p[1], p[2]),
        lambda p: (p[0], p[2], -p[1]),
        lambda p: (p[1], -p[0], p[2]),
        lambda p: (p[1], -p[2], -p[0]),
        lambda p: (p[1], p[0], -p[2]),
        lambda p: (p[1], p[2], p[0]),
        lambda p: (p[2], -p[0], -p[1]),
        lambda p: (p[2], -p[1], p[0]),
        lambda p: (p[2], p[0], p[1]),
        lambda p: (p[2], p[1], -p[0]),
    ]

    scannerProbes = []
    probes = []
    for i in input:
        if i.startswith('---'):
            if len(probes):
                scannerProbes.append(probes)
                probes = []
            next
        p = i.split(',')
        if len(p) == 3:
            probes.append((int(p[0]), int(p[1]), int(p[2])))
    if len(probes):
        scannerProbes.append(probes)
        probes = []

    def mktests(sc, orient):
        for pivot_i in range(len(scannerProbes[sc])):
            pivot = scannerProbes[sc][pivot_i]
            for sp_i in range(pivot_i + 1, len(scannerProbes[sc])):
                sp = scannerProbes[sc][sp_i]
                rel = orient((sp[0] - pivot[0],
                              sp[1] - pivot[1],
                              sp[2] - pivot[2]))
                yield (rel, sp_i, pivot_i)
                rel = orient((pivot[0] - sp[0],
                              pivot[1] - sp[1],
                              pivot[2] - sp[2]))
                yield (rel, pivot_i, sp_i)

    lookup = {}
    for orient_i in range(len(orients)):
        for (rel, sp0_i, sp1_i) in mktests(0, orients[orient_i]):
            if not rel in lookup:
                lookup[rel] = []
            lookup[rel].append((orient_i, sp0_i, sp1_i))

    for sc in range(1, len(scannerProbes)):
        same = {}
        for (rel, sp0_i, sp1_i) in mktests(sc, orients[0]):
            if rel in lookup:
                for v in lookup[rel]:
                    add(same, v[0], 1)
        print(sc, same)

    """
        same = 0
        sc1 = 1
        pivot = scannerProbes[sc1][0]
        for sp in scannerProbes[sc1][1:]:
            rel = orient((sp[0]-pivot[0], sp[1]-pivot[1], sp[1]-pivot[1]))
            if rel in lookup:
                same += 1

        print("SAME", same)
    """

    # print(len(lookup.keys()))

    exit()

    return 0


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
