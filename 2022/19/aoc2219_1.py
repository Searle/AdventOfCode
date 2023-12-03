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

    ore_robots = 1
    clay_robots = 0
    obsidian_robots = 0
    geode_robots = 0

    min = 0

    MAX_MIN = 24

    max_req_ores = max(ore_ores, clay_ores, obsidian_ores, geode_ores)

# Blueprint 1:
#   Each ore robot costs 4 ore.
#   Each clay robot costs 2 ore.
#   Each obsidian robot costs 3 ore and 14 clay.
#   Each geode robot costs 2 ore and 7 obsidian.

# Blueprint 2:
#   Each ore robot costs 2 ore.
#   Each clay robot costs 3 ore.
#   Each obsidian robot costs 3 ore and 8 clay.
#   Each geode robot costs 3 ore and 12 obsidian.

    ore_strs = ["ore-collecting", "collects", "ore", "ore"]
    clay_strs = ["clay-collecting", "collects", "clay", "clay"]
    obsidian_strs = ["obsidian-collecting", "collects", "obsidian", "obsidian"]
    geode_strs = ["geode-cracking", "cracks", "open geode", "open geodes"]

    VERBOSE = True

    def sp(value, singular, plural):
        return str(value) + " " + singular if value == 1 else str(value) + " " + plural

    def get_spend(strs, count1, strs1, count2, strs2):
        spend = sp(count1, strs1[2], strs1[3])
        if count2:
            spend += " and " + sp(count2, strs2[2], strs2[3])
        return "Spend " + spend + " to start building a " + strs[0] + " robot."

    def print_delta(delta, robots, items, strs):
        if robots:
            item_label = sp(robots * delta, strs[2], strs[3])
            items_label = sp(items, strs[2], strs[3])
            print(robots, strs[0], "robot", strs[1],
                  item_label + "; you now have", items_label + ".")

    def print_new_robots(strs, count):
        if VERBOSE:
            print("The new", strs[0],
                  "robot is ready; you now have", count, "of them.")

    def add_mins(delta, in_fn):
        nonlocal min, ores, clays, obsidians, geodes

        print("DELTA", delta)

        min += delta
        ores += ore_robots * delta
        clays += clay_robots * delta
        obsidians += obsidian_robots * delta
        geodes += geode_robots * delta

        if VERBOSE:
            for i in range(0, delta):
                print("\n== Minute", min+i, "==")
                if i == 0:
                    value = in_fn(None)
                    # if value:
                    print(value)
                print_delta(delta, ore_robots, ores, ore_strs)
                print_delta(delta, clay_robots, clays, clay_strs)
                print_delta(delta, obsidian_robots, obsidians, obsidian_strs)
                print_delta(delta, geode_robots, geodes, geode_strs)

    while min < MAX_MIN:
        done = False

        if ores >= geode_ores and obsidians >= geode_obsidians:
            ores -= geode_ores
            obsidians -= geode_obsidians
            geode_robots += 1
            add_mins(1,
                     lambda _: get_spend(geode_strs, geode_ores, ore_strs, geode_obsidians, obsidian_strs))
            print_new_robots(geode_strs, geode_robots)
            done = True

        if ore_robots > 0 and clay_robots > 0:
            ore_mins = math.ceil((obsidian_ores - ores) / ore_robots)
            clay_mins = math.ceil((obsidian_clays - clays) / clay_robots)
            req_mins = max(ore_mins, clay_mins)
            if min + req_mins < MAX_MIN and obsidian_clays <= clays and obsidian_ores <= ores:
                clays -= obsidian_clays
                ores -= obsidian_ores
                add_mins(req_mins,
                         lambda _: get_spend(obsidian_strs, obsidian_clays, clay_strs, ores, ore_strs))
                obsidian_robots += 1
                print_new_robots(obsidian_strs, obsidian_robots)
                done = True

        if clays < obsidian_clays:
            req_mins = math.ceil((clay_ores - ores) / ore_robots)
            if min + req_mins < MAX_MIN and clay_ores <= ores:
                ores -= clay_ores
                add_mins(req_mins,
                         lambda _: get_spend(clay_strs, clay_ores, ore_strs, 0, []))
                clay_robots += 1
                print_new_robots(clay_strs, clay_robots)
                done = True

        if ores < max_req_ores:
            req_mins = math.ceil((ore_ores - ores) / ore_robots)
            if min + req_mins < MAX_MIN and ore_ores <= ores:
                ores -= ore_ores
                add_mins(req_mins,
                         lambda _: get_spend(ore_strs, clay_ores, ore_strs, 0, []))
                ore_robots += 1
                print_new_robots(ore_strs, ore_robots)
                done = True

        if not done:
            add_mins(1, lambda _: "?")

    result = geodes
    return result


# ---
result = run()
print(result)
open(path/("result" + part + ext), "w").write(str(result).rstrip() + "\n")
