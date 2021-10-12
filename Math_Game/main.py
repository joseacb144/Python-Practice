import random
from time import time
import os

random.seed()


def number():
    return random.randint(0, 10)


def symbol():
    return random.choice(['+', '-'])


def symbol_pro():
    return random.choice(['+', '-', '*'])


def _symbol():
    return random.choice(["", "-"])


def game(difficulty):
    question_count = 1
    score = 0
    game_time = 10
    while question_count <= 10:
        if difficulty == 1:
            math_question = f'{number()} {symbol()} {number()}'
        else:
            math_question = f'{_symbol()} {number()} {symbol_pro()} {number()} {symbol_pro()} {number()}'
            initial_time = time()
        math_answer = eval(math_question)
        print(f'Question {question_count}: {math_question}')

        player_answer = int(input("What is the answer? "))
        time_taken = (time() - initial_time)
        intime = time_taken < game_time
        if intime:
            if player_answer == math_answer:
                print(f"Correct! The answer is: {math_answer} \n")
                score += 1
                question_count += 1
                print(game_time-time_taken)
            else:
                print(f"That is incorrect. The answer is: {math_answer}.\n")
                question_count += 1
                print(game_time - time_taken)
        else:
            print("Out of time!")
            break

    print(f'Your total score is: {score}.')


if __name__ == '__main__':
    print('Hello, you get 10 questions to answer!\n')
    player_decision = int(input("Select 1 for beginner or select 2 for pro.\n"))

    game(player_decision)

    os.system('pause')
