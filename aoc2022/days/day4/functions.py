

def get_range_sets(line: str) -> tuple[set, set]:
    first, second = line.split(",")
    first_range = range(int(first.split("-")[0]), int(first.split("-")[1])+1)
    second_range = range(int(second.split("-")[0]), int(second.split("-")[1])+1)
    return set(first_range), set(second_range)


def is_contained(line: str) -> bool:
    first_set, second_set = get_range_sets(line)
    return True if first_set.issubset(second_set) or second_set.issubset(first_set) else False


def is_overlap(line: str) -> bool:
    first_set, second_set = get_range_sets(line)
    return True if first_set.intersection(second_set) else False
