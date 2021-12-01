import numpy as np
from aocd.models import Puzzle

DAY = 1
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def solve_a(puzzle_input):
    report = np.array(puzzle_input.splitlines()).astype(int)
    gradients = np.diff(report)
    return len(gradients[gradients > 0])


def solve_b(puzzle_input):
    report = np.array(puzzle_input.splitlines()).astype(int)
    groups = np.convolve(report, np.ones(3), "valid")
    gradients = np.diff(groups)
    return len(gradients[gradients > 0])


if __name__ == "__main__":
    main()
