from typing import List, Dict


def extract_all_data(lines: List[str]) -> tuple[List[str], List[str], Dict[int, List]]:
    pillars, commands = extract_pillars_and_commands(lines)
    columns = extract_columns(pillars)
    return pillars, commands, columns


def extract_pillars_and_commands(lines: List[str]):
    split_idx = lines.index("")
    pillars, commands = lines[:split_idx], lines[split_idx+1:]
    return pillars, commands


def all_numbers_in_string(line: str) -> List[int]:
    return [int(word) for word in line.split() if word.isdigit()]


def extract_columns(pillars: List[str]) -> Dict[int, List]:
    number_of_columns = max(all_numbers_in_string(pillars[-1]))
    columns = {number: [] for number in range(1, number_of_columns+1)}
    for line in pillars[:-1]:
        elements = [character for _, character in zip(line, line[1::4])]
        for idx, element in enumerate(elements):
            if element != " ":
                columns[idx+1].insert(0, element)
    return columns


def crate_mover_9000(commands: List[str], columns: Dict[int, List]) -> Dict[int, List]:
    for command in commands:
        numbers = all_numbers_in_string(command)
        boxes_to_move, from_column, to_column = numbers
        for _ in range(0, boxes_to_move):
            element_to_move = columns[from_column][-1]
            columns[to_column].append(element_to_move)
            columns[from_column].pop()

    return columns


def crate_mover_9001(commands: List[str], columns: Dict[int, List]) -> Dict[int, List]:
    for command in commands:
        numbers = all_numbers_in_string(command)
        boxes_to_move, from_column, to_column = numbers
        element_to_move = columns[from_column][-boxes_to_move:]
        for element in element_to_move:
            columns[to_column].append(element)
            columns[from_column].pop()

    return columns


def get_top_of_columns(columns: Dict[int, List]) -> str:
    output = ""
    for key, value in columns.items():
        output += value[-1]
    return output
