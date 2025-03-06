import prompt


def play_game(input):
    for i in range(0, 3):
        question, expected_answer = input[i]
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer != expected_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'.")
            return False
        else:
            print('Correct!')
    return True


def finish_game(result, name):
    if result:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
