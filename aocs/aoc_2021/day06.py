from collections import Counter

from aocd.models import Puzzle


DAY = 6
YEAR = 2021

LIFE_CYCLE = 6
BIRTH_OFFSET = 2


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def initialize_population(puzzle_input):
    population = {i: 0 for i in range(8, -1, -1)}
    population.update(Counter(puzzle_input))
    return population


def update_population(population):
    new_population = {k - 1: v for k, v in population.items()}
    offspring = new_population.pop(-1)
    new_population[LIFE_CYCLE] += offspring
    new_population[LIFE_CYCLE + BIRTH_OFFSET] = offspring
    return new_population


def simulate_population(population, days):
    for i in range(days):
        population = update_population(population)
    return population


def solve_a(puzzle_input):
    population = initialize_population(puzzle_input)
    population = simulate_population(population, days=80)
    return sum(population.values())


def solve_b(puzzle_input):
    population = initialize_population(puzzle_input)
    population = simulate_population(population, days=256)
    return sum(population.values())


if __name__ == "__main__":
    main()
