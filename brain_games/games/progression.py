from random import randint
from typing import Tuple


QUESTION: str = 'What number is missing in the progression?'
AMOUNT_OF_NUMBERS_IN_PROGRESSION: int = 10


def game_round() -> Tuple[str, str]:
    progression_question, progression_answer = generating_answer_and_question()
    question: str = f'{" ".join(map(str, progression_question))}'
    answer = progression_answer
    return question, str(answer)


def create_progression() -> list:
    start_number: int = randint(1, 30)
    step: int = randint(1, 5)
    random_numbers = [start_number + step * i for i in
                      range(AMOUNT_OF_NUMBERS_IN_PROGRESSION)]
    return random_numbers


def generating_answer_and_question() -> Tuple[list, int]:
    progression_question = create_progression()
    random_index: int = randint(0, len(progression_question) - 1)
    progression_answer: int = progression_question[random_index]
    progression_question[random_index] = '..'
    return progression_question, progression_answer
