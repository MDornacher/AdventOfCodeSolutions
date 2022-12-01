from aocs.aoc_2021.day06 import (initialize_population, main, solve_a, solve_b,
                                 update_population)

TEST_INPUT = [3, 4, 3, 1, 2]


def test_initialize_population_single():
    for i in range(6):
        population = initialize_population([i])
        assert population[i] == 1
        assert sum(population.values()) == 1


def test_initialize_population_example():
    population = initialize_population(TEST_INPUT)
    assert sum(population.values()) == 5


def test_update_population_single():
    population = initialize_population([8])
    for i in range(7, -1, -1):
        population = update_population(population)
        assert population[i] == 1
        assert sum(population.values()) == 1
    # restarting again with offspring
    population = update_population(population)
    assert population[6] == 1
    assert population[8] == 1
    assert sum(population.values()) == 2


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 5934


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 26984457539


def test_main():
    main()
