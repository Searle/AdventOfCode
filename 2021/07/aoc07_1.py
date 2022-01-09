# https://adventofcode.com/2021/day/7
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    # print(input[0])

    crabs = [int(i) for i in input[0].split(",")]
    leftIndex = min(crabs)
    rightIndex = max(crabs)
    arr = [0] * (rightIndex + 1)
    for i in crabs:
        arr[i] += 1

    fuel = 0

    # print(leftIndex, rightIndex)

    while leftIndex < rightIndex:

        # print(arr)

        if arr[leftIndex] + arr[leftIndex + 1] < arr[rightIndex] + arr[rightIndex - 1]:
            fuel += arr[leftIndex]
            arr[leftIndex + 1] += arr[leftIndex]
            # arr[leftIndex] = 0  # debug
            leftIndex += 1

        else:
            fuel += arr[rightIndex]
            arr[rightIndex - 1] += arr[rightIndex]
            # arr[rightIndex] = 0  # debug
            rightIndex -= 1

    # print(leftIndex, rightIndex)

    return fuel


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
