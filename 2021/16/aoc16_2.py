# https://adventofcode.com/2021/day/16
from pathlib import Path
from functools import reduce

ref = False
part = "_2"

ext = "_ref.txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
input = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    bits = "{0:b}".format(int(input[0], 16))
    bits = bits.rjust((len(bits) + 7) & 0xfff8, "0")
    # print("BITS", bits, len(bits))
    bitsPtr = 0

    versionSum = 0

    def next(count):
        nonlocal bitsPtr
        # print("NEXT", int(bits[bitsPtr:bitsPtr + count], 2),
        #       bits[bitsPtr:bitsPtr + count])
        result = int(bits[bitsPtr:bitsPtr + count], 2)
        bitsPtr += count
        return result

    def nextPacket():
        nonlocal versionSum
        version = next(3)
        typeId = next(3)
        print("Packet", version, typeId)
        versionSum += version

        if typeId == 4:
            num = 0
            while True:
                digit = next(5)
                num = (num << 4) + (digit & 15)
                if digit & 16 == 0:
                    break
            return num
        else:
            packets = []

            # operator
            if next(1):
                subPacketCount = next(11)
                print("subPacketCount", subPacketCount)
                for i in range(subPacketCount):
                    packets.append(nextPacket())
            else:
                subPacketLength = next(15)
                print("subPacketLength", subPacketLength)
                until = bitsPtr + subPacketLength
                while bitsPtr < until:
                    packets.append(nextPacket())

            match typeId:
                case 0:
                    return sum(packets)

                case 1:
                    return reduce(lambda a, b: a*b, packets)

                case 2:
                    return min(packets)

                case 3:
                    return max(packets)

                case 5:
                    return packets[0] > packets[1]

                case 6:
                    return packets[0] < packets[1]

                case 7:
                    return packets[0] == packets[1]

        assert False, "Internal error"

    return nextPacket()


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
