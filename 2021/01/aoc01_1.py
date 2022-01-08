# https://adventofcode.com/2021/day/1
from pathlib import Path

ref = False
part = "_1"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

last = -1
drop_count = 0
for i in input:
    if last > 0 and int(i) > last:
        drop_count = drop_count + 1
    last = int(i)
result = str(drop_count)

# ---
print(result)
open(path/("result" + part + ext), "w").write(result.rstrip() + "\n")
