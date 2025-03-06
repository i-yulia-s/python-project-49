from random import randrange, choice
from brain_games.engine import play_game
from operator import add, sub, mul


def guess_calc():
    print('What is the result of the expression?')
    input = []
    operator_glossary = {"+":add,
               "-":sub,
               "*":mul}
    for i in range(0, 3):
        num1 = randrange(20)
        num2 = randrange(20)
        operator = choice(["+", "-", "*"])
        input.append((f'{str(num1)} {operator} {str(num2)}', str(operator_glossary[operator](num1, num2))))
    return play_game(input)
