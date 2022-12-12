"""
Search Puzzle
"""

import time

import numpy as np
from aocd.models import Puzzle
from matplotlib import pyplot as plt

DAY = 12
YEAR = 2022

Position = tuple[int, int]


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(
    puzzle_input: str, verbose: bool = False
) -> tuple[Position, Position, np.ndarray]:
    """
    Example:
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi

    Convert letters to numbers, with a=0, b=1, c=2, etc.
    'S' marks the start, 'E' marks the goal.
    The starting position 'S' has elevation 'a', and the goal 'E' has elevation 'z'.
    Return numpy int array of height map and indices of start and goal.
    """
    # first parse input as string array
    height_map = np.array([list(line.strip()) for line in puzzle_input.splitlines()])
    # find start and goal
    start = np.argwhere(height_map == "S")[0]
    goal = np.argwhere(height_map == "E")[0]
    # replace start and goal with 'a' and 'z'
    height_map[start[0], start[1]] = "a"
    height_map[goal[0], goal[1]] = "z"
    # convert letters to numbers
    height_map = np.vectorize(lambda x: ord(x) - ord("a"))(height_map)
    if verbose:
        print("Start:", start)
        print("Goal:", goal)
        print("Size:", height_map.shape)
        print("Height map:")
        print(height_map)
    # convert start and goal to tuples
    start = tuple(start.tolist())
    goal = tuple(goal.tolist())
    return start, goal, height_map


def get_neighbors(current: Position, height_map: np.ndarray) -> list[Position]:
    """
    During each step, you can move exactly one square up, down, left, or right.
    You cannot move diagonally.
    You can only move to a square with a height that is at most 1 higher than your current height.
    """
    neighbors = []
    # get all possible neighbors
    # this includes neighbors outside of the height map
    # these neighbors are filtered out later
    for i in range(-1, 2):
        for j in range(-1, 2):
            # skip if current position
            if i == 0 and j == 0:
                continue
            # skip if diagonal
            if abs(i) == abs(j):
                continue
            # add neighbor to list
            neighbors.append(current + np.array([i, j]))
    # turn list of numpy arrays into list of tuples
    neighbors = [tuple(neighbor.tolist()) for neighbor in neighbors]
    # filter out neighbors with invalid indices
    neighbors = [
        neighbor
        for neighbor in neighbors
        if 0 <= neighbor[0] < height_map.shape[0]  # check row index
        and 0 <= neighbor[1] < height_map.shape[1]  # check column index
    ]
    # filter out neighbors with invalid height
    neighbors = [
        neighbor
        for neighbor in neighbors
        if height_map[neighbor] - height_map[current] <= 1
    ]
    return neighbors


def plot_path(
    name, height_map: np.ndarray, path: list, start: Position, goal: Position
):
    # provide some plot maze and path
    plt.imshow(height_map, cmap="gray")
    # plot start and goal as red and green dots
    plt.plot(start[1], start[0], "ro")
    plt.plot(goal[1], goal[0], "go")
    # plot path as blue line
    plt.plot([p[1] for p in path], [p[0] for p in path], "b-")
    # save plot as {name}.png
    plt.savefig(f"{name}.png")
    # close plot
    plt.close()


def path_throguh_map(
    start: Position,
    goal: Position,
    height_map: np.ndarray,
    visualize: bool = False,
) -> tuple[int, list]:
    """
    Return the shortest path from start to goal through the height map.
    Use BFS to find the shortest path.
    """
    # initialize queue
    queue = [(start, 0, [start])]
    # keep track of visited nodes
    visited = set()
    # give some progress information
    print("Start search...")
    while queue:
        # pop first element from queue
        # current: current position
        # distance: distance from start to current
        # path: list of positions from start to current
        # pop(0) is used instead of pop() to implement breadth-first search
        current, distance, path = queue.pop(0)
        # give some progress information about current distance
        # and overwrite previous line
        print(f"Distance: {distance}", end="\r")

        # check if goal is reached
        # if so, return distance and path
        # otherwise, add neighbors to queue
        if current == goal:
            if visualize:
                plot_path("success", height_map, path, start, goal)
            return distance, path

        # add neighbors to queue
        # neighbors are added to queue in order of increasing distance from start
        # this is done by appending to the end of the queue
        for neighbor in get_neighbors(current, height_map):
            # skip if already visited
            if neighbor in visited:
                continue

            # mark as visited
            visited.add(neighbor)

            # add to queue
            # distance is increased by 1
            # path is extended by neighbor
            queue.append((neighbor, distance + 1, path + [neighbor]))

    # plot_path("debug", height_map, path, start, goal)
    # if no path is found, raise ValueError
    # provide distance and neighbors of last visited node
    # check if neighbors have been visited
    debug_message = f"No path found from {start} to {goal} through height map:\n"
    debug_message += f"Largest distance: {distance}\n"
    debug_message += (
        f"Neighbors of last visited node: {get_neighbors(current, height_map)}\n"
    )
    debug_message += f"Have neighbors been visited?\n"
    for neighbor in get_neighbors(current, height_map):
        debug_message += f"{neighbor}: {neighbor in visited}\n"
    debug_message += f"See debug.png for plot of height map and path."
    raise ValueError(debug_message)


example_input = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi\
"""


def solve_a(puzzle_input):
    start, goal, height_map = parse_input(puzzle_input, verbose=True)
    distance, path = path_throguh_map(start, goal, height_map, visualize=True)
    print("Shortest path:")
    print(path)
    print("Distance:", distance)
    return distance


def solve_b(puzzle_input):
    """
    Do reverse search from goal to new starting point.
    Candidates for new starting point are all positions with height 0.
    Return the minimum distance.
    """
    start, goal, height_map = parse_input(puzzle_input)
    # find all positions with height 0
    # these are the candidates for new starting points
    candidates = np.argwhere(height_map == 0)
    # convert candidates to list of tuples
    candidates = [tuple(candidate.tolist()) for candidate in candidates]
    # save winning candidate
    winning_candidate = None
    # keep track of minimum distance
    min_distance = np.inf
    # keep track of path with minimum distance
    min_distance_path = None
    # give some progress information
    # time how long it takes to find the shortest path
    start_time = time.time()
    print("Start search...")
    for i, candidate in enumerate(candidates):
        # give some progress information
        # overwrite previous line
        print(
            f"Progress: {i + 1}/{len(candidates)} ({(i + 1) / len(candidates) * 100:.2f}%)"
        )
        # find path from candidate to goal
        # keep going if path is not found
        try:
            distance, path = path_throguh_map(candidate, goal, height_map)
        except ValueError:
            continue
        # check if distance is smaller than minimum distance
        if distance < min_distance:
            # update minimum distance
            min_distance = distance
            # update path with minimum distance
            min_distance_path = path
            # update winning candidate
            winning_candidate = candidate
    # give some progress information and how long it took
    print(f"Done in {time.time() - start_time:.2f} seconds.")
    # plot path
    plot_path("success", height_map, min_distance_path, winning_candidate, goal)
    # return maximum distance
    return min_distance


if __name__ == "__main__":
    main()
