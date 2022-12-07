# A = Rock, B = Paper, C = Sciss
# x = Rock, Y = Paper, Z = Sciss
# X = lose, Y = Draw, Z = Win

def calculate_score(opponent: str, me: str) -> int:
    points = {"X": 1, "Y": 2, "Z": 3}
    result = get_results(opponent, me)

    return points[me]+result


def score_with_best_move(opponent: str, result: str) -> int:
    choice = get_choice(opponent, result)
    return calculate_score(opponent, choice)


def get_results(opponent: str, me: str) -> int:
    win_matrix = {
        "AX": 3, "AY": 6, "AZ": 0,
        "BX": 0, "BY": 3, "BZ": 6,
        "CX": 6, "CY": 0, "CZ": 3
    }
    return win_matrix[opponent+me]


def get_choice(opponent: str, result: str) -> str:
    result_matrix = {
       "A": {"X": "Z", "Y": "X", "Z": "Y"},
       "B": {"X": "X", "Y": "Y", "Z": "Z"},
       "C": {"X": "Y", "Y": "Z", "Z": "X"},
    }
    return result_matrix[opponent][result]
