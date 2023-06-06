#!/usr/bin/python3

def multiple_returns(sentence):
    long = len(sentence)
    one_carat = sentence[0] if long > 0 else None
    return long, one_carat
