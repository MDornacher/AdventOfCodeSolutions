from aocd.models import Puzzle
import re
from tqdm import tqdm
import math


DAY = 11
YEAR = 2022


def main():
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle.answer_a = solve_a(puzzle.input_data)
    puzzle.answer_b = solve_b(puzzle.input_data)


class Monkey:
    # init Monkey with monkey info string
    # with the following attributes:
    # - sid: int
    # - inventory: list of ints
    # - operation: format string with old as placeholder
    # - test: int to test divisibility
    # - if_true: int monkey id to throw to
    # - if_false: int monkey id to throw to
    # in addition, the following attributes are set:
    # - inspections = 0
    def __init__(self, monkey_info, worrisome=False):
        self.parse_monkey_info(monkey_info)
        self.inspections = 0
        self.worrisome = worrisome
        # initiate group lcm which is filled in later
        self.group_lcm = None

    # nicely formated repr of Monkey
    def __repr__(self):
        return (
            f"Monkey {self.id}:\n"
            f"Inventory: {', '.join([str(item) for item in self.inventory])}\n"
            f"Operation: {self.operation}\n"
            f"Test: divisible by {self.test}\n"
            f"If true: throw to monkey {self.if_true}\n"
            f"If false: throw to monkey {self.if_false}\n"
            f"Inspections: {self.inspections}"
        )

    def parse_monkey_info(self, monkey_info):
        """
        Example:
        '''\
        Monkey 0:
        Starting items: 79, 98
        Operation: new = old * 19
        Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3
        '''
        Extract info using regex:
         - id: int
         - inventory: list of ints
         - operation: string with old as placeholder, starting after "new = ",
            e.g. "{old} * 19"
         - test: int to test divisibility
         - if_true: int monkey id to throw to
         - if_false: int monkey id to throw to
        """
        self.id = int(re.search(r"Monkey (\d+):", monkey_info).group(1))
        self.inventory = [
            int(item)
            for item in re.search(r"Starting items: (.*)", monkey_info)
            .group(1)
            .split(", ")
        ]
        self.operation = re.search(r"Operation: new = (.*)", monkey_info).group(1)
        self.test = int(re.search(r"Test: divisible by (\d+)", monkey_info).group(1))
        self.if_true = int(
            re.search(r"If true: throw to monkey (\d+)", monkey_info).group(1)
        )
        self.if_false = int(
            re.search(r"If false: throw to monkey (\d+)", monkey_info).group(1)
        )
        self._fix_operation()

    def _fix_operation(self):
        # fix operation string
        # replace "old" with "{old}"
        self.operation = self.operation.replace("old", "{old}")

    def execute(self):
        # execute monkey operation
        # use value of each invetory item
        # as old in operation
        # do test on new value
        # depending on test result
        # throw to if_true or if_false
        # repeat until all items are distributed
        # set self.inventory to empty list
        for item in self.inventory:
            new_value = eval(self.operation.format(old=item))
            # add one to inspections
            self.inspections += 1

            # divide new value by three and round down to nearest integer
            # if we are worried about the monkeys
            # else keep numbers low by modulating by lcm of group
            if self.worrisome:
                new_value = new_value // 3
            else:
                new_value = new_value % self.group_lcm

            if new_value % self.test == 0:
                throw_to = self.if_true
            else:
                throw_to = self.if_false
            yield throw_to, new_value
        self.inventory = []


class MonkeyGroup:
    # A MonkeyGroup is a group of monkeys
    # that are adressable by their id
    # and that can be executed in a loop
    # Initiate with string of monkey info
    # Each monkey info is a list of strings
    # and monkey infos are split by empty lines
    def __init__(self, monkey_infos, worrisome=True):
        self.worrisome = worrisome
        self.monkeys = {}
        self.parse_monkey_infos(monkey_infos)
        self.find_lcm_of_group()
        self.rounds_played = 0

    def find_lcm_of_group(self):
        # find lcm of all monkeys test values
        self.lcm = math.lcm(*[monkey.test for monkey in self.monkeys.values()])
        # propagate lcm to all monkeys
        for monkey in self.monkeys.values():
            monkey.group_lcm = self.lcm

    # nicely formated repr of MonkeyGroup
    def __repr__(self):
        # add info about how many monkeys are in the group
        # and include monkey business
        # and add info about how many rounds have been played
        # and repr of each monkey
        group_info = (
            f"MonkeyGroup with {len(self.monkeys)} monkeys:\n"
            f"Monkey business: {self.monkey_business}\n"
            f"Rounds played: {self.rounds_played}\n"
        )
        for monkey in self.monkeys.values():
            group_info += f"{monkey}\n"
        return group_info

    def parse_monkey_infos(self, monkey_infos):
        for monkey_info in monkey_infos.split("\n\n"):
            monkey = Monkey(monkey_info, worrisome=self.worrisome)
            self.monkeys[monkey.id] = monkey

    def play_round(self):
        # play a round of monkey throwing
        # for each monkey
        # run execute method
        # and append thrown items to recipient monkeys inventory
        for monkey in self.monkeys.values():
            for recipient_id, thrown_item in monkey.execute():
                self.monkeys[recipient_id].inventory.append(thrown_item)
        # add one to rounds_played
        self.rounds_played += 1

    def play(self, number_of_rounds):
        # play a number of rounds
        for _ in tqdm(range(number_of_rounds)):
            self.play_round()

    @property
    def inspections(self):
        # return sorted list of inspections
        # of all monkeys in the group
        inspections = [monkey.inspections for monkey in self.monkeys.values()]
        # sort from highest to lowest
        inspections.sort(reverse=True)
        return inspections

    @property
    def monkey_business(self):
        # The level of monkey business can be found
        # by multiplying the number of inspections
        # of the top two monkeys in the group
        # ranked by number of inspections
        # in descending order
        # return the level of monkey business
        # as an integer
        # if there are less than two monkeys
        # return 0
        if len(self.monkeys) < 2:
            return 0
        return self.inspections[0] * self.inspections[1]


example_input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1\
"""


def solve_a(puzzle_input):
    """
    Return monkey business level after 20 rounds
    be worried
    """
    monkey_group = MonkeyGroup(puzzle_input, worrisome=True)
    monkey_group.play(20)
    print(monkey_group.monkey_business)
    return monkey_group.monkey_business


def solve_b(puzzle_input):
    """
    Return monkey business level after 10000 rounds
    but not be worried this time
    """
    monkey_group = MonkeyGroup(puzzle_input, worrisome=False)
    monkey_group.play(10000)
    print(monkey_group.monkey_business)
    return monkey_group.monkey_business


if __name__ == "__main__":
    main()
