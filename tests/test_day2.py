from aocs.day2 import solve_a, solve_b, main


TEST_INPUT = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2"


def test_solve_a_with_example():
    test_result_a = 150
    assert solve_a(TEST_INPUT) == test_result_a


def test_solve_b_with_example():
    test_result_b = 900
    assert solve_b(TEST_INPUT) == test_result_b


def test_main():
    main()
