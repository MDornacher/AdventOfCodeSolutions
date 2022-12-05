from aocd.models import Puzzle


DAY = 4
YEAR = 2022


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def read_sections(puzzle_input: str) -> list[tuple[tuple[str, str], ...]]:
    """
    Split "2-4,6-8\n2-3,4-5" into [((2, 4), (6, 8)), ((2, 3), (4, 5))]
    """
    for line in puzzle_input.splitlines():
        yield tuple(tuple(map(int, section.split("-"))) for section in line.split(","))


def section_to_set(section: tuple[int, int]) -> set[int]:
    return set(range(section[0], section[1] + 1))


def solve_a(puzzle_input):
    # how often is one section fully contained in another?
    fully_contained_sections = 0
    for section_a, section_b in read_sections(puzzle_input):
        set_a = section_to_set(section_a)
        set_b = section_to_set(section_b)
        if set_a.issubset(set_b) or set_b.issubset(set_a):
            fully_contained_sections += 1
    return fully_contained_sections


def solve_b(puzzle_input):
    # how often do the sections overlap?
    overlapping_sections = 0
    for section_a, section_b in read_sections(puzzle_input):
        set_a = section_to_set(section_a)
        set_b = section_to_set(section_b)
        if set_a.intersection(set_b):
            overlapping_sections += 1
    return overlapping_sections


if __name__ == "__main__":
    main()
