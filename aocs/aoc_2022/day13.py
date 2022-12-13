from aocd.models import Puzzle
from functools import cmp_to_key

DAY = 13
YEAR = 2022


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(puzzle_input: str) -> tuple[list, list]:
    """
    Example:
    [1,1,3,1,1]
    [1,1,5,1,1]

    [[1],[2,3,4]]
    [[1],4]

    [9]
    [[8,7,6]]

    [[4,4],4,4]
    [[4,4],4,4,4]

    [7,7,7,7]
    [7,7,7]

    []
    [3]

    [[[]]]
    [[]]

    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    """
    packets = [eval(packet) for packet in puzzle_input.strip().splitlines() if packet]
    return packets[::2], packets[1::2]


def compare(left: list | int, right: list | int) -> int:
    """
    Compare left and right
    If left > right, return > 0
    If left == right, return 0
    If left < right, return < 0
    """
    match (left, right):
        case int(left), int(right):
            return left - right
        case list(left), list(right):
            for l, r in zip(left, right):
                result = compare(l, r)
                if result != 0:
                    return result
            return len(left) - len(right)
        case int(left), list(right):
            return compare([left], right)
        case list(left), int(right):
            return compare(left, [right])
    return 0


def solve_a(puzzle_input):
    """
    Pairwise comparison of left and right
    Save indices of pairs with right order, i.e. left < right
    Return the sum of the indices
    Indices start at 1
    """
    lefts, rights = parse_input(puzzle_input)
    entries_with_right_order = []
    for i, (left, right) in enumerate(zip(lefts, rights), start=1):
        if compare(left, right) < 0:
            entries_with_right_order.append(i)
    return sum(entries_with_right_order)


def solve_b(puzzle_input):
    """
    Group left and right together
    add the special packets to the list of packets:
    - [[2]]
    - [[6]]
    and sort them with the compare function
    Find position of those special packets
    Return the product of those two indices
    """
    special_packets = [[[2]], [[6]]]
    lefts, rights = parse_input(puzzle_input)
    packets = lefts + rights + special_packets
    # sort packets with compare function
    # use key=compare to sort by compare function
    # but compare is not a key function
    # what would be a good package to use for this?
    # functools.cmp_to_key
    # https://docs.python.org/3/library/functools.html#functools.cmp_to_key
    # Thanks you, Copilot! :)
    packets.sort(key=cmp_to_key(compare))
    index_of_special_packets = [packets.index(packet) for packet in special_packets]
    # remember, inidces are expected to start at 1
    return (index_of_special_packets[0] + 1) * (index_of_special_packets[1] + 1)


if __name__ == "__main__":
    main()
