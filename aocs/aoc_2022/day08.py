"""
Example puzzle input:
30373
25512
65332
33549
35390
"""

from aocd.models import Puzzle
import numpy as np


DAY = 8
YEAR = 2022


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_tree_map(puzzle_input: str) -> np.ndarray:
    """
    Example puzzle input:
    30373
    25512
    65332
    33549
    35390
    """
    # split each single digit and cast to int
    return np.array([list(line) for line in puzzle_input.splitlines()]).astype(int)


def map_visible_trees(tree_map: np.ndarray) -> np.ndarray:
    """
    A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
    Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
    """
    # make visibility check for each orientation of tree map
    los_left = visibilty_check(tree_map)
    # rotate tree map 90 degrees in clockwise direction
    los_bottom = np.rot90(visibilty_check(np.rot90(tree_map, k=1)), k=3)
    # rotate tree map 180 degrees
    los_right = np.rot90(visibilty_check(np.rot90(tree_map, k=2)), k=2)
    # rotate tree map 270 degrees
    los_top = np.rot90(visibilty_check(np.rot90(tree_map, k=3)), k=1)

    # overlap all los results
    return los_left + los_right + los_top + los_bottom


def visibilty_check(tree_map: np.ndarray) -> np.ndarray:
    """
    Check how many trees are visible from the edge of the grid.
    Return a boolean array with the same shape as the tree map.
    Mark visible trees with True, the rest with False.
    """
    visible = np.zeros_like(tree_map, dtype=bool)
    for i, row in enumerate(tree_map):
        tallest_tree_so_far = -1
        for j, tree in enumerate(row):
            # check if tree is visible
            if tree > tallest_tree_so_far:
                visible[i, j] = True
                tallest_tree_so_far = tree
    return visible


def solve_a(puzzle_input):
    tree_map = parse_tree_map(puzzle_input)
    visible_trees = map_visible_trees(tree_map)
    return np.sum(visible_trees)


def tree_visibility_score(tree_map: np.ndarray, position: tuple[int, int]) -> int:
    """
    Check how many trees are visible from a given position.
    Return distance of visibility in each direction.
    The distance is the number of trees between the given position and the tree of the same height or the edge of the grid.
    """
    i, j = position
    # slice each direction
    slice_right = tree_map[i, j:]
    slice_bottom = tree_map[i:, j]
    slice_left = tree_map[i, : j + 1][::-1]
    slice_top = tree_map[: i + 1, j][::-1]
    # find visibility distance for each direction
    visibility_right = find_visibility_distance(slice_right)
    visibility_bottom = find_visibility_distance(slice_bottom)
    visibility_left = find_visibility_distance(slice_left)
    visibility_top = find_visibility_distance(slice_top)
    # return the product of all visibility distances
    return visibility_right * visibility_bottom * visibility_left * visibility_top


def find_visibility_distance(tree_slice: np.ndarray) -> int:
    """
    Find the distance to the next tree of the same height.
    """
    tree_height = tree_slice[0]
    distance = 0
    for tree in tree_slice[1:]:
        distance += 1
        if tree >= tree_height:
            break
    return distance


def solve_b(puzzle_input):
    tree_map = parse_tree_map(puzzle_input)
    # create empty score map with the same shape as the tree map
    visibility_score = np.zeros_like(tree_map)
    # loop over all positions, check visibility score and return the maximum
    for i, row in enumerate(tree_map):
        if i == 0 or i == tree_map.shape[0] - 1:
            continue
        for j, _ in enumerate(row):
            if j == 0 or j == tree_map.shape[1] - 1:
                continue
            visibility_score[i, j] = tree_visibility_score(tree_map, (i, j))
    return np.max(visibility_score)


if __name__ == "__main__":
    main()
