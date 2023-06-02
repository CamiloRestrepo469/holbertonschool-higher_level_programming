#!/usr/bin/python3

i = 0
while i <= 99:
    if i == 99:
        print("{:d}".format(i), end='')
    else:
        print("{:d}".format(i), end=', ')
    i += 1
