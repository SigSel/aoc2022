from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day1 import find_n_strongest_elf


class DayOne(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> int:
        total_calories = find_n_strongest_elf(self.lines, 1)
        return total_calories

    def solve_puzzle_two(self) -> int:
        total_calories = find_n_strongest_elf(self.lines, 3)
        return total_calories
