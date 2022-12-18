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

    def opt_graph():
        nonlocal target_usage

        while True:
            dels = {}
            for sk in sources_d.keys():
                for tt in sources_d[sk][1]:
                    if sk != 'AA' and target_usage[tt[0]] == 1:
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
                            if sk == delk:
                                continue
                            print("Correct", sk, tk, delk, deldist,
                                  (delk, tdist + deldist))

                            sources_d[delk][1].append(
                                (sk, tdist + deldist))
                            if sk in next_target_usage:
                                next_target_usage[sk] += 1
                            else:
                                next_target_usage[sk] = 1

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
            # break

    def print_graphviz():
        print("digraph {")
        for sk in sources_d.keys():
            flow, targets = sources_d[sk]
            print(sk, '[label="' + sk + ' (' + str(flow) + ')"]')
            for t, dist in targets:
                print(sk, "->", t, '[label="' +
                      str(dist) + '" color="#ff0000"]' if dist > 1 else '')
        print("}")

    print("SD", sources_d)
    print("TU", target_usage)
    opt_graph()
    # opt_graph()
    # opt_graph()
    print_graphviz()
    print("TU", target_usage)

    result = 0
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
