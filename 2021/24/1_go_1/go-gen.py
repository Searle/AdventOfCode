# https://adventofcode.com/2021/day/24
from pathlib import Path

ref = 0
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("../input" + part + ext), "r").read().rstrip().split("\n")
# ---

# Generate generated.go


def run():

    def padd(line):
        prg.append(line)

    in_int = 'int32'
    int = 'int32'

    prg = [
        'package main',
        '',
        '// Generated with go-gen.py',
        '',
        'func code(in_list [14]' + in_int + ') ' +
        '(' + int + ', ' + int + ', ' + int + ', ' + int + ') {',
        '    var w ' + int + ' = 0',
        '    var x ' + int + ' = 0',
        '    var y ' + int + ' = 0',
        '    var z ' + int + ' = 0',
    ]

    in_index = 0

    for input in inputs:
        m = input.split(' ')
        cmd = m[0]
        reg = m[1]
        val = m[2] if len(m) > 2 else "0"
        if cmd == 'inp':
            padd('    ' + reg + ' = ' + int +
                 '(in_list[' + str(in_index) + '])')
            in_index += 1
        elif cmd == 'add':
            padd('    ' + reg + ' += ' + val)
        elif cmd == 'mul':
            if val == "0":
                padd('    ' + reg + ' = ' + val)
            else:
                padd('    ' + reg + ' *= ' + val)
        elif cmd == 'div':
            padd('    ' + reg + ' /= ' + val)
        elif cmd == 'mod':
            padd('    ' + reg + ' %= ' + val)
        elif cmd == 'eql':
            padd('    if ' + reg + ' == ' + val + ' {')
            padd('        ' + reg + ' = 1')
            padd('    } else {')
            padd('        ' + reg + ' = 0')
            padd('    }')

    padd("    return w, x, y, z")
    padd("}")

    return "\n".join(prg)


# ---
result = run()
print(result)
open(path/("generated.go"), "w").write(str(result).rstrip() + "\n")
