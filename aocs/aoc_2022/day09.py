from aocd.models import Puzzle
from enum import Enum


DAY = 9
YEAR = 2022

# Enum for direction
class Direction(Enum):
    U = 0 + 1j
    D = 0 - 1j
    L = -1 + 0j
    R = 1 + 0j


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(puzzle_input) -> list[tuple[str, int]]:
    """
    Example input:
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2
    Return a list of tuples, e.g. [(R, 4), (U, 4), (L, 3), ...]
    """
    return [(line[0], int(line[1:])) for line in puzzle_input.splitlines()]


class Rope:
    def __init__(self, number_of_knots=10) -> None:
        # Initiate head and tail positon of rope
        # using imaginary numbers for x and y
        initial_postion = 0 + 0j
        self.knots = {i: initial_postion for i in range(number_of_knots)}
        self.tail_history = [self.tail]

    @property
    def head(self):
        return self.knots[0]

    @property
    def tail(self):
        return self.knots[len(self.knots) - 1]

    def distance(self, leading_knot, trailing_knot):
        return abs(leading_knot - trailing_knot)

    def need_to_move(self, distance):
        # Return True if distance is greater than square root of 2
        return distance > (2**0.5)

    @property
    def visited_tail_positions(self) -> set:
        # Return a set of all positions
        # the tail has been to
        return set(self.tail_history)

    def move_head(self, direction: Direction, amount: int):
        for _ in range(amount):
            self.knots[0] += direction.value
            for knot_number in range(1, len(self.knots)):
                leading_knot = self.knots[knot_number - 1]
                trailing_knot = self.knots[knot_number]
                if self.need_to_move(self.distance(leading_knot, trailing_knot)):
                    self.move_knot(knot_number)
            # update tail history
            self.tail_history.append(self.tail)

    def move_knot(self, knot_number):
        # Move tail towards head
        # one step at a time
        # add new tail position to tail_history
        leading_knot = self.knots[knot_number - 1]
        trailing_knot = self.knots[knot_number]

        # if leading knot is directly to the right of trailing knot
        # move trailing knot to the right
        if (
            leading_knot.real > trailing_knot.real
            and leading_knot.imag == trailing_knot.imag
        ):
            self.knots[knot_number] += 1 + 0j
        # if leading knot is directly to the left of trailing knot
        # move trailing knot to the left
        elif (
            leading_knot.real < trailing_knot.real
            and leading_knot.imag == trailing_knot.imag
        ):
            self.knots[knot_number] += -1 + 0j
        # if leading knot is directly above trailing knot
        # move trailing knot up
        elif (
            leading_knot.real == trailing_knot.real
            and leading_knot.imag > trailing_knot.imag
        ):
            self.knots[knot_number] += 0 + 1j
        # if leading knot is directly below trailing knot
        # move trailing knot down
        elif (
            leading_knot.real == trailing_knot.real
            and leading_knot.imag < trailing_knot.imag
        ):
            self.knots[knot_number] += 0 - 1j
        # if leading knot is diagonally
        else:
            # if leading knot is to the right and above trailing knot
            # move trailing knot to the right and up
            if (
                leading_knot.real > trailing_knot.real
                and leading_knot.imag > trailing_knot.imag
            ):
                self.knots[knot_number] += 1 + 1j
            # if leading knot is to the right and below trailing knot
            # move trailing knot to the right and down
            elif (
                leading_knot.real > trailing_knot.real
                and leading_knot.imag < trailing_knot.imag
            ):
                self.knots[knot_number] += 1 - 1j
            # if leading knot is to the left and above trailing knot
            # move trailing knot to the left and up
            elif (
                leading_knot.real < trailing_knot.real
                and leading_knot.imag > trailing_knot.imag
            ):
                self.knots[knot_number] += -1 + 1j
            # if leading knot is to the left and below trailing knot
            # move trailing knot to the left and down
            elif (
                leading_knot.real < trailing_knot.real
                and leading_knot.imag < trailing_knot.imag
            ):
                self.knots[knot_number] += -1 - 1j


def solve_a(puzzle_input):
    rope = Rope(number_of_knots=2)
    for direction, amount in parse_input(puzzle_input):
        rope.move_head(Direction[direction], amount)
    return len(rope.visited_tail_positions)


def solve_b(puzzle_input):
    """Same as solve_a but with a rope of 10 knots instead of 2"""
    rope = Rope(number_of_knots=10)
    for direction, amount in parse_input(puzzle_input):
        rope.move_head(Direction[direction], amount)
    return len(rope.visited_tail_positions)


if __name__ == "__main__":
    main()
