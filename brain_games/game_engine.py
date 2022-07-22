import prompt


def start_game(game) -> None:
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.QUESTION}')
    number_of_attempts: int = 3
    for i in range(number_of_attempts):
        question, answer = game.game_answer()  # самое сложное для понимания
        print(f'Question: {question}')
        user_answer: str = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. \n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
