import random


def get_default_tic_tac_toe_state() -> list[list[str]]:
    return [[".", ".", "."],[".", ".", "."],[".", ".", "."]]


def place_random_o(tic_tac_toe: list[list[str]]) -> list[list[str]]:
    empty_positions = [(row, column) for row in range(3) for column in range(3) if tic_tac_toe[row][column] == "."]

    if not empty_positions:
        return tic_tac_toe

    row, col = random.choice(empty_positions)
    tic_tac_toe[row][col] = "o"

    return tic_tac_toe
