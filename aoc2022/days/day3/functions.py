
from typing import List


def split_line_into_two(line: str) -> tuple[str, str]:
    middle = len(line) // 2
    return line[middle:], line[:middle]


def find_common_char(first: str, second: str) -> List[str]:
    return [element for element in (set(first) & set(second))]


def get_priority(commons: List[str]) -> int:
    total = 0
    for character in commons:
        code = ord(character)
        if 97 <= code <= 122:  # a-z
            total = code - 96
        elif 65 <= code <= 90:  # A-Z
            total = code - 38
        else:
            total = 0
    return total


def return_priority(line: str) -> int:
    first, second = split_line_into_two(line)
    commons = find_common_char(first, second)
    priority = get_priority(commons)
    return priority


def find_sum_badge(all_elves: List[List[str]]) -> int:
    total = 0
    for elves in all_elves:
        commons = [element for element in (set(elves[0]) & set(elves[1]) & set(elves[2]))]
        total += get_priority(commons)

    return total
