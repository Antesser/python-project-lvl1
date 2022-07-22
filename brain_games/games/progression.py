from random import randint


QUESTION: str = 'What number is missing in the progression?'


def game_answer():
    number_in_question, random_index, answer_in_question = hiding_number()
    question: str = f'{" ".join(map(str, number_in_question))}'
    answer = answer_in_question[random_index]
    return question, str(answer)


def generate_end_number() -> int:
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


def hiding_number():
    number_in_question = create_progression().copy()
    answer_in_question = number_in_question.copy()
    random_index = randint(0, len(number_in_question) - 1)
    number_in_question[random_index] = '..'
    return number_in_question, random_index, answer_in_question
