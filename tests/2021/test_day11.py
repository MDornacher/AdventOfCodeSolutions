from aocs.aoc_2021.day11 import main, solve_a, solve_b

TEST_INPUT = "5483143223\n"\
             "2745854711\n"\
             "5264556173\n"\
             "6141336146\n"\
             "6357385478\n"\
             "4167524645\n"\
             "2176841721\n"\
             "6882881134\n"\
             "4846848554\n"\
             "5283751526"


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 1656


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 195


def test_main():
    main()
