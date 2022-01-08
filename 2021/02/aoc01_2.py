# https://adventofcode.com/2021/day/2
from pathlib import Path

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

x = 0
y = 0
aim = 0
for i in input:
    [command, value] = i.split(" ")
    if (command == "forward"):
        x += int(value)
        y += int(value) * aim
    elif command == "up":
        aim -= int(value)
    elif command == "down":
        aim += int(value)
result = str(x * y)

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
