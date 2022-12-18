from typing import List


def find_visible(lines: List[str]) -> int:
    visible_trees = 0
    for row_idx, line in enumerate(lines):
        for column_idx, value in enumerate(line):
            if any([
                    check_right(line, column_idx),
                    check_left(line, column_idx),
                    check_top(lines, row_idx, column_idx),
                    check_bottom(lines, row_idx, column_idx)
                ]
            ):
                visible_trees += 1
    return visible_trees


def check_right(line: str, index: int) -> bool:
    return all(line[index] > line[i] for i in range(index+1, len(line)))


def check_left(line: str, index: int) -> bool:
    return all(line[index] > line[i] for i in range(index-1, -1, -1))


def check_top(lines: List[str], row_index: int, column_index: int) -> bool:
    return all(lines[row_index][column_index] > lines[i][column_index] for i in range(row_index-1, -1, -1))


def check_bottom(lines: List[str], row_index: int, column_index: int) -> bool:
    return all(lines[row_index][column_index] > lines[i][column_index] for i in range(row_index+1, len(lines)))


def find_best_view(lines: List[str]) -> int:
    best_view = 0
    for row_idx, line in enumerate(lines):
        for column_idx, value in enumerate(line):
            right, left = look_right(line, column_idx), look_left(line, column_idx)
            top, bottom = look_top(lines, row_idx, column_idx), look_bottom(lines, row_idx, column_idx)
            best_view = max(best_view, right*left*top*bottom)
    return best_view


def look_right(line: str, index: int) -> int:
    seen_trees = 0
    for i in range(index+1, len(line)):
        seen_trees += 1
        if line[index] <= line[i]:
            break
    return seen_trees


def look_left(line: str, index: int) -> int:
    seen_trees = 0
    for i in range(index-1, -1, -1):
        seen_trees += 1
        if line[index] <= line[i]:
            break
    return seen_trees


def look_top(lines: List[str], row_index: int, column_index: int) -> int:
    seen_trees = 0
    for i in range(row_index-1, -1, -1):
        seen_trees += 1
        if lines[row_index][column_index] <= lines[i][column_index]:
            break
    return seen_trees


def look_bottom(lines: List[str], row_index: int, column_index: int) -> int:
    seen_trees = 0
    for i in range(row_index+1, len(lines)):
        seen_trees += 1
        if lines[row_index][column_index] <= lines[i][column_index]:
            break
    return seen_trees
