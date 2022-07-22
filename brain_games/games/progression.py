from random import randint


QUESTION: str = 'What number is missing in the progression?'
STEP: int = randint(1, 5)
END_NUMBER: int = randint(40, 50)


def game_answer() -> tuple[str, str]:
    start_number: int = randint(1, 30)
    number_in_question = create_progression(start_number).copy()
    random_index = randint(0, len(create_progression(start_number)) - 1)
    number_in_question[random_index] = '..'
    question: str = f'{" ".join(map(str, number_in_question))}'
    answer = create_progression(start_number)[random_index]
    return question, str(answer)


def create_progression(start_number) -> list:
    random_numbers = [i for i in range(start_number, 100, STEP)]
    return random_numbers
