# https://adventofcode.com/2021/day/24
from pathlib import Path
import random

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + part + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

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
        nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        largest = nums.copy()
        running = True

        retval = [0, 0, 0, 0]
    # print("RETVAL", retval)

        while running:
            li += 1
            if li > 100000:
                print("AT", nums)
                li = 0

            exec(code, {"in_list": nums, "retval": retval})

            if retval[3] == 0:
                largest = nums.copy()
                print("FOUND", largest)

            # print("REGS", regs)
            # running = False

            for i in range(13, -1, -1):
                if nums[i] > 1:
                    nums[i] -= 1
                    break
                nums[i] = 9
                if i == 0:
                    running = False

    def run_prg(nums):
        retval = [0, 0, 0, 0]
        exec(code, {"in_list": nums, "retval": retval})
        return retval

    def test1():
        # nums0 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 7]
        nums0 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        nums1 = nums0.copy()

        for n in range(0, 14):
            print(n)
            for i in range(1, 10):
                nums1[n] = i
                regs = run_prg(nums1)
                print("REGS", n, i, nums1, regs)
            nums1[n] = nums0[n]

    def test2():
        # nums0 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 7]
        nums0 = [
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        ]

        ok_fact = 10
        min = 0
        for j in range(0, 10):
            next_nums0 = []
            last_min = min
            min = 0
            for nums in nums0:
                nums1 = nums.copy()
                nums2 = nums.copy()
                for n in range(0, 14):
                    for i in range(1, 10):
                        nums1[n] = i
                        regs = run_prg(nums1)
                        # print("REGS", n, i, nums1, regs)
                        if min == 0 or regs[3] < min:
                            min = regs[3]
                    nums1[n] = nums2[n]
            if min == last_min:
                break
            seen = set()
            for nums in nums0:
                nums1 = nums.copy()
                nums2 = nums.copy()
                for n in range(0, 14):
                    for i in range(1, 10):
                        if nums2[n] == i:
                            continue
                        nums1[n] = i
                        if str(nums1) in seen:
                            continue
                        seen.add(str(nums1))
                        regs = run_prg(nums1)
                        if regs[3] <= min * ok_fact:
                            next_nums0.append(nums1.copy())
                    nums1[n] = nums2[n]
            print(min)
            for nums in next_nums0:
                print("REGS", nums, min)

            nums0 = next_nums0

    # Solutions:
    # [3, 5, 1, 7, 7, 4, 5, 2, 4, 8, 4, 3, 9, 1] [1, 0, 0, 0]
    # [7, 1, 2, 5, 5, 2, 3, 7, 9, 9, 9, 8, 5, 5] [5, 0, 0, 0]
    # [9, 4, 2, 3, 3, 5, 6, 5, 7, 9, 8, 7, 8, 7] [7, 0, 0, 0]

    def test3():
        nums0 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

        ns = [9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 1]

        min = 0
        for j in range(0, 100000):
            i = random.randint(0, 13)
            n = random.randint(0, len(ns) - 1)
            n = ns[n]
            mutate = random.randint(0, 999) == 0
            fact = 20 if mutate else 1.3

            old = nums0[i]
            nums0[i] = n
            regs = run_prg(nums0)
            if min == 0 or regs[3] < min * fact:
                min = regs[3]
                print("REGS", n, i, nums0, regs)
                if min == 0:
                    break
            else:
                nums0[i] = old

    def nums_score(nums):
        score = 0
        for n in iter(nums):
            score = score * 2 + n
        return score

    # FIN 0 112065 [9, 5, 2, 7, 7, 5, 6, 7, 9, 9, 5, 4, 9, 7]
    # FIN 0 115857 [9, 5, 2, 9, 9, 7, 8, 6, 8, 9, 9, 8, 9, 7]

    def test3a():
        nums0 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

        ns = [9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 2, 1]

        zmin = 0
        score = nums_score(nums0)
        for j in range(0, 100000):
            i = random.randint(0, 13)
            n = random.randint(0, len(ns) - 1)
            n = ns[n]
            mutate = random.randint(0, 299) == 0
            zmin_fact = 20 if mutate else 1.3
            mutate = random.randint(0, 299) == 0
            score_fact = 1.6 if mutate else 1.04

            old = nums0[i]
            nums0[i] = n
            regs = run_prg(nums0)
            z = regs[3]  # .bit_count()
            max_zmin = zmin * zmin_fact
            min_score = nums_score(nums0) * score_fact
            if (zmin == 0 or z < max_zmin) and min_score > score:
                # print("REGS", score, min_score, n, i, nums0, regs)
                zmin = z
                score = nums_score(nums0)
                if zmin == 0:
                    break
            else:
                nums0[i] = old
        print("FIN", zmin, score, nums0)

    def test4():
        nums0 = [9, 9, 2, 5, 5, 2, 3, 7, 9, 9, 9, 8, 9, 7]
        nums0 = [9, 9, 9, 9, 9, 2, 3, 7, 9, 9, 9, 8, 1, 7]
        nums0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # nums0 = [9, 9, 9, 9, 9, 9, 9, 7, 9, 1, 9, 8, 1, 7]
        # nums0= [9, 9, 9, 9, 9, 9, 3, 7, 7, 6, 9, 8, 1, 7]
        # nums0 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        nums1 = nums0.copy()

        regs = run_prg(nums1)
        print("REGS", 0, 0, nums1, regs,
              "{0:b}".format(regs[3]).replace("0", " "))

        for n in range(0, 14):
            print(n)
            for i in range(1, 10):
                if nums0[n] == i:
                    continue
                nums1[n] = i
                regs = run_prg(nums1)
                print("REGS", n, i, nums1, regs,
                      "{0:b}".format(regs[3]).replace("0", " "))
            nums1[n] = nums0[n]

    # check_model_nos()
    test3a()

    return result


# ---
result = run()
# print(result)
# open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
