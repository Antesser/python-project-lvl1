from random import randint
from typing import Tuple


QUESTION: str = 'What number is missing in the progression?'
AMOUNT_OF_NUMBERS_IN_PROGRESSION: int = 10
MIN_START_NUMBER: int = 1
MAX_START_NUMBER: int = 30
MIN_STEP: int = 1
MAX_STEP: int = 5


def game_round() -> Tuple[str, str]:
    progression_question, progression_answer = generating_answer_and_question()
    question: str = f'{" ".join(progression_question)}'
    answer = progression_answer
    return question, answer


def create_progression() -> list:
    start_number: int = randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step: int = randint(MIN_STEP, MAX_STEP)
    random_numbers = [start_number + step * i for i in
                      range(AMOUNT_OF_NUMBERS_IN_PROGRESSION)]
    return random_numbers


def generating_answer_and_question() -> Tuple[list, int]:
    progression_question = create_progression()
    random_index: int = randint(0, len(progression_question) - 1)
    progression_answer: int = progression_question[random_index]
    progression_question[random_index] = '..'
    return progression_question, str(progression_answer)
