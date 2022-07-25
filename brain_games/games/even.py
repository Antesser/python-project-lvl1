from random import randint
from typing import Tuple


QUESTION: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_round() -> Tuple[str, str]:
    question: int = randint(1, 100)
    answer: str
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_even(number) -> bool:
    return number % 2 == 0
