"""Code for Day seven of advent of code 2023."""


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(
    raw_lines: list[str], part2: bool = False
) -> tuple[list[list[int]], list[int]]:
    """
    Process raw lines from the input file to lists of ints.
    """
    c = [[ch for ch in val.split()[0]] for val in raw_lines]
    b = [int(val.split()[1]) for val in raw_lines]

    score_dict = {"A": "14", "K": "13", "Q": "12", "J": "11", "T": "10"}
    if part2:
        score_dict = {"A": "13", "K": "12", "Q": "11", "J": "0", "T": "10"}

    for k, v in score_dict.items():
        c = [[val.replace(k, v) for val in hand] for hand in c]

    c = [[int(val) for val in hand] for hand in c]

    return c, b


def get_strength_all(c: list[list[int]]) -> list[int]:
    """
    Get strength of all hands in card set.
    """

    st = [get_strength(h) for h in c]

    return st


def get_strength(h: list[int]) -> int:
    """
    Get strength of single hand accounting for jokers by trying all joker options.
    """
    # Jokers
    # Replace all Jokers with the same value because if multiple 3oak>2p and 40ak>fh
    if 0 in h:
        # print(f"There is a joker in {h}")
        h_st = -1000
        for i in range(1, 14):
            h_st = max(get_raw_strength([i if c == 0 else c for c in h]), h_st)
        return h_st
    # No Jokers
    else:
        return get_raw_strength(h)


def get_raw_strength(h: list[int]) -> int:
    """
    Get strength of single hand with any jokers having been replaced.
    """

    h_count = [h.count(val) for val in h]

    # 5 of a kind
    if 5 in h_count:
        return 6
    # 4 of a kind
    elif 4 in h_count:
        return 5
    # Full house
    elif 3 in h_count and 2 in h_count:
        return 4
    # 3 of a kind
    elif 3 in h_count:
        return 3
    # two pair
    elif h_count.count(2) == 4:
        return 2
    # one pair
    elif 2 in h_count:
        return 1
    # high card
    else:
        return 0


def get_rank(c: list[list[int]], st: list[int], b: list[int]) -> list:
    """
    Sort hands into order based on rank, then card values as they appear.
    """

    c_st = []
    for i in range(len(c)):
        c_st.append([c[i], b[i], st[i]])

    # print(c_st)

    r = sorted(c_st, key=lambda e: (e[2], e[0][0], e[0][1], e[0][2], e[0][3], e[0][4]))

    return r


if __name__ == "__main__":
    # Part 1
    cards, bid = process_input(read_file("data/day7.dat"))
    # cards, bid = process_input(read_file("data/day7.test"))

    strength = get_strength_all(cards)

    rank = get_rank(cards, strength, bid)

    ans_one = 0
    for i in range(len(rank)):
        ans_one += (i + 1) * rank[i][1]

    print(f"Part one answer is {ans_one}")

    # Part 2
    cards, bid = process_input(read_file("data/day7.dat"), part2=True)
    # cards, bid = process_input(read_file("data/day7.test"), part2=True)

    strength_2 = get_strength_all(cards)

    rank_2 = get_rank(cards, strength_2, bid)

    ans_two = 0
    for i in range(len(rank_2)):
        ans_two += (i + 1) * rank_2[i][1]

    print(f"Part two answer is {ans_two}")
