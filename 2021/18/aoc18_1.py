# https://adventofcode.com/2021/day/18
from pathlib import Path
import re

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    def explode(line):
        parts = re.split('([\\[\\],])', line)
        maxOpen = 0
        open = 0
        openInx = -1
        numInx = -1
        leftNumInxs = {}
        rightNumInxs = {}
        for i in range(0, len(parts) - 1, 2):
            if parts[i] != '':
                numInx = i
                if i > openInx + 4 and rightNumInxs[maxOpen] < 0:
                    rightNumInxs[maxOpen] = i
            c = parts[i + 1]
            if c == '[':
                open += 1
                if open > maxOpen:
                    leftNumInxs[open] = numInx
                    rightNumInxs[open] = -1
                    maxOpen = open
                    openInx = i + 1
            if c == ']':
                open -= 1

        if maxOpen > 4:
            if leftNumInxs[maxOpen] >= 0:
                parts[leftNumInxs[maxOpen]] = str(
                    int(parts[leftNumInxs[maxOpen]]) + int(parts[openInx + 1]))
            if rightNumInxs[maxOpen] >= 0:
                parts[rightNumInxs[maxOpen]] = str(
                    int(parts[rightNumInxs[maxOpen]]) + int(parts[openInx + 3]))
            parts[openInx] = '0'
            parts[openInx + 1] = ''
            parts[openInx + 2] = ''
            parts[openInx + 3] = ''
            parts[openInx + 4] = ''

        return "".join(parts)

    def split(line):

        def repl(m):
            value = int(m.group(0))
            return "[" + str(int(value / 2)) + "," + str(int((value + 1) / 2)) + "]"

        return re.sub("\\b(\\d\\d+)\\b", repl, line, 1)

    def _join(left, right):
        return "[" + left + "," + right + "]"

    def join(left, right):
        line = _join(left, right)
        while True:
            line1 = explode(line)
            if line1 != line:
                # print(line)
                line = line1
                continue
            line1 = split(line)
            if line1 != line:
                # print(line)
                line = line1
                continue
            break
        return line

    def magnitude(line):

        def repl(m):
            return str(int(m.group(1)) * 3 + int(m.group(2)) * 2)

        while True:
            line1 = re.sub("\\[(\\d+),(\\d+)\\]", repl, line)
            if line1 == line:
                return line1
            line = line1

        # explode('[[[[[9,8],1],2],3],4]')
        # explode('[7,[6,[5,[4,[3,2]]]]]')
        # explode('[[6,[5,[4,[3,2]]]],1]')

        # print(join('[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]',
        #       '[7,[5,[[3,8],[1,4]]]]'))

    line = input[0]
    for i in input[1:]:
        line = join(line, i)
        # print(line)

    return magnitude(line)


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
