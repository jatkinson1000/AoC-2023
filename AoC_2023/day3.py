"""Code for day three of advent of code 2023."""

sym = ".1234567890"
symn = "1234567890"


def get_num(chars, i, j):
    """
    Search forwards and backwards for full number given its starting point.

    Parameters
    ----------
    chars : list[list[str]]
        input as a list of lines, each as a list of characters
    i : int
        Row location of starting point
    j : int
        Column location of starting point

    Returns
    -------
    num : int
        integer containing the full number
    : int
        number of places forward number occupies
    : int
        number of places backwards number occupies
    """
    num = [chars[i][j]]

    jb = j
    backsearch = True
    while backsearch:
        if jb > 0:
            if chars[i][jb - 1].isdigit():
                num.insert(0, chars[i][jb - 1])
                jb -= 1
            else:
                backsearch = False
        else:
            backsearch = False

    jf = j
    forsearch = True
    while forsearch:
        if jf + 1 < len(chars) - 2:
            if chars[i][jf + 1].isdigit():
                num.append(chars[i][jf + 1])
                jf += 1
            else:
                forsearch = False
        else:
            forsearch = False

    num.insert(0, "0")
    return int("".join(num)), jf - j, j - jb


if __name__ == "__main__":
    # Extract lines from day 3 file
    with open("data/day3.dat", encoding="utf8") as f:
        lines = f.readlines()

    # Example input
    # lines = ["467..114..\n",
    #          "...*......\n",
    #          "..35..633.\n",
    #          "......#...\n",
    #          "617*......\n",
    #          ".....+.58.\n",
    #          "..592.....\n",
    #          "......755.\n",
    #          ".....*....\n",
    #          "$664.598..\n",]

    lines = [line.strip() for line in lines]

    # append empty line above and below
    lenline = len(lines[0])
    extraline = "." * lenline
    lines.insert(0, extraline)
    lines.append(extraline)

    # Break down into list of individual characters
    chars = [[c for c in line] for line in lines]

    # Answer for part 1
    ans_one = 0
    for i, line in enumerate(chars[1:-1]):
        num = []
        is_part = False
        for j, char in enumerate(line):
            if char.isdigit():
                num.append(char)
                if chars[i][j] not in sym or chars[i + 2][j] not in sym:
                    is_part = True
                elif j > 0 and (
                    chars[i + 1][j - 1] not in sym
                    or chars[i][j - 1] not in sym
                    or chars[i + 2][j - 1] not in sym
                ):
                    is_part = True
                elif j < len(line) - 1 and (
                    chars[i + 1][j + 1] not in sym
                    or chars[i][j + 1] not in sym
                    or chars[i + 2][j + 1] not in sym
                ):
                    is_part = True
                if j == len(line) - 1 and is_part:
                    num.insert(0, "0")
                    numval = int("".join(num))
                    ans_one += numval
                    num = []
                    is_part = False

            elif is_part:
                num.insert(0, "0")
                numval = int("".join(num))
                ans_one += numval
                num = []
                is_part = False
            else:
                num = []
                is_part = False

    print(f"Part one answer is {ans_one}.")

    # Answer for part 2
    ans_two = 0
    for i, line in enumerate(chars[1:-1]):
        num1 = 0
        num2 = 0
        gear_1 = False
        is_gear = False
        search_t = [True, True, True]
        search_b = [True, True, True]
        for j, char in enumerate(line):
            if char in "*":
                # could be gear, check for adjacent numbers

                # Above (middle, then forward, then back)
                if chars[i][j] in symn:
                    gear_1 = True
                    num1, _, _ = get_num(chars, i, j)

                else:
                    bt = -1000
                    if chars[i][j + 1] in symn:
                        if gear_1:
                            is_gear = True
                            num2, ft, bt = get_num(chars, i, j + 1)
                        else:
                            gear_1 = True
                            num1, ft, bt = get_num(chars, i, j + 1)
                    if chars[i][j - 1] in symn and bt <= 0:
                        if gear_1:
                            is_gear = True
                            num2, _, _ = get_num(chars, i, j - 1)
                        else:
                            gear_1 = True
                            num1, _, _ = get_num(chars, i, j - 1)

                # Sides (forward, then back)
                if chars[i + 1][j + 1] in symn:
                    if gear_1:
                        is_gear = True
                        num2, _, _ = get_num(chars, i + 1, j + 1)
                    else:
                        gear_1 = True
                        num1, _, _ = get_num(chars, i + 1, j + 1)
                if chars[i + 1][j - 1] in symn:
                    if gear_1:
                        is_gear = True
                        num2, _, _ = get_num(chars, i + 1, j - 1)
                    else:
                        gear_1 = True
                        num1, _, _ = get_num(chars, i + 1, j - 1)

                # Bottom (middle, then forward, then back)
                if chars[i + 2][j] in symn:
                    if gear_1:
                        is_gear = True
                        num2, _, _ = get_num(chars, i + 2, j)
                    else:
                        gear_1 = True
                        num1, _, _ = get_num(chars, i + 2, j)
                else:
                    bb = -1000
                    if chars[i + 2][j + 1] in symn:
                        if gear_1:
                            is_gear = True
                            num2, fb, bb = get_num(chars, i + 2, j + 1)
                        else:
                            gear_1 = True
                            num1, fb, bb = get_num(chars, i + 2, j + 1)
                    if chars[i + 2][j - 1] in symn and bb <= 0:
                        if gear_1:
                            is_gear = True
                            num2, _, _ = get_num(chars, i + 2, j - 1)
                        else:
                            gear_1 = True
                            num1, _, _ = get_num(chars, i + 2, j - 1)

                if is_gear:
                    ans_two += num1 * num2

                num1 = 0
                num2 = 0
                gear_1 = False

    print(f"Part two answer is {ans_two}.")
