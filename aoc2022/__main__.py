import importlib
import sys
from pathlib import Path

from aoc2022.common import parse_args
from aoc2022.days import SUPPORTED_DAYS


def main():
    args = parse_args(sys.argv[1:])
    if args.day not in SUPPORTED_DAYS.keys():
        print(f"Input day : {args.day} is not supported.\n Supported days are {list(SUPPORTED_DAYS.keys())}")
        sys.exit(0)
    day = SUPPORTED_DAYS[args.day]
    mod = importlib.import_module(f"aoc2022.days.{day}")
    input_file = Path.cwd().joinpath(f"inputs", f"{day}_input.txt")
    if not input_file.is_file():
        print(f"Could not find input_file: {input_file} for day{args.day}.")
        sys.exit(0)
    print(f"Solution for the first puzzle of day {args.day}: ")
    mod.puzzle_one(input_file=input_file)
    print(f"Solution for the second puzzle of day {args.day}: ")
    mod.puzzle_two(input_file=input_file)


if __name__ == "__main__":
    main()
