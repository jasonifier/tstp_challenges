#!/usr/bin/env python3

def convert_to_float(num_string):
    """
    Returns the 'str' input as a 'float' data type. Else, indicates the data cannot be converted and return None.
    :param num_string: str.
    :return: float, None. Will return a 'float' if conversion is possible.
    """
    try:
        return float(num_string)
    except ValueError:
        print("Input string does not represent a valid rational number.")

print(convert_to_float('3.02'))
print(convert_to_float('100'))
print(convert_to_float('10a'))
