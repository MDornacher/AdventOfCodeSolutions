from aocs.day14 import solve_a, solve_b, main


TEST_INPUT = "NNCB\n\n"\
             "CH -> B\n"\
             "HH -> N\n"\
             "CB -> H\n"\
             "NH -> C\n"\
             "HB -> C\n"\
             "HC -> B\n"\
             "HN -> C\n"\
             "NN -> C\n"\
             "BH -> H\n"\
             "NC -> B\n"\
             "NB -> B\n"\
             "BN -> B\n"\
             "BB -> N\n"\
             "BC -> B\n"\
             "CC -> N\n"\
             "CN -> C"


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 1588


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 2188189693529


def test_main():
    main()
