"""Code for Day two of advent of code 2023."""
import numpy as np

# Bag as defined by the problem
MY_BAG: np.ndarray = np.array([12, 13, 14])


def get_game_res(game_str: str) -> list[list[str]]:
    """
    Extract subgames from a game line and return as list of subgame results.

    Parameters
    ----------
    game_str : str
        input string from file line

    Returns
    -------
    res : list[list[str]]
        list of subgame results, each of which is a list of str "n colour"
    """
    subgames = game_str.split(":")[1].strip().split(";")
    res = [subgame.strip().split(",") for subgame in subgames]
    return res


def game_array(game: list[list[str]]) -> list[np.ndarray]:
    """
    Convert subgame results into array representation for each game.

    Parameters
    ----------
    game : list[list[str]]
        list of subgame results

    Returns
    -------
    game_res : list[np.ndarray]
        list of subgame results in array representation "(l Red, n Green, m Blue)"
    """
    game_res = []
    for subgame in game:
        subgame_res = np.zeros(3)
        for cubes in subgame:
            colour = cubes.strip().split(" ")
            if colour[1] == "red":
                subgame_res[0] = int(colour[0])
            elif colour[1] == "green":
                subgame_res[1] = int(colour[0])
            elif colour[1] == "blue":
                subgame_res[2] = int(colour[0])
            else:
                raise ValueError("Unexpected Colour Cube!")
        game_res.append(subgame_res)
    return game_res


def possible_game(game: list[np.ndarray], bag: np.ndarray) -> bool:
    """
    Check if all subgames in a list are possible using a given bag.

    Parameters
    ----------
    game : list[np.ndarray]
        list of subgame results in numpy representation

    Returns
    -------
    bool
        True if all subgames possible, otherwise False
    """
    for subgame in game:
        if (subgame > bag).any():
            return False
    return True


def min_cubes_reqd(game):
    """
    Scan all subgames to find minimum numbers of each colour required for game.

    Parameters
    ----------
    game : list[np.ndarray]
        list of subgame results in numpy representation

    Returns
    -------
    min_cubes : np.ndarray
        min number of each colour required for game (RGB)
    """
    min_cubes = np.zeros(3)
    for subgame in game:
        min_cubes = np.maximum(min_cubes, subgame)
    return min_cubes


if __name__ == "__main__":
    # Extract lines from day 2 file
    with open("data/day02.dat", encoding="utf8") as f:
        lines = f.readlines()

    # Extract games from lines
    games = [get_game_res(line) for line in lines]
    game_arr = [game_array(game) for game in games]

    # Answer for part 1
    ans_one = 0
    for i, game_i in enumerate(game_arr):
        if possible_game(game_i, MY_BAG):
            ans_one += i + 1
    print(f"Part one answer is {ans_one}.")

    # Answer for part 2
    ans_two = 0
    for i, game_i in enumerate(game_arr):
        game_set = min_cubes_reqd(game_i)
        game_power = int(np.prod(game_set))
        ans_two += game_power
    print(f"Part two answer is {ans_two}.")
