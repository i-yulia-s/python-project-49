from random import randrange
import prompt


def guess_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        question = randrange(20)
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if question % 2 == 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break            
        elif question % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        print('Correct!')
        i += 1
        if i == 3:
            print(f'Congratulations, {name}!')
