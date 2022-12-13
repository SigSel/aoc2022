from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day5 import extract_all_data, get_top_of_columns, crate_mover_9000, crate_mover_9001


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day5_input.txt") if input_file is None else input_file)
    pillars, commands, columns = extract_all_data(lines)
    new_columns = crate_mover_9000(commands, columns)
    top = get_top_of_columns(new_columns)
    print(top)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day5_input.txt") if input_file is None else input_file)
    pillars, commands, columns = extract_all_data(lines)
    new_columns = crate_mover_9001(commands, columns)
    top = get_top_of_columns(new_columns)
    print(top)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
