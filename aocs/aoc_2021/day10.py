from aocd.models import Puzzle


DAY = 10
YEAR = 2021

MATCH = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
REVERSE_MATCH = {v: k for k, v in MATCH.items()}

SYNTAX_SCORE_SYSTEM = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
AUTOCOMPLETE_SCORE_SYSTEM = {
    "": 0,
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def check_syntax(line):
    code = []
    for i, char in enumerate(line):
        if char in MATCH.values():
            code.append(char)
            continue
        if MATCH[char] == code[-1]:
            code.pop()
            continue
        return i, char, code
    return -1, "", code


def solve_a(puzzle_input):
    lines = puzzle_input.splitlines()
    score = 0
    for line in lines:
        _, char, _ = check_syntax(line)
        score += SYNTAX_SCORE_SYSTEM[char]
    return score


def close_broken_code(code):
    return "".join([REVERSE_MATCH[char] for char in reversed(code)])


def calculate_autocomplete_score(code):
    score = 0
    for char in code:
        score = (score * 5) + AUTOCOMPLETE_SCORE_SYSTEM[char]
    return score


def solve_b(puzzle_input):
    lines = puzzle_input.splitlines()
    scores = []
    for line in lines:
        _, last_char, code = check_syntax(line)
        if last_char:
            continue
        code_fix = close_broken_code(code)
        scores.append(calculate_autocomplete_score(code_fix))
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    main()
