#!/usr/bin/python3
"""_summary_
    """


def text_indentation(text):
    """if text is not None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    

    punctuation_marks = ['.', '?', ':']
    for delim in punctuation_marks:
        text = delim.join([line.strip(" ") for line in text.split(delim)])
        text = text.replace(delim, delim + "\n\n")

    print(text, end="")
