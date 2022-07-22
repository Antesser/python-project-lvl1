from random import randint


QUESTION: str = 'What number is missing in the progression?'
START_NUMBER: int = randint(1, 30)
STEP: int = randint(1, 5)
END_NUMBER: int = randint(40, 50)


def game_answer() -> tuple[str, str]:
    number_in_question = create_progression().copy()
    random_index = randint(0, len(create_progression()) - 1)
    number_in_question[random_index] = '..'
    question: str = f'{" ".join(map(str, number_in_question))}'
    answer = create_progression()[random_index]
    return question, str(answer)


def create_progression() -> list:
    random_numbers = [i for i in range(START_NUMBER, 100, STEP)]
    return random_numbers
