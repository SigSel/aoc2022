from aoc2022.common import read_file
from pathlib import Path
from typing import Optional

from aoc2022.days.day2 import calculate_score, score_with_best_move


def puzzle_one(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day2_input.txt") if input_file is None else input_file)
    score = sum([calculate_score(line.split(" ")[0], line.split(" ")[1]) for line in lines])
    print(score)


def puzzle_two(input_file: Optional[Path] = None) -> None:
    lines = read_file(Path("day2_input.txt") if input_file is None else input_file)
    score = sum([score_with_best_move(line.split(" ")[0], line.split(" ")[1]) for line in lines])
    print(score)


if __name__ == "__main__":
    puzzle_one()
    puzzle_two()
