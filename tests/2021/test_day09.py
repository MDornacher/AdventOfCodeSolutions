import numpy as np
import pytest

from aocs.aoc_2021.day09 import (find_minima_mask, find_most_common_basins,
                                 main, parse_input, solve_a, solve_b)

TEST_INPUT = "2199943210\n"\
             "3987894921\n"\
             "9856789892\n"\
             "8767896789\n"\
             "9899965678"


@pytest.mark.parametrize(
    "heat_map, mask_result",
    [
        (
            # easy center minima
            np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            np.array([[False, False, False], [False, True, False], [False, False, False]])
        ),
        (
            # diagonal minima
            np.array([[1, 2, 2], [2, 0, 2], [2, 2, 0]]),
            np.array([[True, False, False], [False, True, False], [False, False, True]])
        ),
        (
            # corner
            np.array([[0, 1, 1], [1, 1, 1], [1, 1, 0]]),
            np.array([[True, False, False], [False, False, False], [False, False, True]])
        ),
        (
            # "fake" local minima (<= instead of <)
            np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]]),
            np.array([[False, False, False], [False, False, False], [False, False, False]])
        ),
    ]
)
def test_find_minima_mask(heat_map, mask_result):
    minima_mask = find_minima_mask(heat_map)
    np.testing.assert_array_equal(minima_mask, mask_result)


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 15


def test_find_most_common_basins():
    heat_map = parse_input(TEST_INPUT)
    most_common_basins = find_most_common_basins(heat_map)
    assert most_common_basins == [(3, 14), (2, 9), (4, 9), (1, 3)]


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 1134


def test_main():
    main()
