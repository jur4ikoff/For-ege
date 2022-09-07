from functools import lru_cache


def task(s):
    return s + 1, s + 2, s * 3


@lru_cache(None)
def game(s):
    if s >= 74:
        return 'W'
    count = 0

    if any(game(move) == 'W' for move in task(s)):  # первый петя 
        return 'P1'

    if all(game(move) == 'P1' for move in task(s)):  # первый ваня
        return 'B1'

    if any(game(move) == 'B1' for move in task(s)):  # второй петя 
        return 'P2'

    if all(game(move) == 'P1' or game(move) == 'P2' for move in task(s)):  # второй ваня 
        return 'B2'


for i in range(1, 80):
    print(i, game(i))
