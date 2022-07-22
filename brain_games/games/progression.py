from random import randint
from typing import Tuple


QUESTION: str = 'What number is missing in the progression?'


def game_answer() -> Tuple[str, str]:
    progression = create_progression()
    initial_progression = progression.copy()
    random_index = hiding_number(progression)
    question: str = f'{" ".join(map(str, progression))}'
    answer = initial_progression[random_index]
    return question, str(answer)


def generate_end_number() -> Tuple[int, int, int]:
    start_number: int = randint(1, 30)
    step: int = randint(1, 5)
    end_number: int = start_number
    for i in range(10):
        end_number += step
    return end_number, start_number, step


def create_progression() -> list:
    end_number, start_number, step = generate_end_number()
    random_numbers = [i for i in range(start_number, end_number, step)]
    return random_numbers


def hiding_number(progression) -> int:
    random_index = randint(0, len(progression) - 1)
    progression[random_index] = '..'
    return random_index
