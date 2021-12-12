from aocd.models import Puzzle
import numpy as np
from scipy.signal import convolve2d
from matplotlib import pyplot as plt


DAY = 11
YEAR = 2021

OCTOPUS_FOOTPRINT = np.ones((3, 3))


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    #puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


def parse_map(puzzle_input):
    return np.array([list(line) for line in puzzle_input.splitlines()]).astype(float)


def flash_critical_octopus(octopus_map):
    if not np.any(octopus_map > 9):
        return octopus_map, 0
    flash_centers = np.ma.masked_where(octopus_map > 9., octopus_map).mask.astype(float)
    flash_area = convolve2d(flash_centers, OCTOPUS_FOOTPRINT, mode="same")

    # flash
    octopus_map += flash_area

    # "remove" flashed octopus
    octopus_map[flash_centers == 1.] = np.nan
    return octopus_map, flash_centers.sum()


def evolve_octopus_map(octopus_map, rounds=1, plot=False):
    breaking_round = None
    flashes = 0
    for i in range(rounds):
        flashes_this_round = 0
        octopus_map += 1

        # flash once
        octopus_map, new_flashes = flash_critical_octopus(octopus_map)
        flashes_this_round += new_flashes

        # repeat until no flasher left
        while np.any(octopus_map > 9):
            octopus_map, new_flashes = flash_critical_octopus(octopus_map)
            flashes_this_round += new_flashes

        # count flashes
        flashes += flashes_this_round

        # reset
        np.nan_to_num(octopus_map, copy=False)

        if plot:
            plt.imshow(octopus_map, cmap="gist_gray")
            plt.axis("off")
            plt.savefig(f"../imgs/octopus_{i:05}", bbox_inches="tight")
            plt.clf()

        if flashes_this_round == octopus_map.size:
            print(f"OCTOPUS SYNCED FLASH IN ROUND {i+1}")
            breaking_round = i + 1
            return octopus_map, flashes, breaking_round

    return octopus_map, flashes, breaking_round


def solve_a(puzzle_input):
    octopus_map = parse_map(puzzle_input)
    _, flashes, _ = evolve_octopus_map(octopus_map, rounds=100)
    return int(flashes)


def solve_b(puzzle_input):
    #octopus_map = parse_map(puzzle_input)
    octopus_map = np.random.randint(9, size=(100, 100)).astype(float)
    *_, final_round = evolve_octopus_map(octopus_map, rounds=10000, plot=True)
    return final_round


if __name__ == "__main__":
    main()
