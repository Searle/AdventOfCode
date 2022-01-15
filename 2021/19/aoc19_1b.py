# https://adventofcode.com/2021/day/19
from pathlib import Path

ref = True
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def add(arr, key, value):
    arr[key] = arr[key] + value if key in arr else value


def pdiff(p0, p1):
    return (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])


def run():

    orients = [
        lambda p: (p[0],  p[1],  p[2]),
        lambda p: (p[0],  p[2], -p[1]),
        lambda p: (p[0], -p[1], -p[2]),
        lambda p: (p[0], -p[2],  p[1]),
        lambda p: (p[1],  p[0], -p[2]),
        lambda p: (p[1],  p[2],  p[0]),
        lambda p: (p[1], -p[0],  p[2]),
        lambda p: (p[1], -p[2], -p[0]),
        lambda p: (p[2],  p[0],  p[1]),
        lambda p: (p[2],  p[1], -p[0]),
        lambda p: (p[2], -p[0], -p[1]),
        lambda p: (p[2], -p[1],  p[0]),
        lambda p: (-p[0],  p[1], -p[2]),
        lambda p: (-p[0],  p[2],  p[1]),
        lambda p: (-p[0], -p[1],  p[2]),
        lambda p: (-p[0], -p[2], -p[1]),
        lambda p: (-p[1],  p[0],  p[2]),
        lambda p: (-p[1],  p[2], -p[0]),
        lambda p: (-p[1], -p[0], -p[2]),
        lambda p: (-p[1], -p[2],  p[0]),
        lambda p: (-p[2],  p[0], -p[1]),
        lambda p: (-p[2],  p[1],  p[0]),
        lambda p: (-p[2], -p[0],  p[1]),
        lambda p: (-p[2], -p[1], -p[0]),
    ]

    orients = [
        lambda p: (p[0],  p[1],  p[2]),
        lambda p: (p[1], -p[0],  p[2]),
        lambda p: (-p[0], -p[1],  p[2]),
        lambda p: (-p[1],  p[0],  p[2]),
    ]

    scannerProbes = []
    probes = []
    for i in input:
        if i == "EOF":
            break
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

    def mktests(sc, orient, biDirection=False):
        for pivot_i in range(len(scannerProbes[sc])):
            pivot = scannerProbes[sc][pivot_i]
            for sp_i in range(pivot_i + 1, len(scannerProbes[sc])):
                sp = scannerProbes[sc][sp_i]
                yield (orient(pdiff(pivot, sp)), sp_i, pivot_i, False)
                if biDirection:
                    yield (orient(pdiff(sp, pivot)), sp_i, pivot_i, True)

    # For each scanner, calculate the distances of all points to each other
    lookup = {}
    for sc in range(len(scannerProbes)):
        for orient_i, orient in enumerate(orients):
            # print("***", sc, orient_i)
            for (rel, sp0_i, sp1_i, inverse) in mktests(sc, orient, True):
                if not rel in lookup:
                    lookup[rel] = []
                # TODO: Nur die ersten beiden Werte genutzt
                lookup[rel].append((sc, orient_i, sp0_i, sp1_i, inverse))
                print("LOOKUP", rel, (sc, orient_i, sp0_i, sp1_i, inverse))

    # print(lookup)
    # exit()

    sames = []
    rels = {}
    for sc in range(0, 2):
        same = {}
        for (rel, sp0_i, sp1_i, inverse) in mktests(sc, orients[0]):
            if rel in lookup:
                for v in lookup[rel]:
                    sc1 = v[0]
                    orient1_i = v[1]
                    if sc1 > sc:
                        print("REL", rel, sc1, orient1_i, sp0_i, sp1_i)
                        key = (sc1, orient1_i)
                        add(same, key, 1)
                        if not sc in rels:
                            rels[sc] = {}
                        if not key in rels[sc]:
                            rels[sc][key] = []
                        rels[sc][key].append((sp0_i, sp1_i))
        sames.append(same)
        print("SAME", sc, same)

    minN = 12
    minNN = 3

    print("RELS", rels)

    # TODO: same = len(rels)

    for sc0 in range(len(sames)):
        same = sames[sc0]
        for key in filter(lambda k: same[k] >= minNN, same.keys()):
            (sc1, orient1_i) = key
            print(sc0, sc1, orient1_i)
            for (sp0_i, sp1_i) in rels[sc0][key]:
                sp0 = scannerProbes[sc0][sp0_i]
                sp1 = scannerProbes[sc1][sp1_i]
                print("A", sc0, sc1, orient1_i, sp0_i,
                      sp1_i, sp0, sp1, pdiff(sp0, sp1))
                sp0 = scannerProbes[sc0][sp0_i]
                sp1 = orients[orient1_i](scannerProbes[sc1][sp1_i])
                print("B", sc0, sc1, orient1_i, sp0_i,
                      sp1_i, sp0, sp1, pdiff(sp0, sp1))
                sp0 = orients[orient1_i](scannerProbes[sc0][sp0_i])
                sp1 = scannerProbes[sc1][sp1_i]
                print("C", sc0, sc1, orient1_i, sp0_i,
                      sp1_i, sp0, sp1, pdiff(sp0, sp1))
            break
        break

    exit()

    sames = []
    rels = {}
    for sc in range(len(scannerProbes)):
        same = {}
        for (rel, sp0_i, sp1_i, inverse) in mktests(sc, orients[0]):
            if rel in lookup:
                for v in lookup[rel]:
                    if v[0] > sc:
                        if sc == 0 and v[0] == 1:
                            print("REL", rel, lookup[rel])
                        add(same, (v[0], v[1]), 1)
                        if not inverse:
                            if not sc in rels:
                                rels[sc] = {}
                            rels[sc][(sp0_i, sp1_i)] = ((sp0_i, sp1_i))
        # print(sc, same)
        sames.append(same)

    for sc0 in range(len(sames)):
        same = sames[sc0]
        for (sc1, orient1_i) in filter(lambda k: same[k] >= 132, same.keys()):
            print(sc0, sc1, orient1_i)
            for (sp0_i, sp1_i) in rels[sc0].keys():
                sp0 = scannerProbes[sc0][sp0_i]
                sp1 = orients[orient1_i](scannerProbes[sc1][sp1_i])
                # print(sc0, sc1, sp0_i, sp1_i, sp0, sp1, pdiff(sp0, sp1))
            break
        break

    # print(rels)
    # print(len(lookup.keys()))

    exit()

    return 0


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
