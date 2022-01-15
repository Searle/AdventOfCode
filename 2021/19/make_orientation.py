# https://adventofcode.com/2021/day/19

xx = [
    lambda p: (p[0],  p[1],  p[2]),  # 0
    lambda p: (p[0],  p[2], -p[1]),  # x + 1
    lambda p: (p[0], -p[1], -p[2]),  # x + 2
    lambda p: (p[0], -p[2],  p[1]),  # x + 3
]

inv_xx = [
    lambda p: (p[0],  p[1],  p[2]),  # 0
    lambda p: (p[0], -p[2],  p[1]),  # x + 1
    lambda p: (p[0], -p[1], -p[2]),  # x + 2
    lambda p: (p[0],  p[2], -p[1]),  # x + 3
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


imap = {0: 0, 1: 3, 2: 2, 3: 1}

lookup = {}
inv_lookup = {}
for xi, x in enumerate(xx):
    for yi, y in enumerate(yy):
        for zi, z in enumerate(zz):
            p = z(y(x((1, 2, 3))))
            inv_p = xx[imap[xi]](yy[imap[yi]]
                                 (zz[imap[zi]]((-1, -2, -3))))

            # p = x((1, 2, 3))
            # inv_p = xx[(xi + 2) & 3]((1, 2, 3))

            # inv_p = x(y(z((1, 2, 3))))

            fn = "lambda p: (" + \
                par(p[0]) + "," + \
                par(p[1]) + "," + \
                par(p[2]) + ")"
            inv_fn = "lambda p: (" + \
                par(inv_p[0]) + "," + \
                par(inv_p[1]) + "," + \
                par(inv_p[2]) + ")"

            # if fn == "lambda p: (p[2],-p[1],p[0])":

            lookup[fn + ","] = True
            inv_lookup[inv_fn + ","] = True

print("    orients = [")
print("       ", "\n        ".join(lookup.keys()))
print("    ]\n")
print("    inv_orients = [")
print("       ", "\n        ".join(inv_lookup.keys()))
print("    ]")
