from aocd.models import Puzzle


DAY = 2
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


class Submarine:
    def __init__(self):
        self.position = 0
        self.depth = 0

    def follow_command(self, instruction):
        command, units = instruction.split()
        units = int(units)
        if command == "forward":
            self.position += units
        elif command == "down":
            self.depth += units
        elif command == "up":
            self.depth -= units


class ImprovedSubmarine:
    def __init__(self):
        self.aim = 0
        self.position = 0
        self.depth = 0

    def follow_command(self, instruction):
        command, units = instruction.split()
        units = int(units)
        if command == "forward":
            self.position += units
            self.depth += self.aim * units
        elif command == "down":
            self.aim += units
        elif command == "up":
            self.aim -= units


def solve_a(puzzle_input):
    submarine = Submarine()
    instructions = puzzle_input.splitlines()
    for instruction in instructions:
        submarine.follow_command(instruction)
    return submarine.position * submarine.depth


def solve_b(puzzle_input):
    submarine = ImprovedSubmarine()
    instructions = puzzle_input.splitlines()
    for instruction in instructions:
        submarine.follow_command(instruction)
    return submarine.position * submarine.depth


if __name__ == "__main__":
    main()
