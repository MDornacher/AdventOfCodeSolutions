import pytest

from aocs.aoc_2021.day10 import (calculate_autocomplete_score, check_syntax,
                                 close_broken_code, main, solve_a, solve_b)

TEST_INPUT = (
    "[({(<(())[]>[[{[]{<()<>>\n"
    "[(()[<>])]({[<{<<[]>>(\n"
    "{([(<{}[<>[]}>{[]{[(<()>\n"
    "(((({<>}<{<{<>}{[]{[]{}\n"
    "[[<[([]))<([[{}[[()]]]\n"
    "[{[{({}]{}}([{[{{{}}([]\n"
    "{<[[]]>}<{[{[{[]{()[[[]\n"
    "[<(<(<(<{}))><([]([]()\n"
    "<{([([[(<>()){}]>(<<{{\n"
    "<{([{{}}[<[[[<>{}]]]>[]]\n"
)


@pytest.mark.parametrize(
    "line, wrong_char",
    [
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
    ],
)
def test_check_syntax_last_char(line, wrong_char):
    _, char, _ = check_syntax(line)
    assert char == wrong_char


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 26397


@pytest.mark.parametrize(
    "line, test_code_fix",
    [
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
    ],
)
def test_close_broken_code(line, test_code_fix):
    *_, code = check_syntax(line)
    code_fix = close_broken_code(code)
    assert code_fix == test_code_fix


@pytest.mark.parametrize(
    "code, test_score",
    [
        ("}}]])})]", 288957),
        (")}>]})", 5566),
        ("}}>}>))))", 1480781),
        ("]]}}]}]}>", 995444),
        ("])}>", 294),
    ],
)
def test_calculate_autocomplete_score(code, test_score):
    assert calculate_autocomplete_score(code) == test_score


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 288957


def test_main():
    main()
