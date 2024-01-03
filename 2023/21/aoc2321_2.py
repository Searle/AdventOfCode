# https://adventofcode.com/2023/day/21

from pathlib import Path

# from PIL import Image, ImageDraw

ref = 0
part = "_2"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path / ("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():
    result = 0

    mw = len(inputs[0])
    mh = len(inputs)
    ofs = mw * 10

    start = (0, 0)
    walls = set()

    for y, input in enumerate(inputs):
        for x in range(0, mw):
            if input[x] == "#":
                walls.add((x, y))
            elif input[x] == "S":
                start = (x + ofs, y + ofs)

    def run1(steps1, answer):
        nonlocal result

        def print_maze(x0, x1, y0, y1):
            count = 0
            print("---")
            for y in range(mh * y0, mh * (y1)):
                s = ""
                for x in range(mw * x0, mw * (x1)):
                    pos = (x + ofs, y + ofs)
                    if pos == start:
                        s += "*"
                    elif pos in fills:
                        if ((pos[0] + pos[1]) & 1) == 0:
                            s += "O"
                            count += 1
                        else:
                            s += "0"
                    elif (pos[0] % mw, pos[1] % mh) in walls:
                        s += "#"
                    else:
                        s += "."
                print("MAZE", s)
            return count

        def count_maze(x0, x1, y0, y1):
            count = 0
            for y in range(mh * y0, mh * y1):
                for x in range(mw * x0, mw * x1):
                    pos = (x + ofs, y + ofs)
                    if pos in fills:
                        if ((pos[0] + pos[1]) & 1) == steps & 1:
                            count += 1
            return count

        steps1div, steps1mod = divmod(steps1, mw)

        r = 4 + (steps1div & 1)

        # r = steps1div  # Orig size

        steps = mw * r + steps1mod

        print("STEPS", steps1, "steps=", steps, "div=", steps1div, "mod=", steps1mod)

        dirs2 = ((0, -1), (1, 0), (0, 1), (-1, 0))

        fills = set()
        toFill = {start}

        for _ in range(0, steps + 1):
            nextToFill = set()
            for pos in toFill:
                fills.add(pos)
                for dir in dirs2:
                    pos2 = (pos[0] + dir[0], pos[1] + dir[1])
                    pos3 = (pos2[0] % mw, pos2[1] % mh)
                    if not pos2 in toFill and not pos3 in walls:
                        nextToFill.add(pos2)
            toFill = nextToFill

        if False:
            result1 = 0
            for x, y in fills:
                if ((x + y) & 1) == 0:
                    result1 += 1
            print("RESULT1", result1)

        # image = Image.new("RGB", (100 + r * 100, 100 + r * 100))
        # draw = ImageDraw.Draw(image)

        def fn(x, y):
            # draw.rectangle(
            #     (
            #         (x + r + 0.5) * 50,
            #         (y + r + 0.5) * 50,
            #         (x + r + 1.5) * 50,
            #         (y + r + 1.5) * 50,
            #     )
            # )
            return count_maze(x, x + 1, y, y + 1)

        if True:
            print("\n")
            res2 = 0
            for y in range(-r - 2, r + 3):
                for x in range(-r - 2, r + 3):
                    res2 += fn(x, y)
                    print(str((fn(x, y)) if fn(x, y) > 0 else "").rjust(6), end="")
                print("\n")
            print("RES2", res2)

        ac0 = fn(0, -r)
        ac1 = fn(0, -r + 1)
        a0 = fn(1, -r)
        a1 = fn(1, -r + 1)
        a2 = fn(1, -r + 2)

        bc0 = fn(r, 0)
        bc1 = fn(r - 1, 0)
        b0 = fn(r, 1)
        b1 = fn(r - 1, 1)
        b2 = fn(r - 2, 1)

        cc0 = fn(0, r)
        cc1 = fn(0, r - 1)
        c0 = fn(-1, r)
        c1 = fn(-1, r - 1)
        c2 = fn(-1, r - 2)

        dc0 = fn(-r, 0)
        dc1 = fn(-r + 1, 0)
        d0 = fn(-r, -1)
        d1 = fn(-r + 1, -1)
        d2 = fn(-r + 2, -1)

        ev = fn(0, 0)
        od = fn(1, 0)

        # image.save("2023/21/canvas" + ext + ".png")

        print("     ", steps1, "ev=", ev, "od=", od, "steps1div=", steps1div)
        print("     ", steps1, "ac0..dc0=", ac0, bc0, cc0, dc0)
        print("     ", steps1, "ac1..dc1=", ac1, bc1, cc1, dc1)
        print("     ", steps1, "a0..d0=", a0, b0, c0, d0)
        print("     ", steps1, "a1..d1=", a1, b1, c1, d1)
        print("     ", steps1, "a2..d2=", a2, b2, c2, d2)
        e = 0
        e += ac0 + bc0 + cc0 + dc0
        e += ac1 + bc1 + cc1 + dc1
        e += (a0 + b0 + c0 + d0) * (steps1div)
        e += (a1 + b1 + c1 + d1) * (steps1div - 1)
        e += (a2 + b2 + c2 + d2) * (steps1div - 2)
        if steps1div & 1:
            e += ev * (steps1div - 2) * (steps1div - 2)
            e += od * (steps1div - 1) * (steps1div - 1)
        else:
            e += od * (steps1div - 2) * (steps1div - 2)
            e += ev * (steps1div - 1) * (steps1div - 1)

        result = e

        print(
            "RES  ",
            steps1,
            "res=",
            result,
            "answer=",
            answer,
            "diff=",
            result - answer,
            "\n",
        )

    if ref == 1:
        run1(50, 1594)
        run1(100, 6536)
        run1(500, 167004)
        run1(1000, 668697)
        run1(5000, 16733044)
    elif ref == 2:  # Steppis Daten
        run1(26501365, 632257949158206)
    else:
        run1(26501365, 605247138198755)

    return result


# ---
result = run()
print(result)
open(path / ("result" + part + ext), "w").write(str(result).rstrip() + "\n")
