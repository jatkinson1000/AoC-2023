"""Code for Day one of advent of code 2023."""
import re
import numpy as np


# Dictionary to convert string numbers to integers
numdict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def extract_num_one(input: str) -> int:
    """
    Extract digits from a string and combine first and last to form a two-digit number.

    Parameters
    ----------
    input : str
        input string

    Returns
    -------
    num : int
        integer composed from first and last digit in input string
    """
    nums = re.findall(r"\d", input)
    try:
        num = 10 * int(nums[0]) + int(nums[-1])
        return num
    except IndexError:
        return 0


def extract_num_two(input: str) -> int:
    """
    Extract numbers from a string and combine first and last to form a two-digit number.

    'numbers' can be digits or words, upper and lower case, and words may overlap.

    Parameters
    ----------
    input : str
        input string containing word and numerical numbers

    Returns
    -------
    num : int
        integer composed from first and last 'numbers' in input string.
    """
    nums = []
    while len(input) > 0:
        try:
            nums.append(
                re.findall(
                    r"(?i)(\d|one|two|three|four|five|six|seven|eight|nine|zero)", input
                )[0]
            )
        except IndexError:
            pass
        input = input[1:]
    num = 10 * numdict[nums[0].lower()] + numdict[nums[-1].lower()]
    return num


if __name__ == "__main__":
    # Extract lines from day 1 file
    with open("data/day1.dat") as f:
        lines = f.readlines()

    # Answer for part 1
    nums_one = [extract_num_one(line) for line in lines]
    ans_one = np.sum(nums_one)
    print(f"Part one answer is {ans_one}.")

    # Answer for part 2
    nums_two = [extract_num_two(line) for line in lines]
    ans_two = np.sum(nums_two)
    print(f"Part two answer is {ans_two}.")
