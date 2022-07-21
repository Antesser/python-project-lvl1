from random import randint


QUESTION: str = 'What number is missing in the progression?'


def main():
    random_index, random_numbers, progr_length = create_random()
    numbers_in_question = random_numbers.copy()
    numbers_in_question[random_index] = '..'
    question: str = f'{" ".join(map(str, numbers_in_question[:progr_length]))}'
    answer = random_numbers[random_index]
    return question, str(answer)


def create_random():
    random_numbers = []
    progr_length: int = 10
    starting_number: int = randint(1, 50)
    step: int = randint(1, 5)
    for i in range(starting_number, 100, step):
        random_numbers.append(i)
    random_index = randint(0, len(random_numbers
                                  [:progr_length]) - 1)
    return random_index, random_numbers, progr_length
