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

        sources.append((s, flow, targets, targets3))
        sources_d[s] = (s, flow, targets, targets3)

    print("TARGET_USAGE", target_usage)
    for k in target_usage.keys():
        if target_usage[k] == 1:
            pass

    tt2 = []
    for s, flow, targets, targets3 in sources:
        targets2 = targets3.copy()
        next_targets = None

        targets_s = set()
        for t2 in targets2:
            targets_s.add(t2[0])

        done = False
        while not done:
            done = True
            next_targets = []
            for t, dist in targets2:
                if target_usage[t] == 1:
                    done = False
                    for t2xxx in sources_d[t][2]:
                        next_targets.append((t2xxx, dist + 1))
                else:
                    next_targets.append((t, dist))
            targets2 = next_targets

        tt2.append(next_targets)

    print("TT2", tt2)

    def print_graphviz():
        print("digraph {")
        for s, flow, targets in sources:
            print(s, '[label="' + s + ' (' + str(flow) + ')"]')
            for t in targets:
                print(s, "->", t)
        print("}")

    # print_graphviz()

    result = 0
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
