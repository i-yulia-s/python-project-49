from random import randrange
from brain_games.engine import play_game


def guess_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    input = []
    for i in range(0, 3):
        question = randrange(20)
        input.append((question, 'yes' if question % 2 == 0 else 'no'))
    return play_game(input)
