from random import randint


QUESTION: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_round() -> tuple[str, str]:
    question: int = randint(1, 100)
    answer: str
    if if_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer


def if_even(question) -> bool:
    return question % 2 == 0
