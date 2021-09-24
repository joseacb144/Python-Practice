# random is needed to use random.sample()
import random

# function that prints a list of v_num random numbers from 1 to num
def random_numbers(num=1, l_num=1, v_num=1):
    for i in range(l_num):
        n = random.sample(range(1, num+1), v_num) #random.sample selects unique values (nonrepetitive)
        print(n)

def megaball(mega_num=1, l_num=1):
    for i in range(l_num):
        m = random.sample(range(1, mega_num+1), 1)
        print(m)

# --------- MAIN ---------
if __name__ == '__main__':
    number = int(input("How many numbers are in your range?\n")) # Ask user for the range of numbers
    list_num = int(input("How many lists of numbers do you need?\n")) # Ask user for the amount of list
    value_num = int(input("How many numbers do you need in each list?\n")) # Ask user how many numbers in each list

    mega_bool = input("Do you need megaball numbers? (YES/NO)\n").upper()
    if mega_bool == 'YES':
        mega_range = int(input("How many numbers are in your megaball range?\n"))

        print("These are your lottery numbers: ")
        random_numbers(number, list_num, value_num)
        print("These are your megaball numbers: ")
        megaball(mega_range, list_num)
        print("Good Luck!")
    else:
        # Run function
        print("These are your lottery numbers: ")
        random_numbers(number, list_num, value_num)
        print("Good Luck!")
