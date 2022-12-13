# https://adventofcode.com/2022/day/11
from pathlib import Path
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    result = 0

    re1 = r'\s*Starting items: (.+?)$' \
        + r'\s*Operation: new = old (\S) (.+?)$' \
        + r'\s*Test: divisible by (\S+?)$' \
        + r'\s*If true: throw to monkey (\S+?)$'\
        + r'\s*If false: throw to monkey (\S+?)$'

    monkeys = [
        {
            "items": [int(i) for i in m[0].split(", ")],
            "op": m[1],
            "op_arg": m[2] if m[2] == "old" else int(m[2]),
            "test_div_by": int(m[3]),
            "test_result": {True: int(m[4]), False: int(m[5])},
            "inspects": 0
        } for m in re.findall(re1, "\n".join(inputs), re.M)]

    for _ in range(0, 20):
        for monkey in monkeys:
            for item in monkey["items"]:
                monkey["inspects"] += 1
                op_arg = item if monkey["op_arg"] == "old" else monkey["op_arg"]
                if monkey["op"] == "*":
                    item *= op_arg
                elif monkey["op"] == "+":
                    item += op_arg
                else:
                    assert True, "OP? " + monkey["op"]
                item //= 3
                target = monkey["test_result"][item %
                                               monkey["test_div_by"] == 0]
                monkeys[target]["items"].append(item)
            monkey["items"] = []

    m = sorted(monkeys, key=lambda m: m["inspects"], reverse=True)

    result = m[0]["inspects"] * m[1]["inspects"]

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
