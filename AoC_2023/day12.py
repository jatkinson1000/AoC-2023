"""Code for day twelve of advent of code 2023."""
from functools import cache


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(raw_lines, ncop=1):
    """
    Process raw lines from the input file to lists of ints.
    """

    s = [
        ((line.split()[0] + "?") * ncop)[:-1].rstrip(".").lstrip(".")
        for line in raw_lines
    ]

    n = [
        tuple(int(c) for c in ((line.split()[1] + ",") * ncop).rstrip(",").split(","))
        for line in raw_lines
    ]

    return s, n


# Decorate with cache to implement dynamic programming approach and store previous inputs
@cache
def n_ways(si, ni):
    """
    Recursively check for possible ways of generating pattern defined by ni using si.
    """

    # if there are no numbers left to be found this can only be achieved with
    # a sequence of dots - i.e. no '#'
    if len(ni) == 0:
        if "#" in si:
            return 0
        return 1

    # If there is no more sequence then check that there are no numbers left to be found
    # If there aren't there is only one way to achieve this.
    # If there are then this is an impossible sequence!
    if len(si) == 0:
        if len(ni) == 0:
            return 1
        return 0

    tot_ways = 0

    # If we start with a . we can ignore it as no impact on pattern
    # Remove and proceed.
    si = si.lstrip(".")

    # If we start with a '?' then get number of ways assuming the '?' is a dot
    if si[0] in "?" and len(si) > 0:
        tot_ways += n_ways(si[1:], ni)

    # Then get the number of ways assuming it is a #

    # If we start with a # followed by a ? the block of springs could be a pattern of
    # length 2 or more.

    # If the required chain length is more than the string length then it won't be found.
    # Check that there is no "." in the subsequent number of springs required for the next block of ni[0]
    # Check that the block of springs defined by ni[0] is exactly the length required, so either the end of si, or not followed by another spring "#".
    # If all this is the case then we have satisfied n[0], so remove this block of springs and n[0], and move to the rest of the chain searching for n[1]
    # After completing this search take one spring the front of the chain and repeat
    if (
        si[0] in "#?"
        and ni[0] <= len(si)
        and "." not in si[: ni[0]]
        and (ni[0] == len(si) or si[ni[0]] != "#")
    ):
        # If there are no numbers left to be found then check that there are no springs left in the string
        # If there are this is an invalid case so return 0
        # If there are not then the previous case was valid so return 1
        tot_ways += n_ways(si[ni[0] + 1 :], ni[1:])

    return tot_ways


if __name__ == "__main__":
    # Get inputs
    # springs, nums = process_input(read_file("data/day12.dat"), ncop=1)
    springs, nums = process_input(read_file("data/day12.test"), ncop=1)

    # for si, ni in zip(springs, nums):
    #     print(si)
    #     print(ni)

    # Part 1
    ans_one = 0
    for si, ni in zip(springs, nums):
        ans_one += n_ways(si, ni)

    print(f"Part one answer is {ans_one}")

    # Part 2
    # Get inputs and multiply by 5
    # springs, nums = process_input(read_file("data/day12.dat"), ncop=5)
    springs, nums = process_input(read_file("data/day12.test"), ncop=5)

    # for si, ni in zip(springs, nums):
    #     print(si)
    #     print(ni)

    ans_two = 0
    for si, ni in zip(springs, nums):
        # print(si)
        ans_two += n_ways(si, ni)

    print(f"Part rwo answer is {ans_two}")
