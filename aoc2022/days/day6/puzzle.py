from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day6 import find_start_of_packet, find_start_of_message


class DaySix(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> int:
        start = find_start_of_packet(self.lines[0])
        return start

    def solve_puzzle_two(self) -> int:
        start = find_start_of_message(self.lines[0])
        return start
