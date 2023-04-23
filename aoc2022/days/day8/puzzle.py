from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day8 import find_visible, find_best_view


class DayEight(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> int:
        visible_trees = find_visible(self.lines)
        return visible_trees

    def solve_puzzle_two(self) -> int:
        best_view = find_best_view(self.lines)
        return best_view
