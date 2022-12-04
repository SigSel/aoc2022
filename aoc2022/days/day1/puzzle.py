from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day1 import find_n_strongest_elf


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day1_input.txt") if input_file is None else input_file)
    total_calories = find_n_strongest_elf(lines, 1)
    print(total_calories)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day1_input.txt") if input_file is None else input_file)
    total_calories = find_n_strongest_elf(lines, 3)
    print(total_calories)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
