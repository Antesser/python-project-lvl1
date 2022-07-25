from random import randint

QUESTION: str = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def game_round() -> tuple[str, str]:
    question: int = randint(1, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def is_prime(number: int) -> int:
    if number > 1:
        for i in range(2, number // 2):
            if (number % i) == 0:
                return False
            break
        else:
            return True
    else:
        return False
