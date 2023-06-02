#!/usr/bin/python3

i = 0
while i <= 99:
    if i == 99:
        print("{}".format(i), end=''"\n")
    else:
        print("{:02d}".format(i), end=', ')
    i += 1
