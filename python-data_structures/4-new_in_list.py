#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list) - 1:
        return my_list.copy()
    else:

        new_in_list = my_list.copy()
        new_in_list[idx] = element

    return new_in_list
