# https://adventofcode.com/2021/day/8
from pathlib import Path
from itertools import permutations
# from str import translate, maketrans

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    digi1 = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
             'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    digiLookup = {}
    for i in range(len(digi1)):
        digiLookup[digi1[i]] = i

    sum = 0
    for i in input:
        parts = i.split('|')
        digits = parts[0].strip().split()
        message = parts[1].strip().split()

        found = False
        for p in permutations('abcdefg'):
            trans = "".maketrans("abcdefg", "".join(p))

            def trans1(a): return "".join(sorted(a.translate(trans)))

            found = True
            for di in range(len(digi1)):
                if not (trans1(digits[di]) in digiLookup):
                    found = False
                    break

            if found:
                sum += int("".join([str(digiLookup[trans1(m)])
                                   for m in message]))
                break

        assert found, "Search failed " + i

    return sum


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
