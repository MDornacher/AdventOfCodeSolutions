import numpy as np

from aocs.day13 import solve_a, solve_b, main

TEST_INPUT = (
    "6,10\n"
    "0,14\n"
    "9,10\n"
    "0,3\n"
    "10,4\n"
    "4,11\n"
    "6,0\n"
    "6,12\n"
    "4,1\n"
    "0,13\n"
    "10,12\n"
    "3,4\n"
    "3,0\n"
    "8,4\n"
    "1,10\n"
    "2,14\n"
    "8,10\n"
    "9,0\n"
    "\n"
    "fold along y=7\n"
    "fold along x=5"
)


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 17


def test_solve_b_with_example():
    expected = np.array(
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
    np.testing.assert_array_equal(solve_b(TEST_INPUT), expected)


def test_main():
    main()
