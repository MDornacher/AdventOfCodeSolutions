import numpy as np
from aocd.models import Puzzle


DAY = 7
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def create_fuel_template(mode, width):
    if mode == "linear":
        return abs(np.arange(-width, width+1, 1))
    if mode == "triangle":
        return np.array([sum(range(abs(i)+1)) for i in range(-width, width+1)])
    raise ValueError(f"Unknown mode {mode}")


def create_fuel_map(puzzle_input, mode):
    positions = np.array(puzzle_input.split(",")).astype(int)
    width = positions.max() + 1
    height = positions.size
    field = np.zeros((height, width))
    fuel_template = create_fuel_template(mode, width)
    for i, position in enumerate(positions):
        field[i] = fuel_template[width-position:2*width-position]
    return field


def solve_a(puzzle_input):
    fuel_map = create_fuel_map(puzzle_input, mode="linear")
    return fuel_map.sum(axis=0, dtype=int).min()


def solve_b(puzzle_input):
    fuel_map = create_fuel_map(puzzle_input, mode="triangle")
    return fuel_map.sum(axis=0, dtype=int).min()


if __name__ == "__main__":
    main()
