#!/usr/bin/env python3

val1 = input("Enter a number: ")
val2 = input("Enter another number: ")

result = int(val1) // int(val2)

answer = "{0} divided by {1} produces a quotient of {2}".format(val1, val2, str(result))
print(answer)
