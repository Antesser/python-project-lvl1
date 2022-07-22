from random import randint
import math

QUESTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def game_answer() -> tuple[str, str]:
    question: int = randint(1, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number: int) -> int:
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True
