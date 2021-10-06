import random

def number():
    return (random.randint(0,10))

def symbol():
    return random.choice(['+','-','*'])


if __name__ == '__main__':
    a = str(number())
    b = str(number())
    c = symbol()
    e = a + c + b
    print(a, c, b)

    player_answer = int(input("What is the answer? "))
    if player_answer == eval(e):
        print("correct\n")
    else:
        print("incorrect\n")

    print(eval(e))