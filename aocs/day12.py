from aocd.models import Puzzle


DAY = 12
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_connections(puzzle_input):
    connections = {}
    for line in puzzle_input.splitlines():
        start, end = line.split("-")
        if start not in connections:
            connections[start] = []
        connections[start].append(end)
        if end not in connections:
            connections[end] = []
        connections[end].append(start)
    return connections


def find_paths_a(position, visited, connections):
    if position == "end":
        return 1
    # stop if small cave has been visited before
    if position.islower() and position in visited:
        return 0
    # create copy of visited set
    visited_updated = visited | {position}
    path_options = 0
    for next_position in connections[position]:
        path_options += find_paths_a(next_position, visited_updated, connections)
    return path_options


def solve_a(puzzle_input):
    connections = parse_connections(puzzle_input)
    return find_paths_a("start", set(), connections)


def find_paths_b(position, visited, double_visit, connections):
    if position == "end":
        return 1
    if position == "start" and visited:
        return 0
    # check if small cave has been visited before
    if position.islower() and position in visited:
        # continue run if no small cave has been visited twice yet
        if double_visit is None:
            double_visit = position
        # stop run after second double visit
        else:
            return 0
    # create copy of visited set
    visited_updated = visited | {position}
    path_options = 0
    for next_position in connections[position]:
        path_options += find_paths_b(
            next_position, visited_updated, double_visit, connections
        )
    return path_options


def solve_b(puzzle_input):
    connections = parse_connections(puzzle_input)
    return find_paths_b("start", set(), None, connections)


if __name__ == "__main__":
    main()
