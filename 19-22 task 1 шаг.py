from functools import lru_cache


def task(s):
    return s + 1, s + 2, s * 3


@lru_cache(None)
def game(s):
    if s >= 74:
        return 'W'
    count = 0

    if any(game(move) == 'W' for move in task(s)):
        return 'P1'

    if all(game(move) == 'P1' for move in task(s)):
        return 'B1'

    if any(game(move) == 'B1' for move in task(s)):
        return 'P2'


for i in range(20, 80):
    print(i, game(i))
