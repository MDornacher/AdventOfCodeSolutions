from aocd.models import Puzzle
import re


DAY = 5
YEAR = 2022

# custom types
Stack = list[str]
Stacks = list[Stack]
Move = tuple[int, int, int]
Moves = list[Move]


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def read_stacks(raw_stacks: str) -> Stacks:
    stacks = []
    for row in raw_stacks.splitlines():
        stacks.append(list(row[1::4]))
    # return without last stack
    return stacks[:-1]


def read_moves(raw_moves: str) -> Moves:
    """
    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    -> [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
    Use regex to parse to extract the numbers
    """
    matches = re.findall(r"move (\d+) from (\d+) to (\d+)", raw_moves)
    return [(int(a), int(b), int(c)) for a, b, c in matches]


def read_input(puzzle_input: str) -> tuple[Stacks, Moves]:
    raw_stacks, raw_moves = puzzle_input.split("\n\n")
    stacks = read_stacks(raw_stacks)
    moves = read_moves(raw_moves)
    return stacks, moves


def rotate_stacks(stacks: Stacks) -> Stacks:
    """
    [['', 'D', ''], ['N', 'C', 'M'], ['Z', 'M', 'P']] -> [['Z', 'N', ''], ['M', 'C', 'D'], ['P', 'M', '']]
    """
    return list(map(list, zip(*stacks[::-1])))


def strip_empty_block_from_stacks(stacks: Stacks) -> Stacks:
    """
    [['Z', 'N', ''], ['M', 'C', 'D'], ['P', 'M', '']] -> [['Z', 'N'], ['M', 'C', 'D'], ['P', 'M']]
    Remove blocks empty blocks (i.e. '') from the stacks
    """
    return [list("".join(stack).strip()) for stack in stacks]


def move_one_at_a_time(stacks: Stacks, move: Move) -> Stacks:
    number_of_boxes, start_stack, end_stack = move
    # stacks labels start at 1, but lists start at 0
    start_stack -= 1
    end_stack -= 1
    # move the boxes
    for _ in range(number_of_boxes):
        stacks[end_stack].append(stacks[start_stack].pop())
    return stacks


def solve_a(puzzle_input):
    horizontal_stacks, moves = read_input(puzzle_input)
    stacks = rotate_stacks(horizontal_stacks)
    stacks = strip_empty_block_from_stacks(stacks)
    for move in moves:
        stacks = move_one_at_a_time(stacks, move)
    # return the top block of each stack
    return "".join([stack[-1] for stack in stacks])


def move_all_at_once(stacks: Stacks, move: Move) -> Stacks:
    number_of_boxes, start_stack, end_stack = move
    # stacks labels start at 1, but lists start at 0
    start_stack -= 1
    end_stack -= 1
    # move the boxes
    stacks[end_stack].extend(stacks[start_stack][-number_of_boxes:])
    stacks[start_stack] = stacks[start_stack][:-number_of_boxes]
    return stacks


def solve_b(puzzle_input):
    horizontal_stacks, moves = read_input(puzzle_input)
    stacks = rotate_stacks(horizontal_stacks)
    stacks = strip_empty_block_from_stacks(stacks)
    for move in moves:
        stacks = move_all_at_once(stacks, move)
    # return the top block of each stack
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    main()
