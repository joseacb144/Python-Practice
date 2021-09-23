# random is needed to use random.sample()
import random

# function that prints an list of 5 random numbers from 1 to 70
def random_numbers(num):
    n = random.sample(range(1, num), 5) #random.sample selects unique values (nonrepetitive)
    print(n)

# main
if __name__ == '__main__':
    number = int(input("How many numbers are in your range?")) # Ask user for the range of numbers
    random_numbers(number)
