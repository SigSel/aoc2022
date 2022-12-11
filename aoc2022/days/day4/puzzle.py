from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day4 import is_contained, is_overlap


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day4_input.txt") if input_file is None else input_file)
    total = sum([is_contained(line) for line in lines])
    print(total)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day4_input.txt") if input_file is None else input_file)
    total = sum([is_overlap(line) for line in lines])
    print(total)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
