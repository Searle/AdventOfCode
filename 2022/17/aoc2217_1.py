# https://adventofcode.com/2022/day/17

from pathlib import Path

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    input = inputs[0]

    blocks = [
        [0b1111000],
        [0b0100000, 0b1110000, 0b0100000],
        [0b1110000, 0b0010000, 0b0010000],
        [0b1000000, 0b1000000, 0b1000000, 0b1000000],
        [0b1100000, 0b1100000],
    ]

    blocks_w = [4, 3, 3, 1, 2]

    chamber = [0] * 10000

    ch_height = 0
    x = 0

    input_i = 0

    block_i = -1

    def next_input():
        nonlocal input_i
        in1 = inputs[0][input_i]
        input_i += 1
        return -1 if in1 == '<' else 1

    def next_push():
        nonlocal x
        x = min(7 - block_w, max(0, next_input()))

    def print_chamber():
        print()
        output = False
        for i in range(len(chamber) - 1, -1, -1):
            if chamber[i]:
                output = True
            if output:
                print(bin(256+chamber[i]).replace('1',
                                                  '#').replace('0', '.')[3:])

    for xx in range(1, 2):

        block_i = (block_i + 1) % 5

        block = blocks[block_i]
        block_w = blocks_w[block_i]

        next_push()
        next_push()
        next_push()

        x1 = x
        y1 = ch_height - 1

        if y1 >= 0:

            pass

        for bi, bb in enumerate(block):
            chamber[ch_height - bi] |= bb >> x

        print_chamber()
        # next_input()
        # ch_i += 1

    # print_chamber()

    for y in range(ch_height, 0, -1):
        pass

    result = 0
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
