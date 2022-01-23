# https://adventofcode.com/2021/day/21
from pathlib import Path
from itertools import combinations

ref = 1
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def add(arr, key, value):
    arr[key] = arr[key] + value if key in arr else value


def run():
    space = [int(input[0].split(':')[1]) - 1,  int(input[1].split(':')[1]) - 1]

    def calcDistribution():

        r = {}

        def roll(startSpace, space, score):
            for die0 in range(1, 4):
                for die1 in range(1, 4):
                    for die2 in range(1, 4):
                        rolled = die0 + die1 + die2
                        newSpace = (space + rolled) % 10
                        newScore = score + newSpace + 1
                        if True:  # space + rolled >= 10:
                            # print(die0, die1, die2, newSpace, newScore)
                            add(r, (startSpace, newSpace, newScore), 1)
                        else:
                            roll(startSpace, newSpace, newScore)

        # for space in range(0, 10):
        #     roll(space, space, 0)
        roll(0, 0, 0)
        # print()

        for k, v in r.items():
            print(k, v)
        exit()

    # calcDistribution()

    def a2():

        def roll1(space):

            distribution = (1, 3, 6, 7, 6, 3, 1)

            c = 0
            stepHist = {}

            def roll2(step, fact, uniCount, space, score):
                nonlocal c

                for i, count in list(enumerate(distribution[:1])):
                    nextFact = fact * count
                    nextUniCount = uniCount + nextFact

                    nextSpace = (space + i + 3) % 10
                    nextScore = score + nextSpace + 1

                    if False:
                        print("N", i, "of", count, ":", nextSpace,
                              nextFact, nextScore, nextUniCount)

                    if nextScore >= 21:
                        c += nextUniCount
                        add(stepHist, step, nextUniCount)
                    else:
                        roll2(step + 1, nextFact, nextUniCount,
                              nextSpace, nextScore)

            print()
            roll2(1, 1, 0, space, 0)
            print("C", c)
            print("SH", stepHist)

        roll1(0)

    def a4():

        def roll1(space1, space2):

            distribution = (1, 3, 6, 7, 6, 3, 1)

            # debug
            # distribution = distribution[0:1]

            wins = [0, 0]
            stepHist = {}

            # space[0]/score[0] ist immer score des player
            def roll2(step, fact, uniCount, player, space, score):
                nonlocal wins

                for i, count in list(enumerate(distribution)):
                    nextFact = fact * count
                    nextUniCount = uniCount + nextFact

                    nextSpace = (space[0] + i + 3) % 10
                    nextScore = score[0] + nextSpace + 1

                    if False:
                        print(step, "N", i, "of", count,
                              ":", nextSpace, nextFact,
                              "|", player, nextScore, nextUniCount, space, score)

                    if nextScore >= 21:
                        wins[player] += nextUniCount
                        add(stepHist, step, nextUniCount)
                        continue

                    roll2(step + 1, nextFact, nextUniCount, 1 - player,
                          (space[1], nextSpace), (score[1], nextScore))

            print()
            roll2(0, 1, 0, 0, (space1, 0), (space2, 0))
            print("WINS", wins)
            print("WINSX",
                  (444356092776315 / wins[0]),
                  (341960390180808 / wins[1]))
            print("SH", stepHist)

        roll1(3, 7)

    a4()

    return 0


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
