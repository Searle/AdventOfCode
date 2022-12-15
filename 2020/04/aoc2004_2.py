# https://adventofcode.com/2020/day/4
from pathlib import Path
import re

ref = 0
part = "_2"

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
        m = re.match(r'byr:(.+?) (?:cid:.+ )?ecl:(.+) eyr:(.+) hcl:(.+) hgt:(.+) iyr:(.+) pid:(.+)',
                     " ".join(sorted(re.split(r'\s+', input, re.M))))

        # if m: print(m[1], m[2], m[3], m[4], m[5], m[6], m[7])

        if m \
                and (re.fullmatch(r'\d\d\d\d', m[1]) and m[1] >= '1920' and m[1] <= '2002') \
                and (re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', m[2])) \
                and (re.fullmatch(r'\d\d\d\d', m[3]) and m[3] >= '2020' and m[3] <= '2030') \
                and (re.fullmatch(r'#[0-9a-f]{6}', m[4])) \
                and (re.fullmatch(r'\d\d\d\d', m[6]) and m[6] >= '2010' and m[6] <= '2020') \
                and (re.fullmatch(r'\d{9}', m[7])):
            m2 = re.fullmatch(r'(\d+)(cm|in)', m[5])
            if m2 and ((m2[2] == 'cm' and m2[1] >= '150' and m2[1] <= '193')
                       or (m2[2] == 'in' and m2[1] >= '59' and m2[1] <= '76')):
                result += 1

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
