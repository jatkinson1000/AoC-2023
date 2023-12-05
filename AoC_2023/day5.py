"""Code for Day five of advent of code 2023."""
from copy import deepcopy


def check_one_map(val, line):
    """
    Check a single map to see if it defines a location for a value.
    """
    if val in range(line[1], line[1] + line[2]):
        dest = line[0] + (val - line[1])
        return dest, True
    else:
        return val, False


def check_map_set(val, map):
    """
    Check through map and return location.
    If not found return 1:1 mapping.
    """
    found = False
    for line in map:
        loc, found = check_one_map(val, line)
        if found:
            return loc
    return val


def track_one_map(bounds_in, maps):
    """
    Track one seed interval through all mappings, subdividing ranges as necessary.
    """
    map_bounds = [[map[1], map[1] + map[2] - 1] for map in maps]
    bounds_new = deepcopy(bounds_in)
    i = 0
    while i < len(bounds_new):
        for pair in map_bounds:
            # Seeds fully remapped
            if bounds_new[i][0] >= pair[0] and bounds_new[i][1] <= pair[1]:
                # bounds_new.append([bound[0], bound[1]])
                pass
            # Partial remap of lower end of seeds
            elif bounds_new[i][0] >= pair[0] and bounds_new[i][0] <= pair[1]:
                # bounds_new.append([bound[0], pair[1]])
                bounds_new.append([pair[1] + 1, bounds_new[i][1]])
                bounds_new[i][1] = pair[1]
            # Partial remap of upper end of seeds
            elif bounds_new[i][1] >= pair[0] and bounds_new[i][1] <= pair[1]:
                bounds_new.append([pair[0], bounds_new[i][1]])
                bounds_new[i][1] = pair[0] - 1
            # Only part of seeds remapped
            elif bounds_new[i][0] < pair[0] and bounds_new[i][1] > pair[1]:
                bounds_new.append([pair[0], pair[1]])
                bounds_new.append([pair[1] + 1, bounds_new[i][1]])
                bounds_new[i][1] = pair[0] - 1
            # Seeds entirely above or below remapping range
            else:
                pass
            ##print(bounds_new)
        i += 1

    # Get output of these bounds
    bounds_out = [
        [check_map_set(val[0], maps), check_map_set(val[1], maps)] for val in bounds_new
    ]

    return bounds_out


if __name__ == "__main__":
    # Extract lines from day 4 file
    with open("data/day5.dat", encoding="utf8") as f:
        lines = f.readlines()

    # lines = ["seeds: 79 14 55 13\n",
    #          "\n",
    #          "seed-to-soil map:\n",
    #          "50 98 2\n",
    #          "52 50 48\n",
    #          "\n",
    #          "soil-to-fertilizer map:\n",
    #          "0 15 37\n",
    #          "37 52 2\n",
    #          "39 0 15\n",
    #          "\n",
    #          "fertilizer-to-water map:\n",
    #          "49 53 8\n",
    #          "0 11 42\n",
    #          "42 0 7\n",
    #          "57 7 4\n",
    #          "\n",
    #          "water-to-light map:\n",
    #          "88 18 7\n",
    #          "18 25 70\n",
    #          "\n",
    #          "light-to-temperature map:\n",
    #          "45 77 23\n",
    #          "81 45 19\n",
    #          "68 64 13\n",
    #          "\n",
    #          "temperature-to-humidity map:\n",
    #          "0 69 1\n",
    #          "1 0 69\n",
    #          "\n",
    #          "humidity-to-location map:\n",
    #          "60 56 37\n",
    #          "56 93 4\n",]

    lines = [line.strip() for line in lines]

    s = [int(val) for val in lines[0].split()[1:]]

    # Test data mappings
    # mappings = [
    # [[int(val) for val in line.split()] for line in lines[3:5]],
    # [[int(val) for val in line.split()] for line in lines[7:10]],
    # [[int(val) for val in line.split()] for line in lines[12:16]],
    # [[int(val) for val in line.split()] for line in lines[18:20]],
    # [[int(val) for val in line.split()] for line in lines[22:25]],
    # [[int(val) for val in line.split()] for line in lines[27:29]],
    # [[int(val) for val in line.split()] for line in lines[31:33]],
    # ]

    # Hard coding the mappings instead of inferring from file. BITE ME!
    mappings = [
        [[int(val) for val in line.split()] for line in lines[3:20]],
        [[int(val) for val in line.split()] for line in lines[22:36]],
        [[int(val) for val in line.split()] for line in lines[38:69]],
        [[int(val) for val in line.split()] for line in lines[71:89]],
        [[int(val) for val in line.split()] for line in lines[91:136]],
        [[int(val) for val in line.split()] for line in lines[138:176]],
        [[int(val) for val in line.split()] for line in lines[178:]],
    ]

    dests = deepcopy(s)
    for i, val in enumerate(s):
        for map in mappings:
            dests[i] = check_map_set(dests[i], map)
            # print(f"{val} -> {check_map_set(val, s2so)}")
    # print(f"{dests}")

    # Answer for part 1
    print(f"Part one answer is {min(dests)}")

    # Get seed starting bounds
    s_bounds = []
    for i in range(0, len(s), 2):
        s_bounds.append([s[i], s[i] + s[i + 1] - 1])
    # print(s_bounds)

    # Get seed bounds breaking up ranges based on map
    min_dest = int(1e30)
    for j, s_range in enumerate(s_bounds):
        # print(f"Seed range {j} of {len(s_bounds)}")
        # print(f"s_range = {s_range}")
        dests = [deepcopy(s_range)]
        for i, map in enumerate(mappings):
            # print(f"Map {i} of {len(mappings)}")
            dests = track_one_map(dests, map)
            # print(f"dests = {dests}")
        # print(f"dests = {dests}")
        min_dest = min(min_dest, min([min(pair) for pair in dests]))
        # print(min_dest)

    # print(dests)

    # print((min(dests)))

    # Answer for part 2
    print(f"Part two answer is {min_dest}")
