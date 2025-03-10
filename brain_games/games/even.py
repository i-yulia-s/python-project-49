from random import randrange

from brain_games.engine import play_game


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def guess_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    input = []
    for i in range(0, 3):
        question = randrange(20)
        input.append((question, 'yes' if is_even(question) else 'no'))
    return play_game(input)
