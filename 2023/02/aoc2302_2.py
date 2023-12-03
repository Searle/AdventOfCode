# https://adventofcode.com/2023/day/02

from pathlib import Path
import re
from typing import List

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

rgbMap = {"r": 0, "g": 1, "b": 2}

def to_rgb(strs: List[str]):
    rgb= [0]*3;
    for str in strs:
        m = re.match(r'\s*(\d+)\s+(b|r|g)', str) 
        assert m is not None
        rgb[rgbMap[m[2]]]= int(m[1])
    return rgb;    

def run():
    result= 0
    for input in inputs:
        m = re.fullmatch(r'Game (\d+):(.*)', input)      
        assert m is not None
        rgbMax=[0]*3;
        game = [to_rgb(set.split(',')) for set in m[2].split(';')]
        for rgb in game:
            for i in range(0,3):
                rgbMax[i]=max(rgbMax[i], rgb[i])
        result += rgbMax[0] * rgbMax[1] * rgbMax[2]

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
