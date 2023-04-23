from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day2 import calculate_score, score_with_best_move


class DayTwo(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> int:
        score = sum([calculate_score(line.split(" ")[0], line.split(" ")[1]) for line in self.lines])
        return score

    def solve_puzzle_two(self) -> int:
        score = sum([score_with_best_move(line.split(" ")[0], line.split(" ")[1]) for line in self.lines])
        return score
