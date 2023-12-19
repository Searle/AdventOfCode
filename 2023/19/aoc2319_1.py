# https://adventofcode.com/2023/day/19

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    parseValues = False
    def_code = ""
    calc_code = ""
    for input in inputs:
        if parseValues:
            m = re.fullmatch(r"\{(.*)\}", input)
            assert m is not None, "NOT MATCHED: " + input

            for st in m[1].split(","):
                calc_code += f"    {st}\n"
            calc_code += f"    c_in()\n"
        elif input == "":
            parseValues = True
        else:
            m = re.fullmatch(r"([a-z]+)\{(.*)\}", input)
            assert m is not None, "NOT MATCHED: " + input

            def_code += f"    def c_{m[1]}():\n"
            for st in m[2].split(","):
                if0 = st.split(":")
                if len(if0) > 1:
                    if1 = if0[0]
                    st = if0[1]
                else:
                    if1 = None
                if st == "A":
                    st = "return accept()"
                elif st == "R":
                    st = "return"
                else:
                    st = f"return c_{st}()"
                if if1 is not None:
                    def_code += f"        if {if1}:\n"
                    def_code += f"            {st}\n"
                else:
                    def_code += f"        {st}\n"

    pre_code = ""
    pre_code += "".join([f"    {v}=0\n" for v in ("x", "m", "a", "s", "result")])
    pre_code += "    def accept():\n"
    pre_code += "        nonlocal result\n"
    pre_code += "        result += x + m + a + s\n"

    post_code = ""
    post_code += calc_code
    post_code += '    print("RESULT:", result)\n'

    code = f"def run():\n{pre_code}{def_code}{post_code}run()\n"

    print("CODE\n" + code)

    with open("2023/19/code" + part + ext + ".py", "w") as file:
        file.write(code)
    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
