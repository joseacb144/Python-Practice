import random
import os

def number():
    return (random.randint(0,10))

def symbol():
    return random.choice(['+','-'])

def symbol_pro():
    return random.choice(['+','-','*'])

def _symbol():
    return random.choice(["", "-"])

def beginner_game():
    question_count = 1
    score = 0
    while question_count <= 10:
        a = str(number())
        b = str(number())
        c = symbol()
        d = a + c + b
        e = eval(d)
        print(f'Question {question_count}: {a} {c} {b}')

        player_answer = int(input("What is the answer? "))
        if player_answer == e:
            print(f"Correct! The answer is: {e} \n")
            score += 1
            question_count += 1
        else:
            print(f"Incorrect!\n")
            question_count += 1

    print(f'Your total score is: {score}.')

def pro_game():
    question_count = 1
    score = 0
    while question_count <= 10:
        a = str(number())
        b = str(number())
        i = str(number())
        c = symbol_pro()
        j = symbol_pro()
        z = _symbol()
        d = z + a + c + b + j + i
        e = eval(d)
        print(f'Question {question_count}: {z} {a} {c} {b} {j} {i}')

        player_answer = int(input("What is the answer? "))
        if player_answer == e:
            print(f"Correct! The answer is: {e} \n")
            score += 1
            question_count += 1
        else:
            print(f"Incorrect!\n")
            question_count += 1

    print(f'Your total score is: {score}.')

if __name__ == '__main__':

    print('Hello, you get 10 questions to answer!\n')
    player_decision = int(input("Select 1 for beginner or select 2 for pro.\n"))

    if player_decision == 1:
        beginner_game()
    elif player_decision == 2:
        pro_game()

    os.system('pause')