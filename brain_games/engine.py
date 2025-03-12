import prompt


def play_game(input):
    for i in range(0, 3):
        task, answer = input[i]
        guess = prompt.string(f'Question: {task}\nYour answer: ')
        if guess == answer:
            print('Correct!')
            continue
        print(f"'{guess}' is wrong answer ;(. Correct answer was '{answer}'.")
        return False
    return True


def finish_game(result, name):
    if result:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
