from aocd.models import Puzzle
import numpy as np
from matplotlib import pyplot as plt


DAY = 10
YEAR = 2022

START_VALUE = 1
DISPLAY_WIDTH = 40
DISPLAY_HEIGHT = 6
SPRITE_WIDTH = 3


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(puzzle_input):
    return puzzle_input.splitlines()


def read_operations(instructions):
    operations = []
    for instruction in instructions:
        # split instuction
        # for ["noop"], append 0
        # for ["addx", value], append int(value)
        match instruction.split():
            case ["noop"]:
                operations.append(0)
            case ["addx", value]:
                # include extra cycle for addx
                operations.append(0)
                operations.append(int(value))
    return operations


def execute_operations(operations, stop_at: int) -> int:
    value = START_VALUE
    for operation in operations[:stop_at]:
        value += operation
    return value


def solve_a(puzzle_input):
    instructions = parse_input(puzzle_input)
    operations = read_operations(instructions)
    # during the 20th cycle and every 40 cycles after that
    # (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).
    # cycle name is 1-based, list of operations is 0-based
    # so we need to check for 19, 59, 99, 139, 179, 219
    signals = []
    for cycle in range(19, 220, 40):
        value = execute_operations(operations, cycle)
        # calculate signal strength by multiplying value with cycle (remember, 1-based)
        signal_strength = value * (cycle + 1)
        # append signal strength to signals
        signals.append(signal_strength)
        # print cycle, value and signal strength
        print(f"Cycle {cycle + 1}: {value} -> {signal_strength}")
    # return sum of all signals
    return sum(signals)


def draw_display(operations):
    display = np.zeros((DISPLAY_HEIGHT, DISPLAY_WIDTH), dtype=bool)
    # sprite is int range from 0 to SPRITE_WIDTH
    sprite = np.arange(SPRITE_WIDTH)
    for pixel, operation in enumerate(operations):
        # check if pixel is in sprite in any row
        # if so, set display pixel to True
        if any(pixel - (i * DISPLAY_WIDTH) in sprite for i in range(DISPLAY_HEIGHT)):
            row = pixel // DISPLAY_WIDTH
            col = pixel % DISPLAY_WIDTH
            display[row, col] = True
        # move sprite by operation
        sprite += operation
        print(sprite)
    # plot display with matplotlib
    # save output to file
    plt.imshow(display, cmap="gray")
    plt.savefig("display.png")


def solve_b(puzzle_input):
    instructions = parse_input(puzzle_input)
    operations = read_operations(instructions)
    draw_display(operations)
    # puzzle is solved by drawing the display
    # so no need to return anything


if __name__ == "__main__":
    main()
