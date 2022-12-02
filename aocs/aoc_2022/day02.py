from aocd.models import Puzzle


DAY = 2
YEAR = 2022

GAME_SCORE = {
    "victory": 6,
    "draw": 3,
    "defeat": 0,
}

SHAPE_SCORE = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def split_input(puzzle_input: str) -> list[list[str, str]]:
    """Example input:
    'A Y\nB X\nC Z'
    """
    return [line.split() for line in puzzle_input.splitlines()]


def play_match(player_a: str, player_b: str) -> str:
    if player_a == player_b:
        return "draw"
    elif player_a == "rock" and player_b == "scissors":
        return "victory"
    elif player_a == "paper" and player_b == "rock":
        return "victory"
    elif player_a == "scissors" and player_b == "paper":
        return "victory"
    else:
        return "defeat"


def reverse_match(opponent_choice: str, outcome: str) -> str:
    if outcome == "draw":
        return opponent_choice
    elif outcome == "victory":
        if opponent_choice == "rock":
            return "paper"
        elif opponent_choice == "paper":
            return "scissors"
        elif opponent_choice == "scissors":
            return "rock"
    elif outcome == "defeat":
        if opponent_choice == "rock":
            return "scissors"
        elif opponent_choice == "paper":
            return "rock"
        elif opponent_choice == "scissors":
            return "paper"


def solve_a(puzzle_input):
    translation = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    guide_choices = split_input(puzzle_input)
    my_score = 0
    for (opponent_choice, my_choice) in guide_choices:
        opponent_choice = translation[opponent_choice]
        my_choice = translation[my_choice]
        match_result = play_match(my_choice, opponent_choice)
        my_score += GAME_SCORE[match_result] + SHAPE_SCORE[my_choice]
    return my_score


def solve_b(puzzle_input):
    choice_translation = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }
    outcome_translation = {
        "X": "defeat",
        "Y": "draw",
        "Z": "victory",
    }
    guide_choices = split_input(puzzle_input)
    my_score = 0
    # choose the choice that will match the outcome
    for (opponent_choice, my_choice) in guide_choices:
        opponent_choice = choice_translation[opponent_choice]
        my_choice = reverse_match(opponent_choice, outcome_translation[my_choice])
        match_result = play_match(my_choice, opponent_choice)
        my_score += GAME_SCORE[match_result] + SHAPE_SCORE[my_choice]
    return my_score


if __name__ == "__main__":
    main()
