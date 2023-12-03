# https://adventofcode.com/2023/day/02

from pathlib import Path
import re
from typing import List

ref = 0
part = "_1"

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
        gameId= int(m[1])
        game = [to_rgb(set.split(',')) for set in m[2].split(';')]
        if all(rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <=14  for rgb in game):
            result += gameId

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
