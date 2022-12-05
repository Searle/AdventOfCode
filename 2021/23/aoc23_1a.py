# https://adventofcode.com/2021/day/23
from pathlib import Path

ref = 0
part = "_1"
debug = False

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + part + ext), "r").read().rstrip().split("\n")
# ---

# 08 09 10 11 12 13 14 15 16 17 18
#       04    05    06    07
#       00    01    02    03

#                  8  9  10 11  12 13  14 15  16 17 18
pos_to_in_paths = [0, 1, -1, 2, -1, 3, -1, 4, -1, 5, 6]

# Index is (amph_type - 1), then start point 8, 9, 11, 13, 15, 17 or 18
in_paths = (
    (
        (9, 10, 4, 0),
        (10, 4, 0),
        (10, 4, 0),
        (12, 11, 10, 4, 0),
        (14, 13, 12, 11, 10, 4, 0),
        (16, 15, 14, 13, 12, 11, 10, 4, 0),
        (17, 16, 15, 14, 13, 12, 11, 10, 4, 0)
    ),
    (
        (9, 10, 11, 12, 5, 1),
        (10, 11, 12, 5, 1),
        (12, 5, 1),
        (12, 5, 1),
        (14, 13, 12, 5, 1),
        (16, 15, 14, 13, 12, 5, 1),
        (17, 16, 15, 14, 13, 12, 5, 1),
    ),
    (
        (9, 10, 11, 12, 13, 14, 6, 2),
        (10, 11, 12, 13, 14, 6, 2),
        (12, 13, 14, 6, 2),
        (14, 6, 2),
        (14, 6, 2),
        (16, 15, 14, 6, 2),
        (17, 16, 15, 14, 6, 2)
    ),
    (
        (9, 10, 11, 12, 13, 14, 15, 16, 7, 3),
        (10, 11, 12, 13, 14, 15, 16, 7, 3),
        (12, 13, 14, 15, 16, 7, 3),
        (14, 15, 16, 7, 3),
        (16, 7, 3),
        (16, 7, 3),
        (17, 16, 7, 3)
    )
)

# Index is start point
out_paths = (
    (
        (4, 10, 9),
        (4, 10, 11),
        (4, 10, 9, 8),
        (4, 10, 11, 12, 13),
        (4, 10, 11, 12, 13, 14, 15),
        (4, 10, 11, 12, 13, 14, 15, 16, 17),
        (4, 10, 11, 12, 13, 14, 15, 16, 17, 18),
    ),
    (
        (5, 12, 11),
        (5, 12, 13),
        (5, 12, 11, 10, 9),
        (5, 12, 13, 14, 15),
        (5, 12, 11, 10, 9, 8),
        (5, 12, 13, 14, 15, 16, 17),
        (5, 12, 13, 14, 15, 16, 17, 18),
    ),
    (
        (6, 14, 13),
        (6, 14, 15),
        (6, 14, 13, 12, 11),
        (6, 14, 15, 16, 17),
        (6, 14, 15, 16, 17, 18),
        (6, 14, 15, 16, 11, 10, 9),
        (6, 14, 15, 16, 11, 10, 9, 8),
    ),
    (
        (7, 16, 15),
        (7, 16, 17),
        (7, 16, 17, 18),
        (7, 16, 15, 14, 13),
        (7, 16, 15, 14, 13, 12, 11),
        (7, 16, 15, 14, 13, 12, 11, 10, 9),
        (7, 16, 15, 14, 13, 12, 11, 10, 9, 8),
    ),
    (
        (10, 9),
        (10, 11),
        (10, 9, 8),
        (10, 11, 12, 13),
        (10, 11, 12, 13, 14, 15),
        (10, 11, 12, 13, 14, 15, 16, 17),
        (10, 11, 12, 13, 14, 15, 16, 17, 18),
    ),
    (
        (12, 11),
        (12, 13),
        (12, 11, 10, 9),
        (12, 13, 14, 15),
        (12, 13, 14, 17),
        (12, 13, 14, 17, 18),
        (12, 11, 10, 9, 8),
    ),
    (
        (14, 13),
        (14, 15),
        (14, 13, 12, 11),
        (14, 15, 16, 17),
        (14, 15, 16, 17, 18),
        (14, 15, 16, 11, 10, 9),
        (14, 15, 16, 11, 10, 9, 8),
    ),
    (
        (16, 15),
        (16, 17),
        (16, 17, 18),
        (16, 15, 14, 13),
        (16, 15, 14, 13, 12, 11),
        (16, 15, 14, 13, 12, 11, 10, 9),
        (16, 15, 14, 13, 12, 11, 10, 9, 8),
    ),
)

amph_energy = [1, 10, 100, 1000]


def run():
    map1 = [ord(inputs[3][3]) - ord('A') + 1,
            ord(inputs[3][5]) - ord('A') + 1,
            ord(inputs[3][7]) - ord('A') + 1,
            ord(inputs[3][9]) - ord('A') + 1,
            ord(inputs[2][3]) - ord('A') + 1,
            ord(inputs[2][5]) - ord('A') + 1,
            ord(inputs[2][7]) - ord('A') + 1,
            ord(inputs[2][9]) - ord('A') + 1] + [0] * 11

    at_pos = [-1, -1, -1, -1, -1, -1, -1, -1]
    for i in range(0, 8):
        if at_pos[map1[i] - 1] < 0:
            at_pos[map1[i] - 1] = i
        else:
            at_pos[map1[i] + 3] = i

    def map_str(map1, at_pos):
        str = ["_____________", "#...........#",
               "###.#.#.#.###", "###.#.#.#.###"]
        pos_to_coords = ((3, 2), (5, 2), (7, 2), (9, 2),
                         (3, 1), (5, 1), (7, 1), (9, 1),
                         (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                         (7, 0), (8, 0), (9, 0), (10, 0), (11, 0))
        # print(map1, at_pos)
        for amph0, pos in enumerate(at_pos):
            amph = (amph0 & 3) + 1

            assert(map1[pos] == amph)

            (x, y) = pos_to_coords[pos]
            str[y + 1] = str[y + 1][:x] + \
                chr(ord('A') + (amph0 & 3)) + str[y + 1][x + 1:]
        return "\n".join(str)

    seen = dict()
    recur = 0

    best_energy = 0
    best_solution = None

    def check(energy, pth):
        nonlocal best_energy
        nonlocal best_solution

        if (map1[0] == 1 and map1[1] == 2 and map1[2] == 3 and map1[3] == 4 and
                map1[4] == 1 and map1[5] == 2 and map1[6] == 3 and map1[7] == 4):
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

        def check_next(energy, pth):
            nonlocal recur

            if recur > 20:
                return

            amph = (amph0 & 3) + 1

            map1[pos] = 0
            map1[path[-1]] = amph
            at_pos[amph0] = path[-1]

            energy1 = amph_energy[amph - 1] * len(path)

            recur += 1

            if debug:
                check(energy + energy1,
                      pth.copy() + [{"recur": recur,
                                     "energy": energy1,
                                    "step": chr(ord('A') + (amph - 1)) + ":" + str(pos) + "->" + str(path[-1]),
                                     "map": map_str(map1, at_pos)}])
            else:
                check(energy + energy1, pth)
            recur -= 1

            map1[pos] = amph
            map1[path[-1]] = 0
            at_pos[amph0] = pos

        for amph0, pos in enumerate(at_pos):
            if pos < 8:
                for path in out_paths[pos]:
                    blocked = False
                    for p in path:
                        if map1[p] > 0:
                            blocked = True
                            break
                    if not blocked:
                        check_next(energy, pth)
            else:
                amph_index = amph0 & 3
                amph = amph_index + 1
                path = in_paths[amph_index][pos_to_in_paths[pos - 8]]
                blocked = False
                for p in path:
                    if map1[p] > 0:
                        if p < 4 and map1[p] == amph:
                            path = path[:-1]
                            break
                        blocked = True
                        break
                if not blocked:
                    check_next(energy, pth)

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
