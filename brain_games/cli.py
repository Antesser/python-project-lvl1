import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
