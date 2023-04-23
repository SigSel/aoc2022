import sys
from pathlib import Path

from aoc2022.common import parse_args
from aoc2022.days.day_fetcher import get_day


def main():
    args = parse_args(sys.argv[1:])
    input_file = Path.cwd().joinpath(f"inputs", f"day{args.day}_input.txt")
    if not input_file.exists():
        print(f"Input file for day {args.day} does not exist in the inputs folder. Please add it.")
        sys.exit(0)
    try:
        day = get_day(day_number=int(args.day), input_puzzle_file=input_file)
        print(day.solve_puzzle_one())
        print(day.solve_puzzle_two())
    except NotImplementedError:
        print(f"Day {args.day} is not implemented.")
        sys.exit(1)


if __name__ == "__main__":
    main()
