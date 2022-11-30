import pytest

from aocs.aoc_2021.day12 import main, solve_a, solve_b

TEST_INPUT_SHORT = "start-A\n" "start-b\n" "A-c\n" "A-b\n" "b-d\n" "A-end\n" "b-end"

TEST_INPUT_MEDIUM = (
    "dc-end\n"
    "HN-start\n"
    "start-kj\n"
    "dc-start\n"
    "dc-HN\n"
    "LN-dc\n"
    "HN-end\n"
    "kj-sa\n"
    "kj-HN\n"
    "kj-dc"
)

TEST_INPUT_LONG = (
    "fs-end\n"
    "he-DX\n"
    "fs-he\n"
    "start-DX\n"
    "pj-DX\n"
    "end-zg\n"
    "zg-sl\n"
    "zg-pj\n"
    "pj-he\n"
    "RW-he\n"
    "fs-DX\n"
    "pj-RW\n"
    "zg-RW\n"
    "start-pj\n"
    "he-WI\n"
    "zg-he\n"
    "pj-fs\n"
    "start-RW\n"
)


@pytest.mark.parametrize(
    "test_input, number_of_paths",
    [
        (TEST_INPUT_SHORT, 10),
        (TEST_INPUT_MEDIUM, 19),
        (TEST_INPUT_LONG, 226),
    ],
)
def test_solve_a_with_example(test_input, number_of_paths):
    assert solve_a(test_input) == number_of_paths


@pytest.mark.parametrize(
    "test_input, number_of_paths",
    [
        (TEST_INPUT_SHORT, 36),
        (TEST_INPUT_MEDIUM, 103),
        (TEST_INPUT_LONG, 3509),
    ],
)
def test_solve_b_with_example(test_input, number_of_paths):
    assert solve_b(test_input) == number_of_paths


def test_main():
    main()
