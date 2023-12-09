"""Code for day nine of advent of code 2023."""
from numpy import diff


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
    s = [[int(c) for c in line.split()] for line in raw_lines]

    return s


def extend_seq(s):
    """
    Recursively check diffs and store last/first val each time, then sum/subtract.
    """
    not_found = True
    d = s[:]
    last_val = [d[-1]]
    first_val = [d[0]]
    while not_found:
        d = list(diff(d))
        first_val.append(d[0])
        last_val.append(d[-1])
        if d.count(0) == len(d):
            not_found = False

    for i in range(len(first_val) - 1, 0, -1):
        first_val[i - 1] = first_val[i - 1] - first_val[i]

    return sum(last_val), first_val[0]


if __name__ == "__main__":
    # seqs = process_input(read_file("data/day9.dat"))
    seqs = process_input(read_file("data/day9.test"))

    # print(seqs)

    # Parts 1 and 2
    ans_one = 0
    ans_two = 0
    for seq in seqs:
        d_1, d_2 = extend_seq(seq)
        ans_one += d_1
        ans_two += d_2

    print(f"Part one answer is {ans_one}")
    print(f"Part two answer is {ans_two}")
