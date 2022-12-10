from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day3.functions import return_priority, find_sum_badge


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day3_input.txt") if input_file is None else input_file)
    total = sum([return_priority(line) for line in lines])
    print(total)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day3_input.txt") if input_file is None else input_file)
    split_in_threes = [list(group) for group in zip(*[iter(lines)] * 3)]
    total = find_sum_badge(split_in_threes)
    print(total)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
