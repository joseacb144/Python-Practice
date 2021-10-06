import random
import os

def number():
    return (random.randint(0,10))

def symbol():
    return random.choice(['+','-','*'])


if __name__ == '__main__':

    print('Hello, you get 10 questions to answer!\n')

    question_count = 1
    score = 0

    while question_count <= 10:
        a = str(number())
        b = str(number())
        c = symbol()
        d = a + c + b
        e =eval(d)
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
    os.system('pause')