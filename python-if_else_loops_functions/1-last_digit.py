#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
    print(f"Last digit of {number} is {last_digit}\
 and is less than 6 and not 0 ")
elif last > 5:
    print(f"Last digit of {number} is {last} he string and is greater than 5 ")
elif last == 0:
    print(f"Last digit of {number} the string and is {last} ")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0 ")
else:
    print(f"Last digit of {number} ")
