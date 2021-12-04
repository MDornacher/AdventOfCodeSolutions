from aocd.models import Puzzle
import numpy as np
import numpy.ma as ma


DAY = 4
YEAR = 2021


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_bingo_input(raw_input):
    raw_picks, *raw_boards = raw_input.split("\n\n")
    picks = np.array(raw_picks.split(",")).astype(int)
    boards = []
    for raw_board in raw_boards:
        board = np.array([line.split() for line in raw_board.splitlines()]).astype(int)
        boards.append(board)
    return picks, boards


def is_bingo(board_mask):
    if vertical_check(board_mask) or horizontal_check(board_mask):
        return True
    return False


def vertical_check(board_mask):
    return any([line.all() for line in board_mask])


def horizontal_check(board_mask):
    return any([line.all() for line in board_mask.T])


def play_bingo(board, picks):
    for i in range(board.shape[0], picks.size + 1):
        board_mask = np.in1d(board, picks[: i + 1]).reshape(board.shape)
        if is_bingo(board_mask):
            return i, board_mask
    raise ValueError(f"No bingo possible with this board {board} and picks {picks}")


def evaluate_final_score(board, mask, final_pick):
    return ma.masked_array(board, mask=mask).sum() * final_pick


def solve_a(puzzle_input):
    picks, boards = parse_bingo_input(puzzle_input)

    winning_round = None
    winning_board = None
    winning_board_mask = None
    for board in boards:
        rounds, board_mask = play_bingo(board, picks)
        if winning_round is None or rounds < winning_round:
            winning_round = rounds
            winning_board = board
            winning_board_mask = board_mask
    score = evaluate_final_score(
        winning_board, winning_board_mask, picks[winning_round]
    )
    return score


def solve_b(puzzle_input):
    picks, boards = parse_bingo_input(puzzle_input)

    losing_round = None
    losing_board = None
    losing_board_mask = None
    for board in boards:
        rounds, board_mask = play_bingo(board, picks)
        if losing_round is None or rounds > losing_round:
            losing_round = rounds
            losing_board = board
            losing_board_mask = board_mask
    score = evaluate_final_score(losing_board, losing_board_mask, picks[losing_round])
    return score


if __name__ == "__main__":
    main()
