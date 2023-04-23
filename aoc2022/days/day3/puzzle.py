from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day3.functions import return_priority, find_sum_badge


class DayThree(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> int:
        total = sum([return_priority(line) for line in self.lines])
        return total

    def solve_puzzle_two(self) -> int:
        split_in_threes = [list(group) for group in zip(*[iter(self.lines)] * 3)]
        total = find_sum_badge(split_in_threes)
        return total
