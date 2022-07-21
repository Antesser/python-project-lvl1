from random import randint

QUESTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def main() -> str:
    question: int = randint(1, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number: int) -> int:
    divider: int = 2
    while number % divider != 0:
        divider += 1
    return divider == number
