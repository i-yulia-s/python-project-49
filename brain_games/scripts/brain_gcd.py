from brain_games.cli import welcome_user
from brain_games.engine import finish_game
from brain_games.games.gcd import guess_gcd


def main():
    name = welcome_user()
    finish_game(guess_gcd(), name)


if __name__ == "__main__":
    main()
