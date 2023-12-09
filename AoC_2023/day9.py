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


def next_val(s):
    """
    Recursively check diffs and store last val at each level, then sum for ans.
    """
    not_found = True
    d = s[:]
    last_val = [d[-1]]
    while not_found:
        d = list(diff(d))
        last_val.append(d[-1])
        if d.count(0) == len(d):
            not_found = False

    return sum(last_val)


def prev_val(s):
    """
    Recursively check diffs and store first val at each level, then subtract for ans.
    """
    # Recursively check diffs and store first val in seq
    not_found = True
    d = s[:]
    first_val = [d[0]]
    while not_found:
        d = list(diff(d))
        first_val.append(d[0])
        if d.count(0) == len(d):
            not_found = False

    for i in range(len(first_val) - 1, 0, -1):
        first_val[i - 1] = first_val[i - 1] - first_val[i]

    return first_val[0]


if __name__ == "__main__":
    seqs = process_input(read_file("data/day9.dat"))
    seqs = process_input(read_file("data/day9.test"))

    # print(seqs)

    # Parts 1 and 2
    ans_one = 0
    ans_two = 0
    for seq in seqs:
        ans_one += next_val(seq)
        ans_two += prev_val(seq)

    print(f"Part one answer is {ans_one}")

    print(f"Part two answer is {ans_two}")
