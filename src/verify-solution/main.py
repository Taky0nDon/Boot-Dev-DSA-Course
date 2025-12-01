def get_num_guesses(length: int) -> int:
    return sum(26 ** l for l in range(1, length + 1))
