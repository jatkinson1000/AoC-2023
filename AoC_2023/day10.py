"""Code for day ten of advent of code 2023."""
import numpy as numpy


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
    Process raw lines from the input file to lists of ints.
    """
    m = [[c for c in line] for line in raw_lines]

    xc = [[xi for xi in range(len(raw_lines[0]))] for _ in range(len(raw_lines))]
    yc = [[yi for _ in range(len(raw_lines[0]))] for yi in range(len(raw_lines))]

    return m, xc, yc


def start_coords(m):
    """
    Search map for start position 'S' and return x, y coords.
    """
    si = [[i, mi.index("S")] for i, mi in enumerate(m) if "S" in mi]
    # print(si)
    return si[0][1], si[0][0]


def start_dir(m, sx, sy, rev=False):
    """
    Search points around 'S' for the start of the loop and return relative position.
    """
    coords = [(xi, yi) for xi in range(-1, 2) for yi in range(-1, 2)]

    if rev:
        coords.reverse()

    for coord in coords:
        # print(x_i, y_i)
        (dx, dy) = coord
        match [dx, dy, m[sy + dy][sx + dx]]:
            case c if c in [[-1, 0, "F"], [-1, 0, "L"], [-1, 0, "-"]]:
                return -1, 0
            case c if c in [[0, -1, "F"], [0, -1, "7"], [0, -1, "|"]]:
                return 0, -1
            case c if c in [[1, 0, "J"], [1, 0, "F"], [1, 0, "-"]]:
                return 1, 0
            case c if c in [[0, 1, "L"], [0, 1, "J"], [0, 1, "|"]]:
                return 0, 1
            case _:
                pass

    raise ValueError("No matching start moves.")


def start_pipe(m, sx, sy):
    """
    Work out what part to replace 'S' by in order to close the loop.
    """
    (x1, y1) = start_dir(m, sx, sy)
    (x2, y2) = start_dir(m, sx, sy, rev=True)

    if x1 == x2:
        return "|"
    elif y1 == y2:
        return "-"
    elif (y1, x2) == (-1, -1) or (y2, x1) == (-1, -1):
        return "J"
    elif (y1, x2) == (-1, 1) or (y2, x1) == (-1, 1):
        return "L"
    elif (y1, x2) == (1, -1) or (y2, x1) == (1, -1):
        return "7"
    elif (y1, x2) == (1, 1) or (y2, x1) == (1, 1):
        return "F"

    raise ValueError("No suitable pipe to complete loop.")


def trace_loop(m, sx, sy, dx, dy):
    """
    Move around the loop from 'S' until returning to 'S', tracking x, y, and part type.
    """
    xvals = [sx, sx + dx]
    yvals = [sy, sy + dy]
    nvals = [m[sy][sx], map[sy + dy][sx + dx]]
    # print(xvals[-1], sx, yvals[-1], sy, xvals[-1] != sx and yvals[-1] != sy)
    while not (xvals[-1] == sx and yvals[-1] == sy):
        if nvals[-1] == "F":
            if dx < 0:
                xvals.append(xvals[-1])
                yvals.append(yvals[-1] + 1)
            else:
                xvals.append(xvals[-1] + 1)
                yvals.append(yvals[-1])
        elif nvals[-1] == "L":
            if dx < 0:
                xvals.append(xvals[-1])
                yvals.append(yvals[-1] - 1)
            else:
                xvals.append(xvals[-1] + 1)
                yvals.append(yvals[-1])
        elif nvals[-1] == "J":
            if dx > 0:
                xvals.append(xvals[-1])
                yvals.append(yvals[-1] - 1)
            else:
                xvals.append(xvals[-1] - 1)
                yvals.append(yvals[-1])
        elif nvals[-1] == "7":
            if dx > 0:
                xvals.append(xvals[-1])
                yvals.append(yvals[-1] + 1)
            else:
                xvals.append(xvals[-1] - 1)
                yvals.append(yvals[-1])
        elif nvals[-1] == "-":
            if dx < 0:
                xvals.append(xvals[-1] - 1)
                yvals.append(yvals[-1])
            else:
                xvals.append(xvals[-1] + 1)
                yvals.append(yvals[-1])
        elif nvals[-1] == "|":
            if dy < 0:
                xvals.append(xvals[-1])
                yvals.append(yvals[-1] - 1)
            else:
                xvals.append(xvals[-1])
                yvals.append(yvals[-1] + 1)
        else:
            raise ValueError(f"{xvals[-1]}, {yvals[-1]}, {nvals[-1]}")
        nvals.append(m[yvals[-1]][xvals[-1]])
        dx = xvals[-1] - xvals[-2]
        dy = yvals[-1] - yvals[-2]
        # print(xvals, yvals, nvals, (xvals[-1] == sx and yvals[-1] == sy))
        # print(xvals[-1], yvals[-1], nvals[-1], dx, dy)

    return xvals, yvals, nvals


if __name__ == "__main__":
    # Set numpy print options to fit maps into terminal output
    numpy.set_printoptions(linewidth=600, threshold=600 * 600)

    # Get inputs
    map, x, y = process_input(read_file("data/day10.dat"))
    # map, x, y = process_input(read_file("data/day10.test"))
    # map, x, y = process_input(read_file("data/day10.test2"))
    # map, x, y = process_input(read_file("data/day10.test3"))
    map, x, y = process_input(read_file("data/day10.test4"))

    # Convert to numpy array to get a nice printout to terminal
    # print(numpy.asarray(map))
    # print(numpy.asarray(x))
    # print(numpy.asarray(y))

    # Get position of start 'S'
    sx, sy = start_coords(map)
    # print(sx, sy, map[sx][sy])

    # Get direction to head in down from start to enter one end of loop
    dx1, dy1 = start_dir(map, sx, sy)
    # print(map[sx+dx1, sy+dy1], dx1, dy1)

    # Trace the loop and return x, y, coords of each successive node
    xp, yp, np = trace_loop(map, sx, sy, dx1, dy1)

    # Part 1
    # Half the length of the loop (rounded up)
    ans_one = int(numpy.ceil((len(np) - 1) / 2))
    print(f"Part one answer is {ans_one}")

    # Part 2
    ans_two = 0

    # Generate map with only the closed loop and sub 'S' to close loop
    bare = [["." for _ in range(len(map[0]))] for _ in range(len(map))]
    for i in range(len(xp)):
        bare[yp[i]][xp[i]] = map[yp[i]][xp[i]]
    bare[yp[0]][xp[0]] = start_pipe(map, sx, sy)

    # Loop along rows and if we cross as vertical pipe we are 'in' until we cross a
    # second vertical pipe. Count any '.' we cross when 'in'.
    for j in range(len(bare)):
        in_loop = False
        for i in range(len(bare[0])):
            if bare[j][i] in ["|"]:
                in_loop = not in_loop
            elif bare[j][i] in ["J", "L"]:
                in_loop = not in_loop
            elif bare[j][i] == "." and in_loop:
                bare[j][i] = "0"
                ans_two += 1

    # print(numpy.asarray(bare))

    print(f"Part two answer is {ans_two}")
