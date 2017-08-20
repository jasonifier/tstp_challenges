#!/usr/bin/env python3

numbers = [1,4,5,7,11,15,19,20,21]

while True:
    input_val = input("Guess a number (type q to quit): ")
    if input_val == 'q':
        break
    guess = int(input_val)
    if guess in numbers:
        print('Correct! ' + input_val + ' is in the list of numbers.')
    else:
        print('Sorry! That number is not in the list. Try again')     
