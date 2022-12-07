# https://adventofcode.com/2021/day/24
from pathlib import Path

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    prg = [
        'x = 0',
        'y = 0',
        'w = 0',
        'z = 0',
    ]

    in_index = 0

    def padd(line):
        prg.append(line)

    for input in inputs:
        m = input.split(' ')
        cmd = m[0]
        reg = m[1]
        val = m[2] if len(m) > 2 else "0"
        if cmd == 'inp':
            padd(reg + ' = in_list[' + str(in_index) + ']')
            in_index += 1
        elif cmd == 'add':
            padd(reg + ' += ' + val)
        elif cmd == 'mul':
            if val == "0":
                padd(reg + ' = ' + val)
            else:
                padd(reg + ' *= ' + val)
        elif cmd == 'div':
            padd(reg + ' //= ' + val)
        elif cmd == 'mod':
            padd(reg + ' %= ' + val)
        elif cmd == 'eql':
            padd(reg + ' = int(' + reg + ' == ' + val + ')')

    padd("retval[0] = w")
    padd("retval[1] = x")
    padd("retval[2] = y")
    padd("retval[3] = z")

    source = "\n".join(prg)
    code = compile(source, "<string>", "exec", optimize=2)

    def check_model_nos():
        li = 0

        digits = [
            [3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5],
            [1, 2],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9],
            [8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7],
        ]

        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        smallest = nums.copy()
        running = True
        retval = [0, 0, 0, 0]

        while running:
            li += 1
            if li > 100000:
                print("AT", nums)
                li = 0

            nums1 = [
                digits[0][nums[0]],
                digits[1][nums[1]],
                digits[2][nums[2]],
                digits[3][nums[3]],
                digits[4][nums[4]],
                digits[5][nums[5]],
                digits[6][nums[6]],
                digits[7][nums[7]],
                digits[8][nums[8]],
                digits[9][nums[9]],
                digits[10][nums[10]],
                digits[11][nums[11]],
                digits[12][nums[12]],
                digits[13][nums[13]],
            ]

            exec(code, {"in_list": nums1, "retval": retval})

            if retval[3] == 0:
                smallest = nums1.copy()
                break

            for i in range(13, -1, -1):
                if nums[i] < len(digits[i]) - 2:
                    nums[i] += 1
                    break
                nums[i] = 0
                if i == 0:
                    running = False

        return "".join(map(str, smallest))

    return check_model_nos()


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
