from random import randint, choice
from typing import Tuple


QUESTION: str = 'What is the result of the expression?'
MIN_FIRST_NUMBER: int = 1
MAX_FIRST_NUMBER: int = 100
MIN_SECOND_NUMBER: int = 1
MAX_SECOND_NUMBER: int = 100


def game_round() -> Tuple[str, str]:
    first_number: int = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    second_number: int = randint(MIN_SECOND_NUMBER, MAX_SECOND_NUMBER)
    operator = ('*', '+', '-')
    operator = choice(operator)
    question: str = f'{first_number} {operator} {second_number}'
    answer: int = solution(first_number, second_number, operator)
    return question, str(answer)


def solution(first_number: int,
             second_number: int,
             operator: str,
             ) -> int:
    if operator == '+':
        return first_number + second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '-':
        return first_number - second_number
