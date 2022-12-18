from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day8 import find_visible, find_best_view


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day8_input.txt") if input_file is None else input_file)
    visible_trees = find_visible(lines)
    print(visible_trees)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day8_input.txt") if input_file is None else input_file)
    best_view = find_best_view(lines)
    print(best_view)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
