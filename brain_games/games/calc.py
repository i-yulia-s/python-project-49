from operator import add, mul, sub
from random import choice, randrange
from brain_games.engine import play_game


def get_random_operation(n1, n2):
    op_map = {"+": add,
        "-": sub,
        "*": mul}
    operator = choice(["+", "-", "*"])
    return (f'{str(n1)} {operator} {str(n2)}', str(op_map[operator](n1, n2)))


def guess_calc():
    print('What is the result of the expression?')
    input = []
    for i in range(0, 3):
        n1 = randrange(20)
        n2 = randrange(20)
        input.append(get_random_operation(n1, n2))
    return play_game(input)
