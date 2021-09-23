# random is needed to use random.sample()
import random

# function that prints an list of 5 random numbers from 1 to 70
def random_numbers(num, a_num=1, v_num=1):
    for i in range(a_num):
        n = random.sample(range(1, num+1), v_num) #random.sample selects unique values (nonrepetitive)
        print(n)

# main
if __name__ == '__main__':
    number = int(input("How many numbers are in your range?\n")) # Ask user for the range of numbers
    array_num = int(input("How many lists of numbers do you need?\n"))
    value_num = int(input("How many numbers do you need in each list?\n"))
    random_numbers(number, array_num, value_num)
