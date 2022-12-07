# https://adventofcode.com/2021/day/24
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("../input" + part + ext), "r").read().rstrip().split("\n")
# ---

# Generate generated.c


def run():

    def padd(line):
        prg.append(line)

    in_int = 'int32_t'
    out_int = 'int32_t'

    IN_INT = 'IN_INT'
    OUT_INT = 'OUT_INT'

    prg = [
        '#include <stdint.h>',
        '',
        '// Generated with aoc24_1a-c-gen.py',
        '',
        '#define IN_INT ' + in_int,
        '#define OUT_INT ' + out_int,
        '',
        'void code(' + IN_INT + ' *in, ' + OUT_INT + ' *out) {',
        '    ' + OUT_INT + ' w = 0;',
        '    ' + OUT_INT + ' x = 0;',
        '    ' + OUT_INT + ' y = 0;',
        '    ' + OUT_INT + ' z = 0;',
    ]

    in_index = 0

    for input in inputs:
        m = input.split(' ')
        cmd = m[0]
        reg = m[1]
        val = m[2] if len(m) > 2 else "0"
        if cmd == 'inp':
            padd('    ' + reg + ' = (' + OUT_INT + ')' +
                 '(in[' + str(in_index) + ']);')
            in_index += 1
        elif cmd == 'add':
            padd('    ' + reg + ' += ' + val + ';')
        elif cmd == 'mul':
            if val == "0":
                padd('    ' + reg + ' = ' + val + ';')
            else:
                padd('    ' + reg + ' *= ' + val + ';')
        elif cmd == 'div':
            padd('    ' + reg + ' /= ' + val + ';')
        elif cmd == 'mod':
            padd('    ' + reg + ' %= ' + val + ';')
        elif cmd == 'eql':
            padd('    ' + reg + ' = ' + reg + ' == ' + val + ';')

    padd("    out[0] = w;")
    padd("    out[1] = x;")
    padd("    out[2] = y;")
    padd("    out[3] = z;")
    padd("}")

    return "\n".join(prg)


# ---
result = run()
print(result)
open(path/("generated.c"), "w").write(str(result).rstrip() + "\n")
