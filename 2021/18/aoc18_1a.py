# https://adventofcode.com/2021/day/18
from pathlib import Path

# Baad, failed solution with  subtle bug i can't find

ref = True
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def parse(line):
    i = 0

    def peek():
        return line[i]

    def consume():
        nonlocal i
        i += 1
        return line[i - 1]

    def expect(c):
        nonlocal i
        assert line[i] == c, c + " expected: " + line[i:]
        i += 1

    def collectExpr(parent):
        if peek() == '[':
            return collectPair(parent)
        if peek() >= '0' and peek() <= '9':
            return {"parent": parent, "value": int(consume())}
        assert False, "PEEK? " + peek() + " " + line[i:]

    def collectPair(parent):
        nonlocal i
        node = {"parent": parent}
        expect('[')
        node["left"] = collectExpr(node)
        expect(',')
        node["right"] = collectExpr(node)
        expect(']')
        return node

    return collectPair(None)


def is_child(node):
    return not "value" in node


def is_value(node):
    return "value" in node


def get_tree(tree):
    def collect(node):
        if is_child(node):
            return [collect(node["left"]), collect(node["right"])]
        return node["value"]
    if tree == None:
        return "NA"
    return collect(tree)


def print_tree(tree):
    print(get_tree(tree))


def find_adj(node, dir1, dir2):
    while node["parent"] != None:
        isDir1Node = node["parent"][dir1] is node
        node = node["parent"]
        if not isDir1Node:
            node = node[dir1]
            if is_value(node):
                return node
            while is_child(node[dir2]):
                node = node[dir2]
            return node[dir2]
    return None


def find_left(node):
    return find_adj(node, "left", "right")


def find_right(node):
    return find_adj(node, "right", "left")


def run():

    def traverse(node, callback, parents=[]):
        if callback([node] + parents):
            return True
        if is_child(node["left"]):
            if traverse(node["left"], callback, [node] + parents):
                return True
        if is_child(node["right"]):
            return traverse(node["right"], callback, [node] + parents)
        return False

    def explode(nodes):
        if (len(nodes) > 4
                and is_value(nodes[0]["left"])
                and is_value(nodes[0]["right"])):
            left = find_left(nodes[0])
            # print("LEFT", get_tree(left))
            right = find_right(nodes[0])
            # print("RIGHT", get_tree(right))
            if left:
                left["value"] += nodes[0]["left"]["value"]
            if right:
                right["value"] += nodes[0]["right"]["value"]
            del nodes[0]["left"]
            del nodes[0]["right"]
            nodes[0]["value"] = 0
            return True
        return False

    def split(nodes):

        def action(node):
            if is_value(node) and node["value"] > 9:
                node["left"] = {
                    "parent": node,
                    "value": int(node["value"] / 2)
                }
                node["right"] = {
                    "parent": node,
                    "value": int((node["value"] + 1) / 2)
                }
                del node["value"]
                return True
            return False

        return action(nodes[0]["left"]) or action(nodes[0]["right"])

    def _join(left, right):
        node = {
            "parent": None,
        }
        left["parent"] = node
        right["parent"] = node
        node["left"] = left
        node["right"] = right
        return node

    def join(left, right):
        tree = _join(left, right)
        while True:
            while traverse(tree, explode):
                pass
            if not traverse(tree, split):
                break
        return tree

    def join1(left, right):

        tree = _join(left, right)

        def explode1():
            before = get_tree(tree)
            changed = traverse(tree, explode)
            after = get_tree(tree)
            if before != after:
                print("EXPLODE", after)
            return changed

        def split1():
            before = get_tree(tree)
            changed = traverse(tree, split)
            after = get_tree(tree)
            if before != after:
                print("SPLIT  ", after)
            return changed

        print("START  ", get_tree(tree))

        # [[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [[[6, 8], [0, 8]], [[9, 9], [9, 0]]]]
        #                                           X                 X

        # [[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [[[7, 8], [0, 8]], [[8, 9], [9, 0]]]]
        while explode1() or split1():
            pass
        return tree

        # [[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [[[7, 8], [0, 8]], [[8, 9], [9, 0]]]]
        while True:
            while explode1():
                pass
            if not split1():
                break
        return tree

        done = False
        while not done:
            done = True
            while explode1():
                done = False
            while split1():
                done = False

        return tree

        while True:
            while explode1():
                pass
            if not split1():
                break
        return tree

    if False:
        tree = join1(parse('[[[[4,3],4],4],[7,[[8,4],9]]]'), parse('[1,1]'))
        exit()

    if False:
        tree = parse('[1,1]')
        tree = join(tree, parse('[2,2]'))
        tree = join(tree, parse('[3,3]'))
        tree = join(tree, parse('[4,4]'))
        tree = join(tree, parse('[5,5]'))
        tree = join(tree, parse('[6,6]'))

        print_tree(tree)

        # explode(parse('[[[2,4],[[[9,8],1],2]],4]'))
        # explode(parse('[[[[[9,8],1],2],3],4]'))
        # explode(parse('[7,[6,[5,[4,[3,2]]]]]'))
        # explode(parse('[[6,[5,[4,[3,2]]]],1]'))
        # explode(parse('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'))
        # explode(parse('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'))
        exit()

    if True:
        tree = parse(
            '[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]')
        tree = join1(tree, parse('[7,[5,[[3,8],[1,4]]]]'))

        # print_tree(tree)
        exit()

    tree = parse(input[0])
    for i in input[1:]:
        tree = join(tree, parse(i))
        print_tree(tree)

    return 0


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
