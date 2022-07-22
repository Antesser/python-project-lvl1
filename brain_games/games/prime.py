from random import randint

QUESTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def game_answer() -> tuple[str, str]:
    question: int = randint(1, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number: int) -> int:
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    return divider * divider > number
