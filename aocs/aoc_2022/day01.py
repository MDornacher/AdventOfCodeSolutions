from aocd.models import Puzzle


DAY = 1
YEAR = 2022


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def split_input(puzzle_input):
    # split string first at `\n\n` than at `\n` and return a list of lists and cast each element to int
    return [
        [int(element) for element in inventory.split("\n")]
        for inventory in puzzle_input.split("\n\n")
    ]


def sum_each_inventory(inventories):
    return [sum(inventory) for inventory in inventories]


def solve_a(puzzle_input):
    inventories = split_input(puzzle_input)
    inventories_summary = sum_each_inventory(inventories)
    assert len(inventories) == len(inventories_summary)
    return max(inventories_summary)


def solve_b(puzzle_input):
    # do the same as in solve_a but return the sum of the top 3 inventories
    inventories = split_input(puzzle_input)
    inventories_summary = sum_each_inventory(inventories)
    assert len(inventories) == len(inventories_summary)
    return sum(sorted(inventories_summary, reverse=True)[:3])


if __name__ == "__main__":
    main()
