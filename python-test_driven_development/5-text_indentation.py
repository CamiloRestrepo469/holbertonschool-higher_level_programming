#!/usr/bin/python3
"""_summary_
    """

def text_indentation(text):
    """_summary_

    Args:
        text (_type_): _description_

    Raises:
        TypeError: _description_
    """
    if not isinstance(text, str):
        """_summary_

        Args:
            text (_type_): _description_
            str (_type_): _description_

        Raises:
            TypeError: _description_
        """
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{}".format(i), '\n\n')
        print(i.strip(), end="")
