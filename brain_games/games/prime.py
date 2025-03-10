from random import randrange

from brain_games.engine import play_game


def is_prime(num):
    # 2 and 3 are the only primes divisible by 2 or 3.
    # We make sure that our number is not 2 or 3,
    # and then skip divisors 2 and 3 in the check.
    if num == 2 or num == 3:
        return True
    # 1 is not a prime
    # All numbers divisible by 2 and 3 are not primes
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    # If the number is divisible by 2*n, it's also divisible by 2.
    # Therefore, we skip 2*n.
    # Check starts from 5 (4 excluded):
    i = 5
    # And the step is 2 (6, 8, etc. excluded)
    d = 2
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += d
        # If the number is divisible by 3*n, it's also divisible by 3.
        # Therefore, we skip 3*n.
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
