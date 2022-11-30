from aocd.models import Puzzle
import numpy as np
from matplotlib import pyplot as plt


DAY = 13
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    solve_b(puzzle.input_data)
    puzzle.answer_b = "JGAJEFKU"


def parse_paper_and_instructions(puzzle_input):
    paper_dots_raw, instructions_raw = puzzle_input.split("\n\n")
    paper_dots = []
    for line in paper_dots_raw.splitlines():
        paper_dots.append(line.split(","))
    paper_dots = np.array(paper_dots).astype(int)

    paper = np.zeros(np.amax(paper_dots, axis=0) + 1)
    for x, y in paper_dots:
        paper[x, y] = 1

    instructions = [
        s
        for line in instructions_raw.splitlines()
        for s in line.split()
        if "x" in s or "y" in s
    ]
    return paper.T, instructions


def add_unmatched_arrays(first_array, second_array, mode):
    if mode is "bottom":
        padding = len(first_array) - len(second_array)
        if padding > 0:
            second_array = np.pad(
                second_array, ((padding, 0), (0, 0)), mode="constant", constant_values=0
            ).astype(int)
        else:
            first_array = np.pad(
                first_array,
                ((int(padding), 0), (0, 0)),
                mode="constant",
                constant_values=0,
            ).astype(int)
    else:
        raise ValueError("Not implemented, only supports mode=bottom")
    return first_array + second_array


def fold_paper(paper, instruction):
    fold_line = int(instruction[2:])
    if "x" in instruction:
        paper = paper.T

    paper_top = paper[:fold_line]
    paper_bottom = np.flipud(paper[fold_line + 1 :])
    paper_folded = add_unmatched_arrays(paper_top, paper_bottom, mode="bottom")

    if "x" in instruction:
        paper_folded = paper_folded.T
    paper_folded[paper_folded > 1] = 1

    return paper_folded.astype(int)


def solve_a(puzzle_input):
    paper, instructions = parse_paper_and_instructions(puzzle_input)
    paper_folded = fold_paper(paper, instructions[0])
    return paper_folded.sum()


def solve_b(puzzle_input):
    paper, instructions = parse_paper_and_instructions(puzzle_input)
    for instruction in instructions:
        paper = fold_paper(paper, instruction)
    plt.imshow(paper, cmap="binary")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    return paper


if __name__ == "__main__":
    main()
