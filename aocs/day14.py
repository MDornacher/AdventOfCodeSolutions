from aocd.models import Puzzle
from collections import Counter
import numpy as np


DAY = 14
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(puzzle_input):
    polymer_mapping = {}
    polymers_seed, _, *lines = puzzle_input.splitlines()

    for line in lines:
        polymer_pair, product = line.split(" -> ")
        polymer_mapping[polymer_pair] = product

    polymers = reset_polymers(polymer_mapping)
    for pair in zip(polymers_seed[:-1], polymers_seed[1:]):
        polymers["".join(pair)] += 1

    return polymers, polymer_mapping, polymers_seed


def reset_polymers(polymer_mapping):
    return {k: 0 for k in polymer_mapping.keys()}


def initialize_letters(polymer_mapping, polymers_seed):
    letters = {c: 0 for c in set(list("".join(polymer_mapping.keys())))}
    for letter in polymers_seed:
        letters[letter] += 1
    return letters


def simulate_polymerization(polymers, polymer_mapping, letters, rounds):
    for _ in range(rounds):
        new_polymers = reset_polymers(polymer_mapping)
        for pair, count in polymers.items():
            if not count:
                continue
            pair_start, pair_end = pair
            insert = polymer_mapping[pair]
            new_polymers[pair_start + insert] += count
            new_polymers[insert + pair_end] += count
            letters[insert] += count
        polymers = new_polymers.copy()
    return polymers, letters


def calculate_result(letters):
    sorted_letters = Counter(letters).most_common()
    return sorted_letters[0][1] - sorted_letters[-1][1]


def solve_a(puzzle_input):
    polymers, polymer_mapping, polymers_seed = parse_input(puzzle_input)
    letters = initialize_letters(polymer_mapping, polymers_seed)
    _, letters = simulate_polymerization(polymers, polymer_mapping, letters, 10)
    return calculate_result(letters)


def solve_b(puzzle_input):
    polymers, polymer_mapping, polymers_seed = parse_input(puzzle_input)
    letters = initialize_letters(polymer_mapping, polymers_seed)
    _, letters = simulate_polymerization(polymers, polymer_mapping, letters, 40)
    return calculate_result(letters)


if __name__ == "__main__":
    main()
