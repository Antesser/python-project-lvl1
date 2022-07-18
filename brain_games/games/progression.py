import random
import prompt


def missing_number():
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    number_of_attempts: int = 3
    for i in range(number_of_attempts):
        random_numbers = []
        starting_number: int = random.randint(1, 50)
        step: int = random.randint(1, 5)
        for i in range(starting_number, 100, step):
            random_numbers.append(i)
        random_index: int = random.randint(0, len(random_numbers[:10]) - 1)
        question: int = random_numbers.copy()
        question[random_index] = ".."
        print(f'Question: {question[:10]}')
        answer: int = prompt.string('Your answer: ')
        if int(answer) == random_numbers[random_index]:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  "Correct answer was "
                  f"'{random_numbers[random_index]}'. \n"
                  f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')