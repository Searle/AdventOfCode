# https://adventofcode.com/2021/day/23
from pathlib import Path

ref = 0
part = "_2"
debug = False

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + part + ext), "r").read().rstrip().split("\n")
# ---

# 08 09 10 11 12 13 14 15 16 17 18
#       04    05    06    07
#       00    01    02    03

# 16 17    18    19    20    21 22
#       12    13    14    15
#       08    09    10    11
#       04    05    06    07
#       00    01    02    03

OFS = 16

amph_energy = [1, 10, 100, 1000]


def run():
    map1 = [ord(inputs[5][3]) - ord('A') + 1,
            ord(inputs[5][5]) - ord('A') + 1,
            ord(inputs[5][7]) - ord('A') + 1,
            ord(inputs[5][9]) - ord('A') + 1,
            ord(inputs[4][3]) - ord('A') + 1,
            ord(inputs[4][5]) - ord('A') + 1,
            ord(inputs[4][7]) - ord('A') + 1,
            ord(inputs[4][9]) - ord('A') + 1,
            ord(inputs[3][3]) - ord('A') + 1,
            ord(inputs[3][5]) - ord('A') + 1,
            ord(inputs[3][7]) - ord('A') + 1,
            ord(inputs[3][9]) - ord('A') + 1,
            ord(inputs[2][3]) - ord('A') + 1,
            ord(inputs[2][5]) - ord('A') + 1,
            ord(inputs[2][7]) - ord('A') + 1,
            ord(inputs[2][9]) - ord('A') + 1] + [0] * 7

    at_pos = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    for i in range(0, OFS):
        if at_pos[map1[i] - 1] < 0:
            at_pos[map1[i] - 1] = i
        elif at_pos[map1[i] + 3] < 0:
            at_pos[map1[i] + 3] = i
        elif at_pos[map1[i] + 7] < 0:
            at_pos[map1[i] + 7] = i
        else:
            at_pos[map1[i] + 11] = i

    def map_str():
        str = ["_____________", "#...........#",
               "###.#.#.#.###", "###.#.#.#.###",
               "###.#.#.#.###", "###.#.#.#.###"]
        pos_to_coords = ((3, 4), (5, 4), (7, 4), (9, 4),
                         (3, 3), (5, 3), (7, 3), (9, 3),
                         (3, 2), (5, 2), (7, 2), (9, 2),
                         (3, 1), (5, 1), (7, 1), (9, 1),
                         (1, 0), (2, 0), (4, 0), (6, 0), (8, 0), (10, 0), (11, 0))
        # print(map1, at_pos)
        for amph0, pos in enumerate(at_pos):
            amph = (amph0 & 3) + 1

            assert(map1[pos] == amph)

            (x, y) = pos_to_coords[pos]
            str[y + 1] = str[y + 1][:x] + \
                chr(ord('A') + (amph0 & 3)) + str[y + 1][x + 1:]
        return "\n".join(str)

    seen = dict()
    depth = 0

    best_energy = 0
    best_solution = None

    def check_next(amph0, pos, energy, next_pos, path_len, pth):
        nonlocal depth

        if depth > 35:
            return

        amph = (amph0 & 3) + 1

        map1[pos] = 0
        map1[next_pos] = amph
        at_pos[amph0] = next_pos

        energy1 = amph_energy[amph - 1] * path_len

        depth += 1
        if debug:
            check(energy + energy1,
                  pth.copy() + [{"recur": depth,
                                 "energy": energy1,
                                 "step": chr(ord('A') + (amph - 1)) + ":" + str(pos) + "->" + str(next_pos),
                                 "map": map_str()}])
        else:
            check(energy + energy1, pth)
        depth -= 1

        # assert(map1[pos] == 0)
        # assert(map1[next_pos] == amph)
        # assert(at_pos[amph0] == next_pos)

        map1[pos] = amph
        map1[next_pos] = 0
        at_pos[amph0] = pos

    def check(energy, pth):
        nonlocal best_energy
        nonlocal best_solution

        if (map1[0] == 1 and map1[1] == 2 and map1[2] == 3 and map1[3] == 4 and
                map1[4] == 1 and map1[5] == 2 and map1[6] == 3 and map1[7] == 4 and
                map1[8] == 1 and map1[9] == 2 and map1[10] == 3 and map1[11] == 4 and
                map1[12] == 1 and map1[13] == 2 and map1[14] == 3 and map1[15] == 4):
            if best_energy == 0 or energy < best_energy:
                print("BETTER SOLUTION FOUND!", energy)
                best_energy = energy
                best_solution = pth
            # for p in pth:
            #     print(p["recur"], p["step"], p["energy"])
            #     print(p["map"])
            return

        seen_key = str(map1)
        if seen_key in seen:
            if seen[seen_key] <= energy:
                return

        seen[seen_key] = energy

        for amph0, pos in enumerate(at_pos):
            amph_index = amph0 & 3
            amph = amph_index + 1
            pos1 = pos
            pl = 0
            blocked = False
            if pos1 < OFS:
                while pos1 + 4 < OFS:
                    pos1 += 4
                    if map1[pos1] > 0:
                        blocked = True
                        break
                    pl += 1
                if blocked:
                    continue
                pos1 += 5
                pl1 = pl
                for pos2 in range(pos1, OFS - 1, -1):
                    if map1[pos2] > 0:
                        break
                    pl1 += 1 if pos2 == OFS else 2
                    check_next(amph0, pos, energy, pos2, pl1, pth)
                pl1 = pl
                for pos2 in range(pos1 + 1, OFS + 7):
                    if map1[pos2] > 0:
                        break
                    pl1 += 1 if pos2 == OFS + 6 else 2
                    check_next(amph0, pos, energy, pos2, pl1, pth)
            else:
                if ((map1[amph_index] != 0 and map1[amph_index] != amph) or
                        (map1[amph_index + 4] != 0 and map1[amph_index + 4] != amph) or
                        (map1[amph_index+8] != 0 and map1[amph_index+8] != amph) or
                        (map1[amph_index + 12] != 0 and map1[amph_index + 12] != amph)):
                    continue
                while pos1 < OFS + amph:
                    pl += 1 if pos1 == OFS else 2
                    pos1 += 1
                    if map1[pos1] > 0:
                        blocked = True
                        break
                while pos1 > OFS + amph + 1:
                    pl += 1 if pos1 == OFS + 6 else 2
                    pos1 -= 1
                    if map1[pos1] > 0:
                        blocked = True
                        break
                if blocked:
                    continue
                pl += 2
                pos1 = OFS + amph - 5
                while pos1 - 4 >= 0:
                    if map1[pos1 - 4] > 0:
                        break
                    pl += 1
                    pos1 -= 4
                check_next(amph0, pos, energy, pos1, pl, pth)

    check(0, [])

    result = best_energy

    if best_solution:
        for p in best_solution:
            print(p["recur"], p["step"], p["energy"])
            # print(p["map"])

    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
