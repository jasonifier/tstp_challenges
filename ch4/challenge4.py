#!/usr/bin/env python3

def divide_by_2(x):
    """
    Returns integer part after dividing a number by 2, i.e. floored quotient.
    :param x: int.
    :return: int floored quotient after dividing by 2.
    """
    if type(x) == int:
        return x // 2

def multiply_by_4(x):
    """
    Returns the result of multiplying an integer by 4.
    :param x: int.
    :return: int product of input and 4 i.e. multiply the input by 4.
    """
    if type(x) == int:
        return x * 4

a = divide_by_2(30)
b = multiply_by_4(a)
print(b) #60
