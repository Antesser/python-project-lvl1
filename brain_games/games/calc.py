from random import randint, choice


QUESTION: str = 'What is the result of the expression?'


def main() -> str:
    first_number: int = randint(1, 100)
    second_number: int = randint(1, 100)
    operation = ('*', '+', '-')
    operation = choice(operation)
    question: str = f'{first_number} {operation} {second_number}'
    answer = choosing_operation(first_number, second_number, operation)
    return question, str(answer)


def choosing_operation(first_number: int, second_number: int,
                       operation: str) -> int:
    multiplication = first_number * second_number
    addition = first_number + second_number
    subtraction = first_number - second_number
    if operation == '+':
        answer: int = addition
    elif operation == '*':
        answer: int = multiplication
    else:
        answer: int = subtraction
    return answer
