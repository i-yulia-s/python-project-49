from brain_games.cli import welcome_user
from brain_games.engine import finish_game
from brain_games.games.calc import guess_calc


def main():
    name = welcome_user()
    finish_game(guess_calc(), name)


if __name__ == "__main__":
    main()