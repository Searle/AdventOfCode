# https://adventofcode.com/2022/day/19

from pathlib import Path
import re
import math

ref = 1
part = "_1"

ext = "_ref" + str(ref) + ".txt" if ref else ".txt"
path = Path(__file__).parent.absolute()
inputs = open(path/("input" + ext), "r").read().rstrip().split("\n")
# ---


def run():

    input = inputs[0]

    m = re.match(
        r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', input)

    assert m is not None

    (no, ore_ores, clay_ores, obsidian_ores,
     obsidian_clays, geode_ores, geode_obsidians) = [int(s) for s in m.groups()]

    print(no, ore_ores, clay_ores, obsidian_ores,
          obsidian_clays, geode_ores, geode_obsidians)

    ores = 0
    clays = 0
    obsidians = 0
    geodes = 0

    ore_robots = 0
    clay_robots = 0
    obsidian_robots = 0
    geode_robots = 0

    geodes_max = 0

    day = 0

    req_ores = max(ore_ores, clay_ores, obsidian_ores, geode_ores)

# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.

    def next_min() -> bool:
        min += 1
        ores += ore_robots
        clays += clay_robots
        obsidians += obsidian_robots
        geodes += geode_robots
        if min >= 24:
            if geodes_max < geodes:
                geodes_max = geodes
            return True
        return False

    def add_mins(delta) -> bool:
        min += delta
        ores += ore_robots * delta
        clays += clay_robots * delta
        obsidians += obsidian_robots * delta
        geodes += geode_robots * delta

    def f2() -> bool:
        if next_min():
            return False
        return f()

    def f() -> bool:

        if ores >= geode_ores and obsidians >= geode_obsidians:
            ores -= geode_ores
            obsidians -= geode_obsidians
            geode_robots += 1
            add_mins(1)
            return f2()

        if ore_robots > 0 and clay_robots > 0:
            ore_mins = math.ceil((obsidian_ores - ores) / ore_robots)
            clay_mins = math.ceil((obsidian_clays - clays) / clay_robots)
            req_mins = max(ore_mins, clay_mins)
            if mins + req_mins < 24:
                clays -= obsidian_clays * req_mins
                ores -= obsidian_ores * req_mins
                obsidian_robots += 1
                add_mins(req_mins)
                return f2()

        if clay < obsidian_clays and ore_robots > 0:
            req_mins = math.ceil((clay_ores - ores) / ore_robots)
            if mins + req_mins < 24:
                ores -= clay_ores * req_mins
                clay_robots += 1
                add_mins(req_mins)
                return f2()

        if ores < req_ores:
            req_mins = math.ceil((ore_ores - ores) / ore_robots)
            if mins + req_mins < 24:
                ores -= ore_ores
                ore_robots += 1
                add_mins(req_mins)

                return f2()

        return next_min()

    result = 0
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
