# https://adventofcode.com/2022/day/16

from pathlib import Path
from itertools import chain
import re

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    sources = []
    sources_d = {}

    target_usage = {}
    for input in inputs:
        m = re.fullmatch(
            r'Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', input)
        assert m is not None

        s, flow, targets = m[1], int(m[2]), m[3].split(', ')

        targets3 = []
        for t in targets:
            if t in target_usage:
                target_usage[t] += 1
            else:
                target_usage[t] = 1
            targets3.append((t, 1))

        # sources.append((s, flow, targets, targets3))
        sources_d[s] = (flow, targets3)

    def opt_graph2():
        print("TARGET_USAGE", target_usage)
        for k in target_usage.keys():
            if target_usage[k] == 1:
                pass

        done = False
        while not done:
            done = True
            dels = set()
            dels2 = {}
            for s in sources_d.keys():
                if s in dels:
                    continue

                flow, targets = sources_d[s]
                next_targets = []
                for t, dist in targets:
                    if target_usage[t] == 1:
                        for t2xxx in sources_d[t][1]:
                            next_targets.append((t2xxx[0], dist + 1))
                        dels2[s] = t
                        # done = False
                    else:
                        next_targets.append((t, dist))
                sources_d[s] = (flow, next_targets)

            print("DELS", dels)

    def opt_graph():
        nonlocal target_usage

        while True:
            dels = {}
            for sk in sources_d.keys():
                for tt in sources_d[sk][1]:
                    if target_usage[tt[0]] == 1:
                        dels[sk] = tt
            if len(dels.keys()) == 0:
                break

            next_target_usage = {}
            for sk in sources_d.keys():
                if not sk in dels:
                    flow, targets = sources_d[sk]
                    next_targets = []
                    for (tk, tdist) in targets:
                        if tk in dels:
                            (delk, deldist) = dels[tk]
                            if sk != delk:
                                print("Correct", sk, tk, delk, deldist,
                                      (delk, tdist + deldist))

                                sources_d[delk][1].append(
                                    (sk, tdist + deldist))
                                tk = delk
                                tdist += deldist

                        next_targets.append((tk, tdist))

                        if tk in next_target_usage:
                            next_target_usage[tk] += 1
                        else:
                            next_target_usage[tk] = 1
                    sources_d[sk] = (flow, next_targets)
            for sk in dels.keys():
                del sources_d[sk]
            target_usage = next_target_usage
            print("DELS", dels)
            print("NS", sources_d)
            print("NT", target_usage)
            break

    def print_graphviz_old():
        print("digraph {")
        for s, flow, targets in sources:
            print(s, '[label="' + s + ' (' + str(flow) + ')"]')
            for t in targets:
                print(s, "->", t)
        print("}")

    def print_graphviz():
        print("digraph {")
        for sk in sources_d.keys():
            flow, targets = sources_d[sk]
            print(sk, '[label="' + sk + ' (' + str(flow) + ')"]')
            for t, dist in targets:
                print(sk, "->", t, '[label="' + str(dist) + '"]')
        print("}")

    print("SD", sources_d)
    print("TU", target_usage)
    opt_graph()
    print_graphviz()
    print("TU", target_usage)

    result = 0
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
