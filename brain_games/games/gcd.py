import random
import prompt
import math


def common_division():
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    number_of_attempts: int = 3
    for i in range(number_of_attempts):
        first_number: int = random.randint(1, 100)
        second_number: int = random.randint(1, 100)
        print(f'Question: {first_number} {second_number}')
        result: int = math.gcd(first_number, second_number)
        answer: int = prompt.string('Your answer: ')
        if int(answer) == result:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'. \n"
                  f"Let's try again, {name}!")
            break
    if int(answer) == result:
        print(f'Congratulations, {name}!')
