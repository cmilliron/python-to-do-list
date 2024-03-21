import random

def random_number(lower_boundary, upper_boundary):
    return random.randint(lower_boundary, upper_boundary)

lower = int(input('Enter the lower bound: '))
upper = int(input("Enter the upper bound: "))


print(f"Your random number is: {random_number(lower,upper)}")