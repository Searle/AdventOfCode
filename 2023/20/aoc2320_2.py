# https://adventofcode.com/2023/day/20

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 0
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
                "%" if node[1] else "&",
                node[0],
                "->",
                [nodes[j][3] for j in node[4]],
                "/",
                [nodes[j][3] for j in node[2]],
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

    # print_nodes()

    """
    def write_h_code():
        dest_max = max([len(node[2]) for node in nodes])
        code = ""
        code += f"#define NODE_WIDTH {dest_max + 2}\n"
        code += f"#define BROADCAST_INX {broadcast_inx}\n"
        code += f"#define RX_INX {rx_inx}\n"
        nodes_code = "int nodes[] = {\n"
        nodes_mask_code = "long long node_masks[] = {\n"
        for node in nodes:
            dest_str = ",".join(
                [
                    "-1" if i >= len(node[2]) else str(node[2][i])
                    for i in range(0, dest_max)
                ]
            )
            nodes_code += f"    {1 if node[0] else 0},  {dest_str}, -1,\n"
            nodes_mask_code += f"    {node[1]},\n"
        nodes_code += "0 };\n"
        nodes_mask_code += "0 };\n"
        code += nodes_code
        code += nodes_mask_code
        with open("2023/20/code" + part + ext + ".h", "w") as file:
            file.write(code)
    """

    # =============

    states = [0] * node_inx
    result1 = 0

    def reset_state():
        nonlocal states
        states = [0] * node_inx

    def push_button(check_inx):
        nonlocal result1

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
                if ninx == check_inx and pulse == 0:
                    return False

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
                    cmds[cmd_end + 1] = states[ninx] ^ nodes[ninx][1]
                    cmd_end = (cmd_end + 2) & 255
        return True

    def wait_for_check(check_inx):
        reset_state()
        res = 1
        while push_button(check_inx):
            res += 1
        return res

    dh = wait_for_check(name_lookup["dh"])
    dp = wait_for_check(name_lookup["dp"])
    bb = wait_for_check(name_lookup["bb"])
    qd = wait_for_check(name_lookup["qd"])

    # Eigentlich kgV, aber sind alle prim
    result = dh * dp * bb * qd

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
