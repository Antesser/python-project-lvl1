#!/usr/bin/env python
import prompt
from random import randint


def main():
    i = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        x = randint(1, 100)
        print(f'Question: {x}')
        answer = prompt.string('Your answer: ')
        if x % 2 == 0:
            if answer.lower() == 'yes':
                print('Correct')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'yes'. \n"
                      f"Let's try again, {name}")
                break
        if x % 2 != 0:
            if answer.lower() == 'no':
                print('Correct')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'no'. \n"
                      f"Let's try again, {name}")
                break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
