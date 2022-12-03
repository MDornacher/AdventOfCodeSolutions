from aocd.models import Puzzle

DAY = 3
YEAR = 2022

LOWER_LETTER_TO_NUMBER = {chr(i): i - 96 for i in range(97, 123)}
UPPER_LETTER_TO_NUMBER = {chr(i): (i - 64) + 26 for i in range(65, 91)}
LETTER_TO_NUMBER = {**LOWER_LETTER_TO_NUMBER, **UPPER_LETTER_TO_NUMBER}


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def read_backpacks(puzzle_input: str) -> list[list[str]]:
    return [list(inventory) for inventory in puzzle_input.splitlines()]


def split_backpack(backpack: str) -> tuple[set, set]:
    return set(backpack[: len(backpack) // 2]), set(backpack[len(backpack) // 2 :])


def overlap_between_backpack_compartments(backpack: tuple[set, set]):
    return backpack[0].intersection(backpack[1])


def score_overlap(overlap: set[str]):
    return sum(LETTER_TO_NUMBER[letter] for letter in overlap)


def solve_a(puzzle_input):
    backpacks = read_backpacks(puzzle_input)
    return sum(
        score_overlap(overlap_between_backpack_compartments(split_backpack(backpack)))
        for backpack in backpacks
    )


def group_backpacks(backpacks: list[str], group_size: int = 3) -> list[list[str]]:
    return [backpacks[i : i + group_size] for i in range(0, len(backpacks), group_size)]


def overlap_between_group_of_backpacks(backpack_group: list[list[str]]) -> set[str]:
    """Return the itmes which are in all backpacks in the group without splitting the compartments"""
    print(backpack_group)
    return set.intersection(*[set(backpack) for backpack in backpack_group])


def solve_b(puzzle_input):
    backpacks = read_backpacks(puzzle_input)
    # return the sum of the scores of the overlap between the backpacks with group size 3
    return sum(
        score_overlap(overlap_between_group_of_backpacks(group))
        for group in group_backpacks(backpacks, 3)
    )


if __name__ == "__main__":
    main()
