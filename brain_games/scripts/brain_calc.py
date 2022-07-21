#!/usr/bin/env python
from brain_games.games import calc
from brain_games.game_engine import start_engine


def main():
    start_engine(calc)


if __name__ == '__main__':
    main()
