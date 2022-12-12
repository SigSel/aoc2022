

def find_start_of_packet(line: str) -> int:
    start_digit = 4
    for code in zip(line, line[1:], line[2:], line[3:]):
        if len(set(code)) == 4:
            break
        else:
            start_digit += 1

    return start_digit


def find_start_of_message(line: str) -> int:
    start_digit = 14
    for idx in range(len(line)-14):
        if len(set(line[idx:idx+14])) == 14:
            break
        else:
            start_digit += 1

    return start_digit
