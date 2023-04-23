from pathlib import Path
from typing import Union

from aoc2022.days import (
    DayOne,
    DayTwo,
    DayThree,
    DayFour,
    DayFive,
    DaySix,
    DayEight
)


def get_day(day_number: int, input_puzzle_file: Path) -> Union[
    DayOne,
    DayTwo,
    DayThree,
    DayFour,
    DayFive,
    DaySix,
    DayEight
]:
    match day_number:
        case 1:
            return DayOne(input_puzzle_file=input_puzzle_file)
        case 2:
            return DayTwo(input_puzzle_file=input_puzzle_file)
        case 3:
            return DayThree(input_puzzle_file=input_puzzle_file)
        case 4:
            return DayFour(input_puzzle_file=input_puzzle_file)
        case 5:
            return DayFive(input_puzzle_file=input_puzzle_file)
        case 6:
            return DaySix(input_puzzle_file=input_puzzle_file)
        case 8:
            return DayEight(input_puzzle_file=input_puzzle_file)
        case _:
            raise NotImplementedError
