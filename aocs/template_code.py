from aocd.models import Puzzle


DAY = 0
YEAR = 2021


def solve_a(puzzle_input):
    return puzzle_input


def solve_b(puzzle_input):
    return puzzle_input


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)
