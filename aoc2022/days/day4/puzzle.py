from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day4 import is_contained, is_overlap


class DayFour(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> int:
        total = sum([is_contained(line) for line in self.lines])
        return total

    def solve_puzzle_two(self) -> int:
        total = sum([is_overlap(line) for line in self.lines])
        return total
