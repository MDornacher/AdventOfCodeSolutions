from aocd.models import Puzzle
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter


DAY = 9
YEAR = 2021

FOOTPRINT = np.array([[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]])


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(puzzle_input):
    return np.array([list(line) for line in puzzle_input.splitlines()]).astype(int)


def filter_function(values):
    return np.all(values[2] < values[[0, 1, 3, 4]])


def find_minima_mask(heat_map):
    minima = ndimage.generic_filter(heat_map, filter_function, footprint=FOOTPRINT, mode="constant", cval=10)
    minima_mask = minima == 1
    return minima_mask


def solve_a(puzzle_input):
    heat_map = parse_input(puzzle_input)
    minima_mask = find_minima_mask(heat_map)
    return (heat_map[minima_mask] + 1).sum()


def find_most_common_basins(heat_map):
    heat_map[heat_map < 9] = 1
    heat_map[heat_map == 9] = 0
    labeled_array, num_features = ndimage.measurements.label(heat_map)
    return Counter(labeled_array.flatten()).most_common()[1:]


def solve_b(puzzle_input):
    heat_map = parse_input(puzzle_input)
    most_common_basins = find_most_common_basins(heat_map)
    return most_common_basins[0][1] * most_common_basins[1][1] * most_common_basins[2][1]


if __name__ == "__main__":
    main()






