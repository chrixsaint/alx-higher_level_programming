#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    k = number * -1
    aii = k % 10
    print(f"Last digit of {number} is {aii * -1} and is less than 6 and not 0")
elif number == 0 or number > 0:
    aii = number % 10
    if aii > 5:
        print(f"Last digit of {number} is {aii} and is greater than 5")
    elif aii == 0:
        print(f"Last digit of {number} is {aii} and is 0")
    elif aii < 6 and not 0:
        print(f"Last digit of {number} is {aii} and is less than 6 and not 0")
