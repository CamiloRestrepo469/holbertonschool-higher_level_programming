#!/usr/bin/python3
from caculadora_1 import add
from caculadora_1 import sub
from caculadora_1 import mul
from caculadora_1 import div
a = 10
b = 5

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
