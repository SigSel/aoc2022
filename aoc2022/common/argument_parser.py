import argparse

from typing import List


def parse_args(argument_list: List[str]) -> argparse.Namespace:
    """Parses command line arguments using argparse."""
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--day", help="Which day to run the puzzles from")
    return parser.parse_args(argument_list)
