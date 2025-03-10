from random import randrange

from brain_games.engine import play_game


def gcd(number1, number2):
    while number1 % number2 != 0:
        number1, number2 = number2, number1 % number2
    return number2


def guess_gcd():
    print('Find the greatest common divisor of given numbers.')
    input = []
    for i in range(0, 3):
        num1 = randrange(1, 100)
        num2 = randrange(1, 100)
        input.append((f'{num1} {num2}', str(gcd(num1, num2))))
    return play_game(input)
