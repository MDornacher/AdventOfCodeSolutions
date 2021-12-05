import numpy as np

from aocs.day5 import solve_a, solve_b, main, mark_vent, parse_vents, create_field


TEST_INPUT = "0,9 -> 5,9\n8,0 -> 0,8\n" \
             "9,4 -> 3,4\n2,2 -> 2,1\n" \
             "7,0 -> 7,4\n6,4 -> 2,0\n" \
             "0,9 -> 2,9\n3,4 -> 1,4\n" \
             "0,0 -> 8,8\n5,5 -> 8,2"


def test_simple_mark_vent():
    vents = parse_vents(TEST_INPUT)
    field = create_field(vents)
    for vent in vents:
        field = mark_vent(field, vent, diagonal=False)

    test_result = np.array([
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ])
    np.testing.assert_array_equal(
        field,
        test_result
    )


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 5


def test_diagonal_mark_vent():
    vents = parse_vents(TEST_INPUT)
    field = create_field(vents)
    for vent in vents:
        field = mark_vent(field, vent, diagonal=True)

    test_result = np.array([
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
        [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
        [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ])
    np.testing.assert_array_equal(
        field,
        test_result
    )


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 12


def test_main():
    main()
