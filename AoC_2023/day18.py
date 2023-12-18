"""Code for day eighteen of advent of code 2023."""
import numpy as np
import sys

sys.setrecursionlimit(1000 * 1000)


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
    Process raw lines from the input file to direction, number of holes, colour, and empty map.
    """
    d = [line.split()[0] for line in raw_lines]
    n = [int(line.split()[1]) for line in raw_lines]
    c = [line.split()[2].lstrip("(").rstrip(")") for line in raw_lines]

    m = [["." for _ in range(1000)] for _ in range(1000)]

    return d, n, c, m


def process_input2(raw_lines):
    """
    Process raw lines from the input file into directions and number of holes.
    """
    dig_dict = {"0": "R", "1": "D", "2": "L", "3": "U"}

    d = [dig_dict[line.split()[2][-2]] for line in raw_lines]
    n = [int(line.split()[2].lstrip("(").rstrip(")")[1:-1], 16) for line in raw_lines]

    return d, n


def dig_edge(d, n, c, m, pos):
    """
    Take plain map and plot holes dug.
    """
    dir_dict = {
        "D": (0, 1, "v"),
        "R": (1, 0, ">"),
        "U": (0, -1, "^"),
        "L": (-1, 0, "<"),
    }

    for i, letter in enumerate(d):
        dir = dir_dict[letter]
        for j in range(n[i]):
            # print(pos)
            m[pos[1]][pos[0]] = "#"
            pos = (pos[0] + dir[0], pos[1] + dir[1])


def fill_interior(m, seed):
    """
    Flood fill interior of reservoir.
    """
    # print(seed)
    dir_dict = {
        "D": (0, 1, "v"),
        "R": (1, 0, ">"),
        "U": (0, -1, "^"),
        "L": (-1, 0, "<"),
    }

    m[seed[1]][seed[0]] = "#"

    for dir in dir_dict:
        check = (seed[0] + dir_dict[dir][0], seed[1] + dir_dict[dir][1])
        if m[check[1]][check[0]] == ".":
            fill_interior(m, check)


def get_volume(m):
    """
    Calculate Volume (area) inside reservoir using shoelace formula.
    """
    count = 0
    for j in range(len(m)):
        for i in range(len(m[0])):
            if m[j][i] == "#":
                count += 1
    return count


def get_coords(d, n, pos):
    """
    Generate coordinates of corners from digging instructions.
    """
    dir_dict = {
        "D": (0, 1, "v"),
        "R": (1, 0, ">"),
        "U": (0, -1, "^"),
        "L": (-1, 0, "<"),
    }
    corners = [
        pos,
    ]

    for i, letter in enumerate(d):
        dir = dir_dict[letter]
        for j in range(n[i]):
            pos = (pos[0] + dir[0], pos[1] + dir[1])
        corners.append(pos)
    return corners


def get_volume2(coords, n_vals):
    """
    Calculate Volume (area) inside reservoir using shoelace formula on corners.
    """
    a = 0
    for i, c in enumerate(coords[:-1]):
        a += (c[1] + coords[i + 1][1]) * (c[0] - coords[i + 1][0])
    return 0.5 * a + 0.5 * sum(n_vals) + 1


if __name__ == "__main__":
    # Part 1 - SLOW WAY
    # Get inputs
    dirs, n_holes, col, map = process_input(read_file("data/day18.dat"))
    # dirs, n_holes, col, map = process_input(read_file("data/day18.test"))

    dig_edge(dirs, n_holes, col, map, (500, 500))

    fill_interior(map, (501, 501))
    ans_one = get_volume(map)

    # print(dirs)
    # print(n_holes)
    # print(col)
    # print(np.asarray(map))

    print(f"Part one answer is {ans_one}")

    # Part 1 - Fast way as required for part 2
    # Get inputs
    dirs, n_holes, col, map = process_input(read_file("data/day18.dat"))
    # dirs, n_holes, col, map = process_input(read_file("data/day18.test"))
    cors = get_coords(dirs, n_holes, (1, 1))
    ans_one = get_volume2(cors, n_holes)
    print(f"Part one answer is {int(ans_one)}")

    # Part 2
    dirs, n_holes = process_input2(read_file("data/day18.dat"))
    # dirs, n_holes = process_input2(read_file("data/day18.test"))
    # dirs, n_holes = process_input(read_file("data/day18.dat"))
    # dirs, n_holes = process_input(read_file("data/day18.test"))

    cors = get_coords(dirs, n_holes, (1, 1))
    # print(cors)
    # print(n_holes)
    ans_two = get_volume2(cors, n_holes)

    print(f"Part two answer is {int(ans_two)}")
