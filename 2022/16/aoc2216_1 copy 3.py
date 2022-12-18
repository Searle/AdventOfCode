# https://adventofcode.com/2022/day/16

from pathlib import Path
from itertools import chain
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    nodes = {}

    target_usage = {}
    for input in inputs:
        m = re.fullmatch(
            r'Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', input)
        assert m is not None

        nodes[m[1]] = (int(m[2]), [(t, 1) for t in m[3].split(', ')])

    def remove_intermediates():

        cont = True
        while cont:
            cont = False

            incomings = {}
            for nk in nodes.keys():
                for tk, _ in nodes[nk][1]:
                    if tk in incomings:
                        incomings[tk].add(nk)
                    else:
                        incomings[tk] = {nk}

            for nk in nodes.keys():
                if nk != 'AA' and nodes[nk][0] == 0 and len(nodes[nk][1]) == 2 and len(incomings[nk]) == 2:
                    targets = nodes[nk][1]
                    t0k, t0dist = targets[0]
                    t1k, t1dist = targets[1]

                    def bridge(t0k, t1k, t1dist):
                        tt = nodes[t0k][1]
                        for i, (tk, tdist) in enumerate(tt):
                            if tk == nk:
                                tt[i] = (t1k, tdist + t1dist)

                    bridge(t0k, t1k, t1dist)
                    bridge(t1k, t0k, t0dist)
                    del nodes[nk]
                    cont = True
                    break

    def solve():

        best = 0
        closed = {}
        closed_count = 0
        visits = {}
        for nk in nodes:
            closed[nk] = nodes[nk][0] > 0
            closed_count += closed[nk]
            visits[nk] = 0

        DEBUG = False
        dpath = ["DD", "+", "CC", "BB", "+", "AA", "JJ", "+", "AA", "DD", "EE", "HH",
                 "+", "EE", "+", "DD", "CC", "+", "", "", "", "", ""]
        dpath_i = -1

        def traverse(nk, time, score, pressure, path):
            nonlocal closed_count, best, dpath_i, DEBUG

            flow, targets = nodes[nk]
            # score += pressure
            dpath_i += 1

            if DEBUG:
                print("==", dpath_i, dpath[dpath_i], score, pressure)

            # lohnt sonst den Sprung und ggfs Valve-Oeffnen nicht
            if visits[nk] >= len(targets) or closed_count == 0 or time >= 29:
                score1 = score + (30 - time) * pressure
                if score1 > best:
                    best = score1
                    print("BEST", best, pressure,
                          best - (30 - time) * pressure, time,  path)
                return

            if closed[nk] and (not DEBUG or dpath[dpath_i] == "+"):
                closed_count -= 1
                closed[nk] = False
                score1 = score + pressure
                if DEBUG:
                    print("+SCORE1", score1)
                pressure += flow
                traverse(nk, time + 1, score1, pressure, path + nk + "+:")
                closed_count += 1
                closed[nk] = True
                pressure -= nodes[nk][0]

            foundOne = False

            visits[nk] += 1
            for tt in targets:

                if DEBUG and tt[0] != dpath[dpath_i]:
                    continue

                foundOne = True
                score1 = score + tt[1] * pressure
                if DEBUG:
                    print("SCORE1", score1, tt[0], tt[1] * pressure)
                traverse(tt[0], time + tt[1], score1,
                         pressure, path + nk + ":")
            visits[nk] -= 1

            if DEBUG and not foundOne:
                assert dpath[dpath_i] == ""
                score1 = score + (30 - time) * pressure
                if score1 > best:
                    best = score1
                    print("BEST", best, pressure,
                          best - (30 - time) * pressure, time,  path)

        traverse('AA', 0, 0, 0, "")
        return best

    def print_graphviz():
        print("digraph {")
        for nk in nodes.keys():
            flow, targets = nodes[nk]
            print(nk, '[label="' + nk + ' (' + str(flow) + ')"]')
            for t, dist in targets:
                print(nk, "->", t, '[label="' +
                      str(dist) + '" color="#ff0000"]' if dist > 1 else '')
        print("}")

    print("SD", nodes)
    print("TU", target_usage)
    remove_intermediates()
    print_graphviz()
    result = solve()
    print("TU", target_usage)

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
