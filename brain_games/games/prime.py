import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    number_of_attempts: int = 3
    for i in range(number_of_attempts):
        number: int = random.randint(2, 100)
        print(f'Question: {number}')
        answer: int = prompt.string('Your answer: ')
        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
            if str(answer.lower()) == correct_answer:
                print('Correct')
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'. \n"
                      f"Let's try again, {name}!")
                break
    print(f'Congratulations, {name}!')


def is_prime(number):
    divider: int = 2
    while number % divider != 0:
        divider += 1
    return divider == number
