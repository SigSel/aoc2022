import pytest
from typing import Union
from pathlib import Path

from aoc2022.days.day_fetcher import get_day


def get_input_path(day_number: int) -> Path:
    parent_dir = Path.cwd().parent
    absolute_path = parent_dir.joinpath(f"inputs", f"day{day_number}_input.txt")
    if not absolute_path.exists():
        print(absolute_path.absolute())
        raise FileNotFoundError
    return absolute_path


@pytest.mark.parametrize(
    "day, expected_solution_one, expected_solution_two",
    [
        (1, 67622, 201491),
        (2, 13809, 12316),
        (3, 7785, 2633),
        (4, 556, 876),
        (5, "FWSHSPJWM", "PWPWHGFZS"),
        (6, 1034, 2472),
        (8, 1859, 332640)
    ]
)
def test_all_days_blackbox(
        day: int,
        expected_solution_one: Union[int, str],
        expected_solution_two: Union[int, str]
) -> None:
    input_path = get_input_path(day)
    current_day = get_day(day_number=day, input_puzzle_file=input_path)
    assert current_day.solve_puzzle_one() == expected_solution_one
    assert current_day.solve_puzzle_two() == expected_solution_two
