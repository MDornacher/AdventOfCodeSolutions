from aocd.models import Puzzle
import numpy as np
from matplotlib import pyplot as plt

DAY = 14
YEAR = 2022

RockStructure = list[tuple[int, int]]

EMPTY = 0
SAND = 1
ROCK = 2

SAND_SOURCE = (500, 0)


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_input(puzzle_input: str) -> list[RockStructure]:
    """
    Example:
    498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9
    Return [[(498, 4), (498, 6), (496, 6)], [(503, 4), (502, 4), (502, 9), (494, 9)]]
    """
    return [
        [tuple(map(int, coord.split(","))) for coord in line.split(" -> ")]
        for line in puzzle_input.strip().splitlines()
    ]


def build_cave(structures: list[RockStructure]) -> np.ndarray:
    # find max x and y in structures
    # create a 2d array of size max x and y
    # fill in the array with EMPTY
    x_max = max(max(x for x, _ in structure) for structure in structures)
    y_max = max(max(y for _, y in structure) for structure in structures)
    cave = np.full((x_max + 1, y_max + 1), EMPTY)

    # for each structure
    # draw the structure in the array
    # the structre is made of rocks
    for structure in structures:
        # slice between each pair of coordinates
        for (x1, y1), (x2, y2) in zip(structure, structure[1:]):
            # if the x coordinates are the same
            if x1 == x2:
                # draw a vertical line
                cave[x1, min(y1, y2) : max(y1, y2) + 1] = ROCK
            # if the y coordinates are the same
            elif y1 == y2:
                # draw a horizontal line
                cave[min(x1, x2) : max(x1, x2) + 1, y1] = ROCK
            else:
                raise ValueError("Invalid structure")
    # NOTE: I should have flipped the cave here, but I didn't
    # ¯\_(ツ)_/¯
    return cave


def plot_cave(cave: np.ndarray, trim_value=EMPTY):
    # trim the cave
    # remove empty rows from the top
    # remove empty rows from the bottom
    # remove empty columns from the left
    # remove empty columns from the right
    cave_trimmed = cave[
        np.any(cave != trim_value, axis=1),
        :,
    ]
    cave_trimmed = cave_trimmed[
        :,
        np.any(cave_trimmed != trim_value, axis=0),
    ]
    # plot the cave
    plt.imshow(cave_trimmed, cmap="binary", vmin=0, vmax=2)
    # save the image
    plt.savefig("cave.png")
    # close the plot
    plt.close()


def pour_sand(cave: np.ndarray, x: int, y: int) -> np.ndarray:
    """
    Pour sand into the cave at the given coordinates.
    Stop when the sand falls below the bottom of the cave.
    Return cave with SAND in the places where sand was poured.
    Sand falls down by incrementing y by 1.
    Sand falls left by decrementing x by 1.
    Sand falls right by incrementing x by 1.
    A unit of sand always falls down one step if possible.
    If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left.
    If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right.
    """
    x_current, y_current = x, y
    while True:
        # if the tile below is empty
        if cave[x_current, y_current + 1] == EMPTY:
            # move down
            y_current += 1
        # if the tile below is blocked
        else:
            # if the tile to the diagonal left is empty
            if cave[x_current - 1, y_current + 1] == EMPTY:
                # move down and left
                x_current -= 1
                y_current += 1
            # if the tile to the diagonal right is empty
            elif cave[x_current + 1, y_current + 1] == EMPTY:
                # move down and right
                x_current += 1
                y_current += 1
            # if the tiles to the left and right are blocked
            else:
                break
        # if the sand is outside the cave both to the left and right and below
        # raise an error
        if y_current >= cave.shape[1] - 1:
            raise ValueError("Sand fell below the bottom of the cave")
        if x_current <= 0 or x_current >= cave.shape[0] - 1:
            raise ValueError("Sand fell below the bottom of the cave")
        # if the sand is at rest
    # if tile is empty
    if cave[x_current, y_current] == EMPTY:
        # fill tile with sand
        cave[x_current, y_current] = SAND
        return
    # if resting position is the source
    if x_current == x and y_current == y:
        # raise overflow error
        raise ValueError("Sand overflowed the source")


def fill_cave_with_sand(cave: np.ndarray, x: int, y: int) -> np.ndarray:
    # repeatetly pour sand into the cave
    # until sand falls out of cave and raises an error
    # catch the error
    # return the cave
    while True:
        try:
            pour_sand(cave, x, y)
        # catch the error, print the error, and break the loop
        except ValueError as e:
            print(e)
            break


def count_sand(cave: np.ndarray) -> int:
    return np.count_nonzero(cave == SAND)


def solve_a(puzzle_input):
    structures = parse_input(puzzle_input)
    cave = build_cave(structures)

    fill_cave_with_sand(cave, *SAND_SOURCE)
    plot_cave(cave)
    return count_sand(cave)


def add_floor(cave: np.ndarray, x: int, y: int) -> tuple[np.ndarray, int, int]:
    """
    Add a floor to the cave.
    The floor is made of rocks.
    The floor is 2 plus the maximum y coordinate of the cave.
    In addition, pad the cave to the left and right with empty tiles.
    Keep the source of sand in the same place.
    Return the extended cave and the new coordinates of the source of sand.
    """
    # pad the cave on both sides of x axis with empty tiles
    cave_extended = np.pad(
        cave,
        ((cave.shape[1], cave.shape[1]), (0, 0)),
        "constant",
        constant_values=EMPTY,
    )
    # pad the cave to the bottom with two empty layers
    cave_extended = np.pad(
        cave_extended, ((0, 0), (0, 2)), "constant", constant_values=EMPTY
    )
    # add a floor to to the bottom of the cave
    cave_extended[:, -1:] = ROCK
    # new coordinates of the source of sand
    # but only x coordinate changes
    x_extended = x + cave.shape[1]
    y_extended = y
    return cave_extended, x_extended, y_extended


def solve_b(puzzle_input):
    structures = parse_input(puzzle_input)
    cave = build_cave(structures)
    cave_extended, x_extended, y_extended = add_floor(cave, *SAND_SOURCE)
    fill_cave_with_sand(cave_extended, x_extended, y_extended)
    plot_cave(cave_extended.T, trim_value=SAND)
    return count_sand(cave_extended)


if __name__ == "__main__":
    main()
