# https://adventofcode.com/2021/day/4
from pathlib import Path
from itertools import count

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    numbers = input[0].split(",")
    boards = []

    for i in count(2, 6):
        if i > len(input):
            break

        lookup = {}
        boardNums = ' '.join(input[i:(i+5)]).strip().split()

        for j in range(25):
            lookup[boardNums[j]] = j

        boards.append({
            "lookup": lookup,
            "bits1": [0, 0, 0, 0, 0],
            "bits2": [0, 0, 0, 0, 0],
            "in": True,
        })

    boardCount = len(boards)
    for number_i in range(len(numbers)):
        number = numbers[number_i]
        for board in boards:
            if board["in"] and number in board["lookup"]:
                index = board["lookup"][number]
                x = index // 5
                y = index % 5
                board["bits1"][x] |= 1 << y
                board["bits2"][y] |= 1 << x
                if board["bits1"][x] == 31 or board["bits2"][y] == 31:
                    sum = 0
                    for number1 in board["lookup"]:
                        index = board["lookup"][number1]
                        x = index // 5
                        y = index % 5
                        if board["bits1"][x] & (1 << y) == 0:
                            sum += int(number1)
                    if boardCount == 1:
                        return sum * int(number)
                    board["in"] = False
                    boardCount = boardCount - 1
    assert False, "No result"


result = str(run())

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
