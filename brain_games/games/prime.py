from random import randrange

from brain_games.engine import play_game


def is_prime(num):
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    if num == 2 or num == 3:
        return True
    i = 5
    d = 2
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += d
        if i % 3 == 0:
            i += d
    return True


def guess_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    input = []
    for i in range(0, 3):
        question = randrange(1, 100)
        input.append((question, 'yes' if is_prime(question) else 'no'))
    return play_game(input)  
