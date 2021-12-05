from aocd.models import Puzzle
import numpy as np


DAY = 5
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_vents(puzzle_input):
    return np.array([pair.split(",") for line in puzzle_input.splitlines()
                     for pair in line.split(" -> ")]).astype(int).reshape((-1, 2, 2))


def create_field(vents):
    field_size = vents.reshape(-1, 2).max() + 1
    return np.zeros((field_size, field_size))


def mark_vent(field, vent, diagonal=False):
    vent_start, vent_end = vent
    start_x, start_y = vent_start
    end_x, end_y = vent_end

    # check if horizontal line
    if start_y == end_y:
        if start_x > end_x:
            start_x, end_x = end_x, start_x
        field[start_y, :][start_x:end_x+1] += 1
        return field

    # check if vertical line
    if start_x == end_x:
        if start_y > end_y:
            start_y, end_y = end_y, start_y
        field[:, start_x][start_y:end_y+1] += 1
        return field

    if not diagonal:
        return field

    for i_y, i_x in zip(
            np.linspace(start_x, end_x, abs(end_x - start_x) + 1).astype(int),
            np.linspace(start_y, end_y, abs(end_x - start_x) + 1).astype(int)):
        field[i_x, i_y] += 1
    return field


def solve_a(puzzle_input):
    vents = parse_vents(puzzle_input)
    field = create_field(vents)
    for vent in vents:
        field = mark_vent(field, vent, diagonal=False)
    return len(field[field > 1])


def solve_b(puzzle_input):
    vents = parse_vents(puzzle_input)
    field = create_field(vents)
    for vent in vents:
        field = mark_vent(field, vent, diagonal=True)
    return len(field[field > 1])


if __name__ == "__main__":
    main()
