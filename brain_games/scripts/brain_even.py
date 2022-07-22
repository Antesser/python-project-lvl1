#!/usr/bin/env python
from brain_games.games import even
from brain_games.game_engine import start_game


def main():
    start_game(even)


if __name__ == '__main__':
    main()
