# https://adventofcode.com/2020/day/4
from pathlib import Path
import re

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

"""
    byr (Birth Year)
    *cid (Country ID)
    ecl (Eye Color)
    eyr (Expiration Year)
    hcl (Hair Color)
    hgt (Height)
    iyr (Issue Year)
    pid (Passport ID)
"""


def run():

    result = 0
    inputs1 = "\n".join(inputs).split("\n\n")
    for input in inputs1:
        if re.match(r'byr:.* ecl:.* eyr:.* hcl:.* hgt:.* iyr:.* pid:.*',
                    " ".join(sorted(re.split(r'\s+', input, re.M)))):
            result += 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
