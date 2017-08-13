#!/usr/bin/env python3

def print_string(s):
    """
    Prints a string input. Else prints 'Not a string.'
    :param s: str.
    :return: None.
    """
    if type(s) == str:
        print(s)
    else:
        print("Not a string.")

print_string("New York")
print_string("Chicago")
print_string(25)
