# https://adventofcode.com/2023/day/07

from pathlib import Path
import re
from typing import List

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    a2s = []
    for input in inputs:
        m = re.fullmatch(r"(\S+)\s(\d+)", input)
        assert m is not None
        a0 = m[1]
        bet = m[2]

        a1 = (
            a0.replace("T", "a")
            .replace("J", "0")
            .replace("Q", "c")
            .replace("K", "d")
            .replace("A", "e")
        )

        a2 = "".join(sorted(a1))[::-1]

        def calcparts(a2):
            a3 = a2
            parts = []
            prefix = "0"
            m = re.match(r"(.*)((.)\3\3\3\3)(.*)", a3)
            if not m is None:
                parts.append(m[2])
                a3 = m[1] + m[4]
                prefix = "6"

            m = re.match(r"(.*)((.)\3\3\3)(.*)", a3)
            if not m is None:
                parts.append(m[2])
                a3 = m[1] + m[4]
                prefix = "5"

            m = re.match(r"(.*)((.)\3\3)(.*)", a3)
            if not m is None:
                parts.append(m[2])
                a3 = m[1] + m[4]
                prefix = "3"

            m = re.match(r"(.*)((.)\3)(.*)", a3)
            if not m is None:
                parts.append(m[2])
                a3 = m[1] + m[4]
                if prefix == "3":
                    prefix = "4"
                else:
                    prefix = "1"

            m = re.match(r"(.*)((.)\3)(.*)", a3)
            if not m is None:
                parts.append(m[2])
                a3 = m[1] + m[4]
                if prefix == "1":
                    prefix = "2"
                else:
                    prefix = "1"
            return prefix, parts, a3

        zs = a2.count("0")
        prefix, parts, a4 = calcparts(a2.replace("0", ""))

        if zs == 5:
            a5 = "00000"
        elif len(parts):
            a5 = parts[0][0] * zs + "".join(parts) + a4
        else:
            a5 = a4[0] * zs + "".join(parts) + a4

        prefix, _, _ = calcparts(a5)
        a2s.append(prefix + "-" + a1 + "-" + bet)

    a2s.sort()

    # print("----")
    # print("\n".join(a2s))
    # print("\n".join(a2s[:10]))
    # print("\n".join(a2s[990:]))
    # print("----", len(a2s))

    result = sum([int(s[8:]) * (i + 1) for i, s in enumerate(a2s)])

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
