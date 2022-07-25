from random import randint
import math

QUESTION: str = 'Find the greatest common divisor of given numbers.'


def game_round() -> tuple[str, str]:
    first_number: int = randint(1, 100)
    second_number: int = randint(1, 100)
    question: str = f'{first_number} {second_number}'
    answer: int = math.gcd(first_number, second_number)
    return question, str(answer)
