from random import randrange

from brain_games.engine import play_game


def is_prime(num):
    # 1 is not a prime
    # All numbers divisible by 2 and 3 are not primes
    if num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
    # 2 and 3 are primes
    if num == 2 or num == 3:
        return True
    # If the number is not even, it's also not divisible by 2*n.
    # If the number is not divisible by 3, it's also not divisible by 3*n.
    # Therefore, we exclude 2*n and 3*n from the check.
    # Check starts from 5:
    i = 5
    # The step is 2 (we skip evens, e.g. skip 6 and go to 7):
    d = 2
    # If num = a*b, then both a and b <= sqrt(num). No need to check further
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += d
        # We also skip numbers divisible by 3
        if i % 3 == 0:
            i += d
        # We could also skip 5s etc. but there's little gain in it.
        # 2s and 3s are a nice middle ground.
    return True


def guess_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    input = []
    for i in range(0, 3):
        question = randrange(1, 100)
        input.append((question, 'yes' if is_prime(question) else 'no'))
    return play_game(input)  
