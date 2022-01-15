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

    orients2d = [
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
                    yield (orient(pdiff(sp, pivot)), pivot_i, sp_i, True)
                    pass

    # For each scanner, calculate the distances of all points to each other
    lookup = {}
    for sc in range(len(scannerProbes)):
        for orient_i, orient in enumerate(orients):
            # print("***", sc, orient_i)
            for (distance, sp0_i, sp1_i, inverse) in mktests(sc, orient, True):
                if not distance in lookup:
                    lookup[distance] = []
                lookup[distance].append((sc, orient_i, sp0_i, sp1_i, inverse))
                # print("LOOKUP", rel, (sc, orient_i, sp0_i, sp1_i, inverse))

    # print(lookup)
    # exit()

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
        print("SAME", sc0, same)

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
            lastSpdiff = None
            for (sp00_i, sp01_i, sp10_i, sp11_i, inv1) in rels[sc0][key]:
                sp00 = scannerProbes[sc0][sp00_i]
                # sp01 = scannerProbes[sc0][sp01_i]
                # print("A", sc0, 0, sp00_i,
                #      sp01_i, sp00, sp01, pdiff(sp00, sp01))

                sp10 = scannerProbes[sc1][sp10_i]
                # sp11 = scannerProbes[sc1][sp11_i]
                sp10o = orients[orient1_i](sp10)
                # sp11o = orients[orient1_i](sp11)
                # print("B", sc1, orient1_i, sp10_i,
                #       sp11_i, sp10o, sp11o, pdiff(sp10o, sp11o), "(", sp10, sp11, ")")

                spdiff = pdiff(sp10o, sp00)
                if lastSpdiff == None:
                    lastSpdiff = spdiff
                elif spdiff != lastSpdiff:
                    print("DIFF!")  # Kommt nur bei input_ref2.txt vor
                    lastSpdiff = None
                    break

                # print("SPXX", sp00, sp10o, spdiff, inv1)

            if lastSpdiff != None:
                print("FOUND", sc0, "=>", sc1, orient1_i, lastSpdiff)
                # print("(", sc0, ",", sc1, ",0,0),")
                scannerRules.append((sc0, sc1, orient1_i, lastSpdiff))

    scannerRulesX = [
        (0, 1, 0, 0),
        (1, 2, 0, 0),
        (2, 3, 0, 0),
        (2, 4, 0, 0),
        (2, 5, 0, 0),
        (4, 5, 0, 0),
    ]

    scannerRulesY = [
        (0, 6, 0, 0),
        (0, 22, 0, 0),
        (1, 5, 0, 0),
        (1, 16, 0, 0),
        (1, 15, 0, 0),
        (1, 17, 0, 0),
        (2, 9, 0, 0),
        (2, 4, 0, 0),
        (3, 20, 0, 0),
        (3, 4, 0, 0),
        (3, 5, 0, 0),
        (3, 17, 0, 0),
        (4, 11, 0, 0),
        (5, 8, 0, 0),
        (5, 14, 0, 0),
        (6, 11, 0, 0),
        (6, 7, 0, 0),
        (7, 24, 0, 0),
        (7, 10, 0, 0),
        (8, 20, 0, 0),
        (8, 22, 0, 0),
        (9, 11, 0, 0),
        (11, 20, 0, 0),
        (11, 22, 0, 0),
        (12, 25, 0, 0),
        (12, 20, 0, 0),
        (13, 18, 0, 0),
        (14, 15, 0, 0),
        (14, 18, 0, 0),
        (14, 23, 0, 0),
        (15, 19, 0, 0),
        (19, 23, 0, 0),
        (21, 24, 0, 0),
    ]

    def yy():
        def compose(g, f):
            def h(x):
                return g(f(x))
            return h

        o = orients[0]

        for sc0, sc1, orient1_i, offset in scannerRules:
            sp0s = sorted(scannerProbes[sc0])
            sp1s = sorted(scannerProbes[sc1], reverse=True)

            o = compose(o, orients[orient1_i])

            for i, sp in enumerate(sp0s):
                print(i, sp, padd(o(sp1s[i]), offset))

            break

        exit()

    # yy()

    def compose(f, g):
        return lambda x: f(g(x))

    def mktrans(o, offset):
        return lambda a: padd(o(a), offset)

    def xx():

        seen = {}
        next = []

        points = {}

        for p in scannerProbes[0]:
            points[p] = True

        def add(info, sc, trans):
            nonlocal points

            ycount = 0
            ncount = 0
            for i, sp in enumerate(scannerProbes[sc]):
                p = trans(sp)
                if p in points:
                    ycount += 1
                else:
                    ncount += 1
                points[p] = True
                # print(i, sp, padd(o(sp1s[i]), offset))

            print("COUNT", info, sc, ycount, ncount)

        def check1a(sc, trans):
            nonlocal seen
            nonlocal next

            for sc0, sc1, orient1_i, offset in scannerRules:
                if sc == sc0 and not sc1 in seen:
                    seen[sc0] = True
                    next.append((sc0, ">", sc1))
                    trans1 = compose(trans, mktrans(
                        orients[orient1_i], offset))
                    add(str(sc0) + ">", sc1, trans1)
                    check1a(sc1, trans1)

                if sc == sc1 and not sc0 in seen:
                    seen[sc1] = True
                    next.append((sc1, ">", sc0))

                    def mkinvtrans(inv_o, offset):
                        return lambda a: inv_o(psub(a, offset))

                    trans1 = compose(trans, mkinvtrans(
                        inv_orients[orient1_i], offset))
                    add("<" + str(sc1), sc0, trans1)
                    check1a(sc0, trans1)

            print

        check1a(0, lambda a: a)
        for i in next:
            print(i)

        print(len(points.keys()))

    xx()

    """


def compose(g, f):
        def h(x):
            return g(f(x))
        return h

    o = orients[0]

    for sc0, sc1, orient1_i, offset in scannerRules:
        sp0s = sorted(scannerProbes[sc0])
        sp1s = sorted(scannerProbes[sc1], reverse=True)

        o = compose(o, orients[orient1_i])

        for i, sp in enumerate(sp0s):
            print(i, sp, padd(o(sp1s[i]), offset))

        break


    def check0():
        nonlocal done

        for sc0, sc1, orient1_i, offset in scannerRules:
            # if sc0 in done:
            #     continue

            if any(r[1] == sc0 for r in scannerRules):
                continue

            if not sc0 in done and sc1 in done:
                print("DOREV", sc0, "<-", sc1)
                done[sc0] = True

            if sc1 in done:
                continue

            next = []
            check1(sc0, next)
            print("NEXT", sc0, next)
            for i, sc1 in enumerate(next):
                if not sc1 in done:
                    print("DO", sc0, "->", sc1)
                    done[sc1] = True
                sc0 = sc1

            break

        # print("CHECK1", sc)

    # for i in range(100):
    #     check0()
    # check1(0)

    print("DONE", sorted(done.keys()))


    exit()

    done = {}

    def check1(sc1p, next, seen={}):
        for sc0, sc1, orient1_i, offset in scannerRules:
            if sc1 in done:
                continue

            # if sc0 in seen:
            #     continue

            if sc1p == sc0:
                # print("> CHECK1?", sc0, sc1, seen)
                next.append(sc1)
                check1(sc1, next, {**seen, sc0: True})
                return

        # print("CHECK1", sc1p, seen)
        # done[sc1p] = True
        # next.append(sc1p)
        # return sc1p

    def check0():
        nonlocal done

        for sc0, sc1, orient1_i, offset in scannerRules:
            # if sc0 in done:
            #     continue

            if any(r[1] == sc0 for r in scannerRules):
                continue

            if not sc0 in done and sc1 in done:
                print("DOREV", sc0, "<-", sc1)
                done[sc0] = True

            if sc1 in done:
                continue

            next = []
            check1(sc0, next)
            print("NEXT", sc0, next)
            for i, sc1 in enumerate(next):
                if not sc1 in done:
                    print("DO", sc0, "->", sc1)
                    done[sc1] = True
                sc0 = sc1

            break

        # print("CHECK1", sc)

    for i in range(100):
        check0()
    # check1(0)

    print("DONE", sorted(done.keys()))

    exit()

    foundTask = True
    while foundTask:
        foundTask = False
        for sc0, sc1, orient1_i, offset in scannerRules:
            if sc1 in done:
                continue

            if any(r[0] == sc1 for r in scannerRules):
                continue

            print("DO", sc1)
            done[sc1] = True
            foundTask = True

    print("")

    exit()

    dep = {}
    blocked = {}
    done = {0: True}
    for sc0, sc1, orient1_i, offset in scannerRules:
        if sc1 in done:
            continue

        blocked[sc1] = True

    for sc0, sc1, orient1_i, offset in scannerRules:
        if sc0 in done and not sc1 in done:
            print("DO", sc0, sc1)

    print(dep)
    print(blocked)

    exit()

    dep = {}
    blocked = {}
    for sc0, sc1, orient1_i, offset in scannerRules:
        if not sc0 in dep:
            dep[sc0] = []
        if not sc1 in dep:
            dep[sc1] = []
        dep[sc0].append((sc0, sc1, orient1_i, offset))

    fixes = {}
    for k, v in dep.items():
        if v == []:
            fixes[k] = True

    print(dep)
    print(fixes)

    exit()

    done = {}

    finished = False
    while not finished:
        finished = True

        print("\n\n")
        print(scannerRules)
        print(done)

        hasDeps = {}
        check = {}
        for sc0, sc1, orient1_i, offset in scannerRules:
            if sc0 in done:
                check[sc1] = True
                continue

            check[sc0] = True
            hasDeps[sc1] = True

        for sc0 in check:
            if sc0 in done:
                continue

            finished = False

            if sc0 in hasDeps:
                continue

            print("DO", sc0)
            done[sc0] = True
            break

    exit()

    def compose(g, f):
        def h(x):
            return g(f(x))
        return h

    o = orients[0]

    for sc0, sc1, orient1_i, offset in scannerRules:
        sp0s = sorted(scannerProbes[sc0])
        sp1s = sorted(scannerProbes[sc1], reverse=True)

        o = compose(o, orients[orient1_i])

        for i, sp in enumerate(sp0s):
            print(i, sp, padd(o(sp1s[i]), offset))

        break

    exit()

    """

    return 0


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
