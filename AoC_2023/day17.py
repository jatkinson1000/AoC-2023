"""Code for day seventeen of advent of code 2023."""
import numpy as np
import heapq


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
    Process raw lines from the input file map and dist matrix.
    """
    m = [[int(c) for c in line] for line in raw_lines]
    d = [[np.inf for _ in range(len(raw_lines[0]))] for _ in range(len(raw_lines))]
    p = [[[0] for _ in range(len(raw_lines[0]))] for _ in range(len(raw_lines))]
    pd = [[(0,) for _ in range(len(raw_lines[0]))] for _ in range(len(raw_lines))]

    return m, d, p, pd


def a_star_path(pos, end, mp, dis, pth, pdirs, p2=False):
    """
    Perform pathfinding via A* algorithm with modifications as required for the problem.
    """
    dirs = [(0, 1, "v"), (1, 0, ">"), (0, -1, "^"), (-1, 0, "<")]
    opdir = {
        "v": "^",
        "^": "v",
        ">": "<",
        "<": ">",
    }

    min_row = 1
    max_row = 3
    if p2:
        min_row = 4
        max_row = 10

    # Implement A* with restriction on 3 consecutive.

    # Initialise
    traversed = set()
    queue = []

    # First step
    dis[pos[1]][pos[0]] = 0
    pth[pos[1]][pos[0]] = [(0, 0), (0, 0)]
    pdirs[pos[1]][pos[0]] = (("."), ("."))

    # Add to the queue the distance to this point, coords, and dirs.
    heapq.heappush(queue, (0, (0, 0), (".", ".", ".")))

    i = 0
    while queue:
        # print("\n")

        # Pull next shortest path off the heap and get location
        cur_dist, cur_pos, last_dirs = heapq.heappop(queue)
        pos = cur_pos

        # Check we've not attempted to visit this node via this edge route already
        if (pos, last_dirs) in traversed:
            i += 1
            continue

        # Add node via this route to list of checked and then process it
        traversed.add((pos, last_dirs))

        # If we have reached the end return
        if pos == end:
            return cur_dist

        # Check extending path by moving to neighbouring indices
        for dir in dirs:
            # Check we haven't moved max number of steps in this direction already
            if last_dirs == tuple(dir[2] for _ in range(max_row)):
                continue

            # don't backtrack
            if last_dirs[-1] == opdir[dir[2]]:
                continue

            # If changing direction move min number of spaces in new dir
            if last_dirs[-1] != dir[2]:
                steps = min_row
                # print(f"changing dir from {last_dirs[-1]} to {dir[2]}")
                dir2 = (min_row * dir[0], min_row * dir[1], min_row * [dir[2]])
            else:
                steps = 1
                dir2 = dir

            newpos = (pos[0] + dir2[0], pos[1] + dir2[1])

            # Check this point is in the grid and if so add to heap to process
            if 0 <= newpos[0] < len(mp[0]) and 0 <= newpos[1] < len(mp):
                new_dis = cur_dist
                intpos = pos
                for i in range(steps):
                    intpos = (intpos[0] + dir[0], intpos[1] + dir[1])
                    new_dis += map[intpos[1]][intpos[0]]
                    # print(last_dirs[-max_row+1:] + tuple(dir[2],))
                    if new_dis < dis[intpos[1]][intpos[0]]:
                        dis[intpos[1]][intpos[0]] = new_dis

                heapq.heappush(
                    queue,
                    (
                        new_dis,
                        newpos,
                        last_dirs[-max_row + 1 :]
                        + tuple(
                            dir2[2],
                        ),
                    ),
                )

        # Monitor progress
        i += 1
        if i % 5000 == 0:
            print(i, pos, cur_dist)

    return 0, [(0, 0)], ["."]


def plot_path(points, path, mp):
    """
    Plot a path on the map and display in terminal.
    """
    for i, pnt in enumerate(points):
        mp[pnt[1]][pnt[0]] = path[i]
    print(np.asarray(mp))


if __name__ == "__main__":
    # Get inputs
    map, dists, paths, pathdirs = process_input(read_file("data/day17.dat"))
    # map, dists, paths, pathdirs = process_input(read_file("data/day17.test"))

    # Part 1
    dist_1 = a_star_path(
        (0, 0), ((len(map[0])) - 1, len(map) - 1), map, dists, paths, pathdirs
    )

    # print(np.asarray(map))
    # print(np.asarray(dists))
    # print(paths)
    # print(pathdirs)
    # plot_path(path_1, dirs_1, map.copy())

    print(f"Part one answer is {dist_1}")

    # Get inputs
    map, dists, paths, pathdirs = process_input(read_file("data/day17.dat"))
    # map, dists, paths, pathdirs = process_input(read_file("data/day17.test"))
    # map, dists, paths, pathdirs = process_input(read_file("data/day17.test_2"))

    # Part 2
    dist_2 = a_star_path(
        (0, 0), ((len(map[0])) - 1, len(map) - 1), map, dists, paths, pathdirs, p2=True
    )

    # print(np.asarray(map))
    # print(np.asarray(dists))
    # print(paths)
    # print(pathdirs)
    # plot_path(path_2, dirs_2, map.copy())

    print(f"Part two answer is {dist_2}")
