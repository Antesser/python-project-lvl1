from random import randint
import math

QUESTION: str = 'Find the greatest common divisor of given numbers.'
MIN_FIRST_NUMBER: int = 1
MAX_FIRST_NUMBER: int = 100
MIN_SECOND_NUMBER: int = 1
MAX_SECOND_NUMBER: int = 100


def game_round() -> tuple[str, str]:
    first_number: int = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    second_number: int = randint(MIN_SECOND_NUMBER, MAX_SECOND_NUMBER)
    question: str = f'{first_number} {second_number}'
    answer: int = math.gcd(first_number, second_number)
    return question, str(answer)
