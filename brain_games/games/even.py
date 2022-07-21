from random import randint


QUESTION: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def main() -> str:
    question: int = randint(1, 100)
    answer: str = ''
    if odd_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def odd_even(question) -> bool:
    return question % 2 == 0
