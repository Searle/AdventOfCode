# https://adventofcode.com/2021/day/19

xx = [
    lambda p: (p[0],  p[1],  p[2]),  # 0
    lambda p: (p[0],  p[2], -p[1]),  # x + 1
    lambda p: (p[0], -p[1], -p[2]),  # x + 1
    lambda p: (p[0], -p[2],  p[1]),  # x + 3
]

yy = [
    lambda p: (p[0], p[1], p[2]),  # 0
    lambda p: (p[2], p[1], -p[0]),  # y + 1
    lambda p: (-p[0], p[1], -p[2]),  # y + 2
    lambda p: (-p[2], p[1], p[0]),  # y + 3
]

zz = [
    lambda p: (p[0],  p[1],  p[2]),  # 0
    lambda p: (p[1], -p[0],  p[2]),  # z + 1
    lambda p: (-p[0], -p[1],  p[2]),  # z + 2
    lambda p: (-p[1],  p[0],  p[2]),  # z + 3
]


def par(p):
    return ("-" if p < 0 else "") + "p[" + str(abs(p)-1) + "]"


lookup = {}
for x in xx:
    for y in yy:
        for z in zz:
            p = z(y(x((1, 2, 3))))
            lookup["lambda p: ("+par(p[0])+"," +
                   par(p[1])+","+par(p[2]) + "),"] = True

print("\n".join(lookup.keys()))
