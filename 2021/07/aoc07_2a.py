# https://adventofcode.com/2021/day/7
from pathlib import Path

assert False, "Does not work, it seems to find a local maximum"

ref = True
part = "_2"

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

    leftCrabs = 0
    rightCrabs = 0
    leftFuel = 0
    rightFuel = 0
    leftFuel2 = 0
    rightFuel2 = 0

    # print(leftIndex, rightIndex)

    while leftIndex < rightIndex:

        print(leftFuel + leftFuel2 + leftCrabs + arr[leftIndex], leftFuel, leftFuel2, ":", leftCrabs, leftIndex, arr,
              rightIndex, rightCrabs, ":", rightFuel2, rightFuel, rightFuel + rightFuel2 + rightCrabs + arr[rightIndex])

        if leftFuel + leftFuel2 + leftCrabs + arr[leftIndex] < rightFuel + rightFuel2 + rightCrabs + arr[rightIndex]:
            # if leftFuel < rightFuel:
            leftCrabs += arr[leftIndex]
            leftFuel2 += leftCrabs
            leftFuel += leftFuel2
            arr[leftIndex] = 9  # debug
            leftIndex += 1

        else:
            rightCrabs += arr[rightIndex]
            rightFuel2 += rightCrabs
            rightFuel += rightFuel2
            arr[rightIndex] = 9  # debug
            rightIndex -= 1

    # print(leftFuel, leftCrabs, leftIndex, arr,
    #       rightIndex, rightCrabs, rightFuel)
    print(leftFuel + leftFuel2 + leftCrabs + arr[leftIndex], leftFuel, leftFuel2, ":", leftCrabs, leftIndex, arr,
          rightIndex, rightCrabs, ":", rightFuel2, rightFuel, rightFuel + rightFuel2 + rightCrabs + arr[rightIndex])

    return leftFuel + rightFuel


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
