# https://adventofcode.com/2023/day/20

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    nodes = []
    states: List[int] = []
    name_lookup: Dict[str, int] = {}

    def print_nodes():
        for node in nodes:
            print(
                "NODE",
                "%" if node[1] else "&",
                node[0],
                "->",
                [nodes[j][0] for j in node[2]],
                "/",
                [nodes[j][0] for j in node[3]],
            )

    node_inx = 0

    def get_node(name: str):
        nonlocal node_inx

        if name in name_lookup:
            return name_lookup[name]

        name_lookup[name] = node_inx
        # name, isFF, dests, srcs, src_mask
        nodes.append([name, False, [], [], 0])
        node_inx += 1
        return node_inx - 1

    for input in inputs:
        m = re.fullmatch(r"([&%]?)([a-z]+) -> (.*)", input)
        assert m is not None, "NOT MATCHED: " + input

        inx = get_node(m[2])

        dest_inxs = []
        for name in re.split(r", ", m[3]):
            dest_inx = get_node(name)
            nodes[dest_inx][3].append(inx)
            nodes[dest_inx][4] |= 1 << inx
            dest_inxs.append(dest_inx)

        nodes += [None] * (len(states) - len(nodes))
        nodes[inx][0] = m[2]
        nodes[inx][1] = m[1] == "%"
        nodes[inx][2] = dest_inxs

    broadcast_inx = name_lookup["broadcaster"]

    DEBUG = False
    if DEBUG:
        print_nodes()

    # =============

    states = [0] * node_inx
    pulse_stats = {False: 0, True: 0}

    def push_button():
        if DEBUG:
            print("----")

        pulse_stats[False] += 1

        cmds: List[Tuple[int, int]] = []
        cmds.append((broadcast_inx, 0))

        while len(cmds):
            src, pulse = cmds.pop(0)

            for ninx in nodes[src][2]:
                _name, isFF, dests, _srcs, src_mask = nodes[ninx]

                pulse_stats[pulse != 0] += 1

                if DEBUG:
                    print(
                        "CMD",
                        nodes[src][0],
                        "-high->" if pulse else "-low->",
                        nodes[ninx][0],
                        "%" if isFF else "&",
                        "(",
                        ", ".join([nodes[j][0] for j in dests]),
                        ")",
                    )
                if isFF:
                    if not pulse:
                        states[ninx] = ~states[ninx]
                        cmds.append((ninx, states[ninx]))
                else:
                    if pulse:
                        states[ninx] |= 1 << src
                    else:
                        states[ninx] &= ~(1 << src)
                    cmds.append((ninx, states[ninx] ^ src_mask))

    for _ in range(0, 1000):
        push_button()

    if DEBUG:
        print("STATS", pulse_stats)

    result = pulse_stats[False] * pulse_stats[True]

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
