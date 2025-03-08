from random import randrange

from brain_games.engine import play_game


def guess_gcd():
    print('Find the greatest common divisor of given numbers.')
    input = []
    for i in range(0, 3):
        num1 = randrange(1, 100)
        num2 = randrange(1, 100)
        i = num1
        j = num2
        while i % j != 0:
            i, j = j, i % j
        input.append((f'{num1} {num2}', str(j)))
    return play_game(input)
