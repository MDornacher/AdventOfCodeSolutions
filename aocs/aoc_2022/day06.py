from aocd.models import Puzzle


DAY = 6
YEAR = 2022


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def solve_a(puzzle_input):
    """
    Example puzzle input: "bvwbjplbgvbhsrlpgdmjqwftvncz"
    Return position of first character after sliding window of 4 characters hits 4 unique characters
    """
    for part in range(len(puzzle_input) - 3):
        if len(set(puzzle_input[part : part + 4])) == 4:
            return part + 4


def solve_b(puzzle_input):
    """
    Same as solve_a, but with sliding window of 14 characters
    """
    for part in range(len(puzzle_input) - 13):
        if len(set(puzzle_input[part : part + 14])) == 14:
            return part + 14


if __name__ == "__main__":
    main()
