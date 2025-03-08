import prompt


def play_game(input):
    for i in range(0, 3):
        que, exp_a = input[i]
        ans = prompt.string(f'Question: {que}\nYour answer: ')
        if ans != exp_a:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{exp_a}'.")
            return False
        else:
            print('Correct!')
    return True


def finish_game(result, name):
    if result:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
