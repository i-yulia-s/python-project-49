from random import randrange

from brain_games.engine import play_game


def guess_progression():
    print('What number is missing in the progression?')
    input = []
    for i in range(0, 3):
        progression = [randrange(1, 50)]
        difference = randrange(2, 10)
        for j in range(1, 10):
            progression.append(progression[j - 1] + difference)
        answer_index = randrange(0, 9)
        answer, progression[answer_index] = progression[answer_index], '..'
        input.append((' '.join(str(i) for i in progression), str(answer)))
    return play_game(input)
