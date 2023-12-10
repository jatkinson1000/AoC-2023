"""Code for Day four of advent of code 2023."""
import numpy as np


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(raw_lines: list[str]) -> tuple[list[int], list[int]]:
    """
    Process raw lines from the input file to lists of ints.
    """
    t = [int(val) for val in raw_lines[0].split(":")[1].split()]
    d = [int(val) for val in raw_lines[1].split(":")[1].split()]
    return t, d


def race(t_hold: int, t_race: int) -> int:
    """
    Get distance travelled in race after a hold of t_hold.

    Speed = t_hold. t_hold is part of race time.
    """
    dist = t_hold * (t_race - t_hold)
    return dist


def n_ways(time: int, rec: int) -> int:
    """
    Get number of ways of beating the distance record on a given race.

    Work from either end inwards.
    """
    i_min = 0
    dist = race(i_min, time)
    while dist <= rec:
        i_min += 1
        dist = race(i_min, time)

    i_max = time
    dist = race(i_max, time)
    while dist <= rec:
        i_max -= 1
        dist = race(i_max, time)

    # print(f"{i_max} ms gives {dist} mm beating {rec} mm")
    return i_max - i_min + 1


if __name__ == "__main__":
    # Dummy data
    t, d = process_input(read_file("data/day06.test"))

    # print(t, d)
    nways = [n_ways(ti, ri) for (ti, ri) in zip(t, d)]

    # Tests
    assert race(0, 7) == 0
    assert race(3, 7) == 12
    assert race(6, 7) == 6
    assert race(7, 7) == 0
    assert np.prod(np.asarray(nways)) == 288

    # Real code
    t, d = process_input(read_file("data/day06.dat"))

    # Get ways for all input races as list
    nways = [n_ways(ti, ri) for (ti, ri) in zip(t, d)]

    print(f"Part one answer is {np.prod(np.asarray(nways))}.")

    # Concat numbers as reqd for part 2
    t2 = int("".join([f"{ti}" for ti in t]))
    d2 = int("".join([f"{di}" for di in d]))

    print(f"Part one answer is {n_ways(t2, d2)}.")
