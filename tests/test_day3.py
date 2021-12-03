from aocs.day3 import (
    solve_a,
    solve_b,
    main,
    calculate_oxygen_rating,
    parse_report,
    calculate_carbon_rating,
    calculate_gamma_rate,
    calculate_epsilon_rate,
)

TEST_INPUT = (
    "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010"
)


def test_gamma_rate():
    report = parse_report(TEST_INPUT)
    assert calculate_gamma_rate(report) == 22


def test_epsilon_rate():
    report = parse_report(TEST_INPUT)
    assert calculate_epsilon_rate(report) == 9


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 198


def test_oxygen_rating():
    report = parse_report(TEST_INPUT)
    assert calculate_oxygen_rating(report) == 23


def test_carbon_rating():
    report = parse_report(TEST_INPUT)
    assert calculate_carbon_rating(report) == 10


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 230


def test_main():
    main()
