# https://adventofcode.com/2021/day/19
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def add(arr, key, value):
    arr[key] = arr[key] + value if key in arr else value


def pdiff(p0, p1):
    return (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])


def padd(p0, p1):
    return (p1[0] + p0[0], p1[1] + p0[1], p1[2] + p0[2])


def psub(p0, p1):
    return (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])


def run():

    # Generated with make_orientation.py

    orients = [
        lambda p: (p[0], p[1], p[2]),
        lambda p: (p[1], -p[0], p[2]),
        lambda p: (-p[0], -p[1], p[2]),
        lambda p: (-p[1], p[0], p[2]),
        lambda p: (p[2], p[1], -p[0]),
        lambda p: (p[1], -p[2], -p[0]),
        lambda p: (-p[2], -p[1], -p[0]),
        lambda p: (-p[1], p[2], -p[0]),
        lambda p: (-p[0], p[1], -p[2]),
        lambda p: (p[1], p[0], -p[2]),
        lambda p: (p[0], -p[1], -p[2]),
        lambda p: (-p[1], -p[0], -p[2]),
        lambda p: (-p[2], p[1], p[0]),
        lambda p: (p[1], p[2], p[0]),
        lambda p: (p[2], -p[1], p[0]),
        lambda p: (-p[1], -p[2], p[0]),
        lambda p: (p[0], p[2], -p[1]),
        lambda p: (p[2], -p[0], -p[1]),
        lambda p: (-p[0], -p[2], -p[1]),
        lambda p: (-p[2], p[0], -p[1]),
        lambda p: (-p[0], p[2], p[1]),
        lambda p: (p[2], p[0], p[1]),
        lambda p: (p[0], -p[2], p[1]),
        lambda p: (-p[2], -p[0], p[1]),
    ]

    inv_orients = [
        lambda p: (-p[0], -p[1], -p[2]),
        lambda p: (p[1], -p[0], -p[2]),
        lambda p: (p[0], p[1], -p[2]),
        lambda p: (-p[1], p[0], -p[2]),
        lambda p: (p[2], -p[1], -p[0]),
        lambda p: (p[2], -p[0], p[1]),
        lambda p: (p[2], p[1], p[0]),
        lambda p: (p[2], p[0], -p[1]),
        lambda p: (p[0], -p[1], p[2]),
        lambda p: (-p[1], -p[0], p[2]),
        lambda p: (-p[0], p[1], p[2]),
        lambda p: (p[1], p[0], p[2]),
        lambda p: (-p[2], -p[1], p[0]),
        lambda p: (-p[2], -p[0], -p[1]),
        lambda p: (-p[2], p[1], -p[0]),
        lambda p: (-p[2], p[0], p[1]),
        lambda p: (-p[0], p[2], -p[1]),
        lambda p: (p[1], p[2], -p[0]),
        lambda p: (p[0], p[2], p[1]),
        lambda p: (-p[1], p[2], p[0]),
        lambda p: (p[0], -p[2], -p[1]),
        lambda p: (-p[1], -p[2], -p[0]),
        lambda p: (-p[0], -p[2], p[1]),
        lambda p: (p[1], -p[2], p[0]),
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
                    yield (orient(pdiff(sp, pivot)), pivot_i, sp_i, True)
                    pass

    # For each scanner, calculate the distances of all points to each other
    lookup = {}
    for sc in range(len(scannerProbes)):
        for orient_i, orient in enumerate(orients):
            for (distance, sp0_i, sp1_i, inverse) in mktests(sc, orient, True):
                if not distance in lookup:
                    lookup[distance] = []
                lookup[distance].append((sc, orient_i, sp0_i, sp1_i, inverse))
                # print("LOOKUP", rel, (sc, orient_i, sp0_i, sp1_i, inverse))

    sames = []
    rels = {}
    for sc0 in range(len(scannerProbes)):
        same = {}
        for (distance, sp00_i, sp01_i, _) in mktests(sc0, orients[0]):
            if distance in lookup:
                for v in lookup[distance]:
                    (sc1, orient1_i, sp10_i, sp11_i, inv1) = v
                    if sc1 > sc0:
                        # print("REL", dict(d=distance, sc1=sc1, o1_i=orient1_i, sp0=(
                        #       sp00_i, sp01_i), sp1=(sp10_i, sp11_i), inv1=inv1))
                        key = (sc1, orient1_i)
                        add(same, key, 1)
                        if not sc0 in rels:
                            rels[sc0] = {}
                        if not key in rels[sc0]:
                            rels[sc0][key] = []
                        # Unused: sp10_i, sp11_i, inv1
                        rels[sc0][key].append(
                            (sp00_i, sp01_i, sp10_i, sp11_i, inv1))
        sames.append(same)
        # print("SAME", sc0, same)

    minNN = 3  # bei input_ref2.txt, benoetigt orient2d
    minNN = 66  # bei input_ref1.txt
    minNN = 66  # bei input.txt

    # print("RELS", rels)

    scannerRules = []
    for sc0 in range(len(sames)):
        same = sames[sc0]
        for key in filter(lambda k: same[k] >= minNN, same.keys()):
            (sc1, orient1_i) = key
            # print("SAMERELS", sc0, sc1, orient1_i)
            for (sp00_i, sp01_i, sp10_i, sp11_i, inv1) in rels[sc0][key]:
                sp00 = scannerProbes[sc0][sp00_i]
                sp10 = scannerProbes[sc1][sp10_i]
                sp10o = orients[orient1_i](sp10)
                distance = pdiff(sp10o, sp00)
                scannerRules.append((sc0, sc1, orient1_i, distance))
                # print("FOUND", sc0, "=>", sc1, orient1_i, distance)
                break

    def compose(f, g):
        return lambda x: f(g(x))

    def mktrans(o, offset):
        return lambda a: padd(o(a), offset)

    def mkinvtrans(inv_o, offset):
        return lambda a: inv_o(psub(a, offset))

    seen = {}
    beacons = {}

    for p in scannerProbes[0]:
        beacons[p] = True

    def addBeacons(info, sc, trans):
        nonlocal beacons

        ycount = 0
        ncount = 0
        for sp in scannerProbes[sc]:
            p = trans(sp)
            if p in beacons:
                ycount += 1
            else:
                ncount += 1
            beacons[p] = True

        # print("COUNT", info, sc, ycount, ncount)

    def rulesToBeacons(sc, trans):
        nonlocal seen

        for sc0, sc1, orient1_i, offset in scannerRules:
            if sc == sc0 and not sc1 in seen:
                seen[sc0] = True
                trans1 = compose(trans, mktrans(
                    orients[orient1_i], offset))
                addBeacons(str(sc0) + ">", sc1, trans1)
                rulesToBeacons(sc1, trans1)

            if sc == sc1 and not sc0 in seen:
                seen[sc1] = True
                trans1 = compose(trans, mkinvtrans(
                    inv_orients[orient1_i], offset))
                addBeacons("<" + str(sc1), sc0, trans1)
                rulesToBeacons(sc0, trans1)

    rulesToBeacons(0, lambda a: a)

    return len(beacons.keys())


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
