"""Code for Day four of advent of code 2023."""
import numpy as np


def get_data(lines: list[str]) -> tuple[list[list[int]], list[list[int]]]:
    """
    Clean input data and extract arrays of winning Nos and card Nos.

    Parameters
    ----------
    lines : list[str]
        input as a list of lines, each as a list of characters

    Returns
    -------
    win : list[list[int]]
        list of list of winning Nos for each card
    card : list[list[int]]
        list of list of card Nos for each card
    """
    clean_lines = [line.split(":")[1].strip().split("|") for line in lines]

    win = [sec[0] for sec in clean_lines]
    card = [sec[1] for sec in clean_lines]

    win = [line.strip().split() for line in win]
    card = [line.strip().split() for line in card]

    win = [[int(val.strip()) for val in vals] for vals in win]
    card = [[int(val.strip()) for val in vals] for vals in card]

    return win, card


def get_further_card_scores(wins, cards, i):
    """
    Clean input data and extract arrays of winning Nos and card Nos.

    Parameters
    ----------
    wins : list[list[int]]
        list of list of winning Nos for each card
    cards : list[list[int]]
        list of list of card Nos for each card
    i : int
        card for which we are calculating for

    Returns
    -------
    n + ans : int
        number of cards earnt from this card
    """
    # Loop over next n and get number of cards
    ans = 0

    n = card_score_2(wins[i], cards[i])
    n = min(len(wins) - 1 - i, n)

    for j in range(n):
        n2 = get_further_card_scores(wins, cards, i + j + 1)
        ans += n2

    return n + ans


def card_score(win, card):
    """
    Get part 1 score for card.

    Parameters
    ----------
    win : list[int]
        list of winning Nos for card
    card : list[int]
        list of card Nos for card

    Returns
    -------
    wcount : int
        points for this card (1 point for a match and double for each additional)
    """
    wcount = 0
    for _, num in enumerate(card):
        if num in win:
            if wcount == 0:
                wcount = 1
            else:
                wcount *= 2
    return wcount


def card_score_2(win, card):
    """
    Get part 2 score for card.

    Parameters
    ----------
    win : list[int]
        list of winning Nos for card
    card : list[int]
        list of card Nos for card

    Returns
    -------
    wcount : int
        points for this card (No. matching numbers)
    """
    wcount = 0
    for _, num in enumerate(card):
        if num in win:
            wcount += 1
    return wcount


if __name__ == "__main__":
    # Extract lines from day 4 file
    with open("data/day04.dat", encoding="utf8") as f:
        lines = f.readlines()

    # lines = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
    #         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
    #         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
    #         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
    #         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
    #         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n",]

    lines = [line.strip() for line in lines]

    w, c = get_data(lines)

    ans_one = 0
    for i, _ in enumerate(w):
        ans_one += card_score(w[i], c[i])

    # Answer for part 1
    print(f"Part one answer is {ans_one}.")

    ans_two = 0
    copies = np.zeros(len(w))
    for i, _ in enumerate(w):
        ans_two += get_further_card_scores(w, c, i)

    # Answer for part 2
    print(f"Part two answer is {ans_two + len(w)}.")
