from aocd.models import Puzzle
import numpy as np


DAY = 8
YEAR = 2021

TRANSLATION = {
    "012456": 0,
    "25": 1,
    "02346": 2,
    "02356": 3,
    "1235": 4,
    "01356": 5,
    "013456": 6,
    "025": 7,
    "0123456": 8,
    "012356": 9,
}

DIGIT_TO_NUMBER = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
}


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_values(puzzle_input):
    return np.array(puzzle_input.splitlines())


def split_values(values):
    input_left, input_right = np.array([line.split("|") for line in values]).T
    input_left = np.array([s.split() for s in input_left])
    input_right = np.array([s.split() for s in input_right])
    return input_left, input_right


def find_digit_lengths(values):
    alen = np.vectorize(len)
    return alen(values)


def solve_a(puzzle_input):
    values = parse_values(puzzle_input)
    input_left, input_right = split_values(values)
    input_lengths = find_digit_lengths(input_right)
    return (
        input_lengths[input_lengths == 2].size
        + input_lengths[input_lengths == 3].size
        + input_lengths[input_lengths == 4].size
        + input_lengths[input_lengths == 7].size
    )


def decode_calibration(calibration_pattern):
    calibration_sets = [set(p) for p in calibration_pattern]

    # identifiable sets
    set_1 = [p for p in calibration_sets if len(p) == 2][0]
    set_4 = [p for p in calibration_sets if len(p) == 4][0]
    set_7 = [p for p in calibration_sets if len(p) == 3][0]
    set_8 = [p for p in calibration_sets if len(p) == 7][0]

    # unknown subsets
    group_235 = [p for p in calibration_sets if len(p) == 5]
    group_069 = [p for p in calibration_sets if len(p) == 6]

    # resolve sets
    set_2 = [p for p in group_235 if len(p - set_4 - set_7) == 2][0]
    set_3 = [p for p in group_235 if len(p - set_2) == 1][0]
    set_5 = [p for p in group_235 if len(p - set_2) == 2][0]

    set_9 = [p for p in group_069 if len(p - set_4 - set_7) == 1][0]
    set_6 = [p for p in group_069 if len(p - set_1) == len(p) - 1][0]
    set_0 = [p for p in group_069 if p != set_9 and p != set_6][0]

    mapper = {
        "".join(sorted(set_0)): "0",
        "".join(sorted(set_1)): "1",
        "".join(sorted(set_2)): "2",
        "".join(sorted(set_3)): "3",
        "".join(sorted(set_4)): "4",
        "".join(sorted(set_5)): "5",
        "".join(sorted(set_6)): "6",
        "".join(sorted(set_7)): "7",
        "".join(sorted(set_8)): "8",
        "".join(sorted(set_9)): "9",
    }
    return mapper


def apply_decoder(mapper, output):
    return int("".join([mapper["".join(sorted(s))] for s in output]))


def solve_b(puzzle_input):
    values = parse_values(puzzle_input)
    input_left, input_right = split_values(values)
    output_sum = 0
    for left, right in zip(input_left, input_right):
        mapper = decode_calibration(left)
        output_sum += apply_decoder(mapper, right)
    return output_sum


if __name__ == "__main__":
    main()
