from random import randrange

from brain_games.engine import play_game


def create_random_progression():
    progression = [randrange(1, 50)]
    difference = randrange(2, 10)
    for j in range(1, 10):
        progression.append(progression[j - 1] + difference)
    return progression


def get_number_and_replace_by_dots(progression, index):
    answer, progression[index] = progression[index], '..'
    return answer


def guess_progression():
    print('What number is missing in the progression?')
    input = []
    for i in range(0, 3):
        question = create_random_progression()
        answer = get_number_and_replace_by_dots(question, randrange(0, 9))    
        input.append((' '.join(str(j) for j in question), str(answer)))
    return play_game(input)
