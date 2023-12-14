"""Code for day fourteen of advent of code 2023."""
import numpy as np


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def tilt_north(g):
    # Loop over columns
    for i in range(len(g[0])):
        for j in range(len(g) - 1):
            # If cube or round ignore
            if g[j][i] in "#O":
                pass

            # If gap, look for next round rock and swap
            # If none then move to next.
            elif g[j][i] in ".":
                k = 1
                while g[j + k][i] not in "O#" and j + k < len(g) - 1:
                    k += 1
                if g[j + k][i] == "O":
                    g[j] = g[j][:i] + "O" + g[j][i + 1 :]
                    g[j + k] = g[j + k][:i] + "." + g[j + k][i + 1 :]

            else:
                raise ValueError("What is this type of rock!?")
    return g


def tilt_south(g):
    # Loop over columns
    for i in range(len(g[0])):
        for j in range(len(g) - 1, 0, -1):
            # If cube or round ignore
            if g[j][i] in "#O":
                pass

            # If gap, look for next round rock and swap
            # If none then move to next.
            elif g[j][i] in ".":
                k = 1
                while g[j - k][i] not in "O#" and j - k > 0:
                    k += 1
                if g[j - k][i] == "O":
                    g[j] = g[j][:i] + "O" + g[j][i + 1 :]
                    g[j - k] = g[j - k][:i] + "." + g[j - k][i + 1 :]

            else:
                raise ValueError("What is this type of rock!?")
    return g


def tilt_west(g):
    for j in range(len(g)):
        for i in range(len(g[0]) - 1):
            # If cube or round ignore
            if g[j][i] in "#O":
                pass

            # If gap, look for next round rock and swap
            # If none then move to next.
            elif g[j][i] in ".":
                k = 1
                while g[j][i + k] not in "O#" and i + k < len(g[j]) - 1:
                    k += 1
                if g[j][i + k] == "O":
                    g[j] = (
                        g[j][:i] + "O" + g[j][i + 1 : i + k] + "." + g[j][i + k + 1 :]
                    )

            else:
                raise ValueError("What is this type of rock!?")
    return g


def tilt_east(g):
    for j in range(len(g)):
        for i in range(len(g[0]) - 1, 0, -1):
            # If cube or round ignore
            if g[j][i] in "#O":
                pass

            # If gap, look for next round rock and swap
            # If none then move to next.
            elif g[j][i] in ".":
                k = 1
                while g[j][i - k] not in "O#" and i - k > 0:
                    k += 1
                if g[j][i - k] == "O":
                    g[j] = (
                        g[j][: i - k] + "." + g[j][i - k + 1 : i] + "O" + g[j][i + 1 :]
                    )

            else:
                raise ValueError("What is this type of rock!?")
    return g


def cycle_grid(g):
    g = tilt_north(g)
    g = tilt_west(g)
    g = tilt_south(g)
    g = tilt_east(g)
    return g


def get_load(g):
    l = 0
    for j, row in enumerate(g):
        l += row.count("O") * (len(g) - j)
    return l


if __name__ == "__main__":
    # Get inputs
    grid = read_file("data/day14.dat")
    # grid = (read_file("data/day14.test"))

    # Check things are working as expected:
    # [print(row) for row in grid]
    # print("\n")
    # grid = tilt_north(grid)
    # [print(row) for row in grid]
    # print("\n")
    # grid = tilt_west(grid)
    # [print(row) for row in grid]
    # print("\n")
    # grid = tilt_east(grid)
    # [print(row) for row in grid]
    # print("\n")
    # grid = cycle_grid(grid)
    # [print(row) for row in grid]
    # print("\n")

    # Part 1
    ans_one = 0
    grid = tilt_north(grid)
    # [print(row) for row in grid]
    ans_one = get_load(grid)
    print(f"Part one answer is {ans_one}")

    # Part 2
    # The rocks will eventually end up moving in a cycle, so keep rotating and
    # recording the positions, and check to see if a cycle has formed

    loop = False
    loads = []
    grids = []
    loop_len = 0
    while not loop:
        grid = cycle_grid(grid)
        loads.append(get_load(grid))
        grids.append("".join(grid))

        # Smallest loop could be 1, largest could be len/2
        for i in range(1, len(grids) // 2):
            trial_loop = grids[-i:]
            if grids[-2 * i : -i] == trial_loop:
                loop_len = i
                loop = True

    # remove 'pre-loop' elements, then work out how far through a loop we are on
    # iteration 1000000000
    loop_loads = loads[-loop_len:]
    ans_two = loop_loads[(1000000000 - (len(loads) % len(loop_loads))) % loop_len - 1]

    print(f"Part two answer is {ans_two}")
