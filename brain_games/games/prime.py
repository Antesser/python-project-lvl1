from random import randint
from math import sqrt
from typing import Tuple

QUESTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no"'
MIN_QUESTION_NUMBER: int = 1
MAX_QUESTION_NUMBER: int = 100


def game_round() -> Tuple[str, str]:
    question: int = randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number: int) -> bool:
    prime_flag: int = 0
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        return True
    else:
        return False
