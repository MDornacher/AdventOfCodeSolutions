from aocd.models import Puzzle
import numpy as np
from collections import Counter


DAY = 3
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_report(raw_input):
    return np.array([list(row) for row in raw_input.splitlines()]).astype(int)


def binary_to_int(binary):
    return int("".join(binary.astype(str)), 2)


def calculate_gamma_rate(report):
    column_sum = report.sum(axis=0)
    threshold = len(report) / 2
    column_sum[column_sum < threshold] = 0
    column_sum[column_sum > threshold] = 1
    return binary_to_int(column_sum)


def calculate_epsilon_rate(report):
    column_sum = report.sum(axis=0)
    threshold = len(report) / 2
    column_sum[column_sum < threshold] = 1
    column_sum[column_sum > threshold] = 0
    return binary_to_int(column_sum)


def calculate_oxygen_rating(report):
    candidates = report.copy()
    for i in range(len(report[0])):
        new_candidates = []
        digits = candidates[:, i]
        most_common_picks = Counter(digits).most_common(2)
        if most_common_picks[0][1] == most_common_picks[1][1]:
            most_common = 1
        else:
            most_common = most_common_picks[0][0]

        for candidate in candidates:
            if candidate[i] == most_common:
                new_candidates.append(candidate)

        if len(new_candidates) == 1:
            return binary_to_int(new_candidates[0])
        candidates = np.array(new_candidates)


def calculate_carbon_rating(report):
    candidates = report.copy()
    for i in range(len(report[0])):
        new_candidates = []
        digits = candidates[:, i]
        most_common_picks = Counter(digits).most_common(2)
        if most_common_picks[0][1] == most_common_picks[1][1]:
            least_common = 0
        else:
            least_common = most_common_picks[1][0]

        for candidate in candidates:
            if candidate[i] == least_common:
                new_candidates.append(candidate)

        if len(new_candidates) == 1:
            return binary_to_int(new_candidates[0])
        candidates = np.array(new_candidates)


def solve_a(puzzle_input):
    report = parse_report(puzzle_input)
    gamma = calculate_gamma_rate(report)
    epsilon = calculate_epsilon_rate(report)
    return gamma * epsilon


def solve_b(puzzle_input):
    report = parse_report(puzzle_input)
    oxygen = calculate_oxygen_rating(report)
    carbon = calculate_carbon_rating(report)
    return oxygen * carbon


if __name__ == "__main__":
    main()
