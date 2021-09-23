# random is needed to use random.sample()
import random

# function that prints an list of 5 random numbers from 1 to 70
def random_numbers():
    n = random.sample(range(1, 71), 5) #random.sample selects unique values (nonrepetitive)
    print(n)

# main
if __name__ == '__main__':
    random_numbers()
