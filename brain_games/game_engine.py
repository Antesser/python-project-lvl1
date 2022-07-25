import prompt


NUMBER_OF_ATTEMPTS: int = 3


def start_game(game) -> None:
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.QUESTION}')
    for _ in range(NUMBER_OF_ATTEMPTS):
        question, correct_answer = game.game_round()
        print(f'Question: {question}')
        user_answer: str = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. \n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
