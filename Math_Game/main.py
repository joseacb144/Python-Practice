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

def print_dash(i):
    print('-' * i)

def game(difficulty):
    question_count = 1
    score = 0
    game_time = 10  # Used for PRO. PRO gives players 10 seconds to answer

    while question_count <= 10:
        if difficulty == 1:  # BEGINNER
            math_question = f'{number()} {symbol()} {number()}'
        elif difficulty == 2:  # PRO
            math_question = f'{_symbol()} {number()} {symbol_pro()} {number()} {symbol_pro()} {number()}'
            initial_time = time()  # Used to grab the initial time after the question is given in PRO.
        math_answer = eval(math_question)
        print(f'Question {question_count}: {math_question}')
        print_dash(25)

        if difficulty == 1:
            player_answer = int(input("What is the answer? "))
            if player_answer == math_answer:
                print(f"Correct! The answer is: {math_answer} \n")
                score += 1
                question_count += 1
            else:
                print(f"That is incorrect. The answer is: {math_answer}.\n")
                question_count += 1

        elif difficulty == 2:
            player_answer = int(input("What is the answer? "))
            time_taken = int(time() - initial_time)  # Used to identify how many seconds the player used to answer in PRO.
            intime = time_taken < game_time  # Checks to see if the player answered in time in PRO.
            if intime:
                if player_answer == math_answer:
                    score += int(game_time - time_taken) # 10 seconds - the amount of seconds taken to answer (to see how much time was left)
                    print(f"Correct! The answer is: {math_answer} ")
                    print(f"Time elapsed: {int(time_taken)}\n")
                    question_count += 1
                else:
                    print(f"That is incorrect. The answer is: {math_answer}.\n")
                    question_count += 1
            else:
                print("Out of time!")
                break

    print(f'\nYour total score is: {score}.')


if __name__ == '__main__':

    print_dash(59)
    print('| Hello and welcome to the Basic Math Game by Jose Chavez |')
    print_dash(59)
    print('* INFO: \n- BEGINNER is basic addition and subtraction. '
          '\n- You are given 1 point for each correct answer for a total of 10 questions.'
          
          '\n\n- PRO has addition, subtraction, and multiplication.'
          '\n- You have 10 seconds to answer each question in PRO.'
          '\n- Your score in PRO depends on how many seconds remain for each question.'
          '\n- If you run out of time in PRO, the game ends.\n')

    player_decision = int(input("Select 1 for BEGINNER or select 2 for PRO.\n"))

    game(player_decision)

    os.system('pause')
