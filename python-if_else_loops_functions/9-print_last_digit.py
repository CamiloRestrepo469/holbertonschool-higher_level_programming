#!/usr/bin/python3
def print_last_digit(number):
    result = int(repr(number)[-1])
    print(result, end='')
    return result

# def print_last_digit(number):
#     if number < 0:
#         number *= -1
#     print(number % 10, end='')
