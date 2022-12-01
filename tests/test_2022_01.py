from aocs.aoc_2022.day01 import solve_a, solve_b, main, split_input, sum_each_inventory


TEST_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000\
"""


def test_split_input():
    test_result = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    assert split_input(TEST_INPUT) == test_result


def test_sum_each_inventory():
    test_result = [6000, 4000, 11000, 24000, 10000]
    assert sum_each_inventory(split_input(TEST_INPUT)) == test_result


def test_solve_a_with_example():
    test_result_a = 24000
    assert solve_a(TEST_INPUT) == test_result_a


def test_solve_b_with_example():
    test_result_b = 45000
    assert solve_b(TEST_INPUT) == test_result_b


def test_main():
    main()
