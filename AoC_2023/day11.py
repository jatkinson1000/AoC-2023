"""Code for day eleven of advent of code 2023."""
import numpy as np

# Set numpy print options to fit maps into terminal output
np.set_printoptions(linewidth=600, threshold=600 * 600)


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(
    raw_lines: list[str], e: int = 2
) -> tuple[list[list[str]], list[list[int]], list[list[str]]]:
    """
    Process raw lines from the input file to lists of ints.
    """
    g = [[c for c in line] for line in raw_lines]

    d = get_dist_grid(g, e)

    gc = [
        [xi, yi] for xi in range(len(g[0])) for yi in range(len(g)) if g[yi][xi] == "#"
    ]

    return g, gc, d


def get_dist_grid(g: list[list[str]], efac: int = 2) -> list[list[str]]:
    d = [["1" for _ in range(len(g[0]))] for _ in range(len(g))]

    irow = 0
    while irow < len(g):
        if g[irow].count("#") == 0:
            # print(f"expanding row {irow}")
            d[irow] = [str(efac)] * len(g[0])
        irow += 1

    # Columns
    icol = 0
    while icol < len(g[0]):
        if [row[icol] for row in g].count("#") == 0:
            # print(f"expanding column {icol}")
            for row in d:
                row[icol] = str(efac)
        icol += 1

    return d


if __name__ == "__main__":
    # Get inputs
    gals, gc, dists = process_input(read_file("data/day11.dat"))
    # gals, gc, dists = process_input(read_file("data/day11.test"))

    # print(np.asarray(gals))
    # print(np.asarray(gc))
    # print(np.asarray(dists))

    # Part 1
    ans_one = 0

    for ci, c1 in enumerate(gc):
        for c2 in gc[ci + 1 :]:
            xd = dists[0][min(c1[0], c2[0]) : max(c1[0], c2[0])]
            # print(c1, c2, sum([int(x) for x in xd]))
            ans_one += sum([int(x) for x in xd])

            yd = [y[0] for y in dists][min(c1[1], c2[1]) : max(c1[1], c2[1])]
            # print(c1, c2, sum([int(y) for y in yd]))
            ans_one += sum([int(y) for y in yd])

    print(f"Part one answer is {ans_one}")

    # Part 2
    ans_two = 0
    gals, gc, dists = process_input(read_file("data/day11.dat"), e=1000000)
    # gals, gc, dists = process_input(read_file("data/day11.test"), e=10)
    # gals, gc, dists = process_input(read_file("data/day11.test"), e=100)

    for ci, c1 in enumerate(gc):
        for c2 in gc[ci + 1 :]:
            xd = dists[0][min(c1[0], c2[0]) : max(c1[0], c2[0])]
            # print(c1, c2, sum([int(x) for x in xd]))
            ans_two += sum([int(x) for x in xd])

            yd = [y[0] for y in dists][min(c1[1], c2[1]) : max(c1[1], c2[1])]
            # print(c1, c2, sum([int(y) for y in yd]))
            ans_two += sum([int(y) for y in yd])

    print(f"Part two answer is {ans_two}")
