from operator import add, mul, sub
from random import choice, randrange

from brain_games.engine import play_game


def guess_calc():
    print('What is the result of the expression?')
    input = []
    op_glos = {"+": add,
               "-": sub,
               "*": mul}
    for i in range(0, 3):
        n1 = randrange(20)
        n2 = randrange(20)
        op = choice(["+", "-", "*"])
        input.append((f'{str(n1)} {op} {str(n2)}', str(op_glos[op](n1, n2))))
    return play_game(input)
