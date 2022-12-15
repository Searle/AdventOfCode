# https://adventofcode.com/2022/day/1
from pathlib import Path

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    arr = [0]
    for i in input:
        if i == '':
            arr.append(0)
        else:
            arr[len(arr)-1] += int(i)
    result = sum(sorted(arr)[-3:])
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
