from random import randint
import prompt


def odd_even():
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_attempts: int = 3
    for i in range(number_of_attempts):
        range_of_numbers = randint(1, 100)
        print(f'Question: {range_of_numbers}')
        answer = prompt.string('Your answer: ')
        if range_of_numbers % 2 == 0:
            if answer.lower() == 'yes':
                print('Correct')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'yes'. \n"
                      f"Let's try again, {name}!")
                break
        if range_of_numbers % 2 != 0:
            if answer.lower() == 'no':
                print('Correct')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      "Correct answer was 'no'. \n"
                      f"Let's try again, {name}!")
                break
        print(f'Congratulations, {name}!')
