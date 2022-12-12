from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day6 import find_start_of_packet, find_start_of_message


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day6_input.txt") if input_file is None else input_file)
    start = find_start_of_packet(lines[0])
    print(start)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day6_input.txt") if input_file is None else input_file)
    start = find_start_of_message(lines[0])
    print(start)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
