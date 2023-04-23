from aoc2022.common import BaseDay
from pathlib import Path

from aoc2022.days.day5 import extract_all_data, get_top_of_columns, crate_mover_9000, crate_mover_9001


class DayFive(BaseDay):
    def __init__(self, input_puzzle_file: Path):
        super().__init__(input_puzzle_file)

    def solve_puzzle_one(self) -> str:
        pillars, commands, columns = extract_all_data(self.lines)
        new_columns = crate_mover_9000(commands, columns)
        top = get_top_of_columns(new_columns)
        return top

    def solve_puzzle_two(self) -> str:
        pillars, commands, columns = extract_all_data(self.lines)
        new_columns = crate_mover_9001(commands, columns)
        top = get_top_of_columns(new_columns)
        return top
