# https://adventofcode.com/2021/day/2
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

x = 0
y = 0
for i in input:
    [command, value] = i.split(" ")
    if (command == "forward"):
        x += int(value)
    elif command == "up":
        y -= int(value)
    elif command == "down":
        y += int(value)
result = str(x * y)

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
