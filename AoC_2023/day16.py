"""Code for day sixteen of advent of code 2023."""
import numpy as numpy
from copy import deepcopy


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(raw_lines):
    """
    Process raw lines from the input file to map and empty path.
    """
    m = [[c for c in line] for line in raw_lines]

    e = [["." for _ in range(len(raw_lines[0]))] for _ in range(len(raw_lines))]

    return m, e


def trace_path(pos, d, m, path):
    """
    Trace light path around grid.

    Record direction of beam at each point and check for edges and loops.
    For each splitter use recursion to track multiple options.
    """
    dirs = [(0, 1, "v"), (1, 0, ">"), (0, -1, "^"), (-1, 0, "<")]
    obs = "/\\-|"

    # Loop until we hit a wall or map on top of an existing beam loop
    termination = False
    while not termination:
        pos = (pos[0] + d[0], pos[1] + d[1])
        # print(pos)
        if (
            pos[0] >= len(m[0])
            or pos[1] >= len(m)
            or pos[0] < 0
            or pos[1] < 0
            or d[2] in path[pos[1]][pos[0]]
        ):
            termination = True
        else:
            path[pos[1]][pos[0]] += d[2]

            if m[pos[1]][pos[0]] in obs:
                match m[pos[1]][pos[0]]:
                    case "|":
                        if d[2] in "><":
                            trace_path(pos, dirs[0], m, path)
                            trace_path(pos, dirs[2], m, path)
                            termination = True
                    case "-":
                        if d[2] in "^v":
                            trace_path(pos, dirs[1], m, path)
                            trace_path(pos, dirs[3], m, path)
                            termination = True
                    case "\\":
                        if d[2] == ">":
                            d = dirs[0]
                        elif d[2] == "<":
                            d = dirs[2]
                        elif d[2] == "v":
                            d = dirs[1]
                        elif d[2] == "^":
                            d = dirs[3]
                    case "/":
                        if d[2] == ">":
                            d = dirs[2]
                        elif d[2] == "<":
                            d = dirs[0]
                        elif d[2] == "v":
                            d = dirs[3]
                        elif d[2] == "^":
                            d = dirs[1]


def get_energisation_level(p):
    """
    Get energisation level of grid by counting any points with a beam.
    """
    e = 0
    for x in range(len(p[0])):
        for y in range(len(p)):
            # print(len(p[y][x]), p[y][x])
            if len(p[y][x]) > 1:
                e += 1
    return e


if __name__ == "__main__":
    # Get inputs
    map, energised = process_input(read_file("data/day16.dat"))
    # map, energised = process_input(read_file("data/day16.test"))

    # Part 1
    e_1 = deepcopy(energised)
    trace_path((-1, 0), (1, 0, ">"), map, e_1)

    # print(numpy.asarray(map))
    # print(numpy.asarray(x))
    # print(numpy.asarray(y))
    # print(numpy.asarray(energised))

    ans_one = get_energisation_level(e_1)
    print(f"Part one answer is {ans_one}")

    # Part 2
    # Check all possible entry points and keep maximum
    max_e = 0
    for xs in range(len(map[1])):
        e_i = deepcopy(energised)
        trace_path((xs, -1), (0, 1, "v"), map, e_i)
        max_e = max(get_energisation_level(e_i), max_e)

        e_i = deepcopy(energised)
        trace_path((xs, len(map)), (0, -1, "^"), map, e_i)
        max_e = max(get_energisation_level(e_i), max_e)

    for ys in range(len(map[0])):
        e_i = deepcopy(energised)
        trace_path((-1, ys), (1, 0, ">"), map, e_i)
        max_e = max(get_energisation_level(e_i), max_e)

        e_i = deepcopy(energised)
        trace_path((len(map[0]), ys), (-1, 0, "<"), map, e_i)
        max_e = max(get_energisation_level(e_i), max_e)

    print(f"Part two answer is {max_e}")
