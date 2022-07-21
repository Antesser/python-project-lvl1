from random import randint, choice


QUESTION: str = 'What is the result of the expression?'


def main():
    first_number: int = randint(1, 100)
    second_number: int = randint(1, 100)
    operation = choosing_operation(first_number, second_number)
    if operation == 'addition':
        question: str = f'{first_number} + {second_number}'
        answer: int = first_number + second_number
    elif operation == 'multiplication':
        question: str = f'{first_number} * {second_number}'
        answer: int + first_number * second_number
    else:
        question: str = f'{first_number} - {second_number}'
        answer: int = first_number - second_number
    return question, str(answer)


def choosing_operation(first_number: int, second_number: int) -> int:
    multiplication: int = first_number * second_number
    addition: int = first_number + second_number
    subtraction: int = first_number - second_number
    operations = (multiplication, addition, subtraction)
    operations = choice(operations)
    return operations
