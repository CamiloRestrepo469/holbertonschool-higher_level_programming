#!/usr/bin/python3
import random

# Generate a random signed number
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Adjust the sign of the last digit if the number is negative
if number < 0:
    last_digit *= -1

# Determine the category of the last digit
if last_digit > 5:
    category = "and is greater than 5"
elif last_digit == 0:
    category = "and is 0"
else:
    category = "and is less than 6 and not 0"

# Print the result
output = f"Last digit of {number} is {last_digit} {category}"
print(output)

# import random
# number = random.randint(-10000, 10000)
# last = number % 10
# last_digit = abs(number) % 10
# if number < 0:
#     last_digit *= -1
#     print(f"Last digit of {number} is {last_digit}\
#  and is less than 6 and not 0 ")
# elif last > 5:
#     print(f"Last digit of {number} is {last} and is greater than 5")
# elif last == 0:
#     print(f"Last digit of {number} the string and is {last} ")
# elif last <= 6 and last != 0:
#     print(f"Last digit of {number} is {last} and is less than 6 and not 0 ")
# else:
#     print(f"Last digit of {number} ")
