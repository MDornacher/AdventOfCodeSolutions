from aocs.day1 import solve_a, solve_b, main


TEST_INPUT = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263\n"


def test_solve_a_with_example():
    test_result_a = 7
    assert solve_a(TEST_INPUT) == test_result_a


def test_solve_b_with_example():
    test_result_b = 5
    assert solve_b(TEST_INPUT) == test_result_b


def test_main():
    main()
