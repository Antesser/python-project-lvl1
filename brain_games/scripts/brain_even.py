#!/usr/bin/env python
from brain_games.games import even
from brain_games.game_engine import start_engine


def main():
    start_engine(even)


if __name__ == '__main__':
    main()
