import random
import prompt


def calculate():
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    number_of_attempts: int = 3
    for i in range(number_of_attempts):
        first_number: int = random.randint(1, 100)
        second_number: int = random.randint(1, 100)

        multiplication: int = first_number * second_number
        addition: int = first_number + second_number
        subtraction: int = first_number - second_number

        operations = (multiplication, addition, subtraction)

        random.operations = random.choice(operations)
        if random.operations == addition:
            print(f'Question: {first_number} + {second_number}')
        elif random.operations == multiplication:
            print(f'Question: {first_number} * {second_number}')
        else:
            print(f'Question: {first_number} - {second_number}')
        answer: int = prompt.string('Your answer: ')
        if int(answer) == random.operations:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{random.operations}'. \n"
                  f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
