from random import randint, choice


QUESTION: str = 'What is the result of the expression?'


def game_round() -> tuple[str, str]:
    first_number: int = randint(1, 100)
    second_number: int = randint(1, 100)
    operation = ('*', '+', '-')
    operation = choice(operation)
    question: str = f'{first_number} {operation} {second_number}'
    answer: int = solution(first_number, second_number, operation)
    return question, str(answer)


def solution(first_number: int,
             second_number: int,
             operation: str,
             ) -> int:
    if operation == '+':
        return first_number + second_number
    elif operation == '*':
        return first_number * second_number
    else:
        return first_number - second_number
