from random import randint
from math import sqrt

QUESTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def game_round() -> tuple[str, str]:
    question: int = randint(1, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number: int) -> bool:
    prime_flag: int = 0
    if(number > 1):
        for i in range(2, int(sqrt(number)) + 1):
            if (number % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False
