from brain_games.cli import welcome_user
from brain_games.even import guess_even


def main():
    name = welcome_user()
    guess_even(name)


if __name__ == "__main__":
    main()
