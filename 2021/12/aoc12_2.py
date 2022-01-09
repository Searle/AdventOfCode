# https://adventofcode.com/2021/day/12
from pathlib import Path
from itertools import count

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
edges = Path(__file__).parent.absolute()
input = open(edges/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    edges = {}

    def addEdge(nodes):
        if nodes[0] in edges:
            edges[nodes[0]].append(nodes[1])
        else:
            edges[nodes[0]] = [nodes[1]]

    for i in input:
        nodes = i.split("-")
        if (nodes[1] != 'start' and nodes[0] != 'end'):
            addEdge(nodes)
        if (nodes[0] != 'start' and nodes[1] != 'end'):
            addEdge((nodes[1], nodes[0]))

    visited = {}
    paths = {}

    def visit(node, path, visited, hasTwice):
        path = path.copy()
        path.append(node)
        for n in edges[node]:
            if n == 'end':
                pathStr = ",".join(path) + ",end"
                if not (pathStr in paths):
                    paths[pathStr] = True
                continue
            if not n in edges:
                continue
            if n[0] == n[0].capitalize():
                visit(n, path, visited, hasTwice)
                continue
            nextHasTwice = hasTwice
            if n in visited:
                if hasTwice:
                    continue
                nextHasTwice = True
            v = visited.copy()
            v[n] = True
            visit(n, path, v, nextHasTwice)

    visit('start', [], {}, False)

    # print("\n".join(paths.keys()))

    return len(paths.keys())


# ---
result = run()
print(result)
open(edges/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
