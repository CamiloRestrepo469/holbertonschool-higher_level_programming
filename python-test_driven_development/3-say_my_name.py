#!/usr/bin/python3
"""create functions"""


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (_type_): call name
        last_name (str, optional): call last_name. Defaults to "".
    """
    if not isinstance(first_name, str):
        """_summary_

        Args:
            str (_type_): isinstance(first_name, str)

        Raises:
            TypeError: first_name must be a string
        """
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        """_summary_

        Args:
            str (_type_): isinstance(last_name,)

        Raises:
            TypeError:last_name must be a string
        """
        raise TypeError('last_name must be a string')
    if first_name:
        """print first_name and last_name
        """
        print("My name is {} {}".format(first_name, last_name))
    else:
        """print Errored first_name and last_name
        """
        print("{}".format(last_name))
