# https://adventofcode.com/2023/day/20

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 1
part = "_2"

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
                "%" if node[0] else "&",
                node[0],
                "->",
                [nodes[j][3] for j in node[2]],
                "/",
                [nodes[j][3] for j in node[3]],
            )

    node_inx = 0

    def get_node(name: str):
        nonlocal node_inx

        if name in name_lookup:
            return name_lookup[name]

        name_lookup[name] = node_inx
        # isFF, src_mask, dests, name, srcs
        nodes.append([False, 0, [], name, []])
        node_inx += 1
        return node_inx - 1

    for input in inputs:
        m = re.fullmatch(r"([&%]?)([a-z]+) -> (.*)", input)
        assert m is not None, "NOT MATCHED: " + input

        inx = get_node(m[2])

        dest_inxs = []
        for name in re.split(r", ", m[3]):
            dest_inx = get_node(name)
            nodes[dest_inx][4].append(inx)
            nodes[dest_inx][1] |= 1 << inx
            dest_inxs.append(dest_inx)

        nodes += [None] * (len(states) - len(nodes))
        nodes[inx][3] = m[2]
        nodes[inx][0] = m[1] == "%"
        nodes[inx][2] = dest_inxs

    broadcast_inx = name_lookup["broadcaster"]

    DEBUG = False
    if DEBUG:
        print_nodes()

    """
    for node in nodes:
        for j in node[2]:
            print(
                '"' + ("" if node[0] else "&") + node[3] + '"',
                "->",
                '"' + ("" if nodes[j][0] else "&") + nodes[j][3] + '"',
            )
    """

    # =============

    states = [0] * node_inx
    pulse_stats = {False: 0, True: 0}

    def push_button():
        if DEBUG:
            print("----")

        pulse_stats[False] += 1

        cmds = [0] * 256
        cmds[0] = broadcast_inx
        cmds[1] = 0
        cmd_start = 0
        cmd_end = 2

        while cmd_start != cmd_end:
            src = cmds[cmd_start]
            pulse = cmds[cmd_start + 1]
            cmd_start = (cmd_start + 2) & 255

            for ninx in nodes[src][2]:
                pulse_stats[pulse != 0] += 1

                if nodes[ninx][0]:
                    if not pulse:
                        states[ninx] = ~states[ninx]
                        cmds[cmd_end] = ninx
                        cmds[cmd_end + 1] = states[ninx]
                        cmd_end = (cmd_end + 2) & 255
                else:
                    if pulse:
                        states[ninx] |= 1 << src
                    else:
                        states[ninx] &= ~(1 << src)
                    cmds[cmd_end] = ninx
                    assert (states[ninx] & ~nodes[ninx][1]) == 0
                    cmds[cmd_end + 1] = states[ninx] ^ nodes[ninx][1]
                    cmd_end = (cmd_end + 2) & 255

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
