from random import randint
import math

QUESTION: str = 'Find the greatest common divisor of given numbers.'


def main():
    first_number: int = randint(1, 100)
    second_number: int = randint(1, 100)
    question: str = f'{first_number} {second_number}'
    answer: str = common_division(first_number, second_number)
    return question, str(answer)


def common_division(first_number: int, second_number: int) -> int:
    return math.gcd(first_number, second_number)
