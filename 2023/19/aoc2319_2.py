# https://adventofcode.com/2023/day/19

from pathlib import Path
import re
from typing import Dict, Set, List

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    def_code = ""
    def_pre_code = ""
    splits = {"x": set(), "m": set(), "a": set(), "s": set()}
    for input in inputs:
        if input == "":
            break
        else:
            m = re.fullmatch(r"([a-z]+)\{(.*)\}", input)
            assert m is not None, "NOT MATCHED: " + input

            def_pre_code += f"bool c_{m[1]}(int x, int m, int a, int s);\n"
            def_code += f"bool c_{m[1]}(int x, int m, int a, int s) {{\n"
            for st in m[2].split(","):
                if0 = st.split(":")
                if len(if0) > 1:
                    if1 = if0[0]
                    st = if0[1]
                    xx = re.split(r"([<>])", if1)
                    if xx[1] == "<":
                        splits[xx[0]].add(int(xx[2]))
                    else:
                        splits[xx[0]].add(int(xx[2]) + 1)
                else:
                    if1 = None
                if st == "A":
                    st = "return true"
                elif st == "R":
                    st = "return false"
                else:
                    st = f"return c_{st}(x,m,a,s)"
                if if1 is not None:
                    def_code += f"    if ({if1}) {st};\n"
                else:
                    def_code += f"    {st};\n"
            def_code += f"}}\n"

    code = ""
    code += "#include <stdbool.h>\n"
    code += "#include <stdio.h>\n"
    code += "\n"
    code += def_pre_code
    code += "\n"
    code += def_code
    code += "\n"

    tuples_code = ""
    loop_code = ""
    loop_code += "    long long result = 0;\n"
    loop_post_code = ""

    for i, k in enumerate(("x", "m", "a", "s")):
        ss0 = sorted(splits[k])
        ss1 = [1] + ss0
        ss2 = ss0 + [4001]
        sstr1 = []
        for a in zip(ss1, ss2):
            sstr1.append(str(a[0]))
            sstr1.append(str(a[1] - a[0]))
        indent = "    " * i
        sstr2 = ",".join(sstr1)
        tuples_code += f"// {k}_list: {len(sstr1) // 2}\n"
        tuples_code += f"int {k}_list[] = {{{sstr2}}};\n"
        tuples_code += f"int {k}_list_size = sizeof({k}_list) / sizeof({k}_list[0]);\n"
        loop_code += (
            f"{indent}    for (int {k}i= 0; {k}i < {k}_list_size; {k}i += 2) {{\n"
        )
        loop_code += f"{indent}        int {k}= {k}_list[{k}i];\n"
        loop_code += f"{indent}        int {k}2= {k}_list[{k}i + 1];\n"
        if i == 2:
            loop_code += f"{indent}        long long xma2= (long long)x2 * (long long)m2 * (long long)a2;\n"
        loop_post_code = f"{indent}    }}\n" + loop_post_code

    loop_code += "    " * 5 + "if (c_in(x,m,a,s)) result += xma2 * s2;\n"
    loop_code += loop_post_code

    code += tuples_code
    code += "\n"
    code += "void main() {\n"
    code += loop_code
    code += '    printf("RESULT: %lld\\n", result);\n'
    code += "}\n"

    with open("2023/19/code" + part + ext + ".c", "w") as file:
        file.write(code)
    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
