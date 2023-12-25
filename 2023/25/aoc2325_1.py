# https://adventofcode.com/2023/day/25

from pathlib import Path
import re
from typing import Dict, Set, List, Tuple

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---

# http://magjac.com/graphviz-visual-editor/ -> neato
# dct -> kns
# jxb -> ksq
# pxp -> nqq


def run():
    result = 0

    cuts = {"cmg": "bvb", "jqt": "nvd", "pzl": "hfx"}
    if ref == 0:
        cuts = {"dct": "kns", "jxb": "ksq", "pxp": "nqq"}

    parents = {}
    children = {}

    # graph = "digraph {\n"

    for input in inputs:
        m = re.fullmatch(r"(\S+):\s+(.*)", input)
        assert m is not None, "NOT MATCHED: " + input

        left = m[1]
        rights = re.split(r"\s+", m[2])

        for right in rights:
            # graph += left + " -> " + right + "\n"
            if left in cuts and right == cuts[left]:
                # print("SKIP", left)
                continue
            if not left in children:
                children[left] = set()
            children[left].add(right)
            if not right in parents:
                parents[right] = set()
            parents[right].add(left)

    # graph += "}\n"
    # open(path / ("graph" + part + ext + ".dot"), "w").write(graph)

    slot1 = set()
    slot2 = set()

    def collect(node):
        nodes = {node}

        def _c(node):
            for parent in parents[node]:
                nodes.add(parent)
                if parent in parents:
                    _c(parent)

        _c(node)
        return nodes

    for parent in parents:
        if not parent in children:
            nodes = collect(parent)
            if len(slot1) == 0 or nodes & slot1:
                slot1 |= nodes
            else:
                slot2 |= nodes

    result = len(slot1) * len(slot2)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
