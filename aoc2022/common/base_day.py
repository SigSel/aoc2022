from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

from aoc2022.common import read_file


class BaseDay(ABC):
    def __init__(self, input_puzzle_file: Path) -> None:
        self.input_puzzle_file = input_puzzle_file
        self.lines = read_file(self.input_puzzle_file)

    @abstractmethod
    def solve_puzzle_one(self) -> Union[str, int, float]:
        raise NotImplementedError

    @abstractmethod
    def solve_puzzle_two(self) -> Union[str, int, float]:
        raise NotImplementedError
