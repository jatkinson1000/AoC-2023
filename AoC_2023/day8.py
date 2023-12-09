"""Code for Day eight of advent of code 2023."""
from numpy import lcm

def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(
    raw_lines
):
    """
    Process raw lines from the input file to lists of ints.
    """
    d = [{"L": 0, "R": 1}[val] for val in raw_lines[0]]
    n = [line[0:3] for line in raw_lines[2:]]
    m = [[line[7:10], line[12:15]] for line in raw_lines[2:]]

    return d, n, m


def path_length(n, d, start, part2=False):
    found = False
    i = 0
    n_n = n.index(start)
    while not found:
        # print(i, n_n, nodes[n_n])
        d_n = d[i%len(d)]
        n_n = n.index(map[n_n][d_n])

        i +=1
        
        if part2:
            if n[n_n][2] == "Z":
                found = True
                return i
        else:
            if n[n_n] == "ZZZ":
                found = True
                return i


if __name__ == "__main__":
    # Part 1
    dirs, nodes, map = process_input(read_file("data/day8.dat"))
    # dirs, nodes, map = process_input(read_file("data/day8.test"))

    # print(dirs)
    # print(nodes)

    print(f"Part one answer is {path_length(nodes, dirs, 'AAA')}")

    # Part 2
    # dirs, nodes, map = process_input(read_file("data/day8.test2"))

    start_nodes = [n for n in nodes if n[2] == "A"]
    path_lens = sorted([path_length(nodes, dirs, node, True) for node in start_nodes])
    print(path_lens)

    print(f"Part two answer is {lcm.reduce(path_lens)}")
