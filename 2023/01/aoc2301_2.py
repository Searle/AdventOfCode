# https://adventofcode.com/2023/day/01

from pathlib import Path
import re

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---

digits= ['zero','one','two','three','four','five','six','seven','eight','nine']

def check_digit(input: str, i: int):
    if input[i] >= '0' and input[i] <= '9':
        return int(input[i])
    for digit in range(0,10):
        if input[i:i+len(digits[digit])] == digits[digit]:
            return digit
    return -1

def run():

    result= 0
    for input in inputs:
        digit1 = 0
        digit2 = 0
        for i in range(0,len(input)):
            digit1= check_digit(input,i)
            if digit1 >= 0:
                break
        for i in range(len(input)-1,-1,-1):
            digit2= check_digit(input,i)
            if digit2 >= 0:
                break
        result +=  digit1 * 10+digit2

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
