from typing import List


def find_n_strongest_elf(lines: List[str], n_strongest: int) -> int:
    elves = []
    tmp_sum = 0
    for line in lines:
        if line == '':
            elves.append(tmp_sum)
            tmp_sum = 0
        else:
            tmp_sum += int(line)
    elves.sort()
    return sum(elves[-n_strongest:])
