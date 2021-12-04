from aocs.day4 import solve_a, solve_b, main, is_bingo, play_bingo
import pytest
import numpy as np


TEST_INPUT = (
    ""
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n"
    "22 13 17 11  0\n8  2 23  4 24\n21  9 14 16  7\n6 10  3 18  5\n1 12 20 15 19\n\n"
    "3 15  0  2 22\n9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6\n\n"
    "14 21 17 24  4\n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n2  0 12  3  7"
)


@pytest.mark.parametrize(
    "board_mask, expected",
    [
        (
            np.array(
                [[False, False, False], [False, False, False], [False, False, False]]
            ),
            False,
        ),
        (np.array([[True, True, True], [True, True, True], [True, True, True]]), True),
        (
            np.array(
                [[True, False, False], [False, True, False], [False, False, True]]
            ),
            False,
        ),
        (
            np.array(
                [[False, False, False], [True, True, True], [False, False, False]]
            ),
            True,
        ),
        (
            np.array(
                [[False, True, False], [False, True, False], [False, True, False]]
            ),
            True,
        ),
    ],
)
def test_is_bingo(board_mask, expected):
    assert is_bingo(board_mask) == expected


@pytest.mark.parametrize(
    "board, picks, expected_winning_round",
    [
        (np.arange(4).reshape((2, 2)), np.array([0]), None),
        (np.arange(4).reshape((2, 2)), np.arange(4), 2),
        (np.arange(4).reshape((2, 2)), np.array([0, 3, 1, 2]), 3),
        (np.arange(9).reshape((3, 3)), np.arange(9), 3),
    ],
)
def test_play_bingo(board, picks, expected_winning_round):
    if expected_winning_round is None:
        with pytest.raises(ValueError):
            play_bingo(board, picks)
    else:
        winning_round, _ = play_bingo(board, picks)
        assert winning_round == expected_winning_round


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 4512


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 1924


def test_main():
    main()
